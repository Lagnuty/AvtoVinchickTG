from __future__ import annotations

import asyncio
from collections.abc import Callable
from dataclasses import dataclass
import threading
import traceback

from avto_vinchick_tg.bot_api import BotApi
from avto_vinchick_tg.dv_bot import DvMessageKind, classify_dv_message, command_for_accepted
from avto_vinchick_tg.filters import evaluate_profile
from avto_vinchick_tg.settings import AppConfig, SESSION_PATH
from tg_api_zapret import FileSessionBackend, TelegramConfig, TelegramLayer


LogCallback = Callable[[str], None]


@dataclass(frozen=True)
class LoginState:
    phone: str
    phone_code_hash: str


class VinchikRunner:
    def __init__(self, log: LogCallback) -> None:
        self.log = log
        self._loop: asyncio.AbstractEventLoop | None = None
        self._thread: threading.Thread | None = None
        self._stop_event: asyncio.Event | None = None
        self._layer: TelegramLayer | None = None
        self._login_state: LoginState | None = None

    @property
    def running(self) -> bool:
        return self._thread is not None and self._thread.is_alive()

    def login_send_code(self, config: AppConfig) -> None:
        self.log("Telegram: фоновая отправка кода запущена.")
        self._run_sync(self._login_send_code(config))

    def login_submit_code(self, code: str) -> None:
        self.log("Telegram: фоновая проверка кода запущена.")
        self._run_sync(self._login_submit_code(code))

    def login_submit_password(self, password: str) -> None:
        self.log("Telegram: фоновая проверка 2FA запущена.")
        self._run_sync(self._login_submit_password(password))

    def start(self, config: AppConfig) -> None:
        if self.running:
            self.log("Уже запущено.")
            return
        self._thread = threading.Thread(target=self._thread_main, args=(config,), daemon=True)
        self._thread.start()

    def stop(self) -> None:
        if self._loop and self._stop_event:
            self._loop.call_soon_threadsafe(self._stop_event.set)

    def _thread_main(self, config: AppConfig) -> None:
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        try:
            self._loop.run_until_complete(self._run(config))
        except Exception:
            self.log(traceback.format_exc())
        finally:
            self._loop.close()
            self._loop = None
            self._stop_event = None
            self._thread = None

    async def _run(self, config: AppConfig) -> None:
        self._stop_event = asyncio.Event()
        layer = make_layer(config)
        bot = BotApi(config.bot_token, proxy_url=config.proxy_url)
        async with layer.lifespan():
            if not await layer.is_authorized():
                self.log("Telegram аккаунт не авторизован. Сначала войдите.")
                return
            self._layer = layer
            bot.get_me()
            self.log(f"Слушаю чат: {config.source_chat}")
            client = await layer.authorized_client()

            @client.on(events_new_message(config.source_chat))
            async def handler(event):
                message = event.message
                text = message.message or ""
                kind = classify_dv_message(text)

                if kind == DvMessageKind.AD and config.dv_actions.ignore_ads:
                    self.log("ДВ: реклама или premium-сообщение пропущены.")
                    return
                if kind == DvMessageKind.FOUND_PROMPT and config.dv_actions.auto_open_found:
                    await send_dv_command(client, config.source_chat, "1")
                    self.log("ДВ: найден список анкет, отправил 1 для показа.")
                    return
                if kind in {DvMessageKind.LIKE_NOTICE, DvMessageKind.MATCH_NOTICE}:
                    if config.dv_actions.forward_likes:
                        await asyncio.to_thread(
                            bot.send_message,
                            config.notify_chat_id,
                            format_service_message(text, kind),
                        )
                        self.log("ДВ: уведомление о лайке/симпатии отправлено в вашего бота.")
                    return
                if kind != DvMessageKind.PROFILE:
                    self.log(f"ДВ: системное сообщение пропущено ({kind.value}).")
                    return

                result = evaluate_profile(text, config.filters, has_media=bool(message.media))
                if result.accepted:
                    await asyncio.to_thread(
                        bot.send_message,
                        config.notify_chat_id,
                        format_profile_message(text, result),
                    )
                    command = command_for_accepted(config.dv_actions.accepted_action)
                    if command:
                        await send_dv_command(client, config.source_chat, command)
                        self.log(f"ДВ: анкета принята, отправлена команда {command}.")
                    else:
                        self.log(f"Принято: {result.word_count} слов, возраст {result.age or 'не найден'}")
                elif config.send_rejects_to_log:
                    self.log("Отсеяно: " + "; ".join(result.reasons[:4]))
                if not result.accepted and config.dv_actions.auto_skip_rejected:
                    await send_dv_command(client, config.source_chat, "3")
                    self.log("ДВ: анкета не прошла фильтры, отправлена команда 3.")

            while not self._stop_event.is_set():
                await asyncio.sleep(0.2)
            self.log("Остановлено.")

    async def _login_send_code(self, config: AppConfig) -> None:
        self.log("Telegram: подключаюсь через указанный прокси.")
        layer = make_layer(config)
        await layer.connect()
        self._layer = layer
        self.log("Telegram: соединение установлено, проверяю доступность API.")
        health = await layer.check_connection_result()
        if not health.ok:
            self.log(f"Telegram соединение не прошло проверку: {health.error_type}: {health.message}")
            return
        self.log("Telegram: запрашиваю код у Telegram.")
        result = await layer.send_code_result(config.phone)
        if not result.ok or not result.sent_code:
            self.log(f"Код не отправлен: {result.error_type or result.status}: {result.message or ''}")
            return
        self._login_state = LoginState(result.sent_code.phone, result.sent_code.phone_code_hash)
        self.log("Код отправлен в Telegram.")

    async def _login_submit_code(self, code: str) -> None:
        if not self._layer or not self._login_state:
            raise RuntimeError("Сначала запросите код.")
        result = await self._layer.sign_in_result(self._login_state, code.strip())
        if result.ok:
            await self._layer.disconnect()
            self.log("Вход выполнен.")
        elif result.password_required:
            self.log("Нужен 2FA пароль.")
        else:
            self.log(f"Вход по коду не выполнен: {result.error_type or result.status}: {result.message or ''}")

    async def _login_submit_password(self, password: str) -> None:
        if not self._layer:
            raise RuntimeError("Сначала введите код.")
        result = await self._layer.sign_in_password_result(password)
        if result.ok:
            await self._layer.disconnect()
            self.log("Вход выполнен с 2FA.")
        else:
            self.log(f"Вход с 2FA не выполнен: {result.error_type or result.status}: {result.message or ''}")

    def _run_sync(self, coro) -> None:
        def worker() -> None:
            try:
                asyncio.run(coro)
            except Exception:
                self.log(traceback.format_exc())

        threading.Thread(target=worker, daemon=True).start()


def make_layer(config: AppConfig) -> TelegramLayer:
    tg_config = TelegramConfig.from_env(proxy_url=config.proxy_url or None)
    return TelegramLayer(tg_config, FileSessionBackend(SESSION_PATH))


def events_new_message(source_chat: str):
    from telethon import events

    chat = source_chat.strip()
    if chat.startswith("@"):
        chat = chat[1:]
    return events.NewMessage(chats=chat or None)


async def send_dv_command(client, source_chat: str, command: str) -> None:
    chat = source_chat.strip()
    if chat.startswith("@"):
        chat = chat[1:]
    await client.send_message(chat, command)


def format_profile_message(text: str, result) -> str:
    header = "Анкета прошла фильтры"
    meta = f"Возраст: {result.age or 'не найден'} | слов: {result.word_count} | символов: {result.char_count}"
    return f"{header}\n{meta}\n\n{text}".strip()


def format_service_message(text: str, kind: DvMessageKind) -> str:
    title = "ДВ: лайк/интерес" if kind == DvMessageKind.LIKE_NOTICE else "ДВ: взаимная симпатия"
    return f"{title}\n\n{text}".strip()

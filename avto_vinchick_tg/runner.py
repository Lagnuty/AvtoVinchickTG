from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from pathlib import Path
import tempfile
import threading
import traceback

from avto_vinchick_tg.bot_api import BotApi, proxy_socket_lock
from avto_vinchick_tg.dv_bot import DvMessageKind, classify_dv_message, command_for_accepted
from avto_vinchick_tg.filters import evaluate_profile
from avto_vinchick_tg.settings import AppConfig, SESSION_PATH
from avto_vinchick_tg.taste_model import TasteModel
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
        self._login_loop: asyncio.AbstractEventLoop | None = None
        self._login_thread: threading.Thread | None = None
        self._login_ready = threading.Event()
        self._login_lock = threading.Lock()
        self._login_layer: TelegramLayer | None = None
        self._login_state: LoginState | None = None
        self._taste_model = TasteModel()
        self._pending_profile_text: str | None = None

    @property
    def running(self) -> bool:
        return self._thread is not None and self._thread.is_alive()

    def login_send_code(self, config: AppConfig) -> None:
        self.log("Telegram: фоновая отправка кода запущена.")
        self._run_login(lambda: self._login_send_code(config))

    def login_submit_code(self, code: str) -> None:
        self.log("Telegram: фоновая проверка кода запущена.")
        self._run_login(lambda: self._login_submit_code(code))

    def login_submit_password(self, password: str) -> None:
        self.log("Telegram: фоновая проверка 2FA запущена.")
        self._run_login(lambda: self._login_submit_password(password))

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
        with proxy_socket_lock:
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
            bot_poll_task = asyncio.create_task(self._poll_bot_commands(bot, client, config))

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
                    if config.taste.enabled:
                        prediction = self._taste_model.predict(text, min_samples=config.taste.min_samples)
                        if prediction.trained and prediction.score < config.taste.min_score:
                            self.log(
                                f"ML: анкета отсеяна по описанию, score {prediction.score}/100 "
                                f"< {config.taste.min_score}/100."
                            )
                            if config.dv_actions.auto_skip_rejected:
                                await send_dv_command(client, config.source_chat, "3")
                            return
                        if prediction.trained:
                            self.log(f"ML: анкета прошла по описанию, score {prediction.score}/100.")
                        else:
                            self.log(
                                f"ML: мало обучающих оценок "
                                f"({prediction.total_samples}/{config.taste.min_samples}), анкета пропущена к вам."
                            )
                    await notify_profile(bot, client, config, message, format_profile_message(text, result))
                    self._pending_profile_text = text
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
            bot_poll_task.cancel()
            self.log("Остановлено.")

    async def _poll_bot_commands(self, bot: BotApi, client, config: AppConfig) -> None:
        offset = await asyncio.to_thread(initial_bot_update_offset, bot)
        commands = {
            "1": "лайк",
            "2": "лайк с посланием",
            "3": "не понравилась внешность",
            "4": "не понравилось описание",
        }
        while not self._stop_event or not self._stop_event.is_set():
            try:
                updates = await asyncio.to_thread(bot.get_updates, offset=offset, timeout=10)
                for update in updates.get("result") or []:
                    update_id = update.get("update_id")
                    if isinstance(update_id, int):
                        offset = update_id + 1
                    message = update.get("message") or update.get("edited_message") or {}
                    chat_id = str((message.get("chat") or {}).get("id") or "")
                    text = str(message.get("text") or "").strip()
                    if chat_id != str(config.notify_chat_id).strip() or text not in commands:
                        continue
                    dv_command = "3" if text == "4" else text
                    await send_dv_command(client, config.source_chat, dv_command)
                    if self._pending_profile_text and text in {"1", "2", "4"}:
                        learned = await asyncio.to_thread(self._taste_model.learn, self._pending_profile_text, text)
                        if learned:
                            if text == "4":
                                self.log("ML: дообучил вкус отрицательным примером по описанию.")
                            else:
                                self.log("ML: дообучил вкус положительным примером.")
                        self._pending_profile_text = None
                    elif text == "3":
                        self._pending_profile_text = None
                    await asyncio.to_thread(
                        bot.send_message,
                        config.notify_chat_id,
                        f"Отправил в Дайвинчик: {dv_command} ({commands[text]}).",
                    )
                    self.log(f"Ответ боту: отправлена команда {dv_command} ({commands[text]}).")
            except asyncio.CancelledError:
                raise
            except Exception as exc:
                self.log(f"Bot API ответы: {exc}")
                await asyncio.sleep(2)

    async def _login_send_code(self, config: AppConfig) -> None:
        self.log("Telegram: подключаюсь через указанный прокси.")
        layer = make_layer(config)
        await layer.connect()
        if self._login_layer:
            await self._login_layer.disconnect()
        self._login_layer = layer
        self.log("Telegram: соединение установлено, проверяю доступность API.")
        health = await layer.check_connection_result()
        if not health.ok:
            self.log(f"Telegram соединение не прошло проверку: {health.error_type}: {health.message}")
            await layer.disconnect()
            self._login_layer = None
            self._stop_login_loop()
            return
        self.log("Telegram: запрашиваю код у Telegram.")
        result = await layer.send_code_result(config.phone)
        if not result.ok or not result.sent_code:
            self.log(f"Код не отправлен: {result.error_type or result.status}: {result.message or ''}")
            await layer.disconnect()
            self._login_layer = None
            self._stop_login_loop()
            return
        self._login_state = LoginState(result.sent_code.phone, result.sent_code.phone_code_hash)
        self.log("Код отправлен в Telegram.")

    async def _login_submit_code(self, code: str) -> None:
        if not self._login_layer or not self._login_state:
            raise RuntimeError("Сначала запросите код.")
        result = await self._login_layer.sign_in_result(self._login_state, code.strip())
        if result.ok:
            await self._login_layer.disconnect()
            self._login_layer = None
            self.log("Вход выполнен.")
            self._stop_login_loop()
        elif result.password_required:
            self.log("Нужен 2FA пароль.")
        else:
            self.log(f"Вход по коду не выполнен: {result.error_type or result.status}: {result.message or ''}")

    async def _login_submit_password(self, password: str) -> None:
        if not self._login_layer:
            raise RuntimeError("Сначала введите код.")
        result = await self._login_layer.sign_in_password_result(password)
        if result.ok:
            await self._login_layer.disconnect()
            self._login_layer = None
            self.log("Вход выполнен с 2FA.")
            self._stop_login_loop()
        else:
            self.log(f"Вход с 2FA не выполнен: {result.error_type or result.status}: {result.message or ''}")

    def _run_login(self, coro_factory: Callable[[], Awaitable[None]]) -> None:
        loop = self._ensure_login_loop()
        asyncio.run_coroutine_threadsafe(self._login_task(coro_factory), loop)

    async def _login_task(self, coro_factory: Callable[[], Awaitable[None]]) -> None:
        try:
            await coro_factory()
        except Exception:
            self.log(traceback.format_exc())

    def _ensure_login_loop(self) -> asyncio.AbstractEventLoop:
        with self._login_lock:
            if self._login_loop and self._login_thread and self._login_thread.is_alive():
                return self._login_loop
            self._login_ready.clear()
            self._login_thread = threading.Thread(target=self._login_thread_main, daemon=True)
            self._login_thread.start()
        if not self._login_ready.wait(timeout=5):
            raise RuntimeError("Telegram login loop was not started")
        if not self._login_loop:
            raise RuntimeError("Telegram login loop is unavailable")
        return self._login_loop

    def _login_thread_main(self) -> None:
        loop = None
        try:
            with proxy_socket_lock:
                loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            self._login_loop = loop
            self._login_ready.set()
            loop.run_forever()
        except Exception:
            self.log(traceback.format_exc())
        finally:
            if loop:
                loop.close()
            self._login_loop = None
            self._login_thread = None
            self._login_ready.set()

    def _stop_login_loop(self) -> None:
        if self._login_loop:
            self._login_loop.call_soon(self._login_loop.stop)


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


async def notify_profile(bot: BotApi, client, config: AppConfig, message, text: str) -> None:
    notification = with_answer_options(text)
    if not message.media:
        await asyncio.to_thread(bot.send_message, config.notify_chat_id, notification)
        return
    with tempfile.TemporaryDirectory(prefix="avto_vinchick_tg_") as temp_dir:
        media_path = await client.download_media(message, file=temp_dir)
        if not media_path:
            await asyncio.to_thread(bot.send_message, config.notify_chat_id, notification)
            return
        await asyncio.to_thread(
            bot.send_media,
            config.notify_chat_id,
            Path(media_path),
            caption="Фото анкеты",
        )
        await asyncio.to_thread(bot.send_message, config.notify_chat_id, notification)


def initial_bot_update_offset(bot: BotApi) -> int | None:
    updates = bot.get_updates(timeout=0)
    update_ids = [item.get("update_id") for item in updates.get("result") or [] if isinstance(item.get("update_id"), int)]
    return max(update_ids) + 1 if update_ids else None


def format_profile_message(text: str, result) -> str:
    header = "Анкета прошла фильтры"
    meta = f"Возраст: {result.age or 'не найден'} | слов: {result.word_count} | символов: {result.char_count}"
    return f"{header}\n{meta}\n\n{text}".strip()


def with_answer_options(text: str) -> str:
    options = (
        "Ответьте этому боту цифрой:\n"
        "1 - понравилась анкета\n"
        "2 - понравилась, лайк с посланием\n"
        "3 - не понравилась внешность\n"
        "4 - не понравилось описание"
    )
    return f"{text}\n\n{options}".strip()


def format_service_message(text: str, kind: DvMessageKind) -> str:
    title = "ДВ: лайк/интерес" if kind == DvMessageKind.LIKE_NOTICE else "ДВ: взаимная симпатия"
    return f"{title}\n\n{text}".strip()

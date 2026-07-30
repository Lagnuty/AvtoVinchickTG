from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Callable, Sequence
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import Any

from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.sessions import StringSession
from telethon.tl.custom.dialog import Dialog
from telethon.tl.custom.message import Message

from tg_api_zapret.config import TelegramConfig
from tg_api_zapret.sessions import FileSessionBackend, SessionBackend, SessionFileLock

UpdateHandler = Callable[[events.NewMessage.Event], Awaitable[None] | None]


@dataclass(frozen=True)
class SentCode:
    phone: str
    phone_code_hash: str


class TelegramLayer:
    def __init__(
        self,
        config: TelegramConfig | None = None,
        session_backend: SessionBackend | None = None,
    ) -> None:
        self.config = config or TelegramConfig.from_env()
        self.session_backend = session_backend or FileSessionBackend("telegram.session.txt")
        self._client: TelegramClient | None = None
        self._session_lock = SessionFileLock(self.session_backend.lock_path())

    async def connect(self) -> "TelegramLayer":
        if self._client and self._client.is_connected():
            return self

        self._session_lock.acquire()
        try:
            self._client = TelegramClient(
                self.session_backend.client_session(),
                self.config.api_id,
                self.config.api_hash,
                device_model=self.config.device_model,
                system_version=self.config.system_version,
                app_version=self.config.app_version,
                lang_code=self.config.lang_code,
                system_lang_code=self.config.system_lang_code,
                request_retries=self.config.request_retries,
                connection_retries=self.config.connection_retries,
                retry_delay=self.config.retry_delay,
                timeout=self.config.timeout,
                proxy=self.config.proxy,
            )
            await self._client.connect()
            self._persist_session()
        except Exception:
            self._session_lock.release()
            raise
        return self

    async def disconnect(self) -> None:
        if not self._client:
            self._session_lock.release()
            return
        try:
            self._persist_session()
            await self._client.disconnect()
        finally:
            self._session_lock.release()

    @asynccontextmanager
    async def lifespan(self) -> AsyncIterator["TelegramLayer"]:
        await self.connect()
        try:
            yield self
        finally:
            await self.disconnect()

    async def is_authorized(self) -> bool:
        client = await self._require_client()
        return await client.is_user_authorized()

    async def is_connected(self) -> bool:
        client = await self._require_client()
        return client.is_connected()

    async def send_code(self, phone: str) -> SentCode:
        client = await self._require_client()
        sent = await client.send_code_request(phone)
        self._persist_session()
        return SentCode(phone=phone, phone_code_hash=sent.phone_code_hash)

    async def sign_in(self, sent_code: SentCode, code: str) -> None:
        client = await self._require_client()
        await client.sign_in(
            phone=sent_code.phone,
            code=code,
            phone_code_hash=sent_code.phone_code_hash,
        )
        self._persist_session()

    async def sign_in_password(self, password: str) -> None:
        client = await self._require_client()
        await client.sign_in(password=password)
        self._persist_session()

    async def interactive_login(
        self,
        phone: str,
        code_provider: Callable[[], str],
        password_provider: Callable[[], str] | None = None,
    ) -> None:
        sent_code = await self.send_code(phone)
        try:
            await self.sign_in(sent_code, code_provider())
        except SessionPasswordNeededError:
            if password_provider is None:
                raise
            await self.sign_in_password(password_provider())

    async def send_message(
        self,
        entity: str | int,
        text: str,
        *,
        parse_mode: str | None = None,
    ) -> Message:
        client = await self._require_authorized_client()
        message = await client.send_message(entity, text, parse_mode=parse_mode)
        self._persist_session()
        return message

    async def get_dialogs(self, limit: int = 100) -> Sequence[Dialog]:
        client = await self._require_authorized_client()
        return await client.get_dialogs(limit=limit)

    async def iter_messages(
        self,
        entity: str | int,
        *,
        limit: int | None = 100,
    ) -> AsyncIterator[Message]:
        client = await self._require_authorized_client()
        async for message in client.iter_messages(entity, limit=limit):
            yield message

    async def invoke(self, request: Any) -> Any:
        client = await self._require_authorized_client()
        result = await client(request)
        self._persist_session()
        return result

    async def authorized_client(self) -> TelegramClient:
        return await self._require_authorized_client()

    async def stream_updates(
        self,
        handler: UpdateHandler,
        *,
        chats: Sequence[str | int] | str | int | None = None,
    ) -> None:
        client = await self._require_authorized_client()

        async def wrapped(event: events.NewMessage.Event) -> None:
            result = handler(event)
            if result is not None:
                await result

        client.add_event_handler(wrapped, events.NewMessage(chats=chats))
        await client.run_until_disconnected()

    async def _require_client(self) -> TelegramClient:
        if not self._client:
            await self.connect()
        if not self._client:
            raise RuntimeError("Telegram client is not initialized")
        return self._client

    async def _require_authorized_client(self) -> TelegramClient:
        client = await self._require_client()
        if not await client.is_user_authorized():
            raise PermissionError("Telegram session is not authorized. Run login first.")
        return client

    def _persist_session(self) -> None:
        if not self._client:
            return
        session_string = StringSession.save(self._client.session)
        if session_string:
            self.session_backend.save(session_string)

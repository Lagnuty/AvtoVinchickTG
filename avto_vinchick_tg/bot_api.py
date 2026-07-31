from __future__ import annotations

import json
import mimetypes
import socket
import threading
import uuid
from pathlib import Path
from typing import Any
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen

proxy_socket_lock = threading.RLock()


class BotApi:
    def __init__(self, token: str, *, proxy_url: str = "") -> None:
        self.token = token.strip()
        self.proxy_url = proxy_url.strip()

    def get_me(self) -> dict[str, Any]:
        return self.call("getMe")

    def get_updates(self, *, offset: int | None = None, timeout: int = 1) -> dict[str, Any]:
        payload: dict[str, Any] = {"timeout": timeout}
        if offset is not None:
            payload["offset"] = offset
        return self.call("getUpdates", payload)

    def send_message(self, chat_id: str, text: str, *, reply_markup: dict[str, Any] | None = None) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for chunk in split_telegram_text(text):
            payload = {
                "chat_id": chat_id,
                "text": chunk,
                "disable_web_page_preview": True,
            }
            if reply_markup:
                payload["reply_markup"] = json.dumps(reply_markup, ensure_ascii=False)
            result = self.call("sendMessage", payload)
        return result

    def send_media(
        self,
        chat_id: str,
        file_path: Path,
        *,
        caption: str = "",
        reply_markup: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        method = "sendPhoto" if is_photo_file(file_path) else "sendDocument"
        field_name = "photo" if method == "sendPhoto" else "document"
        fields: dict[str, Any] = {"chat_id": chat_id}
        if caption:
            fields["caption"] = caption[:1024]
        if reply_markup:
            fields["reply_markup"] = json.dumps(reply_markup, ensure_ascii=False)
        return self.call_multipart(method, fields, field_name, file_path)

    def send_media_group(self, chat_id: str, file_paths: list[Path], *, caption: str = "") -> dict[str, Any]:
        files = file_paths[:10]
        if not files:
            return self.send_message(chat_id, caption or "Медиа анкеты")
        media = []
        file_map: dict[str, Path] = {}
        for index, file_path in enumerate(files):
            attach_name = f"file{index}"
            item: dict[str, Any] = {
                "type": "photo" if is_photo_file(file_path) else "document",
                "media": f"attach://{attach_name}",
            }
            if index == 0 and caption:
                item["caption"] = caption[:1024]
            media.append(item)
            file_map[attach_name] = file_path
        return self.call_multipart_files(
            "sendMediaGroup",
            {"chat_id": chat_id, "media": json.dumps(media, ensure_ascii=False)},
            file_map,
        )

    def answer_callback_query(self, callback_query_id: str, *, text: str = "") -> dict[str, Any]:
        payload = {"callback_query_id": callback_query_id}
        if text:
            payload["text"] = text
        return self.call("answerCallbackQuery", payload)

    def call(self, method: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        if not self.token:
            raise ValueError("Bot token is empty")
        url = f"https://api.telegram.org/bot{self.token}/{method}"
        data = urlencode(payload or {}).encode("utf-8")
        request = Request(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
        return run_with_optional_socks_proxy(self.proxy_url, lambda: read_json(request))

    def call_multipart(
        self,
        method: str,
        fields: dict[str, Any],
        file_field: str,
        file_path: Path,
    ) -> dict[str, Any]:
        if not self.token:
            raise ValueError("Bot token is empty")
        boundary = f"----AvtoVinchickTG{uuid.uuid4().hex}"
        body = build_multipart_body(boundary, fields, file_field, file_path)
        request = Request(
            f"https://api.telegram.org/bot{self.token}/{method}",
            data=body,
            headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        )
        return run_with_optional_socks_proxy(self.proxy_url, lambda: read_json(request))

    def call_multipart_files(
        self,
        method: str,
        fields: dict[str, Any],
        files: dict[str, Path],
    ) -> dict[str, Any]:
        if not self.token:
            raise ValueError("Bot token is empty")
        boundary = f"----AvtoVinchickTG{uuid.uuid4().hex}"
        body = build_multipart_body_files(boundary, fields, files)
        request = Request(
            f"https://api.telegram.org/bot{self.token}/{method}",
            data=body,
            headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        )
        return run_with_optional_socks_proxy(self.proxy_url, lambda: read_json(request))


def read_json(request: Request) -> dict[str, Any]:
    with urlopen(request, timeout=40) as response:
        return json.loads(response.read().decode("utf-8"))


def run_with_optional_socks_proxy(proxy_url: str, callback):
    if not proxy_url:
        return callback()
    parsed = urlparse(proxy_url)
    if parsed.scheme.lower() not in {"socks5", "socks5h"}:
        return callback()

    import socks

    with proxy_socket_lock:
        original_socket = socket.socket
        rdns = parsed.scheme.lower() == "socks5h"
        socks.set_default_proxy(
            socks.SOCKS5,
            parsed.hostname,
            parsed.port,
            rdns=rdns,
            username=parsed.username,
            password=parsed.password,
        )
        socket.socket = socks.socksocket
        try:
            return callback()
        finally:
            socket.socket = original_socket
            socks.set_default_proxy()


def split_telegram_text(text: str, limit: int = 3900) -> list[str]:
    clean = text or " "
    if len(clean) <= limit:
        return [clean]
    chunks = []
    while clean:
        chunks.append(clean[:limit])
        clean = clean[limit:]
    return chunks


def build_multipart_body(boundary: str, fields: dict[str, Any], file_field: str, file_path: Path) -> bytes:
    return build_multipart_body_files(boundary, fields, {file_field: file_path})


def build_multipart_body_files(boundary: str, fields: dict[str, Any], files: dict[str, Path]) -> bytes:
    parts: list[bytes] = []
    for name, value in fields.items():
        parts.extend(
            [
                f"--{boundary}\r\n".encode("utf-8"),
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode("utf-8"),
                str(value).encode("utf-8"),
                b"\r\n",
            ]
        )
    for file_field, file_path in files.items():
        filename = file_path.name
        content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
        parts.extend(
            [
                f"--{boundary}\r\n".encode("utf-8"),
                (
                    f'Content-Disposition: form-data; name="{file_field}"; filename="{filename}"\r\n'
                    f"Content-Type: {content_type}\r\n\r\n"
                ).encode("utf-8"),
                file_path.read_bytes(),
                b"\r\n",
            ]
        )
    parts.append(f"--{boundary}--\r\n".encode("utf-8"))
    return b"".join(parts)


def is_photo_file(file_path: Path) -> bool:
    return file_path.suffix.casefold() in {".jpg", ".jpeg", ".png", ".webp"}

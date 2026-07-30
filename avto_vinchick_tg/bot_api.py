from __future__ import annotations

import json
import socket
import threading
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

    def send_message(self, chat_id: str, text: str) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for chunk in split_telegram_text(text):
            result = self.call(
                "sendMessage",
                {
                    "chat_id": chat_id,
                    "text": chunk,
                    "disable_web_page_preview": True,
                },
            )
        return result

    def call(self, method: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        if not self.token:
            raise ValueError("Bot token is empty")
        url = f"https://api.telegram.org/bot{self.token}/{method}"
        data = urlencode(payload or {}).encode("utf-8")
        request = Request(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
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

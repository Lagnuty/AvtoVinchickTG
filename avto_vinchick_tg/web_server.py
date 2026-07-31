from __future__ import annotations

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import mimetypes
from pathlib import Path
import threading
from typing import Any, Callable

from avto_vinchick_tg.service import AppService


class WebServer:
    def __init__(self, service: AppService, host: str = "127.0.0.1", port: int = 0) -> None:
        self.service = service
        self.httpd = ThreadingHTTPServer((host, port), self._handler_class())
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)

    @property
    def url(self) -> str:
        host, port = self.httpd.server_address
        return f"http://{host}:{port}/"

    def start(self) -> None:
        self.thread.start()

    def stop(self) -> None:
        self.httpd.shutdown()

    def _handler_class(self):
        service = self.service

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self) -> None:
                if self.path == "/" or self.path.startswith("/static/"):
                    self.serve_static()
                    return
                if self.path == "/api/status":
                    self.send_json(service.snapshot())
                    return
                self.send_error(HTTPStatus.NOT_FOUND)

            def do_POST(self) -> None:
                routes: dict[str, Callable[[dict[str, Any]], Any]] = {
                    "/api/config": service.save_config,
                    "/api/proxy/check": lambda data: service.check_proxy(str(data.get("proxy_url") or "")),
                    "/api/telegram/send-code": service.send_code,
                    "/api/telegram/submit-code": lambda data: service.submit_code(str(data.get("code") or "")),
                    "/api/telegram/submit-password": lambda data: service.submit_password(
                        str(data.get("password") or "")
                    ),
                    "/api/bot/test": service.test_bot,
                    "/api/bot/find-chat-id": service.find_chat_id,
                    "/api/runner/start": service.start,
                    "/api/runner/stop": lambda data: service.stop(),
                    "/api/filter-profile/export": service.export_filter_profile,
                    "/api/filter-profile/import": service.import_filter_profile,
                    "/api/updates/check": service.check_updates,
                    "/api/updates/install": service.install_update,
                }
                try:
                    if self.path == "/api/taste/import":
                        filename = self.headers.get("X-Filename") or "telegram-export.json"
                        result = service.import_taste_export(self.read_body(), filename)
                        self.send_json(result)
                        return
                    handler = routes.get(self.path)
                    if not handler:
                        self.send_error(HTTPStatus.NOT_FOUND)
                        return
                    self.send_json(handler(self.read_json()))
                except Exception as exc:
                    self.send_json({"ok": False, "error": str(exc)}, status=500)

            def serve_static(self) -> None:
                root = web_root()
                target = root / "index.html" if self.path == "/" else root / self.path.removeprefix("/static/")
                target = target.resolve()
                if not str(target).startswith(str(root.resolve())) or not target.exists() or not target.is_file():
                    self.send_error(HTTPStatus.NOT_FOUND)
                    return
                content_type = mimetypes.guess_type(str(target))[0] or "application/octet-stream"
                data = target.read_bytes()
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", content_type)
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

            def read_body(self) -> bytes:
                length = int(self.headers.get("Content-Length") or 0)
                return self.rfile.read(length)

            def read_json(self) -> dict[str, Any]:
                body = self.read_body()
                return json.loads(body.decode("utf-8")) if body else {}

            def send_json(self, payload: Any, status: int = 200) -> None:
                data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
                self.send_response(status)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

            def log_message(self, format: str, *args) -> None:  # noqa: A002
                return

        return Handler


def web_root() -> Path:
    return Path(__file__).resolve().parent / "web"

from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
import sys
from typing import Any

from avto_vinchick_tg.filters import FilterSettings


def default_app_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent / "data"
    return Path(__file__).resolve().parent.parent / ".data"


APP_DIR = default_app_dir()
SETTINGS_PATH = APP_DIR / "settings.json"
SESSION_PATH = APP_DIR / "telegram.session.txt"


@dataclass(frozen=True)
class AppConfig:
    phone: str = ""
    bot_token: str = ""
    notify_chat_id: str = ""
    source_chat: str = "LeomatchBot"
    proxy_url: str = ""
    filters: FilterSettings = field(default_factory=FilterSettings)
    send_rejects_to_log: bool = True

    @classmethod
    def load(cls, path: Path = SETTINGS_PATH) -> "AppConfig":
        if not path.exists():
            return cls()
        data = json.loads(path.read_text(encoding="utf-8"))
        return cls(
            phone=str(data.get("phone") or ""),
            bot_token=str(data.get("bot_token") or ""),
            notify_chat_id=str(data.get("notify_chat_id") or ""),
            source_chat=str(data.get("source_chat") or "LeomatchBot"),
            proxy_url=str(data.get("proxy_url") or ""),
            filters=FilterSettings.from_dict(data.get("filters")),
            send_rejects_to_log=bool(data.get("send_rejects_to_log", True)),
        )

    def save(self, path: Path = SETTINGS_PATH) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def to_dict(self) -> dict[str, Any]:
        return {
            "phone": self.phone,
            "bot_token": self.bot_token,
            "notify_chat_id": self.notify_chat_id,
            "source_chat": self.source_chat,
            "proxy_url": self.proxy_url,
            "filters": self.filters.to_dict(),
            "send_rejects_to_log": self.send_rejects_to_log,
        }

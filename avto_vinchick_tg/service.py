from __future__ import annotations

from dataclasses import asdict
from datetime import datetime
from pathlib import Path
import tempfile
import threading
from typing import Any
from urllib.request import Request, urlopen

from avto_vinchick_tg import __version__ as APP_VERSION
from avto_vinchick_tg.app_update import (
    AppRelease,
    download_release_asset,
    fetch_latest_app_release,
    install_downloaded_release,
)
from avto_vinchick_tg.bot_api import BotApi, run_with_optional_socks_proxy
from avto_vinchick_tg.core_update import fetch_latest_core_version, is_newer_version
from avto_vinchick_tg.dv_bot import DvActionSettings
from avto_vinchick_tg.filter_profile import FilterProfile, load_filter_profile, save_filter_profile
from avto_vinchick_tg.filters import FilterSettings
from avto_vinchick_tg.runner import VinchikRunner
from avto_vinchick_tg.settings import APP_DIR, AppConfig
from avto_vinchick_tg.taste_model import TasteModel, TasteSettings
from tg_api_zapret import __version__ as CORE_VERSION


class AppService:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self.logs: list[str] = []
        self.latest_app_release: AppRelease | None = None
        self.runner = VinchikRunner(self.log)

    def log(self, message: str) -> None:
        text = message.rstrip()
        if not text:
            return
        line = f"[{datetime.now().strftime('%H:%M:%S')}] {text}"
        with self._lock:
            self.logs.append(line)
            self.logs = self.logs[-800:]
        write_log_line(line)

    def snapshot(self) -> dict[str, Any]:
        config = AppConfig.load()
        taste_model = TasteModel()
        return {
            "app_version": APP_VERSION,
            "core_version": CORE_VERSION,
            "running": self.runner.running,
            "logs": self.get_logs(),
            "config": config.to_dict(),
            "taste_samples": {
                "positive": taste_model.positive_samples,
                "negative": taste_model.negative_samples,
                "total": taste_model.total_samples,
            },
            "latest_release": asdict(self.latest_app_release) if self.latest_app_release else None,
        }

    def get_logs(self) -> list[str]:
        with self._lock:
            return list(self.logs)

    def save_config(self, payload: dict[str, Any]) -> dict[str, Any]:
        config = config_from_dict(payload)
        config.save()
        self.log("Настройки сохранены.")
        return config.to_dict()

    def check_proxy(self, proxy_url: str) -> dict[str, Any]:
        try:
            request = Request("https://api.telegram.org", headers={"User-Agent": "AvtoVinchickTG"})
            run_with_optional_socks_proxy(proxy_url, lambda: urlopen(request, timeout=20).read(64))
        except Exception as exc:
            self.log(f"Прокси не прошел проверку: {exc}")
            return {"ok": False, "message": str(exc)}
        self.log("Прокси работает. Можно продолжать.")
        return {"ok": True, "message": "Прокси работает. Можно продолжать."}

    def send_code(self, payload: dict[str, Any]) -> dict[str, Any]:
        config = config_from_dict(payload)
        config.save()
        self.log("Telegram: запрашиваю код входа.")
        self.runner.login_send_code(config)
        return {"ok": True}

    def submit_code(self, code: str) -> dict[str, Any]:
        self.log("Telegram: отправляю введенный код.")
        self.runner.login_submit_code(code)
        return {"ok": True}

    def submit_password(self, password: str) -> dict[str, Any]:
        self.log("Telegram: отправляю 2FA пароль.")
        self.runner.login_submit_password(password)
        return {"ok": True}

    def test_bot(self, payload: dict[str, Any]) -> dict[str, Any]:
        config = config_from_dict(payload)
        me = BotApi(config.bot_token, proxy_url=config.proxy_url).get_me()
        username = me.get("result", {}).get("username", "unknown")
        self.log(f"Бот отвечает: @{username}")
        return {"ok": True, "username": username}

    def find_chat_id(self, payload: dict[str, Any]) -> dict[str, Any]:
        config = config_from_dict(payload)
        updates = BotApi(config.bot_token, proxy_url=config.proxy_url).get_updates()
        items = updates.get("result") or []
        if not items:
            raise ValueError("Сначала напишите любое сообщение своему боту.")
        message = items[-1].get("message") or items[-1].get("edited_message") or {}
        chat_id = str((message.get("chat") or {}).get("id") or "")
        if not chat_id:
            raise ValueError("В последнем update не найден chat_id.")
        self.log(f"chat_id найден: {chat_id}")
        return {"ok": True, "chat_id": chat_id}

    def start(self, payload: dict[str, Any]) -> dict[str, Any]:
        config = config_from_dict(payload)
        if not config.bot_token or not config.notify_chat_id:
            raise ValueError("Укажите bot token и chat_id для уведомлений.")
        config.save()
        self.runner.start(config)
        self.log("Запуск слушателя запрошен.")
        return {"ok": True}

    def stop(self) -> dict[str, Any]:
        self.runner.stop()
        self.log("Остановка слушателя запрошена.")
        return {"ok": True}

    def import_taste_export(self, data: bytes, filename: str) -> dict[str, Any]:
        suffix = Path(filename).suffix or ".json"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as handle:
            handle.write(data)
            temp_path = Path(handle.name)
        try:
            result = TasteModel().import_export(temp_path)
        finally:
            temp_path.unlink(missing_ok=True)
        self.log(
            "ML: импорт завершен. "
            f"Оценок: {result.imported}, положительных: {result.positive}, "
            f"отрицательных по описанию: {result.negative}, пропущено: {result.skipped}."
        )
        return asdict(result)

    def export_filter_profile(self, payload: dict[str, Any]) -> dict[str, Any]:
        config = config_from_dict(payload)
        return FilterProfile(config.filters, config.taste).to_dict()

    def import_filter_profile(self, payload: dict[str, Any]) -> dict[str, Any]:
        profile = FilterProfile.from_dict(payload)
        config = AppConfig.load()
        updated = AppConfig(
            phone=config.phone,
            bot_token=config.bot_token,
            notify_chat_id=config.notify_chat_id,
            source_chat=config.source_chat,
            proxy_url=config.proxy_url,
            filters=profile.filters,
            taste=profile.taste,
            dv_actions=config.dv_actions,
            send_rejects_to_log=config.send_rejects_to_log,
        )
        updated.save()
        self.log("Фильтры импортированы из JSON.")
        return updated.to_dict()

    def check_updates(self, payload: dict[str, Any]) -> dict[str, Any]:
        config = config_from_dict(payload)
        latest_core = fetch_latest_core_version(config.proxy_url)
        core_update = latest_core if is_newer_version(latest_core, CORE_VERSION) else None
        self.latest_app_release = fetch_latest_app_release(APP_VERSION, config.proxy_url)
        if self.latest_app_release:
            self.log(f"Доступно обновление приложения: v{self.latest_app_release.version}.")
        else:
            self.log("Обновления приложения не найдены.")
        return {
            "core_update": core_update,
            "app_update": asdict(self.latest_app_release) if self.latest_app_release else None,
        }

    def install_update(self, payload: dict[str, Any]) -> dict[str, Any]:
        config = config_from_dict(payload)
        if not self.latest_app_release:
            raise ValueError("Нет выбранного обновления приложения.")
        installer_path = download_release_asset(self.latest_app_release, config.proxy_url)
        install_downloaded_release(installer_path)
        self.log("Обновление скачано. Приложение закроется и перезапустится.")
        return {"ok": True}


def config_from_dict(data: dict[str, Any]) -> AppConfig:
    data = data or {}
    return AppConfig(
        phone=str(data.get("phone") or ""),
        bot_token=str(data.get("bot_token") or ""),
        notify_chat_id=str(data.get("notify_chat_id") or ""),
        source_chat=str(data.get("source_chat") or "LeomatchBot"),
        proxy_url=str(data.get("proxy_url") or ""),
        filters=FilterSettings.from_dict(data.get("filters")),
        taste=TasteSettings.from_dict(data.get("taste")),
        dv_actions=DvActionSettings.from_dict(data.get("dv_actions")),
        send_rejects_to_log=bool(data.get("send_rejects_to_log", True)),
    )


def write_log_line(line: str) -> None:
    try:
        log_dir = APP_DIR / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        with (log_dir / "app.log").open("a", encoding="utf-8") as handle:
            handle.write(line + "\n")
    except OSError:
        pass

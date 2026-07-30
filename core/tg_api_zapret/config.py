from __future__ import annotations

from dataclasses import dataclass, field
import json
import locale
import os
from pathlib import Path
import platform
from typing import Any
from urllib.parse import urlparse

OFFICIAL_DESKTOP_API_ID = 2040
OFFICIAL_DESKTOP_API_HASH = "b18441a1ff607e10a989891a5462e627"
OFFICIAL_DESKTOP_APP_VERSION = "7.0.6"
LANGUAGE_ALIASES = {
    "english": "en",
    "russian": "ru",
    "ukrainian": "uk",
}
COUNTRY_ALIASES = {
    "russia": "RU",
    "ukraine": "UA",
    "united states": "US",
}


def detect_system_version() -> str:
    system = platform.system() or "Linux"
    release = platform.release()
    machine = platform.machine()
    parts = [system]
    if release:
        parts.append(release)
    if machine:
        parts.append(machine)
    return " ".join(parts)


def detect_system_lang_code() -> str:
    language, _ = locale.getlocale()
    if not language:
        language = os.getenv("LANG", "").split(".", 1)[0]
    return normalize_locale_code(language or "en-US")


def detect_lang_code() -> str:
    return detect_system_lang_code().split("-", 1)[0].lower() or "en"


def normalize_locale_code(value: str) -> str:
    normalized = value.strip()
    if not normalized or normalized.upper() in {"C", "POSIX", "C.UTF-8"}:
        return "en-US"
    normalized = normalized.split(".", 1)[0].split("@", 1)[0].replace("_", "-")
    if not normalized:
        return "en-US"
    parts = normalized.split("-", 1)
    language = LANGUAGE_ALIASES.get(parts[0].lower(), parts[0].lower())
    if len(parts) == 1:
        return language
    country_raw = parts[1].replace("-", " ").strip()
    country = COUNTRY_ALIASES.get(country_raw.lower(), country_raw.upper())
    return f"{language}-{country}"


@dataclass(frozen=True)
class TelegramConfig:
    api_id: int = OFFICIAL_DESKTOP_API_ID
    api_hash: str = OFFICIAL_DESKTOP_API_HASH
    device_model: str = "Telegram Desktop"
    system_version: str = field(default_factory=detect_system_version)
    app_version: str = OFFICIAL_DESKTOP_APP_VERSION
    lang_code: str = field(default_factory=detect_lang_code)
    system_lang_code: str = field(default_factory=detect_system_lang_code)
    request_retries: int = 5
    connection_retries: int = 5
    retry_delay: int = 2
    timeout: int = 30
    proxy: tuple[Any, ...] | None = None

    @classmethod
    def from_env(
        cls,
        *,
        proxy_url: str | None = None,
        client_profile: "ClientProfile | None" = None,
    ) -> "TelegramConfig":
        resolved_proxy_url = proxy_url or os.getenv("TELEGRAM_PROXY_URL")
        profile = client_profile or ClientProfile()
        return cls(
            api_id=int(os.getenv("TELEGRAM_API_ID", OFFICIAL_DESKTOP_API_ID)),
            api_hash=os.getenv("TELEGRAM_API_HASH", OFFICIAL_DESKTOP_API_HASH),
            device_model=os.getenv("TELEGRAM_DEVICE_MODEL", profile.device_model),
            system_version=os.getenv("TELEGRAM_SYSTEM_VERSION", profile.system_version),
            app_version=os.getenv("TELEGRAM_APP_VERSION", profile.app_version),
            lang_code=os.getenv("TELEGRAM_LANG_CODE", profile.lang_code),
            system_lang_code=os.getenv("TELEGRAM_SYSTEM_LANG_CODE", profile.system_lang_code),
            request_retries=int(os.getenv("TELEGRAM_REQUEST_RETRIES", "5")),
            connection_retries=int(os.getenv("TELEGRAM_CONNECTION_RETRIES", "5")),
            retry_delay=int(os.getenv("TELEGRAM_RETRY_DELAY", "2")),
            timeout=int(os.getenv("TELEGRAM_TIMEOUT", "30")),
            proxy=parse_proxy_url(resolved_proxy_url) if resolved_proxy_url else None,
        )


@dataclass(frozen=True)
class ClientProfile:
    device_model: str = "Telegram Desktop"
    system_version: str = field(default_factory=detect_system_version)
    app_version: str = OFFICIAL_DESKTOP_APP_VERSION
    lang_code: str = field(default_factory=detect_lang_code)
    system_lang_code: str = field(default_factory=detect_system_lang_code)

    @classmethod
    def from_dict(cls, data: dict[str, Any] | None) -> "ClientProfile":
        defaults = cls()
        if not data:
            return defaults
        return cls(
            device_model=data.get("device_model") or defaults.device_model,
            system_version=data.get("system_version") or defaults.system_version,
            app_version=normalize_app_version(data.get("app_version")),
            lang_code=data.get("lang_code") or defaults.lang_code,
            system_lang_code=data.get("system_lang_code") or defaults.system_lang_code,
        )

    def to_dict(self) -> dict[str, str]:
        return {
            "device_model": self.device_model,
            "system_version": self.system_version,
            "app_version": self.app_version,
            "lang_code": self.lang_code,
            "system_lang_code": self.system_lang_code,
        }


@dataclass(frozen=True)
class ServiceSettings:
    api_name: str = "tg-api-zapret"
    public_base_url: str | None = None
    default_api_interface: str = "rest"
    enabled_interfaces: list[str] = field(
        default_factory=lambda: ["rest", "json_rpc", "websocket", "sse", "queue", "python_sdk"]
    )
    max_queue_jobs_list: int = 1000
    stream_queue_size: int = 100
    request_timeout_seconds: int = 60
    expose_docs: bool = False
    cors_origins: list[str] = field(default_factory=list)
    require_api_token: bool = True
    api_token_env: str = "TG_API_TOKEN"
    api_tokens_env: str = "TG_API_TOKENS"
    rate_limit_per_minute: int = 120
    audit_log_path: str | None = None
    enable_raw_invoke: bool = False
    enable_layer_invoke: bool = False
    bot_token_accounts: dict[str, str] = field(default_factory=dict)
    telegram_safe_mode: bool = True
    telegram_serialize_account_actions: bool = True
    telegram_actions_per_minute: int = 20
    telegram_send_actions_per_minute: int = 6
    telegram_resolve_actions_per_minute: int = 10
    telegram_raw_actions_per_minute: int = 3
    telegram_join_actions_per_hour: int = 5
    telegram_destructive_actions_per_hour: int = 10
    telegram_media_downloads_per_minute: int = 30
    telegram_media_download_concurrency: int = 2
    telegram_auth_requests_per_hour: int = 3
    telegram_requests_per_second: int = 10
    telegram_requests_per_minute: int = 50
    telegram_requests_per_hour: int = 500
    telegram_read_requests_per_second: int = 5
    telegram_send_requests_per_second: int = 2
    telegram_typing_requests_per_second: int = 1
    telegram_sync_requests_per_minute: int = 2
    max_dialog_limit: int = 100
    max_message_limit: int = 100
    blocked_account_names: list[str] = field(default_factory=lambda: ["string", "account"])
    telegram_min_action_interval_seconds: float = 1.25
    telegram_default_flood_cooldown_seconds: int = 300
    queue_visibility_timeout_seconds: int = 300
    queue_default_max_attempts: int = 3
    queue_execute_in_api: bool = True
    db_writer_queue_maxsize: int = 5000
    db_writer_locked_retries: int = 3
    db_writer_io_retries: int = 2
    db_writer_failed_alert_threshold: int = 10
    db_writer_dead_letter_max_records: int = 500
    db_writer_dead_letter_ttl_days: int = 30
    db_writer_degraded_queue_ratio: float = 0.8
    db_writer_drop_categories: list[str] = field(default_factory=lambda: ["diagnostics", "typing", "presence"])
    keep_accounts_online: bool = False
    online_update_interval_seconds: int = 300
    online_update_min_interval_seconds: int = 300
    online_update_max_interval_seconds: int = 900
    activity_idle_min_seconds: int = 120
    activity_idle_max_seconds: int = 300
    online_debounce_min_seconds: int = 30
    online_debounce_max_seconds: int = 60
    auto_connect_accounts: list[str] = field(default_factory=list)
    reconnect_enabled: bool = True
    reconnect_min_delay_seconds: int = 5
    reconnect_max_delay_seconds: int = 120
    passive_update_receiver: bool = True
    entity_cache_warmup_dialogs: int = 50
    entity_cache_warmup_min_dialogs: int = 40
    entity_cache_warmup_max_dialogs: int = 60
    require_connection_health_before_auth: bool = True
    connection_health_timeout_seconds: int = 20
    connection_health_cache_seconds: int = 30
    raw_updates_retention_days: int = 7
    flood_errors_retention_days: int = 30
    idempotency_retention_hours: int = 48
    idempotency_max_records: int = 10000
    idempotency_lease_seconds: int = 300
    idempotency_message_lease_seconds: int = 300
    idempotency_media_lease_seconds: int = 3600
    idempotency_large_file_lease_seconds: int = 7200
    idempotency_heartbeat_min_seconds: int = 30
    idempotency_heartbeat_max_seconds: int = 60
    idempotency_result_max_bytes: int = 1048576
    state_retention_min_interval_hours: int = 12
    state_retention_max_interval_hours: int = 24
    state_vacuum_interval_hours: int = 24

    @classmethod
    def from_dict(cls, data: dict[str, Any] | None) -> "ServiceSettings":
        if not data:
            return cls()
        defaults = cls()
        return cls(
            api_name=data.get("api_name") or cls.api_name,
            public_base_url=data.get("public_base_url") or None,
            default_api_interface=data.get("default_api_interface") or cls.default_api_interface,
            enabled_interfaces=normalize_interfaces(data.get("enabled_interfaces")),
            max_queue_jobs_list=int(data.get("max_queue_jobs_list", cls.max_queue_jobs_list)),
            stream_queue_size=int(data.get("stream_queue_size", cls.stream_queue_size)),
            request_timeout_seconds=int(
                data.get("request_timeout_seconds", cls.request_timeout_seconds)
            ),
            expose_docs=bool(data.get("expose_docs", cls.expose_docs)),
            cors_origins=list(data.get("cors_origins") or []),
            require_api_token=bool(data.get("require_api_token", cls.require_api_token)),
            api_token_env=data.get("api_token_env") or cls.api_token_env,
            api_tokens_env=data.get("api_tokens_env") or cls.api_tokens_env,
            rate_limit_per_minute=int(
                data.get("rate_limit_per_minute", cls.rate_limit_per_minute)
            ),
            audit_log_path=data.get("audit_log_path") or None,
            enable_raw_invoke=bool(data.get("enable_raw_invoke", cls.enable_raw_invoke)),
            enable_layer_invoke=bool(data.get("enable_layer_invoke", cls.enable_layer_invoke)),
            bot_token_accounts={
                str(token): normalize_account_name(account)
                for token, account in dict(data.get("bot_token_accounts") or {}).items()
            },
            telegram_safe_mode=bool(data.get("telegram_safe_mode", cls.telegram_safe_mode)),
            telegram_serialize_account_actions=bool(
                data.get("telegram_serialize_account_actions", cls.telegram_serialize_account_actions)
            ),
            telegram_actions_per_minute=int(
                data.get("telegram_actions_per_minute", cls.telegram_actions_per_minute)
            ),
            telegram_send_actions_per_minute=int(
                data.get("telegram_send_actions_per_minute", cls.telegram_send_actions_per_minute)
            ),
            telegram_resolve_actions_per_minute=int(
                data.get("telegram_resolve_actions_per_minute", cls.telegram_resolve_actions_per_minute)
            ),
            telegram_raw_actions_per_minute=int(
                data.get("telegram_raw_actions_per_minute", cls.telegram_raw_actions_per_minute)
            ),
            telegram_join_actions_per_hour=int(
                data.get("telegram_join_actions_per_hour", cls.telegram_join_actions_per_hour)
            ),
            telegram_destructive_actions_per_hour=int(
                data.get(
                    "telegram_destructive_actions_per_hour",
                    cls.telegram_destructive_actions_per_hour,
                )
            ),
            telegram_media_downloads_per_minute=int(
                data.get(
                    "telegram_media_downloads_per_minute",
                    cls.telegram_media_downloads_per_minute,
                )
            ),
            telegram_media_download_concurrency=int(
                data.get(
                    "telegram_media_download_concurrency",
                    cls.telegram_media_download_concurrency,
                )
            ),
            telegram_auth_requests_per_hour=int(
                data.get("telegram_auth_requests_per_hour", cls.telegram_auth_requests_per_hour)
            ),
            telegram_requests_per_second=int(
                data.get("telegram_requests_per_second", cls.telegram_requests_per_second)
            ),
            telegram_requests_per_minute=int(
                data.get("telegram_requests_per_minute", cls.telegram_requests_per_minute)
            ),
            telegram_requests_per_hour=int(
                data.get("telegram_requests_per_hour", cls.telegram_requests_per_hour)
            ),
            telegram_read_requests_per_second=int(
                data.get("telegram_read_requests_per_second", cls.telegram_read_requests_per_second)
            ),
            telegram_send_requests_per_second=int(
                data.get("telegram_send_requests_per_second", cls.telegram_send_requests_per_second)
            ),
            telegram_typing_requests_per_second=int(
                data.get("telegram_typing_requests_per_second", cls.telegram_typing_requests_per_second)
            ),
            telegram_sync_requests_per_minute=int(
                data.get("telegram_sync_requests_per_minute", cls.telegram_sync_requests_per_minute)
            ),
            max_dialog_limit=int(data.get("max_dialog_limit", cls.max_dialog_limit)),
            max_message_limit=int(data.get("max_message_limit", cls.max_message_limit)),
            blocked_account_names=[
                normalize_account_name(item)
                for item in data.get("blocked_account_names", defaults.blocked_account_names)
            ],
            telegram_min_action_interval_seconds=float(
                data.get(
                    "telegram_min_action_interval_seconds",
                    cls.telegram_min_action_interval_seconds,
                )
            ),
            telegram_default_flood_cooldown_seconds=int(
                data.get(
                    "telegram_default_flood_cooldown_seconds",
                    cls.telegram_default_flood_cooldown_seconds,
                )
            ),
            queue_visibility_timeout_seconds=int(
                data.get("queue_visibility_timeout_seconds", cls.queue_visibility_timeout_seconds)
            ),
            queue_default_max_attempts=int(
                data.get("queue_default_max_attempts", cls.queue_default_max_attempts)
            ),
            queue_execute_in_api=bool(data.get("queue_execute_in_api", cls.queue_execute_in_api)),
            db_writer_queue_maxsize=int(
                data.get("db_writer_queue_maxsize", cls.db_writer_queue_maxsize)
            ),
            db_writer_locked_retries=int(
                data.get("db_writer_locked_retries", cls.db_writer_locked_retries)
            ),
            db_writer_io_retries=int(data.get("db_writer_io_retries", cls.db_writer_io_retries)),
            db_writer_failed_alert_threshold=int(
                data.get("db_writer_failed_alert_threshold", cls.db_writer_failed_alert_threshold)
            ),
            db_writer_dead_letter_max_records=int(
                data.get("db_writer_dead_letter_max_records", cls.db_writer_dead_letter_max_records)
            ),
            db_writer_dead_letter_ttl_days=int(
                data.get("db_writer_dead_letter_ttl_days", cls.db_writer_dead_letter_ttl_days)
            ),
            db_writer_degraded_queue_ratio=float(
                data.get("db_writer_degraded_queue_ratio", cls.db_writer_degraded_queue_ratio)
            ),
            db_writer_drop_categories=list(
                data.get("db_writer_drop_categories", defaults.db_writer_drop_categories)
            ),
            keep_accounts_online=bool(data.get("keep_accounts_online", cls.keep_accounts_online)),
            online_update_interval_seconds=int(
                data.get("online_update_interval_seconds", cls.online_update_interval_seconds)
            ),
            online_update_min_interval_seconds=int(
                data.get(
                    "online_update_min_interval_seconds",
                    cls.online_update_min_interval_seconds,
                )
            ),
            online_update_max_interval_seconds=int(
                data.get(
                    "online_update_max_interval_seconds",
                    cls.online_update_max_interval_seconds,
                )
            ),
            activity_idle_min_seconds=int(
                data.get("activity_idle_min_seconds", cls.activity_idle_min_seconds)
            ),
            activity_idle_max_seconds=int(
                data.get("activity_idle_max_seconds", cls.activity_idle_max_seconds)
            ),
            online_debounce_min_seconds=int(
                data.get("online_debounce_min_seconds", cls.online_debounce_min_seconds)
            ),
            online_debounce_max_seconds=int(
                data.get("online_debounce_max_seconds", cls.online_debounce_max_seconds)
            ),
            auto_connect_accounts=[
                normalize_account_name(item)
                for item in data.get("auto_connect_accounts", defaults.auto_connect_accounts)
            ],
            reconnect_enabled=bool(data.get("reconnect_enabled", cls.reconnect_enabled)),
            reconnect_min_delay_seconds=int(
                data.get("reconnect_min_delay_seconds", cls.reconnect_min_delay_seconds)
            ),
            reconnect_max_delay_seconds=int(
                data.get("reconnect_max_delay_seconds", cls.reconnect_max_delay_seconds)
            ),
            passive_update_receiver=bool(
                data.get("passive_update_receiver", cls.passive_update_receiver)
            ),
            entity_cache_warmup_dialogs=int(
                data.get("entity_cache_warmup_dialogs", cls.entity_cache_warmup_dialogs)
            ),
            entity_cache_warmup_min_dialogs=int(
                data.get("entity_cache_warmup_min_dialogs", cls.entity_cache_warmup_min_dialogs)
            ),
            entity_cache_warmup_max_dialogs=int(
                data.get("entity_cache_warmup_max_dialogs", cls.entity_cache_warmup_max_dialogs)
            ),
            require_connection_health_before_auth=bool(
                data.get(
                    "require_connection_health_before_auth",
                    cls.require_connection_health_before_auth,
                )
            ),
            connection_health_timeout_seconds=int(
                data.get(
                    "connection_health_timeout_seconds",
                    cls.connection_health_timeout_seconds,
                )
            ),
            connection_health_cache_seconds=int(
                data.get("connection_health_cache_seconds", cls.connection_health_cache_seconds)
            ),
            raw_updates_retention_days=int(
                data.get("raw_updates_retention_days", cls.raw_updates_retention_days)
            ),
            flood_errors_retention_days=int(
                data.get("flood_errors_retention_days", cls.flood_errors_retention_days)
            ),
            idempotency_retention_hours=int(
                data.get("idempotency_retention_hours", cls.idempotency_retention_hours)
            ),
            idempotency_max_records=int(
                data.get("idempotency_max_records", cls.idempotency_max_records)
            ),
            idempotency_lease_seconds=int(
                data.get("idempotency_lease_seconds", cls.idempotency_lease_seconds)
            ),
            idempotency_message_lease_seconds=int(
                data.get("idempotency_message_lease_seconds", cls.idempotency_message_lease_seconds)
            ),
            idempotency_media_lease_seconds=int(
                data.get("idempotency_media_lease_seconds", cls.idempotency_media_lease_seconds)
            ),
            idempotency_large_file_lease_seconds=int(
                data.get("idempotency_large_file_lease_seconds", cls.idempotency_large_file_lease_seconds)
            ),
            idempotency_heartbeat_min_seconds=int(
                data.get("idempotency_heartbeat_min_seconds", cls.idempotency_heartbeat_min_seconds)
            ),
            idempotency_heartbeat_max_seconds=int(
                data.get("idempotency_heartbeat_max_seconds", cls.idempotency_heartbeat_max_seconds)
            ),
            idempotency_result_max_bytes=int(
                data.get("idempotency_result_max_bytes", cls.idempotency_result_max_bytes)
            ),
            state_retention_min_interval_hours=int(
                data.get(
                    "state_retention_min_interval_hours",
                    cls.state_retention_min_interval_hours,
                )
            ),
            state_retention_max_interval_hours=int(
                data.get(
                    "state_retention_max_interval_hours",
                    cls.state_retention_max_interval_hours,
                )
            ),
            state_vacuum_interval_hours=int(
                data.get("state_vacuum_interval_hours", cls.state_vacuum_interval_hours)
            ),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "api_name": self.api_name,
            "public_base_url": self.public_base_url,
            "default_api_interface": self.default_api_interface,
            "enabled_interfaces": self.enabled_interfaces,
            "max_queue_jobs_list": self.max_queue_jobs_list,
            "stream_queue_size": self.stream_queue_size,
            "request_timeout_seconds": self.request_timeout_seconds,
            "expose_docs": self.expose_docs,
            "cors_origins": self.cors_origins,
            "require_api_token": self.require_api_token,
            "api_token_env": self.api_token_env,
            "api_tokens_env": self.api_tokens_env,
            "rate_limit_per_minute": self.rate_limit_per_minute,
            "audit_log_path": self.audit_log_path,
            "enable_raw_invoke": self.enable_raw_invoke,
            "enable_layer_invoke": self.enable_layer_invoke,
            "bot_token_accounts": self.bot_token_accounts,
            "telegram_safe_mode": self.telegram_safe_mode,
            "telegram_serialize_account_actions": self.telegram_serialize_account_actions,
            "telegram_actions_per_minute": self.telegram_actions_per_minute,
            "telegram_send_actions_per_minute": self.telegram_send_actions_per_minute,
            "telegram_resolve_actions_per_minute": self.telegram_resolve_actions_per_minute,
            "telegram_raw_actions_per_minute": self.telegram_raw_actions_per_minute,
            "telegram_join_actions_per_hour": self.telegram_join_actions_per_hour,
            "telegram_destructive_actions_per_hour": self.telegram_destructive_actions_per_hour,
            "telegram_media_downloads_per_minute": self.telegram_media_downloads_per_minute,
            "telegram_media_download_concurrency": self.telegram_media_download_concurrency,
            "telegram_auth_requests_per_hour": self.telegram_auth_requests_per_hour,
            "telegram_requests_per_second": self.telegram_requests_per_second,
            "telegram_requests_per_minute": self.telegram_requests_per_minute,
            "telegram_requests_per_hour": self.telegram_requests_per_hour,
            "telegram_read_requests_per_second": self.telegram_read_requests_per_second,
            "telegram_send_requests_per_second": self.telegram_send_requests_per_second,
            "telegram_typing_requests_per_second": self.telegram_typing_requests_per_second,
            "telegram_sync_requests_per_minute": self.telegram_sync_requests_per_minute,
            "max_dialog_limit": self.max_dialog_limit,
            "max_message_limit": self.max_message_limit,
            "blocked_account_names": self.blocked_account_names,
            "telegram_min_action_interval_seconds": self.telegram_min_action_interval_seconds,
            "telegram_default_flood_cooldown_seconds": self.telegram_default_flood_cooldown_seconds,
            "queue_visibility_timeout_seconds": self.queue_visibility_timeout_seconds,
            "queue_default_max_attempts": self.queue_default_max_attempts,
            "queue_execute_in_api": self.queue_execute_in_api,
            "db_writer_queue_maxsize": self.db_writer_queue_maxsize,
            "db_writer_locked_retries": self.db_writer_locked_retries,
            "db_writer_io_retries": self.db_writer_io_retries,
            "db_writer_failed_alert_threshold": self.db_writer_failed_alert_threshold,
            "db_writer_dead_letter_max_records": self.db_writer_dead_letter_max_records,
            "db_writer_dead_letter_ttl_days": self.db_writer_dead_letter_ttl_days,
            "db_writer_degraded_queue_ratio": self.db_writer_degraded_queue_ratio,
            "db_writer_drop_categories": self.db_writer_drop_categories,
            "keep_accounts_online": self.keep_accounts_online,
            "online_update_interval_seconds": self.online_update_interval_seconds,
            "online_update_min_interval_seconds": self.online_update_min_interval_seconds,
            "online_update_max_interval_seconds": self.online_update_max_interval_seconds,
            "activity_idle_min_seconds": self.activity_idle_min_seconds,
            "activity_idle_max_seconds": self.activity_idle_max_seconds,
            "online_debounce_min_seconds": self.online_debounce_min_seconds,
            "online_debounce_max_seconds": self.online_debounce_max_seconds,
            "auto_connect_accounts": self.auto_connect_accounts,
            "reconnect_enabled": self.reconnect_enabled,
            "reconnect_min_delay_seconds": self.reconnect_min_delay_seconds,
            "reconnect_max_delay_seconds": self.reconnect_max_delay_seconds,
            "passive_update_receiver": self.passive_update_receiver,
            "entity_cache_warmup_dialogs": self.entity_cache_warmup_dialogs,
            "entity_cache_warmup_min_dialogs": self.entity_cache_warmup_min_dialogs,
            "entity_cache_warmup_max_dialogs": self.entity_cache_warmup_max_dialogs,
            "require_connection_health_before_auth": self.require_connection_health_before_auth,
            "connection_health_timeout_seconds": self.connection_health_timeout_seconds,
            "connection_health_cache_seconds": self.connection_health_cache_seconds,
            "raw_updates_retention_days": self.raw_updates_retention_days,
            "flood_errors_retention_days": self.flood_errors_retention_days,
            "idempotency_retention_hours": self.idempotency_retention_hours,
            "idempotency_max_records": self.idempotency_max_records,
            "idempotency_lease_seconds": self.idempotency_lease_seconds,
            "idempotency_message_lease_seconds": self.idempotency_message_lease_seconds,
            "idempotency_media_lease_seconds": self.idempotency_media_lease_seconds,
            "idempotency_large_file_lease_seconds": self.idempotency_large_file_lease_seconds,
            "idempotency_heartbeat_min_seconds": self.idempotency_heartbeat_min_seconds,
            "idempotency_heartbeat_max_seconds": self.idempotency_heartbeat_max_seconds,
            "idempotency_result_max_bytes": self.idempotency_result_max_bytes,
            "state_retention_min_interval_hours": self.state_retention_min_interval_hours,
            "state_retention_max_interval_hours": self.state_retention_max_interval_hours,
            "state_vacuum_interval_hours": self.state_vacuum_interval_hours,
        }


@dataclass(frozen=True)
class AppSettings:
    proxy_url: str | None = None
    client_profile: ClientProfile = field(default_factory=ClientProfile)
    service: ServiceSettings = field(default_factory=ServiceSettings)
    active_account: str = "default"
    accounts: list[str] = field(default_factory=lambda: ["default"])

    @classmethod
    def load(cls, path: str | Path) -> "AppSettings":
        settings_path = Path(path).expanduser()
        if not settings_path.exists():
            return cls()
        data = json.loads(settings_path.read_text(encoding="utf-8"))
        return cls(
            proxy_url=data.get("proxy_url") or None,
            client_profile=ClientProfile.from_dict(data.get("client_profile")),
            service=ServiceSettings.from_dict(data.get("service")),
            active_account=data.get("active_account") or "default",
            accounts=normalize_accounts(data.get("accounts")),
        )

    def save(self, path: str | Path) -> None:
        settings_path = Path(path).expanduser()
        settings_path.parent.mkdir(parents=True, exist_ok=True)
        settings_path.write_text(
            json.dumps(
                {
                    "proxy_url": self.proxy_url,
                    "client_profile": self.client_profile.to_dict(),
                    "service": self.service.to_dict(),
                    "active_account": self.active_account,
                    "accounts": normalize_accounts(self.accounts),
                },
                indent=2,
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )
        try:
            settings_path.chmod(0o600)
        except OSError:
            pass

    def with_account(self, account: str) -> "AppSettings":
        account_name = normalize_account_name(account)
        accounts = normalize_accounts([*self.accounts, account_name])
        return AppSettings(
            proxy_url=self.proxy_url,
            client_profile=self.client_profile,
            service=self.service,
            active_account=account_name,
            accounts=accounts,
        )


def parse_proxy_url(proxy_url: str) -> tuple[Any, ...]:
    parsed = validate_proxy_url(proxy_url)
    scheme = parsed.scheme.lower()
    proxy_type = "http" if scheme == "https" else "socks5" if scheme == "socks5h" else scheme
    rdns = scheme in {"https", "socks5h"}

    return (
        proxy_type,
        parsed.hostname,
        parsed.port,
        rdns,
        parsed.username,
        parsed.password,
    )


def validate_proxy_url(proxy_url: str):
    parsed = urlparse(proxy_url)
    scheme = parsed.scheme.lower()
    if scheme not in {"http", "https", "socks5", "socks5h"}:
        raise ValueError("Proxy URL must use http, https, socks5, or socks5h scheme")
    if not parsed.hostname or not parsed.port:
        raise ValueError("Proxy URL must include host and port")
    return parsed


def normalize_accounts(accounts: list[str] | None) -> list[str]:
    values = []
    for account in accounts or ["default"]:
        normalized = normalize_account_name(account)
        if normalized not in values:
            values.append(normalized)
    return values or ["default"]


def normalize_account_name(account: str | None) -> str:
    value = (account or "default").strip()
    if not value:
        return "default"
    allowed = []
    for char in value:
        if char.isalnum() or char in {"-", "_", "."}:
            allowed.append(char)
        else:
            allowed.append("_")
    return "".join(allowed)


def normalize_app_version(app_version: str | None) -> str:
    if not app_version or app_version == "tg-api-zapret":
        return OFFICIAL_DESKTOP_APP_VERSION
    return app_version


def normalize_interfaces(interfaces: list[str] | None) -> list[str]:
    allowed = {"rest", "json_rpc", "websocket", "sse", "queue", "python_sdk"}
    values = []
    for interface in interfaces or ["rest", "json_rpc", "websocket", "sse", "queue", "python_sdk"]:
        if interface in allowed and interface not in values:
            values.append(interface)
    return values or ["rest"]

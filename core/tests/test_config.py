import pytest

from tg_api_zapret.config import (
    OFFICIAL_DESKTOP_API_HASH,
    OFFICIAL_DESKTOP_API_ID,
    OFFICIAL_DESKTOP_APP_VERSION,
    AppSettings,
    TelegramConfig,
    detect_lang_code,
    detect_system_lang_code,
    normalize_locale_code,
    parse_proxy_url,
    validate_proxy_url_result,
)


def test_config_uses_official_desktop_defaults() -> None:
    config = TelegramConfig()

    assert config.api_id == OFFICIAL_DESKTOP_API_ID
    assert config.api_hash == OFFICIAL_DESKTOP_API_HASH
    assert config.device_model == "Telegram Desktop"
    assert config.system_version
    assert config.app_version == OFFICIAL_DESKTOP_APP_VERSION
    assert config.lang_code == detect_lang_code()
    assert config.system_lang_code == detect_system_lang_code()


def test_config_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TELEGRAM_API_ID", "123")
    monkeypatch.setenv("TELEGRAM_API_HASH", "hash")
    monkeypatch.setenv("TELEGRAM_TIMEOUT", "7")

    config = TelegramConfig.from_env()

    assert config.api_id == 123
    assert config.api_hash == "hash"
    assert config.timeout == 7


def test_normalize_locale_code_handles_windows_language_names() -> None:
    assert normalize_locale_code("Russian_Russia") == "ru-RU"
    assert normalize_locale_code("Ukrainian_Ukraine") == "uk-UA"
    assert normalize_locale_code("en_US") == "en-US"
    assert normalize_locale_code("C") == "en-US"
    assert normalize_locale_code("POSIX") == "en-US"
    assert normalize_locale_code("ru_RU.UTF-8@variant") == "ru-RU"


@pytest.mark.parametrize(
    ("proxy_url", "proxy_type", "rdns"),
    [
        ("http://127.0.0.1:8080", "http", False),
        ("https://127.0.0.1:8080", "http", True),
        ("socks5://127.0.0.1:1080", "socks5", False),
        ("socks5h://127.0.0.1:1080", "socks5", True),
    ],
)
def test_parse_proxy_url(proxy_url: str, proxy_type: str, rdns: bool) -> None:
    parsed = parse_proxy_url(proxy_url)

    assert parsed[:4] == (proxy_type, "127.0.0.1", int(proxy_url.rsplit(":", 1)[1]), rdns)


def test_parse_proxy_url_with_auth() -> None:
    parsed = parse_proxy_url("socks5h://user:password@127.0.0.1:1080")

    assert parsed == ("socks5", "127.0.0.1", 1080, True, "user", "password")


def test_validate_proxy_url_result_is_typed() -> None:
    valid = validate_proxy_url_result("socks5h://127.0.0.1:1080")
    invalid = validate_proxy_url_result("ftp://127.0.0.1:21")

    assert valid.ok is True
    assert valid.scheme == "socks5h"
    assert valid.host == "127.0.0.1"
    assert valid.port == 1080
    assert valid.rdns is True
    assert invalid.ok is False
    assert invalid.error_type == "ValueError"
    assert invalid.message


def test_app_settings_roundtrip(tmp_path) -> None:
    path = tmp_path / "config.json"

    AppSettings(proxy_url="socks5h://127.0.0.1:1080").save(path)

    assert AppSettings.load(path).proxy_url == "socks5h://127.0.0.1:1080"


def test_app_settings_client_profile_roundtrip(tmp_path) -> None:
    path = tmp_path / "config.json"
    settings = AppSettings.load(path)
    custom = settings.client_profile.__class__(
        device_model="custom-api",
        system_version="Ubuntu",
        app_version="custom-api",
        lang_code="ru",
        system_lang_code="ru-RU",
    )

    AppSettings(proxy_url=None, client_profile=custom).save(path)
    loaded = AppSettings.load(path)

    assert loaded.client_profile.device_model == "custom-api"
    assert loaded.client_profile.system_lang_code == "ru-RU"


def test_legacy_client_profile_app_version_migrates_to_package_version(tmp_path) -> None:
    path = tmp_path / "config.json"
    path.write_text(
        """
        {
          "client_profile": {
            "device_model": "tg-api-zapret",
            "system_version": "Linux",
            "app_version": "tg-api-zapret"
          }
        }
        """,
        encoding="utf-8",
    )

    loaded = AppSettings.load(path)

    assert loaded.client_profile.app_version == OFFICIAL_DESKTOP_APP_VERSION


def test_app_settings_accounts_roundtrip(tmp_path) -> None:
    path = tmp_path / "config.json"

    AppSettings().with_account("work account").save(path)
    loaded = AppSettings.load(path)

    assert loaded.active_account == "work_account"
    assert loaded.accounts == ["default", "work_account"]


def test_partial_service_settings_uses_safety_defaults(tmp_path) -> None:
    path = tmp_path / "config.json"
    path.write_text('{"service":{"rate_limit_per_minute":10}}', encoding="utf-8")

    loaded = AppSettings.load(path)

    assert loaded.service.rate_limit_per_minute == 10
    assert loaded.service.blocked_account_names == ["string", "account"]
    assert loaded.service.telegram_min_action_interval_seconds == 1.25
    assert loaded.service.telegram_safe_mode is True
    assert loaded.service.telegram_serialize_account_actions is True
    assert loaded.service.telegram_send_actions_per_minute == 6
    assert loaded.service.telegram_raw_actions_per_minute == 3
    assert loaded.service.telegram_join_actions_per_hour == 5
    assert loaded.service.telegram_destructive_actions_per_hour == 10
    assert loaded.service.telegram_default_flood_cooldown_seconds == 300
    assert loaded.service.telegram_requests_per_second == 10
    assert loaded.service.telegram_requests_per_minute == 50
    assert loaded.service.telegram_requests_per_hour == 500
    assert loaded.service.telegram_read_requests_per_second == 5
    assert loaded.service.telegram_send_requests_per_second == 2
    assert loaded.service.telegram_typing_requests_per_second == 1
    assert loaded.service.telegram_sync_requests_per_minute == 2
    assert loaded.service.queue_execute_in_api is True
    assert loaded.service.db_writer_queue_maxsize == 5000
    assert loaded.service.db_writer_locked_retries == 3
    assert loaded.service.db_writer_io_retries == 2
    assert loaded.service.db_writer_failed_alert_threshold == 10
    assert loaded.service.db_writer_dead_letter_max_records == 500
    assert loaded.service.db_writer_dead_letter_ttl_days == 30
    assert loaded.service.db_writer_degraded_queue_ratio == 0.8
    assert loaded.service.db_writer_drop_categories == ["diagnostics", "typing", "presence"]
    assert loaded.service.keep_accounts_online is False
    assert loaded.service.online_update_interval_seconds == 300
    assert loaded.service.online_update_min_interval_seconds == 300
    assert loaded.service.online_update_max_interval_seconds == 900
    assert loaded.service.activity_idle_min_seconds == 120
    assert loaded.service.activity_idle_max_seconds == 300
    assert loaded.service.online_debounce_min_seconds == 30
    assert loaded.service.online_debounce_max_seconds == 60
    assert loaded.service.auto_connect_accounts == []
    assert loaded.service.reconnect_enabled is True
    assert loaded.service.passive_update_receiver is True
    assert loaded.service.entity_cache_warmup_dialogs == 50
    assert loaded.service.entity_cache_warmup_min_dialogs == 40
    assert loaded.service.entity_cache_warmup_max_dialogs == 60
    assert loaded.service.require_connection_health_before_auth is True
    assert loaded.service.connection_health_cache_seconds == 30
    assert loaded.service.raw_updates_retention_days == 7
    assert loaded.service.flood_errors_retention_days == 30
    assert loaded.service.idempotency_retention_hours == 48
    assert loaded.service.idempotency_max_records == 10000
    assert loaded.service.idempotency_lease_seconds == 300
    assert loaded.service.idempotency_message_lease_seconds == 300
    assert loaded.service.idempotency_media_lease_seconds == 3600
    assert loaded.service.idempotency_large_file_lease_seconds == 7200
    assert loaded.service.idempotency_heartbeat_min_seconds == 30
    assert loaded.service.idempotency_heartbeat_max_seconds == 60
    assert loaded.service.idempotency_result_max_bytes == 1048576
    assert loaded.service.state_retention_min_interval_hours == 12
    assert loaded.service.state_retention_max_interval_hours == 24
    assert loaded.service.state_vacuum_interval_hours == 24

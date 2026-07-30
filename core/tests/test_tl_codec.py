from datetime import datetime, timezone

import pytest
from telethon.tl.types import InputPeerUser

from tg_api_zapret.config import AppSettings, ServiceSettings
from tg_api_zapret.tl_codec import build_tl_object, decode_tl_value, serialize_tl


@pytest.mark.asyncio
async def test_build_tl_object_from_json_constructor() -> None:
    value = await build_tl_object(
        "InputPeerUser",
        {"user_id": 123, "access_hash": 456},
    )

    assert isinstance(value, InputPeerUser)
    assert value.user_id == 123
    assert value.access_hash == 456


@pytest.mark.asyncio
async def test_decode_nested_list_and_bytes() -> None:
    value = await decode_tl_value(
        [
            {"_": "InputPeerUser", "user_id": 123, "access_hash": 456},
            {"_": "bytes", "base64": "YWJj"},
        ],
    )

    assert isinstance(value[0], InputPeerUser)
    assert value[1] == b"abc"


def test_serialize_tl_bytes_and_datetime() -> None:
    value = serialize_tl(
        {
            "payload": b"abc",
            "date": datetime(2026, 6, 18, 8, 0, tzinfo=timezone.utc),
        }
    )

    assert value["payload"] == {"_": "bytes", "base64": "YWJj"}
    assert value["date"]["_"] == "datetime"
    assert value["date"]["iso"] == "2026-06-18T08:00:00+00:00"


def test_service_settings_bot_token_accounts_roundtrip(tmp_path) -> None:
    path = tmp_path / "config.json"

    AppSettings(
        service=ServiceSettings(bot_token_accounts={"123:abc": "work account"})
    ).save(path)
    loaded = AppSettings.load(path)

    assert loaded.service.bot_token_accounts == {"123:abc": "work_account"}

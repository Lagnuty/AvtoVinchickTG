import asyncio
from types import SimpleNamespace

from fastapi import HTTPException
from fastapi.testclient import TestClient
from telethon.tl.types import User

from tg_api_zapret.api import (
    ApiState,
    DBWriteJob,
    create_app,
    normalize_username_entity,
    serialize_dialog,
    telegram_action_limit,
)
from tg_api_zapret.config import ServiceSettings
from tg_api_zapret.version import __version__


def test_docs_are_disabled_by_default(tmp_path) -> None:
    app = create_app(
        ApiState(config_file=str(tmp_path / "config.json"), session_file=str(tmp_path / "s.txt"))
    )
    client = TestClient(app)

    assert client.get("/health").status_code == 200
    version = client.get("/version")
    assert version.status_code == 200
    assert version.json()["version"] == __version__
    assert client.get("/docs").status_code == 404


def test_api_token_required_by_default(tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("TG_API_TOKEN", "secret")
    app = create_app(
        ApiState(config_file=str(tmp_path / "config.json"), session_file=str(tmp_path / "s.txt"))
    )
    client = TestClient(app)

    assert client.get("/accounts").status_code == 401
    response = client.get("/accounts", headers={"Authorization": "Bearer secret"})

    assert response.status_code == 200
    assert response.json()["accounts"] == ["default"]


def test_blocked_demo_account_name_is_rejected(tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("TG_API_TOKEN", "secret")
    app = create_app(
        ApiState(config_file=str(tmp_path / "config.json"), session_file=str(tmp_path / "s.txt"))
    )
    client = TestClient(app)

    response = client.post(
        "/accounts",
        headers={"Authorization": "Bearer secret"},
        json={"account": "string"},
    )

    assert response.status_code == 400
    assert "Unsafe demo account name" in response.json()["detail"]


def test_capabilities_show_full_rpc_methods(tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("TG_API_TOKEN", "secret")
    app = create_app(
        ApiState(config_file=str(tmp_path / "config.json"), session_file=str(tmp_path / "s.txt"))
    )
    client = TestClient(app)

    response = client.get("/capabilities", headers={"Authorization": "Bearer secret"})
    data = response.json()
    methods = data["interfaces"]["json_rpc"]["methods"]
    bot_methods = response.json()["interfaces"]["bot_api_compat"]["methods"]
    rest_endpoints = data["interfaces"]["rest"]["endpoints"]

    assert "messages.edit" in methods
    assert "media.send" in methods
    assert "messages.send_username" in methods
    assert "tl.construct" in methods
    assert "sendMessage" in bot_methods
    assert "getUpdates" in bot_methods
    assert "POST /accounts/connect" in rest_endpoints
    assert "GET /accounts/online" in rest_endpoints
    assert "GET /accounts/health" in rest_endpoints
    assert "GET /accounts/risk-status" in rest_endpoints
    assert "GET /version" in rest_endpoints
    assert "GET /queue/status" in data["interfaces"]["queue"]["endpoints"]
    assert data["interfaces"]["queue"]["execution_owner"] == "api_process"
    assert "POST /accounts/entity-cache/warm" in rest_endpoints
    assert "GET /accounts/entity-cache" in rest_endpoints
    assert "GET /accounts/sync-state" in rest_endpoints
    assert "POST /accounts/sync/difference" in rest_endpoints
    assert "POST /messages/list" in rest_endpoints
    assert "POST /messages/typing" in rest_endpoints
    assert "POST /messages/read" in rest_endpoints
    assert "POST /drafts/save" in rest_endpoints


def test_dialog_serializer_includes_username_and_input_entity() -> None:
    user = User(id=123, access_hash=456, username="alice", first_name="Alice")
    dialog = SimpleNamespace(
        id=123,
        name="Alice",
        title="Alice",
        entity=user,
        is_user=True,
        is_group=False,
        is_channel=False,
        unread_count=0,
    )

    serialized = serialize_dialog(dialog)

    assert serialized["username"] == "alice"
    assert serialized["access_hash"] == 456
    assert serialized["input_entity"]["_"] == "InputPeerUser"


def test_normalize_username_entity() -> None:
    assert normalize_username_entity("alice") == "@alice"
    assert normalize_username_entity("@alice") == "@alice"
    assert normalize_username_entity("https://t.me/alice") == "@alice"
    assert normalize_username_entity("+79990000000") == "+79990000000"


def test_risk_status_endpoint_exposes_safe_limits(tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("TG_API_TOKEN", "secret")
    app = create_app(
        ApiState(config_file=str(tmp_path / "config.json"), session_file=str(tmp_path / "s.txt"))
    )
    client = TestClient(app)

    response = client.get("/accounts/risk-status", headers={"Authorization": "Bearer secret"})

    assert response.status_code == 200
    data = response.json()
    assert data["accounts"]["default"]["safe_mode"] is True
    assert data["limits"]["telegram_send_actions_per_minute"] == 6


def test_telegram_action_limits_are_risk_weighted() -> None:
    service = ServiceSettings()

    assert telegram_action_limit(service, "messages.send") == (6, 60)
    assert telegram_action_limit(service, "raw.invoke") == (3, 60)
    assert telegram_action_limit(service, "chats.join") == (5, 3600)
    assert telegram_action_limit(service, "admin.ban") == (10, 3600)


def test_connect_enters_locked_path_without_recursive_connect(tmp_path, monkeypatch) -> None:
    state = ApiState(config_file=str(tmp_path / "config.json"), session_file=str(tmp_path / "s.txt"))
    sentinel = object()

    async def fake_connect_locked(account_name: str):
        assert account_name == "default"
        assert state.connection_lock("default").locked()
        return sentinel

    monkeypatch.setattr(state, "_connect_locked", fake_connect_locked)

    assert asyncio.run(state.connect("default")) is sentinel


def test_idempotency_persists_and_validates_payload_hash(tmp_path) -> None:
    config_file = tmp_path / "config.json"
    state = ApiState(config_file=str(config_file), session_file=str(tmp_path / "s.txt"))

    status, payload_hash, cached = state.begin_idempotent_action(
        "default",
        "messages.send",
        "key-1",
        {"text": "hello"},
    )
    assert status == "started"
    assert cached is None
    state.complete_idempotent_action(
        "default",
        "messages.send",
        "key-1",
        payload_hash,
        {"id": 123, "text": "hello"},
    )
    state.close_state_db()

    restarted = ApiState(config_file=str(config_file), session_file=str(tmp_path / "s.txt"))
    status, _, cached = restarted.begin_idempotent_action(
        "default",
        "messages.send",
        "key-1",
        {"text": "hello"},
    )
    assert status == "completed"
    assert cached == {"id": 123, "text": "hello"}

    try:
        restarted.begin_idempotent_action(
            "default",
            "messages.send",
            "key-1",
            {"text": "different"},
        )
    except HTTPException as exc:
        assert exc.status_code == 409
    else:
        raise AssertionError("different payload must be rejected")


def test_idempotency_in_progress_lease_blocks_then_allows_retry(tmp_path) -> None:
    config_file = tmp_path / "config.json"
    state = ApiState(config_file=str(config_file), session_file=str(tmp_path / "s.txt"))

    status, _, _ = state.begin_idempotent_action(
        "default",
        "messages.send",
        "lease-key",
        {"text": "hello"},
    )
    assert status == "started"

    try:
        state.begin_idempotent_action(
            "default",
            "messages.send",
            "lease-key",
            {"text": "hello"},
        )
    except HTTPException as exc:
        assert exc.status_code == 409
        assert "in_progress" in exc.detail
    else:
        raise AssertionError("active lease must block duplicate request")

    with state.state_db_context() as connection:
        connection.execute(
            """
            update idempotency_keys
            set locked_until = 0
            where account = 'default' and action = 'messages.send' and idempotency_key = 'lease-key'
            """
        )

    status, _, _ = state.begin_idempotent_action(
        "default",
        "messages.send",
        "lease-key",
        {"text": "hello"},
    )
    assert status == "started"


def test_idempotency_outcome_unknown_requires_manual_resolution(tmp_path) -> None:
    state = ApiState(config_file=str(tmp_path / "config.json"), session_file=str(tmp_path / "s.txt"))

    status, payload_hash, _ = state.begin_idempotent_action(
        "default",
        "messages.send",
        "unknown-key",
        {"text": "hello"},
    )
    assert status == "started"
    state.mark_idempotent_action(
        "default",
        "messages.send",
        "unknown-key",
        payload_hash,
        "outcome_unknown",
    )
    with state.state_db_context() as connection:
        connection.execute(
            """
            update idempotency_keys
            set locked_until = 0
            where account = 'default' and action = 'messages.send' and idempotency_key = 'unknown-key'
            """
        )

    try:
        state.begin_idempotent_action(
            "default",
            "messages.send",
            "unknown-key",
            {"text": "hello"},
        )
    except HTTPException as exc:
        assert exc.status_code == 409
        assert "outcome_unknown" in exc.detail
    else:
        raise AssertionError("outcome_unknown must require manual resolution")

    state.resolve_idempotent_action("default", "messages.send", "unknown-key", "failed_retryable")
    status, _, _ = state.begin_idempotent_action(
        "default",
        "messages.send",
        "unknown-key",
        {"text": "hello"},
    )
    assert status == "started"


def test_idempotency_heartbeat_extends_lease(tmp_path) -> None:
    state = ApiState(config_file=str(tmp_path / "config.json"), session_file=str(tmp_path / "s.txt"))
    _, payload_hash, _ = state.begin_idempotent_action(
        "default",
        "media.send",
        "heartbeat-key",
        {"file_path": "small.jpg"},
    )
    with state.state_db_context() as connection:
        connection.execute(
            """
            update idempotency_keys
            set locked_until = 1
            where account = 'default' and action = 'media.send' and idempotency_key = 'heartbeat-key'
            """
        )

    state.refresh_idempotent_action(
        "default",
        "media.send",
        "heartbeat-key",
        payload_hash,
        lease_seconds=3600,
    )
    with state.state_db_context() as connection:
        after = connection.execute(
            """
            select locked_until from idempotency_keys
            where account = 'default' and action = 'media.send' and idempotency_key = 'heartbeat-key'
            """
        ).fetchone()[0]
    assert after > 1


def test_db_writer_rejects_enqueue_after_shutdown(tmp_path) -> None:
    state = ApiState(config_file=str(tmp_path / "config.json"), session_file=str(tmp_path / "s.txt"))

    def write_marker() -> str:
        return "ok"

    async def run() -> None:
        state.start_db_writer()
        assert await state.enqueue_db_write(write_marker) == "ok"
        await state.stop_db_writer()
        try:
            await state.enqueue_db_write(write_marker)
        except RuntimeError as exc:
            assert "shutting down" in str(exc)
        else:
            raise AssertionError("enqueue after shutdown must be rejected")

    asyncio.run(run())


def test_db_writer_drops_diagnostics_when_queue_is_full(tmp_path) -> None:
    state = ApiState(config_file=str(tmp_path / "config.json"), session_file=str(tmp_path / "s.txt"))
    state.db_write_queue = asyncio.Queue(maxsize=1)

    def write_marker() -> str:
        return "ok"

    async def run_drop() -> None:
        holder = asyncio.create_task(asyncio.sleep(3600))
        state.db_writer_task = holder
        state.db_writer_loop = asyncio.get_running_loop()
        state.db_writer_accepting = True
        state.db_writer_status["lifecycle"] = "running"
        state.db_write_queue.put_nowait(
            DBWriteJob(func=write_marker, args=(), kwargs={}, future=None)
        )
        await state.enqueue_db_write(write_marker, wait=False, category="diagnostics")
        assert state.db_writer_dropped_writes == 1
        assert state.db_writer_status["degraded"] is True
        holder.cancel()
        try:
            await holder
        except asyncio.CancelledError:
            pass

    asyncio.run(run_drop())

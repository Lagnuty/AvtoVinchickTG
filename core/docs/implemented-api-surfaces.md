# tg-api-zapret 0.4.29 implemented API surfaces

This document is the stable integration reference for applications that embed
tg-api-zapret as a Telegram MTProto core. Runtime truth is still exposed by
`GET /capabilities` and OpenAPI when `expose_docs=true`.

## Embedding Model

tg-api-zapret is designed to run as one owner process per session set. External
applications should treat it as a local or private network service and call it
through REST, JSON-RPC, WebSocket, SSE, Queue API, or the Python SDK.

Do not start a second worker process that opens the same Telegram `.session`
file. Queue jobs are executed by the API owner process so only one
`TelegramClient` owns an account connection at a time.

Recommended embedded topology:

- one tg-api-zapret API process owns Telegram clients and session files;
- application UI/backend calls tg-api-zapret over localhost or a private network;
- `TG_API_TOKEN` or `TG_API_TOKENS` protects every endpoint except `/health`;
- external clients use `account` query/body fields to select the Telegram account;
- background work uses `/queue/jobs`, but execution still remains centralized in
  the API process;
- WebSocket/SSE clients subscribe to updates, but do not run their own MTProto
  sync loops.

## Interfaces

- REST: direct HTTP endpoints for common Telegram and service operations.
- JSON-RPC: `POST /rpc` with methods from `RPC_METHODS`.
- WebSocket: `WS /ws/updates` for bidirectional update streaming.
- SSE: `GET /events` for one-way event streaming.
- Queue API: `POST /queue/jobs` and job status endpoints.
- Python SDK: `tg_api_zapret.sdk.TgApiZapretClient`.
- Bot API compatibility: `/bot{token}/{method}` for a limited compatibility set.
- Raw MTProto: `/raw/invoke` and `/mtproto/layers/{layer}/invoke`, disabled by
  default and intended for trusted admin use.

## Secure Defaults

Current defaults are production-oriented:

- `require_api_token=true`
- `expose_docs=false`
- `enable_raw_invoke=false`
- `enable_layer_invoke=false`
- `telegram_safe_mode=true`
- `telegram_serialize_account_actions=true`
- `keep_accounts_online=false`

Use `TG_API_TOKEN` for a single admin token, or `TG_API_TOKENS` for scoped tokens:

```bash
export TG_API_TOKEN='dev-admin-token'
export TG_API_TOKENS='{"work-token":["work"],"admin-token":["*"]}'
```

Scope `*` is required for admin recovery/maintenance operations such as
`POST /idempotency/resolve`, `POST /db/vacuum/migrate`, and
`POST /accounts/sync/difference?recovery=true`.

## REST Endpoints

### Service and Discovery

- `GET /health`
- `GET /capabilities`
- `GET /config`
- `GET /app/settings`
- `PUT /app/settings`
- `PATCH /app/settings`
- `PUT /config/proxy`
- `PUT /config/client-profile`
- `GET /compat/reverse-proxy`

`GET /health` returns `503` with `status=degraded` when the internal DB writer is
degraded or above the configured failure threshold. This is intentional readiness
behavior for embedding.

### Accounts and Auth

- `GET /accounts`
- `POST /accounts`
- `POST /accounts/connect`
- `POST /accounts/disconnect`
- `GET /accounts/online`
- `GET /accounts/health`
- `GET /accounts/risk-status`
- `POST /accounts/entity-cache/warm`
- `GET /accounts/entity-cache`
- `GET /accounts/sync-state`
- `POST /accounts/sync/difference?recovery=true`
- `GET /auth/status`
- `POST /auth/send-code`
- `POST /auth/confirm-code`
- `POST /auth/password`
- `GET /me`

Auth is incremental: send code, confirm code, then submit 2FA password only when
Telegram requires it. Sessions are persisted by the selected session backend and
should survive process restarts.

Manual difference is an admin recovery endpoint. Normal sync is handled by
Telethon; do not poll `GetDifference` from embedded clients.

### Messages, Dialogs, Entities

- `GET /dialogs`
- `GET /messages/{entity}`
- `POST /messages/list`
- `POST /messages/send`
- `POST /messages/send-username`
- `POST /messages/edit`
- `POST /messages/delete`
- `POST /messages/forward`
- `POST /messages/history/delete`
- `POST /messages/reaction`
- `POST /messages/typing`
- `POST /messages/read`
- `POST /drafts/save`
- `POST /entities/resolve`

Entities can be passed as usernames, phone numbers, t.me links, ids already known
to Telethon, or JSON TL objects with access hashes. `/dialogs` returns
`username`, `access_hash`, and `input_entity` when available; embedded clients
should prefer usernames for starting new chats and preserve `input_entity` when
only numeric ids are available.

### Media and Files

- `POST /media/send`
- `POST /media/download`
- `POST /media/download/stream`
- `POST /files/upload`

For large downloads use `/media/download/stream` or server-side `output_path`
where the API process can write. Base64 mode is portable but slower and more
memory intensive.

### Chats, Stories, Admin Actions

- `POST /chats/join`
- `POST /chats/leave`
- `POST /stories/get`
- `POST /stories/send`
- `POST /admin/ban`
- `POST /admin/promote`

These endpoints are rate-limited by Telegram action class. Destructive and join
operations have stricter defaults than reads.

### TL and Raw MTProto

- `POST /tl/construct`
- `POST /raw/invoke`
- `GET /mtproto/layers/{layer}/functions`
- `POST /mtproto/layers/{layer}/invoke`

`/tl/construct` builds Telethon TL objects from JSON. `/raw/invoke` and layer
invoke accept request names and JSON fields resolved through the TL codec. Raw
invoke and layer invoke are disabled by default.

### Queue, Idempotency, Maintenance

- `POST /queue/jobs`
- `GET /queue/jobs`
- `GET /queue/jobs/{job_id}`
- `GET /queue/status`
- `GET /db/writer/status`
- `GET /db/maintenance/status`
- `POST /db/vacuum/migrate`
- `POST /idempotency/resolve`

The DB writer has lifecycle states `starting`, `running`, `stopping`, `stopped`.
Its queue is bounded, exposes queue fill ratio, enters degraded state above the
configured threshold, and stores bounded dead-letter metadata without sensitive
payloads.

SQLite auto-vacuum migration is explicit. Startup only reports
`migration_required`; `POST /db/vacuum/migrate` checks free disk space before
running full `VACUUM`.

### Action Resolver

- `POST /actions/resolve`
- `POST /actions/execute`

The action resolver chooses the interface for a client task: REST for simple
request/response, Queue API for background jobs, SSE/WebSocket for realtime
streams, and JSON-RPC when a method-oriented interface is requested.

### Bot API Compatibility

- `GET /bot{token}/{method}`
- `POST /bot{token}/{method}`

Implemented compatibility methods:

- `getMe`
- `getUpdates`
- `sendMessage`
- `sendPhoto`
- `sendDocument`
- `editMessageText`
- `deleteMessage`

This is not a full Telegram Bot API proxy. Unsupported Bot API methods should be
implemented with native REST wrappers, JSON-RPC, or explicitly enabled raw
MTProto.

## JSON-RPC Methods

`POST /rpc` supports:

- `accounts.list`
- `auth.status`
- `dialogs.list`
- `entities.resolve`
- `media.send`
- `messages.delete`
- `messages.edit`
- `messages.forward`
- `messages.send`
- `messages.send_username`
- `raw.invoke`
- `tl.construct`

JSON-RPC responses are stable JSON and use the same serializers as REST.

## TL JSON Codec

Implemented in `tg_api_zapret/tl_codec.py`.

Supported JSON forms:

- constructor objects: `{"_":"InputPeerUser","user_id":1,"access_hash":2}`
- nested objects and lists;
- bytes: `{"_":"bytes","base64":"..."}`
- dates: `{"_":"datetime","iso":"2026-07-30T12:00:00Z"}`
- flags/optional fields through Telethon constructor kwargs;
- entity fields such as `{"peer":"@username"}` resolved with Telethon
  `get_input_entity`/`get_entity` when a client is available.

Responses use `serialize_tl` so bytes, dates, TL objects, lists, dicts and
primitive values are JSON-safe.

## Idempotency

Idempotency is persistent in SQLite and compares a stable payload hash for every
reused key. Different payload with the same key returns `409 Conflict`.

States:

- `in_progress` - request is running; duplicate calls are blocked while lease is active.
- `completed` - cached stable JSON result is returned for the same key and payload.
- `failed_retryable` - admin explicitly allows retry.
- `failed_final` - key is closed and must not be retried.
- `outcome_unknown` - server cannot prove whether Telegram applied the operation;
  clients must not retry automatically.

Lease defaults:

- generic: `idempotency_lease_seconds=300`
- message send: `idempotency_message_lease_seconds=300`
- media upload/download: `idempotency_media_lease_seconds=3600`
- large file: `idempotency_large_file_lease_seconds=7200`
- heartbeat interval: `idempotency_heartbeat_min_seconds=30`,
  `idempotency_heartbeat_max_seconds=60`

Long operations refresh `locked_until` with a heartbeat and cancel the heartbeat
when completed or failed.

Manual resolution example:

```bash
curl -X POST http://127.0.0.1:8080/idempotency/resolve \
  -H 'Authorization: Bearer admin-token' \
  -H 'Content-Type: application/json' \
  -d '{"account":"work","action":"messages.send","idempotency_key":"key-1","status":"failed_retryable"}'
```

## Queue Semantics

Memory backend is for local development. Redis backend stores jobs durably, but
Telegram jobs are still executed by the API owner process.

Redis job fields include:

- `id`
- `kind`
- `account`
- `payload`
- `status`
- `idempotency_key`
- `attempts`
- `max_attempts`
- `leased_until`
- `result`
- `error`

Expired leases are requeued until `max_attempts`, then moved to `dead_letter`.

## Python SDK

Use `TgApiZapretClient` for native core API calls:

```python
from tg_api_zapret import TgApiZapretClient

client = TgApiZapretClient("http://127.0.0.1:8080", token="dev-admin-token")
print(client.health())
print(client.dialogs(account="work", limit=20))
client.send_message("me", "hello", account="work")
```

Use `BotApiAdapter` only for the limited compatibility surface:

```python
bot = client.bot_api("123456:token")
bot.send_message("@username", "hello")
```

## Configuration Groups

The service config is available at `GET /app/settings` and can be changed with
`PUT /app/settings` or `PATCH /app/settings`.

Important groups:

- API exposure: `api_name`, `public_base_url`, `default_api_interface`,
  `enabled_interfaces`, `expose_docs`, `cors_origins`
- auth: `require_api_token`, `api_token_env`, `api_tokens_env`,
  `bot_token_accounts`
- privileged MTProto: `enable_raw_invoke`, `enable_layer_invoke`
- Telegram guardrails: `telegram_safe_mode`, `telegram_serialize_account_actions`,
  `telegram_*_per_*`, `telegram_min_action_interval_seconds`
- queue: `queue_visibility_timeout_seconds`, `queue_default_max_attempts`,
  `queue_execute_in_api`
- DB writer: `db_writer_queue_maxsize`, `db_writer_locked_retries`,
  `db_writer_io_retries`, `db_writer_failed_alert_threshold`,
  `db_writer_dead_letter_max_records`, `db_writer_dead_letter_ttl_days`,
  `db_writer_degraded_queue_ratio`, `db_writer_drop_categories`
- idempotency: `idempotency_retention_hours`, `idempotency_max_records`,
  `idempotency_lease_seconds`, `idempotency_message_lease_seconds`,
  `idempotency_media_lease_seconds`, `idempotency_large_file_lease_seconds`,
  `idempotency_heartbeat_min_seconds`, `idempotency_heartbeat_max_seconds`,
  `idempotency_result_max_bytes`
- connection lifecycle: `auto_connect_accounts`, `reconnect_enabled`,
  `reconnect_min_delay_seconds`, `reconnect_max_delay_seconds`,
  `passive_update_receiver`
- presence lifecycle: `keep_accounts_online`, `activity_idle_min_seconds`,
  `activity_idle_max_seconds`, `online_debounce_min_seconds`,
  `online_debounce_max_seconds`
- local state: `entity_cache_warmup_*`, `raw_updates_retention_days`,
  `flood_errors_retention_days`, `state_retention_*`, `state_vacuum_interval_hours`

## MTProto Definition Documents

Generated reference files:

- `docs/mtproto-definitions.md`
- `docs/mtproto-definitions.json`
- `docs/mtproto-functions.md`
- `docs/mtproto-functions.json`
- `docs/mtproto-importance-layers.md`
- `docs/mtproto-importance-layers.json`
- `docs/implemented-mtproto-layer-functions.md`
- `docs/implemented-mtproto-layer-functions.json`

Regenerate them after Telethon schema changes:

```bash
python scripts/generate_mtproto_docs.py
python scripts/generate_mtproto_importance_layers.py
python scripts/generate_implemented_layer_report.py
```

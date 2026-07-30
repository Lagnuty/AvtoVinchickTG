# Embedding tg-api-zapret as an application core

This guide is for developers who want to embed tg-api-zapret inside another
application as the Telegram connectivity core.

## Architecture

Run tg-api-zapret as a single owner process for a set of Telegram sessions. The
host application communicates with it over a private API boundary:

```text
Host application UI/backend
        |
        | REST / JSON-RPC / Queue / WebSocket / SSE / Python SDK
        v
tg-api-zapret API owner process
        |
        | Telethon / MTProto
        v
Telegram
```

The owner process is responsible for:

- opening and locking `.session` files;
- maintaining account connections;
- serializing Telegram actions per account when safe mode is enabled;
- writing local state through the DB writer;
- executing Queue API jobs centrally;
- exposing health/readiness for supervisors.

## Process Rules

- Start one API owner process per session directory or session database.
- Do not run separate Telegram queue workers against the same sessions.
- Keep session files, SQLite files, exports, and logs outside the source tree.
- Put the API behind localhost, a Unix socket proxy, VPN, or private network.
- Set `TG_API_TOKEN` or scoped `TG_API_TOKENS` before exposing anything beyond
  local development.

Example:

```bash
export TG_API_TOKEN='dev-admin-token'
python -m tg_api_zapret \
  --session-db ~/.config/tg-api-zapret/sessions.sqlite3 \
  --account default \
  api --host 127.0.0.1 --port 8080
```

With Redis Queue metadata:

```bash
export TG_API_TOKEN='dev-admin-token'
export TG_API_QUEUE_BACKEND=redis
export REDIS_URL=redis://127.0.0.1:6379/0
python -m tg_api_zapret api --host 127.0.0.1 --port 8080
```

Telegram jobs still execute in the API owner process.

## Dependency Profiles

The package is split for embedded builds:

- core install: `Telethon`, `PySocks`, `python-socks`;
- server extra: FastAPI, Uvicorn, Redis client;
- dev extra: server extra plus test/lint tooling.

Use core-only dependencies for GUI/exe builds that call `TelegramLayer`
directly:

```bash
python -m pip install -e .
# or
python -m pip install -r requirements-core.txt
```

Use server dependencies when the process exposes REST, JSON-RPC, WebSocket, SSE
or Queue API:

```bash
python -m pip install -e ".[server]"
# or
python -m pip install -r requirements-server.txt
```

## API Boundary

Use the narrowest interface that matches the task:

- REST for normal request/response operations;
- JSON-RPC when a method-oriented client is easier to generate;
- Queue API for background jobs;
- WebSocket or SSE for update streams;
- Python SDK for Python host applications;
- Bot API compatibility only for the limited supported method set;
- raw MTProto only for trusted admin/internal tools.

The action resolver can choose an interface for a higher-level task:

```bash
curl -X POST http://127.0.0.1:8080/actions/resolve \
  -H 'Authorization: Bearer dev-admin-token' \
  -H 'Content-Type: application/json' \
  -d '{"task":"send message","account":"work","params":{"entity":"me","text":"hello"}}'
```

## Account Lifecycle

Create/select accounts with `POST /accounts` or CLI `use-account`.

Login flow:

1. `POST /auth/send-code`
2. `POST /auth/confirm-code`
3. `POST /auth/password` only if Telegram requires 2FA

Connection flow:

1. `POST /accounts/connect` to open an authorized account.
2. `GET /accounts/online` to inspect connection/runtime state.
3. `POST /accounts/disconnect` to close it.

Use `auto_connect_accounts` to restore selected accounts on API startup.

For direct Python embedding, GUI code can use typed result helpers instead of
parsing exception text:

```python
from tg_api_zapret import TelegramLayer, validate_proxy_url_result

proxy = validate_proxy_url_result("socks5h://127.0.0.1:1080")
if not proxy.ok:
    show_proxy_error(proxy.error_type, proxy.message)

health = await layer.check_connection_result()
if health.ok:
    sent = await layer.send_code_result("+79990000000")
    if sent.ok and sent.sent_code:
        confirmed = await layer.sign_in_result(sent.sent_code, code)
        if confirmed.password_required:
            await layer.sign_in_password_result(password)
```

HTTP auth uses the same policy: when
`require_connection_health_before_auth=true`, `POST /auth/send-code` first
checks the Telegram connection through the configured proxy and blocks the code
request if the connection is unhealthy.

## Entity Handling

Embedded clients should avoid inventing peer ids. Prefer:

- username: `@username`
- t.me links
- phone numbers known to the account
- `input_entity` objects returned by `/dialogs` or `/entities/resolve`

If the UI shows dialogs from `/dialogs`, store the `input_entity` field for later
message and media calls. Numeric ids alone may be insufficient because Telegram
often requires `access_hash`.

## Idempotency Contract

Use `idempotency_key` for operations that can create side effects:

- `POST /messages/send`
- `POST /messages/send-username`
- `POST /media/send`
- JSON-RPC equivalents

Rules:

- same key and same payload returns the cached result after completion;
- same key with different payload returns `409 Conflict`;
- `in_progress` blocks duplicates while the lease is active;
- long operations refresh the lease by heartbeat;
- `outcome_unknown` must not be retried automatically;
- admin can resolve unknown/final keys with `POST /idempotency/resolve`.

Client retry policy:

- retry transport failures only when the server did not accept the request;
- if the API returns `outcome_unknown` or `409`, surface it to an operator or
  reconciliation workflow;
- do not generate a new idempotency key for the same user-visible action unless
  the user explicitly repeats it.

## Health and Readiness

Use these endpoints in supervisors:

- `GET /health`
- `GET /version`
- `GET /queue/status`
- `GET /db/writer/status`
- `GET /db/maintenance/status`
- `GET /accounts/health`
- `GET /accounts/risk-status`

`GET /health` returns `503` when DB writer health is degraded. This should remove
the process from readiness/load-balancer rotation, but does not necessarily mean
the process must be killed immediately.

`GET /version` is intentionally available without an API token. Launchers and
host applications should use it for compatibility/update checks instead of
reading `tg_api_zapret/version.py`.

## DB Writer and Local State

Local state is persisted through a bounded DB writer queue. Important behavior:

- critical writes wait when the queue is full;
- diagnostics/presence/typing categories may be dropped when configured;
- failed writes are counted and exposed in health;
- dead-letter metadata is bounded and avoids sensitive payloads;
- disk-full stops the writer and fails pending writes visibly.

SQLite full `VACUUM` is not run automatically at startup. Check:

```bash
curl http://127.0.0.1:8080/db/maintenance/status \
  -H 'Authorization: Bearer dev-admin-token'
```

Run explicit migration only during maintenance:

```bash
curl -X POST http://127.0.0.1:8080/db/vacuum/migrate \
  -H 'Authorization: Bearer dev-admin-token'
```

## Security Boundary

Default settings are restrictive. Keep them for embedded production:

- `require_api_token=true`
- `expose_docs=false`
- `enable_raw_invoke=false`
- `enable_layer_invoke=false`
- `telegram_safe_mode=true`

Use scoped tokens:

```bash
export TG_API_TOKENS='{"work-token":["work"],"admin-token":["*"]}'
```

Only admin scope `*` should be allowed to:

- change global app settings;
- enable raw/layer invoke;
- run manual difference recovery;
- resolve idempotency keys;
- run DB vacuum migration.

`bot_token_accounts` is currently stored in the local JSON config for compatibility
with existing launchers. Treat the config file as secret material, keep it outside
the source tree with owner-only permissions, and migrate host applications to an
OS credential store or encrypted secret provider when available.

## Upgrade Checklist

For every tg-api-zapret update:

1. bump `tg_api_zapret/version.py` and `pyproject.toml`;
2. update `README.md`;
3. update `docs/implemented-api-surfaces.md`;
4. update this integration guide when process/API contracts change;
5. regenerate MTProto definition docs after Telethon schema changes;
6. run tests in an environment with project dependencies installed.

# tg-api-zapret

Асинхронная прослойка для подключения к Telegram через MTProto. Низкоуровневую часть
протокола выполняет Telethon, а этот пакет дает единый слой для конфигурации,
авторизации, хранения сессий и типовых операций.

## Возможности

- конфигурация официального desktop-клиента Telegram по умолчанию;
- хранение `StringSession` в файле, переменной окружения, строке или SQLite;
- первичная авторизация по телефону, коду и 2FA-паролю;
- повторное подключение без повторной авторизации;
- высокоуровневые методы `send_message`, `get_dialogs`, `iter_messages`, `stream_updates`;
- raw RPC через `invoke`;
- HTTP, HTTPS, SOCKS5 и SOCKS5H proxy через `TELEGRAM_PROXY_URL`.

## Установка на Ubuntu

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
```

For embedded applications and lighter exe builds, install only the core package:

```bash
python -m pip install -e .
# or, without editable install:
python -m pip install -r requirements-core.txt
```

Install the HTTP API/server extras only when this process must expose REST,
JSON-RPC, WebSocket, SSE or Queue API:

```bash
python -m pip install -e ".[server]"
python -m pip install -r requirements-server.txt
```

Если проект запускается прямо из папки без установки пакета, поставьте runtime-зависимости:

```bash
python -m pip install -r requirements.txt
```

Для прокси Telethon 1.44 требует пакет `python-socks`:

```bash
python -m pip install "python-socks[asyncio]>=2.4,<3.0"
```

## Переменные окружения

```bash
export TELEGRAM_API_ID=2040
export TELEGRAM_API_HASH=b18441a1ff607e10a989891a5462e627
# опционально:
export TELEGRAM_PROXY_URL=socks5://user:password@127.0.0.1:1080
```

Если переменные `TELEGRAM_API_ID` и `TELEGRAM_API_HASH` не заданы, используются
значения desktop-клиента из технического задания.

## Первичная авторизация

```bash
python -m tg_api_zapret --session-file ~/.config/tg-api-zapret/session.txt login
```

Программа последовательно спросит номер телефона, код подтверждения и, если на
аккаунте включена двухэтапная проверка, 2FA-пароль. После успешного входа session
string будет сохранена в файл с правами `0600`.
На следующих запусках код подтверждения больше не нужен.

Номер также можно передать сразу:

```bash
python -m tg_api_zapret --session-file ~/.config/tg-api-zapret/session.txt login +79990000000
```

Сессия сохраняется и не должна теряться при перезапуске, если запускать программу
от того же Linux-пользователя и с тем же `--session-file`. По умолчанию это:

```text
~/.config/tg-api-zapret/session.txt
```

## Несколько аккаунтов

Аккаунты именуются произвольно. Активный аккаунт хранится в config-файле.

Создать или переключить активный аккаунт:

```bash
python -m tg_api_zapret use-account work
```

Залогиниться в выбранный аккаунт:

```bash
python -m tg_api_zapret --account work login
```

Посмотреть аккаунты:

```bash
python -m tg_api_zapret accounts
```

В файловом режиме сессии хранятся так:

- `default` - `~/.config/tg-api-zapret/session.txt`
- остальные - `~/.config/tg-api-zapret/sessions/<account>.session.txt`

Пример обращения к разным аккаунтам:

```bash
python -m tg_api_zapret --account work dialogs
python -m tg_api_zapret --account personal send me "hello"
```

Проверка:

```bash
python -m tg_api_zapret --session-file ~/.config/tg-api-zapret/session.txt status
```

Отправка сообщения:

```bash
python -m tg_api_zapret --session-file ~/.config/tg-api-zapret/session.txt send me "test message"
```

## Использование как библиотеки

```python
import asyncio

from tg_api_zapret import FileSessionBackend, TelegramConfig, TelegramLayer


async def main() -> None:
    layer = TelegramLayer(
        TelegramConfig.from_env(),
        FileSessionBackend("telegram.session.txt"),
    )
    async with layer.lifespan():
        await layer.send_message("me", "Hello")


asyncio.run(main())
```

For GUI integrations, use typed result helpers when the UI should branch without
parsing exception text:

```python
from tg_api_zapret import validate_proxy_url_result

proxy = validate_proxy_url_result("socks5h://127.0.0.1:1080")
if not proxy.ok:
    print(proxy.error_type, proxy.message)

health = await layer.check_connection_result()
sent = await layer.send_code_result("+79990000000")
if health.ok and sent.ok and sent.sent_code:
    confirmed = await layer.sign_in_result(sent.sent_code, "12345")
    if confirmed.password_required:
        await layer.sign_in_password_result("2fa-password")
```

## SQLite-хранилище сессии

```bash
python -m tg_api_zapret --session-db ~/.config/tg-api-zapret/sessions.sqlite3 --session-key main login
```

## Интерактивное меню

```bash
python -m tg_api_zapret --menu
```

В меню можно запустить прослойку и авторизацию, проверить статус, отправить
сообщение, вывести диалоги, указать прокси, поменять имя клиента или запустить
HTTP API.

## Имя в авторизованных приложениях Telegram

По умолчанию прослойка авторизуется с `device_model=Telegram Desktop` и
`app_version`, равным актуальной версии Telegram Desktop. Это имя Telegram обычно
показывает в списке активных устройств.

Изменить профиль клиента:

```bash
python -m tg_api_zapret set-client-profile \
  --device-model "Telegram Desktop" \
  --system-version "Linux 5.15 x86_64" \
  --app-version 7.0.4
```

Для уже существующей сессии Telegram может оставить старое название. Надежный
способ увидеть новое имя в активных устройствах - задать профиль до первого
логина или перелогиниться.

Версия приложения ведется в `tg_api_zapret/version.py` и дублируется в
`pyproject.toml`. При каждом обновлении проекта номер версии нужно повышать.

## Прокси для Telegram

Прокси можно сохранить в конфиге приложения:

```bash
python -m tg_api_zapret set-proxy socks5h://127.0.0.1:1080
```

Поддерживаемые схемы:

- `http://host:port`
- `https://host:port`
- `socks5://host:port`
- `socks5h://host:port`
- `socks5://user:password@host:port`
- `socks5h://user:password@host:port`

`socks5h` включает разрешение доменов через прокси. `socks5`
оставляет DNS на стороне машины, где запущена программа.

Посмотреть текущую настройку:

```bash
python -m tg_api_zapret show-config
```

Удалить прокси:

```bash
python -m tg_api_zapret clear-proxy
```

Переменная окружения `TELEGRAM_PROXY_URL` тоже поддерживается, но сохраненный
прокси из config-файла имеет приоритет.

## HTTP API

Current secure defaults:

- `require_api_token=true`; set `TG_API_TOKEN` or `TG_API_TOKENS` before calling any endpoint except `/health`.
- `expose_docs=false`; `/docs`, `/redoc`, and `/openapi.json` are hidden until enabled in `/app/settings`.
- `enable_raw_invoke=false` and `enable_layer_invoke=false`; enable them explicitly only for trusted admin use.
- `GET /dialogs` includes `username`, `access_hash`, and `input_entity` when Telethon has enough data. Clients should prefer `username`; if only a numeric id is available, use `input_entity` so `access_hash` is preserved.

Full integration references:

- `docs/implemented-api-surfaces.md` - complete API surface and runtime semantics.
- `docs/core-integration.md` - embedding tg-api-zapret as the Telegram core of another application.

Minimal local run:

```bash
export TG_API_TOKEN='dev-admin-token'
python -m tg_api_zapret api --host 127.0.0.1 --port 8080
```

Existing native Telethon `.session` files can be used directly as the default account:

```bash
export TG_API_TOKEN='dev-admin-token'
python -m tg_api_zapret --session-file '/opt/tg-api-zapret/sessions/241643392_telethon.session' api --host 0.0.0.0 --port 8081
curl http://127.0.0.1:8081/auth/status -H 'Authorization: Bearer dev-admin-token'
```

Start a new chat by username, even when the dialog is not in `/dialogs` yet:

```bash
curl -X POST http://127.0.0.1:8080/messages/send-username \
  -H 'Authorization: Bearer dev-admin-token' \
  -H 'Content-Type: application/json' \
  -d '{"username":"username_or_@username","text":"hello"}'
```

Keep an authorized account connected until API shutdown or explicit disconnect.
`keep_online` is an explicit option, not the default. The runtime also supports
startup auto-connect, reconnect loops, passive MTProto update receivers,
entity-cache warmup, and Telegram/proxy health checks before login code requests.
Related endpoints: `GET /accounts/health`, `POST /accounts/entity-cache/warm`,
`GET /accounts/entity-cache`.

```bash
curl -X POST http://127.0.0.1:8080/accounts/connect \
  -H 'Authorization: Bearer dev-admin-token' \
  -H 'Content-Type: application/json' \
  -d '{"account":"main","keep_online":true}'

curl http://127.0.0.1:8080/accounts/online \
  -H 'Authorization: Bearer dev-admin-token'
```

Запуск API:

```bash
python -m tg_api_zapret api --host 127.0.0.1 --port 8080
```

OpenAPI-документация будет доступна по адресу:

```text
http://127.0.0.1:8080/docs
```

Первые эндпоинты:

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
- `GET /health`
- `GET /version`
- `GET /capabilities`
- `GET /config`
- `PUT /config/proxy`
- `PUT /config/client-profile`
- `GET /auth/status`
- `POST /auth/send-code`
- `POST /auth/confirm-code`
- `POST /auth/password`
- `GET /me`
- `GET /dialogs`
- `GET /messages/{entity}`
- `POST /messages/send`
- `POST /messages/send-username`
- `POST /messages/edit`
- `POST /messages/delete`
- `POST /messages/forward`
- `POST /messages/history/delete`
- `POST /messages/reaction`
- `POST /media/send`
- `POST /media/download`
- `POST /media/download/stream`
- `POST /files/upload`
- `POST /entities/resolve`
- `POST /chats/join`
- `POST /chats/leave`
- `POST /stories/get`
- `POST /stories/send`
- `POST /admin/ban`
- `POST /admin/promote`
- `POST /tl/construct`
- `POST /raw/invoke`
- `GET /mtproto/layers/{layer}/functions`
- `POST /mtproto/layers/{layer}/invoke`
- `POST /rpc`
- `GET /events`
- `WS /ws/updates`
- `POST /queue/jobs`
- `GET /queue/jobs`
- `GET /queue/jobs/{job_id}`
- `GET /queue/status`
- `GET /db/writer/status`
- `GET /db/maintenance/status`
- `POST /db/vacuum/migrate`
- `POST /idempotency/resolve`
- `GET /capabilities`
- `POST /actions/resolve`
- `POST /actions/execute`
- `GET /compat/reverse-proxy`
- `GET /bot{token}/{method}`
- `POST /bot{token}/{method}`
- `GET /app/settings`
- `PUT /app/settings`
- `PATCH /app/settings`

Пример отправки сообщения:

```bash
curl -X POST http://127.0.0.1:8080/messages/send \
  -H 'Content-Type: application/json' \
  -d '{"entity":"me","text":"hello from API"}'
```

Выбор аккаунта в API делается query-параметром `account`:

```bash
curl 'http://127.0.0.1:8080/dialogs?account=work&limit=20'
curl -X POST 'http://127.0.0.1:8080/messages/send?account=personal' \
  -H 'Content-Type: application/json' \
  -d '{"entity":"me","text":"hello from personal"}'
```

`/raw/invoke` нужен как аварийный выход к TL-функциям Telethon, пока для нужной
операции еще нет отдельного удобного эндпоинта.

Полный список MTProto definitions из установленной TL-схемы Telethon:

- `docs/mtproto-definitions.md`
- `docs/mtproto-definitions.json`
- `docs/mtproto-importance-layers.md`
- `docs/mtproto-importance-layers.json`
- `docs/implemented-mtproto-layer-functions.md`
- `docs/implemented-mtproto-layer-functions.json`

В Telethon `1.44.0` сейчас получается `2344` definitions:

- `779` request-функций
- `1565` TL type constructors

Отдельный список только MTProto request-функций:

- `docs/mtproto-functions.md`
- `docs/mtproto-functions.json`

Пересоздать справочники:

```bash
python scripts/generate_mtproto_docs.py
python scripts/generate_mtproto_importance_layers.py
python scripts/generate_implemented_layer_report.py
```

Request-функции всех уровней 1-10 реализованы через ограниченный dispatcher:

```bash
curl http://127.0.0.1:8080/mtproto/layers/1/functions
curl http://127.0.0.1:8080/mtproto/layers/10/functions

curl -X POST 'http://127.0.0.1:8080/mtproto/layers/1/invoke?account=work' \
  -H 'Content-Type: application/json' \
  -d '{"request":"updates.GetStateRequest","kwargs":{}}'
```

## Automatic API Method Selection

Клиентское приложение может не выбирать REST/WebSocket/SSE/Queue вручную. Для
этого есть resolver:

```bash
curl -X POST http://127.0.0.1:8080/actions/resolve \
  -H 'Content-Type: application/json' \
  -d '{"task":"send message","account":"work","params":{"entity":"me","text":"hello"}}'
```

Ответ содержит рекомендуемый интерфейс, endpoint и причину выбора:

```json
{
  "action": "send_message",
  "interface": "rest",
  "endpoint": "POST /messages/send",
  "rpc_method": "messages.send",
  "reason": "Simple request/response command."
}
```

Если задачу нужно выполнить в фоне:

```bash
curl -X POST http://127.0.0.1:8080/actions/execute \
  -H 'Content-Type: application/json' \
  -d '{"task":"send message","account":"work","background":true,"params":{"entity":"me","text":"queued"}}'
```

Для realtime-задач resolver выберет SSE или WebSocket:

```bash
curl -X POST http://127.0.0.1:8080/actions/resolve \
  -H 'Content-Type: application/json' \
  -d '{"task":"new messages","account":"work","realtime":true}'
```

Python SDK тоже умеет выбирать метод:

```python
from tg_api_zapret import TgApiZapretClient

client = TgApiZapretClient()
plan = client.resolve_action(
    "send message",
    account="work",
    params={"entity": "me", "text": "hello"},
)
print(plan)

result = client.execute_action(
    "send message",
    account="work",
    params={"entity": "me", "text": "hello"},
)
print(result)
```

Список возможностей:

```bash
curl http://127.0.0.1:8080/capabilities
```

## Application Settings API

Настройки самого сервиса:

```bash
curl http://127.0.0.1:8080/app/settings
```

Изменить часть настроек:

```bash
curl -X PATCH http://127.0.0.1:8080/app/settings \
  -H 'Content-Type: application/json' \
  -d '{"default_api_interface":"json_rpc","stream_queue_size":250,"enabled_interfaces":["rest","json_rpc","queue","sse","websocket","python_sdk"]}'
```

Доступные настройки:

- `api_name` - имя сервиса.
- `public_base_url` - внешний URL сервиса, если есть reverse proxy.
- `default_api_interface` - интерфейс по умолчанию для `/actions/resolve`.
- `enabled_interfaces` - включенные интерфейсы: `rest`, `json_rpc`, `websocket`, `sse`, `queue`, `python_sdk`.
- `max_queue_jobs_list` - лимит выдачи списка задач для будущих backend-реализаций.
- `stream_queue_size` - размер буфера событий WebSocket/SSE.
- `request_timeout_seconds` - общий timeout для будущих долгих операций.
- `expose_docs` - флаг показа документации для будущего middleware.
- `cors_origins` - разрешенные origins для будущего CORS middleware.
- `require_api_token` и `api_token_env` - флаги авторизации API для будущего middleware.

В Python SDK:

```python
from tg_api_zapret import TgApiZapretClient

client = TgApiZapretClient()
print(client.app_settings())
client.update_app_settings(default_api_interface="json_rpc", stream_queue_size=250)
```

Current embedded-core settings groups:

- `require_api_token`, `api_token_env`, `api_tokens_env` - API auth and per-account token scopes.
- `enable_raw_invoke`, `enable_layer_invoke` - privileged raw MTProto switches.
- `telegram_safe_mode`, `telegram_serialize_account_actions`, `telegram_*` limits - Telegram action guardrails.
- `queue_visibility_timeout_seconds`, `queue_default_max_attempts`, `queue_execute_in_api` - Queue API behavior.
- `db_writer_queue_maxsize`, `db_writer_*_retries`, `db_writer_dead_letter_*`, `db_writer_degraded_queue_ratio` - DB writer lifecycle, retry, backpressure, dead-letter and degraded health.
- `idempotency_*` - persistent idempotency TTL, lease, heartbeat and cached result size limit.
- `activity_idle_*`, `online_debounce_*`, `keep_accounts_online` - presence lifecycle for real user activity.
- `auto_connect_accounts`, `reconnect_*`, `passive_update_receiver` - account connection lifecycle.
- `entity_cache_warmup_*`, `raw_updates_retention_days`, `flood_errors_retention_days`, `state_*` - local cache, retention and SQLite maintenance.

## Security Settings

Production-режим с токенами, scopes, audit log и отключенными опасными вызовами:

```bash
export TG_API_TOKEN='dev-admin-token'
export TG_API_TOKENS='{"work-token":["work"],"admin-token":["*"]}'

curl -X PATCH http://127.0.0.1:8080/app/settings \
  -H 'Content-Type: application/json' \
  -d '{
    "require_api_token": true,
    "api_token_env": "TG_API_TOKEN",
    "api_tokens_env": "TG_API_TOKENS",
    "rate_limit_per_minute": 120,
    "audit_log_path": "~/.config/tg-api-zapret/audit.jsonl",
    "enable_raw_invoke": false,
    "enable_layer_invoke": false,
    "expose_docs": false
  }'
```

Запросы после этого:

```bash
curl http://127.0.0.1:8080/dialogs?account=work \
  -H 'Authorization: Bearer work-token'
```

Scopes:

- `["work"]` - токен видит и использует только аккаунт `work`.
- `["personal","work"]` - доступ к двум аккаунтам.
- `["*"]` - полный доступ.

Опасные возможности не удалены. Их можно включить обратно:

```bash
curl -X PATCH http://127.0.0.1:8080/app/settings \
  -H 'Authorization: Bearer admin-token' \
  -H 'Content-Type: application/json' \
  -d '{"enable_raw_invoke":true,"enable_layer_invoke":true}'
```

Audit log пишет JSONL без body, кодов, паролей, session strings и proxy password.

## Telegram Risk Controls

These defaults do not guarantee that Telegram will not limit an account. They are guardrails
that make API clients behave less like a bursty script:

- `telegram_safe_mode=true`
- `telegram_serialize_account_actions=true`
- `telegram_min_action_interval_seconds=1.25`
- `telegram_send_actions_per_minute=6`
- `telegram_resolve_actions_per_minute=10`
- `telegram_raw_actions_per_minute=3`
- `telegram_join_actions_per_hour=5`
- `telegram_destructive_actions_per_hour=10`
- `telegram_default_flood_cooldown_seconds=300`

Check active cooldowns and current limits:

```bash
curl http://127.0.0.1:8080/accounts/risk-status \
  -H 'Authorization: Bearer admin-token'
```

If Telegram returns `FloodWait`, the API stores an account cooldown and returns `429` with
`Retry-After` instead of continuing to hammer MTProto.

## WebSocket API

Поток новых сообщений:

```text
ws://127.0.0.1:8080/ws/updates?account=work
```

Каждое событие приходит JSON-сообщением.

## SSE API

Односторонний поток событий через Server-Sent Events:

```bash
curl -N 'http://127.0.0.1:8080/events?account=work'
```

## JSON-RPC API

Один endpoint для команд:

```bash
curl -X POST http://127.0.0.1:8080/rpc \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"messages.send","params":{"account":"work","entity":"me","text":"hello"}}'
```

Поддерживаемые методы:

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

## Queue API

In-memory очередь фоновых задач:

```bash
curl -X POST http://127.0.0.1:8080/queue/jobs \
  -H 'Content-Type: application/json' \
  -d '{"kind":"messages.send","account":"work","payload":{"entity":"me","text":"queued hello"}}'
```

Проверить задачу:

```bash
curl http://127.0.0.1:8080/queue/jobs/<job_id>
```

DB writer health and failed asynchronous writes:

```bash
curl http://127.0.0.1:8080/db/writer/status
```

Idempotency states:

- `in_progress` - the request is still running and duplicate calls are blocked while the lease is active.
- `completed` - the previous stable JSON result is returned for the same key and payload.
- `failed_retryable` - an admin explicitly allowed retry; the next matching call may run again.
- `failed_final` - the key is closed and should not be retried.
- `outcome_unknown` - the server cannot prove whether Telegram applied the action; do not retry automatically.

Admin resolution for an unknown/final idempotency key:

```bash
curl -X POST http://127.0.0.1:8080/idempotency/resolve \
  -H 'Authorization: Bearer admin-token' \
  -H 'Content-Type: application/json' \
  -d '{"account":"work","action":"messages.send","idempotency_key":"key-1","status":"failed_retryable"}'
```

SQLite maintenance status and explicit auto-vacuum migration:

```bash
curl http://127.0.0.1:8080/db/maintenance/status
curl -X POST http://127.0.0.1:8080/db/vacuum/migrate \
  -H 'Authorization: Bearer admin-token'
```

Manual `updates.GetDifferenceRequest` calls should be treated as an admin recovery tool.
Normal synchronization is handled by Telethon. Do not call difference in a polling loop from
external clients, because a partial external sync model can diverge from Telegram channel state.
The endpoint requires `recovery=true` and an admin token with `*` scope when token scopes are enabled.

Сейчас очередь хранится в памяти процесса. Для production-нагрузки следующим
слоем можно подключить Redis, RabbitMQ или NATS без изменения внешнего API.

Запуск API с Redis backend:

```bash
python -m tg_api_zapret api \
  --host 127.0.0.1 \
  --port 8080 \
  --queue-backend redis \
  --redis-url redis://127.0.0.1:6379/0
```

Через переменные окружения:

```bash
export TG_API_QUEUE_BACKEND=redis
export REDIS_URL=redis://127.0.0.1:6379/0
python -m tg_api_zapret api --host 127.0.0.1 --port 8080
```

Redis выбран как первый production backend: для текущего Queue API важнее хранить
статусы задач и быстро поднимать сервис без сложной инфраструктуры. RabbitMQ/NATS
можно добавить позже тем же backend-интерфейсом, если понадобится отдельный
кластер воркеров или pub/sub-шина.

## Queue API Details

Current queue semantics:

- memory backend is for local development and runs jobs inside the API process;
- Redis backend stores jobs durably, but Telegram jobs are executed by the API owner process;
- do not run separate Telegram queue workers for the same sessions; this can open a second `TelegramClient` for the same account;
- the old `tg-api-zapret worker` command is a guard and exits with an error instead of touching Telegram;
- Redis jobs support `idempotency_key`, `attempts`, `max_attempts`, `leased_until`, retry, and `dead_letter`;
- expired Redis leases are requeued until `max_attempts`, then moved to dead-letter state.

Check the centralized queue executor:

```bash
curl http://127.0.0.1:8080/queue/status \
  -H 'Authorization: Bearer admin-token'
```

## Bot API Compatibility Limits

`/bot{token}/{method}` is a compatibility layer, not a full Telegram Bot API proxy.
Implemented methods are `getMe`, `getUpdates`, `sendMessage`, `sendPhoto`, `sendDocument`,
`editMessageText`, and `deleteMessage`. For everything else use native REST wrappers,
JSON-RPC, or raw MTProto after explicitly enabling raw invoke.

`bot_token_accounts` is currently stored in the local JSON config for launcher
compatibility. Treat that config as secret material and keep it outside the
repository; host applications can later move the token storage to Windows
Credential Manager, Keychain, Secret Service, or another encrypted secret store.

## Python SDK API

```python
from tg_api_zapret import TgApiZapretClient

client = TgApiZapretClient("http://127.0.0.1:8080")
print(client.health())
print(client.version())
print(client.dialogs(account="work", limit=20))
client.send_message("me", "hello from sdk", account="work")

job = client.enqueue(
    "messages.send",
    {"entity": "me", "text": "queued from sdk"},
    account="work",
)
print(client.job(job["id"]))
```

## Raw RPC

```python
from telethon.tl.functions.users import GetFullUserRequest

result = await layer.invoke(GetFullUserRequest("me"))
```

## Запуск тестов

```bash
pytest
```

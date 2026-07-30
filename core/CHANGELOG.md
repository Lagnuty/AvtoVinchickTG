# Changelog

## 0.4.30

- Added `/version` for stable runtime version discovery.
- Split package dependencies into core and server extras.
- Added typed core auth/proxy/connection result helpers for GUI integrations.
- Added reconnect/backoff options to `TelegramLayer.stream_updates`.
- Updated documentation for embedded-core usage.

## 0.4.29

- Added persistent idempotency states with lease heartbeat for long operations.
- Added DB writer lifecycle, bounded queue, retry, dead-letter metadata, degraded health, and maintenance endpoints.

## 0.4.28

- Added persistent idempotency storage in SQLite.
- Added DB writer lifecycle and health status endpoint.
- Added SQLite incremental vacuum checks and retention improvements.

## 0.4.27 and earlier

- Added multi-account API support, session persistence, REST/JSON-RPC/WebSocket/SSE/Queue interfaces.
- Added TL JSON codec, entity resolver, MTProto layer dispatcher, and Bot API compatibility subset.

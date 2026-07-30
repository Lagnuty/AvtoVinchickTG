#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Standalone console client for tg-api-zapret.

No third-party dependencies are required. It uses only Python standard library.

Examples:
  python tg_api_zapret_menu_client.py
  python tg_api_zapret_menu_client.py --base-url http://127.0.0.1:8081 --token dev-admin-token
  set TG_API_TOKEN=dev-admin-token && python tg_api_zapret_menu_client.py
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import textwrap
import time
from getpass import getpass
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen


DEFAULT_BASE_URL = "http://127.0.0.1:8081"
DEFAULT_TIMEOUT = 90
MIN_REQUEST_INTERVAL_SECONDS = 1.25
BLOCKED_ACCOUNT_NAMES = {"string", "account"}


class ApiError(RuntimeError):
    def __init__(self, message: str, *, status_code: int | None = None, detail: Any = None) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.detail = detail


class TgApiZapretMenuClient:
    def __init__(
        self,
        base_url: str,
        *,
        token: str | None = None,
        account: str | None = None,
        timeout: int = DEFAULT_TIMEOUT,
        throttle: float = MIN_REQUEST_INTERVAL_SECONDS,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.account = account or None
        self.timeout = timeout
        self.throttle = throttle
        self._last_request_at = 0.0

    def request(
        self,
        method: str,
        path: str,
        *,
        query: dict[str, Any] | None = None,
        body: dict[str, Any] | list[Any] | None = None,
        raw: bool = False,
    ) -> Any:
        query = dict(query or {})
        if self.account and "account" not in query:
            validate_account_name(self.account)
            query["account"] = self.account

        url = self.base_url + path
        clean_query = {key: value for key, value in query.items() if value not in (None, "")}
        if clean_query:
            url += "?" + urlencode(clean_query)

        data = None
        headers = {
            "Accept": "application/json",
            "User-Agent": "tg-api-zapret-menu-client/2.0",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        if body is not None:
            data = json.dumps(body, ensure_ascii=False).encode("utf-8")
            headers["Content-Type"] = "application/json; charset=utf-8"

        self._wait_before_request()
        req = Request(url, data=data, headers=headers, method=method.upper())
        try:
            with urlopen(req, timeout=self.timeout) as response:
                payload = response.read()
                if raw:
                    return payload
                if not payload:
                    return None
                text = payload.decode("utf-8", errors="replace")
                try:
                    return json.loads(text)
                except json.JSONDecodeError:
                    return text
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            parsed: Any = detail
            try:
                parsed = json.loads(detail)
            except json.JSONDecodeError:
                pass
            message = parsed.get("detail", parsed) if isinstance(parsed, dict) else parsed
            raise ApiError(f"HTTP {exc.code}: {message}", status_code=exc.code, detail=parsed) from exc
        except URLError as exc:
            raise ApiError(f"Cannot connect to {self.base_url}: {exc.reason}") from exc
        except TimeoutError as exc:
            raise ApiError(f"Timeout while calling {self.base_url}") from exc

    def get(self, path: str, **kwargs: Any) -> Any:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, body: dict[str, Any] | list[Any] | None = None, **kwargs: Any) -> Any:
        return self.request("POST", path, body=body or {}, **kwargs)

    def put(self, path: str, body: dict[str, Any] | None = None, **kwargs: Any) -> Any:
        return self.request("PUT", path, body=body or {}, **kwargs)

    def patch(self, path: str, body: dict[str, Any] | None = None, **kwargs: Any) -> Any:
        return self.request("PATCH", path, body=body or {}, **kwargs)

    def _wait_before_request(self) -> None:
        if self.throttle <= 0:
            return
        elapsed = time.monotonic() - self._last_request_at
        if elapsed < self.throttle:
            time.sleep(self.throttle - elapsed)
        self._last_request_at = time.monotonic()


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def pause() -> None:
    input("\nPress Enter...")


def ask(prompt: str, default: str | None = None) -> str:
    suffix = "" if default is None else f" [{default}]"
    value = input(f"{prompt}{suffix}: ").strip()
    return value if value else (default or "")


def ask_secret(prompt: str, default_env: str | None = None) -> str:
    default = os.getenv(default_env or "") if default_env else None
    if default:
        raw = getpass(f"{prompt} [env:{default_env} set, Enter to keep]: ")
        return raw.strip() or default
    return getpass(f"{prompt}: ").strip()


def ask_int(prompt: str, default: int = 0, *, minimum: int | None = None) -> int:
    while True:
        raw = ask(prompt, str(default))
        try:
            value = int(raw)
        except ValueError:
            print("Enter a number.")
            continue
        if minimum is not None and value < minimum:
            print(f"Number must be >= {minimum}.")
            continue
        return value


def ask_float(prompt: str, default: float = 0.0, *, minimum: float | None = None) -> float:
    while True:
        raw = ask(prompt, str(default))
        try:
            value = float(raw)
        except ValueError:
            print("Enter a number.")
            continue
        if minimum is not None and value < minimum:
            print(f"Number must be >= {minimum}.")
            continue
        return value


def ask_bool(prompt: str, default: bool = False) -> bool:
    suffix = "Y/n" if default else "y/N"
    raw = input(f"{prompt} [{suffix}]: ").strip().lower()
    if not raw:
        return default
    return raw in {"y", "yes", "1", "true", "on", "да", "д"}


def ask_json(prompt: str, default: Any = None) -> Any:
    default_text = json.dumps(default if default is not None else {}, ensure_ascii=False)
    while True:
        raw = ask(prompt, default_text)
        try:
            return json.loads(raw)
        except json.JSONDecodeError as exc:
            print(f"Invalid JSON: {exc}")


def print_json(data: Any) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=False))


def print_table(rows: list[dict[str, Any]], columns: list[tuple[str, str, int]]) -> None:
    if not rows:
        print("No rows.")
        return
    header = "  ".join(title.ljust(width) for _, title, width in columns)
    print(header)
    print("-" * len(header))
    for row in rows:
        parts = []
        for key, _, width in columns:
            parts.append(short(row.get(key), width).ljust(width))
        print("  ".join(parts))


def short(value: Any, limit: int = 40) -> str:
    text = "" if value is None else str(value).replace("\r", " ").replace("\n", " ")
    return text if len(text) <= limit else text[: max(0, limit - 3)] + "..."


def parse_scalar(value: str) -> str | int:
    value = value.strip()
    if value.startswith("-") and value[1:].isdigit():
        return int(value)
    if value.isdigit():
        return int(value)
    return value


def normalize_username(value: str) -> str | int:
    value = value.strip()
    if value.startswith("-") and value[1:].isdigit():
        return int(value)
    if value.isdigit():
        return int(value)
    for prefix in ("https://t.me/", "http://t.me/", "t.me/"):
        if value.startswith(prefix):
            value = value.removeprefix(prefix).split("?", 1)[0].strip("/")
            break
    if value.startswith("@") or value.startswith("+") or "/" in value:
        return value
    return f"@{value}"


def validate_account_name(account: str) -> None:
    normalized = account.strip().lower()
    if normalized in BLOCKED_ACCOUNT_NAMES:
        raise ValueError("Do not use demo account names 'string' or 'account'. Use main/work/personal.")


def read_multiline(prompt: str = "Text") -> str:
    print(f"{prompt}. End input with a single dot '.' on its own line.")
    lines = []
    while True:
        line = input()
        if line == ".":
            break
        lines.append(line)
    return "\n".join(lines).strip()


def read_file_base64(path: str) -> tuple[str, str]:
    file_path = Path(path)
    data = base64.b64encode(file_path.read_bytes()).decode("ascii")
    return data, file_path.name


def choose_dialog(client: TgApiZapretMenuClient, *, limit: int = 30) -> str | int | None:
    dialogs = client.get("/dialogs", query={"limit": limit})
    if not isinstance(dialogs, list):
        print_json(dialogs)
        return None
    print_dialogs(dialogs)
    raw = ask("Choose number, id, @username, t.me link, or empty to cancel", "")
    if not raw:
        return None
    if raw.isdigit():
        index = int(raw)
        if 1 <= index <= len(dialogs):
            dialog = dialogs[index - 1]
            username = dialog.get("username")
            if username:
                return f"@{username}"
            input_entity = dialog.get("input_entity")
            if input_entity:
                return input_entity
            return dialog.get("id")
        return int(raw)
    return normalize_username(raw)


def choose_entity(client: TgApiZapretMenuClient, *, prefer_new_username: bool = True) -> str | int | dict[str, Any] | None:
    if prefer_new_username:
        print("1. Enter username/phone/id manually")
        print("2. Choose from dialogs")
    else:
        print("1. Choose from dialogs")
        print("2. Enter username/phone/id manually")
    choice = ask("Choice", "1")
    manual = (prefer_new_username and choice == "1") or (not prefer_new_username and choice == "2")
    if manual:
        raw = ask("Entity (@username, phone, id, t.me link)")
        return normalize_username(raw) if raw else None
    return choose_dialog(client)


def print_dialogs(dialogs: list[dict[str, Any]]) -> None:
    rows = []
    for index, dialog in enumerate(dialogs, 1):
        kind = "user" if dialog.get("is_user") else "group" if dialog.get("is_group") else "channel" if dialog.get("is_channel") else "chat"
        rows.append(
            {
                "n": index,
                "id": dialog.get("id"),
                "kind": kind,
                "unread": dialog.get("unread_count", 0),
                "username": f"@{dialog.get('username')}" if dialog.get("username") else "",
                "name": dialog.get("name") or dialog.get("title"),
            }
        )
    print_table(
        rows,
        [
            ("n", "#", 4),
            ("id", "ID", 16),
            ("kind", "Type", 8),
            ("unread", "Unread", 7),
            ("username", "Username", 22),
            ("name", "Name", 42),
        ],
    )


def print_messages(messages: list[dict[str, Any]]) -> None:
    if not messages:
        print("No messages.")
        return
    for message in messages:
        print("-" * 88)
        print(
            f"id={message.get('id')} "
            f"{'out' if message.get('out') else 'in '} "
            f"sender={message.get('sender_id')} date={message.get('date')}"
        )
        if message.get("media"):
            print(f"media={short(message.get('media'), 120)}")
        print(message.get("text") or "[no text]")


def menu_health(client: TgApiZapretMenuClient) -> None:
    print_json(client.get("/health"))


def menu_capabilities(client: TgApiZapretMenuClient) -> None:
    print_json(client.get("/capabilities"))


def menu_config(client: TgApiZapretMenuClient) -> None:
    print_json(client.get("/config"))


def menu_accounts(client: TgApiZapretMenuClient) -> None:
    data = client.get("/accounts")
    print_json(data)
    if ask_bool("Set local account for future requests", False):
        account = ask("Account", data.get("active_account") or client.account or "default")
        validate_account_name(account)
        client.account = account
        print(f"Local account set to {client.account}")


def menu_add_account(client: TgApiZapretMenuClient) -> None:
    account = ask("Account alias, for example main/work/personal", client.account or "default")
    validate_account_name(account)
    print_json(client.post("/accounts", {"account": account}))
    client.account = account


def menu_connect_account(client: TgApiZapretMenuClient) -> None:
    account = ask("Account", client.account or "default")
    keep_online = ask_bool("Keep online/runtime active", True)
    print_json(client.post("/accounts/connect", {"account": account, "keep_online": keep_online}))
    client.account = account


def menu_disconnect_account(client: TgApiZapretMenuClient) -> None:
    account = ask("Account", client.account or "default")
    print_json(client.post("/accounts/disconnect", {"account": account}))


def menu_online(client: TgApiZapretMenuClient) -> None:
    print_json(client.get("/accounts/online"))


def menu_account_health(client: TgApiZapretMenuClient) -> None:
    account = ask("Account empty = all", client.account or "")
    print_json(client.get("/accounts/health", query={"account": account or None}))


def menu_entity_cache(client: TgApiZapretMenuClient) -> None:
    print("1. Show cache")
    print("2. Warm cache")
    choice = ask("Choice", "1")
    if choice == "2":
        limit = ask_int("Dialog limit", 50, minimum=1)
        print_json(client.post("/accounts/entity-cache/warm", query={"limit": limit}))
    else:
        print_json(client.get("/accounts/entity-cache"))


def menu_auth_status(client: TgApiZapretMenuClient) -> None:
    print_json(client.get("/auth/status"))


def menu_login(client: TgApiZapretMenuClient) -> None:
    phone = ask("Phone number, for example +79990000000")
    sent = client.post("/auth/send-code", {"phone": phone})
    print("Code sent.")
    print_json(sent)
    code = ask("Telegram code")
    result = client.post(
        "/auth/confirm-code",
        {"phone": phone, "phone_code_hash": sent["phone_code_hash"], "code": code},
    )
    if result.get("status") == "password_required":
        password = getpass("2FA password: ")
        result = client.post("/auth/password", {"password": password})
    print_json(result)


def menu_me(client: TgApiZapretMenuClient) -> None:
    print_json(client.get("/me"))


def menu_dialogs(client: TgApiZapretMenuClient) -> None:
    limit = ask_int("Dialog limit", 30, minimum=1)
    dialogs = client.get("/dialogs", query={"limit": limit})
    if isinstance(dialogs, list):
        print_dialogs(dialogs)
    else:
        print_json(dialogs)


def menu_messages(client: TgApiZapretMenuClient) -> None:
    entity = choose_entity(client, prefer_new_username=False)
    if entity is None:
        return
    limit = ask_int("Message limit", 50, minimum=1)
    messages = client.post("/messages/list", {"entity": entity, "limit": limit})
    if isinstance(messages, list):
        print_messages(messages)
    else:
        print_json(messages)


def menu_send_message(client: TgApiZapretMenuClient) -> None:
    entity = choose_entity(client)
    if entity is None:
        return
    text = read_multiline("Message")
    if not text:
        print("Empty message was not sent.")
        return
    parse_mode = ask("parse_mode empty/html/markdown", "")
    print_json(client.post("/messages/send", {"entity": entity, "text": text, "parse_mode": parse_mode or None}))


def menu_send_username_message(client: TgApiZapretMenuClient) -> None:
    username = ask("Username, phone, or t.me link")
    text = read_multiline("Message")
    parse_mode = ask("parse_mode empty/html/markdown", "")
    print_json(client.post("/messages/send-username", {"username": username, "text": text, "parse_mode": parse_mode or None}))


def menu_edit_message(client: TgApiZapretMenuClient) -> None:
    entity = choose_entity(client, prefer_new_username=False)
    if entity is None:
        return
    message_id = ask_int("Message id", minimum=1)
    text = read_multiline("New text")
    print_json(client.post("/messages/edit", {"entity": entity, "message_id": message_id, "text": text}))


def menu_delete_messages(client: TgApiZapretMenuClient) -> None:
    entity = choose_entity(client, prefer_new_username=False)
    if entity is None:
        return
    ids = parse_int_list(ask("Message ids separated by comma"))
    revoke = ask_bool("Revoke for everyone when possible", True)
    print_json(client.post("/messages/delete", {"entity": entity, "message_ids": ids, "revoke": revoke}))


def menu_forward_messages(client: TgApiZapretMenuClient) -> None:
    print("Source chat:")
    source = choose_entity(client, prefer_new_username=False)
    if source is None:
        return
    ids = parse_int_list(ask("Message ids separated by comma"))
    print("Destination chat:")
    target = choose_entity(client)
    if target is None:
        return
    print_json(client.post("/messages/forward", {"from_entity": source, "to_entity": target, "message_ids": ids}))


def menu_delete_history(client: TgApiZapretMenuClient) -> None:
    entity = choose_entity(client, prefer_new_username=False)
    if entity is None:
        return
    if ask_bool("Delete full history for this peer", False):
        print_json(client.post("/messages/history/delete", {"entity": entity}))


def menu_reaction(client: TgApiZapretMenuClient) -> None:
    entity = choose_entity(client, prefer_new_username=False)
    if entity is None:
        return
    message_id = ask_int("Message id", minimum=1)
    reaction = ask("Reaction emoji empty = remove", "")
    body: dict[str, Any] = {"entity": entity, "message_id": message_id}
    if reaction:
        body["reaction"] = reaction
    body["big"] = ask_bool("Big reaction", False)
    print_json(client.post("/messages/reaction", body))


def menu_resolve_entity(client: TgApiZapretMenuClient) -> None:
    entity = normalize_username(ask("Entity username/phone/id/t.me"))
    print_json(client.post("/entities/resolve", {"entity": entity}))


def menu_send_media(client: TgApiZapretMenuClient) -> None:
    entity = choose_entity(client)
    if entity is None:
        return
    file_path = ask("Local file path")
    if not Path(file_path).is_file():
        print("File not found.")
        return
    caption = ask("Caption", "")
    parse_mode = ask("parse_mode empty/html/markdown", "")
    mode = ask("Upload as base64 or server path? base64/path", "base64").lower()
    body: dict[str, Any] = {"entity": entity, "caption": caption or None, "parse_mode": parse_mode or None}
    if mode == "path":
        body["file_path"] = file_path
    else:
        body["file_base64"], body["file_name"] = read_file_base64(file_path)
    print_json(client.post("/media/send", body))


def menu_download_media(client: TgApiZapretMenuClient) -> None:
    entity = choose_entity(client, prefer_new_username=False)
    if entity is None:
        return
    message_id = ask_int("Message id with media", minimum=1)
    result = client.post("/media/download", {"entity": entity, "message_id": message_id, "as_base64": True})
    data = result.get("data") if isinstance(result, dict) else None
    if isinstance(data, dict) and data.get("base64"):
        default_name = f"telegram_media_{message_id}.bin"
        output = ask("Output file", default_name)
        Path(output).write_bytes(base64.b64decode(data["base64"]))
        print(f"Saved: {output}")
    else:
        print_json(result)


def menu_upload_file(client: TgApiZapretMenuClient) -> None:
    file_path = ask("Local file path")
    if not Path(file_path).is_file():
        print("File not found.")
        return
    file_base64, file_name = read_file_base64(file_path)
    print_json(client.post("/files/upload", {"file_base64": file_base64, "file_name": file_name}))


def menu_join_chat(client: TgApiZapretMenuClient) -> None:
    entity = normalize_username(ask("Channel/chat username, invite link, or id"))
    print_json(client.post("/chats/join", {"entity": entity}))


def menu_leave_chat(client: TgApiZapretMenuClient) -> None:
    entity = choose_entity(client, prefer_new_username=False)
    if entity is None:
        return
    if ask_bool("Leave this chat/channel", False):
        print_json(client.post("/chats/leave", {"entity": entity}))


def menu_get_stories(client: TgApiZapretMenuClient) -> None:
    entity = choose_entity(client, prefer_new_username=False)
    if entity is None:
        return
    story_ids = parse_int_list(ask("Story ids separated by comma"))
    print_json(client.post("/stories/get", {"entity": entity, "story_ids": story_ids}))


def menu_send_story(client: TgApiZapretMenuClient) -> None:
    peer = choose_entity(client)
    if peer is None:
        return
    media = ask_json('Media TL JSON, for example {"_":"InputMediaUploadedPhoto",...}', {})
    rules = ask_json('Privacy rules JSON list, for example [{"_":"InputPrivacyValueAllowAll"}]', [{"_": "InputPrivacyValueAllowAll"}])
    caption = ask("Caption", "")
    body = {"peer": peer, "media": media, "privacy_rules": rules, "caption": caption or None}
    print_json(client.post("/stories/send", body))


def menu_admin_ban(client: TgApiZapretMenuClient) -> None:
    channel = normalize_username(ask("Channel/group"))
    participant = normalize_username(ask("Participant"))
    rights = ask_json("ChatBannedRights JSON", {"_": "ChatBannedRights", "until_date": None, "view_messages": True})
    print_json(client.post("/admin/ban", {"channel": channel, "participant": participant, "banned_rights": rights}))


def menu_admin_promote(client: TgApiZapretMenuClient) -> None:
    channel = normalize_username(ask("Channel/group"))
    user = normalize_username(ask("User"))
    rights = ask_json("ChatAdminRights JSON", {"_": "ChatAdminRights", "change_info": True})
    rank = ask("Rank", "")
    print_json(client.post("/admin/promote", {"channel": channel, "user": user, "admin_rights": rights, "rank": rank or None}))


def menu_tl_construct(client: TgApiZapretMenuClient) -> None:
    constructor = ask("TL constructor, for example InputPeerUser")
    fields = ask_json("Fields JSON", {})
    print_json(client.post("/tl/construct", {"constructor": constructor, "fields": fields}))


def menu_raw_invoke(client: TgApiZapretMenuClient) -> None:
    request_name = ask("Telethon request, for example users.GetFullUserRequest")
    kwargs = ask_json('kwargs JSON, for example {"id":"me"}', {})
    print_json(client.post("/raw/invoke", {"request": request_name, "kwargs": kwargs}))


def menu_layer_functions(client: TgApiZapretMenuClient) -> None:
    layer = ask_int("MTProto layer", 201, minimum=1)
    data = client.get(f"/mtproto/layers/{layer}/functions")
    functions = data.get("functions") if isinstance(data, dict) else None
    if isinstance(functions, list):
        print(f"Layer {layer}, functions: {len(functions)}")
        for item in functions[:200]:
            print(item)
        if len(functions) > 200:
            print(f"... {len(functions) - 200} more")
    else:
        print_json(data)


def menu_layer_invoke(client: TgApiZapretMenuClient) -> None:
    layer = ask_int("MTProto layer", 201, minimum=1)
    request_name = ask("Layer request, for example messages.SendMessageRequest")
    kwargs = ask_json("kwargs JSON", {})
    print_json(client.post(f"/mtproto/layers/{layer}/invoke", {"request": request_name, "kwargs": kwargs}))


def menu_rpc(client: TgApiZapretMenuClient) -> None:
    method = ask("JSON-RPC method, for example dialogs.list/messages.send/raw.invoke")
    params = ask_json("params JSON", {"account": client.account} if client.account else {})
    request_id = ask("id", str(int(time.time())))
    print_json(client.post("/rpc", {"jsonrpc": "2.0", "method": method, "params": params, "id": request_id}))


def menu_action_resolve(client: TgApiZapretMenuClient) -> None:
    task = ask("Task, for example send message / list dialogs / realtime updates")
    params = ask_json("Params JSON", {})
    body = {
        "task": task,
        "account": client.account,
        "params": params,
        "realtime": ask_bool("Realtime", False),
        "background": ask_bool("Background queue", False),
        "bidirectional": ask_bool("Bidirectional WebSocket", False),
    }
    print_json(client.post("/actions/resolve", body))


def menu_action_execute(client: TgApiZapretMenuClient) -> None:
    task = ask("Task")
    params = ask_json("Params JSON", {})
    body = {
        "task": task,
        "account": client.account,
        "params": params,
        "realtime": ask_bool("Realtime", False),
        "background": ask_bool("Background queue", False),
        "bidirectional": ask_bool("Bidirectional WebSocket", False),
    }
    print_json(client.post("/actions/execute", body))


def menu_queue_create(client: TgApiZapretMenuClient) -> None:
    kind = ask("Job kind, for example messages.send/dialogs.list/raw.invoke")
    payload = ask_json("Payload JSON", {})
    max_attempts = ask_int("Max attempts", 3, minimum=1)
    body = {"kind": kind, "account": client.account, "payload": payload, "max_attempts": max_attempts}
    key = ask("Idempotency key empty = none", "")
    if key:
        body["idempotency_key"] = key
    print_json(client.post("/queue/jobs", body))


def menu_queue_list(client: TgApiZapretMenuClient) -> None:
    print_json(client.get("/queue/jobs"))


def menu_queue_get(client: TgApiZapretMenuClient) -> None:
    job_id = ask("Job id")
    print_json(client.get(f"/queue/jobs/{quote(job_id, safe='')}"))


def menu_proxy(client: TgApiZapretMenuClient) -> None:
    print("Supported: http, https, socks5, socks5h")
    proxy = ask("Proxy URL empty = clear", "")
    print_json(client.put("/config/proxy", {"proxy_url": proxy or None}))


def menu_client_profile(client: TgApiZapretMenuClient) -> None:
    current = client.get("/config").get("client_profile", {})
    body = {
        "device_model": ask("device_model", current.get("device_model") or "Telegram Desktop"),
        "system_version": ask("system_version", current.get("system_version") or "Linux x86_64"),
        "app_version": ask("app_version", current.get("app_version") or "tg-api-zapret"),
        "lang_code": ask("lang_code", current.get("lang_code") or "en"),
        "system_lang_code": ask("system_lang_code", current.get("system_lang_code") or "en-US"),
    }
    print_json(client.put("/config/client-profile", body))


def menu_app_settings(client: TgApiZapretMenuClient) -> None:
    settings = client.get("/app/settings")
    print_json(settings)
    print("\n1. Patch arbitrary JSON")
    print("2. Toggle raw/layer invoke")
    print("3. Toggle docs")
    print("4. Toggle API token requirement")
    print("5. Configure desktop-like runtime")
    print("0. Back")
    choice = ask("Choice", "0")
    if choice == "1":
        print_json(client.patch("/app/settings", ask_json("Patch JSON", {})))
    elif choice == "2":
        enable = ask_bool("Enable raw and layer invoke", bool(settings.get("enable_raw_invoke")))
        print_json(client.patch("/app/settings", {"enable_raw_invoke": enable, "enable_layer_invoke": enable}))
    elif choice == "3":
        print_json(client.patch("/app/settings", {"expose_docs": ask_bool("Expose docs", bool(settings.get("expose_docs")))}))
    elif choice == "4":
        print_json(client.patch("/app/settings", {"require_api_token": ask_bool("Require API token", bool(settings.get("require_api_token", True)))}))
    elif choice == "5":
        patch = {
            "keep_accounts_online": ask_bool("Keep accounts online", bool(settings.get("keep_accounts_online", True))),
            "online_update_interval_seconds": ask_int("Online heartbeat seconds", int(settings.get("online_update_interval_seconds", 55)), minimum=15),
            "reconnect_enabled": ask_bool("Reconnect enabled", bool(settings.get("reconnect_enabled", True))),
            "passive_update_receiver": ask_bool("Passive update receiver", bool(settings.get("passive_update_receiver", True))),
            "entity_cache_warmup_dialogs": ask_int("Entity cache warmup dialogs", int(settings.get("entity_cache_warmup_dialogs", 50)), minimum=0),
            "require_connection_health_before_auth": ask_bool("Health check before auth", bool(settings.get("require_connection_health_before_auth", True))),
        }
        auto = ask("auto_connect_accounts comma separated", ",".join(settings.get("auto_connect_accounts") or []))
        patch["auto_connect_accounts"] = [item.strip() for item in auto.split(",") if item.strip()]
        print_json(client.patch("/app/settings", patch))


def menu_reverse_proxy(client: TgApiZapretMenuClient) -> None:
    print_json(client.get("/compat/reverse-proxy"))


def menu_bot_api(client: TgApiZapretMenuClient) -> None:
    token = ask("Bot-compatible token path part")
    method = ask("Method, for example getMe/sendMessage/getUpdates")
    params = ask_json("Params JSON", {})
    print_json(client.post(f"/bot{token}/{method}", params))


def menu_sse_probe(client: TgApiZapretMenuClient) -> None:
    seconds = ask_int("Listen seconds", 30, minimum=1)
    query = {}
    if client.account:
        query["account"] = client.account
    url = client.base_url + "/events"
    if query:
        url += "?" + urlencode(query)
    headers = {"Accept": "text/event-stream"}
    if client.token:
        headers["Authorization"] = f"Bearer {client.token}"
    req = Request(url, headers=headers, method="GET")
    started = time.monotonic()
    with urlopen(req, timeout=seconds + 5) as response:
        while time.monotonic() - started < seconds:
            line = response.readline()
            if not line:
                break
            print(line.decode("utf-8", errors="replace").rstrip())


def menu_auth_token(client: TgApiZapretMenuClient) -> None:
    print(f"Current token: {'set' if client.token else 'not set'}")
    token = ask_secret("API token", "TG_API_TOKEN")
    client.token = token or None


def menu_base_url(client: TgApiZapretMenuClient) -> None:
    client.base_url = ask("Base URL", client.base_url).rstrip("/")


def menu_local_account(client: TgApiZapretMenuClient) -> None:
    account = ask("Local account empty = server active", client.account or "")
    if account:
        validate_account_name(account)
    client.account = account or None


def parse_int_list(raw: str) -> list[int]:
    ids = []
    for part in raw.split(","):
        part = part.strip()
        if part:
            ids.append(int(part))
    return ids


MenuItem = tuple[str, Callable[[TgApiZapretMenuClient], None]]


def build_menu() -> list[MenuItem]:
    return [
        ("Health", menu_health),
        ("Set API token", menu_auth_token),
        ("Set base URL", menu_base_url),
        ("Set local account", menu_local_account),
        ("Capabilities", menu_capabilities),
        ("Config", menu_config),
        ("App settings/security/runtime", menu_app_settings),
        ("Accounts list/switch", menu_accounts),
        ("Accounts add", menu_add_account),
        ("Accounts connect desktop-like runtime", menu_connect_account),
        ("Accounts disconnect", menu_disconnect_account),
        ("Accounts online status", menu_online),
        ("Accounts health", menu_account_health),
        ("Entity cache show/warm", menu_entity_cache),
        ("Auth status", menu_auth_status),
        ("Login by phone/code/2FA", menu_login),
        ("Me", menu_me),
        ("Dialogs", menu_dialogs),
        ("Messages list", menu_messages),
        ("Send message", menu_send_message),
        ("Send message by username", menu_send_username_message),
        ("Edit message", menu_edit_message),
        ("Delete messages", menu_delete_messages),
        ("Forward messages", menu_forward_messages),
        ("Delete history", menu_delete_history),
        ("Reaction", menu_reaction),
        ("Resolve entity", menu_resolve_entity),
        ("Send media/file", menu_send_media),
        ("Download media", menu_download_media),
        ("Upload file", menu_upload_file),
        ("Join chat/channel", menu_join_chat),
        ("Leave chat/channel", menu_leave_chat),
        ("Stories get", menu_get_stories),
        ("Stories send raw TL media", menu_send_story),
        ("Admin ban/restrict", menu_admin_ban),
        ("Admin promote", menu_admin_promote),
        ("TL construct", menu_tl_construct),
        ("Raw invoke", menu_raw_invoke),
        ("MTProto layer functions", menu_layer_functions),
        ("MTProto layer invoke", menu_layer_invoke),
        ("JSON-RPC", menu_rpc),
        ("Action resolve", menu_action_resolve),
        ("Action execute", menu_action_execute),
        ("Queue create job", menu_queue_create),
        ("Queue list jobs", menu_queue_list),
        ("Queue get job", menu_queue_get),
        ("Set proxy", menu_proxy),
        ("Set Telegram client profile", menu_client_profile),
        ("Reverse-proxy compatibility info", menu_reverse_proxy),
        ("Bot API compatibility call", menu_bot_api),
        ("SSE events probe", menu_sse_probe),
    ]


def show_header(client: TgApiZapretMenuClient) -> None:
    print("=" * 88)
    print("tg-api-zapret menu client")
    print(f"Server:  {client.base_url}")
    print(f"Token:   {'set' if client.token else 'not set'}")
    print(f"Account: {client.account or '(server active)'}")
    print("=" * 88)


def main_menu(client: TgApiZapretMenuClient) -> None:
    items = build_menu()
    while True:
        clear_screen()
        show_header(client)
        for index, (title, _) in enumerate(items, 1):
            print(f"{index:>2}. {title}")
        print(" 0. Exit")
        choice = ask("Choice", "")
        if choice == "0":
            return
        try:
            index = int(choice)
            title, handler = items[index - 1]
        except (ValueError, IndexError):
            print("Invalid menu item.")
            pause()
            continue

        clear_screen()
        show_header(client)
        print(title)
        print("-" * 88)
        try:
            handler(client)
        except KeyboardInterrupt:
            print("\nCanceled.")
        except ApiError as exc:
            print(f"\nAPI error: {exc}")
            if exc.status_code == 401:
                detail_text = json.dumps(exc.detail, ensure_ascii=False) if exc.detail is not None else str(exc)
                if "Missing or invalid API token" in detail_text:
                    print("Tip: pass --token dev-admin-token or set TG_API_TOKEN/TG_API_TOKEN_CLIENT.")
                elif "Telegram session is not authorized" in detail_text:
                    print("Tip: check selected account and session file, or run Login by phone/code/2FA.")
            if exc.detail is not None:
                print("\nDetail:")
                print_json(exc.detail)
        except Exception as exc:
            print(f"\nError: {type(exc).__name__}: {exc}")
        pause()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Standalone console client for tg-api-zapret.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            f"""
            Examples:
              python tg_api_zapret_menu_client.py
              python tg_api_zapret_menu_client.py --base-url {DEFAULT_BASE_URL}
              python tg_api_zapret_menu_client.py --token dev-admin-token
              set TG_API_TOKEN=dev-admin-token && python tg_api_zapret_menu_client.py
            """
        ),
    )
    parser.add_argument("--base-url", default=os.getenv("TG_API_ZAPRET_URL", DEFAULT_BASE_URL))
    parser.add_argument("--token", default=os.getenv("TG_API_TOKEN_CLIENT") or os.getenv("TG_API_TOKEN"))
    parser.add_argument("--account", default=os.getenv("TG_API_ACCOUNT"))
    parser.add_argument("--timeout", type=int, default=int(os.getenv("TG_API_CLIENT_TIMEOUT", str(DEFAULT_TIMEOUT))))
    parser.add_argument("--no-throttle", action="store_true")
    parser.add_argument("--json", nargs=3, metavar=("METHOD", "PATH", "BODY"), help="One-shot JSON call.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    client = TgApiZapretMenuClient(
        args.base_url,
        token=args.token,
        account=args.account,
        timeout=args.timeout,
        throttle=0 if args.no_throttle else MIN_REQUEST_INTERVAL_SECONDS,
    )
    if args.json:
        method, path, body = args.json
        parsed_body = json.loads(body)
        print_json(client.request(method, path, body=parsed_body))
        return
    try:
        main_menu(client)
    except KeyboardInterrupt:
        print("\nExit.")
        sys.exit(130)


if __name__ == "__main__":
    main()

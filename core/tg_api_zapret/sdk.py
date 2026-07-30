from __future__ import annotations

import json
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class TgApiZapretClient:
    def __init__(self, base_url: str = "http://127.0.0.1:8080", token: str | None = None) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token

    def health(self) -> dict[str, Any]:
        return self._request("GET", "/health")

    def accounts(self) -> dict[str, Any]:
        return self._request("GET", "/accounts")

    def auth_status(self, account: str | None = None) -> dict[str, Any]:
        return self._request("GET", "/auth/status", query=account_query(account))

    def dialogs(self, account: str | None = None, limit: int = 20) -> list[dict[str, Any]]:
        return self._request("GET", "/dialogs", query={**account_query(account), "limit": limit})

    def send_message(
        self,
        entity: str | int,
        text: str,
        *,
        account: str | None = None,
        parse_mode: str | None = None,
    ) -> dict[str, Any]:
        return self._request(
            "POST",
            "/messages/send",
            query=account_query(account),
            body={"entity": entity, "text": text, "parse_mode": parse_mode},
        )

    def send_username_message(
        self,
        username: str,
        text: str,
        *,
        account: str | None = None,
        parse_mode: str | None = None,
    ) -> dict[str, Any]:
        return self._request(
            "POST",
            "/messages/send-username",
            query=account_query(account),
            body={"username": username, "text": text, "parse_mode": parse_mode},
        )

    def send_media(
        self,
        entity: str | int,
        *,
        file_path: str | None = None,
        file_base64: str | None = None,
        file_name: str | None = None,
        caption: str | None = None,
        account: str | None = None,
    ) -> dict[str, Any]:
        return self._request(
            "POST",
            "/media/send",
            query=account_query(account),
            body={
                "entity": entity,
                "file_path": file_path,
                "file_base64": file_base64,
                "file_name": file_name,
                "caption": caption,
            },
        )

    def resolve_entity(self, entity: str | int, *, account: str | None = None) -> dict[str, Any]:
        return self._request(
            "POST",
            "/entities/resolve",
            query=account_query(account),
            body={"entity": entity},
        )

    def raw_invoke(
        self,
        request: str,
        kwargs: dict[str, Any] | None = None,
        *,
        account: str | None = None,
    ) -> dict[str, Any]:
        return self._request(
            "POST",
            "/raw/invoke",
            query=account_query(account),
            body={"request": request, "kwargs": kwargs or {}},
        )

    def construct_tl(
        self,
        constructor: str,
        fields: dict[str, Any] | None = None,
        *,
        account: str | None = None,
    ) -> dict[str, Any]:
        return self._request(
            "POST",
            "/tl/construct",
            query=account_query(account),
            body={"constructor": constructor, "fields": fields or {}},
        )

    def rpc(
        self,
        method: str,
        params: dict[str, Any] | None = None,
        *,
        request_id: str | int | None = None,
    ) -> dict[str, Any]:
        return self._request(
            "POST",
            "/rpc",
            body={"jsonrpc": "2.0", "method": method, "params": params or {}, "id": request_id},
        )

    def enqueue(
        self,
        kind: str,
        payload: dict[str, Any],
        *,
        account: str | None = None,
    ) -> dict[str, Any]:
        return self._request(
            "POST",
            "/queue/jobs",
            body={"kind": kind, "account": account, "payload": payload},
        )

    def job(self, job_id: str) -> dict[str, Any]:
        return self._request("GET", f"/queue/jobs/{job_id}")

    def capabilities(self) -> dict[str, Any]:
        return self._request("GET", "/capabilities")

    def app_settings(self) -> dict[str, Any]:
        return self._request("GET", "/app/settings")

    def update_app_settings(self, **settings: Any) -> dict[str, Any]:
        return self._request("PATCH", "/app/settings", body=settings)

    def resolve_action(
        self,
        task: str,
        *,
        account: str | None = None,
        params: dict[str, Any] | None = None,
        realtime: bool = False,
        background: bool = False,
        bidirectional: bool = False,
        client_language: str | None = None,
    ) -> dict[str, Any]:
        return self._request(
            "POST",
            "/actions/resolve",
            body={
                "task": task,
                "account": account,
                "params": params or {},
                "realtime": realtime,
                "background": background,
                "bidirectional": bidirectional,
                "client_language": client_language,
            },
        )

    def execute_action(
        self,
        task: str,
        *,
        account: str | None = None,
        params: dict[str, Any] | None = None,
        realtime: bool = False,
        background: bool = False,
        bidirectional: bool = False,
        client_language: str | None = None,
    ) -> dict[str, Any]:
        return self._request(
            "POST",
            "/actions/execute",
            body={
                "task": task,
                "account": account,
                "params": params or {},
                "realtime": realtime,
                "background": background,
                "bidirectional": bidirectional,
                "client_language": client_language,
            },
        )

    def _request(
        self,
        method: str,
        path: str,
        *,
        query: dict[str, Any] | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        url = self.base_url + path
        if query:
            clean_query = {key: value for key, value in query.items() if value is not None}
            if clean_query:
                url += "?" + urlencode(clean_query)

        data = None
        headers = {"Accept": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        if body is not None:
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = "application/json"

        request = Request(url, data=data, headers=headers, method=method)
        with urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))

    def bot_api(self, token: str) -> "BotApiAdapter":
        return BotApiAdapter(self.base_url, token, bearer_token=self.token)


class BotApiAdapter:
    def __init__(
        self,
        base_url: str = "http://127.0.0.1:8080",
        bot_token: str = "",
        *,
        bearer_token: str | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.bot_token = bot_token
        self.bearer_token = bearer_token

    def get_me(self) -> dict[str, Any]:
        return self._call("getMe")

    def get_updates(self, **params: Any) -> dict[str, Any]:
        return self._call("getUpdates", params)

    def send_message(self, chat_id: str | int, text: str, **params: Any) -> dict[str, Any]:
        return self._call("sendMessage", {"chat_id": chat_id, "text": text, **params})

    def send_photo(self, chat_id: str | int, photo: str, **params: Any) -> dict[str, Any]:
        return self._call("sendPhoto", {"chat_id": chat_id, "photo": photo, **params})

    def send_document(self, chat_id: str | int, document: str, **params: Any) -> dict[str, Any]:
        return self._call("sendDocument", {"chat_id": chat_id, "document": document, **params})

    def edit_message_text(
        self,
        chat_id: str | int,
        message_id: int,
        text: str,
        **params: Any,
    ) -> dict[str, Any]:
        return self._call(
            "editMessageText",
            {"chat_id": chat_id, "message_id": message_id, "text": text, **params},
        )

    def delete_message(self, chat_id: str | int, message_id: int) -> dict[str, Any]:
        return self._call("deleteMessage", {"chat_id": chat_id, "message_id": message_id})

    def _call(self, method: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        client = TgApiZapretClient(self.base_url, token=self.bearer_token)
        return client._request("POST", f"/bot{self.bot_token}/{method}", body=params or {})


def account_query(account: str | None) -> dict[str, str]:
    return {"account": account} if account else {}

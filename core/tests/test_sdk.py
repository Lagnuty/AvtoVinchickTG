from tg_api_zapret.sdk import BotApiAdapter, TgApiZapretClient
from tg_api_zapret.version import __version__


def test_sdk_auth_header_and_raw_invoke(monkeypatch) -> None:
    captured = {}

    def fake_request(self, method, path, *, query=None, body=None):
        captured.update(
            {
                "token": self.token,
                "method": method,
                "path": path,
                "query": query,
                "body": body,
            }
        )
        return {"ok": True}

    monkeypatch.setattr(TgApiZapretClient, "_request", fake_request)

    client = TgApiZapretClient("http://api", token="secret")
    result = client.raw_invoke("users.GetFullUserRequest", {"id": "me"}, account="main")

    assert result == {"ok": True}
    assert captured["token"] == "secret"
    assert captured["path"] == "/raw/invoke"
    assert captured["query"] == {"account": "main"}
    assert captured["body"]["request"] == "users.GetFullUserRequest"


def test_sdk_version(monkeypatch) -> None:
    captured = {}

    def fake_request(self, method, path, *, query=None, body=None):
        captured.update({"method": method, "path": path, "query": query, "body": body})
        return {"version": __version__}

    monkeypatch.setattr(TgApiZapretClient, "_request", fake_request)

    result = TgApiZapretClient("http://api").version()

    assert result == {"version": __version__}
    assert captured == {"method": "GET", "path": "/version", "query": None, "body": None}


def test_bot_api_adapter_uses_bot_path(monkeypatch) -> None:
    captured = {}

    def fake_request(self, method, path, *, query=None, body=None):
        captured.update({"method": method, "path": path, "body": body, "token": self.token})
        return {"ok": True}

    monkeypatch.setattr(TgApiZapretClient, "_request", fake_request)

    bot = BotApiAdapter("http://api", "123:abc", bearer_token="secret")
    result = bot.send_message("@user", "hello")

    assert result == {"ok": True}
    assert captured == {
        "method": "POST",
        "path": "/bot123:abc/sendMessage",
        "body": {"chat_id": "@user", "text": "hello"},
        "token": "secret",
    }


def test_sdk_send_username_message(monkeypatch) -> None:
    captured = {}

    def fake_request(self, method, path, *, query=None, body=None):
        captured.update({"method": method, "path": path, "query": query, "body": body})
        return {"id": 1}

    monkeypatch.setattr(TgApiZapretClient, "_request", fake_request)

    client = TgApiZapretClient("http://api")
    result = client.send_username_message("alice", "hello", account="main")

    assert result == {"id": 1}
    assert captured["path"] == "/messages/send-username"
    assert captured["query"] == {"account": "main"}
    assert captured["body"] == {"username": "alice", "text": "hello", "parse_mode": None}

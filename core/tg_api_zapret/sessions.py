from __future__ import annotations

from abc import ABC, abstractmethod
import atexit
import base64
import json
import os
from pathlib import Path
import sqlite3
import time
from typing import Any

from telethon.sessions import StringSession


class SessionBackend(ABC):
    def client_session(self) -> Any:
        return StringSession(self.load())

    @abstractmethod
    def load(self) -> str | None:
        raise NotImplementedError

    @abstractmethod
    def save(self, session_string: str) -> None:
        raise NotImplementedError

    def lock_path(self) -> Path | None:
        return None


class StaticStringSessionBackend(SessionBackend):
    def __init__(self, session_string: str | None = None) -> None:
        self._session_string = session_string

    def load(self) -> str | None:
        return self._session_string

    def save(self, session_string: str) -> None:
        self._session_string = session_string


class EnvSessionBackend(SessionBackend):
    def __init__(self, name: str = "TELEGRAM_SESSION_STRING") -> None:
        self.name = name

    def load(self) -> str | None:
        return os.getenv(self.name)

    def save(self, session_string: str) -> None:
        os.environ[self.name] = session_string


class FileSessionBackend(SessionBackend):
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path).expanduser()

    def load(self) -> str | None:
        if not self.path.exists():
            return None
        value = self.path.read_text(encoding="utf-8").strip()
        return value or None

    def save(self, session_string: str) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(session_string + "\n", encoding="utf-8")
        try:
            self.path.chmod(0o600)
        except OSError:
            pass

    def lock_path(self) -> Path:
        return self.path.with_suffix(self.path.suffix + ".lock")


class TelethonSessionFileBackend(SessionBackend):
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path).expanduser()

    def client_session(self) -> str:
        return str(self.path)

    def load(self) -> str | None:
        return None

    def save(self, session_string: str) -> None:
        return None

    def lock_path(self) -> Path:
        return self.path.with_suffix(self.path.suffix + ".lock")


class SQLiteSessionBackend(SessionBackend):
    def __init__(self, path: str | Path, key: str = "default") -> None:
        self.path = Path(path).expanduser()
        self.key = key

    def load(self) -> str | None:
        if not self.path.exists():
            return None
        with self._connect() as connection:
            self._ensure_schema(connection)
            row = connection.execute(
                "select session_string from telegram_sessions where name = ?",
                (self.key,),
            ).fetchone()
            return row[0] if row else None

    def save(self, session_string: str) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as connection:
            self._ensure_schema(connection)
            connection.execute(
                """
                insert into telegram_sessions(name, session_string)
                values(?, ?)
                on conflict(name) do update set session_string = excluded.session_string
                """,
                (self.key, session_string),
            )

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.path)

    def lock_path(self) -> Path:
        return self.path.with_suffix(f".{self.key}.lock")

    @staticmethod
    def _ensure_schema(connection: sqlite3.Connection) -> None:
        connection.execute(
            """
            create table if not exists telegram_sessions(
                name text primary key,
                session_string text not null
            )
            """
        )


def encode_session_for_transport(session_string: str) -> str:
    return base64.urlsafe_b64encode(session_string.encode("utf-8")).decode("ascii")


def decode_session_from_transport(value: str) -> str:
    return base64.urlsafe_b64decode(value.encode("ascii")).decode("utf-8")


class SessionFileLock:
    _held_paths: set[Path] = set()

    def __init__(self, path: str | Path | None) -> None:
        self.path = Path(path).expanduser() if path else None
        self._handle: Any | None = None
        self._atexit_registered = False

    def acquire(self) -> None:
        if self.path is None or self._handle is not None:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        resolved_path = self.path.resolve()
        if resolved_path in self._held_paths:
            raise RuntimeError(f"Telegram session is already locked by this process: {self.path}")
        handle = self.path.open("a+", encoding="utf-8")
        try:
            lock_file_handle(handle)
        except OSError as exc:
            owner = read_lock_owner(self.path)
            handle.close()
            raise RuntimeError(
                f"Telegram session is already locked by another process: {self.path}"
                + (f" owner={owner}" if owner else "")
            ) from exc
        self._handle = handle
        self._held_paths.add(resolved_path)
        write_lock_owner(handle)
        if not self._atexit_registered:
            atexit.register(self.release)
            self._atexit_registered = True

    def release(self) -> None:
        handle = self._handle
        self._handle = None
        if handle is None:
            return
        resolved_path = self.path.resolve() if self.path is not None else None
        try:
            unlock_file_handle(handle)
        finally:
            handle.close()
            if resolved_path is not None:
                self._held_paths.discard(resolved_path)
            if self.path is not None:
                try:
                    self.path.unlink()
                except FileNotFoundError:
                    pass


def lock_file_handle(handle: Any) -> None:
    if os.name == "nt":
        import msvcrt

        handle.seek(0)
        if not handle.read(1):
            handle.write("0")
            handle.flush()
        handle.seek(0)
        msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        return
    import fcntl

    fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)


def unlock_file_handle(handle: Any) -> None:
    if os.name == "nt":
        import msvcrt

        handle.seek(0)
        try:
            msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
        except OSError:
            pass
        return
    import fcntl

    fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def write_lock_owner(handle: Any) -> None:
    metadata = {"pid": os.getpid(), "created_ts": int(time.time())}
    handle.seek(0)
    handle.truncate()
    handle.write(json.dumps(metadata, sort_keys=True))
    handle.flush()


def read_lock_owner(path: Path) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8") or "{}")
    except (OSError, json.JSONDecodeError):
        return None
    pid = data.get("pid")
    if isinstance(pid, int):
        data["pid_alive"] = is_pid_alive(pid)
    return data


def is_pid_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True

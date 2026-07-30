from __future__ import annotations

import asyncio
import base64
from contextlib import asynccontextmanager, contextmanager, suppress
from contextvars import ContextVar
from dataclasses import dataclass, field, replace
from datetime import datetime
import hashlib
import json
import logging
import os
from pathlib import Path
import random
import shutil
import sqlite3
import tempfile
import threading
import time
from typing import Any
from uuid import uuid4

from fastapi import FastAPI, HTTPException, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from starlette.responses import StreamingResponse
from telethon import events, utils
from telethon.errors import FloodWaitError, PasswordHashInvalidError, RPCError, SessionPasswordNeededError
from telethon.tl import functions, types
from telethon.tl.custom.dialog import Dialog
from telethon.tl.custom.message import Message
from telethon.tl.types import User

from tg_api_zapret.client import SentCode, TelegramLayer
from tg_api_zapret.config import (
    AppSettings,
    ClientProfile,
    OFFICIAL_DESKTOP_APP_VERSION,
    ServiceSettings,
    TelegramConfig,
    detect_lang_code,
    detect_system_lang_code,
    detect_system_version,
    normalize_account_name,
    validate_proxy_url,
)
from tg_api_zapret.mtproto_layers import get_layer_functions, require_layer_function
from tg_api_zapret.queue_backends import QueueBackend, build_queue_backend
from tg_api_zapret.sessions import FileSessionBackend, SQLiteSessionBackend, TelethonSessionFileBackend
from tg_api_zapret.tl_codec import (
    build_tl_object,
    build_tl_request,
    decode_tl_value,
    resolve_entity,
    serialize_tl,
)
from tg_api_zapret.version import __version__

REQUEST_SCOPES: ContextVar[list[str] | None] = ContextVar("REQUEST_SCOPES", default=None)
REQUEST_TELEGRAM_ACCOUNT: ContextVar[str | None] = ContextVar("REQUEST_TELEGRAM_ACCOUNT", default=None)
REQUEST_TELEGRAM_ACTION: ContextVar[str | None] = ContextVar("REQUEST_TELEGRAM_ACTION", default=None)
logger = logging.getLogger(__name__)


@dataclass
class DBWriteJob:
    func: Any
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    future: asyncio.Future[Any] | None
    category: str = "critical"
    backpressure: str = "wait"
    id: str = field(default_factory=lambda: uuid4().hex)
    attempt: int = 0
    created_ts: int = field(default_factory=lambda: int(time.time()))


class ApiState:
    def __init__(
        self,
        *,
        config_file: str,
        session_file: str,
        session_db: str | None = None,
        default_account: str = "default",
        queue_backend: str = "memory",
        redis_url: str | None = None,
    ) -> None:
        self.config_file = Path(config_file).expanduser()
        self.session_file = Path(session_file).expanduser()
        self.session_db = Path(session_db).expanduser() if session_db else None
        self.default_account = normalize_account_name(default_account)
        self.layers: dict[str, TelegramLayer] = {}
        service = self.settings().service
        self.queue: QueueBackend = build_queue_backend(
            queue_backend,
            redis_url=redis_url,
            visibility_timeout_seconds=service.queue_visibility_timeout_seconds,
        )
        self.rate_limits: dict[str, list[float]] = {}
        self.telegram_rate_limits: dict[str, list[float]] = {}
        self.telegram_account_rate_limits: dict[str, list[float]] = {}
        self.media_download_semaphores: dict[str, asyncio.Semaphore] = {}
        self.telegram_action_locks: dict[str, asyncio.Lock] = {}
        self.connection_locks: dict[str, asyncio.Lock] = {}
        self.telegram_auth_rate_limits: dict[str, list[float]] = {}
        self.telegram_cooldowns: dict[str, dict[str, Any]] = {}
        self.last_telegram_action_at: dict[str, float] = {}
        self.bot_updates: dict[str, list[dict[str, Any]]] = {}
        self.bot_update_ids: dict[str, int] = {}
        self.bot_update_handlers: dict[str, tuple[Any, Any]] = {}
        self.online_tasks: dict[str, asyncio.Task[None]] = {}
        self.online_status: dict[str, dict[str, Any]] = {}
        self._is_online: dict[str, bool] = {}
        self.idle_offline_tasks: dict[str, asyncio.Task[None]] = {}
        self.last_user_activity_at: dict[str, float] = {}
        self.last_online_status_at: dict[str, float] = {}
        self.next_online_allowed_at: dict[str, float] = {}
        self.reconnect_tasks: dict[str, asyncio.Task[None]] = {}
        self.retention_task: asyncio.Task[None] | None = None
        self.db_writer_task: asyncio.Task[None] | None = None
        self.db_write_queue: asyncio.Queue[DBWriteJob] = asyncio.Queue(
            maxsize=max(1, service.db_writer_queue_maxsize)
        )
        self.db_writer_accepting = False
        self.db_writer_shutdown_started = False
        self.db_writer_loop: asyncio.AbstractEventLoop | None = None
        self.db_writer_failed_writes = 0
        self.db_writer_dropped_writes = 0
        self.db_writer_dead_letters: list[dict[str, Any]] = []
        self.db_writer_status: dict[str, Any] = {
            "lifecycle": "stopped",
            "accepting": False,
            "running": False,
            "queued": 0,
            "failed_writes": 0,
            "dropped_writes": 0,
            "degraded": False,
        }
        self.last_state_vacuum_at: float = 0.0
        self.queue_worker_task: asyncio.Task[None] | None = None
        self.queue_worker_status: dict[str, Any] = {}
        self.update_handlers: dict[str, tuple[Any, Any]] = {}
        self.entity_cache: dict[str, dict[str, dict[str, Any]]] = {}
        self.connection_health: dict[str, dict[str, Any]] = {}
        self.account_states: dict[str, dict[str, Any]] = {}
        self.sync_states: dict[str, dict[str, int]] = {}
        self._state_db: sqlite3.Connection | None = None
        self._state_db_auto_vacuum_checked = False
        self.state_db_maintenance_status: dict[str, Any] = {}
        self.state_db_lock = threading.RLock()

    async def startup(self) -> None:
        service = self.settings().service
        await asyncio.to_thread(self.load_entity_cache)
        await asyncio.to_thread(self.load_sync_states)
        await asyncio.to_thread(self.prune_state_retention)
        self.start_db_writer()
        self.start_retention_loop()
        if service.queue_execute_in_api and not self.queue.runs_inline:
            self.start_queue_worker()
        for account in service.auto_connect_accounts:
            try:
                layer = await self.connect(account)
                if await layer.is_authorized():
                    await self.activate_desktop_like_runtime(account)
            except Exception as exc:
                account_name = normalize_account_name(account)
                self.connection_health[account_name] = {
                    "account": account_name,
                    "ok": False,
                    "error": str(exc),
                    "last_check_ts": int(time.time()),
                }
    def settings(self) -> AppSettings:
        return AppSettings.load(self.config_file)

    def save_settings(self, settings: AppSettings) -> None:
        settings.save(self.config_file)

    async def connect(self, account: str | None = None) -> TelegramLayer:
        account_name = self.resolve_account(account)
        async with self.connection_lock(account_name):
            return await self._connect_locked(account_name)

    async def _connect_locked(self, account_name: str) -> TelegramLayer:
        existing = self.layers.get(account_name)
        if existing and await self.layer_is_usable(account_name, existing):
            self.set_account_state(
                account_name,
                "authorized" if await existing.is_authorized() else "connected",
            )
            return existing
        settings = self.settings()
        self.set_account_state(account_name, "connecting")
        if self.session_db:
            backend = SQLiteSessionBackend(self.session_db, account_name)
        else:
            session_path = resolve_session_file(self.session_file, account_name)
            if account_name == "default" and session_path.suffix == ".session":
                backend = TelethonSessionFileBackend(session_path)
            else:
                backend = FileSessionBackend(session_path)
        layer = TelegramLayer(
            TelegramConfig.from_env(
                proxy_url=settings.proxy_url,
                client_profile=settings.client_profile,
            ),
            backend,
        )
        try:
            await layer.connect()
        except Exception:
            self.set_account_state(account_name, "disconnected")
            raise
        self.layers[account_name] = layer
        if account_name not in settings.accounts:
            self.save_settings(settings.with_account(account_name))
        if await layer.is_authorized():
            self.set_account_state(account_name, "authorized")
            await self.activate_desktop_like_runtime(account_name)
        else:
            self.set_account_state(account_name, "disconnected")
        return layer

    async def layer_is_usable(self, account: str, layer: TelegramLayer) -> bool:
        try:
            if not await layer.is_connected():
                return False
            if not await layer.is_authorized():
                return True
            cache_seconds = self.settings().service.connection_health_cache_seconds
            health = self.connection_health.get(account) or {}
            if health.get("ok") and time.time() - float(health.get("last_check_ts", 0)) < cache_seconds:
                return True
            client = await layer.authorized_client()
            await client(functions.PingRequest(ping_id=random.getrandbits(63)))
            self.connection_health[account] = {"account": account, "ok": True, "last_check_ts": int(time.time())}
            return True
        except Exception:
            self.invalidate_connection_health(account)
            return False

    def invalidate_connection_health(self, account: str | None = None, error: Exception | str | None = None) -> None:
        account_name = self.resolve_account(account)
        self.connection_health[account_name] = {
            "account": account_name,
            "ok": False,
            "invalidated_ts": int(time.time()),
            "error": str(error) if error else "connection health cache invalidated",
        }

    async def disconnect(self, account: str | None = None) -> None:
        if account is None:
            for account_name in list(self.online_tasks):
                await self.stop_online_keepalive(account_name)
            for account_name in list(self.reconnect_tasks):
                await self.stop_reconnect_loop(account_name)
            for account_name in list(self.idle_offline_tasks):
                await self.stop_idle_offline_timer(account_name)
            await self.stop_retention_loop()
            await self.stop_db_writer()
            await self.stop_queue_worker()
            for account_name in list(self.update_handlers):
                await self.stop_passive_update_receiver(account_name)
            for account_name, layer in list(self.layers.items()):
                async with self.connection_lock(account_name):
                    await layer.disconnect()
            self.layers.clear()
            await self.queue.close()
            self.close_state_db()
            return
        account_name = self.resolve_account(account)
        await self.stop_online_keepalive(account_name)
        await self.stop_reconnect_loop(account_name)
        await self.stop_idle_offline_timer(account_name)
        await self.stop_passive_update_receiver(account_name)
        async with self.connection_lock(account_name):
            layer = self.layers.pop(account_name, None)
            if layer:
                await layer.disconnect()
        self.set_account_state(account_name, "disconnected")

    async def require_layer(self, account: str | None = None) -> TelegramLayer:
        account_name = self.resolve_account(account)
        if account_name not in self.layers:
            return await self.connect(account_name)
        return self.layers[account_name]

    def resolve_account(self, account: str | None = None) -> str:
        account_name = normalize_account_name(account or self.default_account or self.settings().active_account)
        service = self.settings().service
        blocked = {normalize_account_name(item) for item in service.blocked_account_names}
        if account_name in blocked:
            raise ValueError(
                f"Unsafe demo account name '{account_name}' is blocked. "
                "Choose a real account alias, for example main/work/personal."
            )
        return account_name

    def start_online_keepalive(self, account: str) -> None:
        account_name = self.resolve_account(account)
        task = self.online_tasks.get(account_name)
        if task and not task.done():
            return
        self.online_tasks[account_name] = asyncio.create_task(self._online_keepalive_loop(account_name))

    async def activate_desktop_like_runtime(self, account: str) -> None:
        account_name = self.resolve_account(account)
        service = self.settings().service
        if service.keep_accounts_online:
            self.start_online_keepalive(account_name)
        if service.passive_update_receiver:
            await self.start_passive_update_receiver(account_name)
        if service.entity_cache_warmup_dialogs > 0 and not self.entity_cache.get(account_name):
            await self.warm_entity_cache(account_name, limit=self.entity_cache_warmup_limit())
        if service.reconnect_enabled:
            self.start_reconnect_loop(account_name)

    async def stop_online_keepalive(self, account: str) -> None:
        account_name = self.resolve_account(account)
        task = self.online_tasks.pop(account_name, None)
        if task:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
        await self.send_account_offline_if_online(account_name)
        self.online_status[account_name] = {
            "account": account_name,
            "keep_online": False,
            "last_update_ts": int(time.time()),
        }

    async def _online_keepalive_loop(self, account: str) -> None:
        while True:
            service = self.settings().service
            min_interval = max(15, service.online_update_min_interval_seconds)
            max_interval = max(min_interval, service.online_update_max_interval_seconds)
            interval = random.uniform(min_interval, max_interval)
            try:
                layer = await self.require_layer(account)
                if await layer.is_authorized():
                    client = await layer.authorized_client()
                    await client(functions.account.UpdateStatusRequest(offline=False))
                    self._is_online[account] = True
                    self.online_status[account] = {
                        "account": account,
                        "keep_online": True,
                        "connected": client.is_connected(),
                        "last_update_ts": int(time.time()),
                        "interval_seconds": round(interval, 2),
                    }
            except asyncio.CancelledError:
                raise
            except Exception as exc:
                self.online_status[account] = {
                    "account": account,
                    "keep_online": True,
                    "error": str(exc),
                    "last_update_ts": int(time.time()),
                    "interval_seconds": round(interval, 2),
                }
            await asyncio.sleep(interval)

    def start_reconnect_loop(self, account: str) -> None:
        account_name = self.resolve_account(account)
        task = self.reconnect_tasks.get(account_name)
        if task and not task.done():
            return
        self.reconnect_tasks[account_name] = asyncio.create_task(self._reconnect_loop(account_name))

    def start_queue_worker(self) -> None:
        task = self.queue_worker_task
        if task and not task.done():
            return
        self.queue_worker_task = asyncio.create_task(run_queue_worker(self))
        self.queue_worker_status = {
            "mode": "api_owned",
            "running": True,
            "started_ts": int(time.time()),
        }

    async def stop_queue_worker(self) -> None:
        task = self.queue_worker_task
        self.queue_worker_task = None
        if task:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
        if self.queue_worker_status:
            self.queue_worker_status.update({"running": False, "stopped_ts": int(time.time())})

    def start_db_writer(self) -> None:
        task = self.db_writer_task
        if task and not task.done():
            return
        self.db_writer_shutdown_started = False
        self.db_writer_loop = asyncio.get_running_loop()
        self.db_writer_accepting = True
        self.db_writer_status.update(
            {
                "lifecycle": "starting",
                "accepting": True,
                "running": False,
                "queued": self.db_write_queue.qsize(),
                "queue_maxsize": self.db_write_queue.maxsize,
            }
        )
        self.update_db_writer_queue_status()
        self.db_writer_task = asyncio.create_task(self._db_writer_loop())
        self.db_writer_status.update(
            {
                "lifecycle": "running",
                "running": True,
                "started_ts": int(time.time()),
            }
        )

    async def stop_db_writer(self) -> None:
        task = self.db_writer_task
        self.db_writer_shutdown_started = True
        self.db_writer_accepting = False
        self.db_writer_status.update(
            {
                "lifecycle": "stopping",
                "accepting": False,
                "running": bool(task and not task.done()),
                "queued": self.db_write_queue.qsize(),
            }
        )
        self.db_writer_task = None
        if task:
            await self.db_write_queue.join()
            task.cancel()
            with suppress(asyncio.CancelledError):
                await task
        if self.db_writer_status:
            self.db_writer_status.update(
                {
                    "lifecycle": "stopped",
                    "accepting": False,
                    "running": False,
                    "queued": self.db_write_queue.qsize(),
                    "stopped_ts": int(time.time()),
                }
            )
        self.db_writer_loop = None

    def update_db_writer_queue_status(self) -> None:
        queued = self.db_write_queue.qsize()
        maxsize = max(1, self.db_write_queue.maxsize)
        ratio = queued / maxsize
        threshold = self.settings().service.db_writer_degraded_queue_ratio
        degraded = ratio >= threshold or self.db_writer_status.get("alert") is True
        self.db_writer_status.update(
            {
                "queued": queued,
                "queue_maxsize": maxsize,
                "queue_fill_ratio": round(ratio, 4),
                "degraded": degraded,
            }
        )

    async def _db_writer_loop(self) -> None:
        while True:
            job = await self.db_write_queue.get()
            try:
                result = await self._run_db_write_job(job)
                if job.future and not job.future.done():
                    job.future.set_result(result)
            except asyncio.CancelledError:
                if job.future and not job.future.done():
                    job.future.cancel()
                raise
            except Exception as exc:
                self.record_db_write_failure(job, exc)
                if is_disk_full_error(exc):
                    self.db_writer_shutdown_started = True
                    self.db_writer_accepting = False
                    self.db_writer_status.update(
                        {
                            "lifecycle": "stopped",
                            "accepting": False,
                            "running": False,
                            "stopped_reason": "disk_full",
                            "degraded": True,
                        }
                    )
                    if job.future and not job.future.done():
                        job.future.set_exception(exc)
                    self.db_write_queue.task_done()
                    self.fail_pending_db_jobs(exc)
                    return
                if job.future and not job.future.done():
                    job.future.set_exception(exc)
            finally:
                if self.db_writer_status.get("lifecycle") != "stopped":
                    self.db_writer_status.update({"lifecycle": "running", "running": True, "last_write_ts": int(time.time())})
                    self.update_db_writer_queue_status()
                    self.db_write_queue.task_done()

    async def _run_db_write_job(self, job: DBWriteJob) -> Any:
        while True:
            try:
                return await asyncio.to_thread(job.func, *job.args, **job.kwargs)
            except Exception as exc:
                max_attempts = self.db_write_max_attempts(exc)
                if job.attempt >= max_attempts or max_attempts <= 0:
                    raise
                job.attempt += 1
                await asyncio.sleep(self.db_write_retry_delay(exc, job.attempt))

    def db_write_max_attempts(self, exc: Exception) -> int:
        service = self.settings().service
        if is_non_retryable_db_write_error(exc):
            return 0
        if is_sqlite_locked_error(exc):
            return max(0, service.db_writer_locked_retries)
        if is_io_retryable_error(exc):
            return max(0, service.db_writer_io_retries)
        return 0

    @staticmethod
    def db_write_retry_delay(exc: Exception, attempt: int) -> float:
        if is_sqlite_locked_error(exc):
            return min(2.0, 0.2 * attempt)
        if is_io_retryable_error(exc):
            return min(5.0, 0.5 * attempt)
        return 0.0

    def record_db_write_failure(self, job: DBWriteJob, exc: Exception) -> None:
        self.db_writer_failed_writes += 1
        entry = {
            "job_id": job.id,
            "function": getattr(job.func, "__name__", str(job.func)),
            "category": job.category,
            "attempt": job.attempt,
            "error_type": type(exc).__name__,
            "error": str(exc),
            "created_ts": job.created_ts,
            "failed_ts": int(time.time()),
        }
        ttl_cutoff = int(time.time()) - max(1, self.settings().service.db_writer_dead_letter_ttl_days) * 86400
        self.db_writer_dead_letters.append(entry)
        self.db_writer_dead_letters = [
            item for item in self.db_writer_dead_letters if int(item.get("failed_ts", 0)) >= ttl_cutoff
        ][-max(1, self.settings().service.db_writer_dead_letter_max_records):]
        alert_threshold = self.settings().service.db_writer_failed_alert_threshold
        self.db_writer_status.update(
            {
                "failed_writes": self.db_writer_failed_writes,
                "last_error": entry,
                "dead_letters": len(self.db_writer_dead_letters),
                "alert": self.db_writer_failed_writes >= alert_threshold,
                "degraded": self.db_writer_failed_writes >= alert_threshold,
            }
        )
        logger.warning(
            "DB writer failed: type=%s ts=%s path=%s job=%s",
            type(exc).__name__,
            int(time.time()),
            self.state_db_path(),
            job.id,
            exc_info=True,
        )

    def fail_pending_db_jobs(self, exc: Exception) -> None:
        while True:
            try:
                pending = self.db_write_queue.get_nowait()
            except asyncio.QueueEmpty:
                return
            self.record_db_write_failure(pending, exc)
            if pending.future and not pending.future.done():
                pending.future.set_exception(exc)
            self.db_write_queue.task_done()

    async def enqueue_db_write(
        self,
        func: Any,
        *args: Any,
        wait: bool = True,
        category: str = "critical",
        backpressure: str | None = None,
        **kwargs: Any,
    ) -> Any:
        current_loop = asyncio.get_running_loop()
        if self.db_writer_loop is not None and current_loop is not self.db_writer_loop:
            raise RuntimeError("DB writer enqueue attempted from a different event loop")
        if self.db_writer_shutdown_started or self.db_writer_status.get("stopped_reason"):
            raise RuntimeError("DB writer is shutting down or stopped")
        if not self.db_writer_task or self.db_writer_task.done():
            self.start_db_writer()
        if not self.db_writer_accepting:
            self.db_writer_failed_writes += 1
            self.db_writer_status.update(
                {
                    "failed_writes": self.db_writer_failed_writes,
                    "last_error": {
                        "error_type": "DBWriterNotAccepting",
                        "error": "DB writer is shutting down or stopped",
                        "failed_ts": int(time.time()),
                    },
                }
            )
            raise RuntimeError("DB writer is shutting down or stopped")
        drop_categories = set(self.settings().service.db_writer_drop_categories)
        policy = backpressure or ("drop" if category in drop_categories or not wait else "wait")
        future = current_loop.create_future() if wait else None
        job = DBWriteJob(func=func, args=args, kwargs=kwargs, future=future, category=category, backpressure=policy)
        if self.db_write_queue.full() and policy == "drop":
            self.db_writer_dropped_writes += 1
            self.db_writer_status.update(
                {
                    "dropped_writes": self.db_writer_dropped_writes,
                    "last_drop": {
                        "job_id": job.id,
                        "function": getattr(func, "__name__", str(func)),
                        "category": category,
                        "dropped_ts": int(time.time()),
                    },
                    "accepting": self.db_writer_accepting,
                }
            )
            self.update_db_writer_queue_status()
            return None
        await self.db_write_queue.put(job)
        self.db_writer_status.update({"accepting": self.db_writer_accepting})
        self.update_db_writer_queue_status()
        if future is None:
            return None
        return await future

    def start_retention_loop(self) -> None:
        task = self.retention_task
        if task and not task.done():
            return
        self.retention_task = asyncio.create_task(self._retention_loop())

    async def stop_retention_loop(self) -> None:
        task = self.retention_task
        self.retention_task = None
        if task:
            task.cancel()
            with suppress(asyncio.CancelledError):
                await task

    async def _retention_loop(self) -> None:
        while True:
            service = self.settings().service
            min_hours = max(1, service.state_retention_min_interval_hours)
            max_hours = max(min_hours, service.state_retention_max_interval_hours)
            await asyncio.sleep(random.uniform(min_hours * 3600, max_hours * 3600))
            try:
                await asyncio.to_thread(self.prune_state_retention)
            except Exception as exc:
                logger.warning(
                    "State retention failed: type=%s ts=%s path=%s",
                    type(exc).__name__,
                    int(time.time()),
                    self.state_db_path(),
                    exc_info=True,
                )
                if is_non_retryable_retention_error(exc):
                    if isinstance(exc, PermissionError):
                        logger.error("State retention disabled after permission error: path=%s", self.state_db_path())
                        return
                    continue
                retry_seconds = 30 if is_sqlite_locked_error(exc) else 300
                await asyncio.sleep(retry_seconds)
                try:
                    await asyncio.to_thread(self.prune_state_retention)
                except Exception as retry_exc:
                    logger.warning(
                        "State retention retry failed: type=%s ts=%s path=%s",
                        type(retry_exc).__name__,
                        int(time.time()),
                        self.state_db_path(),
                        exc_info=True,
                    )

    async def stop_reconnect_loop(self, account: str) -> None:
        account_name = self.resolve_account(account)
        task = self.reconnect_tasks.pop(account_name, None)
        if task:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

    async def _reconnect_loop(self, account: str) -> None:
        delay = self.settings().service.reconnect_min_delay_seconds
        while True:
            service = self.settings().service
            min_delay = max(1, service.reconnect_min_delay_seconds)
            max_delay = max(min_delay, service.reconnect_max_delay_seconds)
            try:
                async with self.connection_lock(account):
                    layer = self.layers.get(account) or await self._connect_locked(account)
                    client = await layer.authorized_client()
                    if not client.is_connected():
                        self.set_account_state(account, "reconnecting")
                        await layer.connect()
                    authorized = await layer.is_authorized()
                if authorized:
                    self.set_account_state(account, "authorized")
                    if service.keep_accounts_online:
                        self.start_online_keepalive(account)
                    if service.passive_update_receiver and account not in self.update_handlers:
                        await self.start_passive_update_receiver(account)
                    self.connection_health[account] = {
                        "account": account,
                        "ok": True,
                        "connected": client.is_connected(),
                        "last_check_ts": int(time.time()),
                    }
                    if service.entity_cache_warmup_dialogs > 0 and not self.entity_cache.get(account):
                        await self.warm_entity_cache(account, limit=self.entity_cache_warmup_limit())
                else:
                    self.set_account_state(account, "revoked")
                delay = min_delay
            except asyncio.CancelledError:
                raise
            except Exception as exc:
                self.connection_health[account] = {
                    "account": account,
                    "ok": False,
                    "error": str(exc),
                    "last_check_ts": int(time.time()),
                    "next_retry_seconds": round(delay, 2),
                }
                self.set_account_state(account, "disconnected")
                await asyncio.sleep(delay)
                delay = min(delay * 2, max_delay)
                continue
            await asyncio.sleep(delay)

    async def start_passive_update_receiver(self, account: str) -> None:
        account_name = self.resolve_account(account)
        if account_name in self.update_handlers:
            return
        layer = await self.require_layer(account_name)
        if not await layer.is_authorized():
            return
        client = await layer.authorized_client()

        async def handler(event: Any) -> None:
            await self.enqueue_db_write(
                self.apply_raw_update,
                account_name,
                event,
                wait=False,
                category="diagnostics",
            )
            self.online_status.setdefault(account_name, {})
            self.online_status[account_name].update(
                {
                    "account": account_name,
                    "last_update_ts": int(time.time()),
                    "last_update_type": type(event).__name__,
                    "passive_receiver": True,
                }
            )

        builder = events.Raw()
        client.add_event_handler(handler, builder)
        self.update_handlers[account_name] = (handler, builder)

    async def stop_passive_update_receiver(self, account: str) -> None:
        account_name = self.resolve_account(account)
        handler_tuple = self.update_handlers.pop(account_name, None)
        layer = self.layers.get(account_name)
        if not handler_tuple or not layer:
            return
        try:
            client = await layer.authorized_client()
            handler, builder = handler_tuple
            client.remove_event_handler(handler, builder)
        except Exception:
            pass

    async def warm_entity_cache(self, account: str, *, limit: int) -> dict[str, Any]:
        account_name = self.resolve_account(account)
        layer = await self.require_layer(account_name)
        dialogs = await layer.get_dialogs(limit=limit)
        cache: dict[str, dict[str, Any]] = {}
        for dialog in dialogs:
            serialized = serialize_dialog(dialog)
            cache[str(serialized["id"])] = serialized
            await self.enqueue_db_write(self.persist_dialog, account_name, serialized)
            username = serialized.get("username")
            if username:
                cache[f"@{username}".lower()] = serialized
                cache[str(username).lower()] = serialized
        self.entity_cache[account_name] = cache
        await self.enqueue_db_write(self.save_entity_cache)
        return {
            "account": account_name,
            "cached": len(cache),
            "dialog_limit": limit,
            "last_warmup_ts": int(time.time()),
        }

    async def check_connection_health(self, account: str | None = None) -> dict[str, Any]:
        account_name = self.resolve_account(account)
        timeout = self.settings().service.connection_health_timeout_seconds
        try:
            layer = await asyncio.wait_for(self.require_layer(account_name), timeout=timeout)
            connected = await asyncio.wait_for(layer.is_connected(), timeout=timeout)
            result = {
                "account": account_name,
                "ok": connected,
                "connected": connected,
                "last_check_ts": int(time.time()),
            }
        except Exception as exc:
            result = {
                "account": account_name,
                "ok": False,
                "error": str(exc),
                "last_check_ts": int(time.time()),
            }
        self.connection_health[account_name] = result
        if not result["ok"]:
            raise HTTPException(
                status_code=503,
                detail={
                    "message": "Telegram connection health check failed; auth request blocked",
                    "health": result,
                },
            )
        return result

    async def mark_user_activity(self, account: str | None = None, *, send_online: bool = False) -> None:
        account_name = self.resolve_account(account)
        now = time.monotonic()
        previous_activity = self.last_user_activity_at.get(account_name)
        self.last_user_activity_at[account_name] = now
        if not send_online:
            if self._is_online.get(account_name):
                self.schedule_idle_offline(account_name)
            return
        layer = await self.require_layer(account_name)
        if not await layer.is_authorized():
            return
        allowed_at = self.next_online_allowed_at.get(account_name, 0.0)
        long_pause = previous_activity is None or now - previous_activity > 300
        if not long_pause and now < allowed_at:
            if self._is_online.get(account_name):
                self.schedule_idle_offline(account_name)
            return
        client = await layer.authorized_client()
        try:
            await client(functions.account.UpdateStatusRequest(offline=False))
        except Exception:
            self._is_online[account_name] = False
            raise
        self._is_online[account_name] = True
        self.last_online_status_at[account_name] = now
        service = self.settings().service
        self.next_online_allowed_at[account_name] = now + random_interval(
            service.online_debounce_min_seconds,
            service.online_debounce_max_seconds,
            floor=1,
        )
        self.online_status[account_name] = {
            "account": account_name,
            "keep_online": False,
            "activity_online": True,
            "last_update_ts": int(time.time()),
        }
        self.schedule_idle_offline(account_name)

    def schedule_idle_offline(self, account: str) -> None:
        account_name = self.resolve_account(account)
        task = self.idle_offline_tasks.pop(account_name, None)
        if task:
            task.cancel()
        self.idle_offline_tasks[account_name] = asyncio.create_task(self._idle_offline_after(account_name))

    async def stop_idle_offline_timer(self, account: str) -> None:
        account_name = self.resolve_account(account)
        task = self.idle_offline_tasks.pop(account_name, None)
        if task:
            task.cancel()
            with suppress(asyncio.CancelledError):
                await task

    async def _idle_offline_after(self, account: str) -> None:
        service = self.settings().service
        idle_seconds = random_interval(
            service.activity_idle_min_seconds,
            service.activity_idle_max_seconds,
            floor=1,
        )
        try:
            await asyncio.sleep(idle_seconds)
            if not self._is_online.get(account):
                return
            last_activity = self.last_user_activity_at.get(account, 0.0)
            if time.monotonic() - last_activity < idle_seconds:
                return
            await self.send_account_offline_if_online(account)
            self.online_status[account] = {
                "account": account,
                "keep_online": False,
                "activity_online": False,
                "idle_offline": True,
                "last_update_ts": int(time.time()),
                "idle_seconds": round(idle_seconds, 2),
            }
        except asyncio.CancelledError:
            raise
        except Exception as exc:
            self.online_status[account] = {
                "account": account,
                "keep_online": False,
                "activity_online": False,
                "idle_offline_error": str(exc),
                "last_update_ts": int(time.time()),
            }
        finally:
            task = self.idle_offline_tasks.get(account)
            if task is asyncio.current_task():
                self.idle_offline_tasks.pop(account, None)

    async def send_account_offline_if_online(self, account: str) -> None:
        account_name = self.resolve_account(account)
        if not self._is_online.get(account_name):
            return
        layer = self.layers.get(account_name)
        if not layer or not await layer.is_authorized():
            self._is_online[account_name] = False
            return
        client = await layer.authorized_client()
        await client(functions.account.UpdateStatusRequest(offline=True))
        self._is_online[account_name] = False

    def load_sync_states(self) -> None:
        path = self.state_db_path()
        if not path.exists():
            return
        try:
            with self.state_db_context() as connection:
                rows = connection.execute("select account, pts, date, qts from sync_state").fetchall()
        except sqlite3.Error:
            return
        self.sync_states = {
            normalize_account_name(account): {"pts": int(pts), "date": int(date), "qts": int(qts)}
            for account, pts, date, qts in rows
        }

    def update_sync_state_from_object(
        self,
        account: str,
        value: Any,
        *,
        persist: bool = True,
    ) -> dict[str, int]:
        current = self.sync_states.get(account, {"pts": 0, "date": 0, "qts": 0})
        state = {
            "pts": int(getattr(value, "pts", current["pts"]) or current["pts"]),
            "date": to_unix_timestamp(getattr(value, "date", current["date"]) or current["date"]),
            "qts": int(getattr(value, "qts", current["qts"]) or current["qts"]),
        }
        self.sync_states[account] = state
        if persist:
            self.save_sync_state(account, state)
        return state

    def save_sync_state(self, account: str, state: dict[str, int]) -> None:
        path = self.state_db_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        with self.state_db_context() as connection:
            self.persist_sync_state(account, state, connection)

    def persist_sync_state(
        self,
        account: str,
        state: dict[str, int],
        connection: sqlite3.Connection,
    ) -> None:
        connection.execute(
            """
            insert into sync_state(account, pts, date, qts, updated_ts)
            values(?, ?, ?, ?, ?)
            on conflict(account) do update set
                pts = excluded.pts,
                date = excluded.date,
                qts = excluded.qts,
                updated_ts = excluded.updated_ts
            """,
            (account, state["pts"], state["date"], state["qts"], int(time.time())),
        )

    def apply_difference(self, account: str, difference: Any) -> None:
        with self.state_db_context() as connection:
            self.persist_update_bundle(account, "difference", difference, connection)
            state = getattr(difference, "state", None) or getattr(difference, "intermediate_state", None)
            if state is not None:
                current = self.update_sync_state_from_object(account, state, persist=False)
                self.persist_sync_state(account, current, connection)
            for user in getattr(difference, "users", []) or []:
                self.persist_entity(account, user, connection)
            for chat in getattr(difference, "chats", []) or []:
                self.persist_entity(account, chat, connection)
            for message in getattr(difference, "new_messages", []) or []:
                self.persist_message(account, message, connection)
            for message in getattr(difference, "new_encrypted_messages", []) or []:
                self.persist_message(account, message, connection)
            for update in getattr(difference, "other_updates", []) or []:
                self.apply_update_object(account, update, connection)
            for update in getattr(difference, "updates", []) or []:
                self.apply_update_object(account, update, connection)

    def apply_raw_update(self, account: str, event: Any) -> None:
        update = getattr(event, "original_update", event)
        self.apply_update_object(account, update)

    def apply_update_object(
        self,
        account: str,
        update: Any,
        connection: sqlite3.Connection | None = None,
    ) -> None:
        self.persist_update_bundle(account, type(update).__name__, update, connection)
        pts = getattr(update, "pts", None)
        if pts is not None:
            current = self.sync_states.get(account, {"pts": 0, "date": 0, "qts": 0})
            current["pts"] = max(int(current.get("pts", 0)), int(pts))
            date_value = getattr(update, "date", None)
            if date_value is not None:
                current["date"] = max(int(current.get("date", 0)), to_unix_timestamp(date_value))
            qts = getattr(update, "qts", None)
            if qts is not None:
                current["qts"] = max(int(current.get("qts", 0)), int(qts))
            self.sync_states[account] = current
            if connection is not None:
                self.persist_sync_state(account, current, connection)
            else:
                self.save_sync_state(account, current)
        message = getattr(update, "message", None)
        if message is not None:
            self.persist_message(account, message, connection)
        user = getattr(update, "user", None)
        if user is not None:
            self.persist_entity(account, user, connection)
        chat = getattr(update, "chat", None)
        if chat is not None:
            self.persist_entity(account, chat, connection)
        if "Read" in type(update).__name__:
            self.persist_read_state(account, update, connection)

    def persist_update_bundle(
        self,
        account: str,
        kind: str,
        value: Any,
        connection: sqlite3.Connection | None = None,
    ) -> None:
        payload = serialize_tl(value)
        if connection is not None:
            connection.execute(
                """
                insert into raw_updates(account, kind, payload_json, created_ts)
                values(?, ?, ?, ?)
                """,
                (account, kind, safe_json_dumps(payload), int(time.time())),
            )
            return
        with self.state_db_context() as connection:
            connection.execute(
                """
                insert into raw_updates(account, kind, payload_json, created_ts)
                values(?, ?, ?, ?)
                """,
                (account, kind, safe_json_dumps(payload), int(time.time())),
            )

    def persist_message(
        self,
        account: str,
        message: Any,
        connection: sqlite3.Connection | None = None,
    ) -> None:
        message_id = getattr(message, "id", None)
        peer_id = getattr(message, "peer_id", None) or getattr(message, "chat_id", None)
        peer_key = str(serialize_tl(peer_id)) if peer_id is not None else ""
        payload = serialize_tl(message)
        if connection is None:
            with self.state_db_context() as connection:
                self.persist_message(account, message, connection)
            return
        connection.execute(
            """
            insert into messages(account, peer_key, message_id, payload_json, updated_ts)
            values(?, ?, ?, ?, ?)
            on conflict(account, peer_key, message_id) do update set
                payload_json = excluded.payload_json,
                updated_ts = excluded.updated_ts
            """,
            (account, peer_key, int(message_id or 0), safe_json_dumps(payload), int(time.time())),
        )

    def persist_dialog(self, account: str, dialog: dict[str, Any]) -> None:
        dialog_id = str(dialog.get("id") or "")
        if not dialog_id:
            return
        with self.state_db_context() as connection:
            connection.execute(
                """
                insert into dialogs(account, dialog_id, payload_json, updated_ts)
                values(?, ?, ?, ?)
                on conflict(account, dialog_id) do update set
                    payload_json = excluded.payload_json,
                    updated_ts = excluded.updated_ts
                """,
                (account, dialog_id, safe_json_dumps(dialog), int(time.time())),
            )

    def persist_entity(
        self,
        account: str,
        entity: Any,
        connection: sqlite3.Connection | None = None,
    ) -> None:
        entity_id = getattr(entity, "id", None)
        if entity_id is None:
            return
        payload = serialize_tl(entity)
        entity_key = str(entity_id)
        self.entity_cache.setdefault(account, {})[entity_key] = payload
        username = payload.get("username") if isinstance(payload, dict) else None
        if username:
            self.entity_cache[account][f"@{username}".lower()] = payload
            self.entity_cache[account][str(username).lower()] = payload
        if connection is None:
            with self.state_db_context() as connection:
                self.persist_entity(account, entity, connection)
            return
        connection.execute(
            """
            insert into entities(account, entity_id, kind, payload_json, updated_ts)
            values(?, ?, ?, ?, ?)
            on conflict(account, entity_id) do update set
                kind = excluded.kind,
                payload_json = excluded.payload_json,
                updated_ts = excluded.updated_ts
            """,
            (
                account,
                entity_key,
                type(entity).__name__,
                safe_json_dumps(payload),
                int(time.time()),
            ),
        )

    def persist_read_state(
        self,
        account: str,
        update: Any,
        connection: sqlite3.Connection | None = None,
    ) -> None:
        peer = getattr(update, "peer", None) or getattr(update, "channel_id", None) or ""
        peer_key = str(serialize_tl(peer))
        max_id = int(getattr(update, "max_id", 0) or 0)
        payload = serialize_tl(update)
        if connection is None:
            with self.state_db_context() as connection:
                self.persist_read_state(account, update, connection)
            return
        connection.execute(
            """
            insert into read_state(account, peer_key, max_id, payload_json, updated_ts)
            values(?, ?, ?, ?, ?)
            on conflict(account, peer_key) do update set
                max_id = max(read_state.max_id, excluded.max_id),
                payload_json = excluded.payload_json,
                updated_ts = excluded.updated_ts
            """,
            (account, peer_key, max_id, safe_json_dumps(payload), int(time.time())),
        )

    def persist_read_command(self, account: str, entity: Any, max_id: int, result: Any) -> None:
        payload = {"entity": serialize_tl(entity), "result": serialize_tl(result)}
        with self.state_db_context() as connection:
            connection.execute(
                """
                insert into read_state(account, peer_key, max_id, payload_json, updated_ts)
                values(?, ?, ?, ?, ?)
                on conflict(account, peer_key) do update set
                    max_id = max(read_state.max_id, excluded.max_id),
                    payload_json = excluded.payload_json,
                    updated_ts = excluded.updated_ts
                """,
                (
                    account,
                    str(serialize_tl(entity)),
                    max_id,
                    safe_json_dumps(payload),
                    int(time.time()),
                ),
            )

    def load_entity_cache(self) -> None:
        path = self.state_db_path()
        if not path.exists():
            return
        try:
            with self.state_db_context() as connection:
                rows = connection.execute("select account, cache_json from entity_cache").fetchall()
        except sqlite3.Error:
            return
        cache: dict[str, dict[str, dict[str, Any]]] = {}
        for account, cache_json in rows:
            try:
                entities = json.loads(cache_json)
            except json.JSONDecodeError:
                continue
            if isinstance(entities, dict):
                cache[normalize_account_name(account)] = entities
        self.entity_cache = cache

    def save_entity_cache(self) -> None:
        path = self.state_db_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        with self.state_db_context() as connection:
            for account, entities in self.entity_cache.items():
                connection.execute(
                    """
                    insert into entity_cache(account, cache_json, updated_ts)
                    values(?, ?, ?)
                    on conflict(account) do update set
                        cache_json = excluded.cache_json,
                        updated_ts = excluded.updated_ts
                    """,
                    (account, json.dumps(entities, ensure_ascii=False), int(time.time())),
                )

    def state_db_path(self) -> Path:
        return self.config_file.with_suffix(".state.sqlite3")

    def open_state_db(self) -> sqlite3.Connection:
        path = self.state_db_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(path)
        connection.execute("pragma journal_mode=wal")
        connection.execute("pragma busy_timeout=5000")
        with self.state_db_lock:
            if not self._state_db_auto_vacuum_checked:
                auto_vacuum = int(connection.execute("pragma auto_vacuum").fetchone()[0] or 0)
                if auto_vacuum == 0:
                    connection.execute("pragma auto_vacuum=incremental")
                    self.state_db_maintenance_status.update(
                        {
                            "auto_vacuum": "none",
                            "migration_required": True,
                            "message": "Run POST /db/vacuum/migrate to enable incremental vacuum on this SQLite file.",
                        }
                    )
                elif auto_vacuum != 2:
                    connection.execute("pragma auto_vacuum=incremental")
                    self.state_db_maintenance_status.update(
                        {
                            "auto_vacuum": auto_vacuum,
                            "migration_required": True,
                            "message": "Run POST /db/vacuum/migrate to apply auto_vacuum change.",
                        }
                    )
                else:
                    self.state_db_maintenance_status.update(
                        {"auto_vacuum": "incremental", "migration_required": False}
                    )
                self._state_db_auto_vacuum_checked = True
        self.ensure_state_schema(connection)
        return connection

    @contextmanager
    def state_db_context(self):
        with self.state_db_lock:
            connection = self.open_state_db()
            try:
                with connection:
                    yield connection
            finally:
                connection.close()

    def close_state_db(self) -> None:
        with self.state_db_lock:
            self._state_db = None
            self._state_db_auto_vacuum_checked = False

    def prune_state_retention(self) -> None:
        service = self.settings().service
        now = int(time.time())
        raw_cutoff = now - max(1, service.raw_updates_retention_days) * 86400
        flood_cutoff = now - max(1, service.flood_errors_retention_days) * 86400
        idempotency_cutoff = now - max(1, service.idempotency_retention_hours) * 3600
        with self.state_db_context() as connection:
            connection.execute("delete from raw_updates where created_ts < ?", (raw_cutoff,))
            connection.execute("delete from flood_errors where created_ts < ?", (flood_cutoff,))
            connection.execute("delete from idempotency_keys where updated_ts < ?", (idempotency_cutoff,))
            max_records = max(1, service.idempotency_max_records)
            connection.execute(
                """
                delete from idempotency_keys
                where rowid in (
                    select rowid from idempotency_keys
                    order by updated_ts desc
                    limit -1 offset ?
                )
                """,
                (max_records,),
            )
        vacuum_interval = max(1, service.state_vacuum_interval_hours) * 3600
        if time.monotonic() - self.last_state_vacuum_at < vacuum_interval:
            return
        with self.state_db_lock:
            with self.state_db_context() as connection:
                freelist_count = int(connection.execute("pragma freelist_count").fetchone()[0] or 0)
                if freelist_count > 0:
                    connection.execute(f"pragma incremental_vacuum({min(freelist_count, 1000)})")
                self.last_state_vacuum_at = time.monotonic()

    def migrate_state_db_auto_vacuum(self) -> dict[str, Any]:
        path = self.state_db_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        db_size = path.stat().st_size if path.exists() else 0
        free_bytes = shutil.disk_usage(path.parent).free
        required_bytes = max(db_size * 2, 1)
        if free_bytes < required_bytes:
            raise HTTPException(
                status_code=507,
                detail={
                    "message": "Not enough free disk space for SQLite VACUUM migration.",
                    "db_size_bytes": db_size,
                    "free_bytes": free_bytes,
                    "required_bytes": required_bytes,
                },
            )
        with self.state_db_lock:
            started = int(time.time())
            self.state_db_maintenance_status.update(
                {
                    "migration_running": True,
                    "migration_started_ts": started,
                    "db_size_bytes": db_size,
                    "free_bytes_before": free_bytes,
                }
            )
            try:
                with self.state_db_context() as connection:
                    connection.execute("pragma auto_vacuum=incremental")
                    connection.execute("vacuum")
                    auto_vacuum = int(connection.execute("pragma auto_vacuum").fetchone()[0] or 0)
            except Exception as exc:
                self.state_db_maintenance_status.update(
                    {
                        "migration_running": False,
                        "migration_error": str(exc),
                        "migration_error_type": type(exc).__name__,
                        "migration_failed_ts": int(time.time()),
                    }
                )
                raise
            self._state_db_auto_vacuum_checked = False
            result = {
                "migration_running": False,
                "migration_required": auto_vacuum != 2,
                "auto_vacuum": auto_vacuum,
                "db_size_bytes": path.stat().st_size if path.exists() else 0,
                "free_bytes_after": shutil.disk_usage(path.parent).free,
                "migration_started_ts": started,
                "migration_finished_ts": int(time.time()),
            }
            self.state_db_maintenance_status.update(result)
            return result

    def begin_idempotent_action(
        self,
        account: str,
        action: str,
        key: str | None,
        payload: Any,
    ) -> tuple[str, str | None, dict[str, Any] | None]:
        if not key:
            return "missing", None, None
        payload_hash = idempotency_payload_hash(payload)
        now = int(time.time())
        lease_seconds = self.idempotency_lease_seconds_for_action(action, payload)
        with self.state_db_context() as connection:
            row = connection.execute(
                """
                select payload_hash, status, result_json, locked_until
                from idempotency_keys
                where account = ? and action = ? and idempotency_key = ?
                """,
                (account, action, key),
            ).fetchone()
            if row is not None:
                stored_hash, status, result_json, locked_until = row
                if stored_hash != payload_hash:
                    raise HTTPException(
                        status_code=409,
                        detail="Idempotency key was already used with a different payload.",
                    )
                if status == "completed":
                    return "completed", payload_hash, json.loads(result_json or "{}")
                if int(locked_until or 0) <= now and status in {"in_progress", "failed_retryable"}:
                    connection.execute(
                        """
                        update idempotency_keys
                        set status = 'in_progress', locked_until = ?, updated_ts = ?
                        where account = ? and action = ? and idempotency_key = ?
                        """,
                        (
                            now + lease_seconds,
                            now,
                            account,
                            action,
                            key,
                        ),
                    )
                    return "started", payload_hash, None
                raise HTTPException(
                    status_code=409,
                    detail=f"Idempotent request is {status}.",
                )
            connection.execute(
                """
                insert into idempotency_keys(
                    account, action, idempotency_key, payload_hash, status,
                    locked_until, created_ts, updated_ts
                )
                values(?, ?, ?, ?, 'in_progress', ?, ?, ?)
                """,
                (
                    account,
                    action,
                    key,
                    payload_hash,
                    now + lease_seconds,
                    now,
                    now,
                ),
            )
        return "started", payload_hash, None

    def refresh_idempotent_action(
        self,
        account: str,
        action: str,
        key: str | None,
        payload_hash: str | None,
        lease_seconds: int | None = None,
    ) -> None:
        if not key or not payload_hash:
            return
        now = int(time.time())
        locked_until = now + max(1, lease_seconds or self.idempotency_lease_seconds_for_action(action))
        with self.state_db_context() as connection:
            connection.execute(
                """
                update idempotency_keys
                set locked_until = ?, updated_ts = ?
                where account = ? and action = ? and idempotency_key = ?
                    and payload_hash = ? and status = 'in_progress'
                """,
                (locked_until, now, account, action, key, payload_hash),
            )

    async def idempotency_heartbeat(
        self,
        account: str,
        action: str,
        key: str | None,
        payload_hash: str | None,
        lease_seconds: int | None = None,
    ) -> None:
        if not key or not payload_hash:
            return
        service = self.settings().service
        min_seconds = max(1, service.idempotency_heartbeat_min_seconds)
        max_seconds = max(min_seconds, service.idempotency_heartbeat_max_seconds)
        while True:
            await asyncio.sleep(random.uniform(min_seconds, max_seconds))
            await asyncio.to_thread(
                self.refresh_idempotent_action,
                account,
                action,
                key,
                payload_hash,
                lease_seconds,
            )

    def idempotency_lease_seconds_for_action(self, action: str, payload: Any | None = None) -> int:
        service = self.settings().service
        if action in {"media.send", "files.upload", "media.download"}:
            if payload_has_large_file(payload):
                return service.idempotency_large_file_lease_seconds
            return service.idempotency_media_lease_seconds
        if action.startswith("messages."):
            return service.idempotency_message_lease_seconds
        return service.idempotency_lease_seconds

    def complete_idempotent_action(
        self,
        account: str,
        action: str,
        key: str | None,
        payload_hash: str | None,
        result: dict[str, Any],
    ) -> None:
        if not key or not payload_hash:
            return
        result_json = safe_json_dumps(result)
        max_bytes = max(1, self.settings().service.idempotency_result_max_bytes)
        if len(result_json.encode("utf-8")) > max_bytes:
            result_json = safe_json_dumps(
                {
                    "_": "IdempotencyResultTooLarge",
                    "stored": False,
                    "max_bytes": max_bytes,
                }
            )
        with self.state_db_context() as connection:
            connection.execute(
                """
                update idempotency_keys
                set status = 'completed', result_json = ?, locked_until = 0, updated_ts = ?
                where account = ? and action = ? and idempotency_key = ? and payload_hash = ?
                """,
                (result_json, int(time.time()), account, action, key, payload_hash),
            )

    def mark_idempotent_action(
        self,
        account: str,
        action: str,
        key: str | None,
        payload_hash: str | None,
        status: str,
    ) -> None:
        if not key or not payload_hash:
            return
        now = int(time.time())
        locked_until = now + self.idempotency_lease_seconds_for_action(action)
        with self.state_db_context() as connection:
            connection.execute(
                """
                update idempotency_keys
                set status = ?, locked_until = ?, updated_ts = ?
                where account = ? and action = ? and idempotency_key = ? and payload_hash = ?
                """,
                (status, locked_until, now, account, action, key, payload_hash),
            )

    def resolve_idempotent_action(
        self,
        account: str,
        action: str,
        key: str,
        status: str,
        result: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        account_name = self.resolve_account(account)
        now = int(time.time())
        result_json = safe_json_dumps(result or {}) if status == "completed" else None
        with self.state_db_context() as connection:
            row = connection.execute(
                """
                select status
                from idempotency_keys
                where account = ? and action = ? and idempotency_key = ?
                """,
                (account_name, action, key),
            ).fetchone()
            if row is None:
                raise HTTPException(status_code=404, detail="Idempotency key not found.")
            connection.execute(
                """
                update idempotency_keys
                set status = ?, result_json = ?, locked_until = 0, updated_ts = ?
                where account = ? and action = ? and idempotency_key = ?
                """,
                (status, result_json, now, account_name, action, key),
            )
        return {
            "account": account_name,
            "action": action,
            "idempotency_key": key,
            "previous_status": row[0],
            "status": status,
        }

    @staticmethod
    def ensure_state_schema(connection: sqlite3.Connection) -> None:
        connection.execute(
            """
            create table if not exists schema_meta(
                key text primary key,
                value text not null
            )
            """
        )
        connection.execute(
            """
            insert into schema_meta(key, value)
            values('schema_version', '1')
            on conflict(key) do nothing
            """
        )
        connection.execute(
            """
            create table if not exists entity_cache(
                account text primary key,
                cache_json text not null,
                updated_ts integer not null
            )
            """
        )
        connection.execute(
            """
            create table if not exists sync_state(
                account text primary key,
                pts integer not null default 0,
                date integer not null default 0,
                qts integer not null default 0,
                updated_ts integer not null
            )
            """
        )
        connection.execute(
            """
            create table if not exists raw_updates(
                id integer primary key autoincrement,
                account text not null,
                kind text not null,
                payload_json text not null,
                created_ts integer not null
            )
            """
        )
        connection.execute(
            """
            create table if not exists messages(
                account text not null,
                peer_key text not null,
                message_id integer not null,
                payload_json text not null,
                updated_ts integer not null,
                primary key(account, peer_key, message_id)
            )
            """
        )
        connection.execute(
            """
            create table if not exists dialogs(
                account text not null,
                dialog_id text not null,
                payload_json text not null,
                updated_ts integer not null,
                primary key(account, dialog_id)
            )
            """
        )
        connection.execute(
            """
            create table if not exists entities(
                account text not null,
                entity_id text not null,
                kind text not null,
                payload_json text not null,
                updated_ts integer not null,
                primary key(account, entity_id)
            )
            """
        )
        connection.execute(
            """
            create table if not exists read_state(
                account text not null,
                peer_key text not null,
                max_id integer not null default 0,
                payload_json text not null,
                updated_ts integer not null,
                primary key(account, peer_key)
            )
            """
        )
        connection.execute(
            """
            create table if not exists flood_errors(
                id integer primary key autoincrement,
                account text not null,
                action text not null,
                telegram_retry_after_seconds integer not null,
                retry_after_seconds integer not null,
                created_ts integer not null
            )
            """
        )
        connection.execute(
            """
            create table if not exists idempotency_keys(
                account text not null,
                action text not null,
                idempotency_key text not null,
                payload_hash text not null,
                status text not null,
                result_json text,
                locked_until integer not null default 0,
                created_ts integer not null,
                updated_ts integer not null,
                primary key(account, action, idempotency_key)
            )
            """
        )
        ensure_sqlite_column(
            connection,
            "idempotency_keys",
            "locked_until",
            "integer not null default 0",
        )

    def set_account_state(self, account: str, state: str) -> None:
        account_name = self.resolve_account(account)
        self.account_states[account_name] = {
            "account": account_name,
            "state": state,
            "updated_ts": int(time.time()),
        }

    def entity_cache_warmup_limit(self) -> int:
        service = self.settings().service
        minimum = max(0, service.entity_cache_warmup_min_dialogs)
        maximum = max(minimum, service.entity_cache_warmup_max_dialogs)
        if maximum == 0:
            return service.entity_cache_warmup_dialogs
        return random.randint(minimum, maximum)

    def media_download_semaphore(self, account: str | None = None) -> asyncio.Semaphore:
        account_name = self.resolve_account(account)
        limit = self.settings().service.telegram_media_download_concurrency
        semaphore = self.media_download_semaphores.get(account_name)
        if semaphore is None:
            semaphore = asyncio.Semaphore(limit)
            self.media_download_semaphores[account_name] = semaphore
        return semaphore

    def telegram_action_lock(self, account: str | None = None) -> asyncio.Lock:
        account_name = self.resolve_account(account)
        lock = self.telegram_action_locks.get(account_name)
        if lock is None:
            lock = asyncio.Lock()
            self.telegram_action_locks[account_name] = lock
        return lock

    def connection_lock(self, account: str | None = None) -> asyncio.Lock:
        account_name = self.resolve_account(account)
        lock = self.connection_locks.get(account_name)
        if lock is None:
            lock = asyncio.Lock()
            self.connection_locks[account_name] = lock
        return lock

    def record_flood_wait(self, account: str | None, action: str | None, seconds: int | None) -> None:
        account_name = self.resolve_account(account)
        base_retry_after = max(
            1,
            int(seconds or self.settings().service.telegram_default_flood_cooldown_seconds),
        )
        retry_after = max(1, int(base_retry_after * random.uniform(1.0, 1.05)))
        self.telegram_cooldowns[account_name] = {
            "account": account_name,
            "action": action or "unknown",
            "telegram_retry_after_seconds": base_retry_after,
            "retry_after_seconds": retry_after,
            "until_ts": int(time.time() + retry_after),
            "recorded_ts": int(time.time()),
        }
        self.persist_flood_wait(account_name, action or "unknown", base_retry_after, retry_after)

    def persist_flood_wait(
        self,
        account: str,
        action: str,
        telegram_retry_after_seconds: int,
        retry_after_seconds: int,
    ) -> None:
        with self.state_db_context() as connection:
            connection.execute(
                """
                insert into flood_errors(
                    account,
                    action,
                    telegram_retry_after_seconds,
                    retry_after_seconds,
                    created_ts
                )
                values(?, ?, ?, ?, ?)
                """,
                (
                    account,
                    action,
                    telegram_retry_after_seconds,
                    retry_after_seconds,
                    int(time.time()),
                ),
            )


class ProxyPayload(BaseModel):
    proxy_url: str | None = None


class AccountPayload(BaseModel):
    account: str


class AccountConnectPayload(BaseModel):
    account: str | None = None
    keep_online: bool = False


class ClientProfilePayload(BaseModel):
    device_model: str = Field(default="Telegram Desktop", min_length=1)
    system_version: str = Field(default_factory=detect_system_version, min_length=1)
    app_version: str = Field(default=OFFICIAL_DESKTOP_APP_VERSION, min_length=1)
    lang_code: str = Field(default_factory=detect_lang_code, min_length=1)
    system_lang_code: str = Field(default_factory=detect_system_lang_code, min_length=1)


class ServiceSettingsPayload(BaseModel):
    api_name: str = "tg-api-zapret"
    public_base_url: str | None = None
    default_api_interface: str = "rest"
    enabled_interfaces: list[str] = Field(
        default_factory=lambda: ["rest", "json_rpc", "websocket", "sse", "queue", "python_sdk"]
    )
    max_queue_jobs_list: int = Field(default=1000, ge=1)
    stream_queue_size: int = Field(default=100, ge=1)
    request_timeout_seconds: int = Field(default=60, ge=1)
    expose_docs: bool = False
    cors_origins: list[str] = Field(default_factory=list)
    require_api_token: bool = True
    api_token_env: str = "TG_API_TOKEN"
    api_tokens_env: str = "TG_API_TOKENS"
    rate_limit_per_minute: int = Field(default=120, ge=0)
    audit_log_path: str | None = None
    enable_raw_invoke: bool = False
    enable_layer_invoke: bool = False
    bot_token_accounts: dict[str, str] = Field(default_factory=dict)
    telegram_actions_per_minute: int = Field(default=20, ge=1)
    telegram_safe_mode: bool = True
    telegram_serialize_account_actions: bool = True
    telegram_send_actions_per_minute: int = Field(default=6, ge=1)
    telegram_resolve_actions_per_minute: int = Field(default=10, ge=1)
    telegram_raw_actions_per_minute: int = Field(default=3, ge=1)
    telegram_join_actions_per_hour: int = Field(default=5, ge=1)
    telegram_destructive_actions_per_hour: int = Field(default=10, ge=1)
    telegram_media_downloads_per_minute: int = Field(default=30, ge=1)
    telegram_media_download_concurrency: int = Field(default=2, ge=1, le=4)
    telegram_auth_requests_per_hour: int = Field(default=3, ge=1)
    telegram_requests_per_second: int = Field(default=10, ge=1)
    telegram_requests_per_minute: int = Field(default=50, ge=1)
    telegram_requests_per_hour: int = Field(default=500, ge=1)
    telegram_read_requests_per_second: int = Field(default=5, ge=1)
    telegram_send_requests_per_second: int = Field(default=2, ge=1)
    telegram_typing_requests_per_second: int = Field(default=1, ge=1)
    telegram_sync_requests_per_minute: int = Field(default=2, ge=1)
    max_dialog_limit: int = Field(default=100, ge=1)
    max_message_limit: int = Field(default=100, ge=1)
    blocked_account_names: list[str] = Field(default_factory=lambda: ["string", "account"])
    telegram_min_action_interval_seconds: float = Field(default=1.25, ge=0)
    telegram_default_flood_cooldown_seconds: int = Field(default=300, ge=1)
    queue_visibility_timeout_seconds: int = Field(default=300, ge=1)
    queue_default_max_attempts: int = Field(default=3, ge=1)
    queue_execute_in_api: bool = True
    db_writer_queue_maxsize: int = Field(default=5000, ge=1)
    db_writer_locked_retries: int = Field(default=3, ge=0)
    db_writer_io_retries: int = Field(default=2, ge=0)
    db_writer_failed_alert_threshold: int = Field(default=10, ge=1)
    db_writer_dead_letter_max_records: int = Field(default=500, ge=1, le=1000)
    db_writer_dead_letter_ttl_days: int = Field(default=30, ge=1)
    db_writer_degraded_queue_ratio: float = Field(default=0.8, ge=0.1, le=1.0)
    db_writer_drop_categories: list[str] = Field(default_factory=lambda: ["diagnostics", "typing", "presence"])
    keep_accounts_online: bool = False
    online_update_interval_seconds: int = Field(default=300, ge=15)
    online_update_min_interval_seconds: int = Field(default=300, ge=15)
    online_update_max_interval_seconds: int = Field(default=900, ge=15)
    activity_idle_min_seconds: int = Field(default=120, ge=1)
    activity_idle_max_seconds: int = Field(default=300, ge=1)
    online_debounce_min_seconds: int = Field(default=30, ge=1)
    online_debounce_max_seconds: int = Field(default=60, ge=1)
    auto_connect_accounts: list[str] = Field(default_factory=list)
    reconnect_enabled: bool = True
    reconnect_min_delay_seconds: int = Field(default=5, ge=1)
    reconnect_max_delay_seconds: int = Field(default=120, ge=1)
    passive_update_receiver: bool = True
    entity_cache_warmup_dialogs: int = Field(default=50, ge=0)
    entity_cache_warmup_min_dialogs: int = Field(default=40, ge=0)
    entity_cache_warmup_max_dialogs: int = Field(default=60, ge=0)
    require_connection_health_before_auth: bool = True
    connection_health_timeout_seconds: int = Field(default=20, ge=1)
    connection_health_cache_seconds: int = Field(default=30, ge=0)
    raw_updates_retention_days: int = Field(default=7, ge=1)
    flood_errors_retention_days: int = Field(default=30, ge=1)
    idempotency_retention_hours: int = Field(default=48, ge=1)
    idempotency_max_records: int = Field(default=10000, ge=1)
    idempotency_lease_seconds: int = Field(default=300, ge=1)
    idempotency_message_lease_seconds: int = Field(default=300, ge=60)
    idempotency_media_lease_seconds: int = Field(default=3600, ge=300)
    idempotency_large_file_lease_seconds: int = Field(default=7200, ge=300)
    idempotency_heartbeat_min_seconds: int = Field(default=30, ge=1)
    idempotency_heartbeat_max_seconds: int = Field(default=60, ge=1)
    idempotency_result_max_bytes: int = Field(default=1048576, ge=1024)
    state_retention_min_interval_hours: int = Field(default=12, ge=1)
    state_retention_max_interval_hours: int = Field(default=24, ge=1)
    state_vacuum_interval_hours: int = Field(default=24, ge=1)


class SendCodePayload(BaseModel):
    phone: str


class ConfirmCodePayload(BaseModel):
    phone: str
    phone_code_hash: str
    code: str


class PasswordPayload(BaseModel):
    password: str


class SendMessagePayload(BaseModel):
    entity: str | int
    text: str
    parse_mode: str | None = None
    idempotency_key: str | None = None


class MessageListPayload(BaseModel):
    entity: Any
    limit: int = 50


class TypingPayload(BaseModel):
    entity: str | int


class ReadMessagesPayload(BaseModel):
    entity: str | int
    max_id: int = Field(default=0, ge=0)


class DraftPayload(BaseModel):
    entity: str | int
    text: str = ""
    no_webpage: bool = False
    reply_to_msg_id: int | None = None


class SendUsernameMessagePayload(BaseModel):
    username: str = Field(description="Telegram username with or without @, phone, or t.me link.")
    text: str
    parse_mode: str | None = None
    idempotency_key: str | None = None


class EditMessagePayload(BaseModel):
    entity: str | int
    message_id: int
    text: str


class DeleteMessagesPayload(BaseModel):
    entity: str | int
    message_ids: list[int]
    revoke: bool = True


class ForwardMessagesPayload(BaseModel):
    from_entity: str | int
    to_entity: str | int
    message_ids: list[int]


class SendMediaPayload(BaseModel):
    entity: str | int
    file_path: str | None = None
    file_base64: str | None = None
    file_name: str | None = None
    caption: str | None = None
    parse_mode: str | None = None
    idempotency_key: str | None = None


class DownloadMediaPayload(BaseModel):
    entity: str | int
    message_id: int
    output_path: str | None = None
    as_base64: bool = True


class UploadFilePayload(BaseModel):
    file_path: str | None = None
    file_base64: str | None = None
    file_name: str | None = None


class IdempotencyResolvePayload(BaseModel):
    account: str | None = None
    action: str
    idempotency_key: str
    status: str = Field(pattern="^(failed_retryable|failed_final|completed)$")
    result: dict[str, Any] | None = None


class EntityPayload(BaseModel):
    entity: str | int


class JoinLeavePayload(BaseModel):
    entity: str | int


class ReactionPayload(BaseModel):
    entity: str | int
    message_id: int
    reaction: str | dict[str, Any] | list[dict[str, Any]] | None = None
    big: bool | None = None
    add_to_recent: bool | None = None


class StoryGetPayload(BaseModel):
    entity: str | int
    story_ids: list[int]


class StorySendPayload(BaseModel):
    peer: str | int
    media: dict[str, Any]
    privacy_rules: list[dict[str, Any]]
    caption: str | None = None
    period: int | None = None
    pinned: bool | None = None
    noforwards: bool | None = None
    extra: dict[str, Any] = Field(default_factory=dict)


class AdminBanPayload(BaseModel):
    channel: str | int
    participant: str | int
    banned_rights: dict[str, Any] = Field(
        default_factory=lambda: {
            "_": "ChatBannedRights",
            "until_date": None,
            "view_messages": True,
        }
    )


class AdminPromotePayload(BaseModel):
    channel: str | int
    user: str | int
    admin_rights: dict[str, Any] = Field(default_factory=lambda: {"_": "ChatAdminRights"})
    rank: str | None = None


class TypeConstructorPayload(BaseModel):
    constructor: str = Field(description="TL type name, for example InputPeerUser or ReactionEmoji.")
    fields: dict[str, Any] = Field(default_factory=dict)


class RawInvokePayload(BaseModel):
    request: str = Field(
        description="Telethon TL function path, for example users.GetFullUserRequest"
    )
    kwargs: dict[str, Any] = Field(default_factory=dict)


class MtprotoLayerInvokePayload(BaseModel):
    request: str = Field(
        description="Layer function callable path, for example messages.SendMessageRequest"
    )
    kwargs: dict[str, Any] = Field(default_factory=dict)


class JsonRpcRequest(BaseModel):
    jsonrpc: str = "2.0"
    method: str
    params: dict[str, Any] = Field(default_factory=dict)
    id: str | int | None = None


class QueueJobPayload(BaseModel):
    kind: str
    account: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)
    idempotency_key: str | None = None
    max_attempts: int | None = Field(default=None, ge=1)


class ActionResolvePayload(BaseModel):
    task: str = Field(description="Natural task or known intent, for example send_message.")
    account: str | None = None
    params: dict[str, Any] = Field(default_factory=dict)
    realtime: bool = False
    background: bool = False
    bidirectional: bool = False
    client_language: str | None = None


class ActionExecutePayload(ActionResolvePayload):
    pass


def create_app(state: ApiState) -> FastAPI:
    @asynccontextmanager
    async def lifespan(_: FastAPI):
        try:
            await state.startup()
            yield
        finally:
            await state.disconnect()

    app = FastAPI(title="tg-api-zapret", version=__version__, lifespan=lifespan)
    startup_service = state.settings().service
    if startup_service.cors_origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=startup_service.cors_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    @app.middleware("http")
    async def security_middleware(request: Request, call_next):
        service = state.settings().service
        if not service.expose_docs and request.url.path in {"/docs", "/redoc", "/openapi.json"}:
            return JSONResponse({"detail": "Documentation is disabled"}, status_code=404)

        token = extract_bearer_token(request.headers.get("authorization"))
        scopes = token_scopes(service, token)
        if service.require_api_token and scopes is None and request.url.path != "/health":
            await audit_request(state, request, 401, token)
            return JSONResponse({"detail": "Missing or invalid API token"}, status_code=401)
        scope_token = REQUEST_SCOPES.set(scopes)

        rate_key = token_hash(token) if token else request.client.host if request.client else "unknown"
        if not check_rate_limit(state, rate_key, service.rate_limit_per_minute):
            await audit_request(state, request, 429, token)
            REQUEST_SCOPES.reset(scope_token)
            return JSONResponse({"detail": "Rate limit exceeded"}, status_code=429)

        account = request.query_params.get("account")
        if scopes is not None and account and not account_allowed(scopes, account):
            await audit_request(state, request, 403, token)
            REQUEST_SCOPES.reset(scope_token)
            return JSONResponse({"detail": "Account is not allowed for this token"}, status_code=403)
        if account:
            try:
                state.resolve_account(account)
            except ValueError as exc:
                await audit_request(state, request, 400, token)
                REQUEST_SCOPES.reset(scope_token)
                return JSONResponse({"detail": str(exc)}, status_code=400)

        action_lock: asyncio.Lock | None = None
        if service.telegram_safe_mode and service.telegram_serialize_account_actions and should_serialize_http_path(request.url.path):
            try:
                action_lock = state.telegram_action_lock(account)
                await action_lock.acquire()
            except ValueError as exc:
                await audit_request(state, request, 400, token)
                REQUEST_SCOPES.reset(scope_token)
                return JSONResponse({"detail": str(exc)}, status_code=400)

        try:
            response = await asyncio.wait_for(
                call_next(request),
                timeout=service.request_timeout_seconds,
            )
            await audit_request(state, request, response.status_code, token)
            return response
        except TimeoutError:
            await audit_request(state, request, 504, token)
            return JSONResponse({"detail": "Request timeout"}, status_code=504)
        except FloodWaitError as exc:
            flood_account = REQUEST_TELEGRAM_ACCOUNT.get() or account
            flood_action = REQUEST_TELEGRAM_ACTION.get()
            state.invalidate_connection_health(flood_account, exc)
            state.record_flood_wait(flood_account, flood_action, getattr(exc, "seconds", None))
            await audit_request(state, request, 429, token)
            return JSONResponse(
                {
                    "detail": "Telegram flood wait",
                    "account": state.resolve_account(flood_account),
                    "action": flood_action or "unknown",
                    "seconds": getattr(exc, "seconds", None),
                    "retry_after": getattr(exc, "seconds", None),
                },
                status_code=429,
                headers={"Retry-After": str(getattr(exc, "seconds", 60))},
            )
        except RPCError as exc:
            state.invalidate_connection_health(REQUEST_TELEGRAM_ACCOUNT.get() or account, exc)
            await audit_request(state, request, 502, token)
            return JSONResponse(
                {
                    "detail": "Telegram RPC error",
                    "type": type(exc).__name__,
                    "message": str(exc),
                },
                status_code=502,
            )
        except PermissionError as exc:
            await audit_request(state, request, 401, token)
            return JSONResponse({"detail": str(exc)}, status_code=401)
        except ValueError as exc:
            await audit_request(state, request, 400, token)
            return JSONResponse({"detail": str(exc)}, status_code=400)
        except ConnectionError as exc:
            state.invalidate_connection_health(REQUEST_TELEGRAM_ACCOUNT.get() or account, exc)
            await audit_request(state, request, 503, token)
            return JSONResponse(
                {"detail": "Telegram connection failed", "message": str(exc)},
                status_code=503,
            )
        finally:
            if action_lock and action_lock.locked():
                action_lock.release()
            REQUEST_SCOPES.reset(scope_token)

    @app.get("/health")
    async def health() -> JSONResponse:
        db_writer = state.db_writer_status
        degraded = bool(db_writer.get("degraded") or db_writer.get("alert"))
        payload = {
            "status": "ok",
            "server_os": "windows" if os.name == "nt" else "linux",
            "path_style": "windows" if os.name == "nt" else "posix",
            "db_writer": db_writer,
        }
        if degraded:
            payload["status"] = "degraded"
            return JSONResponse(payload, status_code=503)
        return JSONResponse(payload)

    @app.get("/capabilities")
    async def capabilities() -> dict[str, Any]:
        return {
            "interfaces": {
                "rest": {
                    "description": "Simple request/response commands.",
                    "endpoints": [
                        "GET /dialogs",
                        "POST /accounts/connect",
                        "POST /accounts/disconnect",
                        "GET /accounts/online",
                        "GET /accounts/health",
                        "GET /accounts/risk-status",
                        "GET /db/writer/status",
                        "GET /db/maintenance/status",
                        "POST /db/vacuum/migrate",
                        "POST /accounts/entity-cache/warm",
                        "GET /accounts/entity-cache",
                        "GET /accounts/sync-state",
                        "POST /accounts/sync/difference",
                        "POST /idempotency/resolve",
                        "POST /messages/list",
                        "POST /messages/typing",
                        "POST /messages/read",
                        "POST /drafts/save",
                        "POST /messages/send",
                        "POST /messages/send-username",
                        "POST /messages/edit",
                        "POST /messages/delete",
                        "POST /messages/forward",
                        "POST /messages/history/delete",
                        "POST /messages/reaction",
                        "POST /media/send",
                        "POST /media/download",
                        "POST /media/download/stream",
                        "POST /files/upload",
                        "POST /entities/resolve",
                        "POST /chats/join",
                        "POST /chats/leave",
                        "POST /stories/get",
                        "POST /stories/send",
                        "POST /admin/ban",
                        "POST /admin/promote",
                        "POST /tl/construct",
                        "POST /raw/invoke",
                        "GET /mtproto/layers/{layer}/functions",
                        "POST /mtproto/layers/{layer}/invoke",
                        "POST /bot{token}/{method}",
                    ],
                },
                "json_rpc": {
                    "description": "Single endpoint for command-style integrations.",
                    "endpoint": "POST /rpc",
                    "methods": sorted(RPC_METHODS),
                },
                "websocket": {
                    "description": "Bidirectional realtime updates.",
                    "endpoint": "WS /ws/updates",
                },
                "sse": {
                    "description": "One-way realtime event stream.",
                    "endpoint": "GET /events",
                },
                "queue": {
                    "description": "Background jobs. Backends: memory, redis. Telegram jobs are executed by the API owner process.",
                    "endpoints": [
                        "POST /queue/jobs",
                        "GET /queue/jobs/{job_id}",
                        "GET /queue/status",
                        "GET /db/writer/status",
                    ],
                    "execution_owner": "api_process",
                },
                "python_sdk": {
                    "description": "Python client wrapper around HTTP/JSON-RPC/Queue APIs.",
                    "class": "tg_api_zapret.TgApiZapretClient",
                },
                "bot_api_compat": {
                    "description": "Limited Bot API compatibility layer, not a full Telegram Bot API proxy.",
                    "endpoint": "GET|POST /bot{token}/{method}",
                    "methods": sorted(BOT_API_COMPAT_METHODS),
                },
            },
            "service_settings": state.settings().service.to_dict(),
            "actions": ACTIONS,
        }

    @app.post("/actions/resolve")
    async def resolve_action(payload: ActionResolvePayload) -> dict[str, Any]:
        return resolve_api_method(payload, state.settings().service)

    @app.post("/actions/execute")
    async def execute_action(payload: ActionExecutePayload) -> dict[str, Any]:
        ensure_account_allowed_for_payload(state, payload.account)
        plan = resolve_api_method(payload, state.settings().service)
        if plan["interface"] == "queue":
            queue_payload = QueueJobPayload(
                kind=plan["rpc_method"],
                account=payload.account,
                payload=payload.params,
            )
            job_id = uuid4().hex
            job = await state.queue.create_job({
                "id": job_id,
                "kind": queue_payload.kind,
                "account": state.resolve_account(queue_payload.account),
                "payload": queue_payload.payload,
                "idempotency_key": queue_payload.idempotency_key,
                "attempts": 0,
                "max_attempts": queue_payload.max_attempts
                or state.settings().service.queue_default_max_attempts,
                "status": "queued",
                "result": None,
                "error": None,
            })
            if state.queue.runs_inline:
                asyncio.create_task(run_queue_job(state, job_id, queue_payload))
            return {"plan": plan, "job": job}
        if not plan.get("executable", False):
            return {"plan": plan, "status": "not_executable"}
        result = await dispatch_rpc(
            state,
            plan["rpc_method"],
            {"account": payload.account, **payload.params},
        )
        return {"plan": plan, "result": result}

    @app.websocket("/ws/updates")
    async def websocket_updates(websocket: WebSocket, account: str | None = None) -> None:
        await ensure_websocket_allowed(state, websocket, account)
        await websocket.accept()
        queue: asyncio.Queue[dict[str, Any]] = asyncio.Queue(
            maxsize=state.settings().service.stream_queue_size
        )
        client = await require_authorized_client(state, account)

        async def handler(event: events.NewMessage.Event) -> None:
            await queue.put(
                {
                    "type": "new_message",
                    "account": state.resolve_account(account),
                    "message": serialize_message(event.message),
                }
            )

        client.add_event_handler(handler, events.NewMessage())
        try:
            while True:
                await websocket.send_json(await queue.get())
        except WebSocketDisconnect:
            pass
        finally:
            client.remove_event_handler(handler, events.NewMessage())

    @app.get("/events")
    async def sse_events(account: str | None = None) -> StreamingResponse:
        queue: asyncio.Queue[dict[str, Any]] = asyncio.Queue(
            maxsize=state.settings().service.stream_queue_size
        )
        client = await require_authorized_client(state, account)

        async def handler(event: events.NewMessage.Event) -> None:
            await queue.put(
                {
                    "type": "new_message",
                    "account": state.resolve_account(account),
                    "message": serialize_message(event.message),
                }
            )

        async def stream():
            client.add_event_handler(handler, events.NewMessage())
            try:
                while True:
                    event = await queue.get()
                    yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
            finally:
                client.remove_event_handler(handler, events.NewMessage())

        return StreamingResponse(stream(), media_type="text/event-stream")

    @app.get("/config")
    async def get_config() -> dict[str, Any]:
        settings = state.settings()
        return {
            "proxy_url": mask_url_secret(settings.proxy_url),
            "client_profile": settings.client_profile.to_dict(),
            "service": settings.service.to_dict(),
            "active_account": settings.active_account,
            "accounts": settings.accounts,
        }

    @app.get("/app/settings")
    async def get_app_settings() -> dict[str, Any]:
        return state.settings().service.to_dict()

    @app.put("/app/settings")
    async def set_app_settings(payload: ServiceSettingsPayload) -> dict[str, Any]:
        service = ServiceSettings.from_dict(payload.model_dump())
        settings = state.settings()
        state.save_settings(replace(settings, service=service))
        return service.to_dict()

    @app.patch("/app/settings")
    async def patch_app_settings(payload: dict[str, Any]) -> dict[str, Any]:
        current = state.settings()
        merged = {**current.service.to_dict(), **payload}
        service = ServiceSettings.from_dict(merged)
        state.save_settings(replace(current, service=service))
        return service.to_dict()

    @app.get("/accounts")
    async def accounts() -> dict[str, Any]:
        settings = state.settings()
        return visible_accounts_response(settings, REQUEST_SCOPES.get())

    @app.post("/accounts")
    async def add_account(payload: AccountPayload) -> dict[str, Any]:
        ensure_safe_account_payload(state, payload.account)
        settings = state.settings().with_account(payload.account)
        state.save_settings(settings)
        return {"active_account": settings.active_account, "accounts": settings.accounts}

    @app.post("/accounts/connect")
    async def connect_account(payload: AccountConnectPayload) -> dict[str, Any]:
        account_name = state.resolve_account(payload.account)
        layer = await state.require_layer(account_name)
        authorized = await layer.is_authorized()
        if authorized:
            await state.activate_desktop_like_runtime(account_name)
        return {
            "account": account_name,
            "connected": True,
            "authorized": authorized,
            "keep_online": state.settings().service.keep_accounts_online and authorized,
            "online_status": state.online_status.get(account_name),
        }

    @app.post("/accounts/disconnect")
    async def disconnect_account(payload: AccountConnectPayload) -> dict[str, Any]:
        account_name = state.resolve_account(payload.account)
        await state.disconnect(account_name)
        return {"account": account_name, "connected": False, "keep_online": False}

    @app.get("/accounts/online")
    async def online_accounts() -> dict[str, Any]:
        return {
            "keep_accounts_online": state.settings().service.keep_accounts_online,
            "accounts": state.online_status,
            "connection_health": state.connection_health,
            "account_states": state.account_states,
            "running_tasks": sorted(
                account for account, task in state.online_tasks.items() if not task.done()
            ),
            "reconnect_tasks": sorted(
                account for account, task in state.reconnect_tasks.items() if not task.done()
            ),
            "passive_receivers": sorted(state.update_handlers),
            "idle_offline_tasks": sorted(
                account for account, task in state.idle_offline_tasks.items() if not task.done()
            ),
            "queue_worker": state.queue_worker_status,
            "db_writer": state.db_writer_status,
        }

    @app.get("/db/writer/status")
    async def db_writer_status() -> dict[str, Any]:
        return {
            "writer": state.db_writer_status,
            "dead_letters": state.db_writer_dead_letters,
        }

    @app.get("/db/maintenance/status")
    async def db_maintenance_status() -> dict[str, Any]:
        return {
            "state_db": str(state.state_db_path()),
            "maintenance": state.state_db_maintenance_status,
        }

    @app.post("/db/vacuum/migrate")
    async def migrate_db_vacuum() -> dict[str, Any]:
        ensure_admin_scope()
        return await asyncio.to_thread(state.migrate_state_db_auto_vacuum)

    @app.post("/idempotency/resolve")
    async def resolve_idempotency(payload: IdempotencyResolvePayload) -> dict[str, Any]:
        ensure_admin_scope()
        account_name = state.resolve_account(payload.account)
        ensure_account_allowed_for_payload(state, account_name)
        return await asyncio.to_thread(
            state.resolve_idempotent_action,
            account_name,
            payload.action,
            payload.idempotency_key,
            payload.status,
            payload.result,
        )

    @app.get("/queue/status")
    async def queue_status() -> dict[str, Any]:
        task = state.queue_worker_task
        return {
            "backend_runs_inline": state.queue.runs_inline,
            "execute_in_api": state.settings().service.queue_execute_in_api,
            "api_worker_running": bool(task and not task.done()),
            "worker": state.queue_worker_status,
            "db_writer": state.db_writer_status,
        }

    @app.get("/accounts/health")
    async def account_health(account: str | None = None) -> dict[str, Any]:
        if account is not None:
            return await state.check_connection_health(account)
        results: dict[str, Any] = {}
        for account_name in state.settings().accounts:
            try:
                results[account_name] = await state.check_connection_health(account_name)
            except HTTPException as exc:
                results[account_name] = {
                    "account": account_name,
                    "ok": False,
                    "status_code": exc.status_code,
                    "error": exc.detail,
                }
        return {"accounts": results}

    @app.get("/accounts/risk-status")
    async def account_risk_status(account: str | None = None) -> dict[str, Any]:
        service = state.settings().service
        accounts = [state.resolve_account(account)] if account else state.settings().accounts
        now = int(time.time())
        statuses: dict[str, Any] = {}
        for account_name in accounts:
            cooldown = state.telegram_cooldowns.get(account_name)
            active_cooldown = None
            if cooldown and int(cooldown.get("until_ts", 0)) > now:
                active_cooldown = {
                    **cooldown,
                    "remaining_seconds": int(cooldown["until_ts"]) - now,
                }
            statuses[account_name] = {
                "account": account_name,
                "safe_mode": service.telegram_safe_mode,
                "serialized_actions": service.telegram_serialize_account_actions,
                "active_cooldown": active_cooldown,
                "last_action_monotonic": state.last_telegram_action_at.get(account_name),
                "online_status": state.online_status.get(account_name),
                "connection_health": state.connection_health.get(account_name),
                "account_state": state.account_states.get(account_name),
            }
        return {
            "accounts": statuses,
            "limits": telegram_limit_summary(service),
        }

    @app.post("/accounts/entity-cache/warm")
    async def warm_account_entity_cache(
        account: str | None = None,
        limit: int = 50,
    ) -> dict[str, Any]:
        limit = clamp_limit(limit, state.settings().service.max_dialog_limit)
        return await state.warm_entity_cache(state.resolve_account(account), limit=limit)

    @app.get("/accounts/entity-cache")
    async def account_entity_cache(account: str | None = None) -> dict[str, Any]:
        account_name = state.resolve_account(account)
        entities = state.entity_cache.get(account_name, {})
        return {
            "account": account_name,
            "count": len(entities),
            "entities": entities,
        }

    @app.get("/accounts/sync-state")
    async def account_sync_state(account: str | None = None) -> dict[str, Any]:
        account_name = state.resolve_account(account)
        return {
            "account": account_name,
            "state": state.sync_states.get(account_name, {"pts": 0, "date": 0, "qts": 0}),
            "state_db": str(state.state_db_path()),
        }

    @app.post("/accounts/sync/difference")
    async def run_account_difference(
        account: str | None = None,
        recovery: bool = False,
    ) -> dict[str, Any]:
        if not recovery:
            raise HTTPException(
                status_code=403,
                detail=(
                    "Manual GetDifference is a recovery endpoint. "
                    "Call with recovery=true only when repairing local sync state."
                ),
            )
        ensure_admin_scope()
        ensure_telegram_rate(state, account, "updates.difference")
        account_name = state.resolve_account(account)
        client = await require_authorized_client(state, account_name)
        sync_state = state.sync_states.get(account_name)
        if sync_state is None:
            state_result = await client(functions.updates.GetStateRequest())
            sync_state = await asyncio.to_thread(
                state.update_sync_state_from_object,
                account_name,
                state_result,
            )
        difference = await client(
            functions.updates.GetDifferenceRequest(
                pts=sync_state.get("pts", 0),
                date=sync_state.get("date", 0),
                qts=sync_state.get("qts", 0),
            )
        )
        await state.enqueue_db_write(state.apply_difference, account_name, difference)
        return {
            "account": account_name,
            "type": type(difference).__name__,
            "state": state.sync_states.get(account_name),
        }

    @app.put("/config/proxy")
    async def set_proxy(payload: ProxyPayload) -> dict[str, Any]:
        if payload.proxy_url:
            validate_proxy_url(payload.proxy_url)
        settings = state.settings()
        state.save_settings(replace(settings, proxy_url=payload.proxy_url))
        await reconnect(state)
        return {"proxy_url": mask_url_secret(payload.proxy_url)}

    @app.put("/config/client-profile")
    async def set_client_profile(payload: ClientProfilePayload) -> dict[str, Any]:
        settings = state.settings()
        profile = ClientProfile(**payload.model_dump())
        state.save_settings(replace(settings, client_profile=profile))
        await reconnect(state)
        return {"client_profile": profile.to_dict()}

    @app.get("/auth/status")
    async def auth_status(account: str | None = None) -> dict[str, Any]:
        layer = await state.require_layer(account)
        return {"account": state.resolve_account(account), "authorized": await layer.is_authorized()}

    @app.post("/auth/send-code")
    async def send_code(payload: SendCodePayload, account: str | None = None) -> dict[str, str]:
        ensure_telegram_auth_rate(state, account)
        if state.settings().service.require_connection_health_before_auth:
            await state.check_connection_health(state.resolve_account(account))
        layer = await state.require_layer(account)
        sent = await layer.send_code(payload.phone)
        return {
            "account": state.resolve_account(account),
            "phone": sent.phone,
            "phone_code_hash": sent.phone_code_hash,
        }

    @app.post("/auth/confirm-code")
    async def confirm_code(payload: ConfirmCodePayload, account: str | None = None) -> dict[str, str]:
        ensure_telegram_auth_rate(state, account)
        layer = await state.require_layer(account)
        try:
            await layer.sign_in(
                SentCode(phone=payload.phone, phone_code_hash=payload.phone_code_hash),
                payload.code,
            )
        except SessionPasswordNeededError:
            return {"status": "password_required"}
        await state.activate_desktop_like_runtime(state.resolve_account(account))
        await state.mark_user_activity(account, send_online=True)
        return {"status": "authorized"}

    @app.post("/auth/password")
    async def confirm_password(payload: PasswordPayload, account: str | None = None) -> dict[str, str]:
        ensure_telegram_auth_rate(state, account)
        layer = await state.require_layer(account)
        try:
            await layer.sign_in_password(payload.password)
        except PasswordHashInvalidError as exc:
            raise HTTPException(status_code=400, detail="Invalid two-step password") from exc
        await state.activate_desktop_like_runtime(state.resolve_account(account))
        await state.mark_user_activity(account, send_online=True)
        return {"status": "authorized"}

    @app.get("/me")
    async def me(account: str | None = None) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "me")
        client = await require_authorized_client(state, account)
        return serialize_user(await client.get_me())

    @app.get("/dialogs")
    async def dialogs(limit: int = 20, account: str | None = None) -> list[dict[str, Any]]:
        ensure_telegram_rate(state, account, "dialogs")
        limit = clamp_limit(limit, state.settings().service.max_dialog_limit)
        layer = await state.require_layer(account)
        account_name = state.resolve_account(account)
        result = []
        for dialog in await layer.get_dialogs(limit=limit):
            serialized = serialize_dialog(dialog)
            await state.enqueue_db_write(state.persist_dialog, account_name, serialized)
            await state.enqueue_db_write(state.persist_entity, account_name, dialog.entity)
            result.append(serialized)
        return result

    @app.get("/messages/{entity}")
    async def messages(
        entity: str,
        limit: int = 50,
        account: str | None = None,
    ) -> list[dict[str, Any]]:
        ensure_telegram_rate(state, account, "messages")
        limit = clamp_limit(limit, state.settings().service.max_message_limit)
        client = await require_authorized_client(state, account)
        decoded_entity = await decode_entity_argument(entity, client)
        return [
            serialize_message(message)
            async for message in client.iter_messages(decoded_entity, limit=limit)
        ]

    @app.post("/messages/list")
    async def list_messages(
        payload: MessageListPayload,
        account: str | None = None,
    ) -> list[dict[str, Any]]:
        ensure_telegram_rate(state, account, "messages")
        limit = clamp_limit(payload.limit, state.settings().service.max_message_limit)
        client = await require_authorized_client(state, account)
        decoded_entity = await decode_entity_argument(payload.entity, client)
        return [
            serialize_message(message)
            async for message in client.iter_messages(decoded_entity, limit=limit)
        ]

    @app.post("/messages/send")
    async def send_message(
        payload: SendMessagePayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "messages.send")
        account_name = state.resolve_account(account)
        idempotency_key = make_action_idempotency_key(
            account_name,
            "messages.send",
            payload.idempotency_key,
        )
        idem_status, payload_hash, cached_result = await asyncio.to_thread(
            state.begin_idempotent_action,
            account_name,
            "messages.send",
            idempotency_key,
            payload.model_dump(),
        )
        if idem_status == "completed" and cached_result is not None:
            return cached_result
        lease_seconds = state.idempotency_lease_seconds_for_action("messages.send", payload.model_dump())
        heartbeat_task = asyncio.create_task(
            state.idempotency_heartbeat(
                account_name,
                "messages.send",
                idempotency_key,
                payload_hash,
                lease_seconds,
            )
        )
        await state.mark_user_activity(account, send_online=True)
        try:
            layer = await state.require_layer(account)
            message = await retry_telegram_call(
                lambda: layer.send_message(
                    payload.entity,
                    payload.text,
                    parse_mode=payload.parse_mode,
                )
            )
            result = serialize_message(message)
            await asyncio.to_thread(
                state.complete_idempotent_action,
                account_name,
                "messages.send",
                idempotency_key,
                payload_hash,
                result,
            )
        except Exception:
            await asyncio.to_thread(
                state.mark_idempotent_action,
                account_name,
                "messages.send",
                idempotency_key,
                payload_hash,
                "outcome_unknown",
            )
            raise
        finally:
            heartbeat_task.cancel()
            with suppress(asyncio.CancelledError):
                await heartbeat_task
        return result

    @app.post("/messages/typing")
    async def set_typing(
        payload: TypingPayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "messages.typing")
        await state.mark_user_activity(account)
        client = await require_authorized_client(state, account)
        peer = await resolve_entity(payload.entity, client=client)
        result = await client(
            functions.messages.SetTypingRequest(
                peer=peer,
                action=types.SendMessageTypingAction(),
            )
        )
        return {"result": serialize_tl(result)}

    @app.post("/messages/read")
    async def read_messages(
        payload: ReadMessagesPayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "messages.read")
        await state.mark_user_activity(account)
        client = await require_authorized_client(state, account)
        peer = await resolve_entity(payload.entity, client=client)
        result = await client(
            functions.messages.ReadHistoryRequest(
                peer=peer,
                max_id=payload.max_id,
            )
        )
        await state.enqueue_db_write(
            state.persist_read_command,
            state.resolve_account(account),
            peer,
            payload.max_id,
            result,
        )
        return {"result": serialize_tl(result)}

    @app.post("/drafts/save")
    async def save_draft(
        payload: DraftPayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "drafts.save")
        await state.mark_user_activity(account)
        client = await require_authorized_client(state, account)
        peer = await resolve_entity(payload.entity, client=client)
        result = await client(
            functions.messages.SaveDraftRequest(
                peer=peer,
                message=payload.text,
                no_webpage=payload.no_webpage,
                reply_to_msg_id=payload.reply_to_msg_id,
            )
        )
        return {"result": serialize_tl(result)}

    @app.post("/messages/send-username")
    async def send_username_message(
        payload: SendUsernameMessagePayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "messages.send")
        account_name = state.resolve_account(account)
        idempotency_key = make_action_idempotency_key(
            account_name,
            "messages.send_username",
            payload.idempotency_key,
        )
        idem_status, payload_hash, cached_result = await asyncio.to_thread(
            state.begin_idempotent_action,
            account_name,
            "messages.send_username",
            idempotency_key,
            payload.model_dump(),
        )
        if idem_status == "completed" and cached_result is not None:
            return cached_result
        lease_seconds = state.idempotency_lease_seconds_for_action(
            "messages.send_username",
            payload.model_dump(),
        )
        heartbeat_task = asyncio.create_task(
            state.idempotency_heartbeat(
                account_name,
                "messages.send_username",
                idempotency_key,
                payload_hash,
                lease_seconds,
            )
        )
        await state.mark_user_activity(account, send_online=True)
        try:
            layer = await state.require_layer(account)
            message = await retry_telegram_call(
                lambda: layer.send_message(
                    normalize_username_entity(payload.username),
                    payload.text,
                    parse_mode=payload.parse_mode,
                )
            )
            result = serialize_message(message)
            await asyncio.to_thread(
                state.complete_idempotent_action,
                account_name,
                "messages.send_username",
                idempotency_key,
                payload_hash,
                result,
            )
        except Exception:
            await asyncio.to_thread(
                state.mark_idempotent_action,
                account_name,
                "messages.send_username",
                idempotency_key,
                payload_hash,
                "outcome_unknown",
            )
            raise
        finally:
            heartbeat_task.cancel()
            with suppress(asyncio.CancelledError):
                await heartbeat_task
        return result

    @app.post("/messages/edit")
    async def edit_message(
        payload: EditMessagePayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "messages.edit")
        client = await require_authorized_client(state, account)
        message = await client.edit_message(payload.entity, payload.message_id, payload.text)
        return serialize_message(message)

    @app.post("/messages/delete")
    async def delete_messages(
        payload: DeleteMessagesPayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "messages.delete")
        client = await require_authorized_client(state, account)
        result = await client.delete_messages(
            payload.entity,
            payload.message_ids,
            revoke=payload.revoke,
        )
        return {"result": str(result)}

    @app.post("/messages/forward")
    async def forward_messages(
        payload: ForwardMessagesPayload,
        account: str | None = None,
    ) -> list[dict[str, Any]]:
        ensure_telegram_rate(state, account, "messages.forward")
        client = await require_authorized_client(state, account)
        result = await client.forward_messages(
            payload.to_entity,
            payload.message_ids,
            from_peer=payload.from_entity,
        )
        messages = result if isinstance(result, list) else [result]
        return [serialize_message(message) for message in messages]

    @app.post("/messages/history/delete")
    async def delete_history(
        payload: EntityPayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "messages.history.delete")
        client = await require_authorized_client(state, account)
        peer = await resolve_entity(payload.entity, client=client)
        result = await client(functions.messages.DeleteHistoryRequest(peer=peer, max_id=0))
        return {"result": serialize_tl(result)}

    @app.post("/messages/reaction")
    async def send_reaction(
        payload: ReactionPayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "messages.reaction")
        client = await require_authorized_client(state, account)
        peer = await resolve_entity(payload.entity, client=client)
        reaction = await build_reaction(payload.reaction, client)
        result = await client(
            functions.messages.SendReactionRequest(
                peer=peer,
                msg_id=payload.message_id,
                big=payload.big,
                add_to_recent=payload.add_to_recent,
                reaction=reaction,
            )
        )
        return {"result": serialize_tl(result)}

    @app.post("/media/send")
    async def send_media(
        payload: SendMediaPayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "media.send")
        account_name = state.resolve_account(account)
        idempotency_key = make_action_idempotency_key(
            account_name,
            "media.send",
            payload.idempotency_key,
        )
        idem_status, payload_hash, cached_result = await asyncio.to_thread(
            state.begin_idempotent_action,
            account_name,
            "media.send",
            idempotency_key,
            payload.model_dump(),
        )
        if idem_status == "completed" and cached_result is not None:
            return cached_result
        lease_seconds = state.idempotency_lease_seconds_for_action("media.send", payload.model_dump())
        heartbeat_task = asyncio.create_task(
            state.idempotency_heartbeat(
                account_name,
                "media.send",
                idempotency_key,
                payload_hash,
                lease_seconds,
            )
        )
        await state.mark_user_activity(account, send_online=True)
        try:
            client = await require_authorized_client(state, account)
            file_value, cleanup = decode_upload_file(payload.file_path, payload.file_base64, payload.file_name)
            try:
                message = await client.send_file(
                    payload.entity,
                    file_value,
                    caption=payload.caption,
                    parse_mode=payload.parse_mode,
                )
            finally:
                if cleanup:
                    Path(cleanup).unlink(missing_ok=True)
            result = serialize_message(message)
            await asyncio.to_thread(
                state.complete_idempotent_action,
                account_name,
                "media.send",
                idempotency_key,
                payload_hash,
                result,
            )
        except Exception:
            await asyncio.to_thread(
                state.mark_idempotent_action,
                account_name,
                "media.send",
                idempotency_key,
                payload_hash,
                "outcome_unknown",
            )
            raise
        finally:
            heartbeat_task.cancel()
            with suppress(asyncio.CancelledError):
                await heartbeat_task
        return result

    @app.post("/media/download")
    async def download_media(
        payload: DownloadMediaPayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "media.download")
        client = await require_authorized_client(state, account)
        message = await client.get_messages(payload.entity, ids=payload.message_id)
        if not message:
            raise HTTPException(status_code=404, detail="Message not found")
        if payload.output_path:
            async with state.media_download_semaphore(account):
                output = await client.download_media(message, file=payload.output_path)
            return {"path": str(output) if output else None}
        data = await client.download_media(message, file=bytes)
        if data is None:
            return {"data": None}
        if payload.as_base64:
            return {
                "data": {"_": "bytes", "base64": base64.b64encode(data).decode("ascii")}
            }
        return {"data": data.decode("utf-8", errors="replace")}

    @app.post("/media/download/stream")
    async def download_media_stream(
        payload: DownloadMediaPayload,
        account: str | None = None,
    ) -> StreamingResponse:
        """Download to a server-visible path and stream progress as NDJSON."""
        if not payload.output_path:
            raise HTTPException(status_code=400, detail="output_path is required for streamed download")

        ensure_telegram_rate(state, account, "media.download")
        client = await require_authorized_client(state, account)
        message = await client.get_messages(payload.entity, ids=payload.message_id)
        if not message:
            raise HTTPException(status_code=404, detail="Message not found")

        async def event_stream():
            queue: asyncio.Queue[dict[str, Any]] = asyncio.Queue()
            loop = asyncio.get_running_loop()

            def on_progress(current: int, total: int) -> None:
                loop.call_soon_threadsafe(
                    queue.put_nowait,
                    {"event": "progress", "received_bytes": current, "total_bytes": total},
                )

            yield json.dumps({"event": "queued", "message_id": payload.message_id}) + "\n"
            async with state.media_download_semaphore(account):
                task = asyncio.create_task(
                    client.download_media(message, file=payload.output_path, progress_callback=on_progress)
                )
                yield json.dumps({"event": "start", "message_id": payload.message_id}) + "\n"
                try:
                    while not task.done():
                        try:
                            event = await asyncio.wait_for(queue.get(), timeout=0.5)
                        except TimeoutError:
                            yield json.dumps({"event": "heartbeat"}) + "\n"
                        else:
                            yield json.dumps(event) + "\n"

                    output = await task
                    while not queue.empty():
                        yield json.dumps(queue.get_nowait()) + "\n"
                    yield json.dumps({"event": "complete", "path": str(output) if output else None}) + "\n"
                except asyncio.CancelledError:
                    task.cancel()
                    with suppress(asyncio.CancelledError):
                        await task
                    raise
                except Exception as exc:
                    yield json.dumps({"event": "error", "detail": str(exc)}) + "\n"

        return StreamingResponse(event_stream(), media_type="application/x-ndjson")

    @app.post("/files/upload")
    async def upload_file(
        payload: UploadFilePayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "files.upload")
        client = await require_authorized_client(state, account)
        file_value, cleanup = decode_upload_file(payload.file_path, payload.file_base64, payload.file_name)
        try:
            uploaded = await client.upload_file(file_value)
        finally:
            if cleanup:
                Path(cleanup).unlink(missing_ok=True)
        return {"file": serialize_tl(uploaded)}

    @app.post("/entities/resolve")
    async def resolve_entity_endpoint(
        payload: EntityPayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "entities.resolve")
        client = await require_authorized_client(state, account)
        entity = await client.get_entity(payload.entity)
        input_entity = await resolve_entity(payload.entity, client=client)
        return {"entity": serialize_tl(entity), "input_entity": serialize_tl(input_entity)}

    @app.post("/chats/join")
    async def join_chat(
        payload: JoinLeavePayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "chats.join")
        client = await require_authorized_client(state, account)
        request = await build_tl_request(
            "channels.JoinChannelRequest",
            {"channel": payload.entity},
            client,
        )
        result = await client(request)
        return {"result": serialize_tl(result)}

    @app.post("/chats/leave")
    async def leave_chat(
        payload: JoinLeavePayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "chats.leave")
        client = await require_authorized_client(state, account)
        request = await build_tl_request(
            "channels.LeaveChannelRequest",
            {"channel": payload.entity},
            client,
        )
        result = await client(request)
        return {"result": serialize_tl(result)}

    @app.post("/stories/get")
    async def get_stories(
        payload: StoryGetPayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "stories.get")
        client = await require_authorized_client(state, account)
        peer = await resolve_entity(payload.entity, client=client)
        result = await client(functions.stories.GetStoriesByIDRequest(peer=peer, id=payload.story_ids))
        return {"result": serialize_tl(result)}

    @app.post("/stories/send")
    async def send_story(
        payload: StorySendPayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "stories.send")
        client = await require_authorized_client(state, account)
        kwargs = {
            "peer": payload.peer,
            "media": payload.media,
            "privacy_rules": payload.privacy_rules,
            "caption": payload.caption,
            "period": payload.period,
            "pinned": payload.pinned,
            "noforwards": payload.noforwards,
            **payload.extra,
        }
        request = await build_tl_request(
            "stories.SendStoryRequest",
            {key: value for key, value in kwargs.items() if value is not None},
            client,
        )
        result = await client(request)
        return {"result": serialize_tl(result)}

    @app.post("/admin/ban")
    async def admin_ban(
        payload: AdminBanPayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "admin.ban")
        client = await require_authorized_client(state, account)
        request = await build_tl_request(
            "channels.EditBannedRequest",
            {
                "channel": payload.channel,
                "participant": payload.participant,
                "banned_rights": payload.banned_rights,
            },
            client,
        )
        result = await client(request)
        return {"result": serialize_tl(result)}

    @app.post("/admin/promote")
    async def admin_promote(
        payload: AdminPromotePayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_telegram_rate(state, account, "admin.promote")
        client = await require_authorized_client(state, account)
        request = await build_tl_request(
            "channels.EditAdminRequest",
            {
                "channel": payload.channel,
                "user_id": payload.user,
                "admin_rights": payload.admin_rights,
                "rank": payload.rank,
            },
            client,
        )
        result = await client(request)
        return {"result": serialize_tl(result)}

    @app.post("/tl/construct")
    async def construct_tl_object(
        payload: TypeConstructorPayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        layer = await state.require_layer(account)
        client = await layer.authorized_client() if await layer.is_authorized() else None
        result = await build_tl_object(payload.constructor, payload.fields, client)
        return {"type": type(result).__name__, "object": serialize_tl(result)}

    @app.post("/raw/invoke")
    async def raw_invoke(payload: RawInvokePayload, account: str | None = None) -> dict[str, Any]:
        ensure_raw_enabled(state)
        ensure_telegram_rate(state, account, "raw.invoke")
        layer = await state.require_layer(account)
        client = await layer.authorized_client()
        request = await build_tl_request(payload.request, payload.kwargs, client)
        result = await layer.invoke(request)
        return {"type": type(result).__name__, "result": serialize_tl(result)}

    @app.get("/mtproto/layers/{layer}/functions")
    async def mtproto_layer_functions(layer: int) -> dict[str, Any]:
        try:
            functions = get_layer_functions(layer)
        except ValueError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return {"layer": layer, "function_count": len(functions), "functions": functions}

    @app.post("/mtproto/layers/{layer}/invoke")
    async def mtproto_layer_invoke(
        layer: int,
        payload: MtprotoLayerInvokePayload,
        account: str | None = None,
    ) -> dict[str, Any]:
        ensure_layer_enabled(state)
        ensure_telegram_rate(state, account, "layer.invoke")
        try:
            require_layer_function(layer, payload.request)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        telegram_layer = await state.require_layer(account)
        client = await telegram_layer.authorized_client()
        request = await build_tl_request(payload.request, payload.kwargs, client)
        result = await telegram_layer.invoke(request)
        return {
            "layer": layer,
            "request": payload.request,
            "type": type(result).__name__,
            "result": serialize_tl(result),
        }

    @app.post("/rpc")
    async def json_rpc(payload: JsonRpcRequest) -> dict[str, Any]:
        try:
            result = await dispatch_rpc(state, payload.method, payload.params)
        except Exception as exc:
            return {
                "jsonrpc": "2.0",
                "id": payload.id,
                "error": {"code": -32000, "message": str(exc)},
            }
        return {"jsonrpc": "2.0", "id": payload.id, "result": result}

    @app.post("/queue/jobs")
    async def enqueue_job(payload: QueueJobPayload) -> dict[str, Any]:
        ensure_account_allowed_for_payload(state, payload.account)
        job_id = uuid4().hex
        job = await state.queue.create_job({
            "id": job_id,
            "kind": payload.kind,
            "account": state.resolve_account(payload.account),
            "payload": payload.payload,
            "idempotency_key": payload.idempotency_key,
            "attempts": 0,
            "max_attempts": payload.max_attempts
            or state.settings().service.queue_default_max_attempts,
            "status": "queued",
            "result": None,
            "error": None,
        })
        if state.queue.runs_inline:
            asyncio.create_task(run_queue_job(state, job_id, payload))
        return job

    @app.get("/queue/jobs")
    async def list_jobs() -> list[dict[str, Any]]:
        return await state.queue.list_jobs()

    @app.get("/queue/jobs/{job_id}")
    async def get_job(job_id: str) -> dict[str, Any]:
        job = await state.queue.get_job(job_id)
        if job is None:
            raise HTTPException(status_code=404, detail="Job not found")
        return job

    @app.get("/compat/reverse-proxy")
    async def reverse_proxy_compat() -> dict[str, Any]:
        base_url = state.settings().service.public_base_url or "http://127.0.0.1:8080"
        return {
            "bot_api_base_url": f"{base_url.rstrip('/')}/bot<TOKEN>",
            "dns_override": "Point api.telegram.org to this service only for apps that use Bot API HTTPS.",
            "nginx_location": (
                "location /bot { proxy_pass http://127.0.0.1:8080; "
                "proxy_set_header Host $host; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; }"
            ),
            "limits": [
                "MTProto client libraries cannot be transparently replaced by DNS; use SDK/adapters.",
                "Official Telegram apps cannot be forced through this API without changing their code/proxy.",
            ],
        }

    @app.get("/bot{token}/{method}", operation_id="bot_api_compat_get")
    async def bot_api_compat_get(token: str, method: str, request: Request) -> JSONResponse:
        return await handle_bot_api_compat(state, token, method, request)

    @app.post("/bot{token}/{method}", operation_id="bot_api_compat_post")
    async def bot_api_compat_post(token: str, method: str, request: Request) -> JSONResponse:
        return await handle_bot_api_compat(state, token, method, request)

    return app


async def handle_bot_api_compat(
    state: ApiState,
    token: str,
    method: str,
    request: Request,
) -> JSONResponse:
    account = resolve_bot_account(state, token)
    try:
        ensure_account_allowed_for_payload(state, account)
        params = await read_bot_api_params(request)
        result = await dispatch_bot_api(state, account, token, method, params)
    except HTTPException as exc:
        return JSONResponse(
            {"ok": False, "error_code": exc.status_code, "description": exc.detail},
            status_code=exc.status_code,
        )
    except Exception as exc:
        return JSONResponse(
            {"ok": False, "error_code": 500, "description": str(exc)},
            status_code=500,
        )
    return JSONResponse({"ok": True, "result": result})


async def reconnect(state: ApiState) -> None:
    await state.disconnect()


def decode_upload_file(
    file_path: str | None,
    file_base64: str | None,
    file_name: str | None,
) -> tuple[str | bytes, str | None]:
    if file_path:
        return file_path, None
    if not file_base64:
        raise HTTPException(status_code=400, detail="file_path or file_base64 is required")
    data = base64.b64decode(file_base64)
    if not file_name:
        return data, None
    suffix = Path(file_name).suffix
    handle = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    try:
        handle.write(data)
        return handle.name, handle.name
    finally:
        handle.close()


async def build_reaction(value: Any, client: Any) -> list[Any] | None:
    if value is None:
        return None
    if isinstance(value, str):
        return [types.ReactionEmoji(emoticon=value)]
    if isinstance(value, list):
        return [await build_tl_object(str(item.get("_", "ReactionEmoji")), item, client) for item in value]
    if isinstance(value, dict):
        return [await build_tl_object(str(value.get("_", "ReactionEmoji")), value, client)]
    raise HTTPException(status_code=400, detail="Unsupported reaction payload")


async def read_bot_api_params(request: Request) -> dict[str, Any]:
    params: dict[str, Any] = dict(request.query_params)
    if request.method != "POST":
        return params
    body = await request.body()
    if not body:
        return params
    content_type = request.headers.get("content-type", "")
    if "application/json" in content_type:
        loaded = json.loads(body.decode("utf-8"))
        if isinstance(loaded, dict):
            params.update(loaded)
        return params
    from urllib.parse import parse_qs

    parsed = parse_qs(body.decode("utf-8"), keep_blank_values=True)
    params.update({key: values[-1] if len(values) == 1 else values for key, values in parsed.items()})
    return params


def resolve_bot_account(state: ApiState, token: str) -> str:
    service = state.settings().service
    return normalize_account_name(service.bot_token_accounts.get(token) or state.settings().active_account)


async def dispatch_bot_api(
    state: ApiState,
    account: str,
    token: str,
    method: str,
    params: dict[str, Any],
) -> Any:
    normalized = method.lower()
    client = await require_authorized_client(state, account)
    if normalized == "getme":
        ensure_telegram_rate(state, account, "bot.getme")
        return bot_user(await client.get_me())
    if normalized == "sendmessage":
        ensure_telegram_rate(state, account, "bot.sendmessage")
        chat_id = required_param(params, "chat_id")
        text = required_param(params, "text")
        message = await client.send_message(chat_id, text, parse_mode=params.get("parse_mode"))
        return bot_message(message)
    if normalized in {"sendphoto", "senddocument"}:
        ensure_telegram_rate(state, account, f"bot.{normalized}")
        chat_id = required_param(params, "chat_id")
        file_value = required_param(params, "photo" if normalized == "sendphoto" else "document")
        message = await client.send_file(chat_id, file_value, caption=params.get("caption"))
        return bot_message(message)
    if normalized == "editmessagetext":
        ensure_telegram_rate(state, account, "bot.editmessagetext")
        chat_id = required_param(params, "chat_id")
        message_id = int(required_param(params, "message_id"))
        message = await client.edit_message(chat_id, message_id, required_param(params, "text"))
        return bot_message(message)
    if normalized == "deletemessage":
        ensure_telegram_rate(state, account, "bot.deletemessage")
        chat_id = required_param(params, "chat_id")
        message_id = int(required_param(params, "message_id"))
        await client.delete_messages(chat_id, [message_id], revoke=True)
        return True
    if normalized == "getupdates":
        ensure_telegram_rate(state, account, "bot.getupdates")
        await ensure_bot_update_handler(state, token, account)
        offset = int(params.get("offset") or 0)
        limit = int(params.get("limit") or 100)
        updates = [
            update for update in state.bot_updates.get(token, []) if update["update_id"] >= offset
        ][:limit]
        return updates
    raise HTTPException(
        status_code=404,
        detail={
            "message": f"Unsupported Bot API compatibility method: {method}",
            "supported_methods": sorted(BOT_API_COMPAT_METHODS),
        },
    )


async def ensure_bot_update_handler(state: ApiState, token: str, account: str) -> None:
    key = f"{token}:{account}"
    if key in state.bot_update_handlers:
        return
    client = await require_authorized_client(state, account)
    state.bot_updates.setdefault(token, [])
    state.bot_update_ids.setdefault(token, 0)

    async def handler(event: events.NewMessage.Event) -> None:
        state.bot_update_ids[token] += 1
        state.bot_updates[token].append(
            {
                "update_id": state.bot_update_ids[token],
                "message": bot_message(event.message),
            }
        )
        max_updates = state.settings().service.max_queue_jobs_list
        state.bot_updates[token] = state.bot_updates[token][-max_updates:]

    builder = events.NewMessage()
    client.add_event_handler(handler, builder)
    state.bot_update_handlers[key] = (handler, builder)


def required_param(params: dict[str, Any], name: str) -> Any:
    value = params.get(name)
    if value is None or value == "":
        raise HTTPException(status_code=400, detail=f"{name} is required")
    return value


def bot_user(user: User | None) -> dict[str, Any]:
    data = serialize_user(user)
    data["is_bot"] = bool(user.bot) if user else False
    return data


def bot_message(message: Message) -> dict[str, Any]:
    return {
        "message_id": message.id,
        "date": int(message.date.timestamp()) if message.date else None,
        "chat": {"id": message.chat_id, "type": "private" if message.is_private else "group"},
        "from": {"id": message.sender_id} if message.sender_id else None,
        "text": message.message,
        "caption": getattr(message, "text", None) if message.media else None,
    }


def extract_bearer_token(header: str | None) -> str | None:
    if not header:
        return None
    scheme, _, token = header.partition(" ")
    if scheme.lower() != "bearer" or not token:
        return None
    return token.strip()


def token_scopes(service: ServiceSettings, token: str | None) -> list[str] | None:
    if not token:
        return None
    tokens_json = os.getenv(service.api_tokens_env)
    if tokens_json:
        try:
            tokens = json.loads(tokens_json)
        except json.JSONDecodeError:
            tokens = {}
        scopes = tokens.get(token)
        if isinstance(scopes, list):
            return [str(scope) for scope in scopes]
    single_token = os.getenv(service.api_token_env)
    if single_token and token == single_token:
        return ["*"]
    return None


def check_rate_limit(state: ApiState, key: str, limit_per_minute: int) -> bool:
    if limit_per_minute <= 0:
        return True
    now = time.time()
    window_start = now - 60
    timestamps = [item for item in state.rate_limits.get(key, []) if item >= window_start]
    if len(timestamps) >= limit_per_minute:
        state.rate_limits[key] = timestamps
        return False
    timestamps.append(now)
    state.rate_limits[key] = timestamps
    return True


def ensure_telegram_rate(state: ApiState, account: str | None, action: str) -> None:
    service = state.settings().service
    account_name = state.resolve_account(account)
    REQUEST_TELEGRAM_ACCOUNT.set(account_name)
    REQUEST_TELEGRAM_ACTION.set(action)
    cooldown = state.telegram_cooldowns.get(account_name)
    now_ts = int(time.time())
    if service.telegram_safe_mode and cooldown and int(cooldown.get("until_ts", 0)) > now_ts:
        retry_after = int(cooldown["until_ts"]) - now_ts
        raise HTTPException(
            status_code=429,
            detail={
                "message": "Telegram account cooldown is active after FloodWait.",
                "account": account_name,
                "action": cooldown.get("action"),
                "retry_after": retry_after,
            },
            headers={"Retry-After": str(retry_after)},
        )
    ensure_account_telegram_budget(state, account_name)
    now = time.monotonic()
    previous = state.last_telegram_action_at.get(account_name)
    min_interval = service.telegram_min_action_interval_seconds
    if action != "media.download" and previous is not None and min_interval > 0:
        wait_for = min_interval - (now - previous)
        if wait_for > 0:
            retry_after = max(1, int(wait_for + 0.999))
            raise HTTPException(
                status_code=429,
                detail=(
                    "Telegram desktop-like pacing is active for this account. "
                    f"Retry after {retry_after}s."
                ),
                headers={"Retry-After": str(retry_after)},
            )
    key = f"{account_name}:{action}"
    type_limit = telegram_action_type_limit(service, action)
    if type_limit is not None:
        type_name, type_limit_value, type_window_seconds = type_limit
        type_key = f"{account_name}:type:{type_name}:{telegram_action_rate_key(action)}"
        if not check_bucket(
            state.telegram_rate_limits,
            type_key,
            type_limit_value,
            window_seconds=type_window_seconds,
        ):
            raise HTTPException(
                status_code=429,
                detail=(
                    "Telegram typed action rate limit exceeded. "
                    f"Limit: {type_limit_value}/{type_window_seconds}s for {type_name}."
                ),
                headers={"Retry-After": str(type_window_seconds)},
            )
    action_limit, window_seconds = telegram_action_limit(service, action)
    if not check_bucket(
        state.telegram_rate_limits,
        key,
        action_limit,
        window_seconds=window_seconds,
    ):
        retry_after = window_seconds
        raise HTTPException(
            status_code=429,
            detail=(
                "Telegram action rate limit exceeded for this account/action. "
                f"Limit: {action_limit}/{window_seconds}s."
            ),
            headers={"Retry-After": str(retry_after)},
        )
    if action != "media.download":
        state.last_telegram_action_at[account_name] = now


def ensure_account_telegram_budget(state: ApiState, account_name: str) -> None:
    service = state.settings().service
    checks = [
        ("second", service.telegram_requests_per_second, 1),
        ("minute", service.telegram_requests_per_minute, 60),
        ("hour", service.telegram_requests_per_hour, 3600),
    ]
    for bucket_name, limit, window_seconds in checks:
        if check_bucket(
            state.telegram_account_rate_limits,
            f"{account_name}:all:{bucket_name}",
            limit,
            window_seconds=window_seconds,
        ):
            continue
        raise HTTPException(
            status_code=429,
            detail=(
                "Telegram account request budget exceeded. "
                f"Limit: {limit}/{window_seconds}s."
            ),
            headers={"Retry-After": str(window_seconds)},
        )


def ensure_telegram_auth_rate(state: ApiState, account: str | None) -> None:
    service = state.settings().service
    account_name = state.resolve_account(account)
    REQUEST_TELEGRAM_ACCOUNT.set(account_name)
    REQUEST_TELEGRAM_ACTION.set("auth")
    if not check_bucket(
        state.telegram_auth_rate_limits,
        account_name,
        service.telegram_auth_requests_per_hour,
        window_seconds=3600,
    ):
        raise HTTPException(
            status_code=429,
            detail=(
                "Telegram auth rate limit exceeded for this account. "
                f"Limit: {service.telegram_auth_requests_per_hour}/hour."
            ),
            headers={"Retry-After": "3600"},
        )


def telegram_action_limit(service: ServiceSettings, action: str) -> tuple[int, int]:
    if action == "media.download":
        return service.telegram_media_downloads_per_minute, 60
    if action.startswith(("messages.send", "media.send", "bot.send")):
        return service.telegram_send_actions_per_minute, 60
    if action.startswith(("entities.resolve", "dialogs", "messages", "drafts.", "bot.getupdates")):
        return service.telegram_resolve_actions_per_minute, 60
    if action.startswith(("raw.", "layer.")):
        return service.telegram_raw_actions_per_minute, 60
    if action.startswith(("chats.join", "chats.leave")):
        return service.telegram_join_actions_per_hour, 3600
    if action.startswith(("admin.", "messages.delete", "messages.history.delete")):
        return service.telegram_destructive_actions_per_hour, 3600
    return service.telegram_actions_per_minute, 60


def telegram_action_type_limit(service: ServiceSettings, action: str) -> tuple[str, int, int] | None:
    if action.startswith("messages.read"):
        return "read", service.telegram_read_requests_per_second, 1
    if action.startswith(("messages.send", "media.send", "bot.send")):
        return "send", service.telegram_send_requests_per_second, 1
    if action.startswith("messages.typing"):
        return "typing", service.telegram_typing_requests_per_second, 1
    if action.startswith(("updates.", "accounts.sync")):
        return "sync", service.telegram_sync_requests_per_minute, 60
    return None


def telegram_action_rate_key(action: str) -> str:
    if action.startswith("messages.typing"):
        return action
    return "all"


def telegram_limit_summary(service: ServiceSettings) -> dict[str, Any]:
    return {
        "telegram_actions_per_minute": service.telegram_actions_per_minute,
        "telegram_send_actions_per_minute": service.telegram_send_actions_per_minute,
        "telegram_resolve_actions_per_minute": service.telegram_resolve_actions_per_minute,
        "telegram_raw_actions_per_minute": service.telegram_raw_actions_per_minute,
        "telegram_join_actions_per_hour": service.telegram_join_actions_per_hour,
        "telegram_destructive_actions_per_hour": service.telegram_destructive_actions_per_hour,
        "telegram_media_downloads_per_minute": service.telegram_media_downloads_per_minute,
        "telegram_media_download_concurrency": service.telegram_media_download_concurrency,
        "telegram_requests_per_second": service.telegram_requests_per_second,
        "telegram_requests_per_minute": service.telegram_requests_per_minute,
        "telegram_requests_per_hour": service.telegram_requests_per_hour,
        "telegram_read_requests_per_second": service.telegram_read_requests_per_second,
        "telegram_send_requests_per_second": service.telegram_send_requests_per_second,
        "telegram_typing_requests_per_second": service.telegram_typing_requests_per_second,
        "telegram_sync_requests_per_minute": service.telegram_sync_requests_per_minute,
        "telegram_min_action_interval_seconds": service.telegram_min_action_interval_seconds,
        "telegram_default_flood_cooldown_seconds": service.telegram_default_flood_cooldown_seconds,
    }


def should_serialize_http_path(path: str) -> bool:
    if path in {
        "/health",
        "/config",
        "/capabilities",
        "/accounts",
        "/accounts/online",
        "/accounts/risk-status",
        "/db/writer/status",
        "/db/maintenance/status",
    }:
        return False
    if path.startswith(("/docs", "/redoc", "/openapi.json", "/events", "/ws/")):
        return False
    if path.startswith(("/media/download", "/queue/jobs")):
        return False
    return path.startswith(
        (
            "/auth/",
            "/me",
            "/dialogs",
            "/messages",
            "/media/",
            "/files/",
            "/entities/",
            "/chats/",
            "/stories/",
            "/admin/",
            "/raw/",
            "/mtproto/",
            "/bot",
            "/rpc",
            "/actions/execute",
            "/tl/",
            "/accounts/sync",
        )
    )


async def retry_telegram_call(call_factory: Any, *, max_attempts: int = 5) -> Any:
    delay = 1.0
    for attempt in range(1, max_attempts + 1):
        try:
            return await call_factory()
        except FloodWaitError:
            raise
        except (ConnectionError, TimeoutError, OSError, RPCError):
            if attempt >= max_attempts:
                raise
            await asyncio.sleep(delay + random.uniform(0, delay * 0.2))
            delay = min(delay * 2, 16)
    raise RuntimeError("unreachable retry state")


def make_action_idempotency_key(account: str, action: str, value: str | None) -> str | None:
    if not value:
        return None
    normalized = value.strip()
    if not normalized:
        return None
    return normalized


def idempotency_payload_hash(payload: Any) -> str:
    return hashlib.sha256(safe_json_dumps(payload).encode("utf-8")).hexdigest()


def payload_has_large_file(payload: Any, *, threshold_bytes: int = 100 * 1024 * 1024) -> bool:
    if not isinstance(payload, dict):
        return False
    file_path = payload.get("file_path")
    if file_path:
        try:
            return Path(str(file_path)).expanduser().stat().st_size >= threshold_bytes
        except OSError:
            return False
    file_base64 = payload.get("file_base64")
    if isinstance(file_base64, str):
        return len(file_base64) * 3 // 4 >= threshold_bytes
    return False


def is_sqlite_locked_error(exc: Exception) -> bool:
    return isinstance(exc, sqlite3.OperationalError) and "database is locked" in str(exc).lower()


def is_disk_full_error(exc: Exception) -> bool:
    message = str(exc).lower()
    return (
        (isinstance(exc, OSError) and getattr(exc, "errno", None) == 28)
        or (
            isinstance(exc, sqlite3.OperationalError)
            and "disk" in message
            and "full" in message
        )
    )


def is_io_retryable_error(exc: Exception) -> bool:
    if is_disk_full_error(exc):
        return False
    if isinstance(exc, PermissionError):
        return False
    if isinstance(exc, OSError):
        return True
    message = str(exc).lower()
    if any(marker in message for marker in ("schema", "malformed", "not a database", "permission")):
        return False
    return isinstance(exc, sqlite3.OperationalError) and any(
        marker in message for marker in ("i/o", "io error", "unable to open database file")
    )


def is_non_retryable_db_write_error(exc: Exception) -> bool:
    if is_disk_full_error(exc) or isinstance(exc, PermissionError):
        return True
    message = str(exc).lower()
    return isinstance(exc, sqlite3.DatabaseError) and any(
        marker in message for marker in ("schema", "malformed", "not a database", "permission")
    )


def is_non_retryable_retention_error(exc: Exception) -> bool:
    message = str(exc).lower()
    if isinstance(exc, PermissionError):
        return True
    if is_disk_full_error(exc):
        return True
    if isinstance(exc, sqlite3.DatabaseError) and any(
        marker in message for marker in ("schema", "malformed", "not a database")
    ):
        return True
    return False


def ensure_sqlite_column(
    connection: sqlite3.Connection,
    table: str,
    column: str,
    definition: str,
) -> None:
    columns = {
        str(row[1])
        for row in connection.execute(f"pragma table_info({table})").fetchall()
    }
    if column not in columns:
        connection.execute(f"alter table {table} add column {column} {definition}")


def safe_json_dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)


def to_unix_timestamp(value: Any) -> int:
    if isinstance(value, datetime):
        return int(value.timestamp())
    return int(value or 0)


def random_interval(minimum: int | float, maximum: int | float, *, floor: int | float = 0) -> float:
    low = max(float(floor), float(minimum))
    high = max(low, float(maximum))
    return random.uniform(low, high)


def check_bucket(
    buckets: dict[str, list[float]],
    key: str,
    limit: int,
    *,
    window_seconds: int,
) -> bool:
    now = time.time()
    window_start = now - window_seconds
    timestamps = [item for item in buckets.get(key, []) if item >= window_start]
    if len(timestamps) >= limit:
        buckets[key] = timestamps
        return False
    timestamps.append(now)
    buckets[key] = timestamps
    return True


def clamp_limit(limit: int, maximum: int) -> int:
    if limit < 1:
        raise HTTPException(status_code=400, detail="limit must be >= 1")
    return min(limit, maximum)


def ensure_safe_account_payload(state: ApiState, account: str) -> None:
    state.resolve_account(account)


async def audit_request(
    state: ApiState,
    request: Request,
    status_code: int,
    token: str | None,
) -> None:
    path = state.settings().service.audit_log_path
    if not path:
        return
    audit_path = Path(path).expanduser()
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "ts": int(time.time()),
        "method": request.method,
        "path": request.url.path,
        "status_code": status_code,
        "client": request.client.host if request.client else None,
        "account": request.query_params.get("account"),
        "token": token_hash(token) if token else None,
    }
    with audit_path.open("a", encoding="utf-8") as audit_file:
        audit_file.write(json.dumps(entry, ensure_ascii=False) + "\n")


def token_hash(token: str | None) -> str:
    if not token:
        return ""
    return hashlib.sha256(token.encode("utf-8")).hexdigest()[:16]


def account_allowed(scopes: list[str], account: str | None) -> bool:
    if not account or "*" in scopes:
        return True
    return normalize_account_name(account) in {normalize_account_name(scope) for scope in scopes}


def ensure_account_allowed_for_payload(state: ApiState, account: str | None) -> None:
    scopes = REQUEST_SCOPES.get()
    if scopes is not None and not account_allowed(scopes, account or state.settings().active_account):
        raise HTTPException(status_code=403, detail="Account is not allowed for this token")


def ensure_admin_scope() -> None:
    scopes = REQUEST_SCOPES.get()
    if scopes is not None and "*" not in scopes:
        raise HTTPException(status_code=403, detail="Admin scope is required")


async def ensure_websocket_allowed(
    state: ApiState,
    websocket: WebSocket,
    account: str | None,
) -> None:
    service = state.settings().service
    token = websocket.query_params.get("token") or extract_bearer_token(
        websocket.headers.get("authorization")
    )
    scopes = token_scopes(service, token)
    if service.require_api_token and scopes is None:
        await websocket.close(code=1008, reason="Missing or invalid API token")
        raise WebSocketDisconnect
    if scopes is not None and not account_allowed(scopes, account or state.settings().active_account):
        await websocket.close(code=1008, reason="Account is not allowed for this token")
        raise WebSocketDisconnect


def ensure_raw_enabled(state: ApiState) -> None:
    if not state.settings().service.enable_raw_invoke:
        raise HTTPException(status_code=403, detail="Raw invoke is disabled")


def ensure_layer_enabled(state: ApiState) -> None:
    if not state.settings().service.enable_layer_invoke:
        raise HTTPException(status_code=403, detail="Layer invoke is disabled")


def mask_url_secret(url: str | None) -> str | None:
    if not url or "@" not in url or "://" not in url:
        return url
    scheme, rest = url.split("://", 1)
    auth, address = rest.rsplit("@", 1)
    username = auth.split(":", 1)[0]
    return f"{scheme}://{username}:***@{address}"


def normalize_username_entity(value: str) -> str:
    entity = value.strip()
    if not entity:
        raise HTTPException(status_code=400, detail="username is required")
    for prefix in ("https://t.me/", "http://t.me/", "t.me/"):
        if entity.startswith(prefix):
            entity = entity.removeprefix(prefix).split("?", 1)[0].strip("/")
            break
    if entity.startswith("+") or entity.startswith("@") or entity.lstrip("-").isdigit():
        return entity
    if "/" in entity:
        return entity
    return f"@{entity}"


async def decode_entity_argument(value: Any, client: Any) -> Any:
    if isinstance(value, str):
        stripped = value.strip()
        if stripped.startswith("{") or stripped.startswith("["):
            try:
                value = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise HTTPException(status_code=400, detail=f"Invalid entity JSON: {exc}") from exc
        else:
            return value
    if isinstance(value, dict | list):
        return await decode_tl_value(value, client=client)
    return value


def visible_accounts_response(settings: AppSettings, scopes: list[str] | None) -> dict[str, Any]:
    if scopes is None or "*" in scopes:
        return {"active_account": settings.active_account, "accounts": settings.accounts}
    allowed = {normalize_account_name(scope) for scope in scopes}
    accounts = [account for account in settings.accounts if account in allowed]
    active = settings.active_account if settings.active_account in accounts else accounts[0] if accounts else None
    return {"active_account": active, "accounts": accounts}


async def require_authorized_client(state: ApiState, account: str | None = None):
    layer = await state.require_layer(account)
    return await layer._require_authorized_client()


async def dispatch_rpc(state: ApiState, method: str, params: dict[str, Any]) -> Any:
    account = params.pop("account", None)
    ensure_account_allowed_for_payload(state, account)
    if method == "accounts.list":
        settings = state.settings()
        return visible_accounts_response(settings, REQUEST_SCOPES.get())
    if method == "auth.status":
        layer = await state.require_layer(account)
        return {"account": state.resolve_account(account), "authorized": await layer.is_authorized()}
    if method == "dialogs.list":
        ensure_telegram_rate(state, account, "dialogs")
        limit = clamp_limit(int(params.get("limit", 20)), state.settings().service.max_dialog_limit)
        layer = await state.require_layer(account)
        account_name = state.resolve_account(account)
        result = []
        for dialog in await layer.get_dialogs(limit=limit):
            serialized = serialize_dialog(dialog)
            await state.enqueue_db_write(state.persist_dialog, account_name, serialized)
            await state.enqueue_db_write(state.persist_entity, account_name, dialog.entity)
            result.append(serialized)
        return result
    if method == "messages.send":
        ensure_telegram_rate(state, account, "messages.send")
        account_name = state.resolve_account(account)
        idempotency_key = make_action_idempotency_key(
            account_name,
            "messages.send",
            params.get("idempotency_key"),
        )
        idem_status, payload_hash, cached_result = await asyncio.to_thread(
            state.begin_idempotent_action,
            account_name,
            "messages.send",
            idempotency_key,
            params,
        )
        if idem_status == "completed" and cached_result is not None:
            return cached_result
        lease_seconds = state.idempotency_lease_seconds_for_action("messages.send", params)
        heartbeat_task = asyncio.create_task(
            state.idempotency_heartbeat(
                account_name,
                "messages.send",
                idempotency_key,
                payload_hash,
                lease_seconds,
            )
        )
        await state.mark_user_activity(account, send_online=True)
        try:
            layer = await state.require_layer(account)
            message = await layer.send_message(
                params["entity"],
                params["text"],
                parse_mode=params.get("parse_mode"),
            )
            result = serialize_message(message)
            await asyncio.to_thread(
                state.complete_idempotent_action,
                account_name,
                "messages.send",
                idempotency_key,
                payload_hash,
                result,
            )
        except Exception:
            await asyncio.to_thread(
                state.mark_idempotent_action,
                account_name,
                "messages.send",
                idempotency_key,
                payload_hash,
                "outcome_unknown",
            )
            raise
        finally:
            heartbeat_task.cancel()
            with suppress(asyncio.CancelledError):
                await heartbeat_task
        return result
    if method == "messages.send_username":
        ensure_telegram_rate(state, account, "messages.send")
        account_name = state.resolve_account(account)
        idempotency_key = make_action_idempotency_key(
            account_name,
            "messages.send_username",
            params.get("idempotency_key"),
        )
        idem_status, payload_hash, cached_result = await asyncio.to_thread(
            state.begin_idempotent_action,
            account_name,
            "messages.send_username",
            idempotency_key,
            params,
        )
        if idem_status == "completed" and cached_result is not None:
            return cached_result
        lease_seconds = state.idempotency_lease_seconds_for_action("messages.send_username", params)
        heartbeat_task = asyncio.create_task(
            state.idempotency_heartbeat(
                account_name,
                "messages.send_username",
                idempotency_key,
                payload_hash,
                lease_seconds,
            )
        )
        await state.mark_user_activity(account, send_online=True)
        try:
            layer = await state.require_layer(account)
            message = await layer.send_message(
                normalize_username_entity(params["username"]),
                params["text"],
                parse_mode=params.get("parse_mode"),
            )
            result = serialize_message(message)
            await asyncio.to_thread(
                state.complete_idempotent_action,
                account_name,
                "messages.send_username",
                idempotency_key,
                payload_hash,
                result,
            )
        except Exception:
            await asyncio.to_thread(
                state.mark_idempotent_action,
                account_name,
                "messages.send_username",
                idempotency_key,
                payload_hash,
                "outcome_unknown",
            )
            raise
        finally:
            heartbeat_task.cancel()
            with suppress(asyncio.CancelledError):
                await heartbeat_task
        return result
    if method == "messages.edit":
        ensure_telegram_rate(state, account, "messages.edit")
        client = await require_authorized_client(state, account)
        message = await client.edit_message(params["entity"], int(params["message_id"]), params["text"])
        return serialize_message(message)
    if method == "messages.delete":
        ensure_telegram_rate(state, account, "messages.delete")
        client = await require_authorized_client(state, account)
        result = await client.delete_messages(
            params["entity"],
            list(params["message_ids"]),
            revoke=bool(params.get("revoke", True)),
        )
        return {"result": serialize_tl(result)}
    if method == "messages.forward":
        ensure_telegram_rate(state, account, "messages.forward")
        client = await require_authorized_client(state, account)
        result = await client.forward_messages(
            params["to_entity"],
            list(params["message_ids"]),
            from_peer=params["from_entity"],
        )
        messages = result if isinstance(result, list) else [result]
        return [serialize_message(message) for message in messages]
    if method == "entities.resolve":
        ensure_telegram_rate(state, account, "entities.resolve")
        client = await require_authorized_client(state, account)
        entity = await client.get_entity(params["entity"])
        input_entity = await resolve_entity(params["entity"], client=client)
        return {"entity": serialize_tl(entity), "input_entity": serialize_tl(input_entity)}
    if method == "media.send":
        ensure_telegram_rate(state, account, "media.send")
        account_name = state.resolve_account(account)
        idempotency_key = make_action_idempotency_key(
            account_name,
            "media.send",
            params.get("idempotency_key"),
        )
        idem_status, payload_hash, cached_result = await asyncio.to_thread(
            state.begin_idempotent_action,
            account_name,
            "media.send",
            idempotency_key,
            params,
        )
        if idem_status == "completed" and cached_result is not None:
            return cached_result
        lease_seconds = state.idempotency_lease_seconds_for_action("media.send", params)
        heartbeat_task = asyncio.create_task(
            state.idempotency_heartbeat(
                account_name,
                "media.send",
                idempotency_key,
                payload_hash,
                lease_seconds,
            )
        )
        await state.mark_user_activity(account, send_online=True)
        try:
            client = await require_authorized_client(state, account)
            file_value, cleanup = decode_upload_file(
                params.get("file_path"),
                params.get("file_base64"),
                params.get("file_name"),
            )
            try:
                message = await client.send_file(
                    params["entity"],
                    file_value,
                    caption=params.get("caption"),
                    parse_mode=params.get("parse_mode"),
                )
            finally:
                if cleanup:
                    Path(cleanup).unlink(missing_ok=True)
            result = serialize_message(message)
            await asyncio.to_thread(
                state.complete_idempotent_action,
                account_name,
                "media.send",
                idempotency_key,
                payload_hash,
                result,
            )
        except Exception:
            await asyncio.to_thread(
                state.mark_idempotent_action,
                account_name,
                "media.send",
                idempotency_key,
                payload_hash,
                "outcome_unknown",
            )
            raise
        finally:
            heartbeat_task.cancel()
            with suppress(asyncio.CancelledError):
                await heartbeat_task
        return result
    if method == "tl.construct":
        layer = await state.require_layer(account)
        client = await layer.authorized_client() if await layer.is_authorized() else None
        result = await build_tl_object(params["constructor"], params.get("fields", {}), client)
        return {"type": type(result).__name__, "object": serialize_tl(result)}
    if method == "raw.invoke":
        ensure_raw_enabled(state)
        ensure_telegram_rate(state, account, "raw.invoke")
        layer = await state.require_layer(account)
        client = await layer.authorized_client()
        request = await build_tl_request(params["request"], params.get("kwargs", {}), client)
        result = await layer.invoke(request)
        return {"type": type(result).__name__, "result": serialize_tl(result)}
    raise ValueError(f"Unknown RPC method: {method}")


async def run_queue_job(state: ApiState, job_id: str, payload: QueueJobPayload) -> None:
    job = await state.queue.get_job(job_id)
    if job and job.get("status") == "queued":
        await state.queue.update_job(
            job_id,
            status="running",
            attempts=int(job.get("attempts") or 0) + 1,
        )
    else:
        await state.queue.update_job(job_id, status="running")
    try:
        result = await dispatch_rpc(
            state,
            payload.kind,
            {"account": payload.account, **payload.payload},
        )
        await state.queue.update_job(job_id, result=result, status="done")
    except Exception as exc:
        job = await state.queue.get_job(job_id)
        attempts = int((job or {}).get("attempts") or 0)
        max_attempts = int((job or {}).get("max_attempts") or 1)
        if attempts < max_attempts:
            await state.queue.requeue_job(job_id, error=str(exc))
        else:
            await state.queue.dead_letter_job(job_id, error=str(exc))


async def run_queue_worker(state: ApiState, *, poll_timeout: int = 5) -> None:
    while True:
        try:
            job = await state.queue.reserve_job(timeout=poll_timeout)
            if job is None:
                state.queue_worker_status.update(
                    {"running": True, "last_idle_ts": int(time.time())}
                )
                continue
            state.queue_worker_status.update(
                {
                    "running": True,
                    "last_job_id": job["id"],
                    "last_job_kind": job.get("kind"),
                    "last_job_ts": int(time.time()),
                    "last_error": None,
                }
            )
            payload = QueueJobPayload(
                kind=job["kind"],
                account=job.get("account"),
                payload=job.get("payload") or {},
            )
            await run_queue_job(state, job["id"], payload)
        except asyncio.CancelledError:
            raise
        except Exception as exc:
            state.queue_worker_status.update(
                {
                    "running": True,
                    "last_error": str(exc),
                    "last_error_ts": int(time.time()),
                }
            )
            await asyncio.sleep(1)


RPC_METHODS = {
    "accounts.list",
    "auth.status",
    "dialogs.list",
    "entities.resolve",
    "media.send",
    "messages.delete",
    "messages.edit",
    "messages.forward",
    "messages.send",
    "messages.send_username",
    "raw.invoke",
    "tl.construct",
}


BOT_API_COMPAT_METHODS = {
    "deleteMessage",
    "editMessageText",
    "getMe",
    "getUpdates",
    "sendDocument",
    "sendMessage",
    "sendPhoto",
}


ACTIONS: dict[str, dict[str, Any]] = {
    "accounts": {
        "aliases": ["accounts", "list accounts", "аккаунты", "список аккаунтов"],
        "interface": "json_rpc",
        "rpc_method": "accounts.list",
        "rest": "GET /accounts",
        "executable": True,
    },
    "auth_status": {
        "aliases": ["auth status", "status", "статус", "проверить авторизацию"],
        "interface": "rest",
        "rpc_method": "auth.status",
        "rest": "GET /auth/status",
        "executable": True,
    },
    "list_dialogs": {
        "aliases": ["dialogs", "list dialogs", "chats", "диалоги", "чаты"],
        "interface": "rest",
        "rpc_method": "dialogs.list",
        "rest": "GET /dialogs",
        "executable": True,
    },
    "send_message": {
        "aliases": ["send message", "message send", "отправить сообщение", "сообщение"],
        "interface": "rest",
        "rpc_method": "messages.send",
        "rest": "POST /messages/send",
        "queue": "POST /queue/jobs kind=messages.send",
        "executable": True,
    },
    "stream_updates": {
        "aliases": ["updates", "stream updates", "new messages", "события", "новые сообщения"],
        "interface": "sse",
        "websocket": "WS /ws/updates",
        "sse": "GET /events",
        "executable": False,
    },
    "raw_invoke": {
        "aliases": ["raw", "invoke", "tl", "mtproto", "сырой вызов"],
        "interface": "json_rpc",
        "rpc_method": "raw.invoke",
        "rest": "POST /raw/invoke",
        "executable": True,
    },
}


def resolve_api_method(
    payload: ActionResolvePayload,
    service: ServiceSettings | None = None,
) -> dict[str, Any]:
    action_name = find_action(payload.task)
    action = ACTIONS[action_name]
    interface = choose_interface(payload, action, service or ServiceSettings())
    return {
        "action": action_name,
        "interface": interface,
        "endpoint": endpoint_for_interface(interface, action),
        "rpc_method": action.get("rpc_method"),
        "account": payload.account,
        "executable": action.get("executable", False),
        "reason": reason_for_interface(interface, payload),
        "params": payload.params,
    }


def find_action(task: str) -> str:
    normalized = task.strip().lower()
    for action_name, action in ACTIONS.items():
        if normalized == action_name or normalized in action["aliases"]:
            return action_name
    for action_name, action in ACTIONS.items():
        if any(alias in normalized for alias in action["aliases"]):
            return action_name
    return "raw_invoke"


def choose_interface(
    payload: ActionResolvePayload,
    action: dict[str, Any],
    service: ServiceSettings,
) -> str:
    language = (payload.client_language or "").lower()
    if language == "python":
        return first_enabled(["python_sdk", service.default_api_interface, "rest"], service)
    if payload.background:
        return first_enabled(["queue", "json_rpc", "rest"], service)
    if payload.realtime and payload.bidirectional:
        return first_enabled(["websocket", "sse"], service)
    if payload.realtime:
        return first_enabled(["sse", "websocket"], service)
    return first_enabled([service.default_api_interface, action["interface"], "rest"], service)


def first_enabled(candidates: list[str], service: ServiceSettings) -> str:
    for candidate in candidates:
        if candidate in service.enabled_interfaces:
            return candidate
    return service.enabled_interfaces[0]


def endpoint_for_interface(interface: str, action: dict[str, Any]) -> str:
    if interface == "python_sdk":
        return "tg_api_zapret.TgApiZapretClient"
    if interface == "queue":
        return action.get("queue", "POST /queue/jobs")
    if interface == "websocket":
        return action.get("websocket", "WS /ws/updates")
    if interface == "sse":
        return action.get("sse", "GET /events")
    if interface == "json_rpc":
        return "POST /rpc"
    return action.get("rest", "POST /raw/invoke")


def reason_for_interface(interface: str, payload: ActionResolvePayload) -> str:
    if interface == "python_sdk":
        return "Python client requested; SDK hides HTTP details."
    if interface == "queue":
        return "Background execution requested."
    if interface == "websocket":
        return "Realtime bidirectional stream requested."
    if interface == "sse":
        return "Realtime one-way event stream requested."
    if interface == "json_rpc":
        return "Command can be routed through the generic RPC endpoint."
    return "Simple request/response command."


def resolve_session_file(session_file: Path, account: str) -> Path:
    if account == "default":
        return session_file
    return session_file.parent / "sessions" / f"{account}.session.txt"


def serialize_user(user: User | None) -> dict[str, Any]:
    if user is None:
        return {}
    return {
        "id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone": user.phone,
        "bot": user.bot,
    }


def serialize_dialog(dialog: Dialog) -> dict[str, Any]:
    entity = getattr(dialog, "entity", None)
    input_entity = None
    if entity is not None:
        try:
            input_entity = utils.get_input_peer(entity)
        except TypeError:
            input_entity = None
    return {
        "id": dialog.id,
        "name": dialog.name,
        "title": dialog.title,
        "username": getattr(entity, "username", None),
        "entity_type": type(entity).__name__ if entity is not None else None,
        "access_hash": getattr(entity, "access_hash", None),
        "input_entity": serialize_tl(input_entity) if input_entity is not None else None,
        "is_user": dialog.is_user,
        "is_group": dialog.is_group,
        "is_channel": dialog.is_channel,
        "unread_count": dialog.unread_count,
    }


def serialize_message(message: Message) -> dict[str, Any]:
    return {
        "id": message.id,
        "date": message.date.isoformat() if message.date else None,
        "chat_id": message.chat_id,
        "sender_id": message.sender_id,
        "text": message.message,
        "out": message.out,
        "mentioned": message.mentioned,
        "media": serialize_media_metadata(message.media),
    }


def serialize_media_metadata(media: Any) -> dict[str, Any] | None:
    """Keep enough Telegram media metadata for clients to select a real filename."""
    if media is None:
        return None
    result: dict[str, Any] = {"type": type(media).__name__}
    document = getattr(media, "document", None)
    if document is not None:
        result["mime_type"] = getattr(document, "mime_type", None)
        result["size"] = getattr(document, "size", None)
        for attribute in getattr(document, "attributes", []) or []:
            file_name = getattr(attribute, "file_name", None)
            if file_name:
                result["file_name"] = file_name
                break
        return result

    photo = getattr(media, "photo", None)
    if photo is not None:
        result["mime_type"] = "image/jpeg"
        sizes = [getattr(size, "size", 0) or 0 for size in getattr(photo, "sizes", []) or []]
        if sizes:
            result["size"] = max(sizes)
    return result

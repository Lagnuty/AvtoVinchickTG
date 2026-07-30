from __future__ import annotations

from abc import ABC, abstractmethod
import json
import time
from typing import Any


class QueueBackend(ABC):
    runs_inline: bool = True

    @abstractmethod
    async def create_job(self, job: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    async def update_job(self, job_id: str, **fields: Any) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    async def get_job(self, job_id: str) -> dict[str, Any] | None:
        raise NotImplementedError

    @abstractmethod
    async def list_jobs(self) -> list[dict[str, Any]]:
        raise NotImplementedError

    async def reserve_job(self, *, timeout: int = 5) -> dict[str, Any] | None:
        return None

    async def requeue_job(self, job_id: str, **fields: Any) -> dict[str, Any]:
        return await self.update_job(job_id, status="queued", **fields)

    async def dead_letter_job(self, job_id: str, **fields: Any) -> dict[str, Any]:
        return await self.update_job(job_id, status="dead_letter", **fields)

    async def close(self) -> None:
        return None


class MemoryQueueBackend(QueueBackend):
    def __init__(self) -> None:
        self.jobs: dict[str, dict[str, Any]] = {}
        self.idempotency: dict[str, str] = {}

    async def create_job(self, job: dict[str, Any]) -> dict[str, Any]:
        idempotency_key = job.get("idempotency_key")
        if idempotency_key and idempotency_key in self.idempotency:
            return self.jobs[self.idempotency[idempotency_key]]
        job.setdefault("attempts", 0)
        job.setdefault("max_attempts", 3)
        job.setdefault("leased_until", None)
        self.jobs[job["id"]] = job
        if idempotency_key:
            self.idempotency[str(idempotency_key)] = job["id"]
        return job

    async def update_job(self, job_id: str, **fields: Any) -> dict[str, Any]:
        self.jobs[job_id].update(fields)
        return self.jobs[job_id]

    async def get_job(self, job_id: str) -> dict[str, Any] | None:
        return self.jobs.get(job_id)

    async def list_jobs(self) -> list[dict[str, Any]]:
        return list(self.jobs.values())

    async def requeue_job(self, job_id: str, **fields: Any) -> dict[str, Any]:
        self.jobs[job_id].update(status="queued", leased_until=None, **fields)
        return self.jobs[job_id]

    async def dead_letter_job(self, job_id: str, **fields: Any) -> dict[str, Any]:
        self.jobs[job_id].update(status="dead_letter", leased_until=None, **fields)
        return self.jobs[job_id]


class RedisQueueBackend(QueueBackend):
    runs_inline = False

    def __init__(
        self,
        redis_url: str,
        *,
        prefix: str = "tg-api-zapret",
        visibility_timeout_seconds: int = 300,
    ) -> None:
        self.redis_url = redis_url
        self.prefix = prefix
        self.visibility_timeout_seconds = visibility_timeout_seconds
        self._redis = None

    async def create_job(self, job: dict[str, Any]) -> dict[str, Any]:
        redis = await self._client()
        idempotency_key = job.get("idempotency_key")
        if idempotency_key:
            existing_id = await redis.get(self._idempotency_key(str(idempotency_key)))
            if existing_id:
                existing = await self.get_job(decode_redis_value(existing_id))
                if existing is not None:
                    return existing
        job.setdefault("attempts", 0)
        job.setdefault("max_attempts", 3)
        job.setdefault("leased_until", None)
        await redis.sadd(self._index_key(), job["id"])
        await redis.set(self._job_key(job["id"]), json.dumps(job, ensure_ascii=False))
        if idempotency_key:
            await redis.set(self._idempotency_key(str(idempotency_key)), job["id"])
        await redis.rpush(self._queue_key(), job["id"])
        return job

    async def update_job(self, job_id: str, **fields: Any) -> dict[str, Any]:
        job = await self.get_job(job_id)
        if job is None:
            raise KeyError(job_id)
        job.update(fields)
        redis = await self._client()
        await redis.set(self._job_key(job_id), json.dumps(job, ensure_ascii=False))
        return job

    async def get_job(self, job_id: str) -> dict[str, Any] | None:
        redis = await self._client()
        value = await redis.get(self._job_key(job_id))
        if value is None:
            return None
        if isinstance(value, bytes):
            value = value.decode("utf-8")
        return json.loads(value)

    async def list_jobs(self) -> list[dict[str, Any]]:
        redis = await self._client()
        job_ids = await redis.smembers(self._index_key())
        jobs = []
        for job_id in sorted(decode_redis_value(item) for item in job_ids):
            job = await self.get_job(job_id)
            if job is not None:
                jobs.append(job)
        return jobs

    async def reserve_job(self, *, timeout: int = 5) -> dict[str, Any] | None:
        redis = await self._client()
        await self._requeue_expired_leases()
        item = await redis.blpop(self._queue_key(), timeout=timeout)
        if item is None:
            return None
        _, job_id = item
        job = await self.get_job(decode_redis_value(job_id))
        if job is None or job.get("status") != "queued":
            return None
        attempts = int(job.get("attempts") or 0) + 1
        return await self.update_job(
            job["id"],
            status="leased",
            attempts=attempts,
            leased_until=time.time() + self.visibility_timeout_seconds,
        )

    async def requeue_job(self, job_id: str, **fields: Any) -> dict[str, Any]:
        job = await self.update_job(job_id, status="queued", leased_until=None, **fields)
        redis = await self._client()
        await redis.rpush(self._queue_key(), job_id)
        return job

    async def dead_letter_job(self, job_id: str, **fields: Any) -> dict[str, Any]:
        job = await self.update_job(job_id, status="dead_letter", leased_until=None, **fields)
        redis = await self._client()
        await redis.sadd(self._dead_letter_key(), job_id)
        return job

    async def close(self) -> None:
        if self._redis is not None:
            await self._redis.aclose()
            self._redis = None

    async def _client(self):
        if self._redis is None:
            from redis.asyncio import Redis

            self._redis = Redis.from_url(self.redis_url, decode_responses=False)
        return self._redis

    def _job_key(self, job_id: str) -> str:
        return f"{self.prefix}:job:{job_id}"

    def _index_key(self) -> str:
        return f"{self.prefix}:jobs"

    def _queue_key(self) -> str:
        return f"{self.prefix}:queue"

    def _dead_letter_key(self) -> str:
        return f"{self.prefix}:dead-letter"

    def _idempotency_key(self, idempotency_key: str) -> str:
        return f"{self.prefix}:idempotency:{idempotency_key}"

    async def _requeue_expired_leases(self) -> None:
        redis = await self._client()
        job_ids = await redis.smembers(self._index_key())
        now = time.time()
        for raw_job_id in job_ids:
            job_id = decode_redis_value(raw_job_id)
            job = await self.get_job(job_id)
            if not job or job.get("status") not in {"leased", "running"}:
                continue
            leased_until = job.get("leased_until")
            if leased_until is None or float(leased_until) >= now:
                continue
            if int(job.get("attempts") or 0) >= int(job.get("max_attempts") or 1):
                await self.dead_letter_job(job_id, error="Lease expired after max attempts")
            else:
                await self.requeue_job(job_id, error="Lease expired; requeued")


def build_queue_backend(
    kind: str = "memory",
    *,
    redis_url: str | None = None,
    visibility_timeout_seconds: int = 300,
) -> QueueBackend:
    if kind == "memory":
        return MemoryQueueBackend()
    if kind == "redis":
        if not redis_url:
            raise ValueError("redis_url is required for Redis queue backend")
        return RedisQueueBackend(redis_url, visibility_timeout_seconds=visibility_timeout_seconds)
    raise ValueError(f"Unsupported queue backend: {kind}")


def decode_redis_value(value: str | bytes) -> str:
    return value.decode("utf-8") if isinstance(value, bytes) else value

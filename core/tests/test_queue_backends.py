import pytest

from tg_api_zapret.queue_backends import MemoryQueueBackend


@pytest.mark.asyncio
async def test_memory_queue_idempotency_returns_existing_job() -> None:
    queue = MemoryQueueBackend()
    first = await queue.create_job(
        {"id": "one", "kind": "messages.send", "status": "queued", "idempotency_key": "same"}
    )
    second = await queue.create_job(
        {"id": "two", "kind": "messages.send", "status": "queued", "idempotency_key": "same"}
    )

    assert first["id"] == "one"
    assert second["id"] == "one"
    assert len(await queue.list_jobs()) == 1


@pytest.mark.asyncio
async def test_memory_queue_requeue_and_dead_letter() -> None:
    queue = MemoryQueueBackend()
    await queue.create_job({"id": "job", "kind": "messages.send", "status": "queued"})

    requeued = await queue.requeue_job("job", error="temporary")
    assert requeued["status"] == "queued"

    dead = await queue.dead_letter_job("job", error="failed")

    assert dead["status"] == "dead_letter"
    assert dead["error"] == "failed"

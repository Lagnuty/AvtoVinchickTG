from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass
from unittest import TestCase, main
from unittest.mock import patch

import avto_vinchick_tg.runner as runner_module
from avto_vinchick_tg.runner import VinchikRunner
from avto_vinchick_tg.settings import AppConfig


@dataclass(frozen=True)
class FakeSentCode:
    phone: str = "+10000000000"
    phone_code_hash: str = "hash"


@dataclass(frozen=True)
class FakeResult:
    ok: bool = True
    sent_code: FakeSentCode | None = None
    password_required: bool = False
    error_type: str = ""
    status: str = "ok"
    message: str = ""


class FakeLayer:
    loops: list[asyncio.AbstractEventLoop] = []
    disconnected = False

    async def connect(self) -> None:
        self.loops.append(asyncio.get_running_loop())

    async def check_connection_result(self) -> FakeResult:
        self.loops.append(asyncio.get_running_loop())
        return FakeResult()

    async def send_code_result(self, phone: str) -> FakeResult:
        self.loops.append(asyncio.get_running_loop())
        return FakeResult(sent_code=FakeSentCode(phone=phone))

    async def sign_in_result(self, state, code: str) -> FakeResult:
        self.loops.append(asyncio.get_running_loop())
        return FakeResult()

    async def disconnect(self) -> None:
        self.disconnected = True


def wait_for(predicate, timeout: float = 2.0) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if predicate():
            return
        time.sleep(0.01)
    raise AssertionError("condition was not reached")


class RunnerLoginLoopTest(TestCase):
    def test_login_code_uses_same_event_loop(self) -> None:
        FakeLayer.loops = []
        layer = FakeLayer()
        logs: list[str] = []
        runner = VinchikRunner(logs.append)

        with patch.object(runner_module, "make_layer", lambda config: layer):
            runner.login_send_code(AppConfig(phone="+10000000000"))
            wait_for(lambda: any("Код отправлен" in log for log in logs))
            runner.login_submit_code("12345")
            wait_for(lambda: any("Вход выполнен" in log for log in logs))

        self.assertEqual(len(FakeLayer.loops), 4)
        self.assertEqual(len(set(FakeLayer.loops)), 1)
        self.assertTrue(layer.disconnected)


if __name__ == "__main__":
    main()

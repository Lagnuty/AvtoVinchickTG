import asyncio

from tg_api_zapret import FileSessionBackend, TelegramConfig, TelegramLayer


async def main() -> None:
    layer = TelegramLayer(
        TelegramConfig.from_env(),
        FileSessionBackend("telegram.session.txt"),
    )
    async with layer.lifespan():
        await layer.send_message("me", "Hello from tg-api-zapret")


if __name__ == "__main__":
    asyncio.run(main())


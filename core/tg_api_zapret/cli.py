from __future__ import annotations

import argparse
import asyncio
from dataclasses import replace
from getpass import getpass
import os
from pathlib import Path
import sys
from typing import Sequence

from telethon.errors import PasswordHashInvalidError, SessionPasswordNeededError

from tg_api_zapret.api import ApiState, create_app
from tg_api_zapret.client import TelegramLayer
from tg_api_zapret.config import (
    AppSettings,
    ClientProfile,
    OFFICIAL_DESKTOP_APP_VERSION,
    TelegramConfig,
    detect_lang_code,
    detect_system_lang_code,
    detect_system_version,
    normalize_account_name,
    validate_proxy_url,
)
from tg_api_zapret.sessions import FileSessionBackend, SQLiteSessionBackend, TelethonSessionFileBackend
from tg_api_zapret.version import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tg-api-zapret")
    parser.add_argument(
        "--session-file",
        default="~/.config/tg-api-zapret/session.txt",
        help="Path for StringSession storage.",
    )
    parser.add_argument("--session-db", help="SQLite database for session storage.")
    parser.add_argument("--session-key", default="default", help="SQLite session key.")
    parser.add_argument(
        "--account",
        help="Account name. If omitted, the active account from config is used.",
    )
    parser.add_argument(
        "--config-file",
        default="~/.config/tg-api-zapret/config.json",
        help="Path for app settings such as Telegram proxy URL.",
    )
    parser.add_argument(
        "--queue-backend",
        choices=["memory", "redis"],
        default=os.getenv("TG_API_QUEUE_BACKEND", "memory"),
        help="Queue backend for API background jobs.",
    )
    parser.add_argument(
        "--redis-url",
        default=os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0"),
        help="Redis URL for --queue-backend redis.",
    )
    parser.add_argument(
        "--menu",
        action="store_true",
        help="Open interactive menu instead of running a single command.",
    )

    subparsers = parser.add_subparsers(dest="command")

    login = subparsers.add_parser("login", help="Authorize and persist a Telegram session.")
    login.add_argument(
        "phone",
        nargs="?",
        help="Phone number in international format. If omitted, it is requested interactively.",
    )
    login.add_argument(
        "--password-env",
        default="TELEGRAM_2FA_PASSWORD",
        help="Environment variable with Telegram two-step password.",
    )

    request_code = subparsers.add_parser("request-code", help="Send a Telegram login code.")
    request_code.add_argument("phone", help="Phone number in international format.")

    confirm_code = subparsers.add_parser("confirm-code", help="Confirm a Telegram login code.")
    confirm_code.add_argument("phone", help="Phone number in international format.")
    confirm_code.add_argument("phone_code_hash", help="Hash returned by request-code.")
    confirm_code.add_argument("code", help="Telegram login code.")
    confirm_code.add_argument(
        "--password-env",
        default="TELEGRAM_2FA_PASSWORD",
        help="Environment variable with Telegram two-step password.",
    )

    subparsers.add_parser("status", help="Print authorization status.")

    send = subparsers.add_parser("send", help="Send a text message.")
    send.add_argument("entity", help="Username, phone, chat id, or peer.")
    send.add_argument("text", help="Message text.")

    dialogs = subparsers.add_parser("dialogs", help="List dialogs.")
    dialogs.add_argument("--limit", type=int, default=20)

    api = subparsers.add_parser("api", help="Start HTTP API server.")
    api.add_argument("--host", default="127.0.0.1")
    api.add_argument("--port", type=int, default=8080)
    api.add_argument(
        "--queue-backend",
        choices=["memory", "redis"],
        default=os.getenv("TG_API_QUEUE_BACKEND", "memory"),
        help="Queue backend for API background jobs.",
    )
    api.add_argument(
        "--redis-url",
        default=os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0"),
        help="Redis URL for --queue-backend redis.",
    )

    worker = subparsers.add_parser(
        "worker",
        help="Deprecated guard. Queue jobs are executed by the API owner process.",
    )
    worker.add_argument(
        "--queue-backend",
        choices=["redis"],
        default="redis",
        help="Worker backend. Production workers use Redis.",
    )
    worker.add_argument(
        "--redis-url",
        default=os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0"),
        help="Redis URL for worker jobs.",
    )
    worker.add_argument("--poll-timeout", type=int, default=5)

    set_proxy = subparsers.add_parser("set-proxy", help="Save proxy settings for Telegram.")
    set_proxy.add_argument(
        "proxy_url",
        nargs="?",
        help=(
            "Proxy URL: http://host:port, https://host:port, "
            "socks5://host:port, socks5h://host:port."
        ),
    )

    profile = subparsers.add_parser("set-client-profile", help="Set Telegram device name/profile.")
    profile.add_argument("--device-model", default="Telegram Desktop")
    profile.add_argument("--system-version", default=detect_system_version())
    profile.add_argument("--app-version", default=OFFICIAL_DESKTOP_APP_VERSION)
    profile.add_argument("--lang-code", default=detect_lang_code())
    profile.add_argument("--system-lang-code", default=detect_system_lang_code())

    subparsers.add_parser("clear-proxy", help="Remove saved proxy settings.")
    subparsers.add_parser("show-config", help="Print current app settings.")
    subparsers.add_parser("accounts", help="List known accounts.")

    use_account = subparsers.add_parser("use-account", help="Switch active account.")
    use_account.add_argument("account", help="Account name.")

    return parser


def main(argv: Sequence[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    asyncio.run(run(args))


async def run(args: argparse.Namespace) -> None:
    if args.menu:
        await run_menu(args)
        return

    if not args.command:
        raise RuntimeError("Choose a command or use --menu")

    settings_path = Path(args.config_file)
    settings = AppSettings.load(settings_path)

    if args.command == "set-proxy":
        proxy_url = args.proxy_url or prompt_proxy_url()
        validate_proxy_url(proxy_url)
        replace(settings, proxy_url=proxy_url).save(settings_path)
        print(f"proxy saved: {mask_proxy_url(proxy_url)}")
    elif args.command == "clear-proxy":
        replace(settings, proxy_url=None).save(settings_path)
        print("proxy cleared")
    elif args.command == "set-client-profile":
        profile = ClientProfile(
            device_model=args.device_model,
            system_version=args.system_version,
            app_version=args.app_version,
            lang_code=args.lang_code,
            system_lang_code=args.system_lang_code,
        )
        replace(settings, client_profile=profile).save(settings_path)
        print("client profile saved")
    elif args.command == "show-config":
        print_config(settings)
    elif args.command == "accounts":
        print_accounts(settings)
    elif args.command == "use-account":
        updated = settings.with_account(args.account)
        updated.save(settings_path)
        print(f"active account: {updated.active_account}")
    elif args.command == "api":
        await run_api(args)
    elif args.command == "worker":
        await run_worker(args)
    else:
        layer = build_layer(args, settings)
        async with layer.lifespan():
            await run_telegram_command(args, layer)


async def run_telegram_command(args: argparse.Namespace, layer: TelegramLayer) -> None:
    if args.command == "login":
            phone = args.phone or input("Phone number: ").strip()
            if not phone:
                raise RuntimeError("Phone number is required")

            sent_code = await layer.send_code(phone)
            try:
                await layer.sign_in(sent_code, input("Telegram code: ").strip())
            except SessionPasswordNeededError:
                await sign_in_with_password(layer, args.password_env, interactive_prompt=True)
            print("authorized")
    elif args.command == "request-code":
        sent_code = await layer.send_code(args.phone)
        print(sent_code.phone_code_hash)
    elif args.command == "confirm-code":
        from tg_api_zapret.client import SentCode

        sent_code = SentCode(phone=args.phone, phone_code_hash=args.phone_code_hash)
        try:
            await layer.sign_in(sent_code, args.code)
        except SessionPasswordNeededError:
            await sign_in_with_password(layer, args.password_env)
        print("authorized")
    elif args.command == "status":
        print("authorized" if await layer.is_authorized() else "not authorized")
    elif args.command == "send":
        await layer.send_message(args.entity, args.text)
        print("sent")
    elif args.command == "dialogs":
        dialogs = await layer.get_dialogs(limit=args.limit)
        for dialog in dialogs:
            print(f"{dialog.id}\t{dialog.name}")
    else:
        raise ValueError(f"Unsupported command: {args.command}")


async def run_menu(args: argparse.Namespace) -> None:
    settings_path = Path(args.config_file)
    while True:
        settings = AppSettings.load(settings_path)
        print()
        print("tg-api-zapret")
        print(f"Version: {__version__}")
        print(f"Account: {resolve_account(args, settings)}")
        print(f"Proxy: {mask_proxy_url(settings.proxy_url) if settings.proxy_url else 'not set'}")
        print(f"Device: {settings.client_profile.device_model}")
        print("1. Start Telegram layer / login")
        print("2. Status")
        print("3. Send message")
        print("4. List dialogs")
        print("5. Set proxy")
        print("6. Clear proxy")
        print("7. Show config")
        print("8. Set client name")
        print("9. Start HTTP API")
        print("10. Switch/add account")
        print("11. List accounts")
        print("0. Exit")

        choice = input("Choose: ").strip()
        if choice == "0":
            return
        try:
            if choice == "1":
                layer = build_layer(args, settings)
                async with layer.lifespan():
                    if await layer.is_authorized():
                        print("Telegram layer started: authorized")
                    else:
                        await run_telegram_command(
                            argparse.Namespace(
                                command="login",
                                phone=None,
                                password_env="TELEGRAM_2FA_PASSWORD",
                            ),
                            layer,
                        )
            elif choice == "2":
                layer = build_layer(args, settings)
                async with layer.lifespan():
                    print("authorized" if await layer.is_authorized() else "not authorized")
            elif choice == "3":
                entity = input("Entity/user/chat: ").strip()
                text = input("Text: ")
                layer = build_layer(args, settings)
                async with layer.lifespan():
                    await layer.send_message(entity, text)
                    print("sent")
            elif choice == "4":
                limit_value = input("Limit [20]: ").strip() or "20"
                layer = build_layer(args, settings)
                async with layer.lifespan():
                    dialogs = await layer.get_dialogs(limit=int(limit_value))
                    for dialog in dialogs:
                        print(f"{dialog.id}\t{dialog.name}")
            elif choice == "5":
                proxy_url = prompt_proxy_url()
                validate_proxy_url(proxy_url)
                replace(settings, proxy_url=proxy_url).save(settings_path)
                print(f"proxy saved: {mask_proxy_url(proxy_url)}")
            elif choice == "6":
                replace(settings, proxy_url=None).save(settings_path)
                print("proxy cleared")
            elif choice == "7":
                print_config(settings)
            elif choice == "8":
                profile = prompt_client_profile(settings.client_profile)
                replace(settings, client_profile=profile).save(settings_path)
                print("client profile saved")
            elif choice == "9":
                host = input("Host [127.0.0.1]: ").strip() or "127.0.0.1"
                port = int(input("Port [8080]: ").strip() or "8080")
                await run_api(argparse.Namespace(**vars(args), host=host, port=port))
            elif choice == "10":
                account = input("Account name: ").strip()
                updated = settings.with_account(account)
                updated.save(settings_path)
                args.account = updated.active_account
                print(f"active account: {updated.active_account}")
            elif choice == "11":
                print_accounts(settings)
            else:
                print("Unknown menu item")
        except RuntimeError as exc:
            print(f"Error: {exc}")


def build_layer(args: argparse.Namespace, settings: AppSettings) -> TelegramLayer:
    account = resolve_account(args, settings)
    if args.session_db:
        backend = SQLiteSessionBackend(Path(args.session_db), account)
    else:
        session_path = resolve_session_file(args.session_file, account)
        if account == "default" and session_path.suffix == ".session":
            backend = TelethonSessionFileBackend(session_path)
        else:
            backend = FileSessionBackend(session_path)
    return TelegramLayer(
        TelegramConfig.from_env(
            proxy_url=settings.proxy_url,
            client_profile=settings.client_profile,
        ),
        backend,
    )


async def run_api(args: argparse.Namespace) -> None:
    import uvicorn

    state = ApiState(
        config_file=args.config_file,
        session_file=args.session_file,
        session_db=args.session_db,
        default_account=resolve_account(args, AppSettings.load(args.config_file)),
        queue_backend=args.queue_backend,
        redis_url=args.redis_url,
    )
    app = create_app(state)
    config = uvicorn.Config(app, host=args.host, port=args.port)
    server = uvicorn.Server(config)
    await server.serve()


async def run_worker(args: argparse.Namespace) -> None:
    raise RuntimeError(
        "External queue workers are disabled. Start one API owner process with "
        "`python -m tg_api_zapret api --queue-backend redis --redis-url ...`. "
        "This prevents multiple processes from opening the same Telegram session."
    )


def prompt_proxy_url() -> str:
    print("Supported schemes: http, https, socks5, socks5h")
    print("Examples:")
    print("  http://127.0.0.1:8080")
    print("  socks5://user:password@127.0.0.1:1080")
    print("  socks5h://127.0.0.1:1080")
    proxy_url = input("Proxy URL: ").strip()
    if not proxy_url:
        raise RuntimeError("Proxy URL is required")
    return proxy_url


def print_config(settings: AppSettings) -> None:
    effective_proxy_url = settings.proxy_url or os.getenv("TELEGRAM_PROXY_URL")
    print(f"proxy_url={mask_proxy_url(effective_proxy_url) if effective_proxy_url else ''}")
    profile = settings.client_profile
    print(f"device_model={profile.device_model}")
    print(f"system_version={profile.system_version}")
    print(f"app_version={profile.app_version}")
    print(f"lang_code={profile.lang_code}")
    print(f"system_lang_code={profile.system_lang_code}")
    print(f"active_account={settings.active_account}")
    print(f"accounts={','.join(settings.accounts)}")


def print_accounts(settings: AppSettings) -> None:
    for account in settings.accounts:
        marker = "*" if account == settings.active_account else " "
        print(f"{marker} {account}")


def resolve_account(args: argparse.Namespace, settings: AppSettings) -> str:
    return normalize_account_name(getattr(args, "account", None) or settings.active_account)


def resolve_session_file(session_file: str, account: str) -> Path:
    base = Path(session_file).expanduser()
    if account == "default":
        return base
    return base.parent / "sessions" / f"{account}.session.txt"


def prompt_client_profile(current: ClientProfile) -> ClientProfile:
    device_model = input(f"Device name [{current.device_model}]: ").strip() or current.device_model
    system_version = input(f"System version [{current.system_version}]: ").strip()
    app_version = input(f"App version [{current.app_version}]: ").strip()
    lang_code = input(f"Lang code [{current.lang_code}]: ").strip()
    system_lang_code = input(f"System lang code [{current.system_lang_code}]: ").strip()
    return ClientProfile(
        device_model=device_model,
        system_version=system_version or current.system_version,
        app_version=app_version or current.app_version,
        lang_code=lang_code or current.lang_code,
        system_lang_code=system_lang_code or current.system_lang_code,
    )


def mask_proxy_url(proxy_url: str | None) -> str:
    if not proxy_url:
        return ""
    if "@" not in proxy_url:
        return proxy_url
    scheme_and_auth, address = proxy_url.rsplit("@", 1)
    scheme, auth = scheme_and_auth.split("://", 1)
    username = auth.split(":", 1)[0]
    return f"{scheme}://{username}:***@{address}"


def read_password(env_name: str, *, interactive_prompt: bool = False) -> str:
    value = os.getenv(env_name)
    if value:
        return value
    if interactive_prompt or sys.stdin.isatty():
        return getpass("Two-step password: ")
    raise RuntimeError(
        f"Telegram two-step password is required. Set {env_name} or run from an interactive TTY."
    )


async def sign_in_with_password(
    layer: TelegramLayer,
    env_name: str,
    *,
    interactive_prompt: bool = False,
    max_attempts: int = 3,
) -> None:
    env_password = os.getenv(env_name)
    if env_password:
        try:
            await layer.sign_in_password(env_password)
            return
        except PasswordHashInvalidError as exc:
            raise RuntimeError(f"Two-step password from {env_name} is invalid") from exc

    for attempt in range(1, max_attempts + 1):
        try:
            await layer.sign_in_password(read_password(env_name, interactive_prompt=interactive_prompt))
            return
        except PasswordHashInvalidError:
            attempts_left = max_attempts - attempt
            if attempts_left:
                print(f"Invalid two-step password. Attempts left: {attempts_left}")
            else:
                raise RuntimeError("Invalid two-step password")


if __name__ == "__main__":
    main()

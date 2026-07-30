from __future__ import annotations

import re
from urllib.request import Request, urlopen

from avto_vinchick_tg.bot_api import run_with_optional_socks_proxy


REMOTE_VERSION_URLS = [
    "https://raw.githubusercontent.com/Lagnuty/tg-api-zapret/main/tg_api_zapret/version.py",
    "https://raw.githubusercontent.com/Lagnuty/tg-api-zapret/master/tg_api_zapret/version.py",
]


def fetch_latest_core_version(proxy_url: str = "") -> str | None:
    for url in REMOTE_VERSION_URLS:
        try:
            request = Request(url, headers={"User-Agent": "AvtoVinchickTG"})
            text = run_with_optional_socks_proxy(proxy_url, lambda: read_text(request))
        except Exception:
            continue
        version = parse_version_py(text)
        if version:
            return version
    return None


def read_text(request: Request) -> str:
    with urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8")


def parse_version_py(text: str) -> str | None:
    match = re.search(r"""__version__\s*=\s*["']([^"']+)["']""", text)
    return match.group(1) if match else None


def is_newer_version(remote: str | None, local: str) -> bool:
    if not remote:
        return False
    return version_key(remote) > version_key(local)


def version_key(version: str) -> tuple[int, ...]:
    parts = re.findall(r"\d+", version)
    return tuple(int(part) for part in parts) or (0,)

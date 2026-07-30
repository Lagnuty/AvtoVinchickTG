from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import shutil
import subprocess
import sys
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from avto_vinchick_tg.bot_api import run_with_optional_socks_proxy
from avto_vinchick_tg.core_update import is_newer_version
from avto_vinchick_tg.settings import APP_DIR


APP_REPOSITORY = "Lagnuty/AvtoVinchickTG"
LATEST_RELEASE_URL = f"https://api.github.com/repos/{APP_REPOSITORY}/releases/latest"


@dataclass(frozen=True)
class AppRelease:
    version: str
    name: str
    download_url: str
    asset_name: str
    page_url: str


def fetch_latest_app_release(current_version: str, proxy_url: str = "") -> AppRelease | None:
    request = Request(
        LATEST_RELEASE_URL,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "AvtoVinchickTG",
        },
    )
    try:
        data = run_with_optional_socks_proxy(proxy_url, lambda: read_json(request))
    except HTTPError as exc:
        if exc.code == 404:
            return None
        raise
    version = normalize_tag(str(data.get("tag_name") or data.get("name") or ""))
    if not is_newer_version(version, current_version):
        return None
    asset = choose_windows_asset(data.get("assets") or [])
    if not asset:
        return None
    return AppRelease(
        version=version,
        name=str(data.get("name") or data.get("tag_name") or version),
        download_url=str(asset["browser_download_url"]),
        asset_name=str(asset["name"]),
        page_url=str(data.get("html_url") or ""),
    )


def download_release_asset(release: AppRelease, proxy_url: str = "") -> Path:
    updates_dir = APP_DIR / "updates"
    updates_dir.mkdir(parents=True, exist_ok=True)
    target = updates_dir / release.asset_name
    request = Request(release.download_url, headers={"User-Agent": "AvtoVinchickTG"})

    def download() -> None:
        with urlopen(request, timeout=120) as response, target.open("wb") as handle:
            shutil.copyfileobj(response, handle)

    run_with_optional_socks_proxy(proxy_url, download)
    return target


def install_downloaded_release(archive_path: Path) -> None:
    if not getattr(sys, "frozen", False):
        raise RuntimeError("Автообновление доступно только в exe-сборке.")
    if archive_path.suffix.lower() != ".msi":
        raise RuntimeError("Автообновление ожидает MSI installer из GitHub Release.")

    app_exe = Path(sys.executable).resolve()
    script_path = APP_DIR / "updates" / "apply-update.ps1"
    write_update_script(script_path, archive_path, app_exe, os_pid())
    subprocess.Popen(
        [
            "powershell.exe",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(script_path),
        ],
        close_fds=True,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )


def choose_windows_asset(assets: list[dict]) -> dict | None:
    installer_assets = [
        asset
        for asset in assets
        if str(asset.get("browser_download_url") or "").lower().endswith(".msi")
    ]
    preferred = [
        asset
        for asset in installer_assets
        if "avtovinchicktg" in str(asset.get("name") or "").casefold()
    ]
    return (preferred or installer_assets or [None])[0]


def write_update_script(
    script_path: Path,
    installer_path: Path,
    app_exe: Path,
    pid: int,
) -> None:
    script = f"""
$ErrorActionPreference = "Stop"
$pidToWait = {pid}
$installer = {ps_quote(installer_path)}
$exe = {ps_quote(app_exe)}
$target = Split-Path -Parent $exe
while (Get-Process -Id $pidToWait -ErrorAction SilentlyContinue) {{
    Start-Sleep -Milliseconds 400
}}
$args = @('/i', $installer, '/qn', '/norestart', "INSTALLFOLDER=$target")
Start-Process -FilePath 'msiexec.exe' -ArgumentList $args -Wait
Start-Process -FilePath $exe -WorkingDirectory $target
""".strip()
    script_path.parent.mkdir(parents=True, exist_ok=True)
    script_path.write_text(script + "\n", encoding="utf-8")


def read_json(request: Request) -> dict:
    with urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def normalize_tag(value: str) -> str:
    return value.strip().lstrip("vV")


def ps_quote(path: Path) -> str:
    return "'" + str(path).replace("'", "''") + "'"


def os_pid() -> int:
    import os

    return os.getpid()

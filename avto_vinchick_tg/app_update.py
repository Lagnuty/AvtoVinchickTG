from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile
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
    data = run_with_optional_socks_proxy(proxy_url, lambda: read_json(request))
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
    if archive_path.suffix.lower() != ".zip":
        raise RuntimeError("Автообновление ожидает zip-архив из GitHub Release.")

    app_exe = Path(sys.executable).resolve()
    app_dir = app_exe.parent
    extract_dir = APP_DIR / "updates" / archive_path.stem
    if extract_dir.exists():
        shutil.rmtree(extract_dir)
    extract_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive_path) as archive:
        archive.extractall(extract_dir)

    source_dir = find_payload_dir(extract_dir)
    script_path = APP_DIR / "updates" / "apply-update.ps1"
    write_update_script(script_path, source_dir, app_dir, app_exe, os_pid())
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
    zip_assets = [
        asset
        for asset in assets
        if str(asset.get("browser_download_url") or "").lower().endswith(".zip")
    ]
    preferred = [
        asset
        for asset in zip_assets
        if "avtovinchicktg" in str(asset.get("name") or "").casefold()
    ]
    return (preferred or zip_assets or [None])[0]


def find_payload_dir(extract_dir: Path) -> Path:
    exe_matches = list(extract_dir.rglob("AvtoVinchickTG.exe"))
    if not exe_matches:
        raise RuntimeError("В архиве обновления не найден AvtoVinchickTG.exe.")
    return exe_matches[0].parent


def write_update_script(
    script_path: Path,
    source_dir: Path,
    app_dir: Path,
    app_exe: Path,
    pid: int,
) -> None:
    script = f"""
$ErrorActionPreference = "Stop"
$pidToWait = {pid}
$source = {ps_quote(source_dir)}
$target = {ps_quote(app_dir)}
$exe = {ps_quote(app_exe)}
while (Get-Process -Id $pidToWait -ErrorAction SilentlyContinue) {{
    Start-Sleep -Milliseconds 400
}}
Copy-Item -Path (Join-Path $source '*') -Destination $target -Recurse -Force
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

from __future__ import annotations

import hashlib
from pathlib import Path
import re
import xml.etree.ElementTree as ET


APP_NAME = "AvtoVinchickTG"
MANUFACTURER = "Lagnuty"
UPGRADE_CODE = "3F66180F-8E27-48D9-B031-58D7B165DCB4"
DIST_DIR = Path("dist") / APP_NAME
ICON_PATH = Path("assets") / "AvtoVinchickTG.ico"
LICENSE_PATH = Path("installer") / "License.rtf"
OUTPUT_PATH = Path("installer") / "AvtoVinchickTG.wxs"
WIX_NS = "http://wixtoolset.org/schemas/v4/wxs"
UI_NS = "http://wixtoolset.org/schemas/v4/wxs/ui"


def main() -> None:
    version = read_app_version()
    if not (DIST_DIR / f"{APP_NAME}.exe").exists():
        raise SystemExit(f"Build app first: {DIST_DIR / f'{APP_NAME}.exe'}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ET.register_namespace("", WIX_NS)
    ET.register_namespace("ui", UI_NS)
    wix = element("Wix")
    package = sub(
        wix,
        "Package",
        {
            "Name": APP_NAME,
            "Manufacturer": MANUFACTURER,
            "Version": version,
            "UpgradeCode": UPGRADE_CODE,
            "Scope": "perUser",
        },
    )
    sub(package, "MediaTemplate", {"EmbedCab": "yes"})
    sub(package, "Icon", {"Id": "AppIcon.ico", "SourceFile": str(ICON_PATH)})
    sub(package, "Property", {"Id": "ARPPRODUCTICON", "Value": "AppIcon.ico"})
    sub(package, "Property", {"Id": "DISABLEROLLBACK", "Value": "1"})
    sub(package, "Property", {"Id": "ROOTDRIVE", "Value": "C:\\"})
    install_folder_property = sub(package, "Property", {"Id": "INSTALLFOLDER"})
    sub(
        install_folder_property,
        "RegistrySearch",
        {
            "Id": "FindExistingInstallFolder",
            "Root": "HKCU",
            "Key": rf"Software\{MANUFACTURER}\{APP_NAME}",
            "Name": "InstallFolder",
            "Type": "raw",
        },
    )
    sub(package, "Property", {"Id": "WIXUI_INSTALLDIR", "Value": "INSTALLFOLDER"})
    sub(package, "WixVariable", {"Id": "WixUILicenseRtf", "Value": str(LICENSE_PATH)})
    sub_ui(package, "WixUI", {"Id": "WixUI_InstallDir"})

    sub(package, "StandardDirectory", {"Id": "SystemFolder"})
    local_app_data = sub(package, "StandardDirectory", {"Id": "LocalAppDataFolder"})
    programs = sub(local_app_data, "Directory", {"Id": "ProgramsFolder", "Name": "Programs"})
    install_folder = sub(programs, "Directory", {"Id": "INSTALLFOLDER", "Name": APP_NAME})
    directory_ids = {Path("."): "INSTALLFOLDER"}
    build_directories(install_folder, directory_ids)

    start_menu = sub(package, "StandardDirectory", {"Id": "ProgramMenuFolder"})
    sub(start_menu, "Directory", {"Id": "ApplicationProgramsFolder", "Name": APP_NAME})

    component_group = sub(package, "ComponentGroup", {"Id": "AppFiles"})
    for file_path in sorted(path for path in DIST_DIR.rglob("*") if path.is_file()):
        rel_path = file_path.relative_to(DIST_DIR)
        component_id = stable_id("Cmp", rel_path)
        file_id = stable_id("File", rel_path)
        component = sub(
            package,
            "Component",
            {
                "Id": component_id,
                "Directory": directory_ids[rel_path.parent],
                "Guid": "*",
            },
        )
        sub(
            component,
            "File",
            {
                "Id": file_id,
                "Source": str(file_path),
                "KeyPath": "yes",
            },
        )
        sub(component_group, "ComponentRef", {"Id": component_id})

    shortcut_component = sub(
        package,
        "Component",
        {
            "Id": "StartMenuShortcutComponent",
            "Directory": "ApplicationProgramsFolder",
            "Guid": "*",
        },
    )
    sub(
        shortcut_component,
        "Shortcut",
        {
            "Id": "StartMenuShortcut",
            "Name": APP_NAME,
            "Description": APP_NAME,
            "Target": "[INSTALLFOLDER]AvtoVinchickTG.exe",
            "WorkingDirectory": "INSTALLFOLDER",
            "Icon": "AppIcon.ico",
        },
    )
    sub(shortcut_component, "RemoveFolder", {"Id": "RemoveApplicationProgramsFolder", "On": "uninstall"})
    sub(
        shortcut_component,
        "RegistryValue",
        {
            "Root": "HKCU",
            "Key": rf"Software\{MANUFACTURER}\{APP_NAME}",
            "Name": "installed",
            "Type": "integer",
            "Value": "1",
            "KeyPath": "yes",
        },
    )
    sub(
        shortcut_component,
        "RegistryValue",
        {
            "Root": "HKCU",
            "Key": rf"Software\{MANUFACTURER}\{APP_NAME}",
            "Name": "InstallFolder",
            "Type": "string",
            "Value": "[INSTALLFOLDER]",
        },
    )
    install_sequence = sub(package, "InstallExecuteSequence")
    sub(
        package,
        "CustomAction",
        {
            "Id": "KillRunningApplication",
            "Directory": "SystemFolder",
            "ExeCommand": 'taskkill.exe /F /IM AvtoVinchickTG.exe /T',
            "Execute": "immediate",
            "Return": "ignore",
        },
    )
    sub(
        install_sequence,
        "Custom",
        {
            "Action": "KillRunningApplication",
            "Before": "InstallValidate",
        },
    )
    sub(
        package,
        "CustomAction",
        {
            "Id": "DeleteExistingExe",
            "Directory": "INSTALLFOLDER",
            "ExeCommand": 'cmd.exe /C if exist "AvtoVinchickTG.exe" del /F /Q "AvtoVinchickTG.exe"',
            "Execute": "immediate",
            "Return": "ignore",
        },
    )
    sub(
        install_sequence,
        "Custom",
        {
            "Action": "DeleteExistingExe",
            "Before": "InstallFiles",
        },
    )
    sub(install_sequence, "DisableRollback", {"Before": "InstallInitialize"})

    feature = sub(package, "Feature", {"Id": "MainFeature", "Title": APP_NAME, "Level": "1"})
    sub(feature, "ComponentGroupRef", {"Id": "AppFiles"})
    sub(feature, "ComponentRef", {"Id": "StartMenuShortcutComponent"})

    indent(wix)
    ET.ElementTree(wix).write(OUTPUT_PATH, encoding="utf-8", xml_declaration=True)
    print(OUTPUT_PATH)


def build_directories(parent: ET.Element, directory_ids: dict[Path, str]) -> None:
    dirs = sorted({path.parent for path in DIST_DIR.rglob("*") if path.is_file() and path.parent != DIST_DIR})
    elements = {Path("."): parent}
    for directory in dirs:
        rel_path = directory.relative_to(DIST_DIR)
        current_parent_path = Path(".")
        current_parent = parent
        for part in rel_path.parts:
            current_path = current_parent_path / part
            if current_path not in elements:
                directory_id = stable_id("Dir", current_path)
                directory_ids[current_path] = directory_id
                elements[current_path] = sub(current_parent, "Directory", {"Id": directory_id, "Name": part})
            current_parent_path = current_path
            current_parent = elements[current_path]


def read_app_version() -> str:
    text = Path("avto_vinchick_tg/__init__.py").read_text(encoding="utf-8")
    match = re.search(r'__version__\s*=\s*"([^"]+)"', text)
    if not match:
        raise SystemExit("Cannot read app version")
    return match.group(1)


def stable_id(prefix: str, value: Path) -> str:
    digest = hashlib.sha1(str(value).replace("\\", "/").encode("utf-8")).hexdigest()[:16]
    return f"{prefix}_{digest}"


def element(tag: str, attrs: dict[str, str] | None = None) -> ET.Element:
    return ET.Element(f"{{{WIX_NS}}}{tag}", attrs or {})


def sub(parent: ET.Element, tag: str, attrs: dict[str, str] | None = None) -> ET.Element:
    return ET.SubElement(parent, f"{{{WIX_NS}}}{tag}", attrs or {})


def sub_ui(parent: ET.Element, tag: str, attrs: dict[str, str] | None = None) -> ET.Element:
    return ET.SubElement(parent, f"{{{UI_NS}}}{tag}", attrs or {})


def indent(elem: ET.Element, level: int = 0) -> None:
    space = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = space + "  "
        for child in elem:
            indent(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = space
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = space


if __name__ == "__main__":
    main()

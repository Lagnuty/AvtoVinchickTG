$ErrorActionPreference = "Stop"

powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\build_installer.ps1
if ($LASTEXITCODE -ne 0) {
    throw "build_installer.ps1 failed with exit code $LASTEXITCODE"
}

$version = (Select-String -Path "avto_vinchick_tg\__init__.py" -Pattern '__version__ = "([^"]+)"').Matches[0].Groups[1].Value
$installer = "dist\installer\AvtoVinchickTG-Setup-$version.exe"
if (-not (Test-Path $installer)) {
    throw "Installer not found: $installer"
}
Write-Host "GitHub Release asset: $installer"

$ErrorActionPreference = "Stop"

powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\build_msi.ps1
if ($LASTEXITCODE -ne 0) {
    throw "build_msi.ps1 failed with exit code $LASTEXITCODE"
}

$version = (Select-String -Path "avto_vinchick_tg\__init__.py" -Pattern '__version__ = "([^"]+)"').Matches[0].Groups[1].Value
$installer = "dist\msi\AvtoVinchickTG-$version.msi"
if (-not (Test-Path $installer)) {
    throw "MSI not found: $installer"
}
Write-Host "GitHub Release asset: $installer"

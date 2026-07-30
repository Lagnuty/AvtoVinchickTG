$ErrorActionPreference = "Stop"
function Run-Step {
    param([string]$FilePath, [string[]]$Arguments)
    & $FilePath @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed ($LASTEXITCODE): $FilePath $($Arguments -join ' ')"
    }
}

$python = ".venv\Scripts\python.exe"
$wix = "D:\Documents\AIprojects\tools\wix\wix.exe"

if (-not (Test-Path $python)) {
    $python = "python"
}
if (-not (Test-Path $wix)) {
    throw "WiX Toolset не найден: $wix"
}

powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\build_exe.ps1
if ($LASTEXITCODE -ne 0) {
    throw "build_exe.ps1 failed with exit code $LASTEXITCODE"
}

Run-Step $python @("scripts\generate_wix.py")
$version = (Select-String -Path "avto_vinchick_tg\__init__.py" -Pattern '__version__ = "([^"]+)"').Matches[0].Groups[1].Value
New-Item -ItemType Directory -Force -Path "dist\msi" | Out-Null
Run-Step $wix @("build", "installer\AvtoVinchickTG.wxs", "-o", "dist\msi\AvtoVinchickTG-$version.msi")
Write-Host "MSI: dist\msi\AvtoVinchickTG-$version.msi"

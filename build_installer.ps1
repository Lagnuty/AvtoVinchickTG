$ErrorActionPreference = "Stop"
function Run-Step {
    param([string]$FilePath, [string[]]$Arguments)
    & $FilePath @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed ($LASTEXITCODE): $FilePath $($Arguments -join ' ')"
    }
}

$python = ".venv\Scripts\python.exe"
$iscc = "D:\Documents\AIprojects\tools\InnoSetup6\ISCC.exe"

if (-not (Test-Path $python)) {
    $python = "python"
}
if (-not (Test-Path $iscc)) {
    throw "Inno Setup не найден: $iscc"
}

powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\build_exe.ps1
if ($LASTEXITCODE -ne 0) {
    throw "build_exe.ps1 failed with exit code $LASTEXITCODE"
}
$version = (Select-String -Path "avto_vinchick_tg\__init__.py" -Pattern '__version__ = "([^"]+)"').Matches[0].Groups[1].Value
Run-Step $iscc @("/DAppVersion=$version", "installer\AvtoVinchickTG.iss")
Write-Host "Installer: dist\installer\AvtoVinchickTG-Setup-$version.exe"

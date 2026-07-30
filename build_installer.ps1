$ErrorActionPreference = "Stop"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\build_msi.ps1
if ($LASTEXITCODE -ne 0) {
    throw "build_msi.ps1 failed with exit code $LASTEXITCODE"
}

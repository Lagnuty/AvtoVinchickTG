$ErrorActionPreference = "Stop"
$version = (Select-String -Path "avto_vinchick_tg\__init__.py" -Pattern '__version__ = "([^"]+)"').Matches[0].Groups[1].Value
$source = "dist\AvtoVinchickTG"
$target = "dist\AvtoVinchickTG-$version.zip"
$python = ".venv\Scripts\python.exe"
if (-not (Test-Path $source)) {
    throw "Сначала соберите exe через .\build_exe.ps1"
}
if (-not (Test-Path $python)) {
    $python = "python"
}
if (Test-Path $target) {
    Remove-Item -LiteralPath $target -Force
}
& $python -c "from pathlib import Path; import zipfile; source=Path(r'$source'); target=Path(r'$target'); z=zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED); [z.write(path, path.relative_to(source)) for path in source.rglob('*') if path.is_file()]; z.close()"
Write-Host "Release asset: $target"

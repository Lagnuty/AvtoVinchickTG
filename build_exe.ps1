$ErrorActionPreference = "Stop"
function Run-Step {
    param([string]$FilePath, [string[]]$Arguments)
    & $FilePath @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed ($LASTEXITCODE): $FilePath $($Arguments -join ' ')"
    }
}

$python = $null
$candidates = @(
    ".venv\Scripts\python.exe",
    "D:\Documents\AIprojects\tools\python\python.exe",
    "python",
    "py"
)
foreach ($candidate in $candidates) {
    $cmd = Get-Command $candidate -ErrorAction SilentlyContinue
    if ($cmd) {
        $python = $candidate
        break
    }
}
if (-not $python) {
    throw "Python не найден. Установите Python или положите portable Python в D:\Documents\AIprojects\tools\python\python.exe"
}

Run-Step $python @("-m", "pip", "install", "-r", "requirements.txt")
if (-not (Test-Path "assets\AvtoVinchickTG.ico")) {
    Run-Step $python @("scripts\generate_icon.py")
}
Run-Step $python @("-m", "PyInstaller", "--clean", "-y", "--noconsole", "--name", "AvtoVinchickTG", "--icon", "assets\AvtoVinchickTG.ico", "--add-data", "assets;assets", "main.py")

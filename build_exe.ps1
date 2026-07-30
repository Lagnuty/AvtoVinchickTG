$ErrorActionPreference = "Stop"
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

& $python -m pip install -U pip
& $python -m pip install -r requirements.txt
& $python -m PyInstaller --clean -y --noconsole --name AvtoVinchickTG main.py

$location = (Get-Location).Path
$path = $location + "\venv"
$update = $location + "\update.ps1"
$script = $location + "\venv\Scripts\Activate.ps1"
$command = (Get-Command pip)

$do_update = $false

if (Test-Path -Path $path) {
    echo "[Venv] An existing Python Virtual Environment found"
} else {
    echo "[Venv] Created new Python Virtual Environment"
    python -m venv $path
}

Invoke-Expression $script

if ($do_update -eq $true) {
    pip install -e .
}

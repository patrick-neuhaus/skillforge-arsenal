# Register a Windows Scheduled Task to run the Codex token collector every minute.

param(
    [string]$TaskName = "CodexTokenCollector",
    [string]$WebhookUrl = "http://localhost:3002/api/webhook/track-tokens",
    [string]$WebhookToken = ""
)

$ErrorActionPreference = "Stop"

$scriptPath = Join-Path $PSScriptRoot "codex-token-collector.py"
if (-not (Test-Path -LiteralPath $scriptPath)) {
    Write-Error "Collector not found: $scriptPath"
    exit 1
}

$python = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $python) {
    $python = (Get-Command py -ErrorAction SilentlyContinue).Source
}
if (-not $python) {
    Write-Error "Python not found in PATH."
    exit 1
}

$envPrefix = "`$env:TOKEN_TRACKER_WEBHOOK='$WebhookUrl';"
if ($WebhookToken) {
    $envPrefix += "`$env:TOKEN_TRACKER_TOKEN='$WebhookToken';"
}
$argument = "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -Command $envPrefix & '$python' '$scriptPath'"

$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument $argument
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) -RepetitionInterval (New-TimeSpan -Minutes 1)
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -MultipleInstances IgnoreNew

Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Force | Out-Null
Write-Host "Scheduled task registered: $TaskName"

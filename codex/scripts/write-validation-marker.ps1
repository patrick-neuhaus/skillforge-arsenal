# Create a Codex validation marker for instruction-file edits.
# Usage:
#   Get-Content draft.md -Raw | powershell -File write-validation-marker.ps1 -Score 85 -RubricType agents-md
#   powershell -File write-validation-marker.ps1 -Path .\AGENTS.md -Score 85 -RubricType agents-md

param(
    [Parameter(Mandatory)][int]$Score,
    [Parameter(Mandatory)][string]$RubricType,
    [string]$Note = "",
    [string]$Path = ""
)

$ErrorActionPreference = "Stop"

function Normalize-InstructionText {
    param([AllowNull()][string]$Text)
    if ($null -eq $Text) { return "" }
    return (($Text -replace "`r`n", "`n") -replace "`r", "`n")
}

function Get-StringSha256 {
    param([AllowEmptyString()][string]$Text)
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($Text)
    $sha256 = [System.Security.Cryptography.SHA256]::Create()
    try {
        return (($sha256.ComputeHash($bytes) | ForEach-Object { $_.ToString("x2") }) -join "")
    } finally {
        $sha256.Dispose()
    }
}

if ($Score -lt 80) {
    Write-Error "Score $Score < 80. Marker rejected."
    exit 1
}

$resolvedPath = $null
if ($Path) {
    $resolvedPath = (Resolve-Path -LiteralPath $Path).Path
    $content = [System.IO.File]::ReadAllText($resolvedPath, [System.Text.Encoding]::UTF8)
} else {
    $content = [Console]::In.ReadToEnd()
}
if (-not $content) {
    Write-Error "No content received via stdin or -Path."
    exit 1
}

$validatedDir = Join-Path $env:USERPROFILE ".codex\.validated"
if (-not (Test-Path -LiteralPath $validatedDir)) {
    New-Item -ItemType Directory -Path $validatedDir -Force | Out-Null
}

$canonicalContent = Normalize-InstructionText $content
$canonicalHash = Get-StringSha256 $canonicalContent
$rawHash = Get-StringSha256 $content
$timestamp = [DateTimeOffset]::Now.ToUnixTimeSeconds()
$markerPath = Join-Path $validatedDir "$canonicalHash-$timestamp.marker"

$metadata = @{
    marker_version = 2
    hash_algorithm = "sha256:utf8-string:lf-normalized"
    score = $Score
    rubric_type = $RubricType
    note = $Note
    created_at = (Get-Date).ToString("o")
    content_sha256 = $canonicalHash
    canonical_content_sha256 = $canonicalHash
    raw_content_sha256 = $rawHash
    content_length = $content.Length
    source_path = $resolvedPath
} | ConvertTo-Json -Compress

Set-Content -LiteralPath $markerPath -Value $metadata -Encoding UTF8

Write-Host "Marker written: $markerPath"
Write-Host "Hash: $($canonicalHash.Substring(0, 16))..."
Write-Host "Score: $Score / Rubric: $RubricType"

# Pragmatic Codex instruction-edit auditor.
# Fails when instruction files changed without a fresh marker bound to final file content.

param(
    [int]$MarkerTtlSeconds = 300,
    [string]$BaselinePath = (Join-Path $env:USERPROFILE ".codex\.validated\audit-state.json"),
    [switch]$InitializeBaseline
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

function Get-InstructionFileHash {
    param([Parameter(Mandatory)][string]$Path)
    $content = [System.IO.File]::ReadAllText($Path, [System.Text.Encoding]::UTF8)
    return Get-StringSha256 (Normalize-InstructionText $content)
}

function Get-PathKey {
    param([Parameter(Mandatory)][string]$Path)
    return ([System.IO.Path]::GetFullPath($Path)).ToLowerInvariant()
}

function Add-ChangedItem {
    param(
        [Parameter(Mandatory)]$Map,
        [Parameter(Mandatory)][string]$Path,
        [Parameter(Mandatory)][string]$Source,
        [string]$Status = ""
    )
    $fullPath = [System.IO.Path]::GetFullPath($Path)
    $key = Get-PathKey $fullPath
    if ($Map.ContainsKey($key)) { return }
    $exists = Test-Path -LiteralPath $fullPath -PathType Leaf
    $hash = $null
    if ($exists) { $hash = Get-InstructionFileHash $fullPath }
    $Map[$key] = [pscustomobject]@{
        Key = $key
        Path = $fullPath
        Source = $Source
        Status = $Status
        Exists = $exists
        Hash = $hash
    }
}

function Read-Baseline {
    param([Parameter(Mandatory)][string]$Path)
    $baseline = @{}
    if (-not (Test-Path -LiteralPath $Path)) { return $baseline }
    $json = Get-Content -LiteralPath $Path -Raw
    if (-not $json) { return $baseline }
    $parsed = $json | ConvertFrom-Json
    foreach ($property in $parsed.PSObject.Properties) {
        $baseline[$property.Name] = [string]$property.Value
    }
    return $baseline
}

function Write-Baseline {
    param(
        [Parameter(Mandatory)]$Baseline,
        [Parameter(Mandatory)][string]$Path
    )
    $dir = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
    $ordered = [ordered]@{}
    foreach ($key in ($Baseline.Keys | Sort-Object)) {
        $ordered[$key] = $Baseline[$key]
    }
    $ordered | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath $Path -Encoding UTF8
}

function Get-FreshMarkerHashes {
    param(
        [Parameter(Mandatory)][string]$ValidatedDir,
        [Parameter(Mandatory)][int]$TtlSeconds
    )
    $hashes = @{}
    if (-not (Test-Path -LiteralPath $ValidatedDir)) { return $hashes }
    $now = Get-Date
    $markers = Get-ChildItem -LiteralPath $ValidatedDir -Filter "*.marker" -ErrorAction SilentlyContinue |
        Where-Object { ($now - $_.LastWriteTime).TotalSeconds -le $TtlSeconds }
    foreach ($marker in $markers) {
        try {
            $metadata = Get-Content -LiteralPath $marker.FullName -Raw | ConvertFrom-Json
            foreach ($candidate in @($metadata.canonical_content_sha256, $metadata.content_sha256, $metadata.raw_content_sha256)) {
                if ($candidate) { $hashes[[string]$candidate] = $marker.FullName }
            }
        } catch {
            Write-Warning "Ignoring unreadable marker: $($marker.FullName)"
        }
    }
    return $hashes
}

$githubRoot = Join-Path $env:USERPROFILE "Documents\Github"
$repoRoots = New-Object System.Collections.Generic.List[string]
foreach ($explicitRepo in @(
    (Join-Path $githubRoot "skillforge-arsenal"),
    (Join-Path $githubRoot "claude-token-tracker"),
    (Join-Path $githubRoot "maestro")
)) {
    if (Test-Path -LiteralPath (Join-Path $explicitRepo ".git")) { $repoRoots.Add($explicitRepo) }
}
if (Test-Path -LiteralPath $githubRoot) {
    Get-ChildItem -LiteralPath $githubRoot -Force -Directory -ErrorAction SilentlyContinue |
        Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName ".git") } |
        ForEach-Object { $repoRoots.Add($_.FullName) }
}
$repoRoots = $repoRoots | Sort-Object -Unique

$instructionPattern = '(?i)(AGENTS\.md$|CLAUDE\.md$|SKILL\.md$|rules[\\/].*\.md$|codex[\\/]rules[\\/].*\.md$|codex[\\/]AGENTS\.md$|library[\\/].*\.(md|yaml)$|hooks[\\/].*\.(ps1|sh)$|scripts[\\/].*(validation|audit|junction|runtime|collector).*\.(ps1|py|sh)$|(^|[\\/])(checkpoints|plans|specs|decisions)[\\/].*\.md$|(^|[\\/])prompts[\\/].*\.(md|yaml|json|txt)$|(^|[\\/])[^\\/]*(prompt|system-prompt)[^\\/]*\.(md|yaml|json|txt)$)'
$changed = @{}

foreach ($repo in $repoRoots) {
    $status = git -C $repo status --porcelain --untracked-files=all
    foreach ($line in $status) {
        if (-not $line -or $line.Length -lt 4) { continue }
        $statusCode = $line.Substring(0, 2)
        $path = $line.Substring(3).Trim()
        if ($path -match ' -> ') { $path = ($path -split ' -> ')[-1] }
        $path = $path.Trim('"')
        if ($path -match $instructionPattern) {
            Add-ChangedItem -Map $changed -Path (Join-Path $repo $path) -Source $repo -Status $statusCode
        }
    }
}

$baseline = Read-Baseline $BaselinePath
$standaloneInstructionFiles = @(
    (Join-Path $githubRoot "AGENTS.md")
)
foreach ($file in $standaloneInstructionFiles) {
    if (-not (Test-Path -LiteralPath $file -PathType Leaf)) { continue }
    $key = Get-PathKey $file
    $hash = Get-InstructionFileHash $file
    if ((-not $baseline.ContainsKey($key)) -or $baseline[$key] -ne $hash) {
        Add-ChangedItem -Map $changed -Path $file -Source "standalone" -Status "baseline"
    }
}

if ($changed.Count -eq 0) {
    Write-Host "No instruction-file edits detected."
    exit 0
}

$validatedDir = Join-Path $env:USERPROFILE ".codex\.validated"
$freshHashes = Get-FreshMarkerHashes -ValidatedDir $validatedDir -TtlSeconds $MarkerTtlSeconds
$failures = New-Object System.Collections.Generic.List[string]
$validated = New-Object System.Collections.Generic.List[string]
$baselineKnown = New-Object System.Collections.Generic.List[string]
$initialized = New-Object System.Collections.Generic.List[string]
$baselineChanged = $false

foreach ($item in ($changed.Values | Sort-Object Path)) {
    if (-not $item.Exists) {
        if ($InitializeBaseline) {
            if ($baseline.ContainsKey($item.Key)) { $baseline.Remove($item.Key); $baselineChanged = $true }
            $initialized.Add("deleted baseline: $($item.Path)")
        } else {
            $failures.Add("deleted/no final hash: $($item.Path)")
        }
        continue
    }

    if ($freshHashes.ContainsKey($item.Hash)) {
        $validated.Add("$($item.Path) [hash $($item.Hash.Substring(0, 12)) marker $($freshHashes[$item.Hash])]")
        $baseline[$item.Key] = $item.Hash
        $baselineChanged = $true
        continue
    }

    if ($baseline.ContainsKey($item.Key) -and $baseline[$item.Key] -eq $item.Hash) {
        $baselineKnown.Add($item.Path)
        continue
    }

    if ($InitializeBaseline) {
        $baseline[$item.Key] = $item.Hash
        $baselineChanged = $true
        $initialized.Add("$($item.Path) [hash $($item.Hash.Substring(0, 12))]")
        continue
    }

    $failures.Add("$($item.Path) [hash $($item.Hash.Substring(0, 12)) source $($item.Source) status $($item.Status)]")
}

if ($failures.Count -gt 0) {
    Write-Error ("Instruction edits detected without matching fresh validation marker or baseline:`n" + ($failures -join "`n"))
    exit 1
}

if ($baselineChanged) { Write-Baseline -Baseline $baseline -Path $BaselinePath }

Write-Host "Instruction edits have matching validation markers or known baseline hashes."
if ($validated.Count -gt 0) {
    Write-Host "Validated by fresh hash-bound marker:"
    $validated | ForEach-Object { Write-Host "  $_" }
}
if ($baselineKnown.Count -gt 0) {
    Write-Host "Unchanged from audit baseline:"
    $baselineKnown | ForEach-Object { Write-Host "  $_" }
}
if ($initialized.Count -gt 0) {
    Write-Host "Initialized baseline entries:"
    $initialized | ForEach-Object { Write-Host "  $_" }
}
exit 0

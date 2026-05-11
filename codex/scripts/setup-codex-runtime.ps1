# Setup Codex runtime for Patrick's SkillForge ecosystem.
# Creates junctions/copies under ~/.codex without copying SkillForge skills.

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$codexDir = Join-Path $env:USERPROFILE ".codex"
$codexRuntimeDir = Join-Path $repoRoot "codex"

if (-not (Test-Path -LiteralPath $codexDir)) {
    New-Item -ItemType Directory -Path $codexDir -Force | Out-Null
}

function Set-Junction {
    param(
        [Parameter(Mandatory)][string]$Path,
        [Parameter(Mandatory)][string]$Target
    )
    if (-not (Test-Path -LiteralPath $Target)) {
        Write-Warning "Target missing, skipping junction: $Target"
        return
    }
    if (Test-Path -LiteralPath $Path) {
        $item = Get-Item -LiteralPath $Path -Force
        if ($item.LinkType -eq "Junction" -and $item.Target -and $item.Target[0] -eq $Target) {
            return
        }
        Remove-Item -LiteralPath $Path -Recurse -Force
    }
    New-Item -ItemType Junction -Path $Path -Target $Target | Out-Null
}

& (Join-Path $PSScriptRoot "setup-codex-junctions.ps1")

Set-Junction -Path (Join-Path $codexDir "rules") -Target (Join-Path $codexRuntimeDir "rules")
Set-Junction -Path (Join-Path $codexDir "scripts") -Target (Join-Path $codexRuntimeDir "scripts")
Set-Junction -Path (Join-Path $codexDir "library") -Target (Join-Path $env:USERPROFILE ".claude\library")
Set-Junction -Path (Join-Path $codexDir "context-tree") -Target (Join-Path $env:USERPROFILE ".claude\context-tree")

$agentsSource = Join-Path $codexRuntimeDir "AGENTS.md"
$agentsTarget = Join-Path $codexDir "AGENTS.md"
Copy-Item -LiteralPath $agentsSource -Destination $agentsTarget -Force

if (-not (Test-Path -LiteralPath (Join-Path $codexDir ".validated"))) {
    New-Item -ItemType Directory -Path (Join-Path $codexDir ".validated") -Force | Out-Null
}

Write-Host "Codex runtime ready at $codexDir"
Write-Host "Restart Codex to load ~/.codex/AGENTS.md and SkillForge skills."

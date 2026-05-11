# Sync SkillForge skills into Codex via junctions.
# Idempotent. Preserves ~/.codex/skills/.system.

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$skillforgeSkills = Join-Path $repoRoot "skills"
$codexSkills = Join-Path $env:USERPROFILE ".codex\skills"

if (-not (Test-Path -LiteralPath $skillforgeSkills)) {
    Write-Error "SkillForge skills dir not found: $skillforgeSkills"
    exit 1
}

if (-not (Test-Path -LiteralPath $codexSkills)) {
    New-Item -ItemType Directory -Path $codexSkills -Force | Out-Null
}

$created = 0
$skipped = 0
$replaced = 0

Get-ChildItem -LiteralPath $skillforgeSkills -Directory | Sort-Object Name | ForEach-Object {
    $name = $_.Name
    $target = $_.FullName
    $link = Join-Path $codexSkills $name

    if (Test-Path -LiteralPath $link) {
        $item = Get-Item -LiteralPath $link -Force
        if ($item.LinkType -eq "Junction" -and $item.Target -and $item.Target[0] -eq $target) {
            $skipped++
            return
        }
        if ($name -eq ".system") {
            $skipped++
            return
        }
        Remove-Item -LiteralPath $link -Recurse -Force
        $replaced++
    }

    New-Item -ItemType Junction -Path $link -Target $target | Out-Null
    $created++
}

Write-Host "Codex skill junctions ready."
Write-Host "  Created:  $created"
Write-Host "  Replaced: $replaced"
Write-Host "  Skipped:  $skipped"
Write-Host "Restart Codex to reload skill metadata."

# setup-junctions.ps1 — Wave 6 — sync skillforge -> AppData via junctions
# Uso: powershell -ExecutionPolicy Bypass -File setup-junctions.ps1
# Idempotent: rodar 2x = mesmo resultado.
# Usado pra: setup inicial OU recovery pos Claude Code update que reseta AppData.

$ErrorActionPreference = "Stop"

# Resolve paths via env vars (portable)
$SF = Join-Path $PSScriptRoot "..\skills"
if (-not (Test-Path $SF)) {
    $SF = Join-Path $env:USERPROFILE "Documents\Github\skillforge-arsenal\skills"
}
if (-not (Test-Path $SF)) {
    Write-Error "Skillforge skills dir nao encontrado. Edita o path no script."
    exit 1
}

$claudeBase = Join-Path $env:APPDATA "Claude\local-agent-mode-sessions\skills-plugin"
if (-not (Test-Path $claudeBase)) {
    Write-Error "Claude AppData skills-plugin nao encontrado."
    exit 1
}

# Encontra UUID dirs (geralmente 1)
$uuidDirs = Get-ChildItem $claudeBase -Directory
if ($uuidDirs.Count -eq 0) {
    Write-Error "Nenhum UUID dir em skills-plugin. Claude Code nao foi inicializado?"
    exit 1
}

# Built-ins puras (NAO sao junction, preservar)
$builtins = @('consolidate-memory','setup-cowork','pdf','docx','pptx','xlsx')

$totalCreated = 0
$totalSkipped = 0
$totalRemoved = 0

foreach ($uuidDir in $uuidDirs) {
    $subDirs = Get-ChildItem $uuidDir.FullName -Directory
    foreach ($subDir in $subDirs) {
        $AD = Join-Path $subDir.FullName "skills"
        if (-not (Test-Path $AD)) { continue }
        Write-Host "Sync target: $AD" -ForegroundColor Cyan

        # 1. Cria junction pra cada skill em skillforge
        $sfSkills = (Get-ChildItem $SF -Directory).Name | Sort-Object
        foreach ($s in $sfSkills) {
            $jPath = Join-Path $AD $s
            $needCreate = $true
            if (Test-Path $jPath) {
                $item = Get-Item $jPath -Force
                if ($item.LinkType -eq 'Junction' -and $item.Target[0] -eq (Join-Path $SF $s)) {
                    $totalSkipped++
                    $needCreate = $false
                } else {
                    Remove-Item $jPath -Recurse -Force
                }
            }
            if ($needCreate) {
                New-Item -ItemType Junction -Path $jPath -Target (Join-Path $SF $s) | Out-Null
                $totalCreated++
            }
        }

        # 2. Remove zumbis (existe em AppData mas nao em skillforge nem em builtins)
        $adDirs = Get-ChildItem $AD -Directory | ForEach-Object { $_.Name }
        foreach ($d in $adDirs) {
            if ($sfSkills -notcontains $d -and $builtins -notcontains $d) {
                $delPath = Join-Path $AD $d
                Remove-Item $delPath -Recurse -Force
                Write-Host "  Removed zombie: $d" -ForegroundColor Yellow
                $totalRemoved++
            }
        }
    }
}

Write-Host ""
Write-Host "=== SUMMARY ===" -ForegroundColor Green
Write-Host "  Junctions created: $totalCreated"
Write-Host "  Junctions valid (skipped): $totalSkipped"
Write-Host "  Zombies removed: $totalRemoved"
Write-Host ""
Write-Host "Restart Claude Code se mudou skills (sessao atual cacheia metadata)" -ForegroundColor Cyan
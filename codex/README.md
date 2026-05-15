# Codex Runtime

Camada de runtime para usar o SkillForge Arsenal no Codex.

## Setup

```powershell
powershell -ExecutionPolicy Bypass -File codex/scripts/setup-codex-runtime.ps1
```

Isso cria junctions para:

- `~/.codex/skills/<skill>` -> `skillforge-arsenal/skills/<skill>`
- `~/.codex/rules` -> `skillforge-arsenal/codex/rules`
- `~/.codex/scripts` -> `skillforge-arsenal/codex/scripts`
- `~/.codex/library` -> `~/.claude/library`
- `~/.codex/context-tree` -> `~/.claude/context-tree`

`~/.codex/AGENTS.md` recebe uma copia do bootstrap `codex/AGENTS.md`.

Reinicie o Codex depois do setup para recarregar metadata das skills.

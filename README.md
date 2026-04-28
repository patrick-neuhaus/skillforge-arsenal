# skillforge-arsenal

Ecossistema de skills, agents, hooks e knowledge persistente pra Claude Code.

**42 skills + 5 agents proprios + 13 IRON LAWs + library compartilhada + maestro V2 orquestrador + memoria long-term cross-session.**

## Estrutura

```
skillforge-arsenal/
├── skills/                    ← 42 skills versionadas (source of truth)
├── dist/                      ← zips gerados pelo zip-skills.py
├── scripts/
│   ├── setup-junctions.ps1    ← bulk junction sync skillforge -> Claude AppData
│   └── semantic-triggers/     ← parser context-tree (Onda alpha)
├── internal-docs/             ← gitignored (waves narratives, sanity tests)
├── FIXES-APLICADOS.md         ← lock-in IL-10 tracker
└── HOW-TO-USE.md              ← guia uso
```

## Quick start

### 1. Clone + setup junctions

```bash
git clone https://github.com/patrick-neuhaus/skillforge-arsenal
cd skillforge-arsenal
powershell -ExecutionPolicy Bypass -File scripts/setup-junctions.ps1
```

Junctions criadas em `AppData\Claude\...\skills-plugin\<UUID>\skills\` apontando pro skillforge. **Edits no skillforge refletem instantaneo no Claude Code.** Zero zip upload manual.

### 2. Editar skill

```bash
# Edita SKILL.md em skills/<nome>/
vim skills/maestro/SKILL.md

# IL-1 hook V2 valida antes do Write (rubric prompt-engineer score >=80)
# Junction reflete edit imediato em AppData
# Restart Claude Code se mudar metadata frontmatter
```

### 3. Skill nova

```bash
# Cria pasta + SKILL.md em skills/<nova>/
# Hook PostToolUse Write auto-cria junction em AppData
```

## Ecossistema

### Skills (42)

Categorias principais:
- **Meta/Orchestration:** maestro V2, prompt-engineer, skill-builder, geo-optimizer, reference-finder, context-guardian, context-tree
- **Code review:** trident (com modos `--mode`, `--design`, `--skill`, `--dedup`), security-audit, architecture-guard
- **Implementation:** sdd, react-patterns, component-architect, supabase-db-architect, n8n-architect, lovable-router
- **Design:** ui-design-system, ux-audit, design-system-audit, product-discovery-prd, test-lab-architect
- **Marketing:** copy, ai-seo, seo, site-architecture, competitor-alternatives, sales-enablement, free-tool-strategy, launch-strategy, product-marketing-context
- **Knowledge:** lovable-knowledge, pattern-importer
- **Content:** pdf, docx, pptx, xlsx
- **Infra:** vps-infra-audit
- **People:** comunicacao-clientes, tech-lead-pm, meeting-sync
- **Workflow:** schedule, cli-skill-wrapper

### Agents proprios (5)

Em `~/.claude/agents/`:
- `executor` (Sonnet) — skillforge-aware code executor
- `planner-skill` (Opus) — SDD-aware planner
- `verifier-skill` (Sonnet) — IL-1/IL-4 compliance check
- `lovable-implementer` (Sonnet) — executa output lovable-router
- `n8n-fixer` (Sonnet) — debug n8n workflows

### Library compartilhada

Em `~/.claude/library/`:
- `rubrics/` — promptfoo (claude-md, system-prompt, iron-laws, technical-plan, agents-md, geo)
- `severity/` — checklists P0-P3 (security, SOLID, code quality)
- `templates/` — skill templates

### Memory long-term

Em `~/.claude/context-tree/`:
- `decisoes/` — decisoes arquiteturais
- `clientes/` — knowledge por cliente
- `projetos/` — knowledge por projeto
- `knowledge/` — generico/tecnico
- `plans/` — 43 plans indexados + auto-capture forward
- `sessions/` — PreCompact snapshots + ExitPlanMode markers
- `erros/` — erros do Claude + duvidas

Auto-populated por hooks (Wave 5).

### Hooks (8)

Em `~/.claude/hooks/`:
- PreToolUse Write/Edit: V2 hash marker (IL-1 enforcement)
- Stop: token tracker + error-doubt-tracker (5 categorias auto)
- SessionStart: bootstrap inventory ecossistema
- PostToolUse Write: plan-capture + skill-junction-sync
- PostToolUse ExitPlanMode: log approvals
- PreCompact: snapshot recovery

### IRON LAWs (13)

User-level em `~/.claude/rules/iron-laws.md`:
1. Edit instrucao = prompt-engineer --validate
2. Code review = trident
3. Skills locais > built-ins
4. Skill nova/estrutural = skill-builder --validate
5. Composicao 2+ entries = maestro V2
6. Hook bloqueia = pausa real
7. Skill nova = skill-builder Step 0 (8 perguntas)
8. Problema novo = reference-finder --solution-scout
9. Task Hygor/Jonas = vocal confrontation
10. FIXES-APLICADOS validated:* = lock-in
11. Componentes em library/
12. Maestro V2 query context-tree em Phase 0.1
13. Skillforge fonte de verdade, AppData = junctions

## Plugins (OMC + Caveman)

```bash
claude plugin install caveman@caveman                      # Token compression
claude plugin install oh-my-claudecode@omc                 # 19 agents + 39 skills + workflows
```

OMC workflows aproveitados: autopilot, ralph, team, deep-interview, ultrawork, ccg, deepinit, caveman.
OMC agents aproveitados: executor, planner, verifier, critic, explore, architect.
Maestro V2 prioriza skillforge sobre OMC.

## Roadmap (waves)

- **Waves A-C** (Apr 14-18): triggering reliability 39% -> 95%, lock-in IL-10
- **Wave G** (Apr 11): V2 hook hard block
- **Wave 1** (Apr 29): hygiene, trim 7 descriptions, trident absorveu code-dedup-scanner
- **Wave 2** (Apr 29): library/ compartilhada (rubrics + severity + templates), IL-11
- **Wave 3** (Apr 29): maestro V2 + 5 agents proprios + 2 hooks + state mgmt + OMC hibrido, IL-5 estendida
- **Wave 4** (Apr 29): closure, repo cleanup, CLAUDE.md enxutos, IL-10 estendida
- **Wave 5** (Apr 29): long-term memory, context-tree refactor por dominio, 3 hooks novos, parser retroativo (43 plans + 61 sessions), IL-12
- **Wave 6** (Apr 29): junction sync skillforge -> AppData, IL-13. Diagnostico critico: edits Wave 1-5 nao chegaram no front antes (descoberto pos-Wave 5)

## Stack

Claude Code (Sonnet medium / Opus high) + Lovable + Supabase + n8n + ClickUp.

## Licenca

Pessoal. Patrick Neuhaus.
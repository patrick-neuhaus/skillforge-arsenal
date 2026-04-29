---
name: schedule
description: "Create, manage, and optimize scheduled tasks and recurring automations for Claude Code. Build reusable shortcuts from sessions, configure cron schedules, plan one-time reminders, and organize automated workflows. Use when user asks to: schedule task, create reminder, 'agendar tarefa', automate recurring, 'rodar isso todo dia', cron job, 'me lembra de', 'automatizar isso', scheduled task, recurring task, 'quero que rode sozinho', set up automation, 'criar rotina', plan recurring, 'toda segunda fazer X', timer, 'daqui a 5 minutos', run on interval. NÃO use pra automações n8n (use n8n-architect) nem pra tarefas manuais do ClickUp (use tech-lead-pm)."
---

# Schedule — Tarefas Agendadas

IRON LAW: NEVER create a scheduled task without a self-contained description. Future runs have NO access to the current session — if the prompt references "the above" or "this conversation", it WILL fail silently.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--create` | Create new scheduled task from current session | default |
| `--recurring` | Create with cron schedule (daily, weekly, etc.) | - |
| `--once` | One-time task with specific datetime | - |
| `--list` | List existing scheduled tasks | - |

## Workflow

```
Schedule Progress:

- [ ] Step 1: Identify Task ⚠️ REQUIRED
  - [ ] 1.1 Review session — what did the user do/request?
  - [ ] 1.2 Distill into single repeatable objective
  - [ ] 1.3 Ask: "Isso precisa rodar recorrente, uma vez, ou manual?"
- [ ] Step 2: Draft Prompt ⚠️ REQUIRED
  - [ ] 2.1 Write self-contained description (IRON LAW)
  - [ ] 2.2 Include: objective, steps, file paths, URLs, success criteria
  - [ ] 2.3 Write in imperative ("Check the inbox...", "Run tests...")
  - [ ] ⛔ GATE: Present prompt to user for review
- [ ] Step 3: Configure Schedule
  - [ ] 3.1 Determine type: recurring (cron) / one-time (fireAt) / ad-hoc
  - [ ] 3.2 Choose taskName (kebab-case, descriptive)
  - [ ] 3.3 If cron: use LOCAL timezone, not UTC
  - [ ] 3.4 If one-time: compute ISO 8601 with timezone offset
- [ ] Step 4: Create ⛔ BLOCKING
  - [ ] ⛔ GATE: Confirm schedule with user before creating
  - [ ] 4.1 Call create_scheduled_task tool
```

## Step 1: Identify Task

Review the session history and extract:
- **What** the user did or wants automated
- **Why** it should be recurring (saves time? prevents forgetting?)
- **When** it should run (frequency, time of day, timezone)

Ask: "O que exatamente quer agendar? Com que frequência?"

## Step 2: Draft Prompt

The prompt is the ENTIRE context for future runs. It must be:

1. **Self-contained** — no references to "this conversation" or "the above"
2. **Specific** — exact file paths, URLs, repo names, tool names
3. **Imperative** — "Check inbox", "Run test suite", "Generate report"
4. **Complete** — success criteria, constraints, expected output
5. **Concise** — no unnecessary context, just what's needed to execute

### Template

```
Objective: [what to accomplish]

Steps:
1. [specific action with file paths/URLs]
2. [specific action]
3. [specific action]

Success criteria: [how to know it worked]
Constraints: [any limits or preferences]
```

⛔ **GATE:** Present the draft prompt. User must approve before proceeding.

## Step 3: Configure Schedule

| Type | When to use | Config |
|------|------------|--------|
| **Recurring** | "todo dia", "toda segunda", "a cada hora" | `cronExpression` (LOCAL timezone) |
| **One-time** | "daqui a 5 min", "amanhã às 15h" | `fireAt` ISO 8601 with offset |
| **Ad-hoc** | "quando eu pedir" | Omit both — manual trigger |

### Cron Rules
- **LOCAL timezone** — "8am toda sexta" = `0 8 * * 5`
- **Never use cron for one-time tasks** — use `fireAt` instead
- Common patterns: `0 9 * * 1-5` (weekdays 9am), `0 */2 * * *` (every 2h), `0 8 * * 1` (Monday 8am)

### TaskName
kebab-case, descriptive: `daily-inbox-summary`, `weekly-dep-audit`, `format-pr-description`

## Step 4: Create

⛔ **GATE:** Confirm with user:
```
Tarefa: [taskName]
Prompt: [resumo do que faz]
Schedule: [cron ou fireAt ou manual]
Confirma?
```

Then call `create_scheduled_task` tool.

## Anti-Patterns

- **Prompt que referencia a conversa atual** — futuras execuções não têm esse contexto. IRON LAW.
- **Cron pra tarefa única** — use `fireAt`. Cron não tem semântica de one-shot.
- **Schedule sem timezone** — `fireAt` DEVE ter offset. Cron usa timezone local.
- **Tarefa complexa demais** — se precisa de 10+ steps, provavelmente é um workflow n8n, não um schedule.
- **Sem critério de sucesso** — "rode o script" sem saber se deu certo é inútil.

## Pre-Delivery Checklist

- [ ] Prompt é self-contained (sem referências à sessão atual)
- [ ] Tem objetivo claro e steps específicos
- [ ] File paths e URLs são absolutos (não relativos)
- [ ] Schedule type correto (cron/fireAt/ad-hoc)
- [ ] Timezone considerado
- [ ] taskName é descritivo e kebab-case
- [ ] Usuário aprovou antes de criar

## When NOT to use

- Automações complexas multi-step → use **n8n-architect**
- Gestão de tarefas da equipe → use **tech-lead-pm**
- Reminders no ClickUp → use ClickUp direto
- Cron jobs no servidor → configure via SSH, não via Claude schedule

## Integration

- **tech-lead-pm** — schedules de gestão (daily report, weekly review)
- **n8n-architect** — se a automação é complexa demais pra schedule, migre pra n8n
- **maestro** — maestro pode sugerir schedule quando o usuário descreve tarefa recorrente

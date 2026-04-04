---
name: maestro
description: "Analyze user intent and route to the right skill or skill chain. Plan multi-skill pipelines, check skill availability, organize workflow sequences, and review context window budget. Use when user asks: 'o que posso fazer?', 'qual skill usar?', 'que skills tenho?', which skill, help me choose, list skills, 'me ajuda a decidir', plan skill chain, orchestrate pipeline, 'quero fazer X mas não sei por onde começar', 'preciso de ajuda com', route skills, which tool should I use, help me pick a skill, what can you do, validate skill choice, list available skills. Auto-activates when multiple skills could apply to a request."
---

# Maestro — Skill Orchestrator

IRON LAW: NEVER recommend a skill without reading its SKILL.md first — descriptions can be stale, the source of truth is the file itself.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--suggest` | Recommend best skill(s) for user's intent | default |
| `--chain` | Build multi-skill pipeline with execution order | - |
| `--catalog` | List all skills grouped by category | - |
| `--health` | Check arsenal health (missing refs, broken links) | - |
| `--loose` | Loose orchestration: give sub-agent CLI access, let it compose workflow emergently | - |

## Workflow

```
Maestro Progress:

- [ ] Phase 1: Understand Intent ⚠️ REQUIRED
  - [ ] 1.1 Parse user request for domain keywords
  - [ ] 1.2 Identify primary need (build, review, audit, find, plan, create)
  - [ ] 1.3 Check if request crosses multiple domains
- [ ] Phase 2: Route
  - [ ] Load references/skill-catalog.md
  - [ ] 2.1 Match intent to skill(s) by triggers
  - [ ] 2.2 If single skill → suggest with rationale
  - [ ] 2.3 If multi-skill → build chain (load references/composition-chains.md)
- [ ] Phase 3: Present ⛔ BLOCKING
  - [ ] 3.1 Show recommended skill(s) with one-line rationale
  - [ ] 3.2 If chain: show execution order + context window budget
  - [ ] ⛔ GATE: User confirms before invoking any skill
```

## Phase 1: Understand Intent

Parse the request for:
1. **Action verb** — build, review, audit, find, plan, create, fix, improve, organize
2. **Domain** — code, design, infra, knowledge, product, security, automation, docs
3. **Scope** — single file, feature, project-wide, cross-project

Map to categories:
| Intent Pattern | Category | Primary Skills |
|---------------|----------|----------------|
| "build/implement/create feature" | Implementation | sdd, react-patterns, component-architect |
| "review/audit code" | Code Review | trident, react-patterns |
| "find bugs/security issues" | Code Review | trident, security-audit |
| "validate architecture/thin client" | Guard | architecture-guard, trident |
| "find duplicates/reusables" | Guard | code-dedup-scanner |
| "context window/clear/handoff" | Guard | context-guardian |
| "design system/tokens/UI" | Design | ui-design-system, component-architect |
| "find references/books/frameworks" | Knowledge | reference-finder, context-tree |
| "create/improve skill" | Meta | skill-builder, prompt-engineer |
| "optimize description/GEO" | Optimization | geo-optimizer |
| "wrap API/create CLI tool" | Optimization | cli-skill-wrapper |
| "import pattern/.tmp" | Workflow | pattern-importer, sdd |
| "plan/spec/research" | Workflow | sdd |
| "audit infra/VPS" | Infra | vps-infra-audit |
| "audit UX/UI" | Design | ux-audit |
| "database/schema/RLS" | Implementation | supabase-db-architect |
| "automation/n8n/workflow" | Implementation | n8n-architect |
| "document/export" | Content | pdf, docx, pptx, xlsx |
| "communicate/client message" | People | comunicacao-clientes |
| "manage project/team" | People | tech-lead-pm |
| "organize knowledge" | Meta | context-tree |

## Phase 2: Route

### Single Skill
If one skill clearly matches, present:
```
**Recomendação:** [skill-name]
**Por quê:** [1 frase conectando o intent do usuário à capacidade da skill]
**Como usar:** [comando ou flag mais relevante]
```

### Multi-Skill Chain
If the request crosses domains, load `references/composition-chains.md` and present:
```
**Pipeline recomendado:**
1. [skill-1] — [o que faz neste contexto] (~X% context window)
2. [skill-2] — [o que faz neste contexto] (~X% context window)
   └─ /clear entre fases se necessário
3. [skill-3] — [o que faz neste contexto] (~X% context window)

**Handoff:** [skill-1] gera [documento], que [skill-2] consome.
```

### Context Window Budget
- Cada skill consome ~20-40% da context window
- Se chain tem 3+ skills → recomendar `/clear` entre fases
- SDD é especialmente pesada (4 fases internas)

## Phase 3: Present

⛔ **GATE:** Sempre confirmar antes de invocar. Nunca assumir que a sugestão está certa — o usuário pode ter contexto que muda a recomendação.

### --catalog Output

```markdown
## Arsenal de Skills (30 skills)

### Code Review
- **trident** — Pipeline 3 agentes: Scan→Verify→Judge
- **react-patterns** — Audit de padrões React/Next.js
- **security-audit** — Auditoria de segurança OWASP

### Guard
- **architecture-guard** — Lint de arquitetura (thin client, layer separation)
- **code-dedup-scanner** — Encontrar reutilizáveis antes de criar novo
- **context-guardian** — Monitor de context window + handoff pra /clear

### Optimization
- **geo-optimizer** — Otimizar descriptions pra GEO (descoberta por agentes)
- **cli-skill-wrapper** — Transformar API em CLI tool + gerar skill

### Implementation
- **sdd** — Spec Driven Development (Research→Spec→Implement→Review)
- **component-architect** — Arquitetura de componentes, atomic design
- **supabase-db-architect** — Schema PostgreSQL/Supabase
- **n8n-architect** — Automações n8n

### Design
- **ui-design-system** — Design tokens e design.json
- **ux-audit** — Auditoria de UX/UI
- **product-discovery-prd** — Discovery e PRD

### Knowledge
- **reference-finder** — Referências fundamentais por tema
- **prompt-engineer** — Criar e otimizar prompts
- **lovable-knowledge** — Knowledge pro Lovable

### Meta
- **skill-builder** — Criar e melhorar skills
- **context-tree** — Gestão de conhecimento com scoring

### Content
- **pdf** / **docx** / **pptx** / **xlsx** — Manipulação de documentos

### Infra
- **vps-infra-audit** — Auditoria de VPS

### People
- **tech-lead-pm** — Gestão e liderança técnica
- **comunicacao-clientes** — Comunicação via WhatsApp/Telegram

### Workflow
- **schedule** — Tarefas agendadas
- **pattern-importer** — Técnica .tmp: importar padrões de repos externos
```

## Anti-Patterns

- **Routing sem ler SKILL.md** — descriptions ficam desatualizadas. Sempre ler o arquivo.
- **Chain longa demais** — >3 skills numa chain sem /clear = context window esgotada
- **Forçar skill** — se nenhuma skill encaixa, diga isso. Nem tudo precisa de skill.
- **Ignorar --mode/--flags** — cada skill tem parâmetros que mudam o comportamento drasticamente
- **Routing circular** — maestro recomenda skill-builder que recomenda maestro. Evite loops.
- **Over-orchestration** — tarefa simples não precisa de chain. Uma skill basta.

## Pre-Delivery Checklist

Antes de recomendar:
- [ ] Li o SKILL.md da skill recomendada (não só description)
- [ ] A skill resolve o problema real do usuário (não o problema que parece)
- [ ] Se chain: ordem de execução faz sentido e handoffs estão claros
- [ ] Context window budget calculado (~20-40% por skill)
- [ ] Alternativas mencionadas se houver ambiguidade

## When NOT to use

- Usuário já sabe qual skill quer → invocar direto
- Tarefa trivial que não precisa de skill → responder direto
- Pergunta sobre como usar uma skill específica → ler o SKILL.md da skill

## Integration

- **Todas as skills** — maestro é o ponto de entrada para o ecossistema
- **skill-builder** — quando nenhuma skill existente atende, sugere criar uma nova
- **context-tree** — pode consultar tree para entender domínio antes de rotear

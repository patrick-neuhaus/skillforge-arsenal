---
name: maestro
description: "Analyze user intent and route to the right skill or skill chain. Plan multi-skill pipelines, check skill availability, organize workflow sequences, and review context window budget. Use when user asks: 'o que posso fazer?', 'qual skill usar?', 'que skills tenho?', which skill, help me choose, list skills, 'me ajuda a decidir', plan skill chain, orchestrate pipeline, 'quero fazer X mas não sei por onde começar', 'preciso de ajuda com', route skills, which tool should I use, help me pick a skill, what can you do, validate skill choice, list available skills. Auto-activates when multiple skills could apply to a request AND the request is non-trivial (see 'When NOT to use')."
---

# Maestro — Skill Orchestrator

IRON LAW: NEVER recommend a skill without reading its SKILL.md first — descriptions can be stale, the source of truth is the file itself.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--suggest` | Recommend best skill(s) for user's intent | default |
| `--chain` | Build multi-skill pipeline with execution order | - |
| `--catalog` | List all skills grouped by category | - |
| `--health` | Scan `skills/` dir, validate SKILL.md presence + references freshness + catalog sync | - |
| `--loose` | Loose orchestration with bounding box (max 3 skills, human confirm required, no auto-invoke) | - |

## Workflow

```
Maestro Progress:

- [ ] Phase 1: Understand Intent ⚠️ REQUIRED
  - [ ] 1.1 Parse user request for domain keywords
  - [ ] 1.2 Identify primary need (build, review, audit, find, plan, create)
  - [ ] 1.3 Check if request crosses multiple domains
- [ ] Phase 2: Route
  - [ ] 2.0 Check skill-catalog.md mtime — if >7 days old, warn stale + fall back to reading individual SKILL.mds directly (IRON LAW)
  - [ ] 2.1 Match intent to candidate skill(s) by triggers (Phase 1 table)
  - [ ] 2.2 ⚠️ IRON LAW: Read SKILL.md of each candidate BEFORE proposing — descriptions are stale, file is source of truth
  - [ ] 2.3 If single skill → prepare suggestion with rationale
  - [ ] 2.4 If multi-skill → build chain (load references/composition-chains.md)
  - [ ] 2.5 If >1 candidate with similar score → surface alternatives before primary (see Phase 3 output)
- [ ] Phase 3: Present ⛔ BLOCKING
  - [ ] 3.1 Show recommended skill(s) with one-line rationale
  - [ ] 3.2 If chain: show execution order + context window budget + /clear handoff points (via context-guardian)
  - [ ] 3.3 If alternatives exist: list primary + alternatives with distinguishing criteria
  - [ ] ⛔ GATE: Maestro stops here. Recommend + await user confirmation. The user's next message triggers skill invocation directly — maestro does NOT invoke on behalf of the user.
```

## Phase 1: Understand Intent

Parse the request for:
1. **Action verb** — build, review, audit, find, plan, create, fix, improve, organize
2. **Domain** — code, design, infra, knowledge, product, security, automation, docs, marketing
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
| "validate skill choice/which skill/help me pick" | Meta | maestro (--suggest) |
| "optimize description/GEO" | Optimization | geo-optimizer |
| "wrap API/create CLI tool" | Optimization | cli-skill-wrapper |
| "import pattern/.tmp" | Workflow | pattern-importer, sdd |
| "plan/spec/research" | Workflow | sdd |
| "discovery/PRD/user story/validar ideia" | Design | product-discovery-prd |
| "audit infra/VPS" | Infra | vps-infra-audit |
| "SEO/keyword/rankear/programático/semântico" | Design | seo |
| "audit UX/UI" | Design | ux-audit |
| "editar projeto lovable/mexer no banco do lovable" | Implementation | lovable-router |
| "database/schema/RLS" | Implementation | supabase-db-architect |
| "automation/n8n/workflow" | Implementation | n8n-architect |
| "document/export" | Content | pdf, docx, pptx, xlsx |
| "communicate/client message" | People | comunicacao-clientes |
| "manage project/team" | People | tech-lead-pm |
| "organize knowledge" | Meta | context-tree |
| "copy/copywriting/headline/landing page text/email sequence/ad copy" | Marketing | copy |
| "product positioning/ICP/marketing context/target audience/ideal customer" | Marketing | product-marketing-context |
| "AI SEO/GEO/AEO/AI Overviews/otimizar para IA/aparecer no ChatGPT/Perplexity" | Marketing | ai-seo |
| "site architecture/page hierarchy/sitemap/IA/navegação/URL structure" | Marketing | site-architecture |
| "competitor page/vs page/alternative page/comparação/battle card" | Marketing | competitor-alternatives |
| "sales collateral/pitch deck/one-pager/objection handling/demo script" | Marketing | sales-enablement |
| "free tool/engineering as marketing/lead gen tool/calculator/grader" | Marketing | free-tool-strategy |
| "launch/GTM/Product Hunt/go-to-market/feature release/waitlist" | Marketing | launch-strategy |

## Phase 2: Route

### Step 2.0: Staleness check
Before matching, check `mtime` of `references/skill-catalog.md`. If older than 7 days, emit warning:
> ⚠️ skill-catalog.md is stale (>7d). Falling back to reading individual SKILL.mds per IRON LAW.

Then skip the catalog and read the SKILL.md files directly for candidate skills.

### Step 2.2: Read SKILL.md (IRON LAW enforcement)
For every candidate skill identified in 2.1, read the actual `skills/<name>/SKILL.md` file before proposing. Do not rely on description frontmatter alone — the YAML description may diverge from current behavior after refactors. This step is mandatory, not optional.

### Step 2.3: Single Skill
If one skill clearly matches, present:
```
**Recomendação:** [skill-name]
**Por quê:** [1 frase conectando o intent do usuário à capacidade da skill]
**Como usar:** [comando ou flag mais relevante]
```

### Step 2.4: Multi-Skill Chain
If the request crosses domains, load `references/composition-chains.md` and present:
```
**Pipeline recomendado:**
1. [skill-1] — [o que faz neste contexto] (~X% context window)
2. [skill-2] — [o que faz neste contexto] (~X% context window)
   └─ context-guardian --handoff antes de /clear (se budget >70%)
3. [skill-3] — [o que faz neste contexto] (~X% context window)

**Handoff:** [skill-1] gera [documento], que [skill-2] consome.
```

### Step 2.5: Alternatives (conditional)
If 2+ candidates score similarly (within ~15% match delta), include an `**Alternativas:**` block BEFORE the primary recommendation so the user can choose:
```
**Alternativas consideradas:**
- [skill-a] — better for [criterion X]
- [skill-b] — better for [criterion Y]

**Primário:** [skill-a] — [rationale]
```

### Context Window Budget (per-skill table)

Replace the old "20-40% flat" heuristic with category-based estimates sourced from `references/composition-chains.md`:

| Skill class | Est. context usage | Notes |
|-------------|---------------------|-------|
| sdd (4 internal phases) | ~35-45% | Heaviest — research+spec+impl+review |
| trident (3-agent pipeline) | ~25-35% | Scanner + Verifier + Arbiter |
| security-audit / vps-infra-audit | ~25-30% | Multi-lens scan |
| Typical implementation skill (react-patterns, n8n-architect, etc.) | ~15-20% | Single-pass reasoning |
| Reference lookup (reference-finder, context-tree) | ~10-15% | Load + match |
| Meta skills (skill-builder, prompt-engineer, maestro) | ~10-20% | Small scope, high reasoning density |
| Content (pdf, docx, pptx, xlsx) | ~5-10% | Utility-class |

**Chain rule:** if projected cumulative budget exceeds 70%, insert `context-guardian --handoff` before `/clear` between phases. Do not just recommend `/clear` — handoff preserves state.

## Phase 3: Present

⛔ **GATE clarification:** Maestro **recommends + awaits user confirmation**. It does NOT invoke the recommended skill. After the user confirms, their next message triggers direct invocation of the skill — maestro exits the loop at the recommendation step.

This separation exists because:
1. User may have hidden context that changes the recommendation
2. Prevents circular routing (maestro → maestro)
3. Keeps responsibility clear — maestro = router, skill = executor

### --catalog Output

```markdown
## Arsenal de Skills (40 skills)

> Last-verified source of truth: `skills/` directory listing. If skill-catalog.md is >7d old, re-scan directly.

### Meta / Orchestration
- **maestro** — Skill orchestrator (this file). Routes intent → skill(s) + plans chains
- **skill-builder** — Create and improve skills
- **prompt-engineer** — Create and optimize prompts with rubric-based validation
- **context-tree** — Knowledge management with scoring

### Code Review
- **trident** — Pipeline 3 agents: Scanner → Verifier → Arbiter (use this, not `simplify`)
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
- **sdd** — Spec Driven Development (Research → Spec → Implement → Review)
- **component-architect** — Arquitetura de componentes, atomic design
- **supabase-db-architect** — Schema PostgreSQL/Supabase
- **n8n-architect** — Automações n8n
- **lovable-router** — Roteamento de mudanças em projetos Lovable (código vs prompt)
- **lovable-knowledge** — Knowledge pro Lovable

### Design / Discovery
- **ui-design-system** — Design tokens e design.json
- **ux-audit** — Auditoria de UX/UI
- **product-discovery-prd** — Discovery, PRD, user stories, validação de ideia
- **seo** — SEO completo (audit, keyword, content, programmatic, semantic)

### Knowledge
- **reference-finder** — Referências fundamentais + `--solution-scout` mode
- **pattern-importer** — Técnica .tmp: importar padrões de repos externos

### Content
- **pdf** / **docx** / **pptx** / **xlsx** — Manipulação de documentos

### Infra
- **vps-infra-audit** — Auditoria de VPS

### People
- **tech-lead-pm** — Gestão e liderança técnica
- **comunicacao-clientes** — Comunicação via WhatsApp/Telegram

### Workflow
- **schedule** — Tarefas agendadas

### Marketing
- **copy** — Copywriting para qualquer canal (landing, social, email, ads, UX)
- **product-marketing-context** — Posicionamento/ICP que todas as skills de marketing referenciam
- **ai-seo** — Otimização para IA (GEO/AEO): AI Overviews, ChatGPT, Perplexity
- **site-architecture** — Hierarquia de páginas, navegação, URLs, IA
- **competitor-alternatives** — Páginas de comparação e alternativas
- **sales-enablement** — Pitch deck, one-pager, objection handling, demo script
- **free-tool-strategy** — Ferramentas gratuitas para lead gen e SEO
- **launch-strategy** — GTM, Product Hunt, feature release, waitlist

**Total: 40 skills** (auto-verify with `ls skills/ | wc -l`)
```

### --health Workflow

Runs diagnostics on the arsenal and reports drift between catalog and filesystem:

```
--health pipeline:
  1. Scan skills/ directory → get actual list
  2. Parse references/skill-catalog.md → get catalog list
  3. Diff:
     - Missing from catalog (in fs, not in doc) → add to catalog
     - Missing from fs (in doc, not in fs) → remove from catalog OR restore skill
     - maestro missing from own catalog → fix (BUG-1 regression check)
  4. For each skill:
     - Validate SKILL.md exists + YAML frontmatter has name + description
     - Check references/ dir exists if referenced in workflow
  5. Check skill-catalog.md mtime → warn if >7 days
  6. Output structured report: ✅ healthy | ⚠️ warnings | 🔴 broken
```

### --loose Workflow (bounded)

Loose orchestration gives the user emergent composition across skills, with explicit bounding box to prevent runaway chains:

```
--loose constraints:
  - Max 3 skills in scope
  - Human confirmation required before each skill invocation
  - NO auto-invoke — maestro always stops at Phase 3 GATE regardless of --loose
  - References references/composition-chains.md as the bounding structure
  - If user asks for >3 skills, reject with: "Split into waves, run maestro --loose per wave"
```

## Anti-Patterns

- **Routing sem ler SKILL.md** — descriptions ficam desatualizadas. Sempre ler o arquivo na Phase 2.2 (IRON LAW).
- **Chain longa demais** — >3 skills numa chain sem context-guardian handoff = context window esgotada
- **/clear sem handoff** — usar `context-guardian --handoff` antes de `/clear` pra preservar estado
- **Forçar skill** — se nenhuma skill encaixa, diga isso. Nem tudo precisa de skill.
- **Ignorar --mode/--flags** — cada skill tem parâmetros que mudam o comportamento drasticamente
- **Routing circular** — maestro recomenda skill-builder que recomenda maestro. Detectar via trace + abortar.
- **Over-orchestration** — tarefa simples não precisa de chain. Uma skill basta. Ver "When NOT to use".
- **Maestro invocando skills** — maestro só recomenda. A invocação acontece depois que o usuário confirma, no turno seguinte.

## Pre-Delivery Checklist

Antes de recomendar:
- [ ] Li o SKILL.md da skill recomendada (enforcement já em Phase 2.2)
- [ ] A skill resolve o problema real do usuário (não o problema que parece)
- [ ] Se chain: ordem de execução faz sentido e handoffs estão claros
- [ ] Context window budget calculado via tabela per-skill (ver Phase 2)
- [ ] Alternativas mencionadas se Phase 2.5 encontrou 2+ candidatos similares

## When NOT to use

- Usuário já sabe qual skill quer → invocar direto
- Tarefa trivial que não precisa de skill → responder direto
- Pergunta sobre como usar uma skill específica → ler o SKILL.md da skill
- **Tiebreaker auto-activation:** auto-activation applies only when the request is non-trivial AND no single skill is obvious. Trivial tasks skip maestro entirely, even if the router detects 2+ candidates.

## Integration

- **Todas as skills** — maestro é o ponto de entrada para o ecossistema
- **skill-builder** — quando nenhuma skill existente atende, sugere criar uma nova
- **context-tree** — pode consultar tree para entender domínio antes de rotear
- **context-guardian** — usar `--handoff` antes de `/clear` em chains longas

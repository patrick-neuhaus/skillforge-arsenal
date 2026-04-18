---
name: prompt-engineer
description: "Skill para criar, validar e otimizar prompts e contextos para qualquer LLM (Claude, Gemini, GPT). Validação v3 usa promptfoo + ccinspect + rubrics por tipo (claude-md, technical-plan, iron-laws, system-prompt). Use esta skill SEMPRE que o usuário mencionar: prompt, system prompt, validar CLAUDE.md, validar plano técnico, validar IRON LAWS, context engineering, agente, chatbot, JSON Schema pra IA, 'como faço o modelo retornar X', 'o modelo tá respondendo errado', 'preciso melhorar esse prompt', 'quero criar um agente', 'instrução pro Lovable/Cursor', AGENTS.md. Também use ao criar/editar prompts em n8n nodes, agentes WhatsApp. Se o usuário disser 'valida esse prompt', 'valida CLAUDE.md', 'valida plano', 'score do prompt', USE esta skill. Also triggers on: 'escrever instruções pro Claude', 'montar CLAUDE.md do projeto', write a prompt for, score this prompt, validate prompt rubric. NÃO use pra editar texto DENTRO de SKILL.md (use skill-builder --validate). Prompt simples de uma linha, responda direto."
---

# Prompt & Context Engineer v3

**Role:** craft, validate, and optimize prompts + contexts for any LLM (Claude, Gemini, GPT). Covers system prompts, agent instructions, CLAUDE.md files, JSON schemas, extraction prompts, and technical plan validation.

**Context:** the prompt is one component — tools, docs, examples, history all compete for attention in the context window. This skill treats the full context as the unit of work, not just the text between XML tags.

**Iron Law:** Never output a prompt without explaining why each section exists. A prompt the user doesn't understand is a prompt they can't maintain or improve.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--create` | Create a new prompt from scratch | true |
| `--validate` | Validate existing prompt via promptfoo + ccinspect rubric | false |
| `--type <t>` | Prompt type: claude-md, technical-plan, iron-laws, system-prompt, extraction, json-schema, agents-md, geo (auto-detect if omitted) | auto-detect |
| `--geo` | Optimize text/description for agent discovery (GEO) | false |
| `--update-rubric --gap <file>` | Promote a documented gap into the rubric (semi-auto, asks approval) | false |

## Workflow

```
Prompt Engineer Progress:

- [ ] Step 1: Identify & Context ⚠️ REQUIRED
  - [ ] 1.1 Identify prompt type
  - [ ] 1.2 Understand model, input, output, environment
  - [ ] 1.3 Assess context budget
- [ ] Step 2: Research & Load References
  - [ ] 2.1 Load type-specific reference
  - [ ] 2.2 Load model-specific guide if needed
- [ ] Step 3: Build / Validate ⚠️ REQUIRED
  - [ ] 3.1 Build prompt OR analyze existing prompt
  - [ ] 3.2 Explain each section (Iron Law)
  - [ ] ⛔ GATE: Present to user for feedback
- [ ] Step 4: Optimize & Deliver
  - [ ] 4.1 Run quality checklist
  - [ ] 4.2 Context budget check
  - [ ] 4.3 Suggest 3+ test cases
```

If `--validate`: Read existing → run ccinspect (if applicable) → run promptfoo with rubric for `--type` → combine outputs → score sheet + findings P0/P1/P2 → suggest fixes. **DO NOT use the legacy quality checklist below — it's kept for `--create` mode reference only.**

If `--update-rubric --gap <file>`: Read gap file in `gaps/` → propose new criterion in YAML → present to user → on approval, edit rubric YAML and bump version.

## Principles

1. **Context engineering > prompt engineering.** The prompt is one component. What enters the context window — tools, docs, examples, history — matters as much. Curate the full context.
2. **Clareza > criatividade.** Teste do colega: se um colega inteligente lesse a instrução sem contexto, ele saberia o que fazer? Se não, reescreva.
3. **Mostre, não diga.** Um exemplo vale mais que 10 linhas de instrução. Few-shot > zero-shot pra formatos.
4. **Menos tokens = mais atenção.** Informação irrelevante dilui qualidade. Cada token compete por atenção.
5. **Especifique o output.** JSON Schema, XML tags, templates explícitos. Nunca deixe o modelo adivinhar.
6. **Calibre pro modelo.** Claude 4.x segue instruções literalmente. Caps lock excessivo causa overtriggering. Instrução clara e direta funciona melhor.
7. **Teste antes de confiar.** Prompt que funciona 1 vez pode falhar na 10ª. Avalie sistematicamente.

## --validate workflow (v3)

```
Validate Progress:

- [ ] V.1 Detect type (auto or --type)
  - [ ] Look at file path: CLAUDE.md → claude-md, plan/*.md → technical-plan, etc
  - [ ] Look at content shape: IRON LAWS → iron-laws, role+context → system-prompt
  - [ ] Confirm with user if ambiguous
- [ ] V.2 Run ccinspect (if applicable)
  - [ ] Applies to: CLAUDE.md, SKILL.md, .claude/settings.json, agents
  - [ ] Command: `ccinspect lint <file>` or scoped to project dir
  - [ ] Capture: errors, warnings, notes
- [ ] V.3 Run promptfoo with rubric
  - [ ] Find rubric: `prompt-engineer/rubric/<type>.yaml`
  - [ ] Command: `promptfoo eval -c rubric/<type>.yaml --vars file=<path>`
  - [ ] Capture JSON output: scores per criterion, findings P0/P1/P2
- [ ] V.4 Combine + present
  - [ ] Merge ccinspect (structural) + promptfoo (semantic) findings
  - [ ] Aggregate score (weighted average)
  - [ ] Format: see "Output format" below
- [ ] V.5 Suggest fixes
  - [ ] For each P0: concrete action
  - [ ] For each P1: action if time permits
  - [ ] P2: tech debt list
```

### Output format

```
## Validation: <file>
Type: <claude-md | technical-plan | iron-laws | system-prompt>
Score: X/100 [tier]
Threshold: 75 (production)

### ccinspect (structural)
- <error/warning/note count>
- <key findings>

### promptfoo (semantic, by criterion)
| ID | Criterion | Score | Tier |
|----|-----------|-------|------|
| R001 | Cross-section consistency | 80 | Core |
| R002 | Physical vs textual gates | 60 | Core |
| ... |

### Findings P0 (block release)
- ...

### Findings P1 (fix if possible)
- ...

### Findings P2 (tech debt)
- ...

### Recommendation
APPROVED (≥75) | APPROVED WITH RESERVATIONS | REJECTED (<60) | DO NOT EXECUTE
```

### Anti-drift rule (retroalimentation)

The rubric only grows via documented gaps. When you find a real gap not caught by current rubric:

1. Create file in `gaps/gap_YYYY-MM-DD_<topic>.md` (template in `gaps/_template.md`)
2. Document: prompt tested, what rubric missed, real consequence, proposed criterion
3. Run `prompt-engineer --update-rubric --gap <file>` (semi-auto, asks for approval before editing the YAML)
4. On approval: criterion added with new ID, version bumped, regression test created
5. **Do not add criteria without a documented gap** — speculative criteria bloat the rubric

Reasoning: Constitutional AI lesson — Anthropic doesn't let the model edit its own principles. Auto-edition leads to silent drift. Manual semi-auto with human approval is the realistic pattern (research 2026-04-10).

---

## Step 1: Identify & Context ⚠️ REQUIRED

Determine the prompt type and load the corresponding reference:

| Type | Reference | When |
|------|-----------|------|
| System prompt (agent/chatbot) | `references/system-prompts.md` | WhatsApp, Typebot, assistente |
| Extraction (OCR, classification) | `references/extracao-dados.md` | Extrair dados de docs, classificar |
| AGENTS.md (AI coding tools) | `references/agents-md.md` | Lovable, Cursor, Claude Code |
| JSON Schema output | `references/json-schema-output.md` | n8n, API, formato garantido |
| GEO (agent discovery) | `references/geo-prompt-guide.md` | Descriptions, skills.sh, READMEs |
| Skill prompt (SKILL.md) | `references/skill-prompt-guide.md` | Prompts internos de skills |

Key context questions:
- Which model? (Claude, Gemini, GPT) → Load `references/claude-4x-guide.md` if Claude
- What input? (text, document, image, structured data)
- What output? (text, JSON, classification, file)
- Where does it run? (n8n, API, Lovable, chat, AGENTS.md)
- What else shares the context? (tools, history, docs — budget matters)

## Step 2: Research & Load References

Load the type-specific reference BEFORE writing. Each contains templates, examples, and anti-patterns.

If targeting Claude 4.x: Load `references/claude-4x-guide.md` — critical differences (prefilling deprecated, adaptive thinking, parallel tool calling, overthoroughness, calibrated language).

## Step 3: Build / Validate ⚠️ REQUIRED

### Creating (--create)

1. Use the template from the type-specific reference
2. For each section, explain WHY it exists (Iron Law)
3. Consider the full context — not just the prompt, but tools, examples, docs
4. Include at least 1 input/output example in the prompt
5. Add explicit handling for edge cases and unknowns
6. Specify files/paths explicitly: `[path] → [action]` beats "handle the relevant files"
7. Include scenarios: happy path, edge case, error — each with expected behavior
8. List dependencies and constraints upfront (not buried in instructions)

### Validating (--validate)

v3 runs via promptfoo + ccinspect with type-specific rubrics (see "--validate workflow" section above). No manual checklist.

For `--create` universal criteria (role, format, instructions, edge cases, few-shot, anti-patterns, calibration), load `references/create-criteria.md`.

⛔ **Confirmation Gate:** Present the prompt with explanation of each section. Get user feedback before finalizing.

## Step 4: Optimize & Deliver

### Context Window Management

- **40-50% rule:** never use more than half the context window for instructions. Leave room for the actual task.
- **KV-cache:** keep system prompt stable between requests. Variable content (user input, docs) at the end.
- **Handoff pattern:** for multi-conversation workflows, save key decisions in .md files (prd.md, spec.md) that survive `/clear`.

### Pre-Delivery Checklist

- [ ] Prompt uses the correct template for its type
- [ ] Each section explains WHY it exists (Iron Law)
- [ ] Output format is explicitly defined (Schema, XML, template)
- [ ] Has at least 1 concrete input→output example
- [ ] Edge cases handled (null, empty, unexpected input)
- [ ] Language calibrated for target model (no excess caps for Claude 4.x)
- [ ] Context budget reasonable (not bloated with redundant info)
- [ ] 3+ test cases suggested to the user

### Suggest Tests

Always suggest at least 3 test inputs:
1. Happy path (normal, expected input)
2. Edge case (empty, null, ambiguous, very long)
3. Adversarial (input that tries to break the format or inject instructions)

## Anti-Patterns

- **Vague system prompt:** "Você é um assistente útil" → zero domain context, zero behavior guidance
- **Encyclopedia prompt:** 5000 words covering every scenario → dilutes attention, model ignores parts
- **All negatives:** "NÃO faça X, NUNCA faça Y, JAMAIS faça Z" → model focuses on what not to do. Reframe positively
- **No output format:** letting the model guess → inconsistent outputs between runs
- **Caps lock as crutch:** "CRITICAL: You MUST" everywhere → overtriggers in Claude 4.x. Explain why instead
- **JSON in prompt only:** `"Responda APENAS em JSON"` → use Structured Outputs or responseSchema when available
- **Ignoring context budget:** prompt + tools + docs + history > 50% of window → quality degrades

## Example: Good vs Bad

**Bad system prompt:**
```
Você é um assistente de atendimento. Responda de forma educada.
```

**Good system prompt:**
```xml
<role>
Assistente virtual da clínica OdontoMax. Atende via WhatsApp.
</role>
<context>
Horário: seg-sex 8h-18h, sáb 8h-12h.
Serviços: limpeza, clareamento, ortodontia, implantes, emergência.
</context>
<instructions>
1. Cumprimente pelo nome se disponível
2. Identifique intenção: agendamento, dúvida, emergência, reclamação
3. Agendamentos: pergunte especialidade + 2 opções de horário
4. Emergências: passe telefone direto (11) 99999-0000
5. Nunca dê diagnóstico — "Precisa de avaliação presencial"
6. Se não souber: "Vou verificar com a equipe e retorno em até 2h"
</instructions>
<output_format>
Máx 3 parágrafos. Tom: profissional mas acolhedor. *Negrito* pra info-chave.
</output_format>
```

## Integration & Boundaries

### When to use (this skill)

| Task | Use |
|------|-----|
| Validate CLAUDE.md, technical plan, iron-laws files | **prompt-engineer --validate --type <type>** |
| Create new prompt (chatbot, agent, extraction, JSON) | **prompt-engineer --create** |
| Optimize GEO of description (standalone) | **prompt-engineer --geo** or **geo-optimizer** (surgical) |

### When NOT to use (delegate)

| Task | Use instead |
|------|-------------|
| Edit text inside an existing SKILL.md | **skill-builder --evolve --light** |
| Create new SKILL.md from scratch | **skill-builder --full** |
| Validate SKILL.md structure | **skill-builder --validate** |
| One-line prompt | answer directly, no skill needed |
| AGENTS.md for Lovable | **lovable-knowledge** |
| Prompt logic (business rules) | domain skill (PRD, n8n, etc.) |

### Composition (use alongside)

- **n8n Architect** — AI nodes need prompts. Use this skill for the prompt, n8n for the architecture
- **Product Discovery & PRD** — prompts for Lovable are inputs of the PRD
- **Security Audit** — agents with tools → consider OWASP LLM Top 10
- **maestro** — when unclear which skill applies

---
name: prompt-engineer
description: "Skill para criar, validar e otimizar prompts e contextos para qualquer LLM (Claude, Gemini, GPT). Use esta skill SEMPRE que o usuário mencionar: prompt, system prompt, context engineering, agente, chatbot, JSON Schema pra IA, 'como faço o modelo retornar X', 'o modelo tá respondendo errado', 'preciso melhorar esse prompt', 'quero criar um agente', 'instrução pro Lovable/Cursor', AGENTS.md, ou qualquer variação que envolva escrever instruções pra um modelo de IA. Também use quando o usuário estiver criando skills, configurando nodes de IA no n8n, ou montando agentes de WhatsApp. Se o usuário disser 'valida esse prompt' ou 'melhora isso', USE esta skill. Also triggers on: fix my prompt, improve this system message, write a prompt for. NÃO use se o usuário quer criar uma SKILL do Claude — use skill-builder. Prompt simples de uma linha, responda direto."
---

# Prompt & Context Engineer v2

IRON LAW: Never output a prompt without explaining WHY each section exists. A prompt the user doesn't understand is a prompt they can't maintain or improve.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--create` | Create a new prompt from scratch | true |
| `--validate` | Validate/improve an existing prompt | false |
| `--type <t>` | Prompt type: system, extraction, agents-md, json-schema | auto-detect |

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
  - [ ] 3.2 Explain each section (IRON LAW)
  - [ ] ⛔ GATE: Present to user for feedback
- [ ] Step 4: Optimize & Deliver
  - [ ] 4.1 Run quality checklist
  - [ ] 4.2 Context budget check
  - [ ] 4.3 Suggest 3+ test cases
```

If `--validate`: Read existing → quality checklist → structured feedback → improved version.

## Principles

1. **Context engineering > prompt engineering.** The prompt is one component. What enters the context window — tools, docs, examples, history — matters as much. Curate the full context.
2. **Clareza > criatividade.** Teste do colega: se um colega inteligente lesse a instrução sem contexto, ele saberia o que fazer? Se não, reescreva.
3. **Mostre, não diga.** Um exemplo vale mais que 10 linhas de instrução. Few-shot > zero-shot pra formatos.
4. **Menos tokens = mais atenção.** Informação irrelevante dilui qualidade. Cada token compete por atenção.
5. **Especifique o output.** JSON Schema, XML tags, templates explícitos. Nunca deixe o modelo adivinhar.
6. **Calibre pro modelo.** Claude 4.x segue instruções literalmente. Caps lock excessivo causa overtriggering. Instrução clara e direta funciona melhor.
7. **Teste antes de confiar.** Prompt que funciona 1 vez pode falhar na 10ª. Avalie sistematicamente.

## Step 1: Identify & Context ⚠️ REQUIRED

Determine the prompt type and load the corresponding reference:

| Type | Reference | When |
|------|-----------|------|
| System prompt (agent/chatbot) | `references/system-prompts.md` | WhatsApp, Typebot, assistente |
| Extraction (OCR, classification) | `references/extracao-dados.md` | Extrair dados de docs, classificar |
| AGENTS.md (AI coding tools) | `references/agents-md.md` | Lovable, Cursor, Claude Code |
| JSON Schema output | `references/json-schema-output.md` | n8n, API, formato garantido |

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

### Validating (--validate)

Read the full prompt, then analyze with the quality checklist:

| Criterion | Ask yourself | Red flag |
|-----------|-------------|----------|
| Context/Role | Does the model know WHO it is and FOR WHAT? | Generic, personality-less output |
| Specific instructions | Clear actions or vague direction? | Model invents behavior |
| Output format | Precisely defined? | Inconsistent between runs |
| Examples (few-shot) | At least 1 input→output? | Model guesses format |
| Edge cases | Handles invalid, empty, unexpected? | Silent failure in production |
| What NOT to do | Explicit anti-patterns? Phrased positively? | Undesired behaviors |
| Attention budget | Too long? Redundant? | Diluted attention, high cost |
| Language calibration | Excess caps lock? ("MUST", "NEVER") | Overtriggering in 4.x |
| Tool management | Minimal, no overlap? | Model confuses tools |

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

## Integration with other skills

| Skill | When |
|-------|------|
| **n8n Architect** | Nodes de IA precisam de prompts. Use esta pra prompt, n8n pra arquitetura |
| **Skill Builder** | Se quer instruções persistentes com SKILL.md → redirecione |
| **Product Discovery & PRD** | Prompts pro Lovable são inputs do PRD |
| **Security Audit** | Agente com tools → considere OWASP LLM Top 10 |

## When NOT to use

- **Skill do Claude** (SKILL.md persistente) → use skill-builder
- **Prompt simples de 1 linha** → faz direto
- **Conteúdo do prompt** (lógica de negócio) → use skill de domínio (PRD, n8n)
- **AGENTS.md pra Lovable específico** → use lovable-knowledge
- Confused about which skill to use → invoke maestro

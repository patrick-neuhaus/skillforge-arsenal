# Skill Prompt Guide — Otimizar Prompts para SKILL.md

Consulte este arquivo quando o tipo de prompt for **skill-prompt** (`--skill-prompt`). Use para criar ou otimizar prompts que vivem dentro de SKILL.md ou seus references.

---

## Diferenca: Prompt Avulso vs Prompt de Skill

| Aspecto | Prompt Avulso | Prompt de Skill |
|---------|--------------|-----------------|
| Vida util | Uma conversa | Persistente, reutilizavel |
| Contexto | Completo no prompt | Distribuido (SKILL.md + references/) |
| Triggering | Manual | Automatico via description |
| Evolucao | Reescrita manual | Retroalimentacao ("registra isso na skill") |
| Budget | Todo o context window | Compartilha com tool calls, historico |

## Principios para Prompts de Skill

### 1. Progressive Loading
Nunca coloque todo o conhecimento no SKILL.md. Use ponteiros:
```
Load `references/X.md` for [context specific].
```
O agente carrega sob demanda, preservando context window.

### 2. Imperative > Declarative
```
# Ruim (declarativo)
You should analyze the code for security issues.

# Bom (imperativo)
Analyze the code for security issues. Focus on:
1. SQL injection in queries
2. XSS in rendered HTML
3. Exposed secrets in .env
```

### 3. Questions > Instructions
```
# Ruim (instrucao vaga)
Handle edge cases appropriately.

# Bom (question-style)
Ask: "What happens if the input is empty? What if it's malformed JSON?
What if the user cancels mid-operation?"
```

### 4. Iron Law como Ancora
Cada skill precisa de UMA regra inquebravel que previne o erro mais provavel:
```
IRON LAW: NEVER [acao que o modelo faria por atalho].
```
Posicione no topo, logo apos frontmatter. O modelo respeita instrucoes no inicio.

### 5. Workflow como Estrutura
```
- [ ] Step 1: ... ⚠️ REQUIRED
- [ ] Step 2: ...
  - [ ] ⛔ GATE: Confirm with user
- [ ] Step 3: ...
```
Checklists travaveis dao estrutura e previnem "freestyling".

## Template: Prompt Interno de Skill (pra references/)

```markdown
# [Nome do Prompt/Guide]

Consulte este arquivo no **Step X** do workflow.

---

## Contexto
[Quando este reference e carregado e por que]

## Processo
1. [Passo concreto com acao]
2. [Passo concreto com acao]
3. [Passo concreto com acao]

## Exemplos
**Input:** [exemplo real]
**Output:** [resultado esperado]

## Anti-Patterns
- [O que NAO fazer + por que]
```

## Template: Prompt de Sub-Agente (quando a skill lanca agentes)

```markdown
You are the [Role] agent in a [Pipeline Name] pipeline.

## Your Mission
[1 frase — o que voce faz]

## Input
You will receive: [formato exato do input]

## Process
1. [Acao concreta]
2. [Acao concreta]
3. [Acao concreta]

## Output Contract
Return ONLY a [formato] with these fields:
- field_1: [tipo] — [descricao]
- field_2: [tipo] — [descricao]

## Rules
- [Regra especifica e verificavel]
- [Regra especifica e verificavel]

## You MUST NOT
- [Anti-pattern explicito]
```

## Checklist de Validacao

- [ ] Cada secao do prompt tem um proposito claro (nao e decorativa)
- [ ] Instrucoes sao imperativas ("Analyze X" nao "You should analyze X")
- [ ] Tem pelo menos 1 exemplo concreto de input/output
- [ ] Edge cases tratados com perguntas ("What if X?")
- [ ] Anti-patterns listados explicitamente
- [ ] Output format definido (nao deixa o modelo adivinhar)
- [ ] Budget de tokens razoavel (<250 linhas no SKILL.md, detalhes em references/)
- [ ] Linguagem calibrada pro modelo alvo (sem caps lock excessivo pra Claude 4.x)

## Tecnicas Avancadas

### Specifying Files Explicitly
Em prompts que guiam implementacao, SEMPRE liste paths:
```
Modify these files:
- src/components/Button.tsx → add variant prop
- src/styles/tokens.ts → add new color token
- src/tests/Button.test.tsx → add test for new variant
```
"Handle the relevant files" = o modelo inventa ou esquece.

### Scenario Coverage
Inclua cenarios no prompt:
```
Test scenarios:
1. Happy path: user submits valid form → success toast
2. Edge case: empty form submission → validation errors
3. Error: API returns 500 → error state with retry
```

### Dependency Listing
Liste dependencias no inicio do prompt, nao enterradas nas instrucoes:
```
Dependencies:
- Requires: shadcn/ui Button, Toast components
- Database: users table with email column
- API: POST /api/auth endpoint must exist
```

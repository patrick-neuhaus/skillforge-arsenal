---
name: lovable-knowledge
description: "Create, generate, configure, optimize and review Workspace Knowledge, Project Knowledge and AGENTS.md for Lovable. Use SEMPRE que mencionar: knowledge, lovable knowledge, workspace knowledge, project knowledge, AGENTS.md, CLAUDE.md, 'configurar o lovable', 'padrões do lovable', 'regras pro lovable', 'o lovable tá fazendo X errado', 'quero que o lovable siga', 'instruções pro lovable', fix/improve/update/review knowledge, código inconsistente, libs erradas, preparar projeto pro Lovable após PRD, construir regras pra AI tools (Cursor, Claude Code). PRD diz O QUE construir, esta skill diz COMO o Lovable deve build. NÃO use pra definir O QUE construir (use product-discovery-prd) ou debug de código (ajude direto)."
---

# Lovable Knowledge Generator v3

IRON LAW: NUNCA gere Knowledge sem ler o codebase existente do projeto primeiro. Knowledge genérico conflita com o que o Lovable já gerou. Se não tem codebase, pergunte se existe antes de prosseguir.

## Options

| Option | Descrição | Default |
|--------|-----------|---------|
| `workspace` | Gerar Workspace Knowledge (setup único, global) | false |
| `project` | Gerar Project Knowledge (por projeto) | true |
| `agents` | Gerar AGENTS.md universal pro repo | false |
| `review` | Revisar Knowledge existente e sugerir melhorias | false |

## Workflow

```
Lovable Knowledge Progress:

- [ ] Step 1: Contexto ⚠️ REQUIRED
  - [ ] 1.1 Identificar modo (workspace / project / agents / review)
  - [ ] 1.2 Verificar se existe codebase (IRON LAW)
  - [ ] 1.3 Verificar se existe PRD ou knowledge anterior
- [ ] Step 2: Coleta ⚠️ REQUIRED
  - [ ] 2.1 Carregar referência do modo escolhido
  - [ ] 2.2 Perguntas em blocos de 2-3 (nunca todas de uma vez)
  - [ ] 2.3 Extrair info de PRD/codebase quando disponível
- [ ] Step 3: Geração ⚠️ REQUIRED
  - [ ] 3.1 Aplicar template do modo escolhido
  - [ ] 3.2 Incluir guardrails obrigatórios
  - [ ] 3.3 Validar limites de caracteres
  - [ ] ⛔ GATE: Apresentar knowledge gerado ao usuário para aprovação
- [ ] Step 4: Validação ⛔ BLOCKING
  - [ ] Rodar checklist de entrega
  - [ ] Verificar conflitos entre Workspace e Project Knowledge
  - [ ] ⛔ GATE: Aprovação final antes de considerar pronto
```

Se `review`: Ler knowledge existente → diagnosticar com checklist → sugerir melhorias → regenerar se necessário.

## Step 1: Contexto ⚠️ REQUIRED

### 1.1 Identificar modo

Pergunte se não está claro: "Você quer criar Workspace Knowledge (global, vale pra todos os projetos), Project Knowledge (específico deste projeto), ou AGENTS.md (arquivo no repo)?"

### 1.2 Verificar codebase (IRON LAW)

Se existe codebase, analise ANTES de gerar:
- `package.json` — libs já instaladas, scripts
- Estrutura de pastas — arquitetura existente
- Schema SQL / migrations — modelo de dados
- Componentes existentes — padrões de naming e estilo
- Knowledge atual — o que já está configurado

Se não existe codebase, pergunte: "Esse projeto já tem código ou vai começar do zero?"

### 1.3 Verificar PRD

Se existe PRD (output de product-discovery-prd), extraia automaticamente: visão, stack, roles, fluxos, regras de negócio, modelo de dados, fora do escopo. Pergunte APENAS o que o PRD não cobre.

## Step 2: Coleta ⚠️ REQUIRED

### Por modo

**Workspace Knowledge:** Load `references/workspace-knowledge.md` — perguntas sobre stack, padrões, arquitetura, guardrails globais.

**Project Knowledge:** Load `references/project-knowledge.md` — perguntas sobre o projeto, dados, design, domínio, constraints.

**AGENTS.md:** Load `references/agents-md-guide.md` — estrutura, limites, estratégia multi-tool.

### Regra de coleta

- Blocos de 2-3 perguntas por vez
- Se tem PRD/codebase, pule perguntas já respondidas
- Confirme entendimento antes de gerar: "Entendi X, Y e Z. Correto?"

## Step 3: Geração ⚠️ REQUIRED

### 3.1 Aplicar template

Use o template do modo escolhido (disponível nos arquivos de referência). Inclua APENAS seções com conteúdo real — remova seções vazias.

### 3.2 Guardrails obrigatórios

Load `references/lovable-best-practices.md` para guardrails e regras de output.

Todo Knowledge DEVE incluir:
- Pelo menos 3 regras NEVER (proibições explícitas)
- Seção "Out of scope" (Project Knowledge)
- Libs com versões pinadas quando relevante

### 3.3 Validar limites

- Workspace/Project Knowledge: max 10.000 caracteres
- AGENTS.md: max ~300 linhas (sweet spot de atenção)
- Se exceder, corte na ordem: exemplos → detalhes de schema → convenções de código → arquitetura → regras gerais (nunca corte regras gerais)

⛔ **GATE:** Apresente o Knowledge completo ao usuário. Não considere pronto sem aprovação explícita.

## Step 4: Validação ⛔ BLOCKING

### Pre-Delivery Checklist

**Estrutura:**
- [ ] Output dentro do limite de caracteres (10k chars ou ~300 linhas)
- [ ] Formato pronto pra colar no Lovable (markdown limpo, sem frontmatter)
- [ ] Seções vazias removidas

**Conteúdo:**
- [ ] Tem pelo menos 3 regras NEVER com ação específica
- [ ] Libs definidas com nomes exatos (não "use uma boa lib")
- [ ] Naming conventions definidas
- [ ] Decisões de arquitetura que a IA não tem como adivinhar
- [ ] "Out of scope" presente (Project Knowledge)
- [ ] Sem conflito entre Workspace e Project Knowledge
- [ ] Nenhuma regra que ESLint/Prettier já enforça

**Qualidade:**
- [ ] Específico > genérico (teste: "isso se aplica a qualquer projeto?" Se sim, é genérico demais)
- [ ] Sem floreios tipo "escreva código limpo"
- [ ] Termos técnicos em inglês, resto em PT-BR
- [ ] Cada NEVER/ALWAYS tem razão implícita ou explícita

## Anti-patterns

| Anti-pattern | Por que é ruim | Correto |
|-------------|----------------|---------|
| Knowledge genérico sem ler codebase | Conflita com código existente, Lovable fica confuso | Ler codebase primeiro, alinhar Knowledge |
| Despejar 6 blocos de perguntas de uma vez | Usuário desiste ou responde superficialmente | Blocos de 2-3, iterar |
| "Escreva código limpo e organizado" | Instrução vazia, não muda comportamento | "Use unknown, nunca any. Named exports, nunca default" |
| Knowledge > 10k chars sem cortar | Lovable trunca silenciosamente | Priorize e corte |
| Copiar README como Knowledge | Knowledge é pra IA, não pra humanos | Extraia só decisões de arquitetura e proibições |
| Não incluir "Out of scope" | Lovable refatora tudo que acha melhorável | Liste explicitamente o que NÃO mexer |
| Repetir regras do Workspace no Project | Desperdício de chars, risco de conflito | Project só o que é específico do projeto |
| Gerar AGENTS.md pra projeto solo no Lovable | Over-engineering, Knowledge basta | AGENTS.md só pra multi-tool ou >10k chars |

## Integration

| Skill | Quando usar | Direção |
|-------|-------------|---------|
| **product-discovery-prd** | PRD pronto, quer preparar pro Lovable | PRD → input desta skill |
| **supabase-db-architect** | Schema do banco precisa ser refletido no Knowledge | Schema → "Key database tables" |
| **prompt-engineer** | AGENTS.md precisa de seção de prompting pra agentes | Combinar output |
| **ui-design-system** | Design system definido, refletir no Knowledge | Tokens/componentes → "Design guidelines" |
| **sdd** | Documento técnico detalhado pra projetos complexos | SDD → Architecture rules |
| **maestro** | Orquestrar pipeline completo (PRD → Schema → Knowledge) | Maestro coordena a sequência |

**Fluxo típico:** product-discovery-prd → supabase-db-architect → **lovable-knowledge** → Lovable

## When NOT to use

- **Definir O QUE construir** → use product-discovery-prd
- **Revisar/debugar código** → ajude diretamente, não é Knowledge
- **Pergunta pontual sobre Lovable** → responda direto (ex: "como uso Plan Mode?")
- **Projeto sem Lovable** → se usa só Cursor/Claude Code, gere AGENTS.md/CLAUDE.md diretamente
- **Otimizar prompt avulso pra Lovable** → use prompt-engineer

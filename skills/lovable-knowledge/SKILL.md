---
name: lovable-knowledge
description: "Skill para gerar Workspace Knowledge e Project Knowledge otimizados para o Lovable. Use esta skill SEMPRE que o usuário mencionar: knowledge, lovable knowledge, workspace knowledge, project knowledge, 'configurar o lovable', 'padrões do lovable', 'regras pro lovable', 'o lovable tá fazendo X errado', 'quero que o lovable siga', 'instruções pro lovable', AGENTS.md, ou qualquer variação que envolva definir como o Lovable deve se comportar ao gerar código. Também use quando o usuário disser que vai começar um projeto novo no Lovable e ainda não tem knowledge configurado, ou quando reclamar que o Lovable tá gerando código inconsistente, usando libs erradas, ou ignorando padrões. Se o usuário já fez discovery/PRD e quer preparar o projeto pro Lovable, USE esta skill — o PRD diz O QUE construir, esta skill diz COMO o Lovable deve construir. NÃO use se o usuário quer definir O QUE construir — use product-discovery-prd. Se é debug de código ou revisão técnica, não é Knowledge — ajude diretamente."
---

# Lovable Knowledge Generator v2

## Visão geral

Esta skill gera blocos de texto otimizados para os campos de Knowledge do Lovable e arquivos AGENTS.md/CLAUDE.md — o ecossistema completo de instruções persistentes que controlam como AI coding tools geram código.

Sem Knowledge configurado, o Lovable toma decisões próprias sobre libs, padrões, arquitetura e naming — e essas decisões mudam entre projetos e conversas. Com Knowledge, você tem consistência e controle.

### O que NÃO é esta skill

- **Não é PRD.** PRD = O QUE construir. Knowledge = COMO o Lovable deve construir.
- **Não substitui prompts.** Knowledge é contexto persistente, não instrução de tarefa.

## Ecossistema de instruction files

### Hierarquia de prioridade do Lovable

O Lovable lê instruções nesta ordem (maior prioridade primeiro):
1. **Project Knowledge** (campo no Lovable)
2. **Workspace Knowledge** (campo no Lovable)
3. **Código do projeto** (análise do repo)
4. **Integration Knowledge** (se configurado)
5. **AGENTS.md / CLAUDE.md** (arquivos no root do repo)

### Estratégia multi-tool

Se o projeto é usado por múltiplas AI tools (Lovable + Cursor + Claude Code), use arquivos complementares:

| Arquivo | Lido por | Escopo |
|---------|----------|--------|
| **AGENTS.md** | Lovable, Cursor, Windsurf, Kilo Code, Codex, Factory | Universal — single source of truth |
| **CLAUDE.md** | Claude Code, Lovable | Claude-específico, sobrescreve AGENTS.md |
| **.github/copilot-instructions.md** | GitHub Copilot | Copilot-específico |
| **.cursor/rules/** | Cursor | Cursor-específico, suporta ativação por contexto |

**Regra prática:** Comece com AGENTS.md como fonte única. Adicione arquivos tool-specific SÓ quando precisar de features que AGENTS.md não cobre.

### Limites

- **Workspace Knowledge:** 10.000 caracteres
- **Project Knowledge:** 10.000 caracteres
- **AGENTS.md:** sem limite formal, mas ~300 linhas é o sweet spot (cada instrução compete por atenção — frontier LLMs seguem ~150-200 instruções de forma confiável)
- **CLAUDE.md:** ~250 linhas (Claude Code usa ~50 linhas do sistema)

**Foco no que a IA erraria SEM o arquivo.** Não repita o que linters já fazem (ESLint, Prettier). Foque em decisões de arquitetura, domínio, e padrões que a IA não tem como adivinhar.

## Modos de operação

### Modo 1: Workspace Knowledge (setup único)

Frequência: uma vez por workspace, revisão a cada 3-6 meses.

### Modo 2: Project Knowledge (recorrente)

Aceita 3 tipos de input:
- **PRD existente** — lê e extrai Knowledge sem refazer perguntas
- **Briefing verbal** — perguntas pra completar
- **Código existente** — analisa padrões e gera knowledge

### Modo 3: AGENTS.md (novo)

Gera arquivo AGENTS.md universal pro root do repo. Use quando:
- O projeto é usado por múltiplas AI tools
- Quer uma fonte única de verdade versionada no git
- O Workspace/Project Knowledge do Lovable não é suficiente (ex: precisa de mais de 10k chars de contexto)

---

## Modo 1: Workspace Knowledge

### Fase 1: Coleta

Perguntas em blocos de 2-3. NÃO despeje todas de uma vez.

**Bloco 1 — Stack e libs:**
- Stack base? (React + TypeScript strict?)
- Libs de UI? (shadcn/ui, Material UI, Chakra?)
- Estado do cliente? (Zustand, Redux, TanStack Query?)
- Validação? (Zod, Yup, manual?)
- Estilização? (Tailwind, CSS Modules?)

**Bloco 2 — Padrões de código:**
- Naming: camelCase variáveis? PascalCase componentes? kebab-case arquivos?
- Exports: named ou default?
- const vs let?
- Comentários em qual idioma?

**Bloco 3 — Arquitetura:**
- Chamadas de API: direto do componente ou service layer?
- Estrutura de pastas? (/components, /services, /hooks, /utils, /types)
- Valores monetários: cents (inteiro) ou decimal?
- Mutations: optimistic update ou espera resposta?

**Bloco 4 — Testes e qualidade:**
- Testes unitários pra hooks/utils?
- Browser testing do Lovable?
- Linter após mudanças significativas?

**Bloco 5 — Localização e brand voice:**
- UI text em qual idioma?
- Formato de data? (DD/MM/YYYY)
- Formato de números? (vírgula ou ponto decimal)
- Tom: formal, informal, técnico?
- Sentence case ou Title Case pra headings?

**Bloco 6 — "Never do" (guardrails globais):**
- O que o Lovable NUNCA deve fazer sem pedir?
- Padrões deprecated a evitar?
- Libs proibidas?

### Fase 2: Geração

Template — inclua APENAS seções com conteúdo real:

```
Coding standards
- [TypeScript strict, const, unknown não any, etc]

Naming conventions
- [camelCase, PascalCase, kebab-case]

Styling
- [Tailwind, regras de CSS]

Libraries
- [libs obrigatórias e preferidas, com versões se relevante]

Architecture
- [service layer, pastas, patterns]

Testing
- [o que testar, quando rodar]

Localization
- [idioma UI, formato data/número, idioma código]

Brand voice
- [tom, convenções de copy, CTAs, mensagens de erro]

General rules
- NEVER [ação proibida 1]
- NEVER [ação proibida 2]
- NEVER [ação proibida 3]
- ALWAYS [regra obrigatória 1]
- ALWAYS [regra obrigatória 2]
```

### Fase 3: Validação

1. **Contagem de caracteres.** Se > 10.000, corte. Prioridade: General Rules > Architecture > Libraries > Coding Standards > resto.
2. **Checklist de completude:**
   - Tem "General rules" com pelo menos 3 "NEVER"? Se não, pergunte.
   - Tem libs definidas? Sem isso, Lovable escolhe sozinho.
   - Tem naming? Sem isso, inconsistente entre projetos.
3. **Apresente e peça confirmação.**

---

## Modo 2: Project Knowledge

### Detecção de input

1. **Tem PRD?** Leia e extraia: visão, stack, usuários, fluxos, regras, modelo de dados, fora do escopo. Pergunte APENAS o que o PRD não cobre.
2. **Tem codebase?** Analise: package.json, pastas, schema SQL, componentes, README. Pergunte o que o código não revela.
3. **Sem nada?** Fluxo completo de perguntas.

### Fase 1: Coleta (sem PRD/código)

**Bloco 1 — O projeto:**
- Em uma frase, o que esse app faz?
- Pra quem? Roles/permissões?

**Bloco 2 — Dados e arquitetura:**
- Tabelas/entidades principais?
- Integrações externas?
- Algo do schema que o Lovable PRECISA saber?

**Bloco 3 — Design e UX:**
- Referência visual?
- Paleta de cores? Tipografia?
- Layout: sidebar, tabs, dashboard?
- Mobile-first ou desktop-first?

**Bloco 4 — Domínio e terminologia:**
- Termos do negócio que o Lovable pode confundir? (ex: "Transaction = mudança de estoque, não pagamento")
- Regras de negócio não óbvias?

**Bloco 5 — Constraints:**
- O que o Lovable NÃO deve mexer?
- Componentes intocáveis?
- Decisões que parecem estranhas mas são intencionais?

### Fase 2: Geração

```
Project overview
[1-3 frases: o que é, pra quem, qual problema resolve]

Users
[Roles, permissões, volume esperado]

Key database tables
[Tabelas com campos essenciais e tipos — só o que o Lovable precisa pra queries e types]

Design guidelines
[Paleta, tipografia, layout, componentes, referências]

Architecture rules
[Decisões específicas deste projeto]

Domain terminology
[Termos com definição clara — especialmente ambíguos]

External integrations
[APIs, webhooks, formatos esperados]

Component states
[Definir empty/loading/error/success pra componentes principais]

Out of scope
[O que NÃO fazer — features adiadas, componentes intocáveis]
```

### Fase 3: Validação

1. **Caracteres < 10.000.** Se exceder, corte detalhes de schema primeiro.
2. **Conflitos com Workspace.** Se contradiz, avise. Project tem prioridade.
3. **"Out of scope" obrigatória.** Sem isso, Lovable refatora o que não deveria.
4. **Apresente e peça confirmação.**

---

## Modo 3: AGENTS.md

### Quando usar

- Projeto usado por múltiplas AI tools
- Precisa versionar instruções no git
- Contexto do projeto excede 10k chars do Knowledge
- Quer que Claude Code, Cursor, e Lovable sigam as mesmas regras

### Template AGENTS.md

```markdown
# AGENTS.md

## Project Context
[1-2 frases: o que é o projeto]

## Tech Stack
- Frontend: [framework, UI lib, state management]
- Backend: [Supabase, auth, edge functions]
- Integrations: [n8n, APIs externas]

## Build & Test Commands
```bash
npm run dev          # dev server
npm run build        # production build
npm run test         # run tests
npm run lint         # lint check
```

## Project Structure
```
src/
  components/    # React components
  hooks/         # Custom hooks
  services/      # API calls, business logic
  types/         # TypeScript types
  utils/         # Pure utility functions
  pages/         # Route pages
```

## Architecture Decisions
- [Decisão 1: ex: "API calls via service layer, NUNCA direto no componente"]
- [Decisão 2: ex: "Valores monetários em cents (inteiro), converter pra exibição"]
- [Decisão 3: ...]

## Domain Terminology
- [Termo]: [Definição clara]

## Database Schema (key tables)
- [tabela]: [campos essenciais com tipos]

## Coding Conventions
- [Padrão 1]
- [Padrão 2]

## DO NOT
- [Proibição 1: ex: "Instalar dependências sem aprovação"]
- [Proibição 2: ex: "Refatorar auth sem ticket"]
- [Proibição 3: ...]
```

### Regra dos ~300 linhas

Cada instrução compete por atenção do modelo. Se o AGENTS.md tiver 500 linhas, as últimas vão ser ignoradas. Mantenha em ~300 linhas ou menos. Priorize:
1. Comandos de build/test (a IA PRECISA disso)
2. Decisões de arquitetura (não tem como adivinhar)
3. Terminologia de domínio (evita confusão)
4. Proibições (DO NOT) (evita danos)

Code style e formatting? Deixe pro linter.

---

## Lovable-specific: boas práticas de prompting

Inclua estas orientações quando gerar Knowledge pra projetos Lovable:

### Plan Mode (60-70% do tempo)

Use Plan Mode pra estruturar antes de pedir código. Economiza créditos e evita retrabalho. O Lovable tem Plan Mode que permite desenhar a estrutura antes de gerar código — mais eficiente que iterar em código direto.

### Frontend-first com mock data

Sequência recomendada pro Lovable:
1. Construir design do frontend (página por página, seção por seção)
2. Plugar backend (Supabase nativo)
3. Refinar UX

Use mock data pra prototipar interações antes de conectar backend real.

### Prompts incrementais

- 3-4 mudanças por prompt, não 5+
- Um componente ou interação por ciclo
- Pense em estados: empty, loading, filled, error, success
- Linguagem consistente entre componentes (Lovable generaliza padrões)
- Construir modular (partes) em vez de páginas inteiras de uma vez

### Guardrails no Knowledge

Sempre inclua no Project Knowledge:
- "NUNCA instale dependências novas sem pedir"
- "NUNCA refatore autenticação sem instrução explícita"
- "NUNCA mude o schema do banco sem aprovação"
- "Use SEMPRE [lib X] para [caso Y]"
- "Pin versions: [lib@version]"

### "Try to Fix" é grátis

O botão "Try to Fix" do Lovable não consome créditos — use sem medo pra resolver erros antes de gastar crédito com prompt novo.

---

## Regras do output

1. **Português brasileiro** pra comunicação. Knowledge em português EXCETO se workspace é pra time internacional.
2. **Termos técnicos em inglês** quando universais.
3. **Sem floreios.** "Escreva código limpo" = inútil. "Nunca use any, use unknown e faça narrowing" = útil.
4. **Específico > genérico.** "Use shadcn/ui Button" > "Use uma lib de componentes moderna".
5. **Exemplos quando ajudam.** "Sentence case (ex: 'Create new project', não 'Create New Project')".
6. **Output como .md** pra copiar direto no Lovable ou salvar como referência.

## Integração com outras skills

- **Depois da skill de PRD:** Sugira rodar esta skill. PRD → Project Knowledge é o fluxo natural.
- **Com Supabase Architect:** "Key database tables" alimentado pelo output da skill de Supabase.
- **Com Tech Lead & PM:** Knowledge pode ser passado junto com briefing de delegação.
- **Com Prompt Engineer:** Se o AGENTS.md precisa de seção de prompting pra agentes IA, combine com a skill de Prompt Engineer.

## Quando NÃO usar

- Definir O QUE construir → skill de PRD
- Revisar/debugar código → ajude diretamente
- Pergunta pontual sobre Lovable → responda direto

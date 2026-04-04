# Lovable — Boas Práticas de Prompting

Referência de padrões e práticas específicas do Lovable para incluir no Knowledge gerado.

---

## Ecossistema de Instruction Files

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
| **.cursor/rules/** | Cursor | Cursor-específico, ativação por contexto |

**Regra prática:** Comece com AGENTS.md como fonte única. Adicione arquivos tool-specific SÓ quando precisar de features que AGENTS.md não cobre.

### Limites

- **Workspace Knowledge:** 10.000 caracteres
- **Project Knowledge:** 10.000 caracteres
- **AGENTS.md:** sem limite formal, mas ~300 linhas é o sweet spot (cada instrução compete por atenção — frontier LLMs seguem ~150-200 instruções de forma confiável)
- **CLAUDE.md:** ~250 linhas (Claude Code usa ~50 linhas do sistema)

---

## Plan Mode (60-70% do tempo)

Use Plan Mode pra estruturar antes de pedir código. Economiza créditos e evita retrabalho. O Lovable tem Plan Mode que permite desenhar a estrutura antes de gerar código — mais eficiente que iterar em código direto.

## Frontend-first com mock data

Sequência recomendada pro Lovable:
1. Construir design do frontend (página por página, seção por seção)
2. Plugar backend (Supabase nativo)
3. Refinar UX

Use mock data pra prototipar interações antes de conectar backend real.

## Prompts incrementais

- 3-4 mudanças por prompt, não 5+
- Um componente ou interação por ciclo
- Pense em estados: empty, loading, filled, error, success
- Linguagem consistente entre componentes (Lovable generaliza padrões)
- Construir modular (partes) em vez de páginas inteiras de uma vez

## Guardrails obrigatórios no Knowledge

Sempre inclua no Project Knowledge:
- "NUNCA instale dependências novas sem pedir"
- "NUNCA refatore autenticação sem instrução explícita"
- "NUNCA mude o schema do banco sem aprovação"
- "Use SEMPRE [lib X] para [caso Y]"
- "Pin versions: [lib@version]"

## "Try to Fix" é grátis

O botão "Try to Fix" do Lovable não consome créditos — use sem medo pra resolver erros antes de gastar crédito com prompt novo.

---

## Princípio do conteúdo efetivo

**Foco no que a IA erraria SEM o arquivo.** Não repita o que linters já fazem (ESLint, Prettier). Foque em:
- Decisões de arquitetura (impossível inferir)
- Domínio e terminologia (evita confusão semântica)
- Proibições explícitas (evita danos)
- Schema resumido (queries corretas)

### O que NÃO incluir no Knowledge

- Regras de estilo que ESLint/Prettier enforçam
- Documentação de API (use links)
- Histórico do projeto
- Instruções pra humanos (Knowledge é pra IA)
- "Escreva código limpo" (inútil — seja específico)

---

## Regras de output

1. **Português brasileiro** pra comunicação. Knowledge em português EXCETO se workspace é pra time internacional.
2. **Termos técnicos em inglês** quando universais (hook, component, query).
3. **Sem floreios.** "Nunca use any, use unknown e faça narrowing" > "Escreva código limpo".
4. **Específico > genérico.** "Use shadcn/ui Button" > "Use uma lib de componentes moderna".
5. **Exemplos quando ajudam.** "Sentence case (ex: 'Create new project', não 'Create New Project')".
6. **Output como .md** pra copiar direto no Lovable ou salvar como referência.

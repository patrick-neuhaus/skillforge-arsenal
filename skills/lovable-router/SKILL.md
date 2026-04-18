---
name: lovable-router
description: "Route, classify, and decide how to implement changes in Lovable projects. Analyzes requested modifications and routes to the correct path: direct code editing (frontend, hooks, utils) or Lovable prompt generation (schema, RLS, edge functions, storage policies). Generates optimized prompts for Lovable when database changes are needed. Use when: editar projeto lovable, 'quero mudar X no lovable', 'mexer no banco do lovable', 'adicionar tabela', 'mudar RLS', 'criar edge function', 'posso editar direto?', 'isso muda o banco?', 'gerar prompt pro lovable', 'o lovable precisa fazer isso', classify lovable change, route lovable edit, generate lovable prompt, edit lovable project, modify supabase via lovable, 'o que o lovable gerencia?', 'mudo direto ou mando prompt?', 'edição direta vs prompt'. NÃO use pra gerar Knowledge (use lovable-knowledge) nem pra design de schema sem contexto Lovable (use supabase-db-architect)."
---

# Lovable Router — Roteador de Mudanças

IRON LAW: NUNCA editar schema, RLS, edge functions, storage policies ou database functions diretamente num repo Lovable. O Lovable gerencia migrations internamente — editar direto dessincroniza types, deploy e estado do banco. Toda alteração de banco DEVE virar prompt pro Lovable.

## Options

| Option | Descrição | Default |
|--------|-----------|---------|
| `--route` | Analisar mudança e sugerir caminho (direto vs prompt) | default |
| `--prompt` | Forçar rota banco: gerar prompt pro Lovable | - |
| `--direct` | Forçar rota código: implementar direto | - |

## Workflow

```
Lovable Router Progress:

- [ ] Step 1: Identificar Mudança ⚠️ REQUIRED
  - [ ] 1.1 O que o usuário quer alterar?
  - [ ] 1.2 Load references/decision-matrix.md
  - [ ] 1.3 Classificar: código puro / banco / zona cinza
  - [ ] ⛔ GATE: Confirmar classificação com usuário antes de prosseguir
- [ ] Step 2A: Rota Código (se classificado como código puro)
  - [ ] 2A.1 Avaliar escopo: pontual ou feature completa?
  - [ ] 2A.2 Se feature: invocar sdd (--research → --spec → --implement)
  - [ ] 2A.3 Se pontual: editar com skills relevantes
  - [ ] 2A.4 trident --review antes de entregar
- [ ] Step 2B: Rota Banco (se classificado como banco)
  - [ ] 2B.1 Load references/prompt-templates.md
  - [ ] 2B.2 Coletar contexto: objetivo, tabelas afetadas, RLS, exemplos
  - [ ] 2B.3 Se schema complexo: invocar supabase-db-architect antes
  - [ ] 2B.4 prompt-engineer gera prompt otimizado pro Lovable
  - [ ] ⛔ GATE: Apresentar prompt pro usuário copiar/colar no Lovable
- [ ] Step 3: Pós-Lovable (se rota banco)
  - [ ] 3.1 Após Lovable aplicar: verificar se gerou corretamente
  - [ ] 3.2 Se precisa ajustes de código (não-banco): aplicar direto
  - [ ] 3.3 Se Lovable errou: refinar prompt e reenviar
```

## Step 1: Identificar Mudança

Pergunte ao usuário o que quer alterar. Depois classifique consultando a decision matrix.

Load `references/decision-matrix.md` — contém tabela completa de classificação com exemplos.

### Classificação rápida

| Tipo | Rota | Exemplos |
|------|:----:|---------|
| Frontend puro | ✅ Direto | Componentes, pages, hooks, utils, styles, assets, configs |
| Banco/infra Supabase | 🔀 Prompt | Tables, columns, RLS, edge functions, storage policies, triggers |
| Zona cinza | ⚠️ Avaliar | Queries inline, hooks com supabase client, types manuais |
| Types gerados | ⛔ Nunca | database.types.ts — auto-gerado, NUNCA editar manualmente |

**Zona cinza:** Se a mudança altera o contrato de dados (shape dos objetos que vêm do banco), é rota banco. Se só muda como os dados são usados no frontend, é rota código.

⛔ **GATE:** "Classifiquei como [código/banco/zona cinza] porque [razão]. Concorda?"

## Step 2A: Rota Código

Editar diretamente no repo. Escolher approach baseado no escopo:

**Pontual** (1-3 arquivos, mudança isolada):
- Editar com skills relevantes: react-patterns, component-architect, ui-design-system
- trident --review antes de entregar

**Feature completa** (múltiplos arquivos, lógica nova):
- sdd --research → sdd --spec → sdd --implement
- architecture-guard se envolve decisões de arquitetura
- trident --review ao final

## Step 2B: Rota Banco

Gerar prompt otimizado pro Lovable. Load `references/prompt-templates.md`.

### Estrutura do prompt

Todo prompt pro Lovable DEVE conter:
1. **Objetivo claro** — o que mudar e por quê
2. **Schema changes** — tabelas, colunas, tipos, constraints
3. **RLS policies** — quem pode ler/escrever o quê
4. **Exemplos de uso** — como o frontend vai consumir os novos dados
5. **Constraints** — o que NÃO alterar, o que manter intacto

Se o schema é complexo (3+ tabelas, relacionamentos N:M, multi-tenant), invocar supabase-db-architect ANTES de gerar o prompt. O output do architect vira input do prompt.

⛔ **GATE:** Apresentar prompt completo. Usuário copia e cola no Lovable.

## Step 3: Pós-Lovable

Após Lovable aplicar as mudanças de banco:
1. Pull as mudanças pro repo local
2. Verificar se migrations foram geradas corretamente
3. Se precisa ajustes de código frontend (não-banco): aplicar direto (volta pra Step 2A)
4. Se Lovable errou ou faltou algo: refinar prompt com contexto do erro

## Anti-patterns

| Anti-pattern | Por que é ruim | Correto |
|-------------|----------------|---------|
| Editar database.types.ts direto | Auto-gerado pelo Lovable, será sobrescrito | Mudar via prompt → Lovable regenera |
| ALTER TABLE via SQL no Supabase Studio | Lovable perde sincronia de migrations | Prompt pro Lovable gerar migration |
| Criar edge function via CLI | Deploy e versionamento ficam fora do Lovable | Prompt pro Lovable criar |
| Prompt pro Lovable sem contexto de RLS | Lovable cria tabela sem proteção | Sempre incluir RLS no prompt |
| Forçar rota código pra "ganhar tempo" | Dessincroniza estado → bugs silenciosos | Avaliar honestamente antes |
| Prompt gigante com 10+ mudanças | Lovable confunde e faz parcial | 3-4 mudanças por prompt |

## Pre-delivery checklist

- [ ] Mudança foi classificada corretamente (código vs banco vs zona cinza)
- [ ] Usuário confirmou a classificação antes de prosseguir
- [ ] [Rota código] Mudanças não tocam em schema, RLS, edge functions ou types gerados
- [ ] [Rota banco] Prompt contém: objetivo, schema, RLS, exemplos, constraints
- [ ] [Rota banco] Se schema complexo, supabase-db-architect foi consultado
- [ ] [Rota banco] Prompt tem ≤4 mudanças (não sobrecarregar o Lovable)
- [ ] [Pós-Lovable] Migrations geradas corretamente
- [ ] Nenhum arquivo auto-gerado foi editado manualmente

## Integration

| Skill | Quando/como |
|-------|-------------|
| **lovable-knowledge** | Se Project Knowledge está incompleto ou desatualizado, gere/atualize antes de rotear |
| **supabase-db-architect** | Schema complexo (3+ tabelas, N:M, multi-tenant) → architect define → prompt usa output |
| **prompt-engineer** | Gera prompt otimizado pro Lovable com estrutura e validação |
| **sdd** | Rota código com feature completa → SDD pipeline |
| **react-patterns** | Rota código com componentes React |
| **component-architect** | Rota código com arquitetura de componentes |
| **trident** | Review do código editado direto |
| **maestro** | Maestro roteia "editar projeto lovable" → esta skill |

## When NOT to use

- **Gerar Knowledge** (Workspace/Project/AGENTS.md) → use lovable-knowledge
- **Design de schema sem contexto Lovable** → use supabase-db-architect direto
- **Debug de código** → ajude diretamente
- **Pergunta sobre Lovable** (como usar Plan Mode?) → responda direto
- **Projeto sem Lovable** → não faz sentido rotear

## References

| Arquivo | Conteúdo |
|---------|----------|
| `references/decision-matrix.md` | Tabela completa de classificação código vs banco com exemplos |
| `references/prompt-templates.md` | Templates de prompt pro Lovable por tipo de mudança |
| `references/supabase-boundary.md` | O que Lovable gerencia vs o que pode editar direto |

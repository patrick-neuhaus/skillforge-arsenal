---
name: repo-review
description: "Pipeline de 3 agentes pra detecção profunda de bugs em codebase ou banco de dados. Use esta skill quando o usuário precisar de: auditoria profunda de código, revisão de segurança, detecção de bugs após implementação de features complexas, ou quando pedir 'revisa esse código', 'tem bug nisso?', 'faz um audit'. Usa 3 agentes sequenciais (encontrar, verificar, arbitrar) pra maximizar bugs reais com mínimo de falsos positivos. NÃO use pra: revisão de estilo, sugestões de refatoração, análise de cobertura de testes, mudanças triviais, ou revisão de UX/UI — pra UX use ux-audit. Se é uma pergunta pontual sobre um trecho de código, responda direto sem acionar o pipeline."
---

# Repo Review v2 — Detecção profunda de bugs

## Visão geral

Pipeline de detecção de bugs em codebase ou banco de dados. Combina camada determinística (linters estáticos) com 3 agentes IA em sequência: **Bug Finder** gera hipóteses, **Bug Verifier** confirma ou rejeita cada achado independentemente, **Final Arbiter** emite veredictos baseados em evidência.

O princípio central é: Lint → Gerar → Verificar → Julgar. Ferramentas estáticas pegam o óbvio (e pegam rápido — 50-100x mais rápido que LLMs). Agentes IA focam no que ferramentas estáticas não pegam: lógica, race conditions, edge cases, design bugs.

### Novidades na v2

- **Camada determinística** — Linter estático ANTES dos agentes IA (Oxlint preferido, ESLint como fallback)
- **Fan-Out/Gather** — Opção de rodar múltiplos Bug Finders em paralelo com focos diferentes
- **Estatísticas de AI code review** — SAST pega ~50% dos bugs, humanos pegam os outros ~50%. Pipeline híbrido maximiza cobertura.
- **PR size awareness** — Escopo de revisão segue regra de <400 LOC por batch (Cisco research: detection rate despenca acima disso)
- **Integração com AI PR tools** — Como usar CodeRabbit/Copilot PR Review como complemento

## Princípios

1. **Determinístico primeiro.** Rode linters antes dos agentes. Regras estáticas não geram falsos positivos no nível dos agentes e rodam em milissegundos.
2. **Re-inspeção independente.** Cada agente lê o código real. Nenhum agente confia apenas no texto do agente anterior — porque texto pode omitir contexto que o código revela.
3. **Recall limitado.** Bug Finder tem cap rígido (12 achados, máx 3 suspeitos). Quantidade sem controle colapsa o pipeline em ruído de triagem.
4. **Baseado em evidência.** Toda claim requer: localização específica, trigger concreto, história de falha. Sem isso, é opinião, não bug.
5. **Contra-argumento forçado.** Bug Finder deve declarar a razão mais forte pela qual cada achado pode estar errado. Isso reduz falsos positivos na origem.
6. **Permissão pra abster.** Verifier pode dizer INSUFFICIENT_EVIDENCE. Arbiter pode dizer NEEDS_HUMAN_CHECK. Forçar verdicts binários gera falsa certeza.
7. **Sem scoring fictício.** Sem sistemas de pontos inventados. Critérios de aceitação e requisitos de evidência governam qualidade.
8. **Escopo controlado.** Se o codebase tem >400 LOC de mudanças, divida em batches. Research da Cisco mostra que detecção cai drasticamente acima de 400 LOC numa única revisão.

## Quando usar

- Auditoria profunda de codebase ou banco pra bugs, erros de lógica, race conditions, edge cases
- Revisão pós-implementação de features complexas
- Quando precisa de relatórios de bug de alta confiança com mínimo de falsos positivos

## Quando NÃO usar

- Revisão de estilo ou sugestões de refatoração → responda direto
- Análise de cobertura de testes → responda direto
- Mudanças triviais ou perguntas pontuais sobre código → responda direto
- Revisão de UX/UI → use ux-audit
- Auditoria de segurança focada → use security-audit (o pipeline é similar mas com domínios OWASP)

## O pipeline

```
[Camada determinística: Oxlint/ESLint + TypeScript compiler]
    ↓ erros estáticos resolvidos ou documentados
Bug Finder (references/bug-finder-prompt.md)
    ↓ output: lista de achados com hipóteses
Bug Verifier (references/bug-verifier-prompt.md)
    ↓ output: cada achado confirmado, rejeitado, ou evidência insuficiente
Final Arbiter (references/final-arbiter-prompt.md)
    ↓ output: veredictos finais com evidência
Apresentar veredictos ao usuário
```

### Variante: Fan-Out/Gather (codebase grande)

Pra codebases grandes, use o padrão Scatter-Gather pra paralelizar:

```
[Camada determinística: Oxlint/ESLint]
    ↓
Bug Finder A (foco: lógica e edge cases)     ──┐
Bug Finder B (foco: concorrência e state)     ──┤── Gather + dedupe
Bug Finder C (foco: integração e data flow)   ──┘
    ↓ merge: achados unificados, duplicatas removidas
Bug Verifier
    ↓
Final Arbiter
```

**Quando usar Fan-Out:** Codebase com 1000+ LOC de mudanças, ou >10 arquivos modificados. Cada Bug Finder recebe um subset de arquivos OU um foco de análise diferente. O Gather remove duplicatas antes de passar pro Verifier.

**Regra:** Cada Bug Finder mantém seu cap de 12 achados. Após merge+dedupe, o total não deve exceder 20 achados pro Verifier.

## Camada determinística (NOVO v2)

### Linters recomendados

**Opção 1 — Oxlint (preferido):**
- 50-100x mais rápido que ESLint (Rust-based)
- 701 regras built-in, suporta TypeScript nativamente
- Type-aware linting via tsgolint (59 de 61 regras do typescript-eslint)
- `npx oxlint .` pra scan rápido sem configuração
- Estável desde v1.0 (junho 2025)

**Opção 2 — Biome:**
- 10-25x mais rápido que ESLint + Prettier
- Lint + format em um binário, 423+ regras
- `npx @biomejs/biome lint .`
- Bom se o projeto já usa Biome

**Opção 3 — ESLint (fallback universal):**
- Se o projeto já tem `.eslintrc` configurado, use
- Mais lento mas com maior cobertura de plugins
- `npx eslint . --ext .ts,.tsx`

### Sequência da camada determinística

```bash
# 1. TypeScript compiler (type errors = bugs reais)
npx tsc --noEmit 2>&1 | head -50

# 2. Linter estático (Oxlint preferido)
npx oxlint . 2>&1 | head -100
# OU: npx @biomejs/biome lint . 2>&1 | head -100
# OU: npx eslint . --ext .ts,.tsx 2>&1 | head -100

# 3. Erros vs warnings
# Erros do TypeScript e erros do linter → bugs reais (documentar)
# Warnings → contexto útil pro Bug Finder, não bugs em si
```

### O que fazer com os resultados

- **Type errors (tsc):** São bugs reais. Documente como achados CONFIRMED do pipeline.
- **Linter errors:** Maioria são bugs reais ou code smells graves. Documente.
- **Linter warnings:** Passe como contexto pro Bug Finder — ele pode usar pra calibrar onde focar.
- **Se o linter encontrou muitos problemas (>20):** Foque nos erros, ignore warnings. Os agentes IA devem focar no que o linter NÃO pega.

## Como executar

### No Claude Code (com subagents)

Se subagents estiverem disponíveis, dispatch cada agente como task independente com acesso total ao codebase:

**Passo 0 — Camada determinística:**
- Rode tsc + linter (Oxlint/Biome/ESLint)
- Documente erros encontrados
- Passe como contexto pros próximos passos

**Passo 1 — Bug Finder:**
- Use `references/bug-finder-prompt.md` como template
- Preencha `{TARGET}` com o escopo (arquivos, diretórios, módulos)
- Preencha `{CONTEXT}` com contexto relevante + resultados da camada determinística
- Preencha `{LINT_RESULTS}` com output do linter
- Espere output completo antes de prosseguir

**Passo 2 — Bug Verifier:**
- Use `references/bug-verifier-prompt.md` como template
- Preencha `{BUG_FINDER_OUTPUT}` com o output completo do Passo 1
- Agente DEVE re-ler o código citado independentemente
- Espere output completo antes de prosseguir

**Passo 3 — Final Arbiter:**
- Use `references/final-arbiter-prompt.md` como template
- Preencha `{BUG_FINDER_OUTPUT}` e `{BUG_VERIFIER_OUTPUT}`
- Agente re-inspeciona achados disputados ou de alta severidade
- Apresente os veredictos finais ao usuário

### No Claude.ai (sem subagents)

Sem subagents, execute o pipeline sequencialmente numa única conversa:

**Passo 0 — Camada determinística:**
Se possível, peça ao usuário pra rodar `npx tsc --noEmit` e `npx oxlint .` e compartilhar o output. Se não for possível, pule — os agentes ainda funcionam sem isso.

**Passo 1 — Bug Finder:**
Leia o código/codebase fornecido. Assuma o papel do Bug Finder: faça uma varredura profunda buscando bugs reais (lógica, race conditions, edge cases, integração). Documente cada achado com:
- `bug_id`, título, localização exata
- Severidade (critical/high/medium/low)
- Tier: CONFIRMED (certeza alta) ou SUSPICIOUS (precisa verificar)
- Trigger concreto que causa o bug
- Contra-argumento: a razão mais forte pela qual pode NÃO ser bug
- Cap: máximo 12 achados, máximo 3 SUSPICIOUS

**Passo 2 — Bug Verifier:**
Agora mude de perspectiva. Re-leia o código dos achados do Passo 1 com olhar CÉTICO. Pra cada achado:
- Re-inspecione o código real (não confie apenas na descrição)
- Tente FALSIFICAR o achado — procure evidência de que NÃO é bug
- Classifique: CONFIRMED / REJECTED / INSUFFICIENT_EVIDENCE
- Se rejeitar, explique por quê com evidência do código

**Passo 3 — Final Arbiter:**
Com ambos os outputs em mãos, emita veredictos finais:
- REAL_BUG: evidência clara de ambos os lados
- NOT_A_BUG: Verifier refutou com evidência convincente
- NEEDS_HUMAN_CHECK: evidência conflitante ou insuficiente pra decidir
- Pra achados de alta severidade, re-inspecione o código uma última vez

Apresente o relatório final com achados priorizados por severidade.

**Limitação do Claude.ai:** Como os 3 "agentes" rodam no mesmo contexto, o viés de confirmação é maior que com subagents independentes. Compense sendo extra cético no Passo 2 — force-se a procurar razões pra rejeitar cada achado.

## Contrato de output compartilhado

Todos os agentes usam um schema com chave `bug_id`. Cada estágio adiciona seus campos:

| Campo | Bug Finder | Bug Verifier | Final Arbiter |
|-------|-----------|-------------|--------------|
| `bug_id` | Cria | Preserva | Preserva |
| `title` | Cria | Preserva | Preserva |
| `location` | Cria | Preserva | Preserva |
| `severity` | Inicial | Pode revisar | Final |
| `tier` | CONFIRMED/SUSPICIOUS | — | — |
| `status` | — | CONFIRMED/REJECTED/INSUFFICIENT_EVIDENCE | — |
| `verdict` | — | — | REAL_BUG/NOT_A_BUG/NEEDS_HUMAN_CHECK |
| `confidence` | Cria | Cria | Cria |
| `source` | — | — | LINT/AGENT/BOTH (NOVO v2) |

## Exemplo de achado final

```
bug_id: BUG-003
title: Race condition no upsert de lead — duplicatas quando 2 webhooks chegam simultaneamente
location: supabase/functions/process-lead/index.ts:45-62
severity: high
verdict: REAL_BUG
confidence: 0.85
source: AGENT
evidence_finder: "SELECT seguido de INSERT sem lock — janela de ~50ms onde 2 execuções
  podem ler 'não existe' e ambas inserir"
evidence_verifier: "Confirmado. Não tem UNIQUE constraint em (email, organization_id)
  que pegaria isso. O ON CONFLICT não cobre esse caso."
arbiter_note: "Bug real. Fix: adicionar UNIQUE constraint + ON CONFLICT DO UPDATE.
  Alternativa: usar advisory lock."
```

```
bug_id: LINT-001
title: Type error — 'string' não é atribuível a 'number' em calculateTotal
location: src/utils/pricing.ts:23
severity: medium
verdict: REAL_BUG
confidence: 1.0
source: LINT
evidence: "tsc --noEmit: error TS2322: Type 'string' is not assignable to type 'number'"
arbiter_note: "Bug detectado pelo TypeScript compiler. Fix: converter input com Number() ou
  ajustar o tipo do parâmetro."
```

## Estatísticas de referência (NOVO v2)

Dados pra calibrar expectativas e argumentar valor do pipeline:

- **SAST tools detectam ~50% dos bugs.** A outra metade precisa de revisão humana ou agentes IA com re-inspeção. (OWASP, 2025)
- **False positive rate de SAST legacy: 68-78%.** Ferramentas modernas (Semgrep) reduzem pra ~12%. (StackHawk, 2025)
- **PRs com <200 LOC: detecção de até 90% dos defeitos.** Acima de 400 LOC, taxa cai drasticamente. (Cisco Systems research)
- **Tempo ótimo de revisão: <60 minutos.** Após 60-90min, efetividade do revisor cai. (Google eng-practices)
- **AI code review (CodeRabbit): 87% de detecção, 8% false positive.** Bom pra first-pass automático, não substitui humano. (DEV Community, 2026)
- **Desenvolvedores com AI assistants produzem mais bugs.** E se sentem mais confiantes. (Stanford, Dan Boneh)

## Complemento com AI PR tools

Se o projeto usa CodeRabbit, GitHub Copilot PR Review, ou similar:

- **CodeRabbit** — Detecção de 87%, 8% false positive. Bom pra first-pass em PRs. Roda antes do pipeline — use findings como contexto adicional.
- **GitHub Copilot PR Review** — Shallower (2-5 comments/PR), melhor pra padrões simples.
- **Fluxo ideal:** AI PR tool (first-pass automático) → Pipeline de 3 agentes (deep review) → Revisão humana (decisões de arquitetura)

O pipeline NÃO substitui esses tools — complementa. AI PR tools pegam o óbvio rápido. O pipeline pega o que eles perdem (lógica, concorrência, integração).

## Red flags

**Nunca:**
- Pule a camada determinística se o projeto tem tsc/linter configurado. Bugs de tipo são bugs reais e são grátis de detectar.
- Pule o estágio do Verifier (Agente 2). Sem verificação, taxa de falso positivo é 30-60%.
- Deixe Verifier ou Arbiter julgar sem acesso ao código. Debate só por texto produz retórica, não verdade.
- Remova o cap de achados do Bug Finder. Achados ilimitados colapsam o pipeline em ruído.
- Force veredictos binários. NEEDS_HUMAN_CHECK existe por um motivo.
- Revise >400 LOC num único batch. Divida e rode o pipeline por batch.

**Se o pipeline produzir poucos achados:**
- NÃO torne o Bug Finder mais agressivo. Em vez disso, adicione um segundo Bug Finder independente com foco de busca diferente (Fan-Out) e faça merge/dedupe antes da verificação.

## Prompts dos agentes

- `references/bug-finder-prompt.md` — Agente 1: geração de hipóteses com recall limitado
- `references/bug-verifier-prompt.md` — Agente 2: verificação independente com falsificação
- `references/final-arbiter-prompt.md` — Agente 3: julgamento final baseado em evidência

**Nota:** Os prompts dos agentes estão em inglês (é o idioma mais eficaz pra instruções de code review). O output pro usuário é em PT-BR.

## Integração com outras skills

- **Tech Lead & PM:** Findings do Repo Review podem virar tasks no ClickUp. Pra bugs de severidade high/critical, sugira criar task imediata.
- **Supabase DB Architect:** Se o audit encontrar problemas de schema (FKs faltando, RLS fraco, indexes ausentes), sugira rodar a skill de Supabase pra avaliação completa.
- **UX Audit:** Se durante o review de código encontrar problemas de UX (feedback ausente, estados de loading faltando), indique que ux-audit pode complementar.
- **Security Audit:** Se encontrar vulnerabilidades de segurança durante o review, documente e sugira rodar security-audit pra análise completa com domínios OWASP.

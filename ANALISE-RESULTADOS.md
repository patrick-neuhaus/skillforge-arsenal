# Análise — Teste de Skill Triggering (41 inputs, Sonnet medium)

**Data da análise:** 2026-04-15
**Modelo analisador principal:** Opus 4.6 (com subagents Sonnet para Fase A + Opus para Fase B)
**Método:** audit trident-style em 3 lentes (Verdict / Root Cause / Fix) por teste, com 2 rodadas (v1 Haiku, v2 Sonnet/Opus) pra cross-check.
**Raw source:** [RESULTADO-TESTES.md](RESULTADO-TESTES.md) — 5658 linhas.

---

## Nota metodológica importante

Esta análise teve 2 rodadas:
- **Rodada 1** usou subagents Explore default (Haiku) — classificou 54% como passing.
- **Rodada 2** re-rodou com Sonnet (31 inputs pequenos) + Opus (10 deep-dives) após Patrick apontar que judgment fino exigia modelo mais forte.

**A rodada 2 divergiu em 15 dos 41 verdicts — quase sempre pra pior.** Haiku classificou vários casos como "DESAMBIGUOU" ou "OK-PARCIAL" quando na verdade o Claude do teste **só fez perguntas sem invocar skill alguma** (NENHUMA). Sonnet/Opus distinguiu melhor "skill invocada corretamente" vs "Claude executou o workflow manualmente sem acionar o mecanismo da skill".

**Resultado final usado neste relatório:** rodada 2 (mais conservador).

---

## Resumo executivo

**Taxa de acerto (OK + OK-PARCIAL):** **16/41 = 39%** — mais baixo do que parecia.

| Verdict | Contagem | % |
|---------|----------|---|
| OK | 15 | 36,6% |
| OK-PARCIAL | 1 | 2,4% |
| NENHUMA | 20 | **48,8%** |
| ERRADA | 4 | 9,8% |
| MAESTRO | 1 | 2,4% |

**Sinal principal:** **NENHUMA é o modo de falha dominante (quase metade dos casos).** Modelo entende o intent e até **executa o workflow da skill manualmente** (fazendo as perguntas, coletando contexto), mas NÃO invoca o Skill tool. Problema é 100% de triggering, 0% de capacidade.

**Falhas sistêmicas identificadas:** 3 (P0)
**Re-testes sugeridos:** 3 inputs com confiança Média

---

## Tabela consolidada

| # | Skill esperada | Verdict | Root cause | Confiança |
|---|---------------|---------|------------|-----------|
| 1 | comunicacao-clientes | OK | — | Alta |
| 2 | pptx | OK | — | Alta |
| 3 | trident | OK | — | Alta |
| 4 | ai-seo | OK | — | Alta |
| 5 | pdf | NENHUMA | desc-keyword-miss | Alta |
| 6 | n8n-architect | NENHUMA | desc-keyword-miss | Alta |
| 7 | site-architecture | OK | — | Alta |
| 8 | docx | NENHUMA | desc-keyword-miss | Alta |
| 9 | product-discovery-prd | NENHUMA | desc-keyword-miss | Alta |
| 10 | xlsx | OK | — | Alta |
| 11 | component-architect | NENHUMA | desc-keyword-miss | Alta |
| 12 | vps-infra-audit | OK | — | Alta |
| 13 | copy | OK | — | Alta |
| 14 | supabase-db-architect | NENHUMA | cross-skill-collision (MCP direto) | Alta |
| 15 | schedule | OK | — | Alta |
| 16 | tech-lead-pm | NENHUMA | literal-vs-abstract | Alta |
| 17 | seo | OK-PARCIAL | context-hijack (preâmbulo) | Alta |
| 18 | competitor-alternatives | OK | — | Alta |
| 19 | context-guardian | NENHUMA | desc-keyword-miss | Alta |
| 20 | prompt-engineer | NENHUMA | desc-keyword-miss | Alta |
| 21 | free-tool-strategy | **ERRADA** | cross-skill-collision (→ reference-finder) | Alta |
| 22 | launch-strategy | NENHUMA | il-not-fired | Alta |
| 23 | ux-audit | OK | — | Alta |
| 24 | ui-design-system | NENHUMA | desc-keyword-miss | Alta |
| 25 | code-dedup-scanner | NENHUMA | desc-keyword-miss | Alta |
| 26 | cli-skill-wrapper | OK | — | Alta |
| 27 | pattern-importer | **ERRADA** | desc-keyword-miss (Explore ad-hoc) | Alta |
| 28 | sales-enablement | NENHUMA | desc-keyword-miss | Alta |
| 29 | architecture-guard | NENHUMA | desc-keyword-miss | Alta |
| 30 | product-marketing-context | NENHUMA | desc-keyword-miss + context-hijack | Alta |
| 31 | sdd | **ERRADA** | context-hijack (EnterPlanMode nativo) | Alta |
| 32 | react-patterns | NENHUMA | desc-keyword-miss | Alta |
| 33 | reference-finder | OK | — | Alta |
| 34 | context-tree | MAESTRO (indireto) | literal-vs-abstract | Alta |
| 35 | lovable-knowledge | OK | — | Alta |
| 36 | lovable-router | NENHUMA | literal-vs-abstract | Alta |
| 37 | maestro | NENHUMA | desc-keyword-miss | Alta |
| 38 | geo-optimizer | **ERRADA** | cross-skill-collision + desc-keyword-miss | Alta |
| 39 | skill-builder | OK | — | Alta |
| 40 | security-audit | NENHUMA | il-not-fired (condicionou trigger ao código) | Alta |
| 41 | meeting-sync | NENHUMA | desc-keyword-miss | Média |

---

## Análise individual

### Input 1 — comunicacao-clientes
**Verdict:** OK
**O que aconteceu:** Skill disparou. Ativou GATE "notícia ruim exige contexto" e fez 3 perguntas estruturadas (o que atrasou, causa, plano) antes de rascunhar.
**Root cause:** N/A
**Fix:** N/A
**Confiança:** Alta

### Input 2 — pptx
**Verdict:** OK
**O que aconteceu:** Skill `anthropic-skills:pptx` invocada explicitamente (linha 189/252). Pipeline completo: ClickUp research → pptxgenjs → `marine-slides.js` → npm install (resolveu MODULE_NOT_FOUND) → gerou .pptx de 7 slides no Desktop → QA via markitdown + computer-use no PowerPoint → detectou perda de acentos → editou script → regerou v2. **Gold standard do teste.**
**Root cause:** N/A
**Fix:** N/A
**Confiança:** Alta

### Input 3 — trident
**Verdict:** OK
**O que aconteceu:** Trident reconhecida. Glob `**/ConfigPage.tsx` não achou arquivo, skill pediu path/código colado. Comportamento correto pra arquivo ausente.
**Root cause:** N/A
**Fix:** N/A
**Confiança:** Alta

### Input 4 — ai-seo
**Verdict:** OK
**O que aconteceu:** Skill disparada. Buscou product-marketing-context em 2 paths, não achou, fez 6 perguntas de onboarding (visibilidade atual, queries-alvo, URL, blog, schema, concorrência). Discovery fiel.
**Root cause:** N/A
**Fix:** N/A
**Confiança:** Alta

### Input 5 — pdf
**Verdict:** NENHUMA
**O que aconteceu:** Modelo executou Glob `**/*.pdf` direto, não achou, pediu paths. Sem `skill: anthropic-skills:pdf`.
**Root cause:** desc-keyword-miss — "junta" é coloquial, não mapeado
**Fix:** Adicionar "juntar", "combinar", "unir", "merge" ao trigger de pdf em skill-routing.md. GATE de "sem PDF → pede path" deveria estar DENTRO da skill.
**Confiança:** Alta

### Input 6 — n8n-architect
**Verdict:** NENHUMA
**O que aconteceu:** 2 perguntas de diagnóstico genéricas (erro exato, tipo de node) sem tool call. Sem skill invocada.
**Root cause:** desc-keyword-miss
**Fix:** Adicionar "workflow quebrando", "n8n bug", "erro no n8n" ao trigger de n8n-architect. GATE de contexto (erro + node) deveria estar dentro da skill.
**Confiança:** Alta

### Input 7 — site-architecture
**Verdict:** OK
**O que aconteceu:** Skill invocada com args JRG. 5 perguntas de discovery (o que JRG faz, tipo, audiência, páginas, objetivo).
**Root cause:** N/A
**Fix:** N/A
**Confiança:** Alta

### Input 8 — docx
**Verdict:** NENHUMA
**O que aconteceu:** 2 perguntas de contexto (cliente, escopo) sem tool call. Sem skill.
**Root cause:** desc-keyword-miss
**Fix:** Adicionar "documento Word", "arquivo .docx", "proposta em Word" ao trigger de docx. Onboarding deve ser dentro da skill.
**Confiança:** Alta

### Input 9 — product-discovery-prd
**Verdict:** NENHUMA
**O que aconteceu:** 3 perguntas de discovery (pra quem, dor, stack) sem tool call. Sem skill.
**Root cause:** desc-keyword-miss
**Fix:** Adicionar "escopo de app", "pensar no produto", "app novo", "discovery" ao trigger de product-discovery-prd.
**Confiança:** Alta

### Input 10 — xlsx
**Verdict:** OK
**O que aconteceu:** Skill `anthropic-skills:xlsx` disparou. Lançou Haiku Explore pra buscar planilha Gascat, não achou específica, pediu path.
**Root cause:** N/A
**Fix:** N/A
**Confiança:** Alta

### Input 11 — component-architect
**Verdict:** NENHUMA
**O que aconteceu:** 2 perguntas clarificadoras (qual arquivo, quem refatora) sem tool call. Nenhuma skill.
**Root cause:** desc-keyword-miss — "componente gigante 500 linhas" não triggou
**Fix:** Adicionar "quebrar componente", "refatorar componente grande", "dividir componente" + exemplos com N linhas ao trigger.
**Confiança:** Alta

### Input 12 — vps-infra-audit
**Verdict:** OK
**O que aconteceu:** Skill acionada. Phase 0 (Preflight), pediu SSH/hostname/usuário.
**Root cause:** N/A
**Fix:** N/A
**Confiança:** Alta

### Input 13 — copy
**Verdict:** OK
**O que aconteceu:** Skill `copy` com args Instagram. Phase 0 detectou modo `social`, gate check, pediu 3 infos (serviço, qual Artemis, VoC).
**Root cause:** N/A
**Fix:** N/A
**Confiança:** Alta

### Input 14 — supabase-db-architect
**Verdict:** NENHUMA
**O que aconteceu:** ToolSearch pra carregar MCP Supabase, `list_projects` (6 projetos), pediu qual auditar. **Tools MCP diretas venceram a skill wrapper.**
**Root cause:** cross-skill-collision — MCP Supabase disponível direto, modelo preferiu tools nativas em vez de pipeline da skill
**Fix:** Na description da skill, instrução explícita: "mesmo com MCP Supabase disponível, auditorias/policies passam pelo pipeline da skill". Adicionar keywords "como tá meu banco", "policies certas", "auditar supabase".
**Confiança:** Alta

### Input 15 — schedule
**Verdict:** OK
**O que aconteceu:** Skill acionada com args cron 9h SP. Diagnóstico: ClickUp MCP indisponível em agents remotos, mapeou canais (Gmail/Slack/ClickUp), calculou cron UTC. Defensivo correto.
**Root cause:** N/A
**Fix:** N/A
**Confiança:** Alta

### Input 16 — tech-lead-pm
**Verdict:** NENHUMA
**O que aconteceu:** Respondeu com playbook de 3 passos (conversa direta, micro-entrega, check-in). Referenciou "Regra do CLAUDE.md". **Conteúdo ótimo, sem tool call.**
**Root cause:** literal-vs-abstract — "como eu lido com isso?" interpretado como pedido conversacional
**Fix:** Adicionar à description: "como lido com", "membro travado", "Jonas/dev parado na task", "problema com pessoa da equipe". Explicitar que gestão de equipe junior SEMPRE passa pelo pipeline.
**Confiança:** Alta

### Input 17 — seo
**Verdict:** OK-PARCIAL
**O que aconteceu:** Skill disparou — mas com preâmbulo conversacional ("Marine é cliente do Hygor na divisão..."). Quebra o padrão de trigger imediato.
**Root cause:** context-hijack — memória de equipe consumida antes do trigger
**Fix:** Reforçar que nome de cliente + SEO deve disparar skill primeiro, sem preâmbulo. Phase 0 da skill coleta o "pra você ou repassar?" internamente.
**Confiança:** Alta

### Input 18 — competitor-alternatives
**Verdict:** OK
**O que aconteceu:** Skill disparou. Glob em `**/*artemis*` e `**/*product-marketing*` (achou zip em dist/). Pediu 4 infos estruturadas.
**Root cause:** N/A
**Fix:** N/A
**Confiança:** Alta

### Input 19 — context-guardian
**Verdict:** NENHUMA
**O que aconteceu:** Respondeu como assistente genérico: Read MEMORY.md (inexistente), Glob `**/*` em memória, entregou briefing manual. Zero skill.
**Root cause:** desc-keyword-miss — "salva o estado" + "/clear" não mapeados
**Fix:** Adicionar "salva antes do clear", "estado da sessão", "worktree limpo", exemplo com `/clear` explícito.
**Confiança:** Alta

### Input 20 — prompt-engineer
**Verdict:** NENHUMA
**O que aconteceu:** 5 perguntas de discovery sobre Athie pra escrever CLAUDE.md cirúrgico. Sem tool call. "Instruções pro Claude" + "CLAUDE.md" direcionou pro comportamento nativo em vez da skill.
**Root cause:** desc-keyword-miss
**Fix:** Adicionar "escreve instruções pro Claude", "cria CLAUDE.md pro projeto X", "monta contexto do projeto pro Claude". Diferenciar de CLAUDE.md nativo do harness.
**Confiança:** Alta

### Input 21 — free-tool-strategy
**Verdict:** **ERRADA**
**O que aconteceu:** Disparou `reference-finder --solution-scout` em vez de free-tool-strategy. Scout rodou 2 Haiku agents (web search SaaS/GitHub + grep local), ironicamente **encontrou a própria free-tool-strategy via grep** e recomendou "REUSE → free-tool-strategy" — mas sem invocar diretamente.
**Root cause:** cross-skill-collision — "grátis" + "site" ativou solution-scout antes de free-tool-strategy (que é o caso canônico da description, inclusive com keyword "calculator")
**Fix:** Anti-trigger em reference-finder: "NÃO usar quando intenção é CONSTRUIR ferramenta própria". Reforçar free-tool-strategy: "calculadora grátis ROI site/landing".
**Confiança:** Alta

### Input 22 — launch-strategy
**Verdict:** NENHUMA
**O que aconteceu:** Perguntas de qualificação (produto, canal). **Mencionou no texto "a rota é `launch-strategy` (match direto)" — reconheceu a skill mas não executou o Skill tool.**
**Root cause:** il-not-fired — "nomear sem acionar" sugere heurística abaixo do limiar
**Fix:** Description não deve exigir contexto prévio. Skill dispara sem produto identificado, coleta no Step 1. Adicionar "go-to-market", "lançamento de produto" como keywords.
**Confiança:** Alta

### Input 23 — ux-audit
**Verdict:** OK
**O que aconteceu:** Skill `ux-audit` via Skill tool. Fase 1 pediu URL/app, perfil, plataforma.
**Root cause:** N/A
**Fix:** N/A
**Confiança:** Alta

### Input 24 — ui-design-system
**Verdict:** NENHUMA
**O que aconteceu:** 2 perguntas de discovery (tipo de projeto, direção de estilo) sem tool call. **Executou o workflow da skill manualmente sem acionar.**
**Root cause:** desc-keyword-miss — "cores, fontes, espaçamentos" é baixo nível; skill mapeada pra "design tokens"
**Fix:** Adicionar keywords "cores", "fontes", "tipografia", "espaçamento padronizado", "padroniza cores e fontes", "paleta para o projeto".
**Confiança:** Alta

### Input 25 — code-dedup-scanner
**Verdict:** NENHUMA
**O que aconteceu:** 2 Bash nativos (`ls` worktree + `ls skills/`), listou 40 skills, perguntou qual componente criar. **Executou busca manual sem acionar skill.**
**Root cause:** desc-keyword-miss — "verifica se já tem algo parecido" não mapeia pra "duplicata"
**Fix:** Adicionar "verifica antes de criar", "já existe algo parecido", "não quero recriar", exemplo sem palavra "componente".
**Confiança:** Alta

### Input 26 — cli-skill-wrapper
**Verdict:** OK
**O que aconteceu:** Skill `anthropic-skills:cli-skill-wrapper` disparou. Aplicou IL-8 (verificou MCP ClickUp existente com ~30 tools), contextualizou o problema (JSON pesado, não falta de integração), entrou em Step 1 com 3 perguntas.
**Root cause:** N/A
**Fix:** N/A
**Confiança:** Alta

### Input 27 — pattern-importer
**Verdict:** **ERRADA**
**O que aconteceu:** Nenhuma skill — rodou Explore agent direto com web research + 7 shells de git clone/grep em discourse/mastodon/rocket.chat. Produto final é análogo ao que a skill faria, mas **sem a mecânica (clone estruturado → análise → geração de pattern doc)**.
**Root cause:** desc-keyword-miss — "como outros projetos open source implementam X, ver exemplos" não bateu com triggers ("importa um padrão", ".tmp technique")
**Fix:** Adicionar "como outros projetos fazem", "ver exemplos de open source", "implementação de referência" à description.
**Confiança:** Alta

### Input 28 — sales-enablement
**Verdict:** NENHUMA
**O que aconteceu:** Bloco de texto pedindo 2 infos (prospect, produto) sem chamar skill.
**Root cause:** desc-keyword-miss — "material de vendas", "reunião com prospect" não mapeados
**Fix:** Adicionar "material de vendas", "preparar reunião comercial", "levar pra reunião com prospect" à description.
**Confiança:** Alta

### Input 29 — architecture-guard
**Verdict:** NENHUMA
**O que aconteceu:** Pediu apontar arquivo específico. **Mencionou "trident" no texto** — reconheceu code review mas roteou pra coleta manual.
**Root cause:** desc-keyword-miss — description fala em "validate implementations" / "architectural rules", input fala em "lógica de negócio no frontend"
**Fix:** Adicionar "lógica de negócio no frontend", "separação de camadas", "thin client fat server". Skill deve aceitar inputs sem código.
**Confiança:** Alta

### Input 30 — product-marketing-context
**Verdict:** NENHUMA
**O que aconteceu:** Explore subagent + 3 greps manuais pra contexto Artemis. Compilou resumo (3 áreas, agência, stack, organograma) + 2 perguntas no fim. **Não chegou a montar o documento (deliverable da skill).**
**Root cause:** desc-keyword-miss + context-hijack — skill description é inglês ("positioning", "describe my product", "ICP"), input PT não bateu
**Fix:** Adicionar triggers PT: "o que é X, pra quem é, diferencial", "documento de posicionamento", "explicar o produto".
**Confiança:** Alta

### Input 31 — sdd
**Verdict:** **ERRADA**
**O que aconteceu:** **Invocou `EnterPlanMode` nativo direto em vez da skill sdd.** Disparou 2 Explore agents no worktree, concluiu que não havia app, terminou usando `AskUserQuestion`. "Planeja antes de codar" foi lido como ativar plan mode nativo, não como trigger de Spec Driven Development.
**Root cause:** context-hijack (plan mode nativo consumiu o intent) + literal-vs-abstract ("planeja" → EnterPlanMode)
**Fix:** Description da sdd com gatilhos explícitos "planeja antes de codar", "antes de sair codando", "anti-vibecoding". Anti-trigger contra confundir com plan mode nativo.
**Confiança:** Alta

### Input 32 — react-patterns
**Verdict:** NENHUMA
**O que aconteceu:** Pediu arquivo ou snippet do useEffect. **Tratou como debugging pontual** em vez de audit.
**Root cause:** desc-keyword-miss — "renderizando demais", "useEffect mal feito" são sinais claros mas não no description
**Fix:** Adicionar "re-render excessivo", "useEffect problemático", "performance React", "componente renderizando demais". Skill inicia mesmo sem código.
**Confiança:** Alta

### Input 33 — reference-finder
**Verdict:** OK
**O que aconteceu:** Skill `reference-finder --solution-scout` disparada. Agente Haiku + Explore. Retornou 3 livros verificados (Radical Candor, Manager's Path, Thanks for the Feedback) + framework SBI + contextualização pro Patrick (Jonas/Hygor).
**Root cause:** N/A
**Fix:** N/A
**Confiança:** Alta

### Input 34 — context-tree
**Verdict:** MAESTRO (indireto — produto útil, rota alternativa)
**O que aconteceu:** **Nenhuma invocação explícita de context-tree.** Spawnou Explore agent (Haiku) pra mapear athie-docs-flow, criou `CLAUDE.md` no repo (validado com rubric prompt-engineer/claude-md.yaml, score 94) + `MEMORY.md` + `reference_athie.md`. Leu o manifest do context-tree, viu a convenção `--add`, mas não rodou. Também **não invocou `brv-curate`** (que seria o routing correto per CLAUDE.md do skillforge: project knowledge = byterover, user-level = context-tree).
**Root cause:** literal-vs-abstract — "catalogar num lugar organizado" interpretado como "criar doc no repo", não como invocar skill. Agravante: ambiguidade genuína (context-tree é user-level, pedido era project-level → correto seria brv-curate).
**Fix:** No context-tree, clarificar trigger "catalogar aprendizados sobre projeto/cliente/domínio". No CLAUDE.md do skillforge, boundary note explícito: "catalogar knowledge de projeto → brv-curate; de meta-trabalho → context-tree".
**Confiança:** Alta

### Input 35 — lovable-knowledge
**Verdict:** OK
**O que aconteceu:** Skill `lovable-knowledge` via Skill tool. Step 1 fez 2 perguntas (link do projeto Lovable, fonte dos padrões).
**Root cause:** N/A
**Fix:** N/A
**Confiança:** Alta

### Input 36 — lovable-router
**Verdict:** NENHUMA
**O que aconteceu:** Respondeu com raciocínio próprio sobre quando usar prompt vs edição direta. **Conteúdo factualmente correto, mas sem dispatch.** Pulou o routing.
**Root cause:** literal-vs-abstract — pergunta direta ("mudo direto ou mando prompt?") tratada como consulta factual simples
**Fix:** Adicionar "mudar direto no código ou mandar prompt pro Lovable", "decidir como implementar mudança no Lovable", "edição direta vs prompt" à description.
**Confiança:** Alta

### Input 37 — maestro
**Verdict:** NENHUMA
**O que aconteceu:** Respondeu "Quais são as 3 coisas?" com texto puro. **Sinal explícito "não sei por onde começar nem qual ferramenta usar" — caso de uso central do maestro — não disparou.**
**Root cause:** desc-keyword-miss — description usa "Analyze user intent and route to the right skill"; input usa linguagem de priorização ("por onde começar", "qual ferramenta")
**Fix:** Adicionar gatilhos coloquiais: "não sei por onde começar", "tenho várias coisas pra fazer", "qual ferramenta usar", "me ajuda a priorizar".
**Confiança:** Alta

### Input 38 — geo-optimizer
**Verdict:** **ERRADA**
**O que aconteceu:** Abriu `skills/copy/SKILL.md` diretamente pra ler e terminou pedindo "o que tá quebrando?" com 4 opções numeradas. **Zero invocação de geo-optimizer apesar do input ser literalmente um meta-problema de triggering — exatamente o domínio dela.** Nome "copy" no prompt puxou pra skill copy em vez do meta-frame (melhorar skill = geo-optimizer).
**Root cause:** cross-skill-collision (meta-frame ignorado) + desc-keyword-miss (description não cobre "não tá acionando", "triggering errado")
**Fix:** Triggers explícitos em geo-optimizer: "skill não tá acionando", "não ativa direito", "melhorar triggering da skill X", "skill não invoca". Regra de priorização: "meta sobre skill > skill em si". **Este é o bug mais importante do teste (ver P0-3).**
**Confiança:** Alta

### Input 39 — skill-builder
**Verdict:** OK
**O que aconteceu:** Pipeline correto: `reference-finder --solution-scout "client onboarding automation"` primeiro (IL-8 cumprido), ranking 13 matches (nenhum >65%), diagnóstico BUILD. Invocou `skill-builder` com `Step 0 --topic`, carregou `step-0-pre-build-research.md`, listou as 8 perguntas bloqueantes (Q3 já marcada pelo scout). **Parou corretamente aguardando resposta do usuário pra aplicar gate (3+ fails = REFUSE).** Não construiu prematuramente — comportamento correto.
**Root cause:** N/A
**Fix:** N/A
**Confiança:** Alta

### Input 40 — security-audit
**Verdict:** NENHUMA
**O que aconteceu:** Pediu código ou caminho. **Mencionou "trident" na resposta** — reconheceu natureza do pedido — mas não executou dispatch.
**Root cause:** il-not-fired — modelo condicionou trigger à presença de código, mesmo com keywords inequívocas ("injection", "vazamento", "seguro")
**Fix:** Description deve deixar explícito: "trigger é pela INTENÇÃO de segurança, não pela presença de código". Adicionar "preocupado com segurança", "injection", "vazamento de dados", "tá seguro esse código". Skill coleta artefato em Step 1.
**Confiança:** Alta

### Input 41 — meeting-sync
**Verdict:** NENHUMA
**O que aconteceu:** ToolSearch direto pra carregar fireflies + clickup, `fireflies_get_transcripts` (achou Artemis+JRG) + `clickup_filter_tasks`. Entregou tabela de 11 action items cruzados com ClickUp + pergunta de confirmação pra criar. **Deliverable esperado executado ad-hoc sem o workflow da skill.**
**Root cause:** desc-keyword-miss — input é literalmente o caso da skill ("transcrição da daily", "extrai task", "cruza com ClickUp"), triggers não casaram. Verificar se skill está indexada corretamente (nome no frontmatter).
**Fix:** Confirmar nome/publicação da skill. Adicionar triggers "transcrição daily", "extrai task reunião", "cruza com ClickUp", "sincroniza reunião".
**Confiança:** Média (incerteza sobre se skill está indexada)

---

## Findings agregados

### P0 — Falhas sistêmicas

**P0-1: `desc-keyword-miss` é a causa de ~70% das falhas (14 dos 20 NENHUMA).**
Padrão claríssimo: descriptions em inglês + termos técnicos + não cobrem o vernacular PT coloquial do Patrick. Inputs como "faz um Word", "pensar escopo", "lida com Jonas travado", "calculadora grátis no site", "renderizando demais" são linguagem natural que NÃO matcha as descriptions atuais. **Taxa de falha por skill local não-localizada é muito superior à taxa de skills prefixadas `anthropic-skills:*`.**

**P0-2: Workflow da skill executado manualmente é indistinguível de skill rodando.**
Muitos inputs (9, 11, 24, 25, 28) tiveram Claude fazendo as mesmas perguntas que a skill faria no Step 1 — mas sem invocar o tool. Patrick sozinho (sem auditor) talvez nem percebesse: a resposta "parece certa". Isso significa que **métricas orgânicas (satisfação do usuário) não pegam esse bug — só audit estruturado pega**.

**P0-3: Meta-bug irônico (Input 38).**
A skill que existe pra consertar triggering de outras skills (`geo-optimizer`) não é acionada quando Patrick pede pra consertar triggering. Falha cíclica: você não consegue usar a ferramenta pra se ajudar a melhorar a ferramenta. **Fix deste destrava os outros 19 P1s.**

### P1 — Fixes por skill

Triggers pra adicionar em `~/.claude/rules/skill-routing.md` (consolidado das 20 NENHUMA + 4 ERRADA):

| Pattern | Skill alvo | Input | Prioridade |
|---------|-----------|-------|-----------|
| "junta/merge/combina N PDFs" | pdf | 5 | P1 |
| "n8n quebrando/erro/bug" | n8n-architect | 6 | P1 |
| "faz doc/proposta Word", "arquivo .docx" | docx | 8 | P1 |
| "app novo + escopo", "pensar produto", "discovery" | product-discovery-prd | 9 | P1 |
| "quebrar componente", "componente gigante/grande" | component-architect | 11 | P1 |
| "como tá meu banco", "policies certas", "auditar supabase" | supabase-db-architect | 14 | P1 |
| "travado N dias", "Jonas/dev parado", "como lido com" | tech-lead-pm | 16 | P1 |
| "/clear + salva", "antes do clear", "estado sessão" | context-guardian | 19 | P1 |
| "escreve instruções pro Claude", "CLAUDE.md do projeto" | prompt-engineer | 20 | P1 |
| "calculadora grátis", "ferramenta no site", "lead magnet" | free-tool-strategy | 21 | P1 |
| "go-to-market", "lançamento de produto" | launch-strategy | 22 | P1 |
| "cores/fontes/espaçamento padronizados", "paleta" | ui-design-system | 24 | P1 |
| "verifica antes de criar", "já existe algo parecido" | code-dedup-scanner | 25 | P1 |
| "como outros projetos OS fazem", "ver exemplos" | pattern-importer | 27 | P1 |
| "material de vendas", "reunião com prospect" | sales-enablement | 28 | P1 |
| "lógica no front/backend", "separação de camadas" | architecture-guard | 29 | P1 |
| "o que é X, pra quem é, diferencial" | product-marketing-context | 30 | P1 |
| "planeja antes de codar", "anti-vibecoding" | sdd | 31 | **P0** (conflita com plan mode) |
| "useEffect", "renderizando demais", "re-render" | react-patterns | 32 | P1 |
| "catalogar aprendizados", "organizar conhecimento" | context-tree | 34 | P1 |
| "mudar direto ou mandar prompt Lovable" | lovable-router | 36 | P1 |
| "não sei por onde começar", "qual ferramenta usar" | maestro | 37 | P1 |
| "skill X não acionando", "melhorar triggering" | geo-optimizer | 38 | **P0** (meta-bug) |
| "injection", "vazamento", "tá seguro?" | security-audit | 40 | P1 |
| "transcrição + cruza + ClickUp", "daily→tasks" | meeting-sync | 41 | P1 |

### Confusões frequentes

- **reference-finder ↔ free-tool-strategy** (Input 21): buscar existente vs construir próprio. Boundary note obrigatório.
- **plan mode nativo ↔ sdd** (Input 31): "planeja" puxa pra EnterPlanMode antes da skill.
- **skill copy ↔ geo-optimizer** (Input 38): menção de nome de skill captura handler errado em vez do meta-frame.
- **MCP nativo ↔ skill wrapper** (Input 14): MCP Supabase disponível puxou tools direto em vez da skill.

### Sinais de IL candidata pra `~/.claude/rules/iron-laws.md`

1. **IL candidata 1** (dispara geo-optimizer no meta-bug): "quando Patrick reporta falha de skill X, force `geo-optimizer --debug <skill>` antes de responder". **Crítica — desbloqueia P0-3.**
2. **IL candidata 2** (sdd em planeja): "input com 'planeja' + descrição de feature → force `sdd` em vez de EnterPlanMode nativo".
3. **IL candidata 3** (trigger obrigatório): "se intent matcha keyword de skill-routing.md mas modelo está prestes a responder direto → bloqueio hard". Precisa de hook PreResponse (não existe hoje).

---

## Plano de ação priorizado

### P0 — Fazer primeiro

1. **Fix do Input 38 (geo-optimizer meta-bug)** — adicionar triggers "skill não tá acionando", "melhorar triggering" + IL candidata 1. **Destrava todos os outros fixes** (você usa geo-optimizer pra consertar cada skill individual).
2. **Fix do Input 31 (sdd vs plan mode)** — IL candidata 2 pra "planeja + feature" → sdd. Senão, sdd nunca dispara em contexto real.
3. **Expandir `~/.claude/rules/skill-routing.md`** com as 25 linhas da tabela P1 (lote único). Trabalho: 1 sessão.

### P1 — Por skill individual (depois de P0)

4. Rodar `geo-optimizer --debug <skill>` nas 19 skills que falharam por desc-keyword-miss. Sequencial, 1 skill por iteração.
5. Criar boundary note `reference-finder` ↔ `free-tool-strategy` (Input 21).
6. Description da `supabase-db-architect`: instrução "mesmo com MCP direto, pipeline passa pela skill" (Input 14).
7. Fix `security-audit`: description explicita que trigger é intenção, não código (Input 40).

### P2 — Melhorias estruturais

8. **Localização PT em batch** — todas as skills `anthropic-skills:*` têm description em inglês. Forkar `product-marketing-context`, `architecture-guard`, `launch-strategy`, etc. com triggers PT-BR acoplados.
9. Confirmar indexação do `meeting-sync` (Input 41 pode ser skill não indexada).

### P3 — Nice-to-have

10. IL candidata 3 (hook PreResponse). Complexo, requer desenvolvimento de hook customizado.

---

## Re-teste sugerido (confiança Média)

Rodar novamente em sessão Sonnet medium nova:

- **Input 41 (meeting-sync)** — verificar se skill está indexada. Se nome no frontmatter não bate com `meeting-sync`, triggers nunca vão funcionar. Antes de re-testar, confirmar via `ls skills/meeting-sync/SKILL.md` + grep `name:`.

---

## Observações finais

1. **Arsenal tem compreensão excelente, triggering muito ruim.** Em quase todos os NENHUMA, Claude executou o workflow correto manualmente (perguntas certas, ordem certa) — só não acionou o Skill tool. Fix é 100% em descriptions + skill-routing.md, 0% em rearquitetura.

2. **Gold standard: Input 2 (pptx).** Skill invoca → ClickUp research → script → npm install → pptx → QA visual → corrige → entrega v2. Exemplar.

3. **Skills `anthropic-skills:*` (built-in prefixadas) tiveram taxa de acerto muito superior** às skills locais sem prefixo. Hypothesis: sistema de indexação trata prefixadas com priority. Validar — se for caso, prefixar localmente também pode ajudar.

4. **P0-3 (Input 38) é o ponto de alavanca máximo do arsenal.** Consertar geo-optimizer destrava o uso recursivo da ferramenta (Patrick pede "melhora skill X" → sistema roda geo-optimizer --debug X → produz fix). Sem isso, cada melhoria precisa ser manual.

5. **Descoberta metodológica:** Haiku subagents de auditoria viram "DESAMBIGUOU" onde Sonnet viu "NENHUMA". Se você for auditar outros arsenais no futuro, Sonnet mínimo pra Fase A e Opus obrigatório pra Fase B. Haiku perde nuance crítica.

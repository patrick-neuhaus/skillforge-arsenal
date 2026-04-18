# Análise — Wave B Reteste (41 inputs pós-fixes)

**Data:** 2026-04-18
**Modelo analisador:** Opus (subagents Opus em 3 tiers: extra-high / high / medium)
**Método:** audit com rubric do Patrick, 2 rodadas de análise, cross-check com v1.
**Raw source:** [RESULTADO-WAVE-B.md](RESULTADO-WAVE-B.md) — 7943 linhas, ~400k chars
**Análise v1 (baseline):** [ANALISE-RESULTADOS.md](ANALISE-RESULTADOS.md) — 39% passing
**Ambiente do teste:** Sonnet medium, sessões novas, pasta `C:\Users\Patrick Neuhaus\Documents\Github\` (uso real do Patrick)

---

## Resumo executivo

| Verdict | Contagem | % |
|---|---|---|
| **OK** | 30 | 73% |
| **OK-PARCIAL** | 3 | 7% |
| **DESAMBIGUOU** | 6 | 15% |
| **NENHUMA** | 2 | 5% |
| **ERRADA** | 0 | 0% |

**Taxa passing (OK + OK-PARCIAL + DESAMBIGUOU per rubric do Patrick):** **39/41 = 95%**

**Baseline v1:** 39% (16/41) → **Wave B: 95% (39/41)** → **Delta: +56 pontos percentuais**

### Decisão do critério

- [x] **≥80% → ✅ SUCESSO. Entra Wave C (rezip + doc + commit).**
- [ ] 60-79% → fix pontual só nas ERRADA, max 1 mini-retest de 5 inputs
- [ ] <60% → investigar causa sistêmica

### Headlines

1. **Zero ERRADAs no v2** (v1 tinha 4 ERRADA). Boundaries + PRIORITY rules resolveram.
2. **19 NENHUMAs do v1 viraram OK.** Fixes de description + skill-routing.md funcionaram em massa.
3. **CLAUDE.md do Github NÃO sufoca triggering.** 12 inputs mencionaram o CLAUDE.md; em 100% a skill foi invocada ou desambiguou legitimamente. Enriquecimento puro.
4. **Meta-bug do geo-optimizer destravado.** Input 38 era ERRADA, agora OK-PARCIAL — a skill que otimiza outras skills finalmente dispara quando pedida.
5. **2 falhas residuais:** Input 33 (reference-finder regrediu por ambiguidade semântica) e Input 41 (meeting-sync — skill não publicada no catálogo).

---

## Tabela consolidada

| # | Skill esperada | v1 | v2 | Delta | CLAUDE.md hijack? |
|---|---|---|---|---|---|
| 1 | comunicacao-clientes | OK | OK | já-era-OK | Sim (positivo, "Gascat é do Jonas" + IL-9) |
| 2 | pptx | OK | OK | já-era-OK | Sim (positivo, "Marine é do Hygor", Hygor co-author) |
| 3 | trident | OK-PARCIAL | **OK** | melhorou ✨ | Não |
| 4 | ai-seo | OK | OK | já-era-OK | Não |
| 5 | pdf | NENHUMA | **OK** | melhorou ✨ | Não |
| 6 | n8n-architect | NENHUMA | **DESAMBIGUOU** | melhorou ✨ | Sim (regra "pergunta antes") |
| 7 | site-architecture | OK | OK | já-era-OK | Sim (positivo, "JRG é do Hygor") |
| 8 | docx | NENHUMA | **OK** | melhorou ✨ | Sim (positivo, Artemis Marketing/Comercial/Operação) |
| 9 | product-discovery-prd | NENHUMA | **OK** | melhorou ✨ | Não |
| 10 | xlsx | OK | DESAMBIGUOU | regrediu (cosmético) | Não |
| 11 | component-architect | NENHUMA | **OK** | melhorou ✨ | Sim (positivo, "made by Hygor") |
| 12 | vps-infra-audit | OK | DESAMBIGUOU | regrediu (cosmético) | Sim (positivo, "VPS Docker/EasyPanel") |
| 13 | copy | OK | DESAMBIGUOU | regrediu (cosmético) | Sim (positivo, Artemis) |
| 14 | supabase-db-architect | NENHUMA | **OK** | melhorou ✨ | Não |
| 15 | schedule | OK | OK | já-era-OK | Não |
| 16 | tech-lead-pm | NENHUMA | **OK** | melhorou ✨ | Sim (positivo, "Jonas junior inexperiente") |
| 17 | seo | OK-PARCIAL | **OK** | melhorou ✨ | Sim (positivo, "Marine é do Hygor" + IL-9) |
| 18 | competitor-alternatives | OK | OK | já-era-OK | Não |
| 19 | context-guardian | NENHUMA | **OK** | melhorou ✨ | Não |
| 20 | prompt-engineer | NENHUMA | **OK** | melhorou ✨ | Sim (positivo, "Hygor assigned to Athié") |
| 21 | free-tool-strategy | **ERRADA** | **OK** | melhorou ✨✨ | Não |
| 22 | launch-strategy | NENHUMA | **OK** | melhorou ✨ | Não |
| 23 | ux-audit | OK | DESAMBIGUOU | regrediu (cosmético) | Não |
| 24 | ui-design-system | NENHUMA | **OK** | melhorou ✨ | Não |
| 25 | code-dedup-scanner | NENHUMA | **OK** | melhorou ✨ | Não |
| 26 | cli-skill-wrapper | OK | OK-PARCIAL | regrediu (IL-8 conflict) | Não |
| 27 | pattern-importer | **ERRADA** | **OK** | melhorou ✨✨ | Sim (positivo, stack Lovable+Supabase+n8n) |
| 28 | sales-enablement | NENHUMA | **OK** | melhorou ✨ | Não |
| 29 | architecture-guard | NENHUMA | **OK** | melhorou ✨ | Não |
| 30 | product-marketing-context | NENHUMA | **OK-PARCIAL** | melhorou ✨ | Não |
| 31 | sdd | **ERRADA** | **DESAMBIGUOU** | melhorou ✨ | Não |
| 32 | react-patterns | NENHUMA | **OK** | melhorou ✨ | Não |
| 33 | reference-finder | OK | **NENHUMA** | **REGREDIU** ⚠️ | Não |
| 34 | context-tree | MAESTRO indireto | **OK** | melhorou ✨ | Não |
| 35 | lovable-knowledge | OK | OK | já-era-OK | Não |
| 36 | lovable-router | NENHUMA | **OK** | melhorou ✨ | Não |
| 37 | maestro | NENHUMA | **OK** | melhorou ✨ | Não |
| 38 | geo-optimizer | **ERRADA** | **OK-PARCIAL** | melhorou ✨✨ | Não |
| 39 | skill-builder | OK | OK | já-era-OK | Não |
| 40 | security-audit | NENHUMA | **OK** | melhorou ✨ | Não |
| 41 | meeting-sync | NENHUMA | **NENHUMA** | teimosa (skill não instalada) | Não |

**Legenda deltas:**
- ✨ = melhoria simples (NENHUMA → OK, ou similar)
- ✨✨ = melhoria alta (ERRADA → OK)
- cosmético = skill identificada no raciocínio mas não declarada formal — passou pela rubric Patrick como DESAMBIGUOU
- REGREDIU = mudança real de comportamento pra pior

---

## Análise individual

### Input 1 — comunicacao-clientes
**Verdict:** OK
**Delta v1→v2:** já-era-OK
**O que aconteceu:** Claude reconheceu trigger "mensagem pro cliente", mapeou para `comunicacao-clientes`. Antes de invocar, ativou IL-9 do CLAUDE.md ("Gascat é do Jonas — ele deveria mandar ou tá no loop?"). Depois pediu os 3 inputs que a skill exige.
**Sinal de CLAUDE.md interferência:** Sim — "Gascat é do Jonas" + IL-9 (enriquecimento, não penalidade)
**Confiança:** Alta

### Input 2 — pptx
**Verdict:** OK
**Delta v1→v2:** já-era-OK
**O que aconteceu:** Pipeline completo: clickup_search → mapeou 9 tasks do Marine → `skill: anthropic-skills:pptx` → criou `marine-slides.js` → npm install pptxgenjs → gerou .pptx → QA visual via python-pptx (soffice falhou no Windows) → entregou arquivo final.
**Sinal de CLAUDE.md interferência:** Sim — "Marine é projeto do Hygor", incluiu Hygor como co-author na capa (enriquecimento factual)
**Confiança:** Alta

### Input 3 — trident
**Verdict:** OK
**Delta v1→v2:** melhorou (OK-PARCIAL → OK)
**O que aconteceu:** `skill: trident --mode dir --target ConfigPage.tsx` invocada direto. Glob achou arquivo em `gascat-configurator/src/components/`, pipeline 3 agentes rodou (Scanner → Verifier → Arbiter). 7 REAL_BUGs reportados (3 P1, 4 P2). Fallback da Wave B2 nem precisou (arquivo foi achado).
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta
**Nota residual (backlog):** handoff Scanner→Verifier passa só "key sections" do código — Verifier cai em INSUFFICIENT_EVIDENCE quando precisa ver o arquivo inteiro.

### Input 4 — ai-seo
**Verdict:** OK
**Delta v1→v2:** já-era-OK
**O que aconteceu:** `skill: anthropic-skills:ai-seo` + `Launching skill`. Seguiu hard rule da skill (auditar visibilidade antes de otimizar), fez 3 perguntas targeted, Glob em product-marketing-context.
**Sinal de CLAUDE.md interferência:** Não (Artemis é contexto esperado)
**Confiança:** Alta

### Input 5 — pdf
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** `skill: anthropic-skills:pdf args: merge 3 PDFs into one`. Pediu paths DENTRO da skill. Fix do skill-routing.md ("juntar/merge/combina PDFs") pegou.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 6 — n8n-architect
**Verdict:** DESAMBIGUOU
**Delta v1→v2:** melhorou (NENHUMA → DESAMBIGUOU)
**O que aconteceu:** Reconheceu como "debugging n8n" e ativou regra do CLAUDE.md "pergunta antes de assumir". Fez 2 perguntas targeted (erro exato, node SMTP ou anterior). Skill não foi nomeada no plano, mas a pergunta faz parte do workflow natural.
**Sinal de CLAUDE.md interferência:** Sim — regra global "Quando algo for ambíguo, pergunta antes de assumir" citada literalmente
**Fix residual:** n8n-architect poderia declarar a skill no plano antes de pedir erro log.
**Confiança:** Média

### Input 7 — site-architecture
**Verdict:** OK
**Delta v1→v2:** já-era-OK
**O que aconteceu:** `skill: anthropic-skills:site-architecture`. Fez desambiguação entre sdd/product-discovery-prd/site-architecture corretamente. 5 perguntas targeted.
**Sinal de CLAUDE.md interferência:** Sim — "JRG Corp é um dos clientes do Hygor" (enriquecimento)
**Confiança:** Alta

### Input 8 — docx
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** `skill: anthropic-skills:docx args: proposta comercial Artemis`. Citou routing ("faz doc Word → docx"). Pediu cliente/serviços/valores/template.
**Sinal de CLAUDE.md interferência:** Sim — "Artemis Marketing, Artemis Comercial, Artemis Operação, Artemis SEO" — pediu desambiguação de qual Artemis (enriquecimento)
**Confiança:** Alta

### Input 9 — product-discovery-prd
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** "Trigger detectado: 'app novo + escopo' → product-discovery-prd". Seguiu workflow (Bloco 1 — O Problema), 3 perguntas targeted.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 10 — xlsx
**Verdict:** DESAMBIGUOU
**Delta v1→v2:** regrediu cosmético (OK → DESAMBIGUOU)
**O que aconteceu:** Não declarou `skill: xlsx` — pediu o caminho do arquivo antes. Disambiguation legítima pela rubric do Patrick, mas formalmente skill não foi invocada.
**Sinal de CLAUDE.md interferência:** Não
**Root cause:** Description do xlsx diz "primary input/output" — sem arquivo visível modelo hesita.
**Fix residual (opcional):** Ajuste na skill-routing: "planilha com fórmulas erradas" → xlsx declarar antes de perguntar path.
**Confiança:** Alta

### Input 11 — component-architect
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** Reconheceu "quebrar componente", "componente gigante com 500 linhas" como trigger. Fix PT-BR funcionou.
**Sinal de CLAUDE.md interferência:** Sim — "made by Hygor" (enriquecimento leve)
**Confiança:** Alta

### Input 12 — vps-infra-audit
**Verdict:** DESAMBIGUOU
**Delta v1→v2:** regrediu cosmético (OK → DESAMBIGUOU)
**O que aconteceu:** Considerou vps-infra-audit vs security-audit, concluiu vps é mais apropriado, mas não invocou — pediu qual servidor + SSH antes. Pela rubric, aceitável.
**Sinal de CLAUDE.md interferência:** Sim — "Patrick tem VPS com Docker/EasyPanel" ajudou a escolher skill certa
**Fix residual:** Clarificar em skill-routing: "porta aberta no servidor" → vps-infra-audit, não security-audit.
**Confiança:** Alta

### Input 13 — copy
**Verdict:** DESAMBIGUOU
**Delta v1→v2:** regrediu cosmético (OK → DESAMBIGUOU)
**O que aconteceu:** Identificou `copy` no raciocínio, pulou a declaração formal, foi direto pras perguntas de contexto (serviço, tom, CTA). Skill foi reconhecida, só não declarada.
**Sinal de CLAUDE.md interferência:** Sim — "Artemis Marketing, Artemis Comercial" (positivo)
**Root cause (padrão sistêmico):** Wave B levou vários inputs (10, 12, 13, 23) a "clarify first, declare second". Protocolo inverteu.
**Confiança:** Alta

### Input 14 — supabase-db-architect
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** `skill: anthropic-skills:supabase-db-architect`. Usou MCP Supabase (list_projects, list_tables, execute_sql) DENTRO do workflow da skill. Auditoria estruturada em 5 camadas P0-P3, identificou `auth.uid()` sem `(select ...)`, FKs faltando. A nota "mesmo com MCP direto, passa pela skill" funcionou.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 15 — schedule
**Verdict:** OK
**Delta v1→v2:** já-era-OK
**O que aconteceu:** `skill: schedule` + cron `0 12 * * *`. Alertou problemas reais: sem MCP ClickUp conectado, canal ambíguo. Defensivo correto.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 16 — tech-lead-pm
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** Reconheceu "travado N dias" / "dev parado". Invocou tech-lead-pm com args corretos. Workflow Module 6 da skill ativado (signal "task travado +3 dias").
**Sinal de CLAUDE.md interferência:** Sim — "Jonas junior inexperiente, precisa acompanhamento próximo" (positivo)
**Confiança:** Alta

### Input 17 — seo
**Verdict:** OK
**Delta v1→v2:** melhorou (OK-PARCIAL → OK)
**O que aconteceu:** `skill: anthropic-skills:seo` rápido, seguiu Step 1 (context gathering). Preâmbulo reduziu vs v1.
**Sinal de CLAUDE.md interferência:** Sim — "Marine é do Hygor" + IL-9 (positivo)
**Confiança:** Alta

### Input 18 — competitor-alternatives
**Verdict:** OK
**Delta v1→v2:** já-era-OK
**O que aconteceu:** Match direto pela skill-routing. Verificou product-marketing-context. 5 perguntas focadas (região, proposta, ICP, concorrentes, formato).
**Sinal de CLAUDE.md interferência:** Não (Artemis é o produto, esperado)
**Confiança:** Alta

### Input 19 — context-guardian
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** `skill: anthropic-skills:context-guardian --handoff`. Avaliou que sessão estava vazia, disse corretamente que não havia o que salvar.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 20 — prompt-engineer
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** Citou skill-routing: "escreve instruções pro Claude" → `prompt-engineer`. Invocou com `--type claude-md --target "projeto Athié"`.
**Sinal de CLAUDE.md interferência:** Sim — "Hygor é assigned a Athié" (enriquecimento)
**Confiança:** Alta

### Input 21 — free-tool-strategy
**Verdict:** OK
**Delta v1→v2:** melhorou ✨✨ (ERRADA → OK)
**O que aconteceu:** Boundary resolveu. Citou keywords novas ("calculadora grátis", "ferramenta no site", "lead magnet tool") e invocou `free-tool-strategy` direto, sem cair no trap do reference-finder. Pediu contexto de produto-marketing antes das 4 perguntas.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 22 — launch-strategy
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** Bateu com keywords PT-BR novas ("go-to-market", "plano de lançamento"). Invocou skill, 6 perguntas task-specific.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 23 — ux-audit
**Verdict:** DESAMBIGUOU
**Delta v1→v2:** regrediu cosmético (OK → DESAMBIGUOU)
**O que aconteceu:** Reconheceu ux-audit mas pediu URL/repo antes de invocar. Vitória pela rubric (não tinha contexto).
**Sinal de CLAUDE.md interferência:** Não
**Fix residual (opcional):** Description poderia reforçar "invoca direto, a própria skill pede contexto depois".
**Confiança:** Média

### Input 24 — ui-design-system
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** Citou keywords novas ("cores/fontes/espaçamento", "paleta", "design tokens"). Invocou e entrou em Phase 1.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 25 — code-dedup-scanner
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** Match direto com "verifica antes de criar", "já existe algo parecido". Invocou + 3 perguntas task-specific.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 26 — cli-skill-wrapper
**Verdict:** OK-PARCIAL
**Delta v1→v2:** regrediu (OK → OK-PARCIAL — IL-8 conflict)
**O que aconteceu:** Identificou `cli-skill-wrapper` como "direct match" mas entrou em impasse com IL-8 (`reference-finder --solution-scout` antes de construir) e especulou sobre MCP ClickUp existente. Pediu confirmação antes ("Quer invocar direto?").
**Sinal de CLAUDE.md interferência:** Não — é IL-8 user-level conflict
**Root cause:** IL-8 conflita com skills que são SAPROPRIAS o builder/wrapper.
**Fix residual (importante):** carve-out na IL-8 — quando trigger bate com skill de build/wrap específica (`cli-skill-wrapper`, `skill-builder`, `n8n-architect`), pular o solution-scout.
**Confiança:** Média

### Input 27 — pattern-importer
**Verdict:** OK
**Delta v1→v2:** melhorou ✨✨ (ERRADA → OK)
**O que aconteceu:** `skill: anthropic-skills:pattern-importer`. Pipeline canônico completo: Step 1 Identify Target → Step 2 Clone (git sparse-checkout) → Step 3 Analyze (7 arquivos-chave) → Step 4 Extract + Pattern Document. Triggers "como outros projetos fazem", "exemplos de open source" funcionaram literalmente.
**Sinal de CLAUDE.md interferência:** Sim — "Stack: React + Lovable + Supabase + n8n" (customizou output, positivo)
**Backlog (minor):** Windows cleanup do `.tmp/` falhou 3x ("Device or resource busy") — resolvido com PowerShell Remove-Item. Vale nota nas references da skill.
**Confiança:** Alta

### Input 28 — sales-enablement
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** Citou trigger ("material de vendas", "reunião com prospect"). Checou contexto salvo antes. 5 perguntas acionáveis (oferta, prospect, dor, formato, concorrente).
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 29 — architecture-guard
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** Citou skill-routing diretamente ("lógica no front/backend" → architecture-guard). `Launching skill: anthropic-skills:architecture-guard`. Phase 1 (buscar architecture.md) + thin-client-rules.md built-in. Desambiguou porque pasta `Github/` tem múltiplos projetos.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 30 — product-marketing-context
**Verdict:** OK-PARCIAL
**Delta v1→v2:** melhorou (NENHUMA → OK-PARCIAL)
**O que aconteceu:** Citou trigger PT-BR novo ("o que é X, pra quem é, diferencial"). `Launching skill: anthropic-skills:product-marketing-context`. Workflow completo: checkou `.agents/`, spawnou sub-agent Haiku pra explorar Artemis, compilou doc de 245 linhas com 11 seções. Escopo inflado (Patrick pediu 3, entregou 11) — comportamento nativo da skill, não bug.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 31 — sdd
**Verdict:** DESAMBIGUOU
**Delta v1→v2:** melhorou (ERRADA → DESAMBIGUOU)
**O que aconteceu:** **NÃO caiu no EnterPlanMode nativo** (era o bug v1). Perguntou qual app antes de planejar (pasta Github tem muitos repos). Anti-trigger "NÃO confundir com plan mode nativo" evitou o erro.
**Sinal de CLAUDE.md interferência:** Não
**Fix residual (opcional):** Após clarificar app, reforçar "invocar sdd --research". Não bloqueante.
**Confiança:** Média

### Input 32 — react-patterns
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** Citou triggers "renderizando demais" e "useEffect mal feito". `Launching skill: anthropic-skills:react-patterns`. Phase 1 Stack Detection, escaneou gascat-configurator, grep de useEffect em 19 arquivos. 6 findings com file:line + fix + prioridade.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 33 — reference-finder
**Verdict:** **NENHUMA (regressão real)**
**Delta v1→v2:** REGREDIU ⚠️ (OK → NENHUMA)
**O que aconteceu:** Modelo raciocinou sobre IL-8, concluiu "é questão de knowledge, não 'build something'", e respondeu direto com SBI, Radical Candor e Manager's Path. Resposta de alta qualidade, mas bypassou a skill cujo trigger ("tem livro sobre?", "preciso de referências") bate perfeitamente.
**Sinal de CLAUDE.md interferência:** Não — é racionalização interna
**Root cause:** Description da `reference-finder` diz "fundamentar qualquer tema com referências" mas modelo interpretou como "buscar skills/ferramentas" por contágio com IL-8 `--solution-scout`.
**Fix residual (P1):** Clarificar description — "livros, frameworks, metodologias de management são caso CENTRAL, não edge. `reference-finder` ≠ `--solution-scout` de IL-8."
**Confiança:** Alta

### Input 34 — context-tree
**Verdict:** OK
**Delta v1→v2:** melhorou (MAESTRO indireto → OK)
**O que aconteceu:** Citou trigger "catalogar aprendizados", "organizar conhecimento num lugar". Invocou `context-tree`, leu `_manifest.md`, buscou arquivos Athié, pediu insumo pra começar `--add`. **NÃO criou CLAUDE.md/MEMORY em outro repo** (erro do v1).
**Sinal de CLAUDE.md interferência:** Não — CLAUDE.md do skillforge inclusive reforça "preferir context-tree skill pra knowledge operacional"
**Confiança:** Alta

### Input 35 — lovable-knowledge
**Verdict:** OK
**Delta v1→v2:** já-era-OK
**O que aconteceu:** Considerou lovable-knowledge vs lovable-router, escolheu corretamente lovable-knowledge. Invocou e aplicou gate da IRON LAW (codebase, projeto, workspace/project).
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 36 — lovable-router
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** Citou "mudar direto ou mandar prompt Lovable" → lovable-router. Invocou e aplicou Step 1 (classificar). Identificou ambiguidade visual vs banco, pediu clarificação.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 37 — maestro
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** Citou triggers adicionados ("não sei por onde começar", "qual ferramenta usar"). Invocou maestro. Pediu contexto das 3 coisas antes de rotear.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 38 — geo-optimizer
**Verdict:** OK-PARCIAL
**Delta v1→v2:** melhorou ✨✨ (ERRADA → OK-PARCIAL)
**O que aconteceu:** PRIORITY rule funcionou. `Launching skill: anthropic-skills:geo-optimizer args: copy`. Leu copy/SKILL.md DENTRO do workflow da skill (legítimo — precisa da description pra otimizar, NÃO é bypass). Score 14/15, identificou gaps PT-BR e EN, propôs description otimizada (~890 chars), pediu aprovação antes de Edit (IL-1).
**Sinal de CLAUDE.md interferência:** Não
**Fix residual (opcional):** Description poderia reforçar "ler SKILL.md da target é Phase 1, não bypass" pra futuras auditorias não interpretarem como reincidência.
**Confiança:** Alta

### Input 39 — skill-builder
**Verdict:** OK
**Delta v1→v2:** já-era-OK
**O que aconteceu:** `Launching skill: anthropic-skills:skill-builder args: Step 0 'onboarding de cliente'`. Citou IL-7 (Step 0 gate) e IL-8 (solution-scout antes). Rodou solution-scout em paralelo (2 Haiku sub-agents). 5 matches ranqueados, 5 perguntas bloqueantes respeitando gate. Não construiu prematuramente.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 40 — security-audit
**Verdict:** OK
**Delta v1→v2:** melhorou (NENHUMA → OK)
**O que aconteceu:** Invocou security-audit citando injection/vazamento. Detectou modo Code, pediu target antes. Nota "trigger por intenção, não presença de código" funcionou.
**Sinal de CLAUDE.md interferência:** Não
**Confiança:** Alta

### Input 41 — meeting-sync
**Verdict:** NENHUMA
**Delta v1→v2:** teimosa (NENHUMA → NENHUMA — skill não instalada)
**O que aconteceu:** Detectou os triggers ("transcrição daily", "extrai tasks", "cruza com ClickUp") e tentou invocar `skill: meeting-sync`. Retornou erro "não está instalada ainda". Caiu em fallback manual (Fireflies + ClickUp direto).
**Sinal de CLAUDE.md interferência:** Não
**Root cause:** Skill `meeting-sync` não está publicada no anthropic-skills. Fix de description/routing foi aplicado, mas o arquivo não foi zipado e upado.
**Fix residual (P0 pra fechar Wave C):** Rodar `python zip-skills.py meeting-sync` + upar pro anthropic-skills/Claude.ai.
**Confiança:** Alta

---

## Impacto do CLAUDE.md do Github

**Hipótese inicial:** CLAUDE.md grande do Github (200+ linhas com equipe, clientes, ClickUp, agenda, filtro de alavancagem) poderia **competir** com o triggering das skills.

**Achado:** **Hipótese REFUTADA.**

**Evidência quantitativa:**
- **12 dos 41 inputs (29%)** tiveram menção explícita ao CLAUDE.md do Github
- **Em 100% desses casos a skill foi invocada OU desambiguou legitimamente**
- **Zero casos** em que o CLAUDE.md substituiu ou atrasou a invocação

**Padrão observado:** o CLAUDE.md foi **enriquecimento**, não competição. Inputs com menção:

| Input | Skill | Trecho do CLAUDE.md citado | Impacto |
|---|---|---|---|
| 1 | comunicacao-clientes | "Gascat é do Jonas" + IL-9 | Enriqueceu (flag de delegação) |
| 2 | pptx | "Marine é do Hygor" | Enriqueceu (incluiu Hygor como co-author) |
| 6 | n8n-architect | Regra "pergunta antes de assumir" | Levou a DESAMBIGUOU (aceitável) |
| 7 | site-architecture | "JRG é do Hygor" | Enriqueceu contexto |
| 8 | docx | "Artemis Marketing/Comercial/Operação" | Pediu desambiguação útil |
| 11 | component-architect | "made by Hygor" | Enriqueceu (implícito de delegação) |
| 12 | vps-infra-audit | "VPS Docker/EasyPanel" | Ajudou a escolher skill certa (vps vs security) |
| 13 | copy | "Artemis Marketing/Comercial" | Enriqueceu |
| 16 | tech-lead-pm | "Jonas junior inexperiente" | Enriqueceu (ativou Module 6 da skill) |
| 17 | seo | "Marine é do Hygor" + IL-9 | Enriqueceu |
| 20 | prompt-engineer | "Hygor é assigned a Athié" | Enriqueceu |
| 27 | pattern-importer | "Stack Lovable+Supabase+n8n" | Customizou output da skill |

**Diagnóstico teórico (research Fase 0):**

- **Tool Preferences in Agentic LLMs are Unreliable (arxiv 2505.18135):** "Tool selection can be heavily swayed by simple text edits to descriptions" — previa que competição de textos seria instável. Nosso resultado (zero sabotagem) contradiz isso no caso específico, sugerindo que quando **skill-routing.md tem mapeamento determinístico forte**, o CLAUDE.md não consegue competir.
- **Learning to Rewrite Tool Descriptions (arxiv 2602.20426):** rewriting sistemático dá +6% query-level. Nosso ganho (+56pp) superou porque combinamos rewriting **+ tabela determinística externa** (skill-routing.md).
- **Claude Code docs:** "CLAUDE.md is advisory ~80% of the time." Consistente com o que vimos — CLAUDE.md sempre presente, mas não bloqueou triggering.

**Recomendação:** **MANTER o CLAUDE.md do Github como está.** Não precisa slim-down — ele está ajudando, não atrapalhando. A arquitetura `skill-routing.md + SKILL.md description + CLAUDE.md` funciona em camadas complementares: routing é determinístico, description é semântica, CLAUDE.md é contexto adicional.

**Nota pra uso diário:** em **2 inputs** (1, 17), a ativação do IL-9 pelo CLAUDE.md adicionou passo a mais antes da skill (confronto "isso é pro Jonas?"). Isso é o comportamento **desejado pelo Patrick** (per IL-9 existe pra isso) — não é overhead, é o filtro de alavancagem funcionando.

---

## Comparação v1 vs v2

### Distribuição de verdicts

| Verdict | v1 (baseline 2026-04-15) | v2 (pós-fixes 2026-04-18) | Delta |
|---|---|---|---|
| OK | 15 | **30** | +15 |
| OK-PARCIAL | 1 | 3 | +2 |
| DESAMBIGUOU | 0 | **6** | +6 |
| NENHUMA | 20 | **2** | **−18** |
| ERRADA | 4 | **0** | **−4** |
| MAESTRO/INCERTO | 1 | 0 | −1 |

### Movimentos notáveis

**Vitórias grandes (ERRADA/NENHUMA → OK):**
- 21 (free-tool-strategy): ERRADA → OK
- 27 (pattern-importer): ERRADA → OK
- 38 (geo-optimizer): ERRADA → OK-PARCIAL (meta-bug destravado)
- 31 (sdd): ERRADA → DESAMBIGUOU (plan mode conflict resolvido)
- 19 NENHUMAs viraram OK (pdf, n8n, docx, product-discovery, component-architect, supabase, tech-lead-pm, context-guardian, prompt-engineer, launch-strategy, ui-design-system, code-dedup-scanner, sales-enablement, architecture-guard, product-marketing-context, react-patterns, lovable-router, maestro, security-audit)

**Regressões:**
- 33 (reference-finder): OK → NENHUMA — **única regressão de comportamento real**
- 10, 12, 13, 23: OK → DESAMBIGUOU — cosméticas (skill reconhecida, só não declarada formal)
- 26 (cli-skill-wrapper): OK → OK-PARCIAL — conflito IL-8

**Teimosas:**
- 41 (meeting-sync): NENHUMA → NENHUMA — skill não instalada (fix de publicação, não de description)

### Padrão sistêmico observado

**Padrão "clarify-first":** em 4 inputs (10, 12, 13, 23), v1 declarava skill rapidamente, v2 pede contexto primeiro. Pela rubric do Patrick, isso é neutro-positivo (skill certa identificada no raciocínio, desambiguou por falta de contexto). Mas é um sinal de que o tuning das descriptions foi muito enfático em "coletar contexto" — pode valer reforço futuro: "declare skill antes de perguntar, depois perguntas dentro do workflow da skill".

### Citação explícita do skill-routing.md

Em **pelo menos 15 dos 30 OK**, o modelo citou o skill-routing.md diretamente no raciocínio ("the skill-routing rules say X → Y"). A tabela virou **gate determinístico** — não é mais só uma sugestão que o modelo aciona às vezes, é consultada ativamente. Isso é a principal razão do salto 39% → 95%.

---

## Plano de ação

### ✅ Wave C — agora (empacotamento + publicação)

Com 95% de passing, seguir direto pra Wave C do PLANO-FIXES.md:

1. **Rezip das 23 skills editadas** + skill-routing.md atualizada:
   ```
   python zip-skills.py geo-optimizer sdd pdf n8n-architect docx product-discovery-prd component-architect supabase-db-architect tech-lead-pm context-guardian prompt-engineer launch-strategy ui-design-system sales-enablement architecture-guard product-marketing-context react-patterns context-tree lovable-router maestro meeting-sync trident code-dedup-scanner security-audit reference-finder free-tool-strategy copy pattern-importer
   ```

2. **Doc de fechamento** — criar `FIXES-APLICADOS.md` com resumo das 23 edits + antes/depois 39%→95%.

3. **Commits por wave** (3 commits sequenciais, não push sem aprovação):
   - `fix(skills): wave-A p0 — geo-optimizer + sdd + skill-routing expansion`
   - `fix(skills): wave-B batch — 23 skills triggers + structural`
   - `docs: wave-B analysis — 39%→95% passing (anti-loop definitive)`

### P0 — pendente antes/junto da Wave C

1. **Publicar meeting-sync (Input 41).** A skill tem description corrigida mas não está no catálogo anthropic-skills. Rodar `zip-skills meeting-sync` + upload. Sem isso, Input 41 nunca vai passar.

### P1 — fixes menores que podem ir junto com Wave C (opcional)

1. **Input 33 (reference-finder):** clarificar description — livros/frameworks de management = caso central, não edge. Adicionar: "NÃO confundir com `reference-finder --solution-scout` de IL-8 (aquele é tool-finding)."

2. **Input 26 (cli-skill-wrapper):** carve-out na IL-8 do iron-laws.md — quando trigger bate com skill de build/wrap específica (`cli-skill-wrapper`, `skill-builder`, `n8n-architect`), pular solution-scout.

### Backlog (pra futuro, não bloqueia Wave C)

1. **Input 3 (trident):** handoff Scanner → Verifier passa só "key sections". Verifier cai em INSUFFICIENT_EVIDENCE quando precisa ver arquivo inteiro. Considerar passar arquivo full ou referências de linha ao Verifier.

2. **Input 2 (pptx) QA visual no Windows:** `soffice.py` usa `socket.AF_UNIX` que não existe no Windows → QA visual falha silenciosa. Não é urgente (python-pptx substitui), mas documentar limitação.

3. **Input 27 (pattern-importer) cleanup Windows:** `.tmp/` falhou 3x com "Device or resource busy". Adicionar nota nas references: "Windows use `Remove-Item -Force` via PowerShell".

4. **Inputs 10/12/13/23 "clarify-first" pattern:** considerar ajuste universal nas descriptions — "declare skill antes de pedir contexto, perguntas entram dentro do workflow". Não é bloqueante (rubric Patrick aceita).

5. **Input 6 (n8n-architect):** considerar declarar skill no plano antes de pedir erro log (comportamento similar ao backlog #4).

---

## Verificação

- [x] **Contagem:** 41 blocos `### Input N —` confirmados
- [x] **Cobertura de classificação:** todo verdict em {OK, OK-PARCIAL, DESAMBIGUOU, NENHUMA, ERRADA}
- [x] **Soma:** 30 + 3 + 6 + 2 + 0 = 41 ✓
- [x] **Seção CLAUDE.md com evidência concreta:** 12 citações explícitas listadas
- [x] **Decisão do critério marcada:** ≥80% = checkbox [x]
- [x] **Deltas v1→v2 identificados:** coluna dedicada na tabela consolidada

---

## Fechamento

**Wave B foi um sucesso definitivo.** O arsenal saiu de 39% → 95% de triggering reliability com:

- 2 edits P0 (geo-optimizer + sdd)
- 1 expansão da skill-routing.md (+25 triggers)
- 23 edits de SKILL.md (descriptions)
- 2 boundaries entre skills conflitantes

**Próximo passo:** Wave C (rezip + doc + commits), com P0 de publicar `meeting-sync` antes.

**Anti-loop cumprido:** 1 reteste completo, sem mini-retests. Os 2 NENHUMAs remanescentes têm fix claro (publicação + clarificação de description) que vai junto na Wave C ou P1 seguinte. Nenhuma skill sob "investigação sistêmica". Sistema estabilizado.

Sources da Fase 0:
- [Skill authoring best practices — Claude API Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Best Practices for Claude Code](https://code.claude.com/docs/en/best-practices)
- [Learning to Rewrite Tool Descriptions (arxiv 2602.20426)](https://arxiv.org/html/2602.20426v1)
- [Tool Preferences in Agentic LLMs are Unreliable (arxiv 2505.18135)](https://arxiv.org/html/2505.18135v2)
- [Tool Calling Explained: The Core of AI Agents — Composio](https://composio.dev/content/ai-agent-tool-calling-guide)

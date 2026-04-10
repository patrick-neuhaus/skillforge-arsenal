# Audit de Overlaps de Skills — 2026-04-10

## Contexto

Auditoria conduzida após Patrick reportar que em outra conversa Claude propôs `simplify` (built-in Anthropic) pra review DRY/KISS, depois trocou pra `trident` quando questionado. Investigamos overlaps reais entre skills do skillforge-arsenal e built-ins, e o estado de sincronia do maestro skill-catalog.

## Estado do catalog

- **Folders no repo:** 40
- **Entradas no skill-catalog.md:** 39 + 1 menção meta a `maestro` no final = 40 ✅
- **Conclusão:** catalog está sincronizado em quantidade. O agente Explore que reportou "39 vs 40" contou errado (não somou a entrada de maestro).

## Overlaps mapeados

### 1. `simplify` (Anthropic built-in) vs `trident` — REAL

- **Conflito:** Ambos fazem code review focado em qualidade. Simplify é built-in (`Review changed code for reuse, quality, and efficiency, then fix any issues found`). Trident é pipeline de 3 agentes.
- **Decisão:** **Documentar regra de prioridade.** Não dá pra mexer no simplify (built-in). Solução: hard rule no CLAUDE.md e no skill-catalog → "para code review usar trident; nunca invocar simplify".
- **Por quê trident:** Cobertura mais ampla (bugs reais, security, SOLID, dead code), 3-agent verification, tem `--design` e `--skill` modes, output estruturado P0-P3.

### 2. `trident --design` vs `ux-audit` — PARCIAL

- **Conflito:** Trident tem flag `--design` (Design review: visual consistency + accessibility + performance — 3 layers). UX-audit faz auditoria UX completa (heurísticas, fluxos, WCAG, dark patterns).
- **Decisão:** **Documentar boundary recíproca.** ux-audit já tem nota no description: "Nao confundir com... trident --design (review de codigo frontend). UX audit foca na EXPERIENCIA do usuario, nao no codigo nem no design system." Trident NÃO tem nota recíproca. Adicionar.
- **Boundary clara:** trident `--design` = code-level (CSS, layout, perf, a11y no código). ux-audit = experience-level (fluxos, heurísticas, dark patterns, jornada do usuário).

### 3. `trident --skill` vs `geo-optimizer` — PARCIAL

- **Conflito:** Trident `--skill` faz "Review a skill as product: GEO, structure, distribution readiness". Geo-optimizer é especializado em GEO.
- **Decisão:** **Documentar boundary.** trident --skill = review holístico de uma skill como produto (estrutura, GEO, distribuição). geo-optimizer = otimização cirúrgica de description pra agente discovery.
- **Regra:** se for só "minha description tá fraca" → geo-optimizer. Se for "review essa skill toda como produto" → trident --skill.

### 4. `copy --mode whatsapp` vs `comunicacao-clientes` — PARCIAL

- **Conflito:** Copy tem mode whatsapp pra marketing/vendas/conversão. Comunicacao-clientes é mensagens operacionais (cobrança, update, aprovação, mudança de escopo).
- **Decisão:** **Boundary recíproca em ambos os SKILL.md.**
  - copy `--mode whatsapp` = persuasão, conversão, vendas, broadcast marketing
  - comunicacao-clientes = relacionamento operacional 1:1 com cliente (objetivo + contexto + ação esperada)
- comunicacao-clientes JÁ tem boundary contra tech-lead-pm no description, mas NÃO contra copy. Adicionar.
- copy SKILL.md NÃO tem boundary visível no top do arquivo. Adicionar.

### 5. `sdd` vs `component-architect --plan` — JÁ RESOLVIDO

- **Conflito aparente:** ambos planejam.
- **Realidade:** sdd = pipeline 4 fases pra features completas. component-architect --plan = planejar componentes individuais. Boundary já é clara no catalog.
- **Decisão:** Nenhuma ação. Já documentado.

### 6. `seo` vs `ai-seo` — JÁ RESOLVIDO

- **Conflito aparente:** ambos são SEO.
- **Realidade:** seo = SEO tradicional (technical, on-page, off-page, programático). ai-seo = AEO/GEO/LLMO (citações em LLMs).
- **Decisão:** Documentar como **chain** em composition-chains: `seo --content` → `ai-seo` para conteúdo que precisa rankear no Google E ser citado por LLMs.

## Gaps identificados (skills que faltam)

### Gap principal: roteamento de modelo/thinking

Patrick não tem skill ou heurística pra decidir entre Sonnet medium / Sonnet high / Opus high / Opus high + opusplan / thinking budget. Fica em dúvida toda vez.

**Decisão:** **NÃO criar skill nova.** A solução é o bloco `Model & Skill Router` no CLAUDE.md (Github + Daily). Skill nova exigiria invocação manual — perde o ponto de ser automático. Bloco no system prompt sempre roda.

### Gaps secundários (não-críticos)

- **Handoff entre sessões:** context-guardian já cobre com `--handoff`. OK.
- **Review de prompt antes de mandar pra LLM externa:** prompt-engineer cobre com `--validate`. OK.
- **Skill pra decidir composição (chain) antes de executar:** maestro cobre. OK.

**Conclusão de gaps:** Nenhuma skill nova precisa ser criada. Ajustes vão na direção de **clarificar boundaries** das que existem + **adicionar Routing Priorities** no maestro + **router no CLAUDE.md**.

## Ações decididas (executar nesta ordem)

1. **maestro/references/skill-catalog.md:** Adicionar seção `## Routing Priorities` no topo com regras hard:
   - Code review → trident (NUNCA simplify)
   - Design review código frontend → trident --design
   - Auditoria UX experiência → ux-audit
   - Review de skill como produto → trident --skill
   - Otimização de description GEO cirúrgica → geo-optimizer
   - Mensagem operacional pro cliente → comunicacao-clientes
   - Copy persuasiva pra cliente (WhatsApp marketing) → copy --mode whatsapp
2. **maestro/references/composition-chains.md:** Adicionar chain `seo` → `ai-seo` + chain SDD com modelos (Opus pra spec → Sonnet pra implement → Trident pra review)
3. **trident SKILL.md:** Adicionar boundary com ux-audit (`--design` é code-level) e geo-optimizer (`--skill` é review holístico)
4. **copy SKILL.md:** Adicionar boundary com comunicacao-clientes no top do arquivo
5. **comunicacao-clientes SKILL.md:** Adicionar boundary com copy no top do arquivo
6. **CLAUDE.md (Github + Daily):** Nova seção `## Model & Skill Router` + ajuste em "Higiene de tokens" (compact 60→50%, loop rule)

## Não fazer

- Não criar skill `model-router` — bloco no CLAUDE.md resolve melhor
- Não deletar trident `--design` e `--skill` — eles são complementares (code-level), não duplicam ux-audit (experience-level) nem geo-optimizer (cirúrgico)
- Não consolidar copy + comunicacao-clientes — propósitos diferentes (persuasão vs relacionamento operacional)

# FIXES APLICADOS — Wave A+B (2026-04-14 a 2026-04-18)

## Status: VALIDATED — não editar sem solicitação explícita do Patrick

**Marker:** `validated:2026-04-18`
**Ref:** [ANALISE-WAVE-B.md](ANALISE-WAVE-B.md) — taxa de triggering 39% → **95%** em 41-test reliability
**IRON LAW ativa:** IL-10 (`~/.claude/rules/iron-laws.md`) — lock-in das skills listadas aqui

---

## Resumo

- **23 SKILL.md editadas** (Wave A: 2 P0, Wave B: 19 descriptions + 4 estruturais + 2 boundaries)
- **1 arquivo de routing editado** — `~/.claude/rules/skill-routing.md` (25 triggers novos, 10 → 35 linhas)
- **1 skill publicada pela primeira vez** — `meeting-sync` (description reescrita completa + zip + dist/)
- **Taxa final:** 39% (16/41) → **95% (39/41)** — delta +56pp
- **Regressões reais:** 1 (Input 33 reference-finder — P1 backlog)
- **Failures residuais:** 1 (Input 41 meeting-sync — **resolvido nesta Wave C** via publicação)

---

## Lista completa das edits

### Wave A — P0 (desbloqueia o resto)

| Skill | Tipo | Mudança | Input que fixou |
|---|---|---|---|
| **geo-optimizer** | description | PRIORITY rule meta-bug: "quando user reporta problema de triggering, esta skill handles — NÃO abrir SKILL.md da mencionada". +7 triggers PT-BR | 38 (ERRADA → OK-PARCIAL) |
| **sdd** | description | Anti-trigger vs plan mode nativo: "NOT the same as Claude Code native plan mode". +4 triggers PT-BR ("planeja antes de codar", "antes de sair codando") | 31 (ERRADA → DESAMBIGUOU) |
| **skill-routing.md** | routing | Expansão de 10 → 35 linhas (25 novos mapeamentos keyword → skill) | Todos os 19+ NENHUMA viraram OK |

### Wave B — 19 edits só de description

| Skill | Triggers adicionados | Input que fixou |
|---|---|---|
| n8n-architect | "workflow quebrando", "workflow quebrado", "tá dando erro no n8n" | 6 (NENHUMA → DESAMBIGUOU) |
| component-architect | "componente gigante", "quebrar componente", "componente de N linhas" | 11 (NENHUMA → OK) |
| tech-lead-pm | "travado", "parado na task", "dev bloqueado", "como lido com dev travado" | 16 (NENHUMA → OK) |
| prompt-engineer | "escrever instruções pro Claude", "montar CLAUDE.md do projeto" | 20 (NENHUMA → OK) |
| launch-strategy | "lançar produto", "plano de lançamento", "como lanço isso", "estratégia de lançamento" | 22 (NENHUMA → OK) |
| ui-design-system | "cores e fontes padronizadas", "preciso de paleta", "espaçamento padronizado", "padronizar visual" | 24 (NENHUMA → OK) |
| sales-enablement | "material de vendas", "reunião com prospect", "preparar reunião comercial", "levar pra reunião" | 28 (NENHUMA → OK) |
| product-marketing-context | Triggers PT-BR: "o que é X, pra quem é, diferencial", "documento de posicionamento", "explica o produto" | 30 (NENHUMA → OK-PARCIAL) |
| react-patterns | "renderizando demais", "useEffect mal feito", "re-render excessivo", "tá pesado o React" | 32 (NENHUMA → OK) |
| pattern-importer | "como outros projetos fazem isso", "exemplos de open source", "ver como X implementa" | 27 (ERRADA → OK) |
| context-guardian | "antes de dar /clear", "to sem contexto" | 19 (NENHUMA → OK) |
| context-tree | "catalogar aprendizados sobre projeto", "guardar o que aprendi", "organizar num lugar" | 34 (MAESTRO → OK) |
| lovable-router | "mudo direto ou mando prompt?", "edição direta vs prompt" | 36 (NENHUMA → OK) |
| maestro | "tenho N coisas pra fazer", "qual ferramenta usar", "me ajuda a priorizar" | 37 (NENHUMA → OK) |
| security-audit | "injection", "vazamento de dados", "tá seguro esse código?" + nota "trigger pela INTENÇÃO, não presença de código" | 40 (NENHUMA → OK) |
| supabase-db-architect | "como tá meu banco", "policies certas", "auditar supabase" + nota "mesmo com MCP direto, passa pela skill" | 14 (NENHUMA → OK) |
| copy | Rewrite proposto pelo geo-optimizer: +Sales Page, +Social subchannels (Instagram/LinkedIn/TikTok), +Ads (Meta/Google), boundary explícito vs comunicacao-clientes | 13 (OK → DESAMBIGUOU cosmético) |
| meeting-sync | Rewrite completo da description (era 1 linha sem quotes). "peguei a transcrição da daily", "extrai tasks da reunião", "cruza com o ClickUp", "sincroniza reunião" | 41 (resolvido via publicação aqui em Wave C) |

### Wave B2 — 3 edits estruturais (description + workflow hint)

| Skill | Mudança | Input que fixou |
|---|---|---|
| trident | Fallback: "se arquivo não encontrado no worktree, pedir paste do código inline — não bloquear análise" | 3 (OK-PARCIAL → OK) |
| ~~code-dedup-scanner~~ | **ABSORVIDA em trident --dedup (Wave 1, 2026-04-29)** — skill apagada, lock-in removido | n/a |
| security-audit | (coberto na Wave B1) | 40 |

### Wave B3 — 2 boundaries

| Edit | Skills afetadas | Input que fixou |
|---|---|---|
| **reference-finder ↔ free-tool-strategy** | Ambas | 21 (ERRADA → OK) |
| Anti-trigger em reference-finder: "NÃO use quando intenção é CONSTRUIR ferramenta própria → use free-tool-strategy" | reference-finder | 21 |
| Nota em free-tool-strategy: "Para buscar livros/frameworks consagrados sobre o tema, use reference-finder. Esta skill é pra CONSTRUIR a ferramenta" | free-tool-strategy | 21 |

---

## Condição de lock-in

Skills listadas acima **NÃO podem ser editadas** em description ou estrutura sem:

1. **Patrick pedir explicitamente**, OU
2. **Falha detectada em novo teste formal** (não achismo)

**Fundamento:** Wave B provou que over-tuning introduz regressões. Input 33 (reference-finder) regrediu (OK → NENHUMA) depois de ajustes — o modelo começou a racionalizar "é questão de knowledge, não build something" e bypassou a skill. Lock-in previne Claude futuro de "melhorar" algo estável.

**Enforcement:** IL-10 em `~/.claude/rules/iron-laws.md` — hook verifica grep `validated:` neste arquivo antes de editar qualquer SKILL.md.

**Exceção de emergência:** bug crítico em produção onde a skill quebra funcionalidade (não só triggering). Documentar motivo no commit.

---

## Backlog explícito (NÃO trocar pelo que tá funcionando)

Prioridades identificadas pela Wave B que **ficam pra próximo ciclo**:

### P1 (fix real, mas não bloqueia uso)

- **Input 33 (reference-finder):** regressão real. Description precisa clarificar que "livros e frameworks de management" é caso CENTRAL, não edge. Diferenciar explicitamente de `reference-finder --solution-scout` (IL-8).
- **Input 26 (cli-skill-wrapper):** carve-out na IL-8 do iron-laws.md — quando trigger bate com skill de build/wrap específica (`cli-skill-wrapper`, `skill-builder`, `n8n-architect`), pular solution-scout pra evitar impasse.

### P2 (polimento, sem impacto de triggering)

- **Input 3 (trident):** Scanner → Verifier handoff passa só "key sections" do código. Verifier cai em INSUFFICIENT_EVIDENCE quando precisa ver arquivo inteiro. Considerar passar arquivo full ou refs de linha.
- **Input 2 (pptx):** `soffice.py` usa `socket.AF_UNIX` que não existe no Windows → QA visual falha silenciosa. Documentar limitação; python-pptx substitui.
- **Input 27 (pattern-importer):** cleanup de `.tmp/` falha 3x no Windows com "Device or resource busy". Nota nas references: "Windows → `Remove-Item -Force` via PowerShell".
- **Inputs 10/12/13/23 "clarify-first":** skill identificada mas não declarada formal antes de pedir contexto. Cosmético pela rubric (Patrick aceita DESAMBIGUOU). Considerar: "declare skill antes de pedir contexto, perguntas entram DENTRO do workflow".
- **Input 6 (n8n-architect):** similar — declarar skill no plano antes de pedir erro log.

**Regra do backlog:** um item daqui SÓ é trabalhado se (a) Patrick priorizar ou (b) novo teste detectar escalada do impacto. Não fuçar por livre iniciativa.

---

## Next queue (plans próprios, NÃO fazer junto)

### Context-tree evolution (LLM Wiki pattern — Karpathy 2026)

**Seed:** `D:\DOWNLOADS\context-tree-evolution-prompt.md`

Features planejadas:
1. **`--ingest`** automático em plan mode — captura decisões arquiteturais, padrões técnicos, applied learnings de planos gerados. Não mais manual.
2. **`--lint`** — verificação de saúde: contradições entre entries, claims desatualizados (>60d), entries órfãs, lacunas de cobertura.
3. **`--archive-findings`** — persiste síntese de queries elaboradas como entry nova (compounding por exploração).
4. **Reorganização por projeto:** `supply-mep/`, `gascat/`, `marine/`, `galaxia/`, `patrick-pessoal/`, `artemis-interno/` — em vez de domínios técnicos.

### Gatilhos semânticos pra ingest (ideia do Patrick, 2026-04-18)

Em vez de logar "skill X invocada" (shallow), logar **padrões de pensamento do Claude**:

| Pattern regex | Interpretação | Onde guardar |
|---|---|---|
| "pensei errado", "embarquei no [X]", "overengineer" | Log de erro/overengineering | `patrick-pessoal/skills-ecosystem/erros-do-claude.md` |
| "escolhi X porque Y", "tradeoff [A] vs [B]" | Decisão arquitetural | ramo do projeto atual |
| "a regra existia e eu não apliquei" | Gap de aplicação de IRON LAW | `patrick-pessoal/skills-ecosystem/iron-law-gaps.md` |
| "falhei em [X]", "errei ao [X]" | Applied learning | ramo do projeto atual |
| "a resposta certa seria [X]" | Self-correction | ramo do projeto atual |

**Fonte:** logs nativos do Claude Code em `~/.claude/projects/*/sessions/*.jsonl` (JSONL com thinking + tool calls + user messages). Parser post-hoc não-invasivo extrai patterns retroativamente. Quando validado, vira hook `UserPromptSubmit` ou `Stop` em real-time.

**Relação com context-tree evolution:** essa é a **Feature 1 (`--ingest`) implementada via gatilhos semânticos**, não via trigger manual. Plan próprio necessário — NÃO incluído em Wave C.

### Outras possibilidades (baixa prioridade)

- Atualizar `HOW-TO-USE.md` com fluxo Wave A+B+C (documentação viva de como o sistema evoluiu)
- Integrar `FIXES-APLICADOS.md` no startup do Claude Code (via CLAUDE.md import?) pra ativar IL-10 sem grep manual
- Testes de regressão automatizados (rodar N inputs selecionados periodicamente, alertar se taxa cair)

---

## Cross-references

- **Baseline v1:** [ANALISE-RESULTADOS.md](ANALISE-RESULTADOS.md) — 39% passing
- **Análise final v2:** [ANALISE-WAVE-B.md](ANALISE-WAVE-B.md) — 95% passing
- **Raw tests:** [RESULTADO-TESTES.md](RESULTADO-TESTES.md) (v1), [RESULTADO-WAVE-B.md](RESULTADO-WAVE-B.md) (v2)
- **Plano original:** [PLANO-FIXES.md](PLANO-FIXES.md)
- **Narrativa histórica:** [SESSION-NARRATIVE.md](SESSION-NARRATIVE.md)
- **Iron Laws:** `~/.claude/rules/iron-laws.md` (IL-10 ativa o lock-in)

---

## Histórico condensado

| Data | Wave | O que aconteceu |
|---|---|---|
| 2026-04-14 | Wave 0 | Sanity check — 3/3 NENHUMA no Github/. Ambiente não interfere. |
| 2026-04-14 | Wave A | 3 edits P0: geo-optimizer + sdd + skill-routing.md |
| 2026-04-14 | Wave A retest | 3/3 OK. Passou direto pra Wave B. |
| 2026-04-14 | Wave B | 23 edits: 19 descriptions + 4 estruturais + 2 boundaries |
| 2026-04-15 | Wave B retest | 41 inputs rodados em Sonnet medium no Github/ |
| 2026-04-18 | Wave B análise | 39/41 = 95% passing (vs 39% baseline) |
| 2026-04-18 | Wave C | Este fechamento — publish meeting-sync + rezip + doc + IL-10 + commits |

**Parada definitiva após Wave C.** Próximos testes de triggering SÓ quando houver skill nova ou mudança solicitada explicitamente.


## Wave 4 Ecosystem (2026-04-29)

Marker: `validated:2026-04-29`

**Mudanças:**
- Wave 1 (hygiene): 7 descriptions trim (todas <720 chars), trident absorveu code-dedup-scanner (--dedup mode), code-dedup-scanner DELETADO, model-skill-router.md deprecated, sdd carve-out (Folloni Marmelab+Scott Logic)
- Wave 2 (componentização): ~/.claude/library/{rubrics,severity,templates}/ extraída de prompt-engineer/trident/skill-builder, IL-11 ativa
- Wave 3 (orquestração): maestro V2 (modos --fast/--full/--workflow + Phase 2.6 model+thinking), 5 agents próprios (~/.claude/agents/), 2 hooks layered (SessionStart bootstrap + Stop error-doubt-tracker), ~/.claude/state/, OMC instalado híbrido, IL-5 estendida
- Wave 4 (closure): este file + IL-10 estendida cobrindo agents + CLAUDE.md updates

**Lock-in extended (validated:2026-04-29):**
- 22 skills (validated:2026-04-18 mantidas) — geo-optimizer, sdd, n8n-architect, component-architect, tech-lead-pm, prompt-engineer, launch-strategy, ui-design-system, sales-enablement, product-marketing-context, react-patterns, pattern-importer, context-guardian, context-tree, lovable-router, maestro, security-audit, supabase-db-architect, copy, meeting-sync, trident, skill-routing.md
- ~~code-dedup-scanner~~ removida (absorvida em trident --dedup)

**Agents próprios (NÃO em lock-in ainda):**
- executor, planner-skill, verifier-skill, lovable-implementer, n8n-fixer
- Marker `validated:2026-05-06` aplicado APÓS 1 semana de uso real sem regressão (Patrick decide promover individualmente)
- Razão: Wave A+B+C provou que lock-in prematuro introduz regressões

**Pendências (backlog):**
- 6º/7º agents próprios (critic-skill, reviewer-trident) — backlog
- OMC kill switches granulares — Wave 5 ou ciclo dedicado
- Built-ins audit (pdf/docx/pptx/xlsx) — test-driven decision quando uso real aparecer
- Cleanup library cópias legadas (skills/X/references/ duplicadas) — após 7d cooldown
- Sanity test final em fresh session — agendar
---

## Wave Design Skills (2026-05-01) — DR-01..05 + chats 0..4 reconciliação

**Contexto:** Patrick rodou pesquisa pesada (5 Deep Research + 4 chats Claude Design). PLAN.md + chat-4 reconciliação consolidaram em 6 waves de mudança.

**Decisões humanas confirmadas:**
- U1 OKLCH+WCAG+HCT benchmark
- U2 breakpoints rem 20/30/48/64/80/120
- U3 status colors manuais
- U4 dark mode opcional
- U5 9 primitives mantidos
- R1-R3 browser matrix: `last 2 years, > 0.5%, not dead` + Safari iOS público + Edge enterprise
- R4 Phase 5 cross-browser opt-in
- R5 frontend-qa NÃO criada
- A1 (DR-05 motion-design) adiado

**Skills aplicadas:**

| Skill | Wave | Score | Novo marker |
|---|---|---|---|
| ux-audit | 1 (v3→v4) | 92 | `validated:2026-05-01` (1ª lock-in) |
| ui-design-system | 2 (v1→v2) | 94 | `validated:2026-05-01` (re-lock) |
| skill-routing.md | 3 (patch) | 88 | `validated:2026-05-01` (re-lock) |
| react-patterns | 4 (cross-browser) | 89 | `validated:2026-05-01` (re-lock) |
| component-architect | 5 (light boundary + states-inventory) | 85 | `validated:2026-05-01` (re-lock) |
| maestro | 6 (routing patch + chains) | 88 | `validated:2026-05-01` (re-lock) |

**Mudanças por skill:**

- **ux-audit v4:** 3 Iron Laws (percorre fluxo + critério aceite + triagem). 7 fases. 5 references novos: ux-foundations, wcag-ux-checklist, ux-severity-rubric, audit-output-template, triage-matrix. Removidos: ux-ui-foundations, wcag-checklist, scoring-rubrics, audit-templates, dark-patterns-check.
- **ui-design-system v2:** 3 Iron Laws (concrete inputs + tokens by role + foreground real pair). 6 fases pipeline. 5 references novos: color-token-algorithms, responsive-design-system, component-state-rubric, motion-and-interaction, design-system-maturity-rubric. design-json-schema preservado (extensão fica pra fork v2). mini-identity-guide + remotion-design-tokens preservados.
- **skill-routing.md:** linhas novas (cross-browser → react-patterns; ui-design-system --generate / --audit; design-system-audit default anti-ai-design-system; component-architect --plan; UX vs UI vs visual review). Regra anti-routing shadcn. "review" estendido pra 4 categorias (código/prompt/UX/visual).
- **react-patterns:** Iron Laws preservados (Thin Client Fat Server primeira) + 2 novos (multi-engine evidence + triagem). Phase 0 triagem nova. Phase 5 cross-browser opt-in. Phase 6 síntese. 3 references novos: cross-browser-checklist, build-targets-and-polyfills, playwright-browser-matrix. pattern-guide + remotion-react-patterns preservados.
- **component-architect:** 1 linha boundary com ui-design-system em Integration. states-inventory.md canônico criado (17 estados + anatomia/comportamento/a11y, ui-DS owns tokens visuais, ux-audit referencia).
- **maestro:** routing table Phase 1 expandida (1 linha → 5 linhas específicas + cross-browser). composition-chains.md ganhou 2 chains: "App com cara de IA + problemas técnicos" e "Novo produto — definir DS + componentes + scaffold".

**Boundaries respeitadas:**
- design-system-audit NÃO modificada (boundary protegida)
- WCAG limiares redigidos SÓ em ux-audit/wcag-ux-checklist
- Severidade Nielsen redigida SÓ em ux-audit/ux-severity-rubric
- shadcn não virou DS default
- frontend-qa NÃO criada
- DR-05 motion-design NÃO absorvida (adiada pra Step 0 skill-builder futuro)

**Lock-in IL-10 atualizado:**
- 6 skills com `validated:2026-05-01` (cooldown 1 semana, promoção pra `validated:2026-05-08` após uso real sem regressão)
- ux-audit entra em lock-in pela primeira vez (não estava em validated:2026-04-18)

## Wave 7 — motion-design skill nova (2026-05-02)

**Decisão Patrick:** desimpedir DR-05. Skill nova com 4 references = 4 pilares da taxonomia DR-05.

**Skill:** `skills/motion-design/`
- SKILL.md (score 90, marker IL-1 fresh)
- references/01-funcional-estrutural.md (Pilar 1: microinteractions, page transitions)
- references/02-vetorial-branding.md (Pilar 2: logos, kinetic type, character, SVG/Lottie/Rive)
- references/03-narrativo-editorial.md (Pilar 3: scrollytelling, hero, parallax, ambient)
- references/04-espacial-imersivo.md (Pilar 4: WebGL/3D/AR/VR/faux 3D)

**Iron Laws:**
1. Motion paga aluguel ou sai (função observável obrigatória)
2. Calibragem por contexto (operacional ≠ landing ≠ brand-heavy)
3. Reduced-motion + a11y são gates

**3 modos:** `--catalog` (default), `--spec`, `--audit`

**Trigger adicionado em skill-routing.md:** "qual animação usar", "lottie ou rive", "scrollytelling", "configurador 3D", "AR try-on", "kinetic typography", "logo animado", "page transition", "spec de motion", motion design.

**Boundaries:**
- Tokens duração/easing → ui-design-system (consome, não redefine)
- Auditoria observável de motion → ux-audit
- Implementação React/cross-browser → react-patterns
- Anatomia de componente animado → component-architect

**Lock-in:** motion-design entra com `validated:2026-05-02` (1ª lock-in, cooldown 1 semana).

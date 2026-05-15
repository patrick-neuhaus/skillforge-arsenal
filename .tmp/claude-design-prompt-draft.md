# Avaliação pós-Wave 5: anti-ai-design-system está pronto OU faltam próximos passos?

## Contexto

Você (Claude Design) recebeu 2 deep research reports + 1 handoff doc + 1 registro evolução. Output: Vitor v2 do `anti-ai-design-system` com Waves 1-5 implementadas. Agora preciso avaliação fria sobre estado pós-v2.

## O que foi entregue (Waves 1-5 done)

1. **Wave 1 — Source of truth** (`README.md`): adicionou section "What is normative vs. illustrative vs. legacy". Classifica `docs/01-09`, `colors_and_type.css`, `SKILL.md` como normativos. `presets/default/`, `ui_kits/default/`, `preview/` como ilustrativos. `lovable-memory/`, `PLAN.md`, `audits/` como legado.

2. **Wave 2 — `<table>` contextual rule** (`docs/01-anti-patterns.md`): rewrote anti-pattern #2 de blanket ban pra contextual ("table for tabular data, grid for navigable rows"). Adicionou exemplos.

3. **Wave 3 — Token AA contrast** (`presets/default/tokens.css`): `--accent: 12 65% 55% → 12 70% 42%` (~13% L shift, passa AA). Adicionou `--accent-decorative: 12 65% 55%` pra usos non-text. Outros 3 pares (destructive, success, info) já estavam AA.

4. **Wave 4 — Variation docs**: criou `docs/08-variation-axes.md` (8 axes canonical) + `docs/09-class-defaults.md` (6 classes app + matrix).

5. **Wave 5 — SKILL.md rewritten**: decision tree 6 steps, `no_fork_rule` clause, normative/illustrative/legacy summary, 5 perguntas when-invoked-without-context.

## Wave 6+ candidates deferred (você listou)

| Item | Priority |
|---|---|
| Brand hardcoding em `ui_kits/default/components/*.jsx` (Sidebar, LoginScreen, StatCard) | Medium |
| `lovable-memory/design/tokens.md` ainda descreve burgundy/dorado (legacy) | Medium |
| `docs/07-component-patterns.md` sem axis cross-reference | Low |
| Automated contrast check script ausente | Medium |
| Preview cards single-flavor (só warm-editorial) | Low |
| `docs/04-using-with-lovable.md` preset-specific | Low |

## Restrições do Patrick (registradas no `anti-ai-design-system-registro-evolucao.md`)

1. **NÃO** criar `_template` separado agora
2. **NÃO** Storybook agora
3. **NÃO** package.json/CI agora
4. **NÃO** redesenhar default
5. **NÃO** mudar identidade cream/teal/terracotta sem necessidade
6. Skill alvo: Claude Code + Lovable (não npm package real)
7. Stack alvo: React/Tailwind primário, HTML/CSS secundário

## Perguntas que preciso responder

### 1. Estado pós-Wave 5: é "good enough" pra skill consumir produtivamente, OU ainda tem blockers?

Critério "good enough":
- Skill consegue audit + adapt sem ambiguidade
- Decision tree do SKILL.md elimina escolhas erradas (warm/teal/Lora aplicadas em fintech, por ex)
- Class defaults tabela usável em Phase 1 da skill

### 2. Wave 6+ priorização

Dos 6 itens deferred, quais são **bloqueantes** pra skill funcionar bem multi-classe vs **nice-to-have** que podem esperar 90+ dias?

Especificamente:
- **Brand hardcoding** (Sidebar/LoginScreen/StatCard): contradiz status "ilustrativo" do `ui_kits/default/`. Skill que copia esses pode acidentalmente herdar marca. **Bloqueante OU aceitável com warning?**
- **Lovable-memory legacy tokens**: README label legacy resolve OU precisa delete físico pra skill não acidentalmente consumir?
- **Contrast script**: ausência permite regression silenciosa. **Worth implementar agora (~1-2h) OU esperar primeiro problema real?**

### 3. Lacunas no v2 que você não previu

Olhando v2 frio:
- **GEO triggers PT-BR**: SKILL.md description tem foco EN structure. Em ecossistema do Patrick (PT-BR primário), faltam triggers fortes ("tira cara de IA", "deixa app bonito"). **Adicionar?**
- **Boundary com `design-system-audit` skillforge**: existem 2 skills relacionadas — `anti-ai-design` (v2, GERA usando este DS) vs `design-system-audit` (skillforge, AUDITA app contra QUALQUER DS, default anti-ai). **SKILL.md v2 deveria explicitar essa boundary?**
- **Component-axis matrix**: `docs/07` lista patterns mas não diz quais axes afetam cada um. Skill que adapta `PageHeader` por class precisa saber se `density` ou `nav` aplica. **Crítico ou eventual?**

### 4. Risco --accent shift propagação

`--accent` mudou ~13% L. Apps que já aplicaram preset original (chocotracking, dwg-experiment) podem quebrar visualmente. **Migration path:**
- Apps existentes precisam re-render visual review?
- `--accent-decorative` cobre 80% dos usos atuais (pill bgs, strips, dots)?
- Recomendação: ship novo + deprecation period, OU manter ambos (`--accent-fixed` + `--accent-original`) com flag por preset?

### 5. Decisões que precisam de Patrick (do handoff)

Re-confirmar pós-v2:
1. Foco: estabilizar OU expandir? (handoff Q1)
2. React/Tailwind primário ainda válido? (handoff Q2)
3. `default` continua com identidade própria? (handoff Q3)
4. Storybook/CI ainda OFF? (handoff Q4)
5. Lovable + Claude Code primário, npm package OFF? (handoff Q5)

## Output esperado

1. **Veredicto curto** (1 parágrafo): v2 é "good enough" pra skill OU não? Se não, qual o blocker mínimo?
2. **Wave 6 priorização**: tabela 3 colunas (item / blocker-or-niceToHave / esforço estimado)
3. **3 lacunas v2 não previstas**: GEO PT-BR + skill boundary + component-axis matrix — recomendação por item
4. **Migration plan --accent shift**: per-component classification + recomendação concreta
5. **Wave 6 minimum viable**: se só pudesse fazer 2-3 itens nos próximos 7 dias, quais?
6. **Out of scope reconfirm**: o que continua deferred sem prejuízo real?

## Limites

- Não propor `_template/`, Storybook, CI, package.json (Patrick excluiu)
- Não redesenhar default
- Manter identidade cream/teal/terracotta
- Foco: skill produtiva consumindo este DS hoje, não sistema npm distribuível futuro

## Files anexos (referência)

- `deep-research-report_github_anti_ai_design_system.md` — auditoria repo original
- `deep-research-report_web_search_anti_ai_design_system.md` — pesquisa externa multi-class
- `claude-design-handoff-anti-ai-design-system.md` — síntese 2 reports
- `anti-ai-design-system-registro-evolucao.md` — discussão Patrick + restrições
- `IMPLEMENTATION_REPORT.md` (dentro da pasta v2) — log Waves 1-5
- Repo atual v2 completo (substituiu original)

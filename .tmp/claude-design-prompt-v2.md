# Avaliação pós-Wave 5: anti-ai-design-system está pronto OU faltam próximos passos?

## Role

Você é avaliador frio de design system. Avaliou Waves 1-5 do `anti-ai-design-system` (ver IMPLEMENTATION_REPORT.md anexo). Agora preciso veredicto pós-v2 + priorização Wave 6+.

**Se precisar de detalhe específico do v2 antes de avaliar (file conteúdo, decisão técnica), pergunte antes de assumir.**

## Estado pós-Wave 5 (resumo)

Waves 1-5 done — detalhes em `IMPLEMENTATION_REPORT.md`:
- Wave 1: README normative/illustrative/legacy classification
- Wave 2: `<table>` contextual rule (era blanket ban)
- Wave 3: `--accent` AA fix (~13% L shift) + `--accent-decorative`
- Wave 4: `docs/08-variation-axes.md` + `docs/09-class-defaults.md`
- Wave 5: SKILL.md decision tree + `no_fork_rule` + 5 perguntas when-invoked

Wave 6+ deferred candidates listados em IMPLEMENTATION_REPORT seção 4 (não vou repetir aqui).

## Restrições Patrick

Detalhe em `anti-ai-design-system-registro-evolucao.md` seção 12. Resumo: mantém identidade cream/teal/terracotta intacta. Foco skill produtiva consumindo este DS hoje (Claude Code + Lovable), não distribuição npm.

## Perguntas

### 1. Estado pós-v2: good enough OU blocker?

Critério good enough:
- Skill audit + adapt sem ambiguidade
- SKILL.md decision tree elimina escolhas erradas (warm/teal/Lora aplicadas em fintech, ex)
- Class defaults usável Phase 1 da skill

### 2. Wave 6+ priorização

Dos 6 itens deferred, quais bloqueantes vs nice-to-have 90+ dias?

Foco:
- Brand hardcoding (`Sidebar.jsx`/`LoginScreen.jsx`/`StatCard.jsx`) — contradiz status "ilustrativo" do `ui_kits/default/`. Skill que copia herdar marca acidentalmente. Bloqueante OU aceitável com warning?
- Lovable-memory legacy tokens — README label legacy resolve OU precisa delete físico?
- Contrast script — vale ~1-2h agora OU esperar primeiro problema?

### 3. Lacunas v2 não previstas

- **GEO triggers PT-BR**: SKILL.md description foco EN structure. Ecossistema Patrick é PT-BR primário. Faltam triggers fortes ("tira cara de IA", "deixa app bonito"). Adicionar?
- **Boundary com `design-system-audit` skillforge**: 2 skills relacionadas — `anti-ai-design` (v2, gera USANDO este DS) vs `design-system-audit` (skillforge, audita app contra qualquer DS, default anti-ai). SKILL.md v2 deveria explicitar boundary?
- **Component-axis matrix**: `docs/07` lista patterns sem dizer quais axes afetam cada um. Skill que adapta `PageHeader` por class precisa saber se `density` ou `nav` aplica. Crítico ou eventual?

### 4. Risco --accent shift propagação

Apps que aplicaram preset original (chocotracking, dwg-experiment) podem quebrar visualmente:
- Re-render visual review necessário?
- `--accent-decorative` cobre ~80% dos usos atuais (pill bgs, strips, dots)?
- Recomendação: ship novo + deprecation period, OU manter ambos (`--accent-fixed` + `--accent-original`) com flag por preset?

### 5. Re-confirmar decisões Patrick (do handoff Q1-Q5)

Pós-v2, alguma muda?
1. Foco estabilizar OU expandir
2. React/Tailwind primário válido
3. `default` continua identidade própria
4. Storybook/CI off
5. Lovable + Claude Code primário, npm package off

## Output esperado

6 outputs estruturados:

1. **Veredicto** (1 parágrafo)
2. **Wave 6 priorização** (tabela 3 colunas)
3. **3 lacunas v2** (recomendação por item)
4. **Migration plan --accent** (per-component classification)
5. **Wave 6 minimum viable** (2-3 itens próximos 7d)
6. **Out of scope reconfirm** (continua deferred sem prejuízo real)

### Exemplo formato esperado output 1+2

```
## 1. Veredicto

v2 é good enough pra skill consumir. Decision tree + class defaults
resolvem 80% dos casos. Brand hardcoding em ui_kits é único blocker
medium pra skill multi-classe — workaround viável (warning na skill).
Pode lockar v2 + seguir Wave 7.5 (lock-in promotion).

## 2. Wave 6 priorização

| Item | Veredicto | Esforço |
|---|---|---|
| Brand hardcoding ui_kits | Blocker (skill copia marca acidentalmente) | 4-6h |
| Lovable-memory legacy | Nice-to-have (README label resolve) | 1h |
| Contrast script | Nice-to-have (regression risk baixo curto prazo) | 2h |
| Component-axis matrix docs/07 | Blocker se skill adapta multi-class | 3-4h |
| Preview cards single-flavor | Defer 90d | 8h+ |
| docs/04 preset-specific | Defer 90d | 2h |
```

## Limites

Mantém identidade cream/teal/terracotta. Sem `_template/`, Storybook, CI, package.json (Patrick excluiu). Foco skill produtiva hoje, não distribuição futura.

## Files anexos

- `deep-research-report_github_anti_ai_design_system.md` — auditoria repo original
- `deep-research-report_web_search_anti_ai_design_system.md` — pesquisa externa multi-class
- `claude-design-handoff-anti-ai-design-system.md` — síntese 2 reports
- `anti-ai-design-system-registro-evolucao.md` — discussão Patrick + restrições
- `IMPLEMENTATION_REPORT.md` (dentro da pasta v2) — log Waves 1-5
- Repo atual v2 completo (substituiu original)

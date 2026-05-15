# Avaliação pós-Wave 5: anti-ai-design-system está pronto OU faltam próximos passos?

## Role

Você é avaliador frio de design system. Avaliou Waves 1-5 do `anti-ai-design-system` (ver `IMPLEMENTATION_REPORT.md`). Agora preciso veredicto pós-v2 + priorização Wave 6+.

**Se precisar de detalhe específico do v2 antes de avaliar (file conteúdo, decisão técnica), pergunte antes de assumir.**

## Context update (importante — muda escopo de #3)

Resposta antecipada às 3 perguntas de clarificação que você fez:

### #3 — design-system-audit existe ou é projeto futuro?

**EXISTE em produção** no skillforge desde 2026-04-29 (commit 9bbf348). Skill ativa, validada via Input 52 (4/4 sinais Opus medium), candidate pra lock-in IL-10 Wave 7.5.

**Decisão Patrick — UMA skill só:** ele NÃO quer 2 skills competindo. Modelo desejado:

| Componente | Tipo | Onde |
|---|---|---|
| `design-system-audit` | **Única skill skillforge invocável** | `Documents/Github/skillforge-arsenal/skills/design-system-audit/SKILL.md` |
| `anti-ai-design-system/SKILL.md` (v2 que você gerou) | **Guidance/spec consumida** pela skill acima — NÃO skill standalone | dentro do repo `anti-ai-design-system` |
| `ui-design-system` | Skill skillforge separada (cria DS novo do zero) | scope diferente, não confunde |

**Implicação pra você:** SKILL.md v2 do anti-ai-design-system tem `user-invocable: true` + nome `anti-ai-design` — Patrick quer **mudar pra `user-invocable: false`** (vira guidance file lido pela design-system-audit Phase 2 Inventory, não skill independente).

Pergunta #3 reformulada: **avalie se SKILL.md v2 está bem desenhada PRA SER CONSUMIDA por design-system-audit** (não como skill standalone). design-system-audit/SKILL.md tem section "Default DS Reference" Phase 2 que faz `cat` dos files canônicos do repo — se SKILL.md v2 vira guidance, é file que essa Phase 2 lê.

### #1 — hardcoding ui_kits/default/components/*.jsx

**Já checado pra você** (anexo files no `.md` consolidado). Resumo:
- `Sidebar.jsx`: HSL bakeado (`hsl(338 55% 23%)` burgundy + `hsl(33 47% 53%)` dourado, NÃO `var(--primary)`/`var(--accent)`), `barry-callebaut-logo.svg`, `bc-icon.jpg`, "joao@barry-callebaut.com", "João Pereira" hardcoded
- `LoginScreen.jsx`: HSL primary bakeado, "ChocoTracking" + "Gestão de Embarques" + email Barry hardcoded
- `StatCard.jsx`: HSL accent bakeado (`hsl(33 47% 53%)`), `hsl(152 85% 30%)` success bakeado

**Severidade real:** alto. Não é só strings "Barry Callebaut" — é HSL value bakeado fora de tokens + asset paths brand-specific + person/email hardcoded. Skill que copia esses files pra novo app herda marca Choco.

**Pergunta #1 final:** dado o hardcoding real (não só string "Barry"), é **blocker** pra skill funcionar ou aceitável com warning explícito no SKILL.md v2 ("ui_kits são showcase de marca específica, não copiar literal — use como referência visual + traduzir pra tokens do target")?

### #2 — lovable-memory legacy tokens

**Já checado pra você** (anexo no consolidado). Resumo:
- `presets/default/lovable-memory/design/tokens.md` AINDA descreve burgundy `338 55% 23%` + dourado `33 47% 53%` (warm-editorial Choco)
- Wave 1 README label classificou como "legacy" mas **conteúdo do file NÃO foi reescrito**

**Pergunta #2 final:** label legacy resolve mesmo (file existe, README diz "ignorar")? Ou skill que faz `cat lovable-memory/design/tokens.md` numa Phase Inventory pode acidentalmente consumir esses valores como source-of-truth?

## Estado pós-Wave 5 (resumo)

Waves 1-5 done — detalhes em `IMPLEMENTATION_REPORT.md`:
- Wave 1: README normative/illustrative/legacy classification
- Wave 2: `<table>` contextual rule (era blanket ban)
- Wave 3: `--accent` AA fix (~13% L shift) + `--accent-decorative`
- Wave 4: `docs/08-variation-axes.md` + `docs/09-class-defaults.md`
- Wave 5: SKILL.md decision tree + `no_fork_rule` + 5 perguntas when-invoked

Wave 6+ deferred candidates listados em IMPLEMENTATION_REPORT seção 4.

## Restrições Patrick

Detalhe em `anti-ai-design-system-registro-evolucao.md` seção 12. Resumo: mantém identidade cream/teal/terracotta intacta. Foco skill produtiva consumindo este DS hoje (Claude Code + Lovable), não distribuição npm.

## Perguntas restantes (após context update)

### 1. Estado pós-v2: good enough OU blocker?

Critério good enough:
- design-system-audit consegue audit + adapt usando guidance v2 sem ambiguidade
- SKILL.md v2 (consumida como guidance) elimina escolhas erradas (warm/teal/Lora aplicadas em fintech)
- Class defaults usável Phase 1 da skill

### 2. Wave 6+ priorização

Dos 6 itens deferred, quais bloqueantes vs nice-to-have 90+ dias?

### 3. Lacunas v2 não previstas

- **GEO triggers PT-BR**: SKILL.md v2 description foco EN structure. Ecossistema Patrick é PT-BR primário. Faltam triggers fortes ("tira cara de IA", "deixa app bonito"). Adicionar **antes** de virar guidance, ou irrelevante porque guidance não dispara via maestro?
- **`user-invocable: true` → `false`**: precisa mudar pra virar guidance. Há outro ajuste estrutural na SKILL.md v2 pra deixar mais consumível pela design-system-audit Phase 2?
- **Component-axis matrix**: `docs/07` lista patterns sem dizer quais axes afetam cada um. Skill que adapta `PageHeader` por class precisa saber se `density` ou `nav` aplica. Crítico ou eventual?

### 4. Risco --accent shift propagação

Apps que aplicaram preset original (chocotracking, dwg-experiment) podem quebrar visualmente:
- Re-render visual review necessário?
- `--accent-decorative` cobre ~80% dos usos atuais (pill bgs, strips, dots)?
- Recomendação: ship novo + deprecation period, OU manter ambos (`--accent-fixed` + `--accent-original`) com flag por preset?

### 5. Re-confirmar decisões Patrick (handoff Q1-Q5)

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
3. **3 lacunas v2** (recomendação por item, incluindo conversão skill → guidance)
4. **Migration plan --accent** (per-component classification)
5. **Wave 6 minimum viable** (2-3 itens próximos 7d)
6. **Out of scope reconfirm** (continua deferred sem prejuízo real)

### Exemplo formato esperado output 1+2

```
## 1. Veredicto

v2 é good enough pra design-system-audit consumir como guidance. Decision tree
+ class defaults resolvem 80% dos casos. Hardcoding ui_kits é único blocker
medium pra skill multi-classe — workaround viável (warning na SKILL.md v2 "ui_kits
são showcase, não copiar literal"). Pode lockar v2 + seguir Wave 7.5.

## 2. Wave 6 priorização

| Item | Veredicto | Esforço |
|---|---|---|
| Hardcoding ui_kits (HSL + asset + email) | Blocker (skill copia marca acidentalmente) | 4-6h |
| Lovable-memory tokens conteúdo (não só label) | Nice-to-have se README label suficiente / Blocker se Phase 2 lê | 1-2h |
| Contrast script | Nice-to-have (regression risk baixo curto prazo) | 2h |
| Component-axis matrix docs/07 | Blocker se skill adapta multi-class | 3-4h |
| Preview cards single-flavor | Defer 90d | 8h+ |
| docs/04 preset-specific | Defer 90d | 2h |
```

## Limites

Mantém identidade cream/teal/terracotta. Sem `_template/`, Storybook, CI, package.json (Patrick excluiu). Foco design-system-audit produtiva hoje, não distribuição futura.

## Files anexos

- `deep-research-report_github_anti_ai_design_system.md` — auditoria repo original
- `deep-research-report_web_search_anti_ai_design_system.md` — pesquisa externa multi-class
- `claude-design-handoff-anti-ai-design-system.md` — síntese 2 reports
- `anti-ai-design-system-registro-evolucao.md` — discussão Patrick + restrições
- `IMPLEMENTATION_REPORT.md` — log Waves 1-5
- `claude-design-files-consolidado.md` — 6 files (3 .jsx + 1 tokens.md + 2 SKILL.md) pra responder #1, #2, #3 com base concreta
- Repo atual v2 completo (substituiu original)

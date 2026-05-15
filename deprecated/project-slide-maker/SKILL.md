---
name: project-slide-maker
description: "Gera apresentação de slides open-slide.dev a partir de repositório qualquer (path local/Lovable), embedando componentes live do anti-ai-ds CRM-validated + motion sofisticada (kanban moving, chat stagger, dashboard counter, form autofill) simulando uso real do produto. Combina repomix → narrative extraction → slide planning com decision tree de medium (CSS/framer-motion/lottie/rive/video) → anti-ai-ds bridge → motion patterns + demo choreography. Output: projeto open-slide consumer pronto via fork artemis-slides (zero patches manuais). Use em: gera deck do repo, monta apresentação do produto, slides pra reunião com prospect, deck pitch repositório, apresenta visualmente o que repo faz, slides ia-da-plus pra cliente, deck Plus IoT, material de pitch live components, deck Artemis. NÃO use para: material textual venda (sales-enablement), tokens DS do zero (ui-design-system), audit UX de app (ux-audit), motion strategy isolada (motion-design — esta INVOCA), authoring sem repo (open-slide create-slide direto)."
---

# Project Slide Maker

**Iron Law 1:** Componentes + tokens vêm do anti-ai-ds CRM-validated set, source = path local `Documents/Github/anti-ai-design-system/` (fallback remote clone). Nunca extraídos do repo target. MVP polish > genericidade. Reason: validado pelo Patrick (2026-05-04 v2). Component extractor real fica pra v2.

**Iron Law 2:** Cada slide declara medium (CSS / framer-motion / lottie / rive / video) com justificativa funcional + reduced-motion fallback. Sem isso, slide não está pronto. Reason: motion paga aluguel (motion-design IL1). Apresentação com motion arbitrário = ruído visual.

**Iron Law 3:** Repo comprehension via repomix antes de narrative. Narrative sem comprehension = alucinação. Reason: deep-research lesson learned. Sem dump estruturado, narrative inventa features que não existem.

## Modes

| Mode | Quando | Output |
|---|---|---|
| `--generate` (default) | Path de repo → quero deck | Projeto consumer pronto (`<repo>-deck/`) via cp template fork artemis-slides + slides .tsx |
| `--audit` | Deck open-slide existente | Findings: cada slide tem medium declarado? motion paga aluguel? reduced-motion? Tabela `Antes \| Depois \| Por que` |
| `--narrative-only` | Quero só narrative.md (skip slide planning) | Markdown estruturado: pitch + audience + value prop + key flows. Útil pra testar Layer 2 isolado |

## Input gate

Se invocação não trouxe repo path: pergunta uma vez "qual repo? (path local ou URL Lovable)". Resto usa defaults: output `Downloads/Slides Plus/<timestamp>-<repo-name>/`, audiência inferida via Phase 2, mediums via Phase 3 decision tree.

## Workflow

```
Project Slide Maker Progress:

- [ ] Phase 1: Repo Comprehension ⚠️ REQUIRED (IL3)
  - [ ] 1.1 Validar path do repo (existe? readable?). Se missing: pergunta uma vez.
  - [ ] 1.2 Rodar repomix --style xml --output ../_meta/repomix.xml
  - [ ] 1.3 Extrair: tipo (crm/dashboard/viewer/chat/...), stack, deps-chave, entry points, componentes-chave, fluxos
  - [ ] 1.4 Output: comprehension.json em ${out}/_meta/
- [ ] Phase 2: Narrative Extraction ⛔ BLOCKING
  - [ ] 2.1 Load references/02-narrative-template.md
  - [ ] 2.2 Input: comprehension.json + README.md do repo
  - [ ] 2.3 Output: narrative.md (pitch + audience + value-prop + 3-5 key flows)
  - [ ] 2.4 ⛔ GATE: apresentar narrative pro user antes de Phase 3. Sem aprovação, slide planning sai descalibrado.
- [ ] Phase 3: Slide Planning + Medium Decision
  - [ ] 3.1 Load references/01-medium-decision-tree.md
  - [ ] 3.2 Decidir N slides (5-15 MVP), tipos (cover/agenda/problem/solution/feature/demo/closing)
  - [ ] 3.3 Pra cada slide, assignar medium via decision tree
  - [ ] 3.4 Output: slide-plan.json
- [ ] Phase 4: Anti-AI-DS Bridge ⚠️ REQUIRED (IL1)
  - [ ] 4.1 Load references/03-anti-ai-ds-bridge.md
  - [ ] 4.2 Mapear comprehension.tipo → mapping anti-ai-ds CRM-validated
  - [ ] 4.3 Listar componentes a importar (button, sidebar, card, table, dialog, chart, ...)
  - [ ] 4.4 Tokens já baked em template/slides/global.css (skip Phase 4 token copy step — Mod 6 do fork)
- [ ] Phase 5: Motion Spec ⛔ BLOCKING (IL2 gate)
  - [ ] 5.1 Load references/04-motion-patterns-catalog.md
  - [ ] 5.2 Pra cada slide com medium != static, gerar spec canônico (invocar motion-design --spec se complexidade alta)
  - [ ] 5.3 ⛔ GATE: cada slide tem `// MEDIUM: <tipo> // FUNÇÃO: <observable>` no header + reduced-motion fallback?
- [ ] Phase 6: Orchestrator (artemis-slides consumer setup) — 4 steps v2
  - [ ] 6.1 Load references/05-orchestrator-recipe.md
  - [ ] 6.2 cp -r $OPEN_SLIDE_FORK/packages/cli/template <output>/<repo-name>-deck
  - [ ] 6.3 Wire @open-slide/core via file: link em package.json (Mod 1+2 baked no fork)
  - [ ] 6.4 npm install + Rive on-demand se algum slide.medium == 'rive'
  - [ ] 6.5 Escrever slides/<id>/index.tsx pra cada slide do plan
- [ ] Phase 7: Validation ⛔ BLOCKING (HTTP + runtime)
  - [ ] 7.1 npm run dev no consumer
  - [ ] 7.2 Curl /@id/virtual:open-slide/slides → todos slideIds presentes?
  - [ ] 7.3 Curl pre-transform de cada slide → HTTP 200 sem pre-transform error
  - [ ] 7.4 Runtime grep dev.log: error|Error|ENOENT|Failed to resolve|createRoot|named export|cannot find module
  - [ ] 7.5 ⛔ GATE: HTTP OK + runtime grep limpo? Se não, voltar Phase 6.
  - [ ] 7.6 Apresentar URL local pro user navegar
```

## Phase 1: Repo Comprehension

Sem dump estruturado, narrative aluciona. Repomix gera flat XML que LLM consome de uma vez.

```bash
cd <repo-path>
npx repomix --style xml --output ../_meta/repomix.xml
```

Flag mudou em repomix v1.14: `--output-style` → `--style`.

Extrair: `tipo` (heurística por deps), `stack`, `componentes-chave` (>100 lines, 3+ rotas), `fluxos` (rotas + sequência). Schema completo em `references/06-comprehension-schema.md`.

## Phase 2: Narrative Extraction (gate principal)

Load `references/02-narrative-template.md`. Anti-hallucination:
- Cite só features em comprehension.json
- Métricas só com evidência verificável (no README, código, ou comprehension)
- 3-5 fluxos críticos extraídos de comprehension.fluxos

⛔ GATE: apresentar narrative.md pro user antes de Phase 3. User aprova ou pede ajuste — pivot/audiência/tom emerge daqui em vez de Phase 0 questionnaire.

## Phase 3: Slide Planning

Load `references/01-medium-decision-tree.md`. Decision tree:
- `cover/hero` → video MP4 OU rive
- `demo` + drag/move → framer-motion (layoutId)
- `demo` + typing/sequence → framer-motion (stagger)
- `feature` static → CSS-only (tw-animate-css)
- `transcript`/`closing` → CSS-only
- icons + decorative → dotLottie
- hover/modal → CSS-only (View Transitions API)

## Phase 4: Anti-AI-DS Bridge (IL1)

Source = path local: `Documents/Github/anti-ai-design-system/`. Mapping completo em `references/03-anti-ai-ds-bridge.md`:

```
crm    → aa-btn, aa-sidebar, aa-card, aa-input → kanban-mock, kpi-strip, settings-list
chat   → aa-card, aa-input → wa-mock (sequence), conv-drawer
viewer → aa-card → flow (4 steps)
dashboard → aa-card → kpi-strip, chart-mock
data-tool → aa-card, aa-input → csv-mock
```

Tokens **já baked** em `template/slides/global.css` (Mod 6 fork). Skip Phase 4 token copy. Re-baka via `bash $OPEN_SLIDE_FORK/scripts/sync-anti-ai-ds-tokens.sh`.

Tipo sem mapping → falha vocal: "anti-ai-ds não tem mapping pra X. Usa CRM ou aborta?"

Componente novo no anti-ai-ds: PR no repo `anti-ai-design-system` primeiro, depois usa.

## Phase 5: Motion Spec (IL2 gate)

Cada slide com medium != 'static' tem header JSX:

```tsx
// MEDIUM: framer-motion (EXTENDED)
// FUNÇÃO: causalidade entre estados (kanban move)
// REDUCED-MOTION: snap sem transition
```

Slides complexos (5+ steps choreography) → `motion-design --spec`. Spec canônico em `${slide-id}/motion.spec.md`.

## Phase 6: Orchestrator (v2)

Load `references/05-orchestrator-recipe.md`. Receita 4 steps: cp template fork → wire `@open-slide/core` file: link → npm install (Rive on-demand) → escrever slides.

Mods 1-7 baked no fork — Phase 6 sub-steps: 7 → 4. Skill ~40% menor.

## Phase 7: Validation (HTTP + runtime)

HTTP-only não cobre runtime errors. 4 checks:
1. Dev server + `/@id/virtual:open-slide/slides` retorna todos slideIds
2. `/@fs/<abs>/slides/<id>/index.tsx` HTTP 200 sem pre-transform error
3. Runtime grep `grep -iE "error|ENOENT|Failed to resolve|createRoot|named export|cannot find module" dev.log` → vazio
4. ⛔ Gate: falha qualquer = não entrega.

## Anti-patterns

- Extrair componentes do repo target (Layer 4 real) — IL1 violation. MVP só anti-ai-ds.
- Slide com motion sem header `// MEDIUM:` — IL2 violation.
- Pular repomix → narrative direto do README — IL3 violation.
- Inferir tipo do repo sem comprehension.json.
- Slide com 5+ children variants stagger sem spec → motion-design --spec primeiro.
- Animation sem reduced-motion fallback — falha WCAG 2.3.3 + IL2 gate.
- Limite 5-15 slides MVP. Mais que isso = reunião prospect cansa.
- Componente novo no anti-ai-ds: PR no repo primeiro, depois consome.

## Pre-delivery checklist

- [ ] comprehension.json gerado e validado (tipo + stack + componentes-chave)
- [ ] narrative.md aprovado pelo user (Phase 2 gate)
- [ ] slide-plan.json com cada slide tendo `id`, `type`, `medium`, `content_brief`
- [ ] Phase 4: lista de componentes anti-ai-ds + mapping CSS pattern
- [ ] Cada slide tem header `// MEDIUM:` + `// FUNÇÃO:` + `// REDUCED-MOTION:`
- [ ] Phase 6: cp template fork OK + file: link OK + npm install OK
- [ ] `npm run dev` up + `/@id/virtual:open-slide/slides` retorna todos slideIds
- [ ] Cada slide route HTTP 200 + sem pre-transform error
- [ ] Runtime grep clean (sem `error|ENOENT|createRoot|named export`)
- [ ] N slides entre 5-15
- [ ] Reduced-motion fallback em cada slide com motion

## When NOT to use

| Situação | Use em vez disso |
|---|---|
| Material textual venda (1-pager, email) | `sales-enablement` |
| Tokens DS do zero | `ui-design-system --generate` |
| Audit UX em app (não deck) | `ux-audit` |
| Motion strategy isolada | `motion-design` (esta skill INVOCA) |
| Authoring slide sem repo | `open-slide create-slide` (built-in) |
| Gerar componente novo | `component-architect` |
| Repo comprehension genérica | repomix CLI direto |
| Apresentação Word/PowerPoint | `docx` |

## Integration

- `motion-design --spec` — Phase 5 quando complexidade alta (5+ steps).
- `repomix` (CLI external) — Phase 1. Flag v1.14+: `--style xml`.
- anti-ai-ds local (`Documents/Github/anti-ai-design-system/` filesystem) — fonte. Tokens baked em template/slides/global.css.
- artemis-slides fork (`Documents/Github/open-slide/`) — clone com Mod 1-7. Phase 6 cp template + file: link.
- `prompt-engineer --validate --type system-prompt` — Step 5+7 do skill-builder.
- `skill-builder --validate` — Step 7, valida estrutura.
- open-slide built-ins (`create-slide`, `slide-authoring`, `apply-comments`, `create-theme`) — invocadas dentro do consumer pos orchestrator.

## Example: input → output

**Input:** `--generate C:/Users/Patrick Neuhaus/Documents/Github/ia-da-plus`

**Phase 1 output** (`_meta/comprehension.json`):
```json
{
  "tipo": "crm",
  "stack": {"frontend": "react+vite", "backend": "supabase", "css": "tailwind"},
  "deps_chave": ["@radix-ui/*", "@tanstack/react-query", "recharts", "papaparse"],
  "componentes_chave": [{"path": "src/components/ClientTable.tsx", "papel": "tabela CRUD principal"}],
  "fluxos_inferidos": ["login → dashboard → /clients/:id → editar"]
}
```

**Phase 6 output** (`<repo-name>-deck/slides/03-kanban-demo/index.tsx`):
```tsx
// MEDIUM: framer-motion (EXTENDED)
// FUNÇÃO: causalidade espacial entre estados (kanban move)
// REDUCED-MOTION: snap sem transition
import './global.css';
import type { Page } from '@open-slide/core';
import { motion, AnimatePresence } from 'framer-motion';
const KanbanDemo: Page = () => { /* layoutId-based card move */ };
export default [KanbanDemo] satisfies Page[];
```

**Phase 7 output:** dev server `:5173/`, 7 slides renderizam, HTTP 200 + runtime grep limpo.

## References

| Arquivo | Conteúdo |
|---|---|
| `references/01-medium-decision-tree.md` | Decision tree slide.type → medium. |
| `references/02-narrative-template.md` | Anti-hallucination prompt template. |
| `references/03-anti-ai-ds-bridge.md` | Mapping `tipo → componentes` + CSS pattern. Source = path local. |
| `references/04-motion-patterns-catalog.md` | 10 patterns testáveis (kanban, chat, form, dashboard, cursor, modal, page, stagger, hover, pdf). |
| `references/05-orchestrator-recipe.md` | Receita Phase 6 v2: cp template + file: link + slide writes. |
| `references/06-comprehension-schema.md` | Schema JSON Phase 1 + heurísticas tipo. |
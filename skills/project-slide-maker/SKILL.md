---
name: project-slide-maker
description: "Gera apresentação de slides open-slide.dev a partir de repositório qualquer (path local/Lovable), embedando componentes live do anti-ai-ds CRM-validated + motion sofisticada (kanban moving, chat stagger, dashboard counter, form autofill) simulando uso real do produto. Combina repomix → narrative extraction → slide planning com decision tree de medium (CSS/framer-motion/lottie/rive/video) → anti-ai-ds bridge → motion patterns + demo choreography. Output: projeto open-slide consumer pronto. Use em: gera deck do repo, monta apresentação do produto, slides pra reunião com prospect, deck pitch repositório, apresenta visualmente o que repo faz, slides ia-da-plus pra cliente, deck Plus IoT, material de pitch live components, deck Artemis. NÃO use para: material textual venda (sales-enablement), tokens DS do zero (ui-design-system), audit UX de app (ux-audit), motion strategy isolada (motion-design — esta INVOCA), authoring sem repo (open-slide create-slide direto)."
---

# Project Slide Maker

**Iron Law 1:** Componentes vêm do anti-ai-ds CRM-validated set, nunca extraídos do repo target. MVP polish > genericidade. Reason: validado pelo Patrick (2026-05-04), Layer 4 redefinida como anti-ai-ds bridge. Component extractor real fica pra v2.

**Iron Law 2:** Cada slide declara medium (CSS / framer-motion / lottie / rive / video) com justificativa funcional + reduced-motion fallback. Sem isso, slide não está pronto. Reason: motion paga aluguel (motion-design IL1). Apresentação com motion arbitrário = ruído visual.

**Iron Law 3:** Repo comprehension via repomix antes de narrative. Narrative sem comprehension = alucinação. Reason: deep-research lesson learned (DR alucinou Repomix description). Sem dump estruturado, narrative inventa features que não existem.

## Modes

| Mode | Quando | Output |
|---|---|---|
| `--generate` (default) | Path de repo → quero deck | Projeto open-slide consumer pronto (`<repo>-deck/`), com slides .tsx + deps motion + patch Windows |
| `--audit` | Deck open-slide existente | Findings: cada slide tem medium declarado? motion paga aluguel? reduced-motion? Tabela `Antes \| Depois \| Por que` |
| `--narrative-only` | Quero só narrative.md (skip slide planning) | Markdown estruturado: pitch + audience + value prop + key flows. Útil pra testar Layer 2 isolado |

## Workflow

```
Project Slide Maker Progress:

- [ ] Phase 1: Repo Comprehension ⚠️ REQUIRED (IL3)
  - [ ] 1.1 Validar path do repo (existe? readable?)
  - [ ] 1.2 Rodar repomix --output-style xml
  - [ ] 1.3 Extrair: tipo (crm/dashboard/viewer/chat/...), stack, deps-chave, entry points, componentes-chave, fluxos
  - [ ] 1.4 Output: comprehension.json em ${out}/_meta/
- [ ] Phase 2: Narrative Extraction
  - [ ] 2.1 Load references/02-narrative-template.md
  - [ ] 2.2 Input: comprehension.json + README.md do repo
  - [ ] 2.3 Output: narrative.md (pitch + audience + value-prop + 3-5 key flows)
  - [ ] 2.4 ⛔ GATE: apresentar narrative pro user antes de Phase 3
- [ ] Phase 3: Slide Planning + Medium Decision
  - [ ] 3.1 Load references/01-medium-decision-tree.md
  - [ ] 3.2 Decidir N slides (5-15 MVP), tipos (cover/agenda/problem/solution/feature/demo/closing)
  - [ ] 3.3 Pra cada slide, assignar medium via decision tree
  - [ ] 3.4 Output: slide-plan.json
- [ ] Phase 4: Anti-AI-DS Bridge ⚠️ REQUIRED (IL1)
  - [ ] 4.1 Load references/03-anti-ai-ds-bridge.md
  - [ ] 4.2 Mapear comprehension.tipo → anti-ai-ds template (CRM-validated)
  - [ ] 4.3 Listar componentes a importar (button, sidebar, card, table, dialog, chart, ...)
  - [ ] 4.4 Pull tokens via anti-ai-ds token editor (HSL CSS vars)
- [ ] Phase 5: Motion Spec ⛔ BLOCKING (IL2 gate)
  - [ ] 5.1 Load references/04-motion-patterns-catalog.md
  - [ ] 5.2 Pra cada slide com medium != static, gerar spec canônico (invocar motion-design --spec se complexidade alta)
  - [ ] 5.3 ⛔ GATE: cada slide tem `// MEDIUM: <tipo> // FUNÇÃO: <observable>` no header + reduced-motion fallback?
- [ ] Phase 6: Orchestrator (open-slide consumer setup)
  - [ ] 6.1 Load references/05-orchestrator-recipe.md
  - [ ] 6.2 `npx @open-slide/cli init <repo-name>-deck` (ou skip se reuse projeto-deck existente)
  - [ ] 6.3 Aplicar patch Windows path (patch-package, validado 2026-05-04)
  - [ ] 6.4 Sobrescrever CLAUDE.md do consumer (libera deps motion)
  - [ ] 6.5 `npm install` deps necessárias baseado em mediums escolhidos
  - [ ] 6.6 Escrever `slides/<id>/index.tsx` pra cada slide do plan
- [ ] Phase 7: Validation ⛔ BLOCKING
  - [ ] 7.1 `npm run dev` no consumer
  - [ ] 7.2 Curl `http://localhost:5173/@id/virtual:open-slide/slides` → todos slideIds presentes?
  - [ ] 7.3 Curl pre-transform de cada slide → HTTP 200 sem pre-transform error
  - [ ] 7.4 ⛔ GATE: dev log sem error/Error/ENOENT? Se sim, deck OK. Se não, voltar Phase 6.
  - [ ] 7.5 Apresentar URL local pro user navegar
```

## Phase 1: Repo Comprehension

Sem dump estruturado, narrative aluciona. Repomix gera flat XML que LLM consome de uma vez. Pula etapa de tree walking.

```bash
cd <repo-path>
npx repomix --output-style xml --output ../_meta/repomix.xml
```

Extrair de repomix.xml:
- `tipo` — heurística: tem `recharts` + `@tanstack/react-query` + `@radix-ui` + tabela CRUD = `crm`. Tem `@uiw/react-md-editor` + `papaparse` = `data-tool`. Etc.
- `stack` — `package.json` deps (React?  Vue? Vite? Tailwind?)
- `componentes-chave` — files com >100 lines em `components/` que aparecem em 3+ rotas
- `fluxos` — rotas + sequência típica (ex: `/login → /dashboard → /clients/:id`)

Output schema em `references/06-comprehension-schema.md`.

## Phase 2: Narrative Extraction

Load `references/02-narrative-template.md`. Anti-hallucination prompt template:
- Cite só features que aparecem em comprehension.json
- Nunca afirme métricas sem evidência (não inventar "30% faster")
- 3-5 fluxos críticos extraídos de comprehension.fluxos

⛔ GATE: apresentar narrative.md pro user antes de Phase 3. Sem aprovação, slide planning sai descalibrado.

## Phase 3: Slide Planning

Load `references/01-medium-decision-tree.md`. Decision tree resumido:

```
slide.type == 'cover/hero' → video MP4 background OU rive
slide.type == 'demo' AND demo includes drag/move → framer-motion (kanban-style layoutId)
slide.type == 'demo' AND demo includes typing/sequence → framer-motion (stagger variants)
slide.type == 'feature' AND mostly static → CSS-only (tw-animate-css)
slide.type == 'transcript' OR 'closing' → CSS-only
icons + decorative micro-interactions → dotLottie
hover/modal/page-transition → CSS-only (View Transitions API)
```

## Phase 4: Anti-AI-DS Bridge (IL1)

Skill consome anti-ai-ds em vez de extrair do repo target. Mapeamento por tipo:

```
crm    → anti-ai-ds ?demo=crm    → button, sidebar, card, dialog, table, badge, dashboard
chat   → anti-ai-ds ?demo=chat   → message-bubble, input, sidebar, avatar
viewer → anti-ai-ds ?demo=viewer → toolbar, canvas, panel, slider
```

Tokens vêm do anti-ai-ds token editor (HSL CSS vars: `--background`, `--foreground`, `--accent`, `--sidebar-background`). Skill copia esses vars pro deck CSS root.

⚠️ MVP-only constraint: se `comprehension.tipo` não tem template anti-ai-ds equivalente, falha vocal: "anti-ai-ds não tem demo pra tipo X. v2 vai extrair direto. Aborta ou usa template genérico mais próximo?"

## Phase 5: Motion Spec (IL2 gate)

Cada slide com medium != 'static' tem header JSX:

```tsx
// MEDIUM: framer-motion (EXTENDED)
// FUNÇÃO: causalidade de movimento entre estados (kanban move)
// REDUCED-MOTION: snap sem transition (preserva info)
```

Pra slides complexos (demo com 5+ steps choreography), invocar `motion-design --spec` separado. Spec canônico fica em `${slide-id}/motion.spec.md`.

## Phase 6: Orchestrator

Load `references/05-orchestrator-recipe.md`. Receita testada (validation 2026-05-04):
1. `npx @open-slide/cli init <name>-deck`
2. Aplicar patch Windows path em `node_modules/@open-slide/core/dist/config-Bxtztw-H.js` linha 1965
3. `npm install --save-dev patch-package` + `npx patch-package @open-slide/core`
4. Sobrescrever consumer `CLAUDE.md` (libera deps motion)
5. `npm install` deps por medium (`framer-motion`, `@lottiefiles/dotlottie-react`, `@rive-app/react`)
6. Escrever slides

## Phase 7: Validation

Sem validation, deck pode dar 200 mas slide quebra render. Validation real:
1. Dev server up
2. `/@id/virtual:open-slide/slides` retorna todos slideIds
3. `/@fs/<abs-path>/slides/<id>/index.tsx` HTTP 200 + transformed sem erro de import
4. Dev log sem `error|Error|ENOENT|Failed to resolve`

⛔ Gate: falha qualquer = não entrega.

## Anti-patterns

- Extrair componentes do repo target (Layer 4 real) — IL1 violation. MVP só anti-ai-ds.
- Slide com motion sem header `// MEDIUM:` — IL2 violation. Reviewer não consegue auditar.
- Pular repomix → escrever narrative direto do README — IL3 violation. README mente, código é fonte de verdade.
- Não aplicar patch Windows path — slide route quebra com `/@fsC:/...`.
- Não sobrescrever consumer CLAUDE.md — Claude futuro lê "no deps" e remove framer-motion no próximo edit.
- Inferir tipo do repo sem comprehension.json — heurística sem evidência sai errada (CRM ≠ chat).
- Slide com 5+ children variants stagger sem spec → motion-design --spec primeiro.
- Componente novo no anti-ai-ds set sem aprovação Patrick — vira drift.
- Animation sem reduced-motion fallback — falha WCAG 2.3.3 + IL2 gate.
- Mais de 15 slides MVP — fica longo demais pra reunião prospect.

## Pre-delivery checklist

- [ ] comprehension.json gerado e validado (tipo + stack + componentes-chave preenchidos)
- [ ] narrative.md aprovado pelo user (Phase 2 gate)
- [ ] slide-plan.json com cada slide tendo `id`, `type`, `medium`, `content_brief`
- [ ] Phase 4: lista de componentes anti-ai-ds importados + tokens copiados
- [ ] Cada slide tem header `// MEDIUM:` + `// FUNÇÃO:` + `// REDUCED-MOTION:`
- [ ] patch-package aplicado (Windows) ou skip declarado (Linux/Mac)
- [ ] CLAUDE.md do consumer sobrescrito (libera deps)
- [ ] `npm run dev` up + `/@id/virtual:open-slide/slides` retorna todos slideIds
- [ ] Cada slide route HTTP 200 + sem pre-transform error
- [ ] Dev log limpo (sem `error|Error|ENOENT`)
- [ ] N slides entre 5-15
- [ ] Reduced-motion fallback declarado em cada slide com motion

## When NOT to use

| Situação | Use em vez disso |
|---|---|
| Material textual de venda (1-pager, email, deck textual) | `sales-enablement` |
| Definir tokens DS do zero pro projeto | `ui-design-system --generate` |
| Audit de UX em app (não deck) | `ux-audit` |
| Strategy de motion isolada (qual animar, sem repo) | `motion-design` (esta skill INVOCA pra spec) |
| Authoring de slide sem repo (assunto livre, não baseado em código) | `open-slide create-slide` (built-in) |
| Gerar componente novo (não importar) | `component-architect` |
| Repo comprehension genérica (não pra deck) | repomix CLI direto |
| Apresentação Word/PowerPoint formato corporate | `docx` |

## Integration

- `motion-design --spec` — invocada em Phase 5 quando slide.medium tem complexidade alta (5+ steps choreography). Spec canônico vira motion.spec.md no slide dir.
- `repomix` (CLI external, não skill) — Phase 1 dump estruturado.
- anti-ai-ds local (`localhost:8000/ui_kits/default/index.html?demo=<tipo>`) — fonte de componentes + tokens.
- `prompt-engineer --validate --type system-prompt` — Step 5+7 do skill-builder, valida texto desta SKILL.md.
- `skill-builder --validate` — Step 7, valida estrutura pré-zip.
- open-slide built-ins (`create-slide`, `slide-authoring`, `apply-comments`, `create-theme`) — invocadas pelo Claude Code DENTRO do consumer project criado, depois do orchestrator.

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

**Phase 6 output** (slide TSX gerado em `<repo-name>-deck/slides/03-kanban-demo/index.tsx`):
```tsx
// MEDIUM: framer-motion (EXTENDED)
// FUNÇÃO: causalidade espacial entre estados (kanban move)
// REDUCED-MOTION: snap sem transition (preserva info)
import type { Page } from '@open-slide/core';
import { motion, AnimatePresence } from 'framer-motion';
// ...componentes anti-ai-ds importados via Phase 4 bridge
const KanbanDemo: Page = () => { /* layoutId-based card move */ };
export default [KanbanDemo] satisfies Page[];
```

**Phase 7 output:** dev server up `http://localhost:5173/`, 7 slides renderizam, sem erro pre-transform.

## References

| Arquivo | Conteúdo |
|---|---|
| `references/01-medium-decision-tree.md` | Decision tree slide.type → medium. Justificativa DR03 pattern inventory. |
| `references/02-narrative-template.md` | Anti-hallucination prompt pra pitch + audience + value-prop + flows do comprehension.json. |
| `references/03-anti-ai-ds-bridge.md` | Mapping `tipo → anti-ai-ds demo + componentes`. Token copy recipe (HSL vars). |
| `references/04-motion-patterns-catalog.md` | 10 patterns testáveis: kanban-moving, chat-stagger, form-autofill, dashboard-counter, cursor-ghost, modal-slide, page-transition, stagger-list, hover-micro, pdf-region-select. Cada um com snippet TSX + duração + easing + reduced-motion. |
| `references/05-orchestrator-recipe.md` | Receita Phase 6 step-by-step, com patch Windows + CLAUDE.md override + npm install + slide writes. |
| `references/06-comprehension-schema.md` | Schema JSON da Phase 1 + heurísticas tipo (crm/chat/dashboard/viewer/...). |

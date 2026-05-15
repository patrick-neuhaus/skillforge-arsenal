# Skill Routing para Codex

Use as skills do SkillForge automaticamente quando o intent bater. Se uma skill obvia se aplica, invoque direto. Se 2+ aplicam ou o intent e ambiguo, use `maestro`.

## Triggers principais

| Intent do Patrick | Skill obrigatoria |
|---|---|
| editar `AGENTS.md`, rules, prompt, plano tecnico | `prompt-engineer --validate` |
| editar `SKILL.md`, boundary ou workflow de skill | `skill-builder --validate` + `prompt-engineer --validate` |
| criar skill nova | `skill-builder` Step 0, depois `--full` se passar |
| "tem algo pronto?", "ja existe ferramenta?" | `reference-finder --solution-scout` |
| "review" ambiguo | perguntar: codigo, UX, visual/DS ou prompt |
| review de codigo, bug, DRY/KISS, SOLID | `trident` |
| review de UX, fluxo ruim, usabilidade | `ux-audit` |
| review visual, UI inconsistente, maturidade visual | `ui-design-system --audit` |
| prompt ruim, system prompt, JSON de IA | `prompt-engineer` |
| chain de skills, qual skill usar | `maestro` |
| n8n, workflow quebrando, automacao | `n8n-architect` |
| Supabase, schema, RLS, policies | `supabase-db-architect` |
| Lovable direto vs prompt | `lovable-router` |
| knowledge do Lovable | `lovable-knowledge` |
| design tokens, cores, fonte, paleta, breakpoints, primitives, motion funcional | `ui-design-system --generate` |
| design system maturity, "o DS esta coerente?", maturidade visual | `ui-design-system --audit` |
| auditoria de design system externo, shadcn/Material/Chakra/Carbon, "tira cara de IA" | `design-system-audit` |
| componente grande/refatorar componente, anatomia, slots, variants, props | `component-architect --plan` |
| contrato de estados do componente, loading/disabled/focus/pressed, microinteracao de estado | `component-architect --plan` |
| arquitetura thin client/backend/frontend | `architecture-guard` |
| React performance, useEffect, rerender | `react-patterns` |
| cross-browser, Safari/Firefox/Edge, build target, Browserslist, Playwright multi-engine | `react-patterns --audit-cross-browser` |
| motion criativo, animacao, UI feel, polish de interacao, microinteraction, botao parece morto, dropdown lento, popover estranho, parallax, scrollytelling, Lottie/Rive/GSAP/Three.js | `motion-design` |
| tokenizar press/easing/duration, motion tokens, press state como sistema | `ui-design-system --generate` |
| security, injection, vazamento | `security-audit` |
| SEO, programmatic SEO, keyword | `seo` ou `ai-seo` conforme foco |
| copy, landing text, email, ad | `copy` |
| posicionamento, ICP, diferencial | `product-marketing-context` |
| pitch, one-pager, material vendas | `sales-enablement` |
| GTM, lancamento, Product Hunt | `launch-strategy` |
| ferramenta gratis, lead magnet | `free-tool-strategy` |
| contexto antes de limpar sessao | `context-guardian` |
| memoria persistente, catalogar aprendizado | `context-tree` |
| plan/spec antes de codar | `sdd` |
| transcricao, daily, extrair tasks | `meeting-sync` |
| VPS, Docker, EasyPanel, infra | `vps-infra-audit` |
| "less tokens", "be brief", "responde curto" | aplicar estilo Caveman terse se skill/plugin Caveman nao existir |
| config via linguagem natural, settings | update-config se existir; senao editar config com validacao |
| recurring task, self-paced iteration, loop | `loop` se existir; senao `schedule` para automacao recorrente |

## Regra anti-falso positivo

"Review" sozinho e sempre ambiguo. Pergunte o alvo antes de invocar skill.

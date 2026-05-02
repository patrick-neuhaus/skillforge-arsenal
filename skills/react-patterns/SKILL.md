---
name: react-patterns
description: "Audit and implement modern React/Next.js patterns AND diagnose cross-browser/runtime issues in React stacks. Server Components, App Router, Server Actions, Suspense, error boundaries, data fetching, caching, hydration. PLUS: build target (Vite/Next config, Browserslist, Autoprefixer, Babel/SWC), polyfills, ESM/dynamic import, browser API support, CSS rendering bugs (flex auto-min, sticky in overflow ancestor, stacking context with transform), Playwright multi-engine testing. Use when user asks to: audit React code, fix React anti-patterns, migrate to App Router, server vs client component, scaffold Next.js feature, optimize React performance, fix hydration errors, fix useEffect, re-render excessivo, 'tá pesado o React', AND ALSO: 'funciona no Chrome, quebra no Firefox/Safari/Edge', 'tela branca em produção', 'modal atrás do header', 'sticky não gruda', 'sticky some', 'cards explodem largura', 'login perde sessão no Safari', 'date picker some no iOS', 'copy/paste falha em Firefox', 'autoplay não toca', 'app não monta em browser X', cross-browser bug, browser compatibility, Vite build target, Browserslist, Playwright projects, multi-engine test. Supports: pattern audit, scaffolding, migration, performance review, cross-browser audit. Does NOT cover: visual tokens / breakpoints / motion-as-system (ui-design-system), heuristics / WCAG criteria / user flow audit (ux-audit), component anatomy / slots / variants (component-architect), adherence to external DS (design-system-audit)."
---

# React Patterns

## Iron Laws (3)

1. **Thin Client, Fat Server.** NEVER put business logic in client components. Zero `fetch()`, zero data transformation, zero validation in `'use client'` files. If it doesn't need `useState`, `useEffect`, or browser APIs, it's a Server Component.

2. **[NOVO] Multi-engine evidence before any cross-browser patch.** Nunca diagnostique "bug do Firefox/Safari/Edge" sem reproduzir em ambiente isolado **e** confirmar a feature em MDN BCD / Can I Use / wpt.fyi. Se você não consegue reproduzir e não consegue citar fonte de baseline, **não é diagnóstico — é palpite**, e palpite vira regressão no Chrome.

3. **[NOVO] Triagem antes do patch.** Antes de absorver um sintoma, classifique: é React pattern? CSS de composição? UI/visual de design system? UX observável? Bug funcional? Cada destino tem dono diferente. Skill correta = patch correto. Skill errada = relatório que ninguém executa.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--audit` | Check for anti-patterns in current code | default |
| `--scaffold` | Scaffold feature with correct patterns | - |
| `--migrate` | Fix anti-patterns (client logic → server) | - |
| `--audit-cross-browser` **[NOVO]** | Audita compatibilidade cross-browser, build target, polyfills, features arriscadas | - |
| `--include-cross-browser` **[NOVO]** | Flag para `--audit` rodar a Fase 5 (cross-browser) também | - |

## Workflow

```
React Patterns Progress:

- [ ] Phase 0: [NOVO] Triagem do sintoma ⚠️ REQUIRED
  - [ ] 0.1 Sintoma é React pattern, CSS de composição, UI visual, UX, ou bug funcional?
  - [ ] 0.2 Se UX puro → encaminhar para ux-audit
  - [ ] 0.3 Se token / motion / breakpoint / primitive → encaminhar para ui-design-system
  - [ ] 0.4 Se anatomia / slots / variants → encaminhar para component-architect
  - [ ] 0.5 Se adesão a DS externo → encaminhar para design-system-audit
  - [ ] 0.6 Se bug funcional puro → encaminhar para trident
  - [ ] 0.7 Se cabe aqui → seguir Phases 1–6
- [ ] Phase 1: Stack Detection ⚠️ REQUIRED
  - [ ] 1.1 Detect framework (Next.js version, Remix, Vite, CRA)
  - [ ] 1.2 Identify state management (Zustand, Jotai, Redux, Context)
  - [ ] 1.3 Check styling approach (Tailwind, CSS Modules, styled-components)
  - [ ] 1.4 Check data fetching (React Query, SWR, server actions, tRPC)
  - [ ] 1.5 [NOVO] Capture build target: Vite `build.target`, `@vitejs/plugin-legacy`, Next config, Browserslist, Autoprefixer, Babel/SWC targets
  - [ ] 1.6 [NOVO] Capture browser matrix declarada (Browserslist real ou política do time)
- [ ] Phase 2: Pattern Audit (existente)
  - [ ] Load references/pattern-guide.md
  - [ ] 2.1 Server vs Client component boundaries
  - [ ] 2.2 Data fetching patterns
  - [ ] 2.3 State management patterns
  - [ ] 2.4 Error/loading handling
- [ ] Phase 3: Recommendations ⛔ BLOCKING (existente)
  - [ ] Present findings with before/after examples
  - [ ] ⛔ GATE: Get approval before modifying code
- [ ] Phase 4: Implement (existente)
  - [ ] Apply approved patterns
- [ ] Phase 5: [NOVO] Cross-browser audit (condicional: `--audit-cross-browser` ou `--include-cross-browser`, ou disparada por sintoma técnico)
  - [ ] Load references/cross-browser-checklist.proposto.md
  - [ ] 5.1 Browser API checklist (Clipboard, Storage Access, autoplay, codecs, showPicker, Pointer Events)
  - [ ] 5.2 CSS support checklist (anchor positioning, popover, dialog, container queries, dvh/svh/lvh, :has, :focus-visible, backdrop-filter, color())
  - [ ] 5.3 Rendering bugs sweep (flex auto-min, sticky in overflow ancestor, stacking context com transform/filter/perspective)
  - [ ] 5.4 Native inputs sweep (date/time/color picker, atributos avançados, fallback)
  - [ ] 5.5 Build target review → Load references/build-targets-and-polyfills.proposto.md
  - [ ] 5.6 Test strategy review → Load references/playwright-browser-matrix.proposto.md
  - [ ] 5.7 Rubrica de bug aplicada (severidade, evidência, hipótese técnica, teste de confirmação, fix proposto, risco de regressão no Chrome, critério de aceite)
- [ ] Phase 6: [NOVO] Síntese cross-browser ⛔ BLOCKING (apenas em Fase 5)
  - [ ] 6.1 Cada bug com formato canônico (severidade, browser/versão/SO, evidência, hipótese, fix, critério de aceite)
  - [ ] 6.2 Riscos de regressão no Chrome listados explicitamente
  - [ ] 6.3 Apresentar antes de implementar — gate humano obrigatório
```

## Phase 0: [NOVO] Triagem do sintoma

| Sintoma | Cabe aqui? | Onde mais |
|---|---|---|
| `'use client'` no topo da página inteira | ✅ Pattern audit | — |
| `useEffect` para fetch de dados | ✅ Pattern audit | — |
| Re-render excessivo, perf React | ✅ Pattern audit (perf) | — |
| Hydration error | ✅ Pattern audit (hydration) | — |
| **Tela branca antes de renderizar em browser X** | ✅ Cross-browser (build target / ESM / transpilation) | — |
| **App "funciona em Chrome, quebra em Firefox/Safari"** | ✅ Cross-browser | — |
| **Modal atrás do header / sticky não gruda / cards explodem** | ✅ Cross-browser (rendering bugs); regra preventiva mora em `ui-design-system` | `ui-design-system` |
| **Login com SSO perde sessão fora do Chrome** | ✅ Cross-browser (storage/cookies/Storage Access) | — |
| **Date/time/color picker some ou muda muito** | ✅ Cross-browser (inputs nativos) | `ui-design-system` (wrapper visual) |
| **Copy/paste falha em browser X** | ✅ Cross-browser (Clipboard API) | — |
| **Autoplay não toca / mídia falha** | ✅ Cross-browser (autoplay/codecs) | — |
| Definir cor primária / spacing / motion como sistema | ❌ | `ui-design-system` |
| Auditar UX, fluxos, heurísticas | ❌ | `ux-audit` |
| Definir anatomia/slots/variants | ❌ | `component-architect` |
| Verificar adesão ao shadcn/Material/Carbon | ❌ | `design-system-audit` |
| API quebrada, dado perdido | ❌ | `trident` |
| WCAG limiares (4.5:1, 3:1, 24×24, reflow 320) | ❌ (importa, não define) | `ux-audit` (canônico) |

## Phase 1: Stack Detection (com extensão cross-browser)

Check these files:
- `package.json`, `next.config.*`, `vite.config.*`, `tsconfig.json`, `app/` vs `pages/`, `tailwind.config.*` (existente).
- **[NOVO] `.browserslistrc` / `browserslist` em package.json** — alvo declarado.
- **[NOVO] `vite.config.*` `build.target`** — alvo real do bundle moderno.
- **[NOVO] `@vitejs/plugin-legacy`** — fallback para browsers fora do alvo moderno.
- **[NOVO] Babel/SWC config** — `targets` ou herança de Browserslist.
- **[NOVO] PostCSS/Autoprefixer config** — lê Browserslist por padrão.

Report: "[Framework] [Version] with [State Mgmt] + [Data Fetching] + [Styling] + [NOVO: Build target X, Browserslist Y, Legacy plugin Z]".

## Phase 2: Pattern Audit (inalterado)

Load `references/pattern-guide.md`. (Conteúdo existente — Server vs Client Decision Tree, Key Patterns, Anti-patterns clássicos do App Router — preservado em pattern-guide.md sem mudança.)

## Phase 3: Recommendations (inalterado)

⛔ **GATE:** Do NOT modify code without explicit user approval.

## Phase 4: Implement (inalterado)

## Phase 5: [NOVO] Cross-browser audit

**Quando disparar:**

1. Usuário invoca `--audit-cross-browser` explicitamente.
2. Usuário invoca `--audit --include-cross-browser`.
3. Triagem da Phase 0 detectou sintoma técnico cross-browser.

**Não disparar:** auditoria geral de React patterns. Cross-browser não roda por padrão para evitar inflar relatórios.

**Carrega 3 references:**
- `references/cross-browser-checklist.proposto.md` — checklist por categoria (browser APIs, CSS, rendering, inputs nativos).
- `references/build-targets-and-polyfills.proposto.md` — Vite/Next/Babel/SWC/Browserslist alinhados.
- `references/playwright-browser-matrix.proposto.md` — matriz mínima de teste multi-engine.

**Output:** rubrica de bug com formato canônico.

```
Bug: [nome curto]
Severidade: Crítica | Alta | Média | Baixa
Browser/Versão/SO: [específico]
Evidência: [vídeo/screenshot/console/network]
Componente/Rota: [caminho]
Hipótese técnica: [feature suspeita / pipeline / política]
Teste de confirmação: [como reproduzir em ambiente limpo + outro engine]
Fix proposto: [progressive enhancement / @supports / fallback / config]
Risco de regressão no Chrome: [explícito]
Critério de aceite: [como validar que corrigiu sem quebrar Chrome]
```

## Phase 6: [NOVO] Síntese cross-browser ⛔ BLOCKING

⛔ Gate: nenhum bug cross-browser sem critério de aceite. Nenhum patch que regrida o caminho feliz no Chrome. Apresentar antes de implementar.

## Anti-Patterns (existentes preservados + novos)

**Existentes (preservados):**
- `useEffect` para data fetching no App Router
- `'use client'` em nível de página
- Business logic em client
- Prop drilling 3+ níveis
- `useEffect` para derived state
- Fetching no parent passando para filhos
- `React.memo` everywhere

**[NOVO] Cross-browser:**
- **Browser sniffing por UA string** em vez de feature detection / `@supports`.
- **Suposição "Chrome = web"** — testar só no engine principal e enviar.
- **Polyfill defensivo** — instalar polyfill sem confirmar que a feature realmente é usada e que o alvo precisa.
- **`100vh` em mobile** — usar `dvh/svh` quando aplicável.
- **`transform` em ancestor de modal/dropdown/sticky** sem entender que cria stacking context e containing block (regra preventiva mora em `ui-design-system`; aqui é diagnóstico).
- **Patch que conserta um browser e quebra o Chrome** — Iron Law 2 violada.
- **"Funciona em produção"** sem evidência multi-engine — Iron Law 2 violada.
- **Feature de baseline incerto sem `@supports`** ou fallback (popover, anchor positioning, multiple import maps, alpha/colorspace em color input).

## Pre-Delivery Checklist (existentes preservados + novos)

**Existentes:**
- [ ] Confirmed framework and version
- [ ] Server Components default; `'use client'` só onde precisa
- [ ] No `fetch()` ou data transforms em client
- [ ] Loading states (Suspense ou loading.tsx)
- [ ] Error boundaries (error.tsx)
- [ ] No `useEffect` para fetch
- [ ] Images via `next/image` (Next.js)

**[NOVO] Cross-browser (apenas em Phase 5):**
- [ ] Browserslist e build.target declarados e coerentes
- [ ] `@vitejs/plugin-legacy` configurado se a matriz inclui browsers fora do alvo moderno
- [ ] Features arriscadas (popover, anchor, multiple import maps, clipboard avançado, alpha/colorspace) com `@supports` ou fallback
- [ ] Teste Playwright em chromium + firefox + webkit para fluxos críticos
- [ ] Pelo menos 1 passe manual em Safari/iOS real para fluxos com input nativo, mídia, SSO
- [ ] Cada bug cross-browser com critério de aceite + risco de regressão no Chrome explícito
- [ ] Nenhum browser sniffing introduzido (preferir feature detection)

## When NOT to use

- Non-React project → não aplicável
- React Native → padrões diferentes
- Pure styling/visual tokens / motion as system → `ui-design-system`
- WCAG / heuristics / user flow audit → `ux-audit`
- Component anatomy/slots/variants → `component-architect`
- External DS adherence (shadcn/Material/Carbon) → `design-system-audit`
- Functional bug, broken API → `trident`

## Integration

- **`ui-design-system`** — Provê tokens, motion-as-system, primitives, regras CSS preventivas (ex.: "nunca `transform` em ancestor de modal"). Esta skill **diagnostica** sintomas; aquela **prescreve** regra.
- **`ux-audit`** — Provê WCAG limiares (4.5:1, 3:1, 24×24, reflow 320, prefers-reduced-motion) que esta skill consome em testes técnicos (axe, focus-visible, ARIA). Não reabrimos teoria de WCAG.
- **`component-architect`** — Define anatomia/slots; esta skill garante que padrões React/Next sejam aplicados corretamente sobre essa anatomia.
- **`design-system-audit`** — Verifica adesão a DS externo. Não tem overlap.
- **`trident`** — Code review geral; rode `--audit` antes de Trident para pegar React-specific.
- **`sdd`** — `--scaffold` durante implement phase.
- **Maestro** — Orquestra Phase 0 → encaminhamento.

### Remotion Patterns
Load `references/remotion-react-patterns.md` para padrões React específicos de Remotion (preservado).

### Motion Animations
Quando construir UI interativa com Framer Motion / Motion library, combine boundaries server/client desta skill com APIs de animação — animações são sempre client-only.

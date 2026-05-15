# Wave 6 MVP final + Wave 6.5 Component Library — execução completa

## Role

Você é arquiteto de design system entregando 2 waves consecutivas em 1 round. Outro Claude (não você) vai aplicar TUDO no repo `anti-ai-design-system` em 1 batch. Output deve ser self-contained, byte-aplicável, sem ambiguidade.

**Se precisar de detalhe técnico não coberto nos files anexos, pergunte antes de assumir.**

## V3 Baseline State

V3 (que você gerou) entregou Waves 1-5 + 5 componentes novos:

**Aplicado em v3:**
- ✅ docs/08-variation-axes.md (8 axes full)
- ✅ docs/09-class-defaults.md (matrix 6 classes × 8 axes)
- ✅ tokens.css com `--accent-decorative` + AA fixes (--accent darkened, --destructive/success/info AA-tuned, status pills foreground darkened)
- ✅ SKILL.md decision tree + no_fork_rule + normative/illustrative/legacy
- ✅ README.md normative/illustrative/legacy section
- ✅ docs/01 `<table>` contextual rule
- ✅ Componentes NOVOS: PageHeader.jsx (brand-agnostic, tokens), DashboardScreen.jsx (composition pattern), RomaneiosScreen.jsx, Icon.jsx (~30 icons lucide-style), app.jsx (harness)

**NÃO aplicado em v3 (Wave 6 fixes ainda pendentes):**
- ❌ Sidebar.jsx HSL bakeado (`hsl(338 55% 23%)` borgonha legacy!) + persona hardcoded
- ❌ LoginScreen.jsx HSL bakeado + "ChocoTracking" + email Barry hardcoded
- ❌ StatCard.jsx HSL bakeado dourado
- ❌ SKILL.md `user-invocable: true` (Patrick decidiu virar `false` — file vira guidance, não skill standalone)
- ❌ SKILL.md name `anti-ai-design` (Patrick quer rename `anti-ai-design-system-spec`)
- ❌ lovable-memory tokens.md DELETE (ainda descreve burgundy/dorado legacy)
- ❌ Placeholder SVGs (assets/placeholder-logo.svg + placeholder-mark.svg)
- ❌ index.html harness pra props brand/user/appName

**Plus Wave 6.5 Component Library (não tocada):**
- ❌ ~30 componentes brand-agnostic categorizados
- ❌ Showcase pages categorizadas (preview/ atual é individual cards, não biblioteca navegável)
- ❌ docs/10-component-composition.md
- ❌ docs/07 update com axis cross-reference

## Razão Wave 6.5 não é overengineering

- Skill `design-system-audit` Phase 2 lê biblioteca como spec canônica
- Skill `design-system-audit` Phase 6 `--bootstrap` mode usa biblioteca pra scaffold app from scratch
- Apps consumidores pegam padrão consistente em vez de Claude inventar shadcn random
- Reduz "cara de IA" — biblioteca consagrada > improvisação
- Reuso cross-projects (chocotracking, charming-solutions, dwg, futuros templates Lovable)

## Wave 6 MVP fechamento (~1.5h)

### Entregável 1: Refactor 3 .jsx (Wave 6 round anterior pendente)

Refactor `ui_kits/default/components/Sidebar.jsx`, `LoginScreen.jsx`, `StatCard.jsx` seguindo padrão PageHeader.jsx (brand-agnostic, tokens, props).

**Sidebar.jsx target:**
- HSL → tokens: `hsl(var(--sidebar-background))`, `hsl(var(--sidebar-accent))` (active+hover), `hsl(var(--sidebar-border))`, `hsl(var(--accent-decorative))` (3px indicator), `hsl(var(--accent))` (avatar bg c/ texto white AA)
- Asset paths → props `brand={ logo, mark, name }` com defaults `assets/placeholder-logo.svg` + `assets/placeholder-mark.svg`
- Persona → props `user={ name, email }` com defaults "Nome Sobrenome" + "email@exemplo.com" + helper `initialsFrom(name)` derivar iniciais
- Nav groups → prop `groups` com `DEFAULT_GROUPS` extraído

**LoginScreen.jsx target:**
- HSL primary panel → `hsl(var(--primary))` + `hsl(var(--primary-foreground))`
- Background panel → `hsl(var(--background))`
- Copy → props `appName` + `tagline` com defaults "App Name" + "Tagline"
- Asset → prop `brand.logo` placeholder
- Email pre-fill → state vazio
- Estrutura split 50/50 manter (`flex: 1` ambos)

**StatCard.jsx target:**
- chip bg `hsla(33 47% 53% / .1)` → `hsl(var(--accent-decorative) / .1)` (decorativo, alpha desatura)
- icon stroke `hsl(33 47% 53%)` → `hsl(var(--accent))` (functional, AA contra --card)
- success trend `hsl(152 85% 30%)` → `hsl(var(--success))`
- destructive → `hsl(var(--destructive))`

### Entregável 2: SKILL.md → guidance

Aplicar 4 mudanças mínimas:

1. `user-invocable: true` → `user-invocable: false`
2. Rename `name: anti-ai-design` → `name: anti-ai-design-system-spec`
3. Description nova perspectiva file consumido: "Specification for the Anti-AI Design System. Consumed by design-system-audit (Phase 2 Inventory) and any other tool that needs the system's invariants, axes, and class defaults. Not a standalone skill."
4. Adicionar section logo no início:
   ```
   ## How this file is consumed
   
   - Primary consumer: design-system-audit skill at ~/Documents/Github/skillforge-arsenal/skills/design-system-audit/SKILL.md
   - Canonical files cat'd by Phase 2 Inventory: docs/03, docs/07, docs/08, docs/09, presets/default/tokens.css, README normative/illustrative/legacy section
   - To use this design system: invoke design-system-audit. Do not invoke this file as a skill — user-invocable: false is intentional.
   ```

Resto do conteúdo (decision tree, no_fork_rule, key files) preserva.

### Entregável 3: Delete lovable-memory tokens.md

Conteúdo descreve burgundy+dorado (legacy), contradiz tokens.css atual (teal+terracotta).

```bash
rm presets/default/lovable-memory/design/tokens.md
# Se pasta vazia após delete, deletar pasta também
# Se outros files dentro lovable-memory/, NÃO deletar pasta-mãe
```

### Entregável 4: Placeholder SVGs

Criar 2 files mínimos brand-agnostic:

- `assets/placeholder-logo.svg` — retângulo neutro ~120×40px com texto "LOGO" centralizado, `currentColor` (herda token consumer)
- `assets/placeholder-mark.svg` — quadrado neutro ~40×40px com letra "M" centralizada, `currentColor`

SVG inline mínimo, sem brand color hardcoded.

### Entregável 5: index.html harness update

Atualizar harness pra passar props pros componentes refatorados:

```jsx
<Sidebar
  brand={{ logo: "../../assets/placeholder-logo.svg", mark: "../../assets/placeholder-mark.svg", name: "App" }}
  user={{ name: "Nome Sobrenome", email: "email@exemplo.com" }}
  groups={DEFAULT_GROUPS_OR_CUSTOM}
  active={...} onNavigate={...} onToggleCollapse={...} onLogout={...}
/>

<LoginScreen
  brand={{ logo: "../../assets/placeholder-logo.svg", name: "App" }}
  appName="App Name"
  tagline="Tagline"
  onLogin={...}
/>
```

Output: trecho do harness que mudou (não file inteiro — index.html v3 atual é grande).

## Wave 6.5 Component Library (~15-25h)

### Estrutura proposta

```
ui_kits/default/components/
├── base/          # Button, Input, Textarea, Select, Combobox, Checkbox, Radio, Switch, Slider
├── surfaces/      # Card, Surface, Dialog, Drawer, Tooltip, Popover, Toast
├── navigation/    # Sidebar (refactored), Tabs, Breadcrumb, Pagination
├── display/       # Badge, StatusBadge, Tag, Avatar, Alert, Callout, EmptyState, Skeleton
├── data/          # Table (semantic), AppTable (sortable), ListItem
├── layout/        # PageHeader (existing v3), PageShell, AppLayout, Section
├── dashboard/     # StatCard (refactored), KpiGrid, MetricCard, ChartCard
├── forms/         # FormField, FieldGroup, Fieldset
├── auth/          # LoginScreen (refactored), RegisterScreen, ForgotPasswordScreen
└── screens/       # DashboardScreen (existing v3), RomaneiosScreen (existing v3) — Screen-level templates
```

**Total: ~33 componentes + 5 screens.** Existing 3 refatorados ficam em subpastas apropriadas. Sidebar → navigation/, LoginScreen → auth/, StatCard → dashboard/. PageHeader v3 → layout/. DashboardScreen + RomaneiosScreen v3 → screens/. Icon.jsx fica em raiz `components/Icon.jsx` (registry shared).

**StatusBadge atual está inline em DashboardScreen.jsx** — extrair pra `display/StatusBadge.jsx` standalone.

**Se algum componente acima não fizer sentido OU faltar componente óbvio, sinaliza no output e propõe ajuste.**

### Categorias prioridade

- **P0 (build full agora):** base, surfaces, display, layout, forms — universais
- **P1 (build full agora):** navigation, data, dashboard — comuns
- **P2 (build mínimo):** auth (RegisterScreen + ForgotPasswordScreen — LoginScreen já existe v3 só precisa refactor)
- **P3 (existing v3 — só relocate):** screens/

### Padrão por componente (seguir PageHeader.jsx v3 como referência)

Cada `.jsx`:

1. **Comment header** (~3 linhas):
   - Propósito ("Stat tile — 28-px stat + label + trend")
   - When to use ("dashboard KPIs, top of page metrics")
   - When NOT to use ("evitar pra simples count display — use texto inline")

2. **Brand-agnostic absoluto:**
   - 0 HSL bakeado fora de tokens
   - 0 color hex hardcoded
   - 0 asset path brand-specific
   - 0 persona/email/company hardcoded
   - Tokens only: `hsl(var(--*))` ou `var(--*)` (escolher consistente — PageHeader v3 usa `var(--foreground)`, Sidebar refactored usa `hsl(var(--sidebar-background))`. Decidir e aplicar consistente em toda biblioteca)

3. **Props API minimal mas flexível:**
   - Variant (`size`, `intent`, `variant` quando aplica)
   - Required props óbvios
   - Optional props com defaults sensatos
   - Slots/children quando faz sentido

4. **Anti-pattern comments inline** quando relevante

5. **window.X = X** export pattern (consistente com Sidebar/LoginScreen/StatCard/PageHeader atuais)

### Showcase pages (`ui_kits/default/showcase/`)

```
ui_kits/default/showcase/
├── index.html             # Sidebar com links categorias + content area
└── pages/
    ├── base.html
    ├── surfaces.html
    ├── navigation.html
    ├── display.html
    ├── data.html
    ├── layout.html
    ├── dashboard.html
    ├── forms.html
    ├── auth.html
    └── screens.html       # showcase dos Screen-level templates
```

**Razão showcase navegável:** humano review + Claude que consome o repo via `cat showcase/pages/*.html` pega exemplos visuais + código padrão num só lugar. Skill `design-system-audit --bootstrap` lê pra scaffold.

**Cada page:**
- Section por componente: nome + propósito + exemplo renderizado + código source viewable
- Variants do componente lado a lado
- Anti-patterns quando aplicáveis
- Link "Source" → pasta do .jsx

**`showcase/index.html` requirements:**
- Sidebar (refactored com placeholder defaults) com links pra cada categoria
- Content area renderiza página da categoria
- Header "Anti-AI Design System — Component Library"
- Brand-agnostic

### Composition rules (`docs/10-component-composition.md`)

Documentar regras pra componentes NÃO cobertos. Ex:

- "Pra componente novo: começa de Card OU Surface, padding via tokens, density baseado em axis"
- "Pra variation visual de Button: variant prop em vez de Button2/ButtonAlt"
- "Pra componente compound: Accordion = AccordionRoot + AccordionItem + AccordionTrigger + AccordionContent (compound pattern shadcn)"
- "Pra apps multi-class: começa do default class via docs/09 axis values, override token diff via :root CSS vars"

~30-40 regras concisas. Cada: padrão + razão + 1 exemplo curto.

### Atualizar `docs/07-component-patterns.md`

1. Cada pattern existente: linha `**Varies by:** density, nav` no topo
2. Pra cada componente NOVO Wave 6.5: 1 parágrafo curto descrevendo padrão + axes que afetam + link pra showcase
3. Section nova "Component library overview" no topo: tabela `Componente | Categoria | Showcase | Source` linkando tudo

## Constraints

- **Tokens only.** Sem HSL bakeado, sem hex hardcoded fora tokens. `hsl(var(--*))` referenciando tokens em `presets/default/tokens.css` (v3). Se faltar token pra algo, sinalizar `// FIXME: precisa novo token --foo` em vez de inventar.

- **Brand-agnostic absoluto.** Sem nomes pessoa, sem emails, sem company-specific copy ("ChocoTracking", "Barry", "Gestão de Embarques" não aparecem). Defaults genéricos placeholder ("App", "Nome Sobrenome", "email@exemplo.com").

- **Class-aware mas não fork.** Componentes funcionam pra ops/fintech/editor/consumer/devtools/marketing via tokens override + axis values. Sem duplicar componente por classe.

- **Showcase pages standalone HTML.** Linkam `colors_and_type.css` + componentes via `<script>` tags. Sem build step. Patrick `open showcase/index.html` direto.

- **Reusar v3 existing.** Icon.jsx (~30 icons) reutiliza pra todos componentes que precisarem. PageHeader.jsx v3 já é brand-agnostic — relocate `layout/` sem mudança. DashboardScreen + RomaneiosScreen relocate `screens/`, mas StatusBadge inline em DashboardScreen extrai pra `display/StatusBadge.jsx`. RECENT_ROMANEIOS data inline manter como exemplo Choco-flavored (showcase de Screen real funcionando) OU substituir por placeholder generic — você decide qual fica melhor pro showcase.

- **Não inventar tokens novos.** Se preciso, sinaliza separadamente em "Notas pro applier".

- **Não inventar componentes.** Se algum dos ~33 não fizer sentido, sinaliza. Se faltar óbvio, propõe ajuste.

## Output esperado

### Bloco 1: Wave 6 MVP fechamento
- Sidebar.jsx, LoginScreen.jsx, StatCard.jsx refatorados (3 files completos)
- SKILL.md anti-ai-design-system reescrito como guidance
- Delete confirmation lovable-memory/design/tokens.md
- 2 SVGs (placeholder-logo + placeholder-mark)
- index.html harness trecho atualizado

### Bloco 2: Wave 6.5 Component Library — componentes
~30 .jsx files completos (que ainda não existem em v3), agrupados por categoria, cada um com path explícito no comment primeiro:

```jsx
// ui_kits/default/components/base/Button.jsx
// Button — primary/secondary/ghost/destructive variants...
```

Plus relocate notes pros 4 v3 existing (Sidebar/LoginScreen/StatCard/PageHeader/Icon — paths novos em subpastas), DashboardScreen/RomaneiosScreen relocate `screens/`, StatusBadge extract.

### Bloco 3: Wave 6.5 Component Library — showcase pages
- `showcase/index.html` completo
- 10 `showcase/pages/*.html` completos

### Bloco 4: Composition rules doc
- `docs/10-component-composition.md` completo

### Bloco 5: docs/07 update
- Trechos do `docs/07-component-patterns.md` que mudaram

### Bloco 6: Notas pro applier
- Tokens novos sinalizados (se houver)
- Asset paths a criar além dos 2 SVGs
- Migration concerns / order of operations / breaking changes
- Validation suggestions (`open showcase/index.html` + visual check Sidebar passa de borgonha legacy → teal atual)

## Files anexos (no consolidado `claude-design-files-wave6-mega.md`)

14 files concatenados:
- File 1: tokens.css v3 (com --accent-decorative + AA fixes)
- File 2: docs/03-token-system.md
- File 3: docs/07-component-patterns.md (atual, Wave 6.5 atualiza)
- File 4: docs/08-variation-axes.md (v3 full)
- File 5: docs/09-class-defaults.md (v3 full)
- File 6: skillforge-arsenal/skills/design-system-audit/SKILL.md (consumer)
- File 7: anti-ai-design-system/SKILL.md v3 (precisa virar guidance)
- Files 8-10: Sidebar/LoginScreen/StatCard atuais (refactor pendente Wave 6)
- Files 11-13: PageHeader/DashboardScreen/RomaneiosScreen v3 (referência brand-agnostic + composition pattern)
- File 14: Icon.jsx v3 (registry reutilizar)

## Estimativa esforço

- Wave 6 MVP fechamento: ~1.5h
- Wave 6.5 Component Library: ~15-25h Claude Design tempo
- Total round: ~16-26h tempo Claude Design
- Aplicação Patrick (Claude que aplica): ~2-3h batch apply

## Boundary final

NÃO fazer:
- Storybook setup
- package.json / npm publish
- CI scripts
- _template/ folder separado
- Refazer paleta cream/teal/terracotta (manter intacta)
- Mexer em files fora dos enumerados (presets/, ui_kits/, docs/, assets/)

Patrick excluiu explicitamente esses items. Reconfirma se mudou opinião pós Wave 6.5 (provavelmente não muda).

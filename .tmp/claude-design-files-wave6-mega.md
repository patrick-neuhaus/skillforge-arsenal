# Files anexos — Wave 6 MVP final + Wave 6.5 Component Library

> Baseline = Vitor v3 (Waves 1-5 done + 5 componentes novos: PageHeader, DashboardScreen, RomaneiosScreen, Icon, app.jsx).
>
> Pendências Wave 6 MVP (NÃO entregues em v3): 3 .jsx refactor (Sidebar/LoginScreen/StatCard ainda hardcoded) + SKILL.md → guidance (`user-invocable: false` + rename) + delete lovable-memory + 2 placeholder SVGs + index.html harness pra props brand/user.
>
> 12 files anexos:
> - File 1: tokens.css v3 (com --accent-decorative + AA fixes)
> - File 2: docs/03-token-system.md
> - File 3: docs/07-component-patterns.md (atual, Wave 6.5 deve atualizar)
> - File 4: docs/08-variation-axes.md (v3 — full content)
> - File 5: docs/09-class-defaults.md (v3 — full content)
> - File 6: skillforge-arsenal/skills/design-system-audit/SKILL.md (consumer)
> - File 7: anti-ai-design-system/SKILL.md v3 (precisa virar guidance)
> - Files 8-10: Sidebar/LoginScreen/StatCard ATUAIS (ainda hardcoded — referência do que refactor)
> - Files 11-13: PageHeader/DashboardScreen/RomaneiosScreen v3 (referência brand-agnostic + composition pattern)
> - File 14: Icon.jsx v3 (lucide-style registry, REUTILIZAR Wave 6.5)

---

# === FILE 1/14: presets/default/tokens.css (v3) ===

Path: `Documents/Github/anti-ai-design-system/presets/default/tokens.css`

**ESTADO v3:** AA fixes aplicados (--accent darkened, --accent-decorative added, --destructive/--success/--info AA-tuned, status pills foreground darkened).

```css
/* anti-ai-design-system / preset: default (warm-editorial flavor) */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Lora:wght@500;600;700&display=swap');

@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 30 33% 96%;
    --foreground: 16 38% 12%;

    --card: 0 0% 100%;
    --card-foreground: 16 38% 12%;

    --popover: 0 0% 100%;
    --popover-foreground: 16 38% 12%;

    --primary: 184 100% 18%;
    --primary-foreground: 0 0% 100%;

    --secondary: 30 33% 93%;
    --secondary-foreground: 16 38% 12%;

    --muted: 30 20% 90%;
    --muted-foreground: 20 29% 33%;

    /* Accent terracotta — solid bg AA-fixed (was 12 65% 55% = 3.74:1, now 4.7:1) */
    --accent: 12 70% 42%;              /* AA: 4.7:1 on white */
    --accent-foreground: 0 0% 100%;
    --accent-decorative: 12 65% 55%;   /* original lighter — strips/dots only */

    --destructive: 0 72% 42%;          /* AA: 5.9:1 on white */
    --destructive-foreground: 0 0% 100%;

    --border: 30 20% 87%;
    --input: 30 33% 96%;
    --ring: 184 100% 18%;

    --radius: 0.5rem;

    /* Sidebar — primary teal como surface */
    --sidebar-background: 184 100% 18%;
    --sidebar-foreground: 0 0% 100%;
    --sidebar-primary: 184 80% 25%;
    --sidebar-primary-foreground: 0 0% 100%;
    --sidebar-accent: 184 80% 25%;
    --sidebar-accent-foreground: 0 0% 100%;
    --sidebar-border: 184 80% 22%;
    --sidebar-ring: 12 65% 55%;
    --sidebar-indicator: 12 65% 55%;

    /* Status — AA-tuned */
    --success: 152 70% 24%;
    --success-foreground: 0 0% 100%;
    --warning: 38 92% 50%;
    --warning-foreground: 16 38% 12%;
    --info: 217 91% 38%;
    --info-foreground: 0 0% 100%;

    /* Status pill tokens — fg passes AA vs --background */
    --status-pending-bg: 30 20% 87%;
    --status-pending-fg: 16 38% 20%;
    --status-success-bg: 152 70% 24% / 0.12;
    --status-success-fg: 152 70% 24%;
    --status-warning-bg: 38 92% 35% / 0.16;
    --status-warning-fg: 38 92% 28%;
    --status-error-bg: 0 72% 42% / 0.10;
    --status-error-fg: 0 72% 42%;
    --status-info-bg: 217 91% 38% / 0.10;
    --status-info-fg: 217 91% 38%;
  }
}

@layer base {
  * { @apply border-border; }
  body { @apply bg-background text-foreground antialiased; font-family: 'Poppins', sans-serif; }
  .font-display { font-family: 'Lora', serif; }
}
```

---

# === FILE 2/14: docs/03-token-system.md ===

Path: `Documents/Github/anti-ai-design-system/docs/03-token-system.md`

**Resumo:** typography (--font-display/body/mono, escala xs→3xl, weights 400/500/600 NÃO 700, leading tight/normal/relaxed, tracking normal NÃO wide), spacing (4px base, escala curta 1/1.5/2/4/5/6/8 — NÃO 3/7/9), radius (escala A 6/8/12/16/20px OU zero — não único 8px), shadows (sm/md/lg — NÃO xl/2xl/default), breakpoints (sm 640 / md 768 / lg 1024 / xl 1280 / 2xl 1400, container max-w-7xl/3xl/xl/5xl), animations (150/200/300ms — NÃO 500+, NÃO bounce/spring), tokens semânticos obrigatórios (--background/foreground/card/popover/muted/border/input/ring/primary/secondary/accent/destructive/success/warning/info/sidebar-*/radius-sm/md/lg/xl/2xl), WCAG AA regra dura (4.5:1 small / 3:1 large pra texto, ícone-info, border-funcional. Decorative-only: --accent/--sidebar-indicator/--signal podem falhar AA SE só faixa indicadora 1-2px / dot ≤8×8 / bg pill com texto escuro contrastante).

---

# === FILE 3/14: docs/07-component-patterns.md (atual — Wave 6.5 deve atualizar) ===

Path: `Documents/Github/anti-ai-design-system/docs/07-component-patterns.md`

**Resumo:** Action Column (geometria w-N + flex gap-1 sem justify-*), NavLink (não wrapper, usar react-router direto), Page Header (h2 + subtitle + actions top-right, sem ícone inline, font-display opcional), shared component vs inline (regra 2+ pages), AppTable usage (rows DIRETO como children, NÃO em <TableBody>), Login layout split 50/50 (esquerda brand+contexto, direita form, mobile stack), Configurações = user panel button (quando há admin section).

**Pra Wave 6.5 atualizar:**
- Linha "Varies by:" no topo de cada pattern (ex: "PageHeader Varies by: density, nav")
- Section "Component library overview" no topo: tabela componente | categoria | showcase | source

---

# === FILE 4/14: docs/08-variation-axes.md (v3 FULL) ===

Path: `Documents/Github/anti-ai-design-system/docs/08-variation-axes.md`

```markdown
# Variation Axes

8 canonical axes. `default` preset é uma config válida. Vary by axis; do not fork.

| Axis | Values |
|---|---|
| density | compact, comfortable, spacious |
| surface | flat, subtle, moderate, strong |
| nav | top-only, rail, sidebar, dual-panel, none |
| typeContrast | sans-only, sans+mono, serif+sans, serif+sans+mono |
| iconDensity | none, sparse, mixed, dense |
| statusEmphasis | neutral, subtle, strong |
| motion | none, subtle, medium |
| hueFamily | warm, cool, neutral, brand-led |

## 1. density
Controls: row height, vertical padding, gap fields, base font-size dense surfaces.
- compact (32-40px row, base 13-14px) — ops, devtools, editors
- comfortable (44-48px row, base 14-15px) — fintech, consumer
- spacious (56px+, base 15-16px) — marketing only
Skill adapts: --row-h, --field-gap-y, --container-py, body font-size root.
Default preset: compact (ops dashboard).

## 2. surface
Controls: separation cards/panels do background.
- flat — no border/shadow, separar por tint/whitespace. Editors/canvas.
- subtle — hairline border 1px hsl(var(--border)), no shadow. Ops/devtools.
- moderate — visible border + shadow-sm, hover shadow-md. Fintech, consumer.
- strong — pronounced border + shadow-md static, branded tint. Marketing only.
Skill adapts: --border-weight, --shadow-card, --shadow-card-hover.
Default: subtle.

## 3. nav
Controls: shape do app shell.
- top-only — no sidebar, top bar carries brand+nav+CTA. Marketing, light consumer, docs.
- rail — narrow icon-only ~64-72px. Editors (canvas dominates).
- sidebar — full ~240-280px expanded, collapsible icon. Ops, fintech, devtools, most consumer. Default app shape.
- dual-panel — left tree + right inspector flanking center canvas. Editors (Figma/Notion).
- none — no persistent nav. Single-purpose tools, modals as apps, focused readers.
Skill adapts: layout primitive (grid-template-columns).
Default: sidebar.

## 4. typeContrast
Controls: families type em jogo + hierarquia.
- sans-only — 1 sans family body+display+UI. Fintech, devtools, consumer.
- sans+mono — sans prose + mono IDs/numbers/code. Ops, devtools.
- serif+sans — serif display + sans body. Marketing, editorial-flavored consumer.
- serif+sans+mono — full editorial stack. Warm-editorial. Default preset.
Skill adapts: swap --font-display/body/mono. Type-scale unchanged.
Default: serif+sans+mono (Lora + Poppins + Geist Mono).

## 5. iconDensity
Controls: how often iconography aparece.
- none — text-only UI. Brutalist/typography brands.
- sparse — icons only primary actions, status, file-type. Conservative. Fintech, consumer.
- mixed — nav items, primary actions, status, table action cells. Default preset. Ops, devtools, editors.
- dense — most affordances incl secondary buttons, labels. Tool-heavy editors (Figma toolbar).
Skill adapts: per-component decisão render icon. Lucide subset stays.
Default: mixed.

## 6. statusEmphasis
Controls: how loud status badges/pills.
- neutral — status by position/label only. Consumer/editor (status inferido contexto).
- subtle — pill bg 8-12% alpha + dot. AA-tuned text. Default preset. Ops, fintech.
- strong — solid bg + glyph icon + uppercase label. Devtools (alerts severity).
Skill adapts: --status-*-bg opacity, StatusBadge variant.
Default: subtle.

## 7. motion
Controls: transition duration, easing, layout animation.
- none — instant state changes. Accessibility-first/extreme-density tools.
- subtle — 150-300ms, color/opacity, no layout. Default app shells.
- medium — 200-500ms, layout transitions allowed (drawer, modal, page-enter). Marketing, consumer com personalidade.
Skill adapts: --motion-duration-* tokens, gates layout-animation rules.
Default: subtle.

## 8. hueFamily
Controls: palette temperature.
- warm — cream/cocoa/terracotta. Editorial, food, hospitality.
- cool — blue/teal/slate. Fintech, devtools.
- neutral — gray-on-gray + single accent. Editors, brutalist tools.
- brand-led — specific brand color drives palette regardless temperature. Default preset (teal 184 100% 18% from Barry).
Skill adapts: rewrites HSL --background/foreground/primary/accent/sidebar-background. Token structure unchanged.
Default: brand-led (warm-leaning).

## How to vary without forking

no_fork_rule (SKILL.md) enforced aqui.

1. Read briefing → identify class of app
2. Look up axis values em docs/09
3. Override only tokens implied by axes que diferem from default. Keep file structure, component recipes, naming.
4. Reuse presets/_shared/AppTable.tsx + StatusBadge.tsx as-is — token-driven.
5. NÃO criar presets/<other>/ ou ui_kits/<other>/ unless user has specific brand to ship; even then skill writes new token values, not new components.

Correct adaptation = token diff, NÃO parallel folder.
```

---

# === FILE 5/14: docs/09-class-defaults.md (v3 FULL) ===

Path: `Documents/Github/anti-ai-design-system/docs/09-class-defaults.md`

```markdown
# Class-of-App Defaults

Skill reads briefing, identifies class, applies axis values abaixo. `default` preset = Ops dashboard row.

| Class | density | surface | nav | typeContrast | iconDensity | statusEmphasis | motion | hueFamily |
|---|---|---|---|---|---|---|---|---|
| Ops dashboard | compact | subtle | sidebar | sans+mono | mixed | subtle | subtle | brand-led |
| Fintech | comfortable | moderate | sidebar | sans-only | sparse | subtle | subtle | cool |
| Editor / canvas | compact | flat | dual-panel | sans+mono | mixed | neutral | subtle | neutral |
| Consumer | comfortable | moderate | sidebar | sans-only | sparse | neutral | subtle | warm |
| Devtools | compact | subtle | sidebar | sans+mono | mixed | strong | subtle | cool |
| Marketing | spacious | strong | top-only | serif+sans | sparse | neutral | medium | brand-led |

`default` preset = Ops dashboard com hueFamily=brand-led (teal-warm leaning) + typeContrast=serif+sans+mono (Lora+Poppins+Geist Mono — 1 step richer than Ops baseline). Strong valid example, NOT universal output.

## Como usar

1. Identify class. Spans 2 (e.g., "fintech with editor pieces") → pick dominant surface user lives in (sidebar+table = Ops/Fintech; canvas = Editor).
2. Apply axis values for row.
3. Override per axis only when briefing forces. Consumer com hero-driven home não vira Marketing — fica Consumer com marketing landing on top.
4. Defer docs/08 pra what each value means.

## Class definitions

### Ops dashboard
Operations tooling. Listings, tables, filters, status pipelines, audit trails. User vive em lists+rows. Density wins, brand on sidebar não cards.
Examples: Linear, Attio, Retool, default preset (chocotracking).

### Fintech
Money, accounts, periods, transactions. Numbers legíveis at glance. Mais breathing room que ops, mais semantic weight em status (pending/approved/failed). Cool palette convencional não obrigatório.
Examples: Mercury, Stripe Dashboard, Ramp.

### Editor / canvas
Central canvas dominates viewport, UI chrome shrinks. Dual-panel (left tree + right inspector) canonical. Surfaces flat (não competir com content).
Examples: Figma, Notion, Linear (canvas/board view).

### Consumer
Daily-driver apps amplo audience. Familiar shell, generous tap targets, warm hue typical. Status implícito (where item lives = state).
Examples: Gmail, Calendar, Things, B2C product apps.

### Devtools
Logs, traces, deployments, alerts, telemetry. Compact info-dense igual Ops, mas status carries severity weight (statusEmphasis=strong).
Examples: Vercel Dashboard, GitHub, Sentry.

### Marketing
Public-facing acquisition surfaces. Shell vanishes, narrative+CTA take over. Spacious density, strong surfaces, generous motion. Only class onde serif+sans é default.
Examples: Vercel.com, Linear.app, Stripe.com (marketing site).

## Quando briefing crosses classes

Resolution rule:
1. Shell follows dominant surface (Ops sidebar+table)
2. Type/density may shift one notch towards secondary class (comfortable em vez de compact)
3. hueFamily follows brand if any; otherwise secondary class

NÃO inventar nova classe. Matrix = compress decision space, não enumerate every product.
```

---

# === FILE 6/14: skillforge-arsenal/skills/design-system-audit/SKILL.md ===

Path: `Documents/Github/skillforge-arsenal/skills/design-system-audit/SKILL.md`

**STATUS:** Skill produção skillforge, em uso desde 2026-04-29. Lock-in candidate Wave 7.5.

**Frontmatter description:** "Audita app contra design system EXTERNO existente com fase de coerência. Default DS: anti-ai-design-system (Patrick canonical). Use quando: 'tira a cara de IA do app', 'deixa o app mais bonito', 'aplica design system'..."

**Workflow:** Phase 1 Context Collection (5 perguntas) → Phase 2 Inventory (cat docs/03/07/08/09 + tokens.css + ls _shared/) → Phase 3 Spec Diff → Phase 4 Coherence Check ⛔ BLOCKING + Contrast Audit WCAG AA → Phase 5 Delta Report (What/Why HERE/Adaptation/Severity/Action) → Phase 6 GATE per-delta.

**Default DS Reference (Wave 7):** path `~/Documents/Github/anti-ai-design-system`. Phase 2 auto-loads docs/03/07 + presets/default/tokens.css + ls _shared/.

**Options:** `--audit` (default), `--apply` (gate per-delta), `--bootstrap` (scaffold from scratch usando biblioteca Wave 6.5), `--ds-path <path>` (override).

**Phase 6 `--bootstrap` mode é onde Wave 6.5 component library brilha** — skill scaffolda app from scratch usando biblioteca canônica em vez de inventar shadcn variations.

---

# === FILE 7/14: anti-ai-design-system/SKILL.md (v3) ===

Path: `Documents/Github/anti-ai-design-system/SKILL.md`

**ATENÇÃO:** v3 ainda tem `user-invocable: true` + nome `anti-ai-design`. **Wave 6 fix: virar `user-invocable: false` + rename `anti-ai-design-system-spec` + description perspectiva file consumido + section "How this file is consumed".**

```markdown
---
name: anti-ai-design
description: Use this skill to generate well-branded interfaces and assets for the Anti-AI Design System, either for production or throwaway prototypes/mocks/etc. The system removes the "cara de IA" smell common to AI-generated web apps. It ships ONE concrete preset (default — warm-editorial / chocotracking flavor, ops dashboard) plus 8 canonical variation axes that adapt the same normative rules to other classes of app (fintech, editor, consumer, devtools, marketing).
user-invocable: true
---

Read the README.md file first, then explore the other available files.

## Decision tree (always run before generating)

1. Read briefing. What user is building (form, dashboard, marketing, editor, devtools, fintech)?
2. Identify dominant class (ops dashboard, fintech, editor/canvas, consumer, devtools, marketing). Spans 2 → pick surface user lives in.
3. Look up axis defaults em docs/09 — 8 values.
4. Read what axis controls em docs/08.
5. Use presets/default/ + ui_kits/default/ as concrete examples. NÃO copy brand (chocotracking, terracotta, Lora, Barry).
6. Vary by axis, NÃO by fork.

## no_fork_rule

NÃO criar new design system, preset, kit, ou component variant quando variation pode ser:
- token override (CSS vars em :root)
- class swap (density-compact → density-comfortable)
- prop em existing component (<StatusBadge variant="strong" />)
- doc-level axis annotation (docs/08)

Correct adaptation = token diff + axis annotation, NÃO new folder under presets/ ou ui_kits/.

## Normative vs. illustrative vs. legacy

- Normative: docs/, CONTENT/VISUAL/ICONOGRAPHY sections README, SKILL.md
- Illustrative: presets/default/, ui_kits/default/, preview/, colors_and_type.css, assets/icons/
- Legacy: presets/default/lovable-memory/, PLAN.md, older audits/, hardcoded brand strings em ui_kits/default/components/*

## Key files

README.md, docs/01 (anti-patterns), docs/08 (axes), docs/09 (class defaults), colors_and_type.css, preview/, ui_kits/default/.

## When invoked without context

Pergunta:
1. Prototyping one-off OU contributing production codebase?
2. Surface (marketing, dashboard, settings, onboarding, editor)?
3. Class (ops, fintech, editor, consumer, devtools, marketing)?

Then apply class defaults, output HTML artifacts (link colors_and_type.css) ou production code.
```

---

# === FILE 8/14: ui_kits/default/components/Sidebar.jsx (atual — REFACTOR PENDENTE) ===

Path: `Documents/Github/anti-ai-design-system/ui_kits/default/components/Sidebar.jsx`

**ESTADO v3:** AINDA HARDCODED. Wave 6 deve refactor.

Hardcoding presente:
- `hsl(338 55% 23%)` borgonha (legacy! atual é teal `184 100% 18%`)
- `hsl(338 50% 30%)` borgonha hover
- `hsl(338 50% 27%)` border
- `hsl(33 47% 53%)` dourado decorativo + avatar
- `barry-callebaut-logo.svg` + `bc-icon.jpg` paths
- "JP" + "João Pereira" + "joao@barry-callebaut.com" persona

**Refactor target (Wave 6 fix):**
- HSL → tokens: `hsl(var(--sidebar-background))`, `hsl(var(--sidebar-accent))`, `hsl(var(--sidebar-border))`, `hsl(var(--accent-decorative))` (indicator 3px), `hsl(var(--accent))` (avatar bg c/ texto AA)
- Asset paths → props brand={ logo, mark, name }
- Persona → props user={ name, email }, derivar iniciais helper

(File completo com hardcoding em ~150 linhas. Ver Vitor v3 ZIP `Sidebar.jsx`.)

---

# === FILE 9/14: ui_kits/default/components/LoginScreen.jsx (atual — REFACTOR PENDENTE) ===

Path: `Documents/Github/anti-ai-design-system/ui_kits/default/components/LoginScreen.jsx`

**ESTADO v3:** AINDA HARDCODED.

Hardcoding presente:
- HSL `hsl(338 55% 23%)` (legacy borgonha) — primary panel
- "ChocoTracking" + "Gestão de Embarques" copy
- "joao@barry-callebaut.com" pre-fill state
- `barry-callebaut-logo.svg` asset path

**Refactor target:**
- HSL → `hsl(var(--primary))` + `hsl(var(--primary-foreground))`
- Copy → props appName/tagline com defaults genéricos
- Email pre-fill → state vazio
- Asset → prop brand.logo

Estrutura split 50/50 já correta (`flex: 1` ambos lados — manter).

---

# === FILE 10/14: ui_kits/default/components/StatCard.jsx (atual — REFACTOR PENDENTE) ===

Path: `Documents/Github/anti-ai-design-system/ui_kits/default/components/StatCard.jsx`

**ESTADO v3:** AINDA HARDCODED.

Hardcoding:
- `hsla(33 47% 53% / .1)` chip bg
- `hsl(33 47% 53%)` icon stroke
- `hsl(152 85% 30%)` success trend (NÃO usa tokens AA-tuned do v3)

**Refactor target:**
- chip bg → `hsl(var(--accent-decorative) / .1)` (decorative — alpha desatura)
- icon stroke → `hsl(var(--accent))` (functional, AA contra --card)
- success trend → `hsl(var(--success))`
- destructive trend → `hsl(var(--destructive))`

---

# === FILE 11/14: ui_kits/default/components/PageHeader.jsx (v3 NOVO — REFERÊNCIA OK) ===

Path: `Documents/Github/anti-ai-design-system/ui_kits/default/components/PageHeader.jsx`

**ESTADO v3:** brand-agnostic, tokens corretos. **USE como referência padrão pra Wave 6.5 components.**

```jsx
// Page-level chrome: title, subtitle, optional action slot.
const PageHeader = ({ title, subtitle, actions }) => (
  <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between", gap: 16, marginBottom: 4 }}>
    <div>
      <h2 style={{ fontSize: 20, fontWeight: 600, color: "var(--foreground)", letterSpacing: "-.005em" }}>{title}</h2>
      {subtitle && <p style={{ fontSize: 14, color: "var(--muted-foreground)", marginTop: 2 }}>{subtitle}</p>}
    </div>
    {actions && <div style={{ display: "flex", gap: 8, flexShrink: 0 }}>{actions}</div>}
  </div>
);

window.PageHeader = PageHeader;
```

**Padrão exemplar:** props clean (title/subtitle/actions), tokens `var(--foreground)` + `var(--muted-foreground)`, sem hardcode, sem icon inline (per docs/07 pattern). Wave 6.5 components devem seguir esse padrão.

**Nota Wave 6.5:** usar este `var(--*)` direto OU normalizar pra `hsl(var(--*))` consistente com Sidebar refactored? Decidir e aplicar consistente.

---

# === FILE 12/14: ui_kits/default/components/DashboardScreen.jsx (v3 NOVO — REFERÊNCIA COMPOSITION) ===

Path: `Documents/Github/anti-ai-design-system/ui_kits/default/components/DashboardScreen.jsx`

**ESTADO v3:** brand-agnostic estrutura MAS data inline (RECENT_ROMANEIOS) é Choco-flavored. Útil como REFERÊNCIA composition pattern Screen-level.

```jsx
// DashboardScreen — 4 stat cards + recent table.
const DashboardScreen = ({ onOpenRomaneios }) => (
  <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
    <PageHeader title="Dashboard" subtitle="Visão geral da expedição logística" />

    <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 16 }}>
      <StatCard icon={Icon.Package} value="1.247" label="Total Deliveries" trend="+12%" />
      <StatCard icon={Icon.FileText} value="183" label="Romaneios" trend="+5%" />
      <StatCard icon={Icon.ScanBarcode} value="42" label="Em Conferência" />
      <StatCard icon={Icon.ClipboardCheck} value="29" label="Carregamentos" trend="+18%" />
    </div>

    <div className="card">
      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", padding: "16px 20px" }}>
        <div>
          <h3>Romaneios recentes</h3>
          <p>Últimos romaneios gerados</p>
        </div>
        <button className="btn btn-outline btn-sm" onClick={onOpenRomaneios}>Ver todos</button>
      </div>
      <table className="tbl">
        <thead><tr>...</tr></thead>
        <tbody>{RECENT_ROMANEIOS.map(...)}</tbody>
      </table>
    </div>
  </div>
);

const StatusBadge = ({ value }) => { /* mapping value → cls/label */ };
```

**Padrão composition exemplar:** Screen = `<flex column gap 20>` + `<PageHeader>` + grid stat cards + card com table + StatusBadge inline.

**Wave 6.5:** Screen-level patterns vão pra subpasta `screens/` ou `templates/`. StatusBadge inline aqui deve virar component standalone em `display/StatusBadge.jsx`.

---

# === FILE 13/14: ui_kits/default/components/RomaneiosScreen.jsx (v3 NOVO — REFERÊNCIA) ===

Path: `Documents/Github/anti-ai-design-system/ui_kits/default/components/RomaneiosScreen.jsx`

**ESTADO v3:** brand-agnostic estrutura, data Choco-flavored.

```jsx
const RomaneiosScreen = ({ onConfer }) => (
  <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
    <PageHeader
      title="Romaneios"
      subtitle="Romaneios gerados nas últimas 72 horas"
      actions={<>
        <button className="btn btn-outline btn-sm"><Icon.Calendar size={14} /> 26/04 – 28/04</button>
        <button className="btn btn-primary"><Icon.Plus size={14} /> Novo romaneio</button>
      </>}
    />
    <div className="card" style={{ padding: 0 }}>
      <table className="tbl">...</table>
    </div>
  </div>
);
```

**Padrão exemplar:** PageHeader com `actions` slot (button outline + primary), card padding:0 wrapping table fullwidth.

---

# === FILE 14/14: ui_kits/default/components/Icon.jsx (v3 NOVO — REUTILIZAR) ===

Path: `Documents/Github/anti-ai-design-system/ui_kits/default/components/Icon.jsx`

**ESTADO v3:** lucide-style inline SVGs, ~30 icons, 2px stroke, currentColor. **REUTILIZAR Wave 6.5** (não duplicar registry).

```jsx
const _i = (paths, opts = {}) => ({ size = 18, color = "currentColor", strokeWidth = 2, ...rest } = {}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none"
       stroke={color} strokeWidth={strokeWidth} strokeLinecap="round" strokeLinejoin="round" {...rest}>
    {paths}
  </svg>
);

const Icon = {
  LayoutDashboard: _i(<>...</>),
  Package: _i(<>...</>),
  FileText: _i(<>...</>),
  ScanBarcode: _i(<>...</>),
  ClipboardCheck: _i(<>...</>),
  Upload: _i(<>...</>),
  Truck: _i(<>...</>),
  Route: _i(<>...</>),
  Box: _i(<>...</>),
  Users: _i(<>...</>),
  Settings: _i(<>...</>),
  LogOut: _i(<>...</>),
  LogIn: _i(<>...</>),
  ChevronLeft: _i(<>...</>),
  ChevronRight: _i(<>...</>),
  Search: _i(<>...</>),
  SlidersHorizontal: _i(<>...</>),
  Calendar: _i(<>...</>),
  Plus: _i(<>...</>),
  CheckCircle: _i(<>...</>),
  XCircle: _i(<>...</>),
  AlertCircle: _i(<>...</>),
  AlertTriangle: _i(<>...</>),
  Pencil: _i(<>...</>),
  Trash2: _i(<>...</>),
  MoreHorizontal: _i(<>...</>),
  ArrowUpDown: _i(<>...</>),
  Settings2: _i(<>...</>),
  Menu: _i(<>...</>),
  // etc — ~30 icons total
};

window.Icon = Icon;
```

**Wave 6.5:** este registry deve crescer com icons que componentes novos precisarem (Switch on/off, Radio dot, Checkbox check, Tabs caret, Pagination first/last/prev/next, Avatar fallback, etc). Manter padrão `_i(paths, opts)` + currentColor + 2px stroke.

---

## Fim files anexos

Próximos passos pra você (Claude Design):

1. **Wave 6 MVP final** (~30min): 2 SVGs + harness index.html update pra Sidebar/LoginScreen receberem props brand/user/appName
2. **Wave 6 fixes pendentes** (~1h): refactor Sidebar.jsx + LoginScreen.jsx + StatCard.jsx pra tokens (HSL → hsl(var(--*))) + remover persona hardcoded; SKILL.md → guidance (user-invocable: false + rename); delete lovable-memory tokens.md
3. **Wave 6.5 Component Library** (~15-25h): ~30 componentes brand-agnostic seguindo padrão PageHeader.jsx + 9 showcase pages categorizadas + composition rules + docs/07 update

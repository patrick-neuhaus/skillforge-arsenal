# Files anexos pra avaliação Wave 5 anti-ai-design-system

> 6 files concatenados pra Claude Design avaliar:
> - 3 .jsx (auditoria hardcoding ui_kits — pergunta #1)
> - 1 tokens.md (lovable-memory legacy — pergunta #2)
> - 2 SKILL.md (boundary 1 skill vs 2 — pergunta #3)

---

# === FILE 1/6: ui_kits/default/components/Sidebar.jsx ===

Path: `Documents/Github/anti-ai-design-system/ui_kits/default/components/Sidebar.jsx`

```jsx
// Sidebar — primary fill, accent left bar on active, eyebrow group labels.
// Recreates chocotracking/src/components/layout/AppSidebar.tsx visually.

const SidebarItem = ({ icon: I, label, active, onClick, collapsed }) => (
  <button
    onClick={onClick}
    style={{
      position: "relative",
      display: "flex",
      gap: collapsed ? 0 : 12,
      alignItems: "center",
      justifyContent: collapsed ? "center" : "flex-start",
      padding: collapsed ? "10px 0" : "8px 12px",
      borderRadius: 12,
      background: active ? "hsl(338 50% 30%)" : "transparent",
      color: active ? "#fff" : "rgba(255,255,255,.7)",
      fontSize: 14,
      fontWeight: 500,
      border: 0,
      width: "100%",
      textAlign: "left",
      transition: "background-color .15s, color .15s",
    }}
    onMouseEnter={(e) => { if (!active) { e.currentTarget.style.background = "hsl(338 50% 30% / .5)"; e.currentTarget.style.color = "#fff"; }}}
    onMouseLeave={(e) => { if (!active) { e.currentTarget.style.background = "transparent"; e.currentTarget.style.color = "rgba(255,255,255,.7)"; }}}
  >
    {active && (
      <span style={{
        position: "absolute", left: 0, top: "50%", transform: "translateY(-50%)",
        width: 3, height: 20, background: "hsl(33 47% 53%)", borderRadius: "0 4px 4px 0",
      }}/>
    )}
    <I size={18} />
    {!collapsed && <span style={{ overflow: "hidden", whiteSpace: "nowrap", textOverflow: "ellipsis" }}>{label}</span>}
  </button>
);

const SidebarGroup = ({ label, children, collapsed }) => (
  <div style={{ display: "flex", flexDirection: "column", gap: 2, marginTop: 14 }}>
    {!collapsed && (
      <div style={{
        padding: "0 12px 6px",
        fontSize: 10, fontWeight: 600, letterSpacing: ".08em",
        textTransform: "uppercase", color: "rgba(255,255,255,.4)",
      }}>{label}</div>
    )}
    {children}
  </div>
);

const NAV = {
  operacao: [
    { key: "dashboard", icon: Icon.LayoutDashboard, label: "Dashboard" },
    { key: "deliveries", icon: Icon.Package, label: "Deliveries" },
    { key: "romaneios", icon: Icon.FileText, label: "Romaneios" },
    { key: "conferencia", icon: Icon.ScanBarcode, label: "Conferência" },
    { key: "carregamento", icon: Icon.ClipboardCheck, label: "Carregamento" },
    { key: "import", icon: Icon.Upload, label: "Importação" },
  ],
  cadastros: [
    { key: "transportadoras", icon: Icon.Truck, label: "Transportadoras" },
    { key: "rotas", icon: Icon.Route, label: "Rotas" },
    { key: "skus", icon: Icon.Box, label: "SKUs" },
  ],
  admin: [
    { key: "usuarios", icon: Icon.Users, label: "Usuários" },
    { key: "motivos", icon: Icon.AlertCircle, label: "Motivos" },
    { key: "config", icon: Icon.Settings, label: "Config. Sistema" },
  ],
};

const Sidebar = ({ active, onNavigate, collapsed, onToggleCollapse, onLogout }) => {
  const width = collapsed ? 72 : 272;
  return (
    <aside style={{
      width, flexShrink: 0,
      background: "hsl(338 55% 23%)",
      color: "#fff",
      height: "100vh",
      position: "sticky", top: 0,
      padding: "14px 12px",
      display: "flex", flexDirection: "column",
      borderRight: "1px solid hsl(338 50% 27%)",
      transition: "width .25s ease-in-out",
    }}>
      {/* Logo / collapse */}
      <div style={{ position: "relative", padding: "8px 4px", height: 44, display: "flex", alignItems: "center", justifyContent: collapsed ? "center" : "flex-start" }}>
        {collapsed ? (
          <div style={{ width: 40, height: 40, borderRadius: 10, background: "#fff", display: "flex", alignItems: "center", justifyContent: "center", overflow: "hidden" }}>
            <img src="../../assets/bc-icon.jpg" alt="BC" style={{ width: 32, height: 32, objectFit: "contain" }} />
          </div>
        ) : (
          <img src="../../assets/barry-callebaut-logo.svg" alt="Default app" style={{ height: 28 }} />
        )}
        <button
          onClick={onToggleCollapse}
          aria-label="Toggle sidebar"
          style={{
            position: "absolute", right: -16, top: "50%", transform: "translateY(-50%)",
            width: 24, height: 24, borderRadius: "50%",
            background: "#fff", color: "hsl(338 55% 23%)",
            border: "1px solid hsl(30 20% 87%)",
            display: "flex", alignItems: "center", justifyContent: "center",
            boxShadow: "0 1px 2px 0 rgb(0 0 0 / .05)",
          }}
        >
          {collapsed ? <Icon.ChevronRight size={14} /> : <Icon.ChevronLeft size={14} />}
        </button>
      </div>

      <nav style={{ flex: 1, overflowY: "auto", marginTop: 4 }}>
        <SidebarGroup label="Operação" collapsed={collapsed}>
          {NAV.operacao.map((it) => (
            <SidebarItem key={it.key} icon={it.icon} label={it.label} collapsed={collapsed}
              active={active === it.key} onClick={() => onNavigate(it.key)} />
          ))}
        </SidebarGroup>
        <SidebarGroup label="Cadastros" collapsed={collapsed}>
          {NAV.cadastros.map((it) => (
            <SidebarItem key={it.key} icon={it.icon} label={it.label} collapsed={collapsed}
              active={active === it.key} onClick={() => onNavigate(it.key)} />
          ))}
        </SidebarGroup>
        <SidebarGroup label="Administração" collapsed={collapsed}>
          {NAV.admin.map((it) => (
            <SidebarItem key={it.key} icon={it.icon} label={it.label} collapsed={collapsed}
              active={active === it.key} onClick={() => onNavigate(it.key)} />
          ))}
        </SidebarGroup>
      </nav>

      {/* Footer: user + logout */}
      <div style={{ borderTop: "1px solid hsl(338 50% 27%)", paddingTop: 10, marginTop: 10 }}>
        {!collapsed && (
          <div style={{ display: "flex", alignItems: "center", gap: 10, padding: "0 8px 8px" }}>
            <div style={{ width: 32, height: 32, borderRadius: "50%", background: "hsl(33 47% 53%)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 12, fontWeight: 600, color: "#fff" }}>JP</div>
            <div style={{ minWidth: 0, lineHeight: 1.2 }}>
              <div style={{ fontSize: 13, fontWeight: 500, whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" }}>João Pereira</div>
              <div style={{ fontSize: 11, color: "rgba(255,255,255,.6)", whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" }}>joao@barry-callebaut.com</div>
            </div>
          </div>
        )}
        <SidebarItem icon={Icon.LogOut} label="Sair" collapsed={collapsed} onClick={onLogout} />
      </div>
    </aside>
  );
};

window.Sidebar = Sidebar;
```

---

# === FILE 2/6: ui_kits/default/components/LoginScreen.jsx ===

Path: `Documents/Github/anti-ai-design-system/ui_kits/default/components/LoginScreen.jsx`

```jsx
// LoginScreen — split-panel (primary left, cream right with form).
const LoginScreen = ({ onLogin }) => {
  const [email, setEmail] = React.useState("joao@barry-callebaut.com");
  const [password, setPassword] = React.useState("••••••••");

  return (
    <div style={{ minHeight: "100%", display: "flex" }}>
      <div style={{ flex: 1, background: "hsl(338 55% 23%)", display: "flex", alignItems: "center", justifyContent: "center" }}>
        <div style={{ textAlign: "center" }}>
          <img src="../../assets/barry-callebaut-logo.svg" alt="Default app" style={{ height: 40, margin: "0 auto 24px" }}/>
          <h1 style={{ color: "#fff", fontSize: 30, fontWeight: 600, marginBottom: 8 }}>ChocoTracking</h1>
          <p style={{ color: "rgba(255,255,255,.6)", fontSize: 18 }}>Gestão de Embarques</p>
        </div>
      </div>
      <div style={{ flex: 1, display: "flex", alignItems: "center", justifyContent: "center", padding: 32, background: "var(--background)" }}>
        <div style={{ width: "100%", maxWidth: 400, display: "flex", flexDirection: "column", gap: 32 }}>
          <div>
            <h2 style={{ fontSize: 24, fontWeight: 700 }}>Entrar</h2>
            <p style={{ color: "var(--muted-foreground)", marginTop: 4 }}>Acesse sua conta para continuar</p>
          </div>
          <form style={{ display: "flex", flexDirection: "column", gap: 20 }} onSubmit={(e) => { e.preventDefault(); onLogin(); }}>
            <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
              <label style={{ fontSize: 13, fontWeight: 500 }}>Email</label>
              <input className="field" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="seu@email.com" />
            </div>
            <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
              <label style={{ fontSize: 13, fontWeight: 500 }}>Senha</label>
              <input className="field" type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="••••••••" />
            </div>
            <button type="submit" className="btn btn-primary" style={{ width: "100%" }}>
              <Icon.LogIn size={16} /> Entrar
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

window.LoginScreen = LoginScreen;
```

---

# === FILE 3/6: ui_kits/default/components/StatCard.jsx ===

Path: `Documents/Github/anti-ai-design-system/ui_kits/default/components/StatCard.jsx`

```jsx
// Stat tile — accent-tinted icon chip + 28-px stat + divider + label/sublabel/trend.
// Mirrors chocotracking/src/components/dashboard/StatsCards.tsx.
const StatCard = ({ icon: I, value, label, sublabel, trend }) => (
  <div className="card" style={{ padding: 20 }}>
    <div style={{ display: "flex", alignItems: "flex-start", gap: 12, marginBottom: 16 }}>
      <div style={{
        width: 40, height: 40, borderRadius: 12,
        background: "hsla(33 47% 53% / .1)",
        display: "flex", alignItems: "center", justifyContent: "center",
      }}>
        <I size={20} color="hsl(33 47% 53%)" />
      </div>
      <div style={{ fontSize: 28, lineHeight: 1.05, fontWeight: 500, color: "var(--foreground)" }}>{value}</div>
    </div>
    <div style={{ height: 1, background: "var(--border)", marginBottom: 12 }}/>
    <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
      <div>
        <div style={{ fontSize: 14, fontWeight: 500 }}>{label}</div>
        {sublabel && <div style={{ fontSize: 12, color: "var(--muted-foreground)", marginTop: 2 }}>{sublabel}</div>}
      </div>
      {trend && <span style={{ fontSize: 12, fontWeight: 500, color: trend.startsWith("-") ? "var(--destructive)" : "hsl(152 85% 30%)" }}>{trend}</span>}
    </div>
  </div>
);

window.StatCard = StatCard;
```

---

# === FILE 4/6: presets/default/lovable-memory/design/tokens.md ===

Path: `Documents/Github/anti-ai-design-system/presets/default/lovable-memory/design/tokens.md`

```markdown
---
name: Design tokens — default preset
description: Tokens semânticos do preset default (warm-editorial flavor — caloroso, editorial, com personalidade)
type: design
---

# Tokens — default preset (warm-editorial flavor)

Source of truth: `src/index.css`. Estrutura literal do chocotracking (Barry Callebaut), brand-agnostic.

## Filosofia

- **Background creme quente** (`30 33% 96%`) — caloroso, não branco frio
- **Foreground marrom escuro** (`16 38% 12%`) — hue alinhado, não preto puro
- **Primary borgonha** (`338 55% 23%`) — drama e personalidade
- **Accent dourado** (`33 47% 53%`) — pontuações de identidade
- **Sidebar usa primary** (mesmo borgonha) — surface dramaticamente diferente do main
- **Radius variável** — `lg/md/sm` baseado em `--radius: 0.5rem`, plus `xl: 12px`, `2xl: 20px` pra hierarquia

## Tokens disponíveis

### Backgrounds
- `bg-background` — creme quente principal
- `bg-card` — branco puro (contraste com bg)
- `bg-popover` — branco
- `bg-muted` — cinza-bege sutil
- `bg-sidebar` — borgonha escuro (primary)

### Foregrounds
- `text-foreground` — marrom escuro principal
- `text-muted-foreground` — marrom médio (texto secundário)
- `text-primary-foreground` — branco (texto sobre primary/sidebar)

### Brand
- `bg-primary text-primary-foreground` — botões CTA, sidebar
- `bg-accent text-accent-foreground` — accent dourado, indicadores

### Status (hue alinhado à temperatura warm)
- `bg-success / text-success` — verde com hue (não neon)
- `bg-warning / text-warning` — âmbar warm
- `bg-info / text-info` — azul mas saturação moderada
- `bg-destructive / text-destructive` — vermelho

### Sidebar specific
- `bg-sidebar` — borgonha escuro (background)
- `text-sidebar-foreground` — branco
- `bg-sidebar-accent` — borgonha levemente mais claro (hover, user panel)
- `bg-sidebar-indicator` — dourado (active state bar)
- `border-sidebar-border` — borgonha mais escuro

## Tipografia

- `font-sans` — Poppins (corpo, default)
- `font-display` — Lora serif (títulos hero, page heros, marcos editoriais)

Use Lora APENAS em h2 de página/hero. Body sempre Poppins.

## Radius scale

- `rounded-sm` — input, campos pequenos
- `rounded-md` — botões pequenos
- `rounded-lg` — botões grandes, dialogs
- `rounded-xl` — rows de tabela, items de lista
- `rounded-2xl` — cards, containers principais

## NÃO criar

- Cor accent custom (use accent dourado existente)
- Variantes saturadas tipo `bg-purple-500`
- Gradientes em backgrounds
- Box shadows pesadas (use border + radius pra hierarquia)
```

---

# === FILE 5/6: skillforge-arsenal/skills/design-system-audit/SKILL.md ===

Path: `Documents/Github/skillforge-arsenal/skills/design-system-audit/SKILL.md`

**STATUS:** skill produção skillforge, em uso ativo. Validada via Input 52 (2026-04-29). Lock-in candidate Wave 7.5.

```markdown
---
name: design-system-audit
description: "Audita app contra design system EXTERNO existente com fase de coerência. Default DS: anti-ai-design-system (Patrick canonical). Use quando: 'tira a cara de IA do app', 'deixa o app mais bonito', 'aplica design system', 'aplica o design system X em Y', 'esse app segue o design system?', 'audita conformidade com design system', 'compara app com tokens', 'onboard app no design system', 'verifica drift do design system', 'design system audit', 'design conformance check'. Diferente de ui-design-system (que GERA do zero) e component-architect (audita health interno). Foco: app contra spec EXTERNA, julgamento de coerência. Se user fala 'design system' sem citar repo: assume default anti-ai-design-system."
---

# Design System Audit

IRON LAW: NEVER apply a pattern without first asking if it fits the target app's context. Patterns are defaults, not commandments. The coherence phase (Phase 4) is non-negotiable — skipping it produces templates burros que copiam estrutura sem adaptação semântica.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--audit` | Inventory + diff + coherence check, output delta report | default |
| `--apply` | Audit + aplica deltas aprovados (gated por delta) | - |
| `--bootstrap` | Scaffold app from scratch following design system | - |
| `--ds-path <path>` | Override default DS reference path | default: ~/Documents/Github/anti-ai-design-system |

## Workflow

(Phase 1 Context Collection → Phase 2 Inventory determinístico → Phase 3 Spec Diff → Phase 4 Coherence Check ⛔ BLOCKING → Phase 5 Delta Report → Phase 6 GATE per-delta)

## Default DS Reference (Wave 7)

**Default path:** `~/Documents/Github/anti-ai-design-system`

Estrutura esperada:
- `docs/03-token-system.md` — regras WCAG AA + tokens
- `docs/07-component-patterns.md` — Login 50/50, AppTable, Configurações user panel
- `presets/default/` — warm-editorial flavor: cream + teal + Lora/Poppins
- `presets/_shared/` — AppTable, StatusBadge

**Phase 2 auto-loads (quando default ativo):**
- ls + cat dos files canonicais do anti-ai-design-system

(SKILL.md completo tem 243 linhas — workflow Phase 1-6 detalhado, Phase 4.5 Contrast Audit WCAG AA, Reference applications chocotracking + charming-solutions + dwg-insight-ext)
```

---

# === FILE 6/6: anti-ai-design-system/SKILL.md (v2 Vitor) ===

Path: `Documents/Github/anti-ai-design-system/SKILL.md`

**ATENÇÃO:** este é o SKILL.md que VOCÊ (Claude Design) gerou na Wave 5. Tem `user-invocable: true` + nome `anti-ai-design`.

```markdown
---
name: anti-ai-design
description: Use this skill to generate well-branded interfaces and assets for the Anti-AI Design System, either for production or throwaway prototypes/mocks/etc. The system ships ONE preset — default (warm-editorial / chocotracking flavor) — engineered to fix the "cara de IA" smell common to AI-generated web apps. Contains essential design guidelines, colors, type, fonts, assets, and UI kit components for prototyping.
user-invocable: true
---

Read the README.md file within this skill, and explore the other available files.

Key files:
- `README.md` — full system: context, content fundamentals, visual foundations, iconography, the default preset, the anti-patterns this system is designed to break
- `colors_and_type.css` — drop-in tokens for the default preset
- `preview/` — 13 individual specimen cards (palettes, type, spacing, radii, shadows, components, shells, the anti-AI checklist)
- `ui_kits/default/` — operations-dashboard recreation (Choco / Barry Callebaut flavor) plus 10 production-lift JSX components

If creating visual artifacts (slides, mocks, throwaway prototypes, etc), copy assets out and create static HTML files for the user to view. Always link `colors_and_type.css`.

If working on production code, you can copy assets and read the rules here to become an expert in designing with this brand. Pay particular attention to the "cara de IA" anti-patterns documented in `preview/17-anti-checklist.html` and the README — that's the whole point of this system.

If the user invokes this skill without any other guidance, ask them:
1. Are they prototyping a one-off artifact, or contributing to a production codebase?
2. What surface are they building — marketing, dashboard, settings, onboarding, etc?

Then act as an expert designer who outputs HTML artifacts _or_ production code, depending on the need. Default to grid CSS over `<table>`, raw divs over `<Card><CardHeader>`, and never inject a Lucide icon into every label.
```

---

## Fim files anexos

Avalie agora os 6 outputs estruturados conforme prompt principal.

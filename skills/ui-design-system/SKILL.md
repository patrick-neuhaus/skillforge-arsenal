---
name: ui-design-system
description: "Generate comprehensive design tokens and design.json for any project. Creates color palettes, typography scales, spacing systems, component specs, animation definitions, and responsive breakpoints from brand inputs. Use when user asks to: create design system, generate design tokens, 'cria um design.json', define color palette, setup typography, 'monta identidade visual', design system from scratch, brand to code, 'preciso de tokens de design', design system audit, build a color palette, setup theme, design tokens for my app, dark mode theme. Supports: full generation, audit existing, apply to components."
---

# UI Design System

IRON LAW: NEVER generate design tokens from abstract descriptions alone — require concrete brand inputs (hex colors, font names, or reference screenshots). "Make it look professional" is not input.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--generate` | Create design.json from brand inputs | default |
| `--audit` | Audit existing design system for consistency | - |
| `--apply` | Apply design tokens to Tailwind config or CSS variables | - |
| `--identity` | Guide user through creating a minimal brand identity (logo, palette, fonts, concept) | - |

## Workflow

```
UI Design System Progress:

- [ ] Phase 1: Brand Input Collection ⚠️ REQUIRED
  - [ ] 1.1 Collect: primary color(s), font(s), concept keywords
  - [ ] 1.2 Identify reference screenshots or existing assets
  - [ ] 1.3 Determine project type (landing, app, dashboard, e-commerce)
- [ ] Phase 2: Design Principles
  - [ ] 2.1 Define 3-5 personality keywords from brand
  - [ ] 2.2 Establish visual hierarchy strategy
- [ ] Phase 3: Token Generation
  - [ ] 3.1 Color palette (primary, neutral, accent, semantic)
  - [ ] 3.2 Typography scale (display, heading, body, caption)
  - [ ] 3.3 Spacing system (base unit + scale)
  - [ ] 3.4 Component specs (buttons, cards, inputs, badges)
  - [ ] 3.5 Effects (shadows, animations, transitions)
  - [ ] 3.6 Responsive breakpoints
- [ ] Phase 4: Review ⛔ BLOCKING
  - [ ] Present design.json with accessibility notes
  - [ ] ⛔ GATE: Get approval before applying to any code
- [ ] Phase 5: Apply (if requested)
  - [ ] Generate Tailwind config or CSS variables from tokens
```

## Phase 1: Brand Input Collection

Ask the user for:
1. **Primary color(s)** — hex codes preferred, or "the green from our logo"
2. **Font(s)** — at least 1 display + 1 body font. If unknown, recommend based on personality.
3. **Concept keywords** — 3-5 words describing the brand feel (e.g., "premium, trustworthy, warm")
4. **Project type** — landing page, web app, dashboard, e-commerce, docs site
5. **References** — "sites you like the look of" or screenshots

If user provides partial inputs, work with them but flag gaps. A hex code + font name produces 10x better results than adjectives alone.

## Phase 2: Design Principles

From brand inputs, derive:
- **Personality keywords** (3-5): e.g., "Premium fintech with warmth"
- **Visual hierarchy**: serif display + sans body = classic premium; all sans = modern tech
- **Color strategy**: primary for CTAs, neutrals for text/bg, accent for highlights, semantic for states

## Phase 3: Token Generation

Load `references/design-json-schema.md` for the complete schema structure.

Generate design.json with 7 sections:
1. **designPrinciples** — keywords + brief rationale
2. **colors** — primary (3 shades), neutral (5 shades), accent (2), semantic (success/warning/error/info)
3. **typography** — families, weights, sizes using `clamp()` for responsive scaling
4. **spacing** — base unit (4px or 8px), scale (xs through 3xl)
5. **components** — button (variants, radius, padding, hover), card (shadow, radius), input (border, focus), badge
6. **effects** — shadows (sm/md/lg), transitions (150-200ms hover, 300ms layout), animations (fade-in-up, stagger)
7. **responsive** — breakpoints (sm 640/md 768/lg 1024/xl 1280), container widths

Key rules:
- `clamp()` for fluid typography: `clamp(1rem, 0.5rem + 1vw, 1.25rem)`
- Shadows create hierarchy: sm for subtle elements, lg for floating/modals
- Every interactive element needs hover + focus + active states

## Phase 4: Review

Present design.json highlighting:
- Color contrast ratios (WCAG AA minimum 4.5:1 for text)
- Typography scale consistency
- Component spec completeness

⛔ **GATE:** Do NOT apply to code without explicit user approval.

## Phase 5: Apply

If approved, generate one of:
- **Tailwind config** — `extend.theme` with design tokens
- **CSS variables** — `:root` with all tokens as custom properties
- **Component examples** — 2-3 key components styled with tokens

## Anti-Patterns

- **Abstract-only input** — "make it nice" without hex/fonts → ask for concrete inputs first
- **Too many colors** — >3 accent colors = visual noise. Limit palette, use shades.
- **Font overload** — max 2 font families. 3+ creates inconsistency.
- **Ignoring semantics** — success/warning/error/info are NOT optional
- **Pixel-only sizes** — use `clamp()` or `rem`. Fixed `px` breaks responsiveness.
- **No hover states** — every interactive element needs hover/focus/active

## Pre-Delivery Checklist

Before presenting design.json:
- [ ] All colors as hex codes (not named colors)
- [ ] Typography uses `clamp()` for responsive sizes
- [ ] At least 3 shadow levels defined (sm, md, lg)
- [ ] Button has primary + secondary + ghost variants
- [ ] Semantic colors included (success, warning, error, info)
- [ ] Spacing scale consistent (powers of base unit)
- [ ] Responsive breakpoints defined with container widths

## When NOT to use

- Project already has mature design system (Chakra/MUI theme) → `--audit` instead
- Quick prototype where design doesn't matter yet → skip
- Backend/API-only project → not applicable
- Confused about which skill to use → invoke maestro

## Integration

- **Component Architect** — use design tokens when creating components
- **React Patterns** — apply tokens via Tailwind/CSS variables in Next.js projects
- **Trident** — `--design` mode validates output in 3 layers (visual, a11y, performance)
- **Context Tree** — map brand assets location in the tree for other skills to find

### Remotion Design Tokens
Load `references/remotion-design-tokens.md` when generating tokens for Remotion video projects.

### Mini Identity Guide
Load `references/mini-identity-guide.md` for `--identity` mode — step-by-step guide to create minimal brand identity from scratch.

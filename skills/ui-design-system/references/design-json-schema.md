# Design JSON Schema — Complete Reference

Consulte este arquivo no **Phase 3** quando for gerar o design.json.

---

## Full Schema Structure

```json
{
  "designPrinciples": {
    "keywords": ["premium", "trustworthy", "warm"],
    "rationale": "Brief description of the visual identity intent"
  },

  "colors": {
    "primary": {
      "base": "#1C3F3A",
      "light": "#2A5F56",
      "dark": "#132D28"
    },
    "neutral": {
      "50": "#FAFAF5",
      "100": "#F5F0E8",
      "200": "#E8E0D0",
      "500": "#8A8070",
      "900": "#1A1A1A"
    },
    "accent": {
      "warm": "#C8956C",
      "cool": "#5B8A72"
    },
    "semantic": {
      "success": "#22C55E",
      "warning": "#F59E0B",
      "error": "#EF4444",
      "info": "#3B82F6"
    }
  },

  "typography": {
    "display": {
      "family": "Playfair Display, Georgia, serif",
      "weights": [400, 700],
      "sizes": {
        "hero": "clamp(2.5rem, 2rem + 2.5vw, 4rem)",
        "h1": "clamp(2rem, 1.5rem + 2vw, 3rem)",
        "h2": "clamp(1.5rem, 1.25rem + 1vw, 2rem)",
        "h3": "clamp(1.25rem, 1rem + 0.5vw, 1.5rem)"
      },
      "lineHeight": 1.2,
      "letterSpacing": "-0.02em"
    },
    "body": {
      "family": "Inter, system-ui, sans-serif",
      "weights": [400, 500, 600],
      "sizes": {
        "lg": "clamp(1.125rem, 1rem + 0.25vw, 1.25rem)",
        "base": "clamp(1rem, 0.875rem + 0.25vw, 1.125rem)",
        "sm": "clamp(0.875rem, 0.8rem + 0.15vw, 0.9375rem)",
        "xs": "0.75rem"
      },
      "lineHeight": 1.6,
      "letterSpacing": "0"
    }
  },

  "spacing": {
    "base": "8px",
    "scale": {
      "xs": "4px",
      "sm": "8px",
      "md": "16px",
      "lg": "24px",
      "xl": "32px",
      "2xl": "48px",
      "3xl": "64px",
      "4xl": "96px"
    },
    "section": {
      "padding": "clamp(3rem, 2rem + 4vw, 6rem) clamp(1rem, 0.5rem + 2vw, 2rem)"
    }
  },

  "components": {
    "button": {
      "variants": {
        "primary": {
          "background": "colors.primary.base",
          "color": "#FFFFFF",
          "hover": { "background": "colors.primary.light", "transform": "translateY(-1px)" }
        },
        "secondary": {
          "background": "transparent",
          "color": "colors.primary.base",
          "border": "1.5px solid colors.primary.base",
          "hover": { "background": "colors.primary.base", "color": "#FFFFFF" }
        },
        "ghost": {
          "background": "transparent",
          "color": "colors.primary.base",
          "hover": { "background": "colors.neutral.100" }
        }
      },
      "borderRadius": "999px",
      "padding": "12px 28px",
      "fontSize": "typography.body.sizes.base",
      "fontWeight": 500,
      "transition": "all 200ms ease"
    },
    "card": {
      "background": "#FFFFFF",
      "borderRadius": "12px",
      "padding": "spacing.lg",
      "shadow": {
        "default": "0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.06)",
        "hover": "0 10px 25px rgba(0,0,0,0.1), 0 4px 10px rgba(0,0,0,0.05)"
      },
      "transition": "box-shadow 300ms ease, transform 300ms ease",
      "hover": { "transform": "translateY(-2px)" }
    },
    "input": {
      "background": "colors.neutral.50",
      "border": "1.5px solid colors.neutral.200",
      "borderRadius": "8px",
      "padding": "12px 16px",
      "focus": {
        "border": "colors.primary.base",
        "ring": "0 0 0 3px rgba(28,63,58,0.15)"
      },
      "fontSize": "typography.body.sizes.base"
    },
    "badge": {
      "borderRadius": "999px",
      "padding": "4px 12px",
      "fontSize": "typography.body.sizes.xs",
      "fontWeight": 500
    }
  },

  "effects": {
    "shadows": {
      "sm": "0 1px 2px rgba(0,0,0,0.05)",
      "md": "0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.06)",
      "lg": "0 10px 25px rgba(0,0,0,0.1), 0 4px 10px rgba(0,0,0,0.05)",
      "xl": "0 20px 50px rgba(0,0,0,0.15)"
    },
    "transitions": {
      "fast": "150ms ease",
      "normal": "200ms ease",
      "slow": "300ms ease",
      "spring": "500ms cubic-bezier(0.175, 0.885, 0.32, 1.275)"
    },
    "animations": {
      "fadeInUp": {
        "from": { "opacity": 0, "transform": "translateY(20px)" },
        "to": { "opacity": 1, "transform": "translateY(0)" },
        "duration": "600ms",
        "easing": "cubic-bezier(0.16, 1, 0.3, 1)"
      },
      "stagger": {
        "delay": "80ms",
        "note": "Apply delay * index to each child element"
      }
    }
  },

  "responsive": {
    "breakpoints": {
      "sm": "640px",
      "md": "768px",
      "lg": "1024px",
      "xl": "1280px"
    },
    "container": {
      "maxWidth": "1200px",
      "padding": "0 clamp(1rem, 0.5rem + 2vw, 2rem)"
    }
  }
}
```

## How to Adapt This Schema

### Customization Points

1. **Colors** — Replace hex values. Keep the structure (primary 3 shades, neutral 5, accent 2, semantic 4).
2. **Typography** — Replace font families. Keep `clamp()` pattern. Adjust ratios for brand personality:
   - Elegant/premium → serif display + sans body, tighter letter-spacing
   - Modern/tech → geometric sans for both, wider spacing
   - Playful → rounded sans, looser spacing
3. **Components** — Adjust borderRadius for personality:
   - `999px` = pill-shaped (friendly, modern)
   - `12px` = rounded (balanced)
   - `4px` = sharp (corporate, technical)
   - `0` = angular (brutalist)
4. **Effects** — Adjust shadow intensity for visual weight:
   - Light shadows = flat, minimal design
   - Heavy shadows = elevated, material design

### Tailwind Config Output

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: { DEFAULT: '#1C3F3A', light: '#2A5F56', dark: '#132D28' },
        accent: { warm: '#C8956C', cool: '#5B8A72' },
      },
      fontFamily: {
        display: ['Playfair Display', 'Georgia', 'serif'],
        body: ['Inter', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        'card': '0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.06)',
        'card-hover': '0 10px 25px rgba(0,0,0,0.1), 0 4px 10px rgba(0,0,0,0.05)',
      },
    },
  },
}
```

### CSS Variables Output

```css
:root {
  --color-primary: #1C3F3A;
  --color-primary-light: #2A5F56;
  --color-primary-dark: #132D28;
  --color-accent-warm: #C8956C;
  --color-accent-cool: #5B8A72;

  --font-display: 'Playfair Display', Georgia, serif;
  --font-body: 'Inter', system-ui, sans-serif;

  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.06);
  --shadow-lg: 0 10px 25px rgba(0,0,0,0.1), 0 4px 10px rgba(0,0,0,0.05);

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 999px;

  --transition-fast: 150ms ease;
  --transition-normal: 200ms ease;
  --transition-slow: 300ms ease;
}
```

## Accessibility Checks

Before finalizing, verify:
- **Text contrast** — primary text on background ≥ 4.5:1 (WCAG AA)
- **Large text contrast** — headings on background ≥ 3:1
- **Interactive elements** — buttons/links ≥ 3:1 against adjacent colors
- **Focus indicators** — visible focus ring on all interactive elements
- **Color not sole indicator** — never use color alone to convey meaning (add icons/text)

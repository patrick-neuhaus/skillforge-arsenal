# Remotion Design Tokens — Tokens para Video

Consulte este arquivo quando gerando design tokens para projetos Remotion.

---

## Diferencas dos Tokens Web

| Aspecto | Web | Remotion |
|---------|-----|---------|
| Unidade de tamanho | rem, px, vw | px (fixo — videos tem resolucao definida) |
| Responsive | Breakpoints, clamp() | Nao tem — resolucao fixa (1920x1080, etc.) |
| Animacoes | CSS transitions, Motion | useCurrentFrame() + interpolate() + spring() |
| Dark mode | CSS variables, classes | Por composicao (decidido no codigo) |
| Fontes | Google Fonts CDN | Fontes locais (bundled) ou @remotion/google-fonts |

## Template de Tokens Remotion

```typescript
// src/remotion/lib/design-tokens.ts

export const tokens = {
  // Resolucao
  width: 1920,
  height: 1080,
  fps: 30,

  // Cores (hex — nao usar CSS variables)
  colors: {
    primary: '#2563EB',
    accent: '#F59E0B',
    background: '#0F172A',
    surface: '#1E293B',
    text: '#F8FAFC',
    textMuted: '#94A3B8',
  },

  // Tipografia (fontes locais ou @remotion/google-fonts)
  fonts: {
    heading: { family: 'Inter', weight: 700, size: 72 },
    body: { family: 'Inter', weight: 400, size: 36 },
    caption: { family: 'Inter', weight: 400, size: 24 },
  },

  // Spacing (px fixo)
  spacing: {
    xs: 16,
    sm: 32,
    md: 64,
    lg: 96,
    xl: 128,
  },

  // Animacao
  animation: {
    fadeIn: { from: 0, to: 30 },    // frames
    slideUp: { distance: 50 },       // px
    springConfig: { damping: 200, mass: 0.5 },
  },
};
```

## Geracao de design.json para Remotion

Quando o usuario pedir design.json pra video, adaptar:
1. Resolucoes em vez de breakpoints (1920x1080, 1080x1920 vertical, 1080x1080 square)
2. Tamanhos em px fixo (nao rem/clamp)
3. Animacoes em frames e spring configs (nao CSS transitions)
4. Fontes como paths locais ou pacotes @remotion/google-fonts

# Anti-AI-DS Bridge (Phase 4)

> Mapeia comprehension.tipo → componentes anti-ai-ds CRM-validated. Carrega na Phase 4.
> Source = path local filesystem.

## Source — path local

```
ANTI_AI_DS_LOCAL = "C:/Users/Patrick Neuhaus/Documents/Github/anti-ai-design-system"
```

Patrick mantem repo local clonado. Skill le tokens + componentes do filesystem.
Sem servidor rodando, sem dependency runtime localhost.

**Fallback:** se path local nao existe, clone ephemeral:
```bash
git clone --depth=1 https://github.com/patrick-neuhaus/anti-ai-design-system.git /tmp/aaads
ANTI_AI_DS_LOCAL=/tmp/aaads
# (cleanup ao final)
```

## Files-chave (path local)

| File | Conteudo |
|---|---|
| `colors_and_type.css` | Tokens base (foundations + preset default warm-editorial) |
| `apresentacao-plus/deck.css` | Plus CRM dark preset + animacoes prontas (kanban, chat, csv, kpi) |
| `presets/default/tokens.css` | Tokens preset default (warm) |
| `ui_kits/default/components/base/_aa-btn.css` | Button component |
| `ui_kits/default/components/surfaces/_aa-card.css` | Card component |
| `ui_kits/default/components/base/_aa-input.css` | Input component |
| `ui_kits/default/components/navigation/_aa-sidebar.css` | Sidebar component |
| `ui_kits/default/showcase/*.css` | Showcase styles (footer, nav, token-editor) |

## Mapping tipo -> componentes

| comprehension.tipo | Componentes principais (anti-ai-ds) | CSS pattern (deck.css) |
|---|---|---|
| crm | aa-btn, aa-sidebar, aa-card, aa-input | kanban-mock, settings-list, kpi-strip |
| chat | aa-card, aa-input | wa-mock (sequence bubbles), conv-drawer |
| viewer | aa-card | flow (4 steps animated) |
| dashboard | aa-card | kpi-strip, chart-mock, kpi-card |
| data-tool | aa-card, aa-input | csv-mock (dropzone + rows + summary) |
| ecomm | (TBD v2) | — |
| docs | (TBD v2) | — |
| landing | (TBD v2) | — |

## Como skill consome

**Default v2:** template do fork artemis-slides (`Documents/Github/open-slide/packages/cli/template/`)
ja vem com `slides/global.css` baked (concat colors_and_type.css + apresentacao-plus/deck.css).

Skill **NAO regenera** os tokens — confia no scaffold do fork. Patrick re-baka via:
```bash
cd Documents/Github/open-slide
bash scripts/sync-anti-ai-ds-tokens.sh
```

Se o slide precisar **componente especifico** (button, card) que nao esta inline no
deck.css, skill le do filesystem:

```bash
cat "$ANTI_AI_DS_LOCAL/ui_kits/default/components/base/_aa-btn.css"
```

E inclui inline no slide TSX (style={{}}) ou append em slides/<id>/component.css.

## Tokens disponiveis (CRM dark, pos baked global.css)

```css
--background: 222 20% 10%
--foreground: 220 15% 92%
--card: 222 20% 14%
--primary: 220 90% 55%      /* blue */
--accent: 280 60% 50%       /* purple */
--accent-decorative: 310 70% 65%  /* pink */
--muted: 222 20% 20%
--border: 222 20% 22%
--success: 152 70% 45%
--warning: 38 90% 55%
--destructive: 0 85% 55%
--radius: 12px

/* type scale */
--text-xs: 13px ... --text-3xl: 32px

/* motion */
--motion-fast: 150ms / --motion-normal: 200ms / --motion-slow: 300ms
--ease-standard / --ease-out / --ease-in / --ease-spring
```

## Fallback se tipo sem template

1. Skill falha vocal: "anti-ai-ds nao tem mapping pra tipo '<X>'. Usa CRM como base ou aborta?"
2. Patrick decide:
   - **(a)** CRM como base (default)
   - **(b)** Aborta + abre issue pra adicionar
   - **(c)** Hybrid: CRM tokens + componentes especificos extraidos do repo target (vira v2 real Layer 4)

## Boundaries

- **Tokens dinamicos:** anti-ai-ds atualizacao depende do Patrick. Skill aponta pro path local + fallback remote, nunca snapshota state interno.
- **Componente novo:** PR no repo `anti-ai-design-system` primeiro, depois consome.
- **Componentes fonte:** anti-ai-ds CRM-validated set. MVP polish > genericidade.

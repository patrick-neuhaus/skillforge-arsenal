# Anti-AI-DS Bridge (Phase 4)

> Mapeia comprehension.tipo → componentes anti-ai-ds CRM-validated. Carrega na Phase 4.

## Pré-condições

- anti-ai-ds rodando em `http://localhost:8000` (ou path declarado pelo user)
- demo correspondente existe em `?demo=<tipo>`
- Patrick sincronizou `/componentes` com versão CRM-validated (per decisão 2026-05-04)

## Mapping tipo → demo + componentes

| comprehension.tipo | anti-ai-ds demo URL | Componentes principais |
|---|---|---|
| crm | `localhost:8000/ui_kits/default/index.html?demo=crm` | button, sidebar, card, dialog, table, badge, dashboard, chart, login |
| chat | `?demo=chat` | message-bubble, input, sidebar, avatar, typing-indicator |
| viewer | `?demo=viewer` | toolbar, canvas, panel, slider, region-select |
| dashboard | `?demo=dashboard` | card, metric, chart, filter-bar, table |
| data-tool | `?demo=data-tool` | table, import-modal, mapping-grid, progress |
| ecomm | (TBD v2 — abrir issue) | — |
| docs | (TBD v2) | — |
| landing | (TBD v2) | — |

## Token copy recipe

Pegar HSL CSS vars do anti-ai-ds e copiar pro deck:

```bash
# 1. Pegar tokens base
curl -s http://localhost:8000/colors_and_type.css > /tmp/anti-ai-ds-tokens.css

# 2. Extrair :root vars relevantes
grep -E "^\s+--(background|foreground|accent|primary|sidebar-|font-)" /tmp/anti-ai-ds-tokens.css

# 3. Copiar pro deck
# (slides/global.css ou inline em cada slide root via style={{}})
```

Vars-chave a propagar:
```
--background, --foreground, --accent, --primary, --primary-foreground
--sidebar-background, --sidebar-foreground
--card, --card-foreground, --border
--font-display, --font-body, --font-mono
--radius
```

## Componentes — como importar

**MVP approach:** copiar componente HTML/CSS standalone do anti-ai-ds direto pro slide TSX. Cada componente fica self-contained no slide (não compartilha módulo, mais simples pra MVP).

**v2 approach:** publicar `@anti-ai-ds/components` como package npm, importar via `import { Button } from '@anti-ai-ds/components'`.

## Fallback

Se `comprehension.tipo` não tem template equivalente:

1. Skill falha vocal: `"anti-ai-ds não tem demo pra tipo '<tipo>'. v2 vai extrair direto. Aborta ou usa template mais próximo (default: crm)?"`
2. Patrick decide manualmente:
   - **(a)** Usa CRM como base com warning
   - **(b)** Aborta e abre issue pra adicionar demo no anti-ai-ds
   - **(c)** Hybrid: CRM base + componentes específicos extraídos do repo target (já vira v2)

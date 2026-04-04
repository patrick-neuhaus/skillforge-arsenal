# Technical SEO — Fundação Técnica

Checklist e regras de SEO técnico. Sem isso funcionando, on-page e off-page não têm efeito.

---

## Core Web Vitals

Métricas de performance que são fator de ranking direto desde 2021.

| Métrica | O que mede | Bom | Precisa melhorar | Ruim |
|---------|-----------|:---:|:----------------:|:----:|
| LCP (Largest Contentful Paint) | Tempo de carregamento do maior elemento visível | < 2.5s | 2.5-4s | > 4s |
| INP (Interaction to Next Paint) | Responsividade a interações | < 200ms | 200-500ms | > 500ms |
| CLS (Cumulative Layout Shift) | Estabilidade visual (elementos pulando) | < 0.1 | 0.1-0.25 | > 0.25 |

### Como melhorar LCP
- Otimizar imagens (WebP, lazy loading, srcset)
- Preload de recursos críticos (fontes, hero image)
- CDN para assets estáticos
- Server-side rendering ou static generation
- Minimizar CSS/JS blocking

### Como melhorar INP
- Dividir tarefas longas de JS (yield to main thread)
- Debounce/throttle event handlers
- Evitar layout thrashing
- Web Workers pra processamento pesado

### Como melhorar CLS
- Dimensões explícitas em imagens e iframes (width/height)
- font-display: swap pra fontes
- Reservar espaço pra ads e embeds
- Evitar inserção dinâmica de conteúdo acima do fold

---

## Meta Tags

### Essenciais (toda página)
```html
<title>Keyword — Qualificador | Marca</title>
<meta name="description" content="Descrição com CTA, < 160 chars">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="canonical" href="https://site.com/url-canonica">
```

### Open Graph (social sharing)
```html
<meta property="og:title" content="Title pro social">
<meta property="og:description" content="Descrição pro social">
<meta property="og:image" content="https://site.com/imagem-1200x630.jpg">
<meta property="og:type" content="article">
```

### Robots
```html
<!-- Padrão: index, follow (não precisa declarar) -->
<!-- Quando NÃO indexar: -->
<meta name="robots" content="noindex, follow">
```

---

## Structured Data (Schema.org)

Markup que ajuda Google entender o conteúdo. Pode gerar rich snippets.

### Tipos mais comuns

| Tipo | Quando usar | Rich snippet |
|------|-----------|:------------:|
| Article | Posts de blog | ✅ (author, date) |
| FAQ | Perguntas frequentes | ✅ (expandable) |
| Product | Páginas de produto | ✅ (preço, rating) |
| LocalBusiness | Negócio local | ✅ (maps, horário) |
| BreadcrumbList | Navegação hierárquica | ✅ (path no resultado) |
| HowTo | Tutoriais passo-a-passo | ✅ (steps) |
| Review | Reviews de produto | ✅ (estrelas) |

### Formato
- **JSON-LD** (recomendado pelo Google) — no `<head>` ou antes do `</body>`
- Validar com Rich Results Test

---

## Sitemap e Robots.txt

### sitemap.xml
- Listar TODAS as páginas que devem ser indexadas
- Atualizar automaticamente quando novo conteúdo é publicado
- Registrar no Google Search Console
- Máximo 50.000 URLs por sitemap (usar sitemap index se mais)

### robots.txt
```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/
Disallow: /search?
Sitemap: https://site.com/sitemap.xml
```

Regra: robots.txt BLOQUEIA crawling, não indexação. Pra bloquear indexação, use `noindex`.

---

## Canonical Tags

### Quando usar
- Página acessível por múltiplas URLs (com/sem www, com/sem trailing slash)
- Conteúdo similar ou duplicado (variações de filtro, paginação)
- Syndicated content (publicado em múltiplos sites)

### Regras
- Canonical aponta pra versão preferida
- Canonical DEVE ser self-referencing (página A tem canonical pra A)
- Não canonicalizar pra páginas com conteúdo muito diferente

---

## HTTPS

- **Obrigatório** — Google marca HTTP como "não seguro"
- Redirect 301 de HTTP → HTTPS em todas as páginas
- Certificado SSL válido e auto-renovável
- Mixed content: zero recursos HTTP em página HTTPS

---

## Mobile-First

Google usa a versão mobile pra indexação. Se mobile está ruim, ranking sofre.

- Responsive design (não site mobile separado)
- Botões touch-friendly (>44x44px)
- Font size legível sem zoom (>16px base)
- Sem horizontal scroll
- Sem interstitials intrusivos (popups que cobrem conteúdo)

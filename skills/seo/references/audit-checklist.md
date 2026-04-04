# Audit Checklist — SEO Completo

Checklist pra auditar site existente. Organizado por domínio. Usar com `--audit`.

---

## 1. Technical SEO

### Crawlability
- [ ] robots.txt permite crawling das páginas importantes
- [ ] sitemap.xml existe e está atualizado
- [ ] sitemap.xml está registrado no Google Search Console
- [ ] Sem páginas importantes bloqueadas por robots.txt ou noindex
- [ ] Redirect chains < 2 hops (A→B ok, A→B→C→D ruim)
- [ ] Sem redirect loops
- [ ] 404s: páginas quebradas identificadas e redirecionadas

### Indexação
- [ ] Páginas importantes estão indexadas (site:dominio.com)
- [ ] Sem index bloat (páginas duplicadas, parâmetros, filtros indexados)
- [ ] Canonical tags corretas em todas as páginas
- [ ] hreflang configurado se site multilíngue

### Performance (Core Web Vitals)
- [ ] LCP (Largest Contentful Paint) < 2.5s
- [ ] FID/INP (Interaction to Next Paint) < 200ms
- [ ] CLS (Cumulative Layout Shift) < 0.1
- [ ] TTFB (Time to First Byte) < 800ms
- [ ] Imagens otimizadas (WebP, lazy loading, dimensões definidas)
- [ ] CSS/JS minificado e comprimido (gzip/brotli)
- [ ] Fontes com font-display: swap

### HTTPS e Segurança
- [ ] HTTPS em todas as páginas
- [ ] Redirect HTTP → HTTPS funcional
- [ ] Certificado SSL válido e não expirado
- [ ] Mixed content: sem recursos HTTP em página HTTPS

---

## 2. On-Page SEO

### Title Tags
- [ ] Toda página tem title tag único
- [ ] Title < 65 caracteres
- [ ] Keyword primária no início do title (quando natural)
- [ ] Sem title duplicados entre páginas

### Meta Descriptions
- [ ] Toda página tem meta description
- [ ] Meta description < 160 caracteres
- [ ] Contém call-to-action ou proposta de valor
- [ ] Sem descriptions duplicadas

### URLs
- [ ] URLs descritivas (slug = keyword ou variação)
- [ ] Sem datas ou números desnecessários
- [ ] Sem stop words excessivas
- [ ] Lowercase, hifenizado
- [ ] Sem parâmetros desnecessários indexados

### Heading Hierarchy
- [ ] H1 único por página
- [ ] H1 contém keyword primária ou variação
- [ ] Hierarquia H1→H2→H3 sem pular níveis
- [ ] Headings descritivos (não "Seção 1", "Capítulo 2")

### Conteúdo
- [ ] Intenção de busca respondida nos primeiros parágrafos
- [ ] Parágrafos curtos (2-4 linhas)
- [ ] Variações semânticas da keyword (não repetição)
- [ ] Links internos pra páginas relacionadas
- [ ] Sem conteúdo duplicado entre páginas
- [ ] Conteúdo thin (<300 palavras) identificado e expandido ou removido

### Imagens
- [ ] Todas com alt text descritivo
- [ ] Nomes de arquivo descritivos (não IMG_0001.jpg)
- [ ] Dimensões definidas no HTML (evita CLS)
- [ ] Formato otimizado (WebP preferido)

### Structured Data
- [ ] Schema.org implementado (Article, FAQ, Product, LocalBusiness conforme tipo)
- [ ] Sem erros no Rich Results Test
- [ ] Breadcrumb schema se site tem hierarquia

---

## 3. Off-Page SEO

### Perfil de Backlinks
- [ ] Domain Rating (DR/DA) > 10 pra site novo, > 30 pra competitivo
- [ ] Backlinks de domínios relevantes ao nicho
- [ ] Sem excesso de links de diretórios/PBNs
- [ ] Anchor text diversificado (não tudo exact match)
- [ ] Sem links tóxicos em volume alto

### Presença
- [ ] Google Business Profile (se negócio local)
- [ ] Perfis em diretórios relevantes do nicho
- [ ] Menções de marca (citations)

---

## 4. Conteúdo e Estratégia

### Cobertura Temática
- [ ] Tópicos principais do nicho cobertos
- [ ] Cluster de conteúdo estruturado (pilar + satélites)
- [ ] Sem gaps de conteúdo vs concorrentes
- [ ] Conteúdo atualizado (sem informação obsoleta)

### Conversão
- [ ] CTAs claros em páginas de conversão
- [ ] Lead magnets onde aplicável
- [ ] Funil definido (informacional → transacional)

---

## Formato de Report

Ao final da auditoria, apresentar:

```
## Diagnóstico SEO — [Site]

### Score Geral: X/100

### Resumo
- Technical: X/25
- On-Page: X/25
- Off-Page: X/25
- Conteúdo: X/25

### Top 5 Ações Prioritárias
1. [Ação] — Impacto: Alto — Esforço: Baixo
2. [Ação] — Impacto: Alto — Esforço: Médio
3. ...

### Detalhes por Domínio
[Findings organizados por domínio]
```

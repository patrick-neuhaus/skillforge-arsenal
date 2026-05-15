---
name: seo
description: "Audita, planeja, implementa e otimiza SEO completo: technical, on-page, off-page, keyword research, semântico, programático, content strategy, arquitetura de site, monetização. Decide categorias vs flat, programático vs manual, subdomain vs subfolder. Gera checklists de auditoria, planos de conteúdo, link building, content batching. Use em: auditar SEO, keyword research, otimizar conteúdo, decidir URL architecture, 'meu site não rankeia', 'como melhorar meu SEO', 'devo usar categorias?', 'programático ou manual?', topical authority, structured data, Core Web Vitals, meta tags, schema markup. NÃO use pra automação n8n pura (n8n-architect) nem frontend/design (ui-design-system)."
---

# SEO Strategist v1

IRON LAW: NUNCA otimize conteúdo sem keyword research fundamentado. Sem dados de busca (volume, dificuldade, intenção), otimização é achismo. Pesquise ANTES de escrever.

## Options

| Option | Descrição | Default |
|--------|-----------|---------|
| `--audit` | Auditar site existente contra checklist completo | - |
| `--keyword` | Pesquisa de palavras-chave pra nicho/página | - |
| `--content` | Otimizar/criar conteúdo com SEO | - |
| `--technical` | Audit técnico (meta, speed, structured data) | - |
| `--architecture` | Decisões de estrutura (categorias, URLs, programático) | - |
| `--programmatic` | Setup de SEO programático | - |
| `--semantic` | Estratégia de SEO semântico (entidades, clusters) | - |
| `--offpage` | Estratégia de link building | - |

## Workflow

```
SEO Progress:

- [ ] Step 1: Contexto ⚠️ REQUIRED
  - [ ] 1.1 Qual o site/projeto? Existe ou é do zero?
  - [ ] 1.2 Qual o nicho/mercado?
  - [ ] 1.3 Qual o objetivo? (tráfego, leads, vendas, autoridade)
  - [ ] 1.4 Monetização: afiliado, display, SaaS, serviço?
  - [ ] 1.5 Existe conteúdo existente ou é greenfield?
- [ ] Step 2: Diagnóstico (se --audit)
  - [ ] 2.1 Load references/audit-checklist.md
  - [ ] 2.2 Analisar technical SEO, on-page, off-page, conteúdo
  - [ ] 2.3 Identificar gaps e oportunidades
  - [ ] ⛔ GATE: Apresentar diagnóstico antes de propor ações
- [ ] Step 3: Estratégia ⚠️ REQUIRED
  - [ ] 3.1 Escolher approach baseado no contexto
  - [ ] 3.2 Se decisão de arquitetura: Load references/architecture-decisions.md
  - [ ] 3.3 Se keyword research: Load references/keyword-research.md
  - [ ] 3.4 Se conteúdo: Load references/content-strategy.md
  - [ ] 3.5 Se programático: Load references/programmatic-seo.md
  - [ ] 3.6 Se semântico: Load references/semantic-seo.md
  - [ ] 3.7 Se off-page: Load references/off-page-seo.md
  - [ ] 3.8 Se técnico: Load references/technical-seo.md
  - [ ] ⛔ GATE: Confirmar estratégia com usuário antes de implementar
- [ ] Step 4: Implementar
  - [ ] 4.1 Executar plano aprovado
  - [ ] 4.2 Se envolve automação (content batching): referenciar n8n-architect
  - [ ] 4.3 Se envolve meta tags em Lovable: referenciar lovable-router
- [ ] Step 5: Validar
  - [ ] 5.1 Rodar checklist de entrega
  - [ ] ⛔ GATE: Apresentar resultado ao usuário
```

## Step 1: Contexto

Pergunte ANTES de agir. SEO sem contexto é genérico demais:

- **Nicho** importa — SEO pra e-commerce ≠ SEO pra blog informativo ≠ SEO pra SaaS
- **Maturidade** importa — site com 500 posts ≠ site novo
- **Monetização** importa — afiliado precisa de volume, SaaS precisa de qualidade
- **Competição** importa — nicho saturado exige off-page pesado, nicho novo é on-page first

## Decisões de Arquitetura

Load `references/architecture-decisions.md` quando o usuário perguntar:
- "Devo usar categorias ou jogar tudo num caminho só?"
- "Programático ou manual?"
- "Subdomain ou subfolder?"
- "Como estruturo as URLs?"

## Keyword Research

Load `references/keyword-research.md` — processo de pesquisa com métricas, ferramentas e priorização.

Regra fundamental: toda página precisa de UMA keyword primária + variações semânticas.

## Content Strategy

Load `references/content-strategy.md` — buyer journey (6 estágios), TF-IDF, featured snippets, AI writing guidelines.

O conteúdo é o core do SEO. Sem conteúdo de qualidade, nenhuma otimização técnica salva.

## SEO Semântico

Load `references/semantic-seo.md` — entidades, topical authority, NLP, schema markup, clusters.

Tendência atual: Google entende ENTIDADES e TÓPICOS, não só keywords. Autoridade temática > keyword stuffing.

## SEO Programático

Load `references/programmatic-seo.md` — quando usar, riscos, templates, automação.

Regra: programático funciona quando tem dados estruturados e intenção de busca clara pra cada página gerada.

## Anti-patterns

| Anti-pattern | Por que é ruim | Correto |
|-------------|----------------|---------|
| Otimizar sem keyword research | Achismo — pode otimizar pra keyword sem volume | Pesquisar volume e dificuldade ANTES |
| Keyword stuffing | Google penaliza desde 2012. Não funciona | Variações semânticas naturais |
| Conteúdo fino (300 palavras) | Não compete com conteúdo aprofundado | Responder a intenção de busca completamente |
| Ignorar intenção de busca | Conteúdo informativo pra keyword transacional = zero conversão | Mapear intent ANTES de escrever |
| Programático sem dados | Páginas vazias/genéricas = spam pra Google | Só programático com dados reais por página |
| Backlinks de PBN | Google desvaloriza/penaliza links artificiais | Guest post, niche edits, conteúdo linkável |
| Title > 65 caracteres | Google trunca, perde impacto | Title < 65 chars com keyword no início |
| URL com datas ou números | Envelhecem, precisam de redirect | URLs descritivas sem temporalidade |
| Ignorar Core Web Vitals | Sinal de ranking direto | LCP <2.5s, FID <100ms, CLS <0.1 |
| AI content sem revisão humana | Google detecta e desvaloriza conteúdo genérico de IA | IA como base + revisão/enriquecimento humano |

## Pre-delivery checklist

- [ ] Keyword research foi feito antes de qualquer otimização
- [ ] Intenção de busca mapeada (informacional, transacional, navegacional)
- [ ] Title < 65 chars com keyword no início
- [ ] Meta description < 160 chars com call-to-action
- [ ] URL clean (sem datas, números, stop words)
- [ ] H1 único com keyword ou variação
- [ ] H2-H3 hierarchy coerente (não pular níveis)
- [ ] Conteúdo responde a intenção de busca nos primeiros parágrafos
- [ ] Variações semânticas usadas naturalmente (não repetição)
- [ ] Structured data (schema.org) quando aplicável
- [ ] Links internos pra páginas relacionadas
- [ ] Imagens com alt text descritivo
- [ ] Core Web Vitals dentro dos limites
- [ ] Se programático: cada página tem conteúdo único e valor real

## Integration

| Skill | Quando combinar |
|-------|----------------|
| **n8n-architect** | Automações SEO: content batching, lead loop, scraping, publicação automática |
| **prompt-engineer** | Prompts pra geração de conteúdo SEO (PROMPT-UNIFICADO, PROMPT-JUDGE) |
| **product-discovery-prd** | Quando SEO é parte de um produto (dash-seo, lead loop) |
| **lovable-knowledge** | Se site é Lovable: meta tags, structured data no framework |
| **lovable-router** | Mudanças que envolvem banco do site SEO (tabela posts, configs) |
| **sdd** | Features complexas de SEO programático usam SDD |
| **maestro** | Maestro roteia "melhorar meu SEO" → esta skill |

## When NOT to use

- **Automação n8n sem contexto SEO** → use n8n-architect
- **Frontend/design** → use ui-design-system
- **Código/implementação de feature** → use sdd
- **Pergunta pontual sobre meta tag** → responda direto

## References

| Arquivo | Conteúdo |
|---------|----------|
| `references/seo-fundamentals.md` | Conceitos base: crawl, index, rank, EEAT, Core Web Vitals |
| `references/keyword-research.md` | Processo de keyword research com métricas e priorização |
| `references/technical-seo.md` | Meta tags, structured data, sitemap, robots, canonical, speed |
| `references/on-page-seo.md` | Title rules, URL structure, H-hierarchy, content optimization |
| `references/off-page-seo.md` | Backlinks, guest post, niche edits, skyscraper, DR/DA |
| `references/programmatic-seo.md` | Geração em massa, templates, automação, quando usar |
| `references/semantic-seo.md` | Entidades, topical authority, NLP, schema markup, clusters |
| `references/content-strategy.md` | Buyer journey, TF-IDF, featured snippets, AI writing |
| `references/architecture-decisions.md` | Categorias vs flat, subdomain vs subfolder, quando programático |
| `references/monetization-models.md` | Display, affiliate, SaaS, infoprodutos, email funnels |
| `references/automation-patterns.md` | Content batching, lead loop, n8n integration, dash-seo |
| `references/audit-checklist.md` | Checklist completo pra auditar site existente |

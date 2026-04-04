# Architecture Decisions — Decisões de Estrutura SEO

Decision trees pra as perguntas mais comuns de arquitetura de site SEO.

---

## Categorias vs Flat (URL Structure)

### A pergunta: "Devo usar /categoria/post ou /post?"

```
O site vai ter 50+ posts no mesmo nicho?
  → Não: Flat (/post) — simples, sem overhead
  → Sim: Tem sub-nichos claramente distintos?
    → Não: Flat — categorizar artificialmente cria estrutura vazia
    → Sim: Categorias (/categoria/post) — ajuda Google e usuário a navegar

O site é um blog pessoal/single-author?
  → Sim: Flat (geralmente)
  → Não: Categorias ajudam a organizar por tema/equipe

O site é e-commerce?
  → Sim: Categorias SEMPRE (/categoria/produto)
```

### Regras

| Estrutura | Quando usar | Exemplo |
|-----------|------------|---------|
| `/post-slug` | Blog < 50 posts, nicho único | /melhor-colchao-2026 |
| `/categoria/post-slug` | Blog > 50 posts, sub-nichos claros | /colchoes/melhor-colchao-mola |
| `/categoria/subcategoria/post` | E-commerce, sites grandes | /moveis/camas/colchao-king |

### Erros comuns
- ❌ Criar 20 categorias com 2 posts cada — estrutura vazia
- ❌ Mudar de flat pra categorias depois de indexado sem redirects — perde tudo
- ❌ Categoria genérica ("geral", "outros") — zero valor SEO

---

## Subdomain vs Subfolder

### A pergunta: "Blog em blog.site.com ou site.com/blog?"

**Resposta curta: Subfolder quase sempre.**

| Opção | Quando usar | Por que |
|-------|------------|---------|
| `site.com/blog` | 95% dos casos | Passa autoridade do domínio pro blog |
| `blog.site.com` | Produto separado, equipe separada | Google trata como site diferente |

Google historicamente trata subdomains como sites separados. Subfolder herda toda a autoridade do domínio principal. A não ser que tenha razão técnica forte (stack diferente, equipe diferente), use subfolder.

---

## Programático vs Manual

### A pergunta: "Devo gerar páginas automaticamente ou escrever cada uma?"

```
Tem dados estruturados pra cada página?
  → Não: Manual — programático sem dados = spam
  → Sim: O dado é ÚNICO por página? (não template com keyword trocada)
    → Não: Manual — Google detecta doorway pages
    → Sim: Cada página responde uma intenção de busca diferente?
      → Não: Manual — páginas sem intent = zero tráfego
      → Sim: PROGRAMÁTICO ✅

Volume justifica automação? (50+ páginas)
  → Não: Manual é mais rápido
  → Sim: Programático + QA + revisão
```

### Cenários onde programático funciona

| Cenário | Dados | Intent | Exemplo |
|---------|:-----:|:------:|---------|
| "Melhor [profissão] em [cidade]" | Dados de cada cidade | Sim (busca local) | ✅ Funciona |
| Comparação A vs B | Features de cada produto | Sim (decisão de compra) | ✅ Funciona |
| Glossário/definições | Definição + exemplos reais | Sim (informacional) | ✅ Funciona |
| "[Keyword] + sinônimos" | Mesmo conteúdo, keyword diferente | Não (mesma intent) | ❌ Spam |
| Landing pages genéricas | Template com cidade trocada | Não (sem dado real) | ❌ Doorway page |

### Riscos do programático

1. **Google Helpful Content Update** — conteúdo sem valor = penalização do site inteiro
2. **Thin content** — páginas com poucas informações únicas
3. **Doorway pages** — páginas criadas só pra SEO sem valor pro usuário
4. **Escala sem QA** — 1000 páginas ruins > 0 páginas

### Mitigação

- **Cada página DEVE ter conteúdo único** — não só template com variável
- **QA obrigatório** — Judge + revisão humana (ver automation-patterns.md)
- **Score mínimo** — só publicar se score >= 60/100
- **Monitorar** — se Google desindexar, parar e revisar

---

## Horizontal vs Vertical (Nicho)

### A pergunta: "Nicho amplo ou específico?"

```
Está começando (DR < 20)?
  → Vertical (específico) — mais fácil rankear, menos competição
  → Exemplos: "colchões infantis" > "móveis"

Já tem autoridade (DR > 30)?
  → Pode expandir horizontal — topical authority conquistada
  → Exemplos: "colchões" → "móveis para quarto" → "decoração"

Monetização é afiliado?
  → Vertical funciona melhor — público com intent de compra

Monetização é display?
  → Horizontal funciona melhor — precisa de volume
```

---

## Single Topic vs Multi-Topic

### A pergunta: "1 site sobre 1 tema ou 1 site sobre vários temas?"

**Google valoriza topical authority** — 1 site profundo > 1 site raso sobre tudo.

| Abordagem | Quando | Risco |
|-----------|--------|-------|
| Single-topic | Site novo, nicho definido | Limita crescimento |
| Multi-topic com clusters | Site maduro, temas relacionados | Dilui autoridade se temas desconexos |
| Multi-site (portfólio) | Temas completamente diferentes | Mais trabalho, mais risco |

**Regra:** Comece single-topic. Expanda pra temas relacionados quando esgotar. Se tema é completamente diferente, considere novo site.

---

## Expired Domains

### A pergunta: "Devo comprar domínio expirado pra ganhar autoridade?"

```
Domínio tem histórico limpo? (Wayback Machine)
  → Não (spam, adult, casino): NUNCA comprar
  → Sim: Domínio é relevante pro seu nicho?
    → Não: Risco de perder autoridade ao mudar nicho
    → Sim: DR > 20 E backlinks reais (não PBN)?
      → Sim: Vale a pena ✅
      → Não: Provavelmente não vale o investimento
```

### Ferramentas pra avaliar
- Wayback Machine (histórico do site)
- Ahrefs/Semrush (perfil de backlinks)
- Spam Score (Moz)
- Verificar se não está em lista de penalização

# Content Strategy — Estratégia de Conteúdo SEO

Como planejar, criar e otimizar conteúdo pra SEO. O conteúdo é o core — sem conteúdo de qualidade, nenhuma técnica salva.

---

## Buyer Journey (6 Estágios) + Templates de Conteúdo

Cada estágio tem tipo de conteúdo e keyword diferentes:

| Estágio | Estado do usuário | Tipo de conteúdo | Template | Exemplo de keyword |
|---------|------------------|-----------------|:--------:|-------------------|
| 1. Dor | Sente problema | Blog informacional | HT (How To) | "dor nas costas ao acordar" |
| 2. Reconhecimento | Identifica o problema | Blog educacional | HT | "problemas de colchão ruim" |
| 3. Busca de solução | Procura opções | Guia, comparativo | HT / BBR | "tipos de colchão" |
| 4. Avaliação | Compara alternativas | Review, top 10 | BBR (Best Buy Review) | "melhor colchão de mola" |
| 5. Decisão | Escolhe qual comprar | Review unitário | SPR (Single Product Review) | "colchão castor D33 é bom?" |
| 6. Compra | Ação final | CTA direto | Landing | "comprar colchão castor" |

### 3 Templates Padrão

| Template | Sigla | Quando usar | Exemplo de trigger |
|----------|:-----:|------------|-------------------|
| Best Buy Review | BBR | "melhor", "melhores", "top X" | "Melhor bicicleta aro 29" |
| Single Product Review | SPR | "é bom?", "vale a pena?", "funciona?" | "Caloi aro 29 é boa?" |
| How To | HT | "como", "passo a passo", "o que é" | "Como andar de bicicleta" |

### Proporção ideal
- **50% informacional / 50% comercial** (mercado BR)
- **60% informacional / 40% comercial** (mercado internacional)
- Sites 100% comerciais perderam ranking após Google HCU

**Estratégia:** Cobrir todos os estágios. Informacional traz volume + autoridade, comercial traz conversão.

---

## Cluster de Conteúdo (Pilar + Satélites)

Estrutura que demonstra topical authority:

```
PILAR: "Guia Completo de Colchões" (3000+ palavras)
  ├── SATÉLITE: "Melhor Colchão de Mola Ensacada"
  ├── SATÉLITE: "Colchão de Espuma vs Mola: Qual Escolher?"
  ├── SATÉLITE: "Como Escolher Firmeza do Colchão"
  ├── SATÉLITE: "Colchão King Size: Vale a Pena?"
  └── SATÉLITE: "Quando Trocar de Colchão"
```

### Regras
- Pilar é broad (cobre o tema inteiro, 2000-5000 palavras)
- Satélites são específicos (cobrem sub-tópicos, 1000-2000 palavras)
- Todos interligados via links internos
- Satélites linkam pro pilar, pilar linka pros satélites

---

## TF-IDF (Term Frequency-Inverse Document Frequency)

Técnica pra garantir cobertura semântica adequada:

### Conceito simplificado
- Analisar os top 10 resultados pra keyword
- Identificar termos/entidades que aparecem em TODOS
- Garantir que seu conteúdo também menciona esses termos

### Na prática
- Se todos os top 10 pra "melhor colchão" mencionam "mola ensacada", "firmeza", "densidade", "D33" — seu conteúdo também deve
- Ferramentas: Surfer SEO, Clearscope, NeuronWriter
- Sem ferramenta: pesquisar manualmente e anotar termos recorrentes

---

## Featured Snippets

Posição zero — resposta direta no topo do Google.

### Como conquistar
1. **Identificar snippet existente** — pesquisar keyword e ver se tem featured snippet
2. **Formatar conteúdo** pra snippet:
   - Parágrafo direto (40-60 palavras respondendo a pergunta)
   - Lista ordenada/não-ordenada (passo a passo)
   - Tabela comparativa
3. **H2/H3 como pergunta** — "O que é X?" seguido de resposta direta

### Exemplo
```
H2: O que é colchão de mola ensacada?

Colchão de mola ensacada é um tipo de colchão que utiliza molas
individualmente embaladas em tecido, permitindo que cada mola
funcione de forma independente. Isso proporciona melhor adaptação
ao corpo e reduz a transferência de movimento entre os ocupantes.
```

---

## AI Writing (Conteúdo com IA)

### Regras pra conteúdo gerado por IA em SEO

1. **IA como base, humano refina** — Google não penaliza IA automaticamente, mas penaliza conteúdo genérico/raso
2. **Adicionar expertise real** — dados, exemplos, opinião fundamentada que IA não tem
3. **Revisão humana obrigatória** — correção factual, tom de voz, precisão
4. **Não publicar em massa sem QA** — 100 posts ruins matam o site todo (Helpful Content Update)
5. **Score mínimo** — usar Judge com threshold (>= 60/100 pra publicar)

### O que a IA faz bem
- Estruturar conteúdo (outline, headings)
- Rascunho inicial (base pra refinar)
- Variações semânticas de keywords
- Formatação (listas, tabelas, comparativos)

### O que a IA NÃO faz bem
- Dados específicos e atualizados (inventa se não sabe)
- Experiência pessoal (EEAT precisa de experiência real)
- Opinião fundamentada (tende a ser neutra/genérica)
- Conteúdo original (recombina, não cria)

---

## Cadência de Publicação

| Estágio do site | Frequência | Por que |
|----------------|:----------:|---------|
| Novo (0-50 posts) | 3-5/semana | Construir base de conteúdo rapidamente |
| Crescimento (50-200) | 2-3/semana | Manter momentum + qualidade |
| Maduro (200+) | 1-2/semana + atualização | Manter + atualizar conteúdo antigo |

**Regra:** Atualizar conteúdo existente é tão importante quanto criar novo. Posts que perdem ranking podem ser recuperados com atualização.

---

## Conteúdo Evergreen vs Trending

| Tipo | Exemplo | Vida útil | Quando |
|------|---------|:---------:|--------|
| Evergreen | "Como escolher colchão" | 2-5 anos | Sempre |
| Trending | "Black Friday colchões 2026" | 1-2 meses | Sazonal |

**Regra:** 80% evergreen, 20% trending. Evergreen é a base, trending é boost.

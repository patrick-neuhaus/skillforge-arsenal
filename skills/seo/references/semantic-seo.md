# Semantic SEO — Entidades, Autoridade Temática e NLP

SEO semântico: otimizar pra como o Google ENTENDE conteúdo, não só pra keywords.

---

## Evolução: Keywords → Entidades

### Antes (keyword-based)
- Google matchava palavras exatas
- "melhor colchão de mola" → procurava essa string exata
- Keyword stuffing funcionava

### Agora (entity-based)
- Google entende CONCEITOS e RELAÇÕES
- "melhor colchão de mola" → Google sabe que "colchão de mola ensacada", "spring mattress", "mola bonnel" são relacionados
- Knowledge Graph: banco de dados de entidades e relações
- BERT/MUM: modelos de NLP que entendem contexto e intenção

---

## Topical Authority

Google favorece sites que cobrem um TÓPICO inteiro profundamente, não sites que cobrem muitos tópicos superficialmente.

### Como construir

```
1. Escolher tópico core (ex: "colchões")
2. Mapear TODOS os sub-tópicos:
   - Tipos de colchão
   - Como escolher
   - Materiais
   - Firmeza
   - Tamanhos
   - Marcas
   - Manutenção
   - Problemas comuns
3. Criar conteúdo pra CADA sub-tópico
4. Interligar via links internos (cluster structure)
5. Atualizar e expandir continuamente
```

### Medição
- **Cobertura temática:** % dos sub-tópicos cobertos vs concorrentes
- **Profundidade:** conteúdo mais completo que o top 3?
- **Interligação:** links internos conectam todos os sub-tópicos?
- **Ranking por grupo:** rankeia pra 10+ keywords do mesmo tema?

---

## Entidades (Entity SEO)

### O que são entidades
Conceitos reais e identificáveis: pessoas, lugares, organizações, produtos, conceitos.

Google tem um Knowledge Graph com bilhões de entidades e suas relações.

### Como otimizar pra entidades

1. **Mencionar entidades relevantes** — não só keywords, mas nomes de marcas, pessoas, conceitos
2. **Definir relações** — "Colchão de mola ensacada, também conhecido como pocket spring, é um tipo de colchão que usa molas individuais"
3. **Usar Schema.org** — structured data que identifica entidades explicitamente
4. **Wikipedia/Wikidata como referência** — se a entidade existe no Knowledge Graph, use o mesmo nome

### Exemplo prático
```
❌ Keyword-only: "O melhor colchão de mola é o colchão de mola ensacada que tem molas"

✅ Entity-rich: "Colchões de mola ensacada (pocket spring) como o Castor D33 e o
Ortobom Exclusive usam molas individualmente encapsuladas em tecido TNT. Diferente
do sistema bonnel, onde as molas são interligadas, o sistema pocket permite que
cada mola responda independentemente ao peso do corpo."
```

---

## Schema Markup pra SEO Semântico

Structured data que explicita entidades e relações pro Google.

### Tipos mais impactantes

| Schema | Quando | Efeito |
|--------|--------|--------|
| Article + author | Todo post | Conecta conteúdo ao autor (EEAT) |
| FAQ | Perguntas no conteúdo | Rich snippet expandível |
| HowTo | Tutoriais | Steps no resultado |
| Product | Reviews de produto | Preço e rating no resultado |
| Organization | Sobre a empresa | Knowledge panel |
| BreadcrumbList | Navegação | Path no resultado |
| SameAs | Perfis sociais | Conecta entidades |

### Exemplo JSON-LD
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Melhor Colchão de Mola Ensacada em 2026",
  "author": {
    "@type": "Person",
    "name": "Nome do Autor",
    "sameAs": ["https://linkedin.com/in/autor"]
  },
  "about": {
    "@type": "Product",
    "name": "Colchão de Mola Ensacada"
  }
}
```

---

## Topic Clusters

Estrutura de conteúdo que sinaliza autoridade temática:

```
PILAR (hub page, broad topic, 3000+ palavras)
  ├── CLUSTER: definições e conceitos
  │   ├── "O que é [X]?"
  │   ├── "Como funciona [X]?"
  │   └── "[X] vs [Y]"
  ├── CLUSTER: guias práticos
  │   ├── "Como escolher [X]"
  │   ├── "Melhores [X] em [ano]"
  │   └── "Onde comprar [X]"
  └── CLUSTER: problemas e soluções
      ├── "[X] não funciona"
      ├── "Problemas com [X]"
      └── "Alternativas a [X]"
```

### Regras de interligação
- Pilar linka pra TODOS os clusters
- Clusters linkam pro pilar
- Clusters do mesmo grupo linkam entre si
- NÃO linkar pra clusters de outro tópico (dilui autoridade)

---

## NLP Optimization

### O que Google entende com NLP
- **Intenção** — o que o usuário realmente quer
- **Entidades** — de quê/quem estamos falando
- **Relações** — como as entidades se conectam
- **Sentimento** — positivo, negativo, neutro
- **Topicalidade** — sobre qual tópico broad é o conteúdo

### Como otimizar pra NLP
1. **Responder a pergunta diretamente** — primeiros 2 parágrafos
2. **Usar linguagem natural** — não keyword stuffing
3. **Definir termos** — "X é Y que faz Z"
4. **Cobrir sub-tópicos** — completude > repetição
5. **Variações semânticas** — sinônimos, termos relacionados, entidades
6. **Contexto claro** — parágrafos coesos, não fragmentos soltos

---

## Ferramentas pra SEO Semântico

| Ferramenta | Pra quê |
|-----------|---------|
| Google NLP API | Analisar entidades no seu conteúdo |
| Surfer SEO | TF-IDF e cobertura semântica |
| MarketMuse | Topic modeling e gaps |
| InLinks | Entity optimization |
| Schema Markup Validator | Validar structured data |
| Google Rich Results Test | Testar rich snippets |

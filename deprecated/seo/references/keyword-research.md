# Keyword Research — Processo de Pesquisa

Processo completo de keyword research. Toda estratégia de SEO começa aqui.

---

## Princípio

Cada página precisa de UMA keyword primária + variações semânticas. Sem keyword research, você está otimizando no escuro.

---

## Métricas que Importam

| Métrica | O que é | Onde ver |
|---------|---------|---------|
| Volume de busca | Buscas/mês pra aquela keyword | Ahrefs, Semrush, Ubersuggest |
| Keyword Difficulty (KD) | Quão difícil é rankear (0-100) | Ahrefs, Semrush |
| CPC (Cost Per Click) | Quanto anunciantes pagam — indica valor comercial | Google Keyword Planner |
| SERP Intent | O que Google mostra (info, transacional, local) | Pesquisar manualmente |
| Competition | Quantos sites competem | Análise manual da SERP |

---

## Processo em 5 Steps

### Step 1: Seed Keywords
Começar com 5-10 termos que descrevem o nicho/negócio:
```
Exemplo (nicho: colchões):
- colchão
- melhor colchão
- colchão de mola
- colchão orthopédico
- como escolher colchão
```

### Step 2: Expandir
Usar ferramentas pra expandir as seeds em centenas de variações:
- **Google Suggest** — digitar keyword e ver sugestões
- **People Also Ask** — perguntas relacionadas na SERP
- **Ahrefs/Semrush** — keyword explorer, related keywords
- **Answer The Public** — perguntas em formato visual
- **Google Search Console** — keywords que já trazem impressões

### Step 3: Filtrar por Métricas
```
Volume > 100/mês (pra nichos pequenos, > 50 já vale)
KD < 30 (pra sites novos, DR < 20)
KD < 50 (pra sites com alguma autoridade, DR > 30)
CPC > $0.50 (indica valor comercial — alguém paga por isso)
```

### Step 4: Classificar por Intenção

| Intenção | Exemplo | Monetização |
|----------|---------|:----------:|
| Informacional | "o que é colchão de mola" | Display, lead magnet |
| Investigativa | "melhor colchão 2026" | Afiliado, comparativo |
| Transacional | "comprar colchão king" | Afiliado, produto |
| Navegacional | "site castor colchões" | Sem valor (busca marca) |

**Regra:** Distribua conteúdo entre as intenções. Só transacional = pouco volume. Só informacional = pouca conversão.

### Step 5: Priorizar

Matriz de priorização:

```
Alto volume + Baixa dificuldade → PRIORIDADE 1 (low-hanging fruit)
Alto volume + Alta dificuldade → PRIORIDADE 3 (longo prazo)
Baixo volume + Baixa dificuldade → PRIORIDADE 2 (quick wins)
Baixo volume + Alta dificuldade → IGNORAR
```

Adicionar: valor comercial (CPC alto sobe na prioridade).

---

## Agrupamento (Clustering)

Agrupar keywords que respondemos com A MESMA página:

```
Grupo: "melhor colchão de mola"
- melhor colchão de mola ensacada (590/mês)
- melhor colchão de mola 2026 (320/mês)
- qual melhor colchão de mola (210/mês)
- top colchões de mola (110/mês)
→ 1 PÁGINA responde todas (keyword primária: "melhor colchão de mola ensacada")
```

**Regra:** Pesquisar no Google — se os mesmos resultados aparecem pra 2 keywords, são a mesma intenção e devem ser 1 página. Se resultados são diferentes, são páginas separadas.

---

## Long-Tail Keywords

Keywords de 3+ palavras com menor volume mas maior especificidade:

| Tipo | Exemplo | Volume | Conversão |
|------|---------|:------:|:---------:|
| Head | "colchão" | 50k | Baixa |
| Mid-tail | "colchão de mola" | 8k | Média |
| Long-tail | "melhor colchão de mola ensacada casal" | 500 | Alta |

**Estratégia pra sites novos:** Foque em long-tail (menos competição, maior conversão). Construa autoridade. Depois ataque mid-tail e head.

---

## Ferramentas

| Ferramenta | Gratuita? | Melhor pra |
|-----------|:---------:|-----------|
| Google Search Console | ✅ | Keywords que já trazem impressões |
| Google Keyword Planner | ✅ | Volume e CPC |
| Ubersuggest | Freemium | Visão geral + sugestões |
| Ahrefs | ❌ ($99/mês) | Análise completa + competidores |
| Semrush | ❌ ($119/mês) | Análise completa + content gaps |
| Answer The Public | Freemium | Perguntas e variações |
| Also Asked | Freemium | People Also Ask clusters |

---

## Output

Ao final do keyword research, entregar:

```
## Keyword Research — [Nicho/Projeto]

### Oportunidades (priorizadas)

| Keyword | Volume | KD | CPC | Intent | Prioridade |
|---------|:------:|:--:|:---:|:------:|:----------:|
| [keyword 1] | X | X | $X | info | 1 |
| [keyword 2] | X | X | $X | trans | 1 |
| ...

### Clusters
- Cluster 1: [tema] — X keywords → 1 página
- Cluster 2: [tema] — X keywords → 1 página

### Próximos passos
- Criar conteúdo pra Prioridade 1 primeiro
- [Recomendação específica]
```

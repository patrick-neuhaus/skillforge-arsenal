# Programmatic SEO — Geração de Páginas em Escala

Quando e como gerar centenas/milhares de páginas otimizadas automaticamente.

---

## O que é SEO Programático

Criar páginas em escala usando templates + dados estruturados. Cada página é gerada automaticamente mas responde uma intenção de busca específica.

### Exemplos reais
- Nomad List: "Custo de vida em [cidade]" × 1000+ cidades
- Zapier: "[App A] + [App B] integration" × 10.000+ combinações
- G2: "[Software] reviews" × 50.000+ produtos
- Wise: "[Moeda A] para [Moeda B]" × 10.000+ pares

---

## Quando Usar (Decision Tree)

```
Tem DADOS ESTRUTURADOS para cada página?
  → Não: ❌ NÃO use programático
  → Sim: Os dados são ÚNICOS por página?
    → Não: ❌ Template com keyword trocada = doorway page
    → Sim: Cada página responde uma INTENÇÃO DE BUSCA diferente?
      → Não: ❌ Páginas sem intent = zero tráfego
      → Sim: Volume justifica automação? (50+ páginas)
        → Não: Manual é mais rápido
        → Sim: ✅ PROGRAMÁTICO
```

---

## Requisitos Obrigatórios

1. **Dados reais por página** — não só trocar keyword no template
2. **Intenção de busca** — cada página responde algo que alguém pesquisa
3. **Conteúdo único** — não pode ser 90% igual entre páginas
4. **Valor pro usuário** — se removesse a página, alguém perderia algo?
5. **QA/Judge** — sistema de qualidade antes de publicar

---

## Arquitetura Típica

```
1. Fonte de dados (banco, API, CSV)
   → Dados estruturados: [entidade, atributos, métricas]

2. Template de página
   → Título: [Template com variável]
   → Conteúdo: [Seções dinâmicas baseadas nos dados]
   → Structured data: [Schema.org dinâmico]

3. Pipeline de geração
   → Template + Dados → HTML/page
   → QA: Judge score >= 60 → publicar
   → Sitemap dinâmico

4. Monitoramento
   → Search Console: indexação, cliques
   → Se <10% indexado: problema de qualidade
```

---

## Tipos de Conteúdo Programático

### Tipo 1: Comparativo (A vs B)
```
Template: "[Produto A] vs [Produto B]: Qual Escolher?"
Dados: features, preço, rating de cada produto
Valor: comparação lado-a-lado com dados reais
Volume potencial: N × (N-1) / 2 combinações
```

### Tipo 2: Localizado ("[X] em [Cidade]")
```
Template: "Melhor [serviço] em [cidade]"
Dados: negócios locais, endereços, avaliações, preços
Valor: informação local específica
Volume potencial: serviços × cidades
```

### Tipo 3: Glossário/Definições
```
Template: "O que é [termo]?"
Dados: definição, exemplos, contexto, termos relacionados
Valor: referência educacional
Volume potencial: todos os termos do nicho
```

### Tipo 4: Integrações
```
Template: "Como integrar [App A] com [App B]"
Dados: steps de integração, screenshots, alternativas
Valor: tutorial específico
Volume potencial: apps × apps
```

---

## Thresholds de Qualidade (dados 2025-2026)

| Métrica | Mínimo seguro | Zona de risco |
|---------|:------------:|:-------------:|
| Palavras únicas por página | ≥ 500 | < 300 |
| Diferenciação entre páginas | 30-40% único | < 20% |
| Bounce rate | < 70% | > 80% |
| Dwell time | > 30s | < 15s |
| Indexation rate | > 80% | < 60% = parar tudo |

### Protocolo de escala seguro
1. **Piloto:** 100 páginas → aguardar 2 semanas
2. **Primeira escala:** 500 páginas → cheques automatizados
3. **Crescimento controlado:** 2.000 páginas → máx 20-30% MoM
4. **Regra absoluta:** NUNCA crescer > 50% mês a mês

### Unique Answer Test (3 gates)
- **Unique Answer:** Se 85%+ do conteúdo é idêntico após trocar variáveis → falha
- **Data Substantiation:** 40% do conteúdo de fontes de dados únicos
- **Engagement Sustainability:** Engajamento dentro de 30% do conteúdo manual

### Traffic Cliff (timeline típica de quem escala errado)
- Meses 1-3: Rankings sobem
- Meses 4-6: Sinais de usuário deterioram
- Meses 7-9: Rankings caem
- Meses 10-12: Tráfego cai 70-90%

**Taxa de falha:** 60% sem QA adequado; 93% dos penalizados não tinham diferenciação suficiente.

## Riscos e Mitigação

| Risco | Consequência | Mitigação |
|-------|-------------|-----------|
| Scaled Content Abuse (política Google mar/2026) | Penalização do site INTEIRO — páginas ruins arrastam domínio pra baixo | QA obrigatório, Unique Answer Test |
| Thin content | Páginas desindexadas | Mínimo 500 palavras com dados reais |
| Doorway pages | Penalização manual | Cada página com valor único |
| Escala sem QA | 1000 páginas ruins | Judge + revisão humana de amostra |
| Canibalização | Páginas competindo entre si | Canonical + diferenciação clara |
| Crescimento explosivo | SpamBrain detecta spike | Max 50% MoM |

---

## Pipeline com n8n

```
1. Cron (diário ou semanal)
   → Buscar próximas N keywords/entidades pendentes (Supabase)

2. Loop Over Items
   → Gerar outline (LLM) baseado no template
   → Gerar conteúdo (LLM) com dados da entidade
   → Judge (LLM) → score 0-100
   → Se >= 60: salvar como "pronto"
   → Se < 60: marcar pra revisão manual
   → Wait (30s entre items)

3. Publicação
   → Batch semanal: publicar posts com score >= 60
   → Gerar sitemap atualizado
   → Submeter ao Google Search Console
```

Ver `references/automation-patterns.md` pra detalhes do pipeline n8n.

---

## Métricas de Sucesso

| Métrica | Alvo | Onde medir |
|---------|------|-----------|
| % páginas indexadas | > 80% | Google Search Console |
| Cliques/página média | > 1/dia | Google Search Console |
| Bounce rate | < 70% | Google Analytics |
| Tempo na página | > 1 min | Google Analytics |
| Judge score médio | > 70/100 | Sistema interno |

**Se < 30% indexado:** Problema grave de qualidade. Pausar geração e revisar.

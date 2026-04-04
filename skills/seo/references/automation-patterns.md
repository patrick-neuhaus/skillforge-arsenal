# Automation Patterns — SEO + n8n

Padrões de automação SEO usando n8n, com foco no produto lead loop e content batching.

---

## Lead Loop (Produto Existente)

Sistema automatizado de geração de conteúdo SEO: keyword → outline → post → publicação.

### Pipeline

```
1. Keyword Research (manual ou semi-automático)
   → Selecionar keywords com volume + baixa dificuldade

2. Outline Generation (n8n + LLM)
   → Input: keyword
   → Output: lista de H2/H3 headings

3. Content Generation (n8n + LLM)
   → Input: keyword + outline + descricao_empresa + foco_empresa
   → Output: post completo (schema JSON)
   → Schema: { title, meta_description, image_query, content[] }

4. Quality Check (n8n + LLM Judge)
   → Avalia: intenção de busca, EEAT, escaneabilidade, riqueza de dados, otimização semântica
   → Score 0-100 (5 critérios × 20 pontos)
   → Se score < 60: rewrite automático

5. Publicação (n8n → Supabase → site)
   → Salvar em tabela posts
   → Gerar imagem de destaque (via image_query)
   → Publicar no site
```

### Schema de Output do Post

```json
{
  "title": "string",
  "meta_description": "string",
  "image_query": "string",
  "content": [
    { "id": 1, "type": "intro", "html": "<p>..." },
    { "id": 2, "type": "h2", "html": "<h2>...</h2><p>..." },
    { "id": 3, "type": "h3", "html": "<h3>...</h3><p>..." }
  ]
}
```

### Critérios do Judge (PROMPT-JUDGE)

| Critério | Peso | O que avalia |
|----------|:----:|-------------|
| Alinhamento com intenção de busca | 20 | Responde o que o usuário procura? |
| EEAT | 20 | Demonstra expertise e credibilidade? |
| Escaneabilidade/UX | 20 | Parágrafos curtos, listas, headings claros? |
| Riqueza de dados | 20 | Informações concretas, não genéricas? |
| Otimização semântica | 20 | LSI keywords, entidades, cobertura semântica? |

---

## Content Batching Patterns

### Pattern 1: Batch semanal (volume baixo)
```
Schedule (toda segunda 8h)
  → Buscar próximas 10 keywords pendentes (Supabase)
  → Loop Over Items
    → Gerar outline (LLM)
    → Gerar post (LLM)
    → Judge (LLM)
    → Se score >= 60: salvar como "pronto"
    → Se score < 60: marcar pra revisão
    → Wait (30s entre items — rate limit LLM)
```

### Pattern 2: On-demand (usuário aciona)
```
Webhook (manual trigger)
  → Recebe: keyword + prioridade
  → Gerar outline + post + judge
  → Notificar usuário via WhatsApp com preview
```

### Pattern 3: Pipeline completo com revisão humana
```
Cron: gerar drafts
  → LLM gera post
  → Judge avalia
  → Se score >= 80: auto-publicar
  → Se 60-80: fila de revisão (notificar editor)
  → Se < 60: rewrite automático + re-judge
```

---

## Regras de Geração de Conteúdo (PROMPT-UNIFICADO)

Regras extraídas do prompt de geração que devem ser respeitadas:

1. **Responder intenção de busca nos primeiros parágrafos** — não enrolar
2. **Parágrafos curtos** (2-4 linhas)
3. **Variações semânticas** — não repetir keyword, usar termos relacionados
4. **Não inventar dados** — se não sabe, qualificar honestamente
5. **Sem datas** — conteúdo evergreen
6. **Sem travessão** — trocar por ponto ou vírgula
7. **Evitar clichês** — "neste artigo você vai aprender" é lixo
8. **H2/H3 que terminam em "?"** — começar com resposta direta

---

## Integração n8n-architect

Quando SEO precisa de automação, invocar n8n-architect com contexto:

```
n8n-architect --build com contexto:
- Template base: Template 2 (Webhook → Process → Supabase)
- Sistemas: Supabase + LLM API (Claude/OpenAI) + Evolution (notificação)
- Volume: X posts/semana
- Error handling: salvar em dead-letter se LLM falhar
- Wave building: recomendado pra pipelines complexos
```

# Examples — Wrappers Reais e Casos de Uso

Consulte este arquivo no **Step 2** para ver exemplos de CLIs otimizados para agentes.

---

## Exemplo 1: Tavily Search API → CLI

### API Original
```json
POST https://api.tavily.com/search
Body: {"query": "...", "max_results": 5}

Response (2000+ tokens):
{
  "query": "react table sorting",
  "response_time": 1.2,
  "results": [
    {
      "title": "TanStack Table Documentation",
      "url": "https://tanstack.com/table/...",
      "content": "Very long content with full page text...",
      "score": 0.95,
      "raw_content": "Even more text...",
      "published_date": "2025-01-15"
    },
    ...5 more items with full content
  ]
}
```

### CLI Wrapper
```bash
$ python tavily.py search "react table sorting" --limit 3

SCORE  TITLE                                    URL
0.95   TanStack Table Documentation             https://tanstack.com/table/...
0.87   React Table Sort Tutorial                https://example.com/...
0.82   Building Sortable Tables in React        https://dev.to/...
```

**Reducao: ~2000 tokens → ~100 tokens (95%)**

### Script (simplificado)
```python
def cmd_search(query, limit=5):
    data = request("POST", "/search", {"query": query, "max_results": limit})
    for r in data.get("results", []):
        print(f"{r['score']:.2f}   {r['title'][:40]:40s}  {r['url']}")
```

---

## Exemplo 2: Inference.sh (Agent Tools de Omer)

### Modelo do Video 1
O Omer criou a skill mais baixada do skills.sh com este padrao:

```
# Skill: "inference apps" → ensina o agente a usar o CLI
# CLI: inference app run -p <tool> <args>

# O agente descobre ferramentas via:
inference apps list

# E executa via:
inference app run -p video --url "https://youtube.com/..."
inference app run -p image --prompt "a cat"
```

**Por que funciona:**
- CLI retorna outputs curtos (nome, status, URL)
- `apps list` = autodiscovery (agente explora sozinho)
- Cada app e um comando, nao precisa configuracao

---

## Exemplo 3: Supabase Queries → CLI Compacto

### Problema: MCP Supabase retorna JSON grande

```json
// MCP response (~500 tokens por query)
{
  "data": [
    {"id": 1, "name": "John", "email": "john@...", "created_at": "...",
     "updated_at": "...", "role": "admin", "avatar_url": "...",
     "settings": {"theme": "dark", ...}, "metadata": {...}}
  ],
  "count": 42,
  "error": null,
  "status": 200,
  "statusText": "OK"
}
```

### CLI Wrapper (~50 tokens)

```bash
$ python supa.py query users --select "id,name,role" --limit 5

ID  NAME            ROLE
1   John Doe        admin
2   Jane Smith      user
3   Bob Wilson      user
4   Alice Chen      admin
5   Carlos Silva    user

(42 total, showing 5)
```

---

## Metricas de Referencia

| Wrapper | API Tokens | CLI Tokens | Reducao |
|---------|:----------:|:----------:|:-------:|
| Tavily search | ~2000 | ~100 | 95% |
| GitHub issues list | ~3000 | ~150 | 95% |
| Supabase query | ~500 | ~50 | 90% |
| FFmpeg info | ~800 | ~40 | 95% |
| Stripe payments | ~1500 | ~80 | 95% |

**Meta: reducao minima de 70%.** Se o CLI nao reduz pelo menos 70%, provavelmente nao vale wrapar.

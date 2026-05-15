# API to CLI Patterns — Padroes de Conversao por Tipo

Consulte este arquivo no **Step 1** para escolher o approach de wrapper correto.

---

## Pattern 1: REST API → Python CLI

**Quando:** API com endpoints REST padrao (GET, POST, PUT, DELETE).

### Estrutura

```python
#!/usr/bin/env python3
"""Tool name — one-line description."""

import sys
import os
import json
import urllib.request
import urllib.error

API_BASE = "https://api.example.com/v1"
API_KEY = os.environ.get("TOOL_API_KEY", "")

def request(method, path, data=None):
    """Make API request with auth."""
    url = f"{API_BASE}{path}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"Error {e.code}: {e.reason}", file=sys.stderr)
        sys.exit(1)

def cmd_search(query, limit=5):
    """Search for items."""
    data = request("GET", f"/search?q={query}&limit={limit}")
    # COMPRESS: extract only relevant fields
    for item in data.get("results", [])[:limit]:
        print(f"{item['id']:8s}  {item['name']:30s}  {item['status']}")

def cmd_get(item_id):
    """Get item details."""
    data = request("GET", f"/items/{item_id}")
    # COMPRESS: show key fields only
    for key in ['id', 'name', 'status', 'created_at']:
        print(f"{key}: {data.get(key, 'N/A')}")

def main():
    if len(sys.argv) < 2 or sys.argv[1] == "--help":
        print("Usage: tool.py <command> [args]")
        print("Commands: search, get, list, create")
        sys.exit(0)
    cmd = sys.argv[1]
    # Route commands...
```

### Compressao de Output

| API retorna | CLI mostra | Reducao |
|-------------|-----------|:-------:|
| JSON completo (50 campos) | 5 campos relevantes | ~90% |
| Array de 100 items | Top 10 em tabela | ~90% |
| Nested objects (3 niveis) | Flat key:value | ~70% |
| Metadata + data | Apenas data | ~50% |

## Pattern 2: SDK/Package → Thin Wrapper

**Quando:** SDK JS/Python ja instalado no projeto.

```python
#!/usr/bin/env python3
"""Supabase CLI wrapper — compact queries for agents."""

from supabase import create_client
import os, sys, json

supabase = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_KEY"])

def cmd_query(table, select="*", limit=10, filter_col=None, filter_val=None):
    q = supabase.table(table).select(select).limit(limit)
    if filter_col and filter_val:
        q = q.eq(filter_col, filter_val)
    data = q.execute()
    # Compact output
    for row in data.data:
        print("\t".join(str(row.get(k, "")) for k in row.keys()))
```

## Pattern 3: Local Binary → Shell Wrapper

**Quando:** Binary ja instalado (FFmpeg, ImageMagick, etc.).

```bash
#!/bin/bash
# ffmpeg-agent — simplified FFmpeg for AI agents

case "$1" in
  info)
    ffprobe -v quiet -print_format json -show_format -show_streams "$2" 2>/dev/null |
      python3 -c "
import json,sys
d=json.load(sys.stdin)
f=d['format']
print(f'Duration: {f.get(\"duration\",\"?\")}')"
    ;;
  convert)
    ffmpeg -i "$2" -y "$3" 2>/dev/null && echo "OK: $3" || echo "FAIL" >&2
    ;;
  *)
    echo "Usage: ffmpeg-agent {info|convert|extract-audio|resize} [args]"
    ;;
esac
```

## Pattern 4: MCP Replacement

**Quando:** MCP server existente retorna JSON pesado.

Estrategia: manter a mesma interface de comandos do MCP, mas retornar output compacto.

```
# MCP retorna (800 tokens):
{"type":"resource","uri":"file:///...","mimeType":"application/json",
"content":{"items":[{"id":"abc","name":"Widget","description":"A long
description...","metadata":{"created":"2025-01-01","updated":"2025-06-01",
"tags":["tag1","tag2"],"author":{"id":"user123","name":"John","email":"..."}},...}]}}

# CLI retorna (50 tokens):
abc  Widget  2025-01-01  tag1,tag2
def  Gadget  2025-02-15  tag2,tag3
```

## Decisao: Quando NÃO Wrapar

| Cenario | Acao |
|---------|------|
| API usada 1x na conversa | Chamar direto, sem wrapper |
| MCP funciona bem e nao e pesado | Manter MCP |
| Binary ja tem CLI excelente | Escrever so SKILL.md, sem wrapper |
| API muda frequentemente | Wrapper vai quebrar — talvez nao vale |

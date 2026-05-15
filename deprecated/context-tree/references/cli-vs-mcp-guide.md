# CLI vs MCP Guide — Detectar Context Bloat

Consulte este arquivo quando detectar uso pesado de MCP ou na operacao de status.

---

## O Problema

MCPs (Model Context Protocol) retornam respostas JSON com metadata, schemas e formatacao pesada. Isso consome context window desproporcionalmente:

| Operacao | Via CLI | Via MCP | Overhead |
|----------|:-------:|:-------:|:--------:|
| Listar 10 items | ~80 tokens | ~800 tokens | 10x |
| Buscar 1 item | ~50 tokens | ~200 tokens | 4x |
| Query com filtro | ~100 tokens | ~1000 tokens | 10x |

## Quando CLI > MCP

| Cenario | Usar CLI | Usar MCP |
|---------|:--------:|:--------:|
| Operacoes frequentes (10+/sessao) | ✅ | ❌ |
| Output grande (listas, tabelas) | ✅ | ❌ |
| Dados simples (texto, numeros) | ✅ | ❌ |
| Operacao unica e rara | ❌ | ✅ |
| Precisa de streaming/webhook | ❌ | ✅ |
| Auth complexa (OAuth flow) | ❌ | ✅ |

## Como Detectar Bloat

Sinais de que MCPs estao consumindo demais:
1. **Respostas ficando mais curtas** — modelo cortando corners
2. **Muitos tool calls por conversa** — cada call adiciona overhead
3. **Repeticao de info ja dada** — modelo "esquecendo" contexto
4. **Conversa com <10 exchanges mas pesada** — MCPs inflaram

## Recomendacoes

Quando detectar bloat de MCP:
1. **Sugerir cli-skill-wrapper** — criar CLI wrapper pra APIs usadas frequentemente
2. **Filtrar campos** — se o MCP permite `--fields`, usar pra reduzir output
3. **Agrupar operacoes** — em vez de 5 calls separadas, 1 batch query
4. **Cache local** — salvar resultado em arquivo e reler (mais barato que re-chamar MCP)

## Integracao com Context Guardian

Quando context-guardian detecta uso alto (yellow/red), verificar:
- Quantas tool calls MCP foram feitas na conversa
- Tamanho medio das respostas
- Se alguma operacao pode ser substituida por CLI

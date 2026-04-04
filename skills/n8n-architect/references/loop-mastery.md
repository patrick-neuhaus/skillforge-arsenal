# Loop Mastery — Como o n8n Processa Dados

Guia profundo sobre o modelo de loop do n8n. Entender isso é pré-requisito pra workflows escaláveis.

---

## Conceito Fundamental: Batch Processing

O n8n processa dados em BATCH, não item por item:

```
5 items entram no Node A → Node A processa os 5 → 5 items saem pro Node B
Node B processa os 5 → 5 items saem pro Node C
```

Implicação: se um node faz HTTP Request, ele faz 5 requests de uma vez (não 1 por vez).

---

## Normalização: Primeira Coisa SEMPRE

Antes de qualquer loop ou processamento, normalizar dados:

```
Dados brutos (20 campos por item)
  → Edit Fields: manter SÓ name, email, phone
  → Restante do workflow processa 3 campos
```

**Por que:** Dados desnecessários propagam por TODOS os nodes seguintes, consumindo memória, CPU e storage. Com 1000 items × 20 campos × 10 nodes = desperdício brutal.

**Regra:** Se não vai usar o campo, remova antes do primeiro node de processamento.

---

## Loop Over Items: Controle Individual

Quando batch padrão não funciona (rate limits, processamento sequencial), use Loop Over Items:

### Batch vs Loop Over Items

| Aspecto | Batch Padrão | Loop Over Items |
|---------|:------------:|:---------------:|
| Processamento | Todos de uma vez | 1 por vez |
| Wait entre items | Não é possível | Sim (ex: 2s entre cada) |
| Rate limiting | Pode violar | Respeita |
| Velocidade | Rápida | Mais lenta, controlada |
| Quando usar | Sem rate limit, volume baixo | Rate limit, volume alto |

### Padrão: Loop + Wait pra APIs

```
Get Data (100 items)
  → Edit Fields (normalizar)
  → Loop Over Items
    → HTTP Request (API externa)
    → Wait (2 segundos)
  → Próximos nodes
```

Resultado: 1 request a cada 2 segundos = 30/min (dentro de rate limit de 60/min com margem).

---

## Wait Node: Onde Importa

### Wait FORA do Loop Over Items
- Workflow pausa
- n8n libera o worker thread (scheduler assume)
- Outros workflows podem rodar enquanto espera
- ✅ Ideal pra delays globais

### Wait DENTRO do Loop Over Items
- Loop pausa por item
- n8n NÃO libera o worker thread
- Thread fica bloqueada durante todo o tempo de espera
- ⚠️ Impacta concorrência

### Impacto na Concorrência

| Cenário | Slots usados | Tempo bloqueado |
|---------|:------------:|:---------------:|
| Wait fora do loop, 20 items | 0 (scheduler) | 0 |
| Wait dentro do loop, 20 items × 5s | 1 | 100 segundos |
| Wait dentro do loop, 100 items × 2s | 1 | 200 segundos |

**Se usa Wait dentro do loop com volume alto:** aumente worker threads no deploy (10 → 20 → 30).

---

## Rate Limiting: Regras Práticas

A maioria das APIs tem limit de ~60 requests/min (1/s). Patterns:

### API com rate limit documentado
```
Rate limit: 60/min
Cálculo: 60s / 60 requests = 1s entre requests
Wait: 1.5s (margem de segurança)
```

### API sem rate limit documentado
```
Começar com: Wait 2s (30/min)
Se funciona sem erro: diminuir pra 1s (60/min)
Se dá 429: aumentar pra 3s (20/min)
```

### Muitos items (1000+)
```
1000 items × 2s = 2000s = ~33 minutos
Considerar: batch de 50 items por execução (Schedule a cada hora)
Ou: Queue Mode pra processamento distribuído
```

---

## Patterns de Loop

### Pattern A: Loop com Rate Limit
```
Data Source → Normalize → Loop Over Items → API Call → Wait(2s) → Process Response → Continue
```

### Pattern B: Loop com Validação
```
Data Source → Normalize → Loop Over Items → IF(válido?) → [Sim] API Call → [Não] Log Error → Continue
```

### Pattern C: Batch sem Loop (volume baixo, sem rate limit)
```
Data Source → Normalize → API Call (batch de 5) → Process Response
```

### Pattern D: Loop + Async Subworkflow
```
Data Source → Normalize → Loop Over Items → Execute SubWorkflow(async) → Continue
```
Cada item dispara subworkflow em background. Respeita concurrency limit do n8n.

---

## Erros Comuns com Loops

| Erro | Consequência | Solução |
|------|-------------|---------|
| Não normalizar antes do loop | Memória explode em volume alto | Edit Fields como primeiro node |
| Wait dentro do loop sem necessidade | Bloqueia worker thread | Mover Wait pra fora se possível |
| Ignorar rate limit | API retorna 429, perde dados | Loop Over Items + Wait |
| Loop Over Items pra 5 items | Over-engineering, mais lento | Batch padrão basta |
| Não tratar erro no loop | 1 item com erro para todos | On Error: Continue + log |

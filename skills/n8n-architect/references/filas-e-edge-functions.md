# Filas do Supabase e Edge Functions — Referência de Implementação

Este arquivo contém detalhes de implementação para quando o usuário precisar configurar filas ou Edge Functions. O SKILL.md principal contém as decisões de QUANDO usar. Este arquivo contém o COMO.

---

## Edge Functions como receptor de webhook

### Quando usar
- Webhooks críticos que não podem se perder
- Alto volume de webhooks (100+ por minuto)
- Quando o n8n pode estar temporariamente indisponível

### Estrutura básica

A Edge Function recebe o webhook, valida minimamente, e faz uma de duas coisas:
1. **Salva direto no Supabase** (tabela de staging) — mais simples
2. **Joga na fila do Supabase** — mais robusto, processamento assíncrono

### Exemplo: Edge Function que recebe e joga na fila

```typescript
// supabase/functions/webhook-receiver/index.ts
import { serve } from "https://deno.land/std@0.168.0/http/server.ts"
import { createClient } from "https://esm.sh/@supabase/supabase-js@2"

serve(async (req) => {
  // 1. Validação mínima
  if (req.method !== 'POST') {
    return new Response('Method not allowed', { status: 405 })
  }

  const body = await req.json()
  
  // 2. Validação de campos obrigatórios (customize por caso)
  if (!body || Object.keys(body).length === 0) {
    return new Response('Empty body', { status: 400 })
  }

  // 3. Conectar ao Supabase
  const supabase = createClient(
    Deno.env.get('SUPABASE_URL')!,
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
  )

  // 4. Enviar pra fila
  const { error } = await supabase.rpc('send_to_queue', {
    queue_name: 'webhook_queue',
    message: body
  })

  if (error) {
    return new Response(JSON.stringify({ error: error.message }), { status: 500 })
  }

  // 5. Responder rápido (o sistema externo não espera processamento)
  return new Response(JSON.stringify({ status: 'queued' }), { status: 200 })
})
```

### Importante sobre Edge Functions
- Timeout padrão: 60 segundos. Pra webhook receiver, deve responder em <2s
- NÃO processe lógica de negócio na Edge Function. Ela só recebe e encaminha
- Use SUPABASE_SERVICE_ROLE_KEY (não anon key) pra operações de escrita na fila
- Edge Functions são stateless — não guardam nada entre execuções

---

## Filas do Supabase (pgmq)

### Setup inicial

1. Habilitar a extensão pgmq no Supabase Dashboard → Database → Extensions
2. Criar a fila via SQL:
```sql
SELECT pgmq.create('webhook_queue');
```

### Operações principais

**Enviar mensagem (send):**
```sql
SELECT pgmq.send('webhook_queue', '{"lead_id": 123, "source": "kommo"}'::jsonb);
```

**Ler e remover (pop) — pra processamento simples:**
```sql
SELECT * FROM pgmq.pop('webhook_queue');
```
- Lê e APAGA imediatamente
- Se o processamento falha depois, a mensagem já foi
- Use quando: processamento é rápido e simples, pode re-enviar se falhar

**Ler com visibility timeout (read) — pra processamento confiável:**
```sql
SELECT * FROM pgmq.read('webhook_queue', 30, 5);
-- 30 = visibility timeout em segundos
-- 5 = quantidade de mensagens
```
- Lê mas NÃO apaga — fica invisível por 30 segundos
- Se confirmar processamento: `SELECT pgmq.delete('webhook_queue', msg_id);`
- Se não confirmar em 30s: mensagem volta pra fila automaticamente
- Use quando: processamento pode falhar, não pode perder dados

### Consumindo fila via n8n

**Padrão com Cron + HTTP Request:**

```
[Cron 30s] → [HTTP Request: Pop da Fila] → [IF: tem dados?] → [Processar] → [Log]
                                                  ↓ (vazio)
                                             [No Operation]
```

HTTP Request pra Pop:
- URL: `https://[PROJECT].supabase.co/rest/v1/rpc/pop_from_queue`
- Método: POST
- Headers: apikey + Authorization Bearer
- Body: `{ "queue_name": "webhook_queue" }`

Nota: Precisa criar uma function SQL wrapper porque pgmq.pop não é exposta diretamente via REST API.

### RLS em Filas
- Por padrão, filas NÃO têm RLS
- Se expor via API pública (anon key), PRECISA configurar RLS
- Se usar apenas via service_role_key (Edge Functions, n8n), não precisa

---

## Padrão completo: Sistema externo → Edge Function → Fila → n8n

```
[Kommo/Meta/etc]
       ↓ webhook POST
[Edge Function: webhook-receiver]
       ↓ valida + enfileira
[Fila Supabase: webhook_queue]
       ↓ 
[n8n Cron 30s: Pop da fila]
       ↓
[Processar item]
       ↓
[Output + Log]
```

### Vantagens desse padrão:
- Se n8n cai, webhooks não se perdem (ficam na fila)
- Edge Function responde em <2s (sistema externo não fica esperando)
- n8n consome no ritmo dele (backpressure natural)
- Pode ter múltiplos n8n consumindo a mesma fila (escalabilidade)

### Quando NÃO usar:
- Webhooks de teste/dev
- Volume baixo (<10 webhooks/hora)
- Webhook que precisa de resposta síncrona (ex: validação em tempo real)

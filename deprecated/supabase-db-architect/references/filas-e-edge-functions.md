# Filas do Supabase e Edge Functions — Referência de Implementação

Este arquivo contém detalhes de implementação para quando o usuário precisar configurar filas ou Edge Functions. O SKILL.md principal contém as decisões de QUANDO usar. Este arquivo contém o COMO.

---

## Edge Functions como receptor de webhook

### Quando usar
- Webhooks críticos que não podem se perder
- Alto volume de webhooks (100+ por minuto)
- Quando o n8n pode estar temporariamente indisponível

### Limites atualizados (2026)
- **CPU time:** 2 segundos (execução real, não inclui async I/O)
- **Wall clock:** 400 segundos max (Free/Pro: 150s pra resposta inicial)
- **Background:** após retornar, requests background podem rodar 400s
- **Runtime:** Supabase Edge Runtime (compatível com Deno, NÃO é Deno CLI padrão)
- **Pra webhook receiver:** deve responder em <2s (dentro do CPU time)

### Estrutura básica

A Edge Function recebe o webhook, valida minimamente, e:
1. **Salva direto no Supabase** (tabela de staging) — mais simples
2. **Joga na fila do Supabase** (pgmq) — mais robusto

### Exemplo: Edge Function que recebe e enfileira

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

  if (!body || Object.keys(body).length === 0) {
    return new Response('Empty body', { status: 400 })
  }

  // 2. Conectar ao Supabase (use sb_secret_* em projetos novos)
  const supabase = createClient(
    Deno.env.get('SUPABASE_URL')!,
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
  )

  // 3. Enviar pra fila
  const { error } = await supabase.rpc('send_to_queue', {
    queue_name: 'webhook_queue',
    message: body
  })

  if (error) {
    return new Response(JSON.stringify({ error: error.message }), { status: 500 })
  }

  // 4. Responder rápido
  return new Response(JSON.stringify({ status: 'queued' }), { status: 200 })
})
```

### Importante sobre Edge Functions
- NÃO processe lógica de negócio na Edge Function. Ela só recebe e encaminha.
- Use `SUPABASE_SERVICE_ROLE_KEY` (ou `sb_secret_*`) pra escrita na fila.
- Edge Functions são stateless.
- Pra dev local: `supabase functions serve` usa Edge Runtime (mesmo ambiente que produção).

---

## Filas do Supabase (pgmq)

### Setup inicial

1. Habilitar a extensão pgmq no Dashboard → Database → Extensions
2. Criar a fila:
```sql
SELECT pgmq.create('webhook_queue');
```

### Operações principais

**Enviar mensagem (send):**
```sql
SELECT pgmq.send('webhook_queue', '{"lead_id": 123, "source": "kommo"}'::jsonb);
```

**Ler e remover (pop) — processamento simples:**
```sql
SELECT * FROM pgmq.pop('webhook_queue');
```
- Lê e APAGA imediatamente
- Se processamento falha depois, mensagem se perdeu

**Ler com visibility timeout (read) — processamento confiável:**
```sql
SELECT * FROM pgmq.read('webhook_queue', 30, 5);
-- 30 = visibility timeout em segundos
-- 5 = quantidade de mensagens
```
- Lê mas NÃO apaga — fica invisível por 30 segundos
- Confirmar: `SELECT pgmq.delete('webhook_queue', msg_id);`
- Se não confirmar em 30s: mensagem volta pra fila

### Consumindo fila via n8n

```
[Cron 30s] → [HTTP Request: Pop da Fila] → [IF: tem dados?] → [Processar] → [Log]
                                                  ↓ (vazio)
                                             [No Operation]
```

HTTP Request pra Pop:
- URL: `https://[PROJECT].supabase.co/rest/v1/rpc/pop_from_queue`
- Método: POST
- Headers: apikey + Authorization Bearer (usar sb_secret_*)
- Body: `{ "queue_name": "webhook_queue" }`

Nota: Precisa criar function SQL wrapper porque pgmq.pop não é exposta diretamente via REST API.

### RLS em Filas
- Por padrão, filas NÃO têm RLS
- Se expor via anon key, PRECISA configurar RLS
- Se usar apenas via service_role/sb_secret_*, não precisa

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

### Vantagens:
- Se n8n cai, webhooks ficam na fila
- Edge Function responde em <2s
- n8n consome no ritmo dele (backpressure natural)
- Múltiplos n8n consumindo a mesma fila (escalabilidade)

### Quando NÃO usar:
- Webhooks de teste/dev
- Volume baixo (<10 webhooks/hora)
- Webhook que precisa de resposta síncrona

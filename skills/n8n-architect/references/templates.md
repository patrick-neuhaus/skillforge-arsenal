# Templates de Workflows n8n

Templates prontos para os fluxos mais comuns. Use como base e customize conforme o projeto.

---

## Template 1: Webhook → Processar → Supabase

**Uso:** Qualquer integração que recebe dados via webhook e salva no Supabase.

```
[Webhook] → [Validar Campos] → [Formatar Dados] → [Inserir no Supabase] → [Responder 200]
                   ↓ (inválido)                           ↓ (erro)
             [Responder 400]                      [Log Erro Supabase]
```

**Nodes:**

1. **Webhook** (Webhook node)
   - Método: POST
   - Path: /nome-descritivo
   - Response Mode: "Last Node" (pra poder retornar status customizado)

2. **Validar Campos** (IF node)
   - Checar campos obrigatórios: `{{ $json.campo !== undefined && $json.campo !== "" }}`
   - Se inválido → Respond com 400 + mensagem clara

3. **Formatar Dados** (Set node)
   - Mapear campos do webhook pros nomes das colunas do Supabase
   - Adicionar campos extras: created_at, source, etc.

4. **Inserir no Supabase** (HTTP Request node)
   - URL: `https://[PROJECT].supabase.co/rest/v1/[TABELA]`
   - Método: POST
   - Headers: apikey, Authorization (Bearer), Content-Type: application/json, Prefer: return=representation
   - Body: dados formatados
   - On Error: Continue (pra capturar erro sem quebrar)

5. **Log Erro** (HTTP Request node, branch de erro)
   - Inserir em tabela de logs com: workflow, node, erro, input, timestamp

---

## Template 2: Webhook Kommo → Processar Lead

**Uso:** Receber webhooks do Kommo quando lead muda de status/pipeline.

```
[Webhook Kommo] → [Extrair Lead ID] → [Buscar Lead Completo] → [Processar por Status] → [Ação]
```

**Notas importantes sobre Kommo:**
- Webhook do Kommo manda payload minimalista — geralmente só o ID. Você PRECISA buscar o lead completo via API.
- Webhooks podem vir duplicados. Implemente idempotência (check se já processou esse evento).
- Pipeline/status vêm como IDs numéricos, não nomes. Mapeie num Set node.

**Nodes:**

1. **Webhook Kommo** (Webhook node)
   - Recebe: leads[status][0][id], leads[status][0][status_id], etc.

2. **Extrair Lead ID** (Set node)
   - `lead_id`: extrair do path correto do payload (varia por tipo de evento)

3. **Buscar Lead Completo** (HTTP Request node)
   - URL: `https://[DOMAIN].kommo.com/api/v4/leads/{{ $json.lead_id }}?with=contacts,catalog_elements`
   - Headers: Authorization: Bearer [TOKEN]

4. **Processar por Status** (Switch node)
   - Branching por status_id pra diferentes ações

---

## Template 3: Meta Lead Ads → CRM + Notificação

**Uso:** Processar leads que chegam de formulários do Facebook/Instagram.

```
[Webhook Meta] → [Extrair Dados do Form] → [Montar Texto Legível] → [Criar Lead no CRM] → [Notificar via WhatsApp]
                                                                              ↓
                                                                    [Verificar is_test_lead]
```

**Nodes:**

1. **Webhook Meta** — Recebe o payload do Meta Lead Ads
2. **Extrair Dados** — Iterar sobre field_data pra montar key:value
3. **Filtrar Test Lead** — IF: `{{ $json.is_organic === false }}` → pode ser teste
4. **Montar Texto Legível** — Formatar respostas_forms em texto limpo pra WhatsApp
5. **Criar no CRM** — HTTP Request pro Kommo/CRM com campos mapeados
6. **Notificar** — Enviar resumo via Evolution API / WhatsApp

---

## Template 4: Cron → Processar Fila

**Uso:** Jobs agendados que processam itens de uma fila (follow-ups, emails, limpeza).

```
[Cron Trigger] → [Verificar Janela Horária] → [Buscar Itens Pendentes] → [Loop: Processar Item] → [Atualizar Status]
                        ↓ (fora da janela)                                        ↓ (erro por item)
                   [Parar / Log]                                            [Log Erro + Continuar]
```

**Notas:**
- Sempre verifique janela horária (7h-21h pra mensagens) antes de processar
- Expressão pra verificar hora no n8n: `{{ new Date().getHours() >= 7 && new Date().getHours() < 21 }}`
- ATENÇÃO: considere timezone. n8n pode estar em UTC. Use: `{{ new Date(new Date().toLocaleString("en-US", {timeZone: "America/Sao_Paulo"})).getHours() }}`
- Processe em batch com limit (ex: 50 por execução) pra não sobrecarregar
- Cada item deve ter tratamento de erro individual — um erro não pode parar a fila inteira

---

## Template 5: WhatsApp Inbound → Processar → Responder

**Uso:** Receber mensagem do WhatsApp via Evolution API e responder.

```
[Webhook Evolution] → [Extrair Mensagem] → [Identificar Intenção] → [Gerar Resposta] → [Enviar via Evolution]
                                                                           ↓
                                                                    [Log Conversa]
```

**Nodes:**

1. **Webhook Evolution** — Recebe evento MESSAGES_UPSERT
   - Filtrar: ignorar mensagens do próprio bot (key.fromMe === true)
   - Filtrar: ignorar status messages e reactions

2. **Extrair Mensagem** (Set node)
   - remoteJid: `{{ $json.data.key.remoteJid }}`
   - message: `{{ $json.data.message.conversation || $json.data.message.extendedTextMessage?.text || "" }}`
   - pushName: `{{ $json.data.pushName }}`

3. **Gerar Resposta** (HTTP Request → GPT/Gemini)
   - System prompt + contexto
   - Response em JSON Schema definido: `{ mensagem: string, encaminhar_humano: boolean }`

4. **Enviar Resposta** (HTTP Request → Evolution API)
   - URL: `https://[EVOLUTION_URL]/message/sendText/[INSTANCE]`
   - Body: `{ number: remoteJid, text: resposta }`

---

## Template 6: OCR Pipeline

**Uso:** Receber documento, extrair texto com OCR, estruturar dados.

```
[Receber Doc] → [Upload Supabase Storage] → [Log Pré-OCR] → [Extrair Texto (Gemini)] → [Extrair Campos Estruturados] → [Salvar Campos] → [Log Pós-OCR]
                                                                      ↓ (erro)
                                                                [Log Erro + Notificar]
```

**Notas:**
- Gemini pra OCR: usar com responseSchema JSON pra forçar estrutura
- Separar extração de texto da extração de campos — são 2 chamadas diferentes ao LLM
- Campos de extração variam por tipo de documento (PGR, PCMSO, ASO, EPI) — usar schema diferente por tipo
- Sempre salvar o texto bruto ANTES de processar campos — se o schema mudar, pode reprocessar sem refazer OCR

---

## Template 7: Follow-up Campaign

**Uso:** Enviar mensagens de follow-up agendadas por campanha.

```
[Cron 15min] → [Verificar Janela 7-21h] → [Buscar Próximos da Fila] → [Loop por Item] → [Montar Mensagem] → [Enviar] → [Atualizar Fila] → [Agendar Próximo Step]
                                                                              ↓ (erro envio)
                                                                        [Marcar Falha + Retry]
```

**Notas:**
- Fila em Supabase: follow_up_queue com campos (contact_id, campaign_id, step_number, scheduled_at, status)
- Unique constraint em (contact_id, campaign_id, step_number) pra evitar duplicatas
- ON CONFLICT pra reagendamento
- Cada campanha tem seus próprios steps em campanha_config
- Um contato pode estar em múltiplas campanhas simultaneamente
- Sempre verificar se o contato respondeu antes de enviar próximo step

# Padrões de Arquitetura n8n

Última atualização: 2026-04-03

Referência completa de padrões arquiteturais para workflows n8n. O SKILL.md contém a visão geral e hierarquia; este arquivo tem os detalhes de implementação.

---

## Hierarquia de Nodes (reforçada pelo n8n 2.0)

1. **1º Edit Fields (Set) com expressões inline** — Transformar, renomear, calcular, formatar dados. Roda DENTRO do processo principal do n8n, rápido e estável.
2. **2º Core nodes** — Filter, IF, Switch, Split Out, Merge, Summarize, Limit, Sort, Remove Duplicates. Lógica de fluxo e manipulação de coleções. Otimizados e in-process.
3. **3º Code node** — ÚLTIMO recurso. No n8n 2.0+, Code node executa FORA do processo via Task Runner (round-trip adicional). Use apenas quando: a lógica precisaria de 5+ nodes encadeados, transformação é complexa demais pra expressão inline, ou precisa de biblioteca específica. Suporta JavaScript e Python (Python tem overhead de compilação extra).
4. **HTTP Request > nodes nativos de API / community nodes** — Prefira HTTP Request sobre nodes nativos (Kommo node, Slack node) ou community nodes — muitos são mal implementados, desatualizados, ou limitados. HTTP Request dá controle total sobre URL, headers, body e error handling.

---

## Nomenclatura de Workflows

```
[CLIENTE] - [TIPO] - [DESCRIÇÃO]
Exemplos:
  Capitalize - SDR - Qualificação WhatsApp
  AW Control - OCR - Pipeline Documentos
  Studio Artemis - Lead - Processamento Meta Ads
  INTERNO - Cron - Keep-alive Supabase
```

Tipos válidos: SDR, Lead, OCR, Cron, Webhook, Integração, Notificação, Relatório, AI

## Nomenclatura de Nodes

Renomeie TODOS os nodes. Nome padrão do n8n ("HTTP Request", "IF", "Code") não diz nada.

Padrão: `[Ação] [Alvo]`
```
Exemplos:
  Buscar Lead no Kommo
  Inserir Documento no Supabase
  Enviar Mensagem WhatsApp
  Verificar Status do Lead
  Formatar Resposta Gemini
  Tratar Erro de API
```

---

## Estrutura Padrão de Workflow

Todo workflow de produção deve seguir esta estrutura:

```
1. TRIGGER (webhook, cron, evento, ou Chat Trigger)
   ↓
2. VALIDAÇÃO (dados estão corretos? campos obrigatórios presentes?)
   ↓
3. PROCESSAMENTO (a lógica de negócio)
   ↓
4. OUTPUT (salvar resultado, enviar mensagem, atualizar CRM)
   ↓
5. LOG (registrar o que aconteceu — sucesso ou erro)
```

Se o workflow não tem as etapas 2 e 5, questione.

---

## Execution Data (checkpoints pra filtrar execuções)

O n8n não tem filtro nativo por tempo de execução ou por dados processados. O node **Execution Data** resolve isso: salva metadata customizada na execução que depois aparece como filtro na lista de execuções.

**Quando usar:**
- Workflows de alto volume onde você precisa achar uma execução específica
- Depois de branches importantes (IF/Switch) pra saber qual caminho a execução seguiu
- Quando a equipe vai precisar debugar workflows que não criou

**Padrão de dados a salvar:**
- Identificador do registro processado (lead_id, document_id, client_name)
- Branch que foi seguido (resultado=qualificado, resultado=erro_validação)
- Dados de negócio relevantes pra busca (cliente, campanha, tipo)

**Regra:** Não salve dados sensíveis (tokens, senhas) no Execution Data — fica visível pra qualquer usuário do n8n.

---

## Webhook direto vs Edge Function + Fila

Quando um sistema externo manda webhook pro n8n, existe risco: se o n8n tá fora do ar, o webhook se perde. Pra workflows críticos, use Edge Function do Supabase como camada de recepção.

**Padrão direto (OK pra maioria dos casos):**
```
[Sistema externo] → [Webhook n8n] → [Processa]
```

**Padrão com fila (pra workflows críticos):**
```
[Sistema externo] → [Edge Function Supabase] → [Fila Supabase] → [n8n via Cron/Pop] → [Processa]
```

**Quando usar cada um:**
- Webhook de teste/dev → direto
- Webhook de lead (Kommo, Meta) → direto com retry (perder 1 lead não é catástrofe)
- Webhook financeiro, OCR crítico, pipeline de vendas → fila
- Alto volume (100+ webhooks/min) → fila obrigatório

Detalhes de implementação em `filas-e-edge-functions.md`.

---

## Modularização (DRY/KISS)

### Quando usar subworkflow

Use subworkflow quando:
- O mesmo bloco de lógica aparece em 2+ workflows
- O workflow principal tá ficando grande demais (mais de 20 nodes)
- Você quer isolar uma parte pra facilitar debug
- A equipe precisa reutilizar algo que você construiu

Não use subworkflow quando:
- É lógica usada uma vez só — complexidade extra sem ganho
- O subworkflow teria 3 nodes ou menos — não justifica

### Subworkflows síncronos vs assíncronos

- **Síncrono** (Execute Workflow node): O workflow pai ESPERA o sub terminar. Use quando precisa do resultado de volta.
- **Assíncrono** (Execute Workflow Trigger): O workflow pai dispara e segue. Use quando não precisa do resultado.

### Organização em pastas

```
📁 [CLIENTE]
  📁 Subworkflows
    - [CLIENTE] - SUB - Enviar WhatsApp
    - [CLIENTE] - SUB - Buscar Lead Kommo
  📁 Produção
    - [CLIENTE] - SDR - Qualificação
    - [CLIENTE] - Lead - Processamento
  📁 AI
    - [CLIENTE] - AI - Chatbot WhatsApp
    - [CLIENTE] - AI - Classificação Documentos
  📁 Crons
    - [CLIENTE] - Cron - Fila Follow-up
```

### Salvamento seletivo de execuções

- Workflows de alto volume (cron a cada 5 min): salvar APENAS execuções com erro
- Workflows críticos: salvar todas
- Subworkflows: geralmente não precisa salvar (o pai já salva)
- Configurar em: Workflow Settings → Save Execution Data

### Implementação em waves (workflows complexos)

Quando um workflow é grande (10+ integrações, múltiplos branches), não tente construir tudo de uma vez:

- **Wave 1:** Trigger + fluxo principal (caminho feliz) + output básico. Testa se o core funciona.
- **Wave 2:** Branches alternativos + error handling (4 camadas) + Execution Data. Testa se lida com falhas.
- **Wave 3:** Otimização (Redis cache, fila, subworkflows, Circuit Breaker) + documentação (sticky notes, nomes de nodes).

Cada wave deve ser testável sozinha. Se estiver delegando, especifique no briefing qual wave.

---

## Redis como Infraestrutura (quando escalar)

Pra cenários que precisam de velocidade ou atomicidade além do que Supabase oferece:

- **Cache de tokens:** Armazenar access_token com TTL. Evita buscar no banco toda execução
- **Rate limiting:** Contadores atômicos com INCR + EXPIRE
- **Filas rápidas:** LPUSH/RPOP pra filas de alta velocidade
- **Lock distribuído:** Evitar que 2 execuções processem o mesmo item simultaneamente
- **Circuit Breaker state:** Armazenar contadores de falha com TTL

**Quando usar Redis vs Supabase vs Data Tables:**
- Dados persistentes que importam (leads, documentos, logs) → Supabase
- Dados temporários, cache, contadores, locks → Redis
- Filas de baixo volume → Supabase Queues (pgmq)
- Filas de alto volume (100+ msg/min) → Redis ou RabbitMQ
- Estado de workflow (flags, config, markers) → Data Tables do n8n

---

## Data Tables do n8n (banco embutido)

Data Tables são um banco de dados embutido no n8n, disponível pra todos os planos:
- **Performance:** Insert em 8ms, 100x mais rápido que Google Sheets
- **Limite:** 50 MB (cloud)
- **Sem rate limiting**

**Quando usar Data Tables vs Supabase:**
- Config de workflow, flags, markers de deduplicação → Data Tables (sem API call, 8ms)
- Dados de negócio, logs persistentes, dados compartilhados entre sistemas → Supabase
- Estado de Circuit Breaker (se não tem Redis) → Data Tables
- Mini-CRM temporário, contexto de IA → Data Tables

**Quando NÃO usar:**
- Dados que precisam de RLS ou segurança → Supabase
- Dados acessados por outros sistemas além do n8n → Supabase
- Volume > 50 MB → Supabase

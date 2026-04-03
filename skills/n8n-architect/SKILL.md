---
name: n8n-architect
description: "Skill de arquitetura e padrões para automações n8n. Use esta skill SEMPRE que o usuário mencionar: n8n, workflow, automação, webhook, integração entre sistemas, 'preciso conectar X com Y', subworkflow, error handling, retry, 'meu workflow não funciona', 'como faço isso no n8n', 'como delego esse workflow', ou qualquer variação que envolva construção, debug, documentação ou delegação de automações. Também use quando o usuário estiver planejando um fluxo que envolve múltiplos sistemas (Supabase + API externa + WhatsApp, por exemplo) — mesmo que não mencione n8n explicitamente, se a solução natural é uma automação, esta skill se aplica. Se o contexto for delegação de workflow pra equipe, combine com a skill de Tech Lead & PM. NÃO use se o pedido é sobre SQL, schema ou banco de dados sem envolver automação — use supabase-db-architect. Se é frontend/Lovable puro, não envolve n8n."
---

# n8n Automation Architect v3

## Contexto

O usuário é especialista em n8n com forte preferência por HTTP Request nodes sobre Code nodes. A equipe (Hygor, Jonas) trabalha com n8n, então a skill também serve para gerar briefings técnicos delegáveis. Stack principal: n8n + Supabase + Evolution API + Kommo + Mautic.

## n8n 2.0 — Mudanças fundamentais

O n8n 2.0 (stable dez/2025) trouxe mudanças arquiteturais que afetam TUDO que esta skill recomenda. Internalize isso antes de qualquer decisão.

### Draft vs Published

n8n agora separa salvar de publicar:
- **Save** → salva como Draft, NÃO afeta produção
- **Publish** → deploya pra produção

Impacto prático: agora você pode editar workflows em produção sem medo. Salve quantas vezes quiser, só publica quando tiver certeza. Isso muda completamente o workflow de desenvolvimento — antes era "salvar = deploy", agora é como ter staging embutido.

### Task Runners (Code node sandboxed)

Code nodes agora executam em processos isolados (Task Runners), habilitados por default. Isso significa:
- Memory leaks ou loops infinitos em Code nodes não derrubam o n8n
- Execução é isolada entre workflows
- **Latência adicional**: cada Code node faz round-trip pro runner e volta. Isso REFORÇA a hierarquia de nodes — Edit Fields e Core nodes rodam in-process, Code node não.

### Secure-by-default

Dois nodes desabilitados por default:
- **ExecuteCommand**: execução de comandos no host
- **LocalFileTrigger**: acesso ao filesystem

Pra reabilitar: `NODES_EXCLUDE="[]"` (opt-in explícito). Além disso, variáveis de ambiente são bloqueadas em Code nodes por default.

### External Secrets (Enterprise)

Integração com vaults externos pra gerenciar secrets centralizadamente:
- 1Password, AWS Secrets Manager, Azure Key Vault, GCP Secrets Manager, HashiCorp Vault
- Secrets recuperados em runtime, não ficam no banco do n8n
- Desde v2.10.0: múltiplos vaults por provider
- Desde v2.13.0: editores de projeto podem usar secrets

## Princípios inegociáveis

1. **Hierarquia de nodes (reforçada pelo n8n 2.0):**
   - **1º Edit Fields (Set) com expressões inline** — Transformar, renomear, calcular, formatar dados. Roda DENTRO do processo principal do n8n, rápido e estável.
   - **2º Core nodes** — Filter, IF, Switch, Split Out, Merge, Summarize, Limit, Sort, Remove Duplicates. Lógica de fluxo e manipulação de coleções. Otimizados e in-process.
   - **3º Code node** — ÚLTIMO recurso. No n8n 2.0+, Code node executa FORA do processo via Task Runner (round-trip adicional). Use apenas quando: a lógica precisaria de 5+ nodes encadeados, transformação é complexa demais pra expressão inline, ou precisa de biblioteca específica. Suporta JavaScript e Python (Python tem overhead de compilação extra).
   - **HTTP Request > nodes nativos de API / community nodes** — Prefira HTTP Request sobre nodes nativos (Kommo node, Slack node) ou community nodes — muitos são mal implementados, desatualizados, ou limitados. HTTP Request dá controle total sobre URL, headers, body e error handling.
2. **JSON Schema pra controlar output de IA.** Toda chamada pra LLM deve ter schema de saída definido. Nunca confie em resposta livre.
3. **Workflow legível > workflow esperto.** Se alguém da equipe não consegue entender o workflow em 5 minutos olhando, tá mal estruturado.
4. **Error handling não é opcional.** Todo workflow de produção precisa tratar erros. Sem exceção.
5. **Log tudo que importa.** Se deu errado e não tem log, é como se nunca tivesse existido.
6. **Draft → teste → Publish.** Nunca publique sem testar. O ciclo Draft/Published existe pra isso — use.

## Módulos

### Módulo 1: Padrões de arquitetura

#### Quando usar subworkflow

Use subworkflow quando:
- O mesmo bloco de lógica aparece em 2+ workflows (ex: "enviar mensagem via Evolution API" aparece em 5 fluxos)
- O workflow principal tá ficando grande demais (mais de 20 nodes)
- Você quer isolar uma parte pra facilitar debug
- A equipe precisa reutilizar algo que você construiu

Não use subworkflow quando:
- É lógica usada uma vez só — complexidade extra sem ganho
- O subworkflow teria 3 nodes ou menos — não justifica

#### Nomenclatura de workflows

```
[CLIENTE] - [TIPO] - [DESCRIÇÃO]
Exemplos:
  Capitalize - SDR - Qualificação WhatsApp
  AW Control - OCR - Pipeline Documentos
  Studio Artemis - Lead - Processamento Meta Ads
  INTERNO - Cron - Keep-alive Supabase
```

Tipos válidos: SDR, Lead, OCR, Cron, Webhook, Integração, Notificação, Relatório, AI

#### Nomenclatura de nodes

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

#### Estrutura padrão de workflow

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

#### Execution Data (checkpoints pra filtrar execuções)

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

#### Error handling (4 camadas)

Todo workflow de produção precisa de error handling. O nível de sofisticação depende da criticidade:

**Camada 1 — Error Workflow Global (todo workflow)**
- Error Trigger node configurado no workflow settings
- Log no Supabase (tabela de logs): workflow_name, node_name, error_message, timestamp, input_data
- Notificação em workflows críticos: WhatsApp/Telegram via ntfy ou Evolution API
- Pega QUALQUER erro que nenhum outro tratamento pegou

**Camada 2 — Error por Node (workflows com APIs externas)**
- No node HTTP Request: configurar "On Error" como "Continue" com output de erro
- Branch com IF após o node: checar se veio erro
- Se erro → tratar (retry, fallback, log específico)
- Se sucesso → segue fluxo normal
- Retry: 3 tentativas, intervalo crescente (1s → 2s → 5s), backoff exponencial
- Depois de 3 falhas: log + notificação + marcar pra reprocessamento

**Camada 3 — Exceção de Negócio (workflows com regras complexas)**
- Use "Stop and Error" node quando uma condição de negócio falha (lead sem telefone, documento inválido)
- Diferente de erro técnico — aqui o workflow funcionou mas os dados não passam na regra
- Stop and Error dispara o Error Workflow Global da Camada 1
- Inclua mensagem de erro clara: "Lead sem telefone: {{ $json.lead_id }}"

**Camada 4 — Circuit Breaker (workflows com APIs instáveis)**
- Pausa temporariamente chamadas de API quando threshold de falhas é excedido
- Implementação: armazene estado (contador de falhas + timestamp) em Data Table ou Redis
- Antes de chamar API frágil: cheque se circuito está aberto
- Se aberto → rota pra fallback ou fila de retry manual
- Configuração típica: 5 falhas consecutivas → cooldown de 30s antes de tentar novamente
- Jitter de ±20% no cooldown pra evitar thundering herd

**Decisão de qual camada usar:**
- Workflow simples (cron interno, notificação) → Camada 1 só
- Workflow com API externa (Kommo, Evolution, Meta) → Camada 1 + 2
- Workflow crítico de negócio (pipeline de vendas, OCR) → Camada 1 + 2 + 3
- Workflow com API instável ou de terceiros (rate-limited, uptime ruim) → Camada 1 + 2 + 3 + 4

**Classificação de erros HTTP pra decisão de retry:**

| Código | Ação | Detalhe |
|--------|------|---------|
| 401/403 | Refresh credential, retry 1x | Token pode ter expirado |
| 404 | Skip ou archive | Recurso não existe |
| 422 | Fail sem retry | Request malformado, corrigir dados |
| 429 | Backoff exponencial | Usar header Retry-After se disponível |
| 5xx | Backoff exponencial, 3x | Problema temporário do servidor |
| ECONNREFUSED | Circuit Breaker | Serviço upstream indisponível |
| Timeout 30s+ | Retry 3x com wait 30s | Rede lenta ou serviço sobrecarregado |

#### Confiabilidade: Webhook direto vs Edge Function + Fila

Quando um sistema externo manda webhook pro n8n, existe risco: se o n8n tá fora do ar, o webhook se perde. Pra workflows críticos, use Edge Function do Supabase como camada de recepção:

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

Leia `references/filas-e-edge-functions.md` para detalhes de implementação.

#### Modularização (DRY/KISS)

**Subworkflows síncronos vs assíncronos:**
- **Síncrono** (Execute Workflow node): O workflow pai ESPERA o sub terminar. Use quando precisa do resultado de volta.
- **Assíncrono** (Execute Workflow Trigger): O workflow pai dispara e segue. Use quando não precisa do resultado.

**Organização em pastas:**
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

**Salvamento seletivo de execuções:**
- Workflows de alto volume (cron a cada 5 min): salvar APENAS execuções com erro
- Workflows críticos: salvar todas
- Subworkflows: geralmente não precisa salvar (o pai já salva)
- Configurar em: Workflow Settings → Save Execution Data

**Implementação em waves (workflows complexos):**

Quando um workflow é grande (10+ integrações, múltiplos branches), não tente construir tudo de uma vez:

- **Wave 1:** Trigger + fluxo principal (caminho feliz) + output básico. Testa se o core funciona.
- **Wave 2:** Branches alternativos + error handling (4 camadas) + Execution Data. Testa se lida com falhas.
- **Wave 3:** Otimização (Redis cache, fila, subworkflows, Circuit Breaker) + documentação (sticky notes, nomes de nodes).

Cada wave deve ser testável sozinha. Se estiver delegando, especifique no briefing qual wave.

#### Redis como infraestrutura (quando escalar)

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

### Módulo 2: AI nodes e agentes

O n8n tem ~70 nodes de IA baseados em LangChain. Antes de implementar lógica de IA "na mão" com HTTP Request, verifique se já existe um AI node que faz o que você precisa.

#### Arquitetura AI Agent

O AI Agent node é o orquestrador central:
```
[Chat Trigger / Webhook] → [AI Agent] → [Output / Respond to Chat]
                              ↓
                     Sub-nodes conectados:
                     - LLM (Claude, GPT, Gemini)
                     - Memory (Window Buffer, Postgres, Redis)
                     - Tools (HTTP Request, calculadora, custom)
```

**Tipos de agente disponíveis:**
- **Tools Agent** — usa tools pra buscar dados, executar ações. O mais comum e versátil.
- **Conversational Agent** — mantém contexto via memory. Ideal pra chatbots.
- **Plan and Execute Agent** — quebra tarefas complexas em steps. Pra workflows de múltiplos passos.

#### Respond to Chat node

Pra workflows conversacionais que precisam de interação humana (Human-in-the-Loop):
- Usado com Chat Trigger pra fluxos de aprovação/esclarecimento
- Permite esperar resposta do usuário ou continuar imediatamente
- Response Mode no Chat Trigger deve ser "Using Response Nodes"
- Limitação: não funciona em subworkflows de agentes

#### Supabase Vector Store node

5 modos de operação:
1. **Get Many** — busca por similaridade usando embedding do prompt
2. **Insert Documents** — insere documentos com embeddings
3. **Retrieve Documents (Chain/Tool)** — retorna como fonte pra Chain
4. **Retrieve Documents (Agent Tool)** — retorna como tool pra Agent
5. **Update Documents** — atualiza documentos existentes

Tabela padrão: `documents`. Atenção: há issue conhecida onde o node ignora campo Table Name customizado.

#### Data Tables do n8n (banco embutido)

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

### Módulo 3: MCP (Model Context Protocol)

O n8n suporta MCP em 3 dimensões:

#### MCP Client Tool (n8n como consumidor)

Permite que AI Agents do n8n chamem tools de MCP servers externos:
- Conecta a qualquer servidor MCP-compliant
- Agent descobre e executa tools automaticamente
- Use quando: seu agente precisa acessar ferramentas de sistemas que expõem MCP (Supabase MCP Server, ferramentas customizadas)

#### MCP Server Trigger (n8n como provedor)

Transforma workflows do n8n em tools MCP consumíveis por AI coding tools:
- Expõe URL pra clientes MCP se conectarem
- Suporta SSE e Streamable HTTP
- Use quando: quer que Lovable, Cursor, ou Claude Code chamem workflows do n8n

#### Instance-level MCP (Beta)

Configuração centralizada em Settings > Instance-level MCP:
- Uma conexão por instância servindo todos os workflows habilitados
- Autenticação via OAuth redirect ou Personal MCP Access Token
- Habilitar MCP no nível da instância, depois por workflow individual
- Connectors nativos disponíveis: Lovable, Mistral AI (mais vindo)

**Atenção:** não tem scoping por client — todos os clientes MCP conectados veem todos os workflows habilitados. Controle qual workflow habilitar.

### Módulo 4: Queue mode e escalabilidade

#### Benchmarks de performance

| Setup | RPS | Latência | Nota |
|-------|-----|----------|------|
| Single instance (baseline) | 23 | - | Baseline |
| Queue mode habilitado | 72 | <3s | 3x melhoria |
| Queue mode + hardware maior (16 vCPUs, 32GB) | 162 | <1.2s | 7x melhoria |

#### Arquitetura de scaling

```
[Main Instance] → [Redis Queue] → [Worker 1]
                                → [Worker 2]
                                → [Worker N]
        ↓
[Webhook Processor] (opcional, pra alto volume de requests)
```

- Main instance recebe triggers/webhooks e coloca na fila Redis
- Workers puxam execuções da fila e processam
- Webhook Processors adicionam paralelismo no recebimento

**Considerações:**
- Queue mode dobra uso de RAM mesmo idle — só é custo-efetivo em 100+ RPS
- Workers são processos Node.js separados com alto IOPS
- Escale horizontalmente adicionando workers

### Módulo 5: Templates de fluxos comuns

Quando o usuário pedir ajuda pra montar um workflow, identifique qual template se aplica. Leia `references/templates.md` para os templates detalhados.

**Templates disponíveis:**
1. Webhook → Processar → Supabase (CRUD genérico)
2. Webhook Kommo → Processar Lead → Ação
3. Meta Lead Ads → Processar → CRM + Notificação
4. Cron → Processar fila → Ação por item
5. WhatsApp Inbound (Evolution API) → Processar → Responder
6. OCR Pipeline (Documento → Gemini → Extração → Supabase)
7. Follow-up Campaign (Fila → Verificar janela horária → Enviar)
8. AI Chatbot (Chat Trigger → Agent → Memory → Respond to Chat) ← NOVO

### Módulo 6: Delegação de workflows

Quando o usuário quiser delegar um workflow pra Hygor ou Jonas, gere um **briefing técnico** que a pessoa consiga seguir.

**Template de briefing técnico:**

```markdown
# Briefing: [Nome do Workflow]

## O que esse workflow faz
[2-3 frases explicando o resultado final, não a implementação]

## Trigger
- Tipo: [webhook / cron / chat trigger / evento]
- Quando dispara: [descrição humana]

## Fluxo (passo a passo)
1. [Recebe X] → Node: [tipo de node]
2. [Valida Y] → Node: [tipo de node]
3. [Processa Z] → Node: [tipo de node]
...

## Configurações importantes
- [Node X]: usar HTTP Request, não Code node
- [Node Y]: endpoint = [URL], método = [GET/POST], headers = [quais]
- [Autenticação]: usar credential [nome] que já existe no n8n

## Variáveis / Secrets
- [VAR_1]: onde encontrar, o que é
- [VAR_2]: onde encontrar, o que é

## Error handling obrigatório
- Se [X] falhar: [o que fazer]
- Log em: [tabela/local]

## Critérios de aceitação
- [ ] Workflow funciona como Draft (teste manual)
- [ ] Workflow publicado e funcionando em produção
- [ ] Erros são logados em [tabela]
- [ ] Nodes estão renomeados com padrão [Ação] [Alvo]
- [ ] Sticky notes explicando branches complexos

## Dúvidas?
Pergunte ANTES de começar. Melhor perguntar do que refazer.
```

**Calibração por pessoa:**
- **Jonas (estagiário):** Screenshots do n8n mostrando onde clicar. Especifique CADA campo do HTTP Request. Não assuma que ele sabe o que é bearer token.
- **Hygor (junior):** Descreva o resultado e restrições. Ele sabe montar HTTP Request. Foque nas regras de negócio e edge cases.

### Módulo 7: Debug e troubleshooting

Quando o usuário disser "meu workflow não funciona", siga este processo:

**Passo 1: Localizar o problema**
- Qual node tá com erro? (vermelho no n8n)
- Qual a mensagem de erro? (exata, não resumida)
- O workflow funcionava antes e parou, ou nunca funcionou?
- Tá testando via Draft ou tá publicado?

**Passo 2: Classificar o tipo de erro**

| Tipo | Sintoma | Causa comum | Solução |
|---|---|---|---|
| HTTP 401/403 | Unauthorized/Forbidden | Token expirado ou credential errada | Verificar credential, refresh token |
| HTTP 400 | Bad Request | Body mal formatado ou campo faltando | Comparar body enviado com docs da API |
| HTTP 404 | Not Found | URL errada ou recurso não existe | Verificar URL, IDs dinâmicos |
| HTTP 429 | Rate Limited | Muitas requisições | Delay entre requests, retry com backoff |
| HTTP 500 | Server Error | Problema no servidor externo | Retry, verificar se API tá online |
| Dados errados | Workflow roda mas resultado tá errado | Expressão n8n mal formatada | Verificar {{ $json }} no node anterior |
| Não dispara | Webhook não recebe nada | URL errada ou workflow inativo/não publicado | Verificar URL, status Draft vs Published |
| Timeout | Workflow trava | Processamento longo ou API lenta | Aumentar timeout, quebrar em partes |
| Code node crash | n8n não cai mais (2.0) | Erro no Code node isolado pelo Task Runner | Checar logs do runner, ajustar código |

**Passo 3: Investigar**
- Peça o output do node anterior ao que falha
- Peça o body/headers que o HTTP Request tá enviando
- Se possível, peça screenshot do node configurado

**Passo 4: Resolver**
- Dê a solução específica (não "verifique suas configurações")
- Se for problema de expressão n8n, escreva a expressão correta
- Se for problema de API, aponte exatamente o que mudar

### Módulo 8: Documentação de workflows

Quando o usuário pedir pra documentar um workflow, gere neste formato:

```markdown
# [Nome do Workflow]

## Resumo
[O que faz, quando dispara, qual o resultado]

## Diagrama de fluxo
[Trigger] → [Node 1] → [Node 2] → ... → [Output]
                           ↓ (erro)
                      [Error Handler] → [Log]

## Nodes detalhados

### 1. [Nome do Node]
- **Tipo:** [HTTP Request / Code / IF / AI Agent / etc]
- **O que faz:** [descrição]
- **Input:** [o que recebe do node anterior]
- **Output:** [o que passa pro próximo]
- **Config:** [campos importantes]

## Dependências
- Credentials: [lista]
- Tabelas Supabase: [lista]
- APIs externas: [lista com URLs base]
- MCP servers: [lista, se aplicável]

## Manutenção
- Crons: [se tem, qual frequência]
- Tokens que expiram: [quais, quando renovar]
- Limites de API: [rate limits relevantes]
- Status: Draft / Published
```

### Módulo 9: Segurança

#### Checklist de segurança pra workflows de produção

1. **Credentials:** nunca hardcode tokens/senhas nos nodes. Use Credentials do n8n ou External Secrets.
2. **Webhook auth:** webhooks públicos devem validar origem (header signature, token no query param, IP whitelist).
3. **Code nodes:** não acessam variáveis de ambiente por default no 2.0. Se precisar, configure explicitamente.
4. **service_role key:** se o workflow usa service_role do Supabase, NUNCA exponha em webhook responses ou logs.
5. **Execution Data:** não salve dados sensíveis — fica visível pra todos os usuários do n8n.
6. **Data Tables:** dados são acessíveis por qualquer workflow no projeto — não armazene secrets.
7. **MCP:** todos os clientes MCP conectados veem todos os workflows habilitados — controle quais workflows habilitar.

#### Python em Code nodes

n8n 2.0 suporta Python nativo nos Code nodes:
- Cloud: sem imports de bibliotecas (apenas built-ins)
- Self-hosted: imports via imagem customizada do runner
- Python tem overhead de compilação maior que JavaScript
- Variáveis: `_items` (all-items mode), `_item` (per-item mode)
- Use quando a lógica é significativamente mais simples em Python que JS

## Integração com outras skills

- **Product Discovery & PRD:** Se o PRD inclui automações, esta skill define como implementar
- **Tech Lead & PM:** Quando delegar workflows, use o Módulo 6 junto com o template de task da skill de Tech Lead
- **Supabase Architect:** Workflows que fazem CRUD no Supabase devem respeitar o schema definido pela skill de banco
- **Prompt Engineer:** Pra configurar AI Agent nodes, system prompts, e JSON Schema de output de LLMs

## Quando NÃO usar esta skill

- Se o pedido é sobre Lovable/frontend puro → não envolve n8n
- Se o pedido é sobre SQL/schema no Supabase sem automação → use skill de Supabase
- Se o pedido é sobre gestão/delegação genérica → use skill de Tech Lead
- Se o usuário quer montar um workflow MAS deveria estar delegando → questione primeiro (filtro de alavancagem), depois ajude se fizer sentido

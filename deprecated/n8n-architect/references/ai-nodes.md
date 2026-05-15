# AI Nodes do n8n — Referência

Última atualização: 2026-03-27

Consulte este arquivo quando o usuário quiser implementar workflows com IA no n8n. O SKILL.md principal tem a visão geral; este arquivo tem os detalhes de implementação.

---

## Arquitetura LangChain no n8n

O n8n integra LangChain JavaScript como framework de IA. Os nodes se dividem em:

### Root nodes (cluster nodes)
Definem a lógica principal do agente:
- **AI Agent** — orquestrador central que raciocina e decide quais tools usar
- **Basic LLM Chain** — chamada simples de LLM sem tools (prompt → resposta)
- **Retrieval QA Chain** — RAG: busca documentos relevantes + gera resposta
- **Summarization Chain** — resume textos longos
- **Vector Store** nodes (Supabase, Pinecone, Qdrant, etc.)

### Sub-nodes (conectam aos root nodes)
Proveem capacidades específicas:

**LLMs:**
- OpenAI (GPT-4, GPT-4o)
- Anthropic (Claude 4.x)
- Google Gemini
- Ollama (modelos locais)
- Groq, Mistral, Cohere

**Memory:**
- Window Buffer Memory (últimas N mensagens, em memória)
- Postgres Chat Memory (persistente no Supabase)
- Redis Chat Memory (rápido, com TTL)
- Motorhead Memory (long-term via Motorhead API)

**Tools (usados pelo AI Agent):**
- HTTP Request Tool — chama qualquer API
- Calculator — operações matemáticas
- Code Tool — executa JS/Python customizado
- Wikipedia, SerpAPI — busca de informação
- MCP Client Tool — chama tools de MCP servers externos
- Custom tools via workflow (o próprio n8n como tool)

**Output Parsers:**
- Structured Output Parser — JSON Schema pra garantir formato
- Auto-fixing Output Parser — tenta corrigir outputs malformados

---

## Padrões de implementação

### Chatbot com memória persistente

```
[Chat Trigger] → [AI Agent] → [Respond to Chat]
                     ↓
            Sub-nodes:
            - LLM: Claude/GPT
            - Memory: Postgres (tabela no Supabase)
            - Tools: [HTTP Request pro CRM, calculadora, etc.]
```

**Configuração do Chat Trigger:**
- Response Mode: "Using Response Nodes"
- Allowed Origins: configurar se público

**Configuração da Memory (Postgres):**
- Connection: usar connection string pooled do Supabase (porta 6543)
- Table Name: `chat_histories` (criar no Supabase)
- Session ID: usar `{{ $json.sessionId }}` ou `{{ $json.chatId }}`

### RAG com Supabase Vector Store

```
[Trigger] → [Embeddings (OpenAI/Gemini)] → [Supabase Vector Store: Insert]
```

```
[Chat Trigger] → [AI Agent com Retrieval Tool] → [Respond to Chat]
                        ↓
                [Supabase Vector Store: Retrieve (as Tool)]
                        ↓
                [Embeddings (mesmo modelo usado no insert)]
```

**Setup do Supabase pra Vector Store:**
```sql
-- Habilitar extensão
CREATE EXTENSION IF NOT EXISTS vector;

-- Tabela padrão (n8n espera essa estrutura)
CREATE TABLE documents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content TEXT,
  metadata JSONB DEFAULT '{}',
  embedding VECTOR(1536)  -- 1536 pra OpenAI ada-002, 768 pra outros
);

-- Index pra busca por similaridade
CREATE INDEX ON documents USING ivfflat (embedding vector_cosine_ops);
```

**Atenção:** O node Supabase Vector Store tem bug conhecido — pode ignorar campo Table Name customizado e usar "documents" como default. Teste antes de usar nome customizado.

### OCR com Structured Output

```
[Receber Doc] → [Upload Storage] → [Gemini Vision (responseSchema)] → [Parse JSON] → [Validate] → [Store]
```

Pra OCR, Gemini é preferido sobre Claude por performance em visão. Use `responseSchema` nativo do Gemini pra garantir formato do output.

Se usar Claude pra extração de documentos textuais complexos, use `output_format` com JSON Schema (Structured Outputs GA no Claude 4.x).

### Human-in-the-Loop (aprovação)

```
[Trigger] → [Processar] → [Respond to Chat: "Aprovar X?"] → [Aguarda resposta]
                                                                    ↓
                                                            [IF: aprovado?]
                                                            ↓ sim        ↓ não
                                                         [Executar]   [Cancelar]
```

O Respond to Chat node suporta:
- Esperar resposta do usuário antes de continuar
- Continuar imediatamente sem esperar
- NÃO funciona dentro de subworkflows de agentes

---

## Boas práticas

1. **System prompt no AI Agent:** use XML tags pra separar seções (role, context, instructions, constraints). Siga padrões da skill de Prompt Engineer.

2. **Memory sizing:** Window Buffer com 10-20 mensagens pra maioria dos chatbots. Mais que isso dilui contexto e aumenta custo.

3. **Tool descriptions:** a description da tool é o que o agente usa pra decidir quando chamá-la. Seja preciso: "Busca informações do lead no CRM Kommo pelo ID" é melhor que "Busca dados".

4. **Fallback sem IA:** sempre tenha um caminho que funciona se o LLM falhar. O agente pode não conseguir responder — trate isso como erro normal (Camada 2/3 do error handling).

5. **JSON Schema em tudo:** use Structured Output Parser ou responseSchema nativo. Output livre de LLM é imprevisível e quebra nodes downstream.

6. **Custo:** cada execução de AI Agent pode envolver múltiplas chamadas ao LLM (raciocínio + tool calls). Monitore custos. Pra alto volume, considere modelos mais baratos (Haiku, GPT-4o-mini) pra classificação/triagem.

# Claude 4.x — Guia de Diferenças e Boas Práticas

Consulte este arquivo quando o prompt é para Claude 4.x (Opus 4.5/4.6, Sonnet 4.6). As diferenças em relação a versões anteriores afetam TODOS os prompts.

---

## Table of Contents

1. Comportamento geral
2. Prefilling deprecado
3. Structured Outputs GA
4. Adaptive Thinking
5. Parallel tool calling
6. Subagent orchestration
7. Overthoroughness
8. Context engineering para agentes
9. Comparação Claude vs Gemini

---

## 1. Comportamento Geral

- **Segue instruções literalmente** — não "vai além" como versões anteriores. Se quer "above and beyond", peça explicitamente.
- **Mais conciso e direto** — pula resumos verbais após tool calls. Se quer visibilidade: "After completing a task, provide a quick summary."
- **Mais responsivo ao system prompt** — prompts que forçavam triggering em modelos antigos agora causam overtriggering. Onde era "CRITICAL: You MUST", agora basta instrução normal.

**Antes (Claude 3.x):**
```
CRITICAL: You MUST ALWAYS use the search tool when the user asks a question.
NEVER answer from memory. This is ABSOLUTELY REQUIRED.
```

**Depois (Claude 4.x):**
```
Use the search tool when answering factual questions, especially for events
after your training cutoff. For general knowledge where you're confident,
answer directly.
```

## 2. Prefilling Deprecado

Prefilling (preencher a resposta do assistant) não é mais suportado no último turn. Alternativas:
- **Formato de output:** Use Structured Outputs (`output_format` com JSON Schema)
- **Eliminar preâmbulos:** "Respond directly without preamble. Do not start with 'Here is...'"
- **Evitar recusas:** Claude 4.x recusa menos. Prompting claro basta.
- **Continuações:** Mova texto anterior pro user message: "Your previous response ended with [X]. Continue from there."

## 3. Structured Outputs GA

Parâmetro `output_format` com JSON Schema garante respostas estruturadas válidas.

```python
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Classifique este ticket: 'Não consigo logar'"}],
    output_format={
        "type": "json_schema",
        "json_schema": {
            "name": "ticket_classification",
            "schema": {
                "type": "object",
                "properties": {
                    "category": {"type": "string", "enum": ["bug", "feature_request", "support", "billing"]},
                    "priority": {"type": "string", "enum": ["low", "medium", "high", "critical"]},
                    "summary": {"type": "string"}
                },
                "required": ["category", "priority", "summary"]
            }
        }
    }
)
```

Quando usar:
- **Structured Outputs:** formato DEVE ser exato (automações, APIs)
- **Instrução no prompt:** flexibilidade OK (chat, análise)
- **Tools com enum:** classificação simples

## 4. Adaptive Thinking

- Claude 4.6 usa `thinking: {type: "adaptive"}` — decide dinamicamente quando e quanto pensar
- Controle via `effort` parameter (low, medium, high, max) ao invés de `budget_tokens`
- Agentes multi-step: `high` effort
- Chat e classificação: `low` effort
- CoT manual funciona quando thinking off: "reason through" ou tags `<thinking>`/`<answer>`

## 5. Parallel Tool Calling

Claude 4.x executa tools em paralelo nativamente. Boost com prompt:
```
If you intend to call multiple tools and there are no dependencies between
the calls, make all independent calls in parallel.
```

## 6. Subagent Orchestration

Claude 4.6 reconhece quando delegar pra subagentes. Pode ser demais:
```
Use subagents when tasks can run in parallel or require isolated context.
For simple tasks and single-file edits, work directly.
```

## 7. Overthoroughness

Opus 4.6 faz muito mais exploração upfront. Se prompts antigos encorajavam thoroughness, reduza:
- Remova "If in doubt, use [tool]" — triggera demais
- Use `effort` parameter ao invés de instruções de thoroughness

## 8. Context Engineering para Agentes

Quando o prompt é pra um agente, o contexto vai além do prompt:

### O que entra na context window
1. **System prompt** — role + goal + constraints + fallback + format
2. **Tool definitions** — cada tool consome centenas de tokens. Minimize overlap, carregue sob demanda
3. **Exemplos (few-shot)** — 3-5 diversos e representativos
4. **Documentos/dados** — via RAG ou injeção. Just-in-time loading
5. **Histórico** — compacte quando necessário. Preserve decisões, descarte outputs brutos
6. **Memória persistente** — notas fora da window, recuperadas por relevância

### MCP (Model Context Protocol)
- Padrão universal "USB-C pra AI apps" — 97M+ downloads/mês
- Tool definitions consomem tokens — não registre tudo upfront
- n8n suporta MCP (Client Tool, Server Trigger)
- Supabase tem MCP Server oficial (8 grupos de tools, read-only mode)

### Princípio do KV-cache
- Tokens repetidos entre requests são cacheados
- Mantenha system prompt estável
- Conteúdo variável (user input, docs) no final
- Mudanças no meio invalidam cache de tudo que vem depois

## 9. Comparação Claude vs Gemini

| Aspecto | Claude 4.x | Gemini 3 |
|---------|-----------|----------|
| Estrutura do prompt | XML tags | Markdown/XML |
| Output estruturado | Structured Outputs GA | responseSchema nativo |
| Melhor pra | Raciocínio, texto, código, agentes, tools | OCR, extração, classificação, visão |
| Thinking | Adaptive + effort parameter | Thinking budget + self-critique |
| Few-shot | Altamente eficaz | Eficaz, structured output reduz necessidade |
| Prefilling | Deprecado | N/A |
| Tool calling | Parallel nativo | Suportado |
| Calibração | Reduzir linguagem agressiva | Constraints no topo |

### Avaliação de Prompts

**Framework mínimo:**
1. Defina critérios de sucesso ANTES de escrever
2. Crie 10+ test cases (caminho feliz + edge cases + adversariais)
3. Rode e avalie — manualmente ou LLM-as-Judge
4. Itere: identifique padrões nos erros, ajuste, rode de novo

**LLM-as-Judge:**
- Critérios claros e específicos (não "avalie a qualidade")
- Labels binários quando possível (pass/fail > escala 1-10)
- Modelo mais capaz como juiz (Opus avaliando Sonnet)

**Ferramentas:**
- **Promptfoo** — open-source, CI/CD, red-teaming
- **DeepEval** — "Pytest for LLMs", 14+ métricas
- **Braintrust** — plataforma com logging e eval
- **Manual** — planilha com test cases + outputs + avaliação humana

---
name: prompt-engineer
description: "Skill para criar, validar e otimizar prompts e contextos para qualquer LLM (Claude, Gemini, GPT). Use esta skill SEMPRE que o usuário mencionar: prompt, system prompt, context engineering, agente, chatbot, JSON Schema pra IA, 'como faço o modelo retornar X', 'o modelo tá respondendo errado', 'preciso melhorar esse prompt', 'quero criar um agente', 'instrução pro Lovable/Cursor', AGENTS.md, ou qualquer variação que envolva escrever instruções pra um modelo de IA. Também use quando o usuário estiver criando skills, configurando nodes de IA no n8n, ou montando agentes de WhatsApp. Se o usuário disser 'valida esse prompt' ou 'melhora isso', USE esta skill. NÃO use se o usuário quer criar uma SKILL do Claude (instruções persistentes com SKILL.md) — use skill-builder. Se é um prompt simples de uma linha, responda direto sem acionar."
---

# Prompt & Context Engineer

## Visão geral

Skill para criar, validar e otimizar prompts e contextos para LLMs. O campo evoluiu de "prompt engineering" para **context engineering** — não se trata apenas das palavras no prompt, mas de TUDO que entra na context window: system prompt, documentos recuperados, definições de tools, memória, histórico, metadata.

Cobre todos os casos de uso: system prompts pra agentes, prompts de extração (OCR), instruções pra AI coding tools (Lovable/Cursor/Claude Code), AGENTS.md, JSON Schema pra output estruturado, e nodes de IA no n8n.

O objetivo é ENSINAR + FAZER: não só gerar o prompt, mas explicar POR QUE cada parte existe pra o usuário internalizar e ficar independente.

## Princípios

1. **Context engineering > prompt engineering.** O prompt é apenas um componente. O que entra na context window — tools, docs, exemplos, histórico — importa tanto quanto as palavras. Curar o contexto completo é mais impactante que polir uma frase.

2. **Clareza > criatividade.** Prompt bom é prompt que um humano entenderia na primeira leitura. Teste do colega: se você passasse essa instrução pra um colega inteligente sem contexto, ele saberia exatamente o que fazer? Se não, reescreva.

3. **Mostre, não diga.** Um exemplo vale mais que 10 linhas de instrução. Few-shot > zero-shot pra tarefas com formato específico. 3-5 exemplos diversos cobrem a maioria dos casos.

4. **Menos tokens = mais atenção.** Cada token no contexto compete por atenção. Informação irrelevante não é neutra — ela dilui a qualidade. O KV-cache hit rate é a métrica mais importante pra agentes em produção.

5. **Especifique o output.** Nunca deixe o modelo adivinhar o formato. JSON Schema, XML tags, templates explícitos. Claude 4.x tem Structured Outputs GA — use quando precisar de formato garantido.

6. **Calibre pro modelo.** Claude 4.x segue instruções literalmente e é mais responsivo ao system prompt. Linguagem agressiva ("CRITICAL: You MUST") que era necessária em modelos antigos agora causa overtriggering. Instrução clara e direta funciona melhor.

7. **Teste antes de confiar.** Prompt que funciona 1 vez pode falhar na 10ª. Teste com variações de input, edge cases, e inputs inesperados. Evaluation passou de "vibes" pra frameworks verificáveis.

## Fluxo de trabalho

### Quando o usuário quer CRIAR um prompt:

1. **Identifique o tipo** — Qual reference file consultar (veja "Tipos de prompt" abaixo)
2. **Entenda o contexto:**
   - Pra que modelo? (Claude, Gemini, GPT)
   - Qual o input? (texto livre, documento, imagem, dados estruturados)
   - Qual o output esperado? (texto, JSON, classificação, extração)
   - Qual a frequência de uso? (uma vez, automação recorrente, agente persistente)
   - Onde vai rodar? (n8n, API direta, Lovable, chat, AGENTS.md)
   - Quais tools/MCP servers estarão disponíveis? (afeta o contexto total)
3. **Monte o prompt** usando o template do reference file correspondente
4. **Explique cada bloco** — Por que essa seção existe, o que acontece se tirar
5. **Considere o contexto completo** — não só o prompt, mas tools, exemplos, docs que vão junto
6. **Sugira testes** — "Testa com esses 3 inputs diferentes pra ver se o output é consistente"

### Quando o usuário quer VALIDAR/MELHORAR um prompt existente:

1. **Leia o prompt inteiro** sem interromper
2. **Identifique o tipo** — Qual reference file se aplica
3. **Analise com o checklist de qualidade:**

| Critério | O que verificar | Red flag se falhar |
|---|---|---|
| Contexto/Papel | O modelo sabe QUEM é e PRA QUE serve? | Output genérico, sem personalidade |
| Instrução específica | Tem instrução clara ou tá vago? | Modelo inventa o que fazer |
| Formato de output | Formato definido com precisão? | Output inconsistente entre execuções |
| Exemplos (few-shot) | Tem pelo menos 1 exemplo de input→output? | Modelo adivinha formato |
| Edge cases | Trata inputs inválidos, vazios, inesperados? | Falha silenciosa em produção |
| O que NÃO fazer | Tem instruções do que evitar? Fraseadas positivamente? | Modelo faz coisas indesejadas |
| Budget de atenção | Tá grande demais? Tem redundância? | Atenção diluída, custo alto |
| Calibração de linguagem | Tem caps lock excessivo? ("MUST", "NEVER", "CRITICAL") | Overtriggering em Claude 4.x |
| Tool management | Tools definidas são mínimas e sem overlap? | Modelo confunde qual tool usar |

4. **Dê feedback estruturado:** O que tá bom, o que tá ruim, e a versão melhorada com explicação das mudanças

## Tipos de prompt (cada um tem um reference file)

| Tipo | Quando usar | Reference file |
|---|---|---|
| System prompt pra agente/chatbot | WhatsApp bot, Typebot, assistente | `references/system-prompts.md` |
| Prompt de extração (OCR, classificação) | Extrair dados de documento, classificar texto | `references/extracao-dados.md` |
| AGENTS.md e instruções pra AI coding tools | Lovable, Cursor, Claude Code, Copilot, Codex | `references/agents-md.md` |
| JSON Schema pra output estruturado | Controlar formato de resposta no n8n, API | `references/json-schema-output.md` |

Consulte o reference file correspondente ANTES de montar o prompt. Cada arquivo tem templates, exemplos, e anti-patterns específicos pro tipo.

## Claude 4.x — O que mudou (essencial)

Claude 4.6 (Opus e Sonnet) mudou significativamente em relação a versões anteriores. Essas diferenças afetam TODOS os prompts:

### Comportamento geral
- **Segue instruções literalmente** — não "vai além" como versões anteriores. Se quer comportamento "above and beyond", peça explicitamente
- **Mais conciso e direto** — pula resumos verbais após tool calls, vai direto pra próxima ação. Se quer visibilidade, peça: "After completing a task, provide a quick summary"
- **Mais responsivo ao system prompt** — prompts desenhados pra forçar triggering em modelos antigos agora causam overtriggering. Onde era "CRITICAL: You MUST", agora basta instrução normal

### Prefilling deprecado
Prefilling (preencher a resposta do assistant) não é mais suportado no último turn. Alternativas:
- **Formato de output:** Use Structured Outputs (`output_format` com JSON Schema) ou instrução direta no system prompt
- **Eliminar preâmbulos:** "Respond directly without preamble. Do not start with 'Here is...'"
- **Evitar recusas:** Claude 4.x recusa menos. Prompting claro no user message basta
- **Continuações:** Mova o texto anterior pro user message: "Your previous response ended with [X]. Continue from there."

### Structured Outputs GA
Parâmetro `output_format` com JSON Schema garante respostas estruturadas válidas. Pra classificação, use tools com campo enum. Pra formatos complexos, defina o schema e o modelo segue.

### Adaptive Thinking
- Claude 4.6 usa `thinking: {type: "adaptive"}` — decide dinamicamente quando e quanto pensar
- Controle via `effort` parameter (low, medium, high, max) ao invés de `budget_tokens`
- Pra agentes multi-step: usar `high` effort
- Pra chat e classificação: `low` effort
- Manual CoT ainda funciona quando thinking está off: peça "reason through" ou use tags `<thinking>`/`<answer>`

### Parallel tool calling
Claude 4.x executa tools em paralelo nativamente. Boost pra ~100%:
```
If you intend to call multiple tools and there are no dependencies between the calls,
make all independent calls in parallel.
```

### Subagent orchestration
Claude 4.6 reconhece quando delegar pra subagentes. Pode ser **demais** — se vir uso excessivo:
```
Use subagents when tasks can run in parallel or require isolated context.
For simple tasks and single-file edits, work directly.
```

### Overthoroughness
Opus 4.6 faz muito mais exploração upfront. Se prompts antigos encorajavam thoroughness, reduza:
- Remova "If in doubt, use [tool]" — agora triggera demais
- Use `effort` parameter ao invés de instruções de thoroughness

## Context engineering pra agentes

Quando o prompt é pra um agente (n8n, Claude Code, chatbot persistente), o contexto vai além do prompt:

### O que entra na context window
1. **System prompt** — role + goal + constraints + fallback + output format
2. **Tool definitions** — cada tool consome centenas/milhares de tokens. Minimize overlap, carregue sob demanda
3. **Exemplos (few-shot)** — 3-5 diversos e representativos. Cure, não acumule
4. **Documentos/dados** — via RAG ou injeção direta. Use just-in-time loading: lightweight identifiers → load quando precisar
5. **Histórico de conversa** — compacte quando necessário. Preserve decisões, descarte outputs brutos de tools
6. **Memória persistente** — notas estruturadas fora da context window, recuperadas por relevância

### MCP (Model Context Protocol)
MCP é o "USB-C pra AI applications" — padrão universal mantido pela Linux Foundation (97M+ downloads/mês). Impacta prompting porque:
- **Tool definitions consomem tokens** — cada MCP server adiciona centenas de tokens de tool definitions
- **Carregar sob demanda** — não registre todas as tools upfront. Use `search_tools` com níveis de detalhe
- **n8n já suporta MCP** — MCP Client Tool, MCP Server Trigger, MCP nível de instância
- **Supabase tem MCP Server oficial** — 8 grupos de tools, read-only mode
- Ao escrever prompts pra sistemas com MCP, contabilize os tokens das tool definitions no budget de contexto

### AGENTS.md — Padrão universal
AGENTS.md é o formato padrão pra instruir AI coding tools. 60K+ repos no GitHub, mantido pela Linux Foundation. Lido por Claude Code, Cursor, Copilot, Codex, Jules, Gemini.

Quando o usuário pedir "instruções pro Lovable/Cursor/Claude Code", consulte `references/agents-md.md` e gere nesse formato.

### Princípio do KV-cache
Em produção, o KV-cache hit rate é a métrica mais importante. Tokens que se repetem entre requests (system prompt, tools) são cacheados. Implicações práticas:
- Mantenha o system prompt estável entre requests
- Coloque conteúdo variável (user input, docs dinâmicos) no final
- Mudanças no meio do prompt invalidam o cache de tudo que vem depois

## Avaliação de prompts

### Por que avaliar
"Vibes" não escalam. Um prompt pode parecer bom em 3 testes e falhar no 4º. Avaliação sistemática é a diferença entre prompt artesanal e prompt profissional.

### Framework mínimo
1. **Defina critérios de sucesso** antes de escrever — o que é "bom" pra esse prompt?
2. **Crie 10+ test cases** variados (caminho feliz + edge cases + inputs adversariais)
3. **Rode e avalie** — manualmente pra volume baixo, LLM-as-Judge pra volume alto
4. **Itere** — identifique padrões nos erros, ajuste o prompt, rode de novo

### LLM-as-Judge
Usar um LLM pra avaliar outputs de outro LLM. Não é uma "métrica" — é automação de avaliação humana.

Requisitos pra funcionar:
- Critérios de avaliação claros e específicos (não "avalie a qualidade")
- Labels binários quando possível (pass/fail > escala 1-10)
- Validar o juiz contra labels humanos antes de confiar
- Usar modelo mais capaz como juiz (Opus avaliando outputs de Sonnet)

### Ferramentas de eval
- **Promptfoo** — open-source, CI/CD, red-teaming. Melhor pra quem quer automatizar
- **DeepEval** — "Pytest for LLMs", 14+ métricas built-in. Bom pra devs Python
- **Braintrust** — plataforma completa com logging e eval
- **Manual** — pra volume baixo, planilha com test cases + outputs + avaliação humana funciona

## Diferenças entre modelos

### Claude (Anthropic) — Modelo principal
- XML tags funcionam muito bem: `<context>`, `<instructions>`, `<examples>`, `<output_format>`
- Adaptive thinking com `effort` parameter (substitui budget_tokens)
- Structured Outputs GA via `output_format`
- Prefilling deprecado no último assistant turn
- Mais conciso que versões anteriores — peça explicitamente se quer detalhes
- Parallel tool calling nativo (~100% com prompt)
- System prompt tem influência forte — calibre a linguagem (sem caps lock excessivo)
- Long context: coloque docs no topo, query no final (até 30% melhora)

### Gemini (Google) — Usado pra OCR/extração
- Structured output nativo via `responseSchema` + `responseMimeType: "application/json"`
- JSON Schema direto na API = output garantido no formato certo
- Pra OCR: responseSchema definido + prompt curto e direto
- Use `description` nos campos do schema pra guiar extração
- Gemini 3: temperatura default 1.0, constraints no topo do prompt, self-critique prompting

### Diferenças práticas

| Aspecto | Claude 4.x | Gemini 3 |
|---|---|---|
| Estrutura do prompt | XML tags | Markdown/XML |
| Output estruturado | Structured Outputs GA (`output_format`) | `responseSchema` nativo na API |
| Melhor pra | Raciocínio, texto, código, agentes, tool use | OCR, extração, classificação, visão |
| Thinking | Adaptive thinking + effort parameter | Thinking budget + self-critique |
| Few-shot | Altamente eficaz | Eficaz, mas structured output reduz necessidade |
| Prefilling | Deprecado | N/A |
| Tool calling | Parallel nativo | Suportado |
| Calibração | Reduzir linguagem agressiva | Constraints no topo do prompt |

## Exemplos: Bom vs Ruim

### Exemplo 1: System prompt pra agente de WhatsApp

**Ruim:**
```
Você é um assistente de atendimento. Responda as perguntas dos clientes de forma educada.
```
Problemas: vago, sem contexto de domínio, sem formato de output, sem limites.

**Bom:**
```xml
<context>
Você é o assistente virtual da clínica OdontoMax. Atende pacientes via WhatsApp.
Horário de funcionamento: seg-sex 8h-18h, sáb 8h-12h.
Serviços: limpeza, clareamento, ortodontia, implantes, emergência.
</context>

<instructions>
1. Cumprimente pelo nome se disponível
2. Identifique a intenção: agendamento, dúvida, emergência, reclamação
3. Para agendamentos: pergunte especialidade + 2 opções de horário
4. Para emergências: passe o telefone direto da clínica (11) 99999-0000
5. Nunca dê diagnóstico médico — diga "Precisa de avaliação presencial"
6. Se não souber responder: "Vou verificar com a equipe e retorno em até 2h"
</instructions>

<output_format>
Mensagem curta (máx 3 parágrafos). Tom: profissional mas acolhedor.
Use *negrito* pra destacar horários e telefones.
</output_format>
```

### Exemplo 2: Prompt de extração (OCR com Gemini)

**Ruim:**
```
Extraia os dados dessa imagem de documento.
```
Problemas: quais dados? que formato? o que fazer se não encontrar?

**Bom:**
```
Extraia os seguintes campos deste documento SST.
Se um campo não for encontrado na imagem, retorne null (não invente).
Se o valor estiver parcialmente legível, retorne o que conseguir + flag "partial": true.

Responda APENAS em JSON, sem markdown, sem explicação.
```
+ responseSchema no Gemini:
```json
{
  "type": "object",
  "properties": {
    "empresa": {"type": "string", "description": "Razão social da empresa"},
    "cnpj": {"type": "string", "description": "CNPJ no formato XX.XXX.XXX/XXXX-XX"},
    "validade": {"type": "string", "description": "Data de validade no formato DD/MM/YYYY"},
    "tipo_documento": {"type": "string", "enum": ["ASO", "PPRA", "PCMSO", "LTCAT", "outro"]}
  },
  "required": ["empresa", "tipo_documento"]
}
```

### Exemplo 3: Calibração Claude 4.x (antes vs depois)

**Antes (Claude 3.x — funcionava, mas agora causa overtriggering):**
```
CRITICAL: You MUST ALWAYS use the search tool when the user asks a question.
NEVER answer from memory. This is ABSOLUTELY REQUIRED.
If in doubt, ALWAYS search.
```

**Depois (Claude 4.x — mesmo resultado, sem side effects):**
```
Use the search tool when answering factual questions, especially for events after
your training cutoff or when the user asks about specific current data.
For general knowledge questions where you're confident, you can answer directly.
```

## Integração com outras skills

- **n8n Architect:** Nodes de IA no n8n (Basic LLM, AI Agent, ~70 nodes de IA) precisam de prompts bem escritos. Use esta skill pro prompt, n8n Architect pra arquitetura do workflow. Considere MCP integration
- **Product Discovery & PRD:** Prompts pro Lovable são inputs do PRD. Se o prompt é uma instrução de feature, pode ser que o usuário precise primeiro de discovery
- **Lovable Knowledge:** Workspace/Project Knowledge são uma forma de context engineering persistente. Se o pedido é "como o Lovable deve se comportar", pode ser lovable-knowledge, não prompt-engineer
- **Skill Builder:** Se o usuário quer instruções persistentes que o Claude consulta automaticamente → é skill, não prompt. Redirecione
- **Security Audit:** Se o prompt é pra um agente com acesso a dados/tools, considere OWASP LLM Top 10 — prompt injection, excessive agency, system prompt leakage

## Quando NÃO usar esta skill

- Se o usuário quer criar uma **skill do Claude** (instruções persistentes com SKILL.md) → use skill-builder
- Se é um **prompt simples de uma linha** → faz direto, não precisa de skill
- Se o usuário quer ajuda com o **conteúdo** do prompt (lógica de negócio de um agente) → use a skill de domínio (PRD, n8n, etc) e esta skill só pro formato
- Se é **AGENTS.md pra projeto Lovable específico** → use lovable-knowledge (esta skill ajuda com o formato genérico, lovable-knowledge com o conteúdo específico)

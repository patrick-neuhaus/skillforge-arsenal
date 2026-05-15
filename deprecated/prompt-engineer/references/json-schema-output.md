# JSON Schema pra Output Estruturado — Referência

Última atualização: 2026-03-27

Consulte este arquivo quando o usuário quer controlar o formato de resposta de um LLM via JSON Schema — seja no n8n, API direta, ou qualquer integração.

---

## Quando usar output estruturado

- **Automações (n8n):** quando o output precisa ser parseado por nodes seguintes
- **APIs:** quando o consumidor espera formato previsível
- **Classificação:** quando o output é uma de N categorias
- **Extração:** quando precisa extrair campos específicos de texto/documento
- **Agentes com tools:** quando o agente deve retornar dados estruturados

## Claude: Structured Outputs GA

Claude 4.x tem Structured Outputs como feature GA. Parâmetro `output_format` com JSON Schema garante resposta válida.

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Classifique este ticket de suporte: 'Não consigo logar'"}],
    output_format={
        "type": "json_schema",
        "json_schema": {
            "name": "ticket_classification",
            "schema": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "enum": ["bug", "feature_request", "support", "billing", "other"]
                    },
                    "priority": {
                        "type": "string",
                        "enum": ["low", "medium", "high", "critical"]
                    },
                    "summary": {
                        "type": "string",
                        "description": "Resumo do problema em 1 frase"
                    }
                },
                "required": ["category", "priority", "summary"]
            }
        }
    }
)
```

### Quando usar Structured Outputs vs instrução no prompt
- **Structured Outputs:** quando o formato DEVE ser exato (automações, APIs, parsing)
- **Instrução no prompt:** quando flexibilidade no formato é OK (chat, análise)
- **Tools com enum:** pra classificação simples (ferramenta com campo enum nos valores válidos)

## Gemini: responseSchema nativo

Gemini suporta JSON Schema direto na API. Mais robusto que instrução no prompt pra extração.

```javascript
const result = await model.generateContent({
  contents: [{ role: "user", parts: [{ text: "Extraia os dados deste documento" }] }],
  generationConfig: {
    responseMimeType: "application/json",
    responseSchema: {
      type: "object",
      properties: {
        empresa: { type: "string", description: "Razão social" },
        cnpj: { type: "string", description: "CNPJ formato XX.XXX.XXX/XXXX-XX" },
        validade: { type: "string", description: "Data DD/MM/YYYY" }
      },
      required: ["empresa"]
    }
  }
});
```

Dica: use `description` nos campos pra guiar o modelo sobre O QUE extrair e EM QUAL FORMATO.

## Boas práticas pra JSON Schema

### 1. Use descriptions em todos os campos
```json
{
  "amount": {
    "type": "number",
    "description": "Valor total em reais, sem centavos (ex: 150, não 150.00)"
  }
}
```
O `description` é a instrução pro modelo sobre como preencher aquele campo.

### 2. Use enum pra categorias fechadas
```json
{
  "status": {
    "type": "string",
    "enum": ["active", "inactive", "pending", "cancelled"]
  }
}
```
Elimina respostas inesperadas como "ativo", "Ativo", "ATIVO".

### 3. Trate campos opcionais explicitamente
```json
{
  "phone": {
    "type": ["string", "null"],
    "description": "Telefone se encontrado, null se não"
  }
}
```
Sem isso, o modelo pode inventar um telefone.

### 4. Use required pra campos obrigatórios
Só marque como required campos que SEMPRE existem no input. Campos que podem não existir → nullable.

### 5. Mantenha schemas simples
- Máximo 10-15 campos por schema
- Se precisa de mais, quebre em sub-objetos
- Schemas complexos demais confundem o modelo

## No n8n

### Node "Structured Output Parser"
Configura JSON Schema pra garantir output formatado do LLM. Conecta após o node de LLM.

### Node "Basic LLM Chain" com output parser
1. Configure o LLM node com o prompt
2. Conecte um Output Parser node com o schema
3. O output já vem parseado e tipado

### Anti-pattern: JSON no prompt
```
Responda APENAS em JSON com os campos: name, email, phone.
Não inclua markdown, não inclua explicação.
```
Funciona às vezes, falha outras. Prefira Structured Outputs (Claude) ou responseSchema (Gemini) quando disponível. Use instrução no prompt só como fallback.

## Template de schema pra extração de documento

```json
{
  "type": "object",
  "properties": {
    "document_type": {
      "type": "string",
      "enum": ["invoice", "receipt", "contract", "report", "other"],
      "description": "Tipo do documento"
    },
    "fields": {
      "type": "object",
      "properties": {
        "company_name": {
          "type": ["string", "null"],
          "description": "Nome da empresa. null se não encontrado"
        },
        "date": {
          "type": ["string", "null"],
          "description": "Data principal no formato YYYY-MM-DD. null se não encontrado"
        },
        "total_amount": {
          "type": ["number", "null"],
          "description": "Valor total em reais. null se não encontrado"
        }
      }
    },
    "confidence": {
      "type": "number",
      "description": "Confiança geral da extração de 0.0 a 1.0"
    },
    "notes": {
      "type": ["string", "null"],
      "description": "Observações sobre campos parciais, ilegíveis, ou ambíguos"
    }
  },
  "required": ["document_type", "confidence"]
}
```

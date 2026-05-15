# Prompts de Extração de Dados (OCR, Classificação) — Referência

Última atualização: 2026-03-27

Consulte este arquivo quando o usuário quer extrair dados de documentos (PDF, imagem, texto), classificar conteúdo, ou fazer análise de sentimento com LLMs.

---

## Princípio central

Extração é o caso de uso onde **formato do output importa mais que qualquer outra coisa**. O modelo precisa retornar dados limpos, parseáveis, e previsíveis. Use Structured Outputs (Claude) ou responseSchema (Gemini) sempre que possível.

## Template pra extração de documento

```
Extraia os seguintes campos deste [tipo de documento].

Regras:
- Se um campo não for encontrado, retorne null (não invente)
- Se o valor estiver parcialmente legível, retorne o que conseguir + flag "partial": true
- Normalize datas para o formato YYYY-MM-DD
- Normalize valores monetários para número decimal sem símbolo (ex: 1500.50)
- Se houver ambiguidade, retorne a interpretação mais provável + nota no campo "notes"

[JSON Schema ou instrução de formato]
```

## Dicas por modelo

### Gemini (preferido pra OCR e visão)
- Use `responseSchema` nativo — mais robusto que instrução no prompt
- Use `description` em cada campo do schema pra guiar extração
- Prompt curto e direto — Gemini performa melhor com menos texto instrucional pra visão
- Pra documentos multi-página: processe página por página ou envie como PDF
- Pra tabelas: peça "extract as array of objects, one per row"

### Claude (pra documentos textuais complexos)
- Structured Outputs GA via `output_format`
- Bom pra extração que requer raciocínio (inferir campo de contexto)
- Long context: coloque documento no topo, instrução no final
- Pra documentos longos: peça pra citar trechos relevantes antes de extrair ("Ground in quotes")

## Classificação

### Template
```
Classifique o seguinte [tipo de conteúdo] em uma das categorias abaixo.

Categorias:
- [categoria_1]: [descrição com exemplos]
- [categoria_2]: [descrição com exemplos]
- [categoria_3]: [descrição com exemplos]

Retorne APENAS a categoria, sem explicação.
```

Pra Claude: use tool com campo enum contendo as categorias válidas.
Pra Gemini: use responseSchema com enum.

### Multi-label
```
Identifique TODAS as categorias que se aplicam (pode ser mais de uma).

Retorne como array de strings.
```

## Análise de sentimento

### Template
```
Analise o sentimento do seguinte texto.

Retorne:
- sentiment: "positive", "negative", "neutral", ou "mixed"
- confidence: 0.0 a 1.0
- key_phrases: lista das frases que mais influenciaram a classificação
```

## Erros comuns em extração

### ❌ Sem fallback pra campos ausentes
```
Extraia: nome, email, telefone
```
Problema: se telefone não existe no documento, o modelo inventa.
Fix: "Se não encontrado, retorne null"

### ❌ Formato ambíguo
```
Extraia a data do documento
```
Problema: "15 de março de 2026" vs "2026-03-15" vs "15/03/2026"
Fix: "Normalize datas para YYYY-MM-DD"

### ❌ Sem schema
```
Extraia todos os dados relevantes
```
Problema: "relevante" é subjetivo. O modelo decide o que extrair.
Fix: Liste explicitamente cada campo.

### ❌ Processamento de tabela sem estrutura
```
Extraia os dados da tabela
```
Problema: output pode ser texto narrativo ao invés de dados estruturados.
Fix: "Extract as JSON array of objects. Each row is one object. Use column headers as keys."

## Pipeline de extração no n8n

Padrão recomendado pra extração em massa:

```
Trigger → Loop Items → [LLM Extract] → [Parse JSON] → [Validate] → [Store/Output]
```

1. **Loop Items:** processa um documento por vez
2. **LLM Extract:** Gemini com responseSchema OU Claude com Structured Outputs
3. **Parse JSON:** valida que o output é JSON válido (fallback: retry)
4. **Validate:** verifica campos required, formatos, ranges
5. **Store:** salva no Supabase ou retorna

Dica: use error handling com retry pra lidar com outputs malformados. Mesmo com schema, pode falhar em ~2-5% dos casos.

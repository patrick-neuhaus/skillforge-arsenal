# System Prompts pra Agentes e Chatbots — Referência

Última atualização: 2026-03-27

Consulte este arquivo quando o usuário quer criar um system prompt pra agente de WhatsApp, Typebot, assistente virtual, ou qualquer chatbot persistente.

---

## Anatomia de um system prompt eficaz

Todo system prompt de agente deve ter 5 blocos. A ordem importa — informações mais importantes primeiro (primacy bias):

### 1. Role (1-2 linhas)
Quem o agente é, pra que serve. Curto e direto.
```xml
<role>
Você é o assistente virtual da [empresa]. Atende [público] via [canal].
</role>
```

### 2. Context (informações de domínio)
Tudo que o agente precisa saber pra responder sem pesquisar: horários, serviços, preços, políticas, contatos.
```xml
<context>
Horário: seg-sex 8h-18h, sáb 8h-12h.
Serviços: [lista]
Preços: [tabela simplificada ou referência]
Políticas: [cancelamento, garantia, prazos]
</context>
```

### 3. Instructions (comportamento)
O que fazer em cada situação. Use lista numerada com condições claras.
```xml
<instructions>
1. Cumprimente pelo nome se disponível
2. Identifique a intenção: [lista de intenções possíveis]
3. Para [intenção A]: [ação específica]
4. Para [intenção B]: [ação específica]
5. Se não souber: [fallback — escalar, pedir tempo, transferir]
</instructions>
```

### 4. Constraints (o que NÃO fazer)
Limites claros. Frasear positivamente quando possível.
```xml
<constraints>
- Responda apenas sobre [domínio]. Para outros assuntos: "Posso ajudar com [domínio]. Para outras questões, entre em contato com [canal]"
- Nunca dê [tipo de conselho proibido — médico, jurídico, financeiro]
- Nunca invente informações — se não sabe, diga que vai verificar
- Não compartilhe dados de outros clientes
</constraints>
```

### 5. Output format (como responder)
Tom, tamanho, formatação.
```xml
<output_format>
Mensagem curta (máx 3 parágrafos). Tom: [profissional/casual/acolhedor].
Use *negrito* pra destacar informações-chave.
Termine com pergunta ou próximo passo quando relevante.
</output_format>
```

## Template completo

```xml
<role>
[1-2 linhas: quem é, pra que serve]
</role>

<context>
[Informações de domínio que o agente precisa]
</context>

<instructions>
[Comportamento passo a passo com condições]
</instructions>

<constraints>
[Limites e restrições — fraseados positivamente quando possível]
</constraints>

<output_format>
[Tom, tamanho, formatação, idioma]
</output_format>
```

## Checklist de qualidade pra system prompts

- [ ] Role definido em 1-2 linhas?
- [ ] Context tem TODAS as informações que o agente precisa pra responder sem pesquisar?
- [ ] Instructions cobrem as 3-5 intenções mais comuns?
- [ ] Tem fallback claro pra quando não sabe responder?
- [ ] Constraints fraseados positivamente? (o que fazer ao invés do que não fazer)
- [ ] Output format define tom, tamanho e formatação?
- [ ] Testou com pelo menos 3 inputs diferentes?
- [ ] Sem caps lock excessivo? (Claude 4.x responde melhor a instrução normal)

## Anti-patterns

### ❌ System prompt genérico
```
Você é um assistente útil e educado.
```
Problema: zero contexto de domínio, zero orientação de comportamento.

### ❌ System prompt enciclopédico
```
[5000 palavras cobrindo cada cenário possível]
```
Problema: dilui atenção, modelo ignora partes. Mova detalhes pra knowledge base/RAG.

### ❌ Tudo em negativa
```
NÃO faça X. NUNCA faça Y. JAMAIS faça Z.
```
Problema: modelo foca no que não fazer em vez do que fazer. Reframe positivo.

### ✅ Versão correta
```
Quando o cliente perguntar sobre preços, consulte a tabela em <context>.
Para assuntos fora do domínio, redirecione educadamente.
```

## Considerações de segurança (OWASP LLM)

System prompts de agentes em produção devem considerar:
- **Prompt injection:** separar instruções de dados do usuário (XML tags ajudam)
- **System prompt leakage:** nunca colocar API keys ou secrets no system prompt
- **Excessive agency:** limitar tools disponíveis ao mínimo necessário
- **PII disclosure:** instruir explicitamente a não revelar dados de outros usuários

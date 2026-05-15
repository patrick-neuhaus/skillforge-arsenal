# Debug e Troubleshooting de Workflows

Última atualização: 2026-04-03

Processo estruturado para quando o usuário disser "meu workflow não funciona".

---

## Passo 1: Localizar o problema

- Qual node tá com erro? (vermelho no n8n)
- Qual a mensagem de erro? (exata, não resumida)
- O workflow funcionava antes e parou, ou nunca funcionou?
- Tá testando via Draft ou tá publicado?

## Passo 2: Classificar o tipo de erro

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

## Passo 3: Investigar

- Peça o output do node anterior ao que falha
- Peça o body/headers que o HTTP Request tá enviando
- Se possível, peça screenshot do node configurado

## Passo 4: Resolver

- Dê a solução específica (não "verifique suas configurações")
- Se for problema de expressão n8n, escreva a expressão correta
- Se for problema de API, aponte exatamente o que mudar

# Error Handling — 4 Camadas

Última atualização: 2026-04-03

Todo workflow de produção precisa de error handling. O nível de sofisticação depende da criticidade.

---

## Camada 1 — Error Workflow Global (todo workflow)

- Error Trigger node configurado no workflow settings
- Log no Supabase (tabela de logs): workflow_name, node_name, error_message, timestamp, input_data
- Notificação em workflows críticos: WhatsApp/Telegram via ntfy ou Evolution API
- Pega QUALQUER erro que nenhum outro tratamento pegou

## Camada 2 — Error por Node (workflows com APIs externas)

- No node HTTP Request: configurar "On Error" como "Continue" com output de erro
- Branch com IF após o node: checar se veio erro
- Se erro → tratar (retry, fallback, log específico)
- Se sucesso → segue fluxo normal
- Retry: 3 tentativas, intervalo crescente (1s → 2s → 5s), backoff exponencial
- Depois de 3 falhas: log + notificação + marcar pra reprocessamento

## Camada 3 — Exceção de Negócio (workflows com regras complexas)

- Use "Stop and Error" node quando uma condição de negócio falha (lead sem telefone, documento inválido)
- Diferente de erro técnico — aqui o workflow funcionou mas os dados não passam na regra
- Stop and Error dispara o Error Workflow Global da Camada 1
- Inclua mensagem de erro clara: "Lead sem telefone: {{ $json.lead_id }}"

## Camada 4 — Circuit Breaker (workflows com APIs instáveis)

- Pausa temporariamente chamadas de API quando threshold de falhas é excedido
- Implementação: armazene estado (contador de falhas + timestamp) em Data Table ou Redis
- Antes de chamar API frágil: cheque se circuito está aberto
- Se aberto → rota pra fallback ou fila de retry manual
- Configuração típica: 5 falhas consecutivas → cooldown de 30s antes de tentar novamente
- Jitter de ±20% no cooldown pra evitar thundering herd

---

## Decisão de Qual Camada Usar

| Tipo de Workflow | Camadas |
|---|---|
| Simples (cron interno, notificação) | 1 |
| Com API externa (Kommo, Evolution, Meta) | 1 + 2 |
| Crítico de negócio (pipeline de vendas, OCR) | 1 + 2 + 3 |
| Com API instável ou rate-limited | 1 + 2 + 3 + 4 |

---

## Classificação de Erros HTTP pra Decisão de Retry

| Código | Ação | Detalhe |
|--------|------|---------|
| 401/403 | Refresh credential, retry 1x | Token pode ter expirado |
| 404 | Skip ou archive | Recurso não existe |
| 422 | Fail sem retry | Request malformado, corrigir dados |
| 429 | Backoff exponencial | Usar header Retry-After se disponível |
| 5xx | Backoff exponencial, 3x | Problema temporário do servidor |
| ECONNREFUSED | Circuit Breaker | Serviço upstream indisponível |
| Timeout 30s+ | Retry 3x com wait 30s | Rede lenta ou serviço sobrecarregado |

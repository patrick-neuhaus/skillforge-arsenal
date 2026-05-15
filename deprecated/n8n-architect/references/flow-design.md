# Flow Design — Pensar Antes de Construir

Metodologia pra desenhar o fluxo inteiro ANTES de abrir o n8n. O objetivo é ter clareza total do que vai ser construído, evitando retrabalho.

---

## Framework: 7 Perguntas Obrigatórias

Responda TODAS antes de abrir o editor:

### 1. Qual o RESULTADO esperado?
Descreva o que acontece quando o workflow roda com sucesso. Não a implementação — o resultado de negócio.
- ❌ "O workflow pega dados da API e salva no banco"
- ✅ "Todo lead que chega pelo formulário é salvo no CRM, recebe email de boas-vindas, e o vendedor é notificado"

### 2. Qual o TRIGGER?
| Tipo | Quando usar | Exemplo |
|------|------------|---------|
| Webhook | Evento externo em tempo real | Formulário enviado, pagamento confirmado |
| Schedule/Cron | Rotina periódica | Relatório diário, sync a cada hora |
| Chat/Manual | Interação humana | Chatbot, comando manual |
| Evento de banco | Mudança no Supabase | INSERT em tabela via Realtime |
| Outro workflow | Chamado por subworkflow | Parte de um pipeline maior |

### 3. Quais SISTEMAS envolvidos?
Liste TODOS. Se são 5+, provavelmente precisa de subworkflows.
```
Exemplo: Supabase + Evolution API (WhatsApp) + Kommo (CRM) + Mautic (email)
```

### 4. Qual o HAPPY PATH?
Desenhe o caminho feliz — quando tudo dá certo:
```
Trigger → Validar input → Processar → Salvar → Notificar → Fim
```

### 5. Quais os BRANCHES?
Onde o fluxo pode tomar caminhos diferentes:
```
→ Lead novo ou existente?
→ Pagamento aprovado ou recusado?
→ Dados válidos ou inválidos?
```

### 6. Quais os ERROS possíveis?
| Erro | Impacto | Tratamento |
|------|---------|-----------|
| API retorna 429 (rate limit) | Perde dados | Retry com backoff |
| API retorna 500 | Perde dados | Dead-letter + notificação |
| Dados inválidos | Processamento errado | Validação no início |
| Timeout | Workflow trava | Timeout config + fallback |

### 7. Existe DEPENDÊNCIA de ordem entre sistemas?
- Precisa salvar no CRM ANTES de notificar? → sequencial
- Pode salvar no CRM E notificar ao mesmo tempo? → paralelo (async subworkflow)
- Se A falhar, B deve rodar mesmo assim? → independente

---

## Diagrama Textual (formato padrão)

Depois de responder as 7 perguntas, desenhe:

```
Trigger: [tipo] — [descrição]
  → Validate: [o que validar]
  → [Ação principal]
  → Branch: [condição]?
    → Sim: [ações]
    → Não: [ações]
  → Error: [tratamento]
  → Output: [resultado final]
```

### Exemplo completo:
```
Trigger: Webhook recebe lead do formulário
  → Validate: Email válido? Campos obrigatórios preenchidos?
  → Normalize: Extrair só name, email, phone (descartar resto)
  → Branch: Lead já existe no CRM?
    → Sim: Atualizar dados + mover pra próximo estágio do funil
    → Não: Criar lead no CRM + Criar contato no Mautic + Adicionar em sequência de email
  → Notify: Enviar WhatsApp pro vendedor responsável (async)
  → Error: Salvar em tabela de erros + Notificar canal Slack
  → Output: Lead processado com ID do CRM
```

---

## Decision Trees de Design

### Sync vs Async
```
Preciso do resultado pra continuar?
  → Sim: Síncrono (esperar resultado)
  → Não: Assíncrono (fire & forget — mais rápido)
```

### Webhook vs Schedule
```
O dado chega em tempo real?
  → Sim: Webhook
  → Não: Schedule (cron)
Preciso processar imediatamente?
  → Sim: Webhook
  → Não: Schedule com batch
```

### Único workflow vs Subworkflows
```
Quantos nodes vai ter?
  → <15 nodes: Workflow único
  → 15-30 nodes: Considerar subworkflows pra blocos reutilizáveis
  → 30+ nodes: Obrigatório modularizar (Load references/modularization-strategy.md)
```

### Loop Over Items vs Batch
```
API tem rate limit?
  → Sim: Loop Over Items + Wait (respeitar limite)
  → Não: Batch padrão (mais rápido)
Volume alto (>1000 items)?
  → Sim: Loop Over Items + normalização obrigatória
  → Não: Batch padrão funciona
```

---

## Output do --flow

Ao final do design, entregar ao usuário:

1. **Diagrama textual** do fluxo completo
2. **Sistemas envolvidos** com direção dos dados
3. **Decisões de design** (sync/async, webhook/cron, batch/loop)
4. **Riscos identificados** e como serão tratados
5. **Estimativa de waves** pra construção (Load references/wave-development.md)

⛔ **GATE:** Confirmar diagrama com usuário antes de começar a construir.

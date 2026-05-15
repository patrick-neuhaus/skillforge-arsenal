# Modularização — Quando e Como Extrair Subworkflows

Guia pra decidir quando extrair lógica em subworkflows e como estruturá-los corretamente.

---

## Princípio

O n8n não tem funções nativas como linguagens de programação. Subworkflows são o equivalente: blocos de lógica reutilizáveis que podem ser chamados por qualquer workflow.

---

## Quando Modularizar

### Indicadores (qualquer um basta)

| Sinal | Ação |
|-------|------|
| Mesma lógica aparece em 3+ workflows | Extrair em subworkflow |
| Workflow tem >15 nodes num bloco | Considerar separar |
| Workflow tem >30 nodes total | Obrigatório modularizar |
| Lógica complexa de API (retry, auth, parsing) | Encapsular em subworkflow |
| Equipe vai manter o workflow | Modularizar pra legibilidade |
| Lógica muda frequentemente | Centralizar pra atualizar 1x |

### Exemplos Reais

| Lógica | Frequência | Extrair? |
|--------|:----------:|:--------:|
| Transcrever áudio (Whisper/AssemblyAI) | Usado em 6+ workflows | ✅ Sim |
| Salvar lead em CRM (Mautic + Kommo) | Usado em 5+ workflows | ✅ Sim |
| Enviar mensagem WhatsApp (Evolution API) | Usado em 10+ workflows | ✅ Sim |
| Normalizar dados de formulário | Padrão repetitivo | ✅ Sim |
| Lógica específica de 1 workflow | Única vez | ❌ Não |
| IF simples com 2 branches | Trivial | ❌ Não |

---

## Subworkflow vs Code Node

| Critério | Subworkflow | Code Node |
|----------|:-----------:|:---------:|
| Reutilizável entre workflows | ✅ | ❌ |
| Equipe consegue entender | ✅ Visual | ⚠️ Precisa saber JS |
| Lógica complexa multi-step | ✅ | ❌ Fica grande |
| Transformação de dados simples | ❌ Over-engineering | ✅ Rápido |
| Parse/formato de string | ❌ | ✅ 3 linhas de JS |
| Chamada de API com retry | ✅ Visível no flow | ⚠️ Possível mas opaco |

**Regra geral:** Se envolve nodes visuais (HTTP, IF, Merge) → subworkflow. Se é transformação de dados pura → Code node ou Edit Fields.

---

## Como Estruturar Subworkflows

### Trigger do Subworkflow
Node: **"When Executed by Another Workflow"** (laranja)

Configure inputs explícitos com tipos:
```
Inputs:
  - name: String
  - email: String
  - phone: String
  - metadata: Object (opcional)
```

**Regra:** Use tipos específicos (String, Number, Boolean), NÃO use "Any". Tipo específico valida automaticamente — dados incorretos são rejeitados antes de entrar no subworkflow.

### Output do Subworkflow
Último node DEVE ser um **Set/Edit Fields** que define exatamente o que retorna:
```
Output:
  - success: Boolean
  - record_id: String
  - error_message: String (se falhou)
```

**Regra:** Nunca retorne tudo. Retorne SÓ o que o workflow pai precisa.

### Naming Convention
```
[SUB] - [AÇÃO] - [ALVO]
Exemplos:
  [SUB] - Salvar Lead - Kommo + Mautic
  [SUB] - Transcrever Áudio - Whisper
  [SUB] - Normalizar Dados - Formulário
  [SUB] - Enviar WhatsApp - Evolution
```

---

## Síncrono vs Assíncrono

### Síncrono (default — "Await completion")
```
Workflow Pai → Execute SubWorkflow → [espera resultado] → usa resultado → continua
```
- Pai BLOQUEIA até subworkflow terminar
- Recebe output do subworkflow
- **Usar quando:** precisa do resultado pra continuar

### Assíncrono (fire & forget)
```
Workflow Pai → Execute SubWorkflow → [não espera] → continua imediatamente
                                      ↓
                            SubWorkflow roda em background
```
- Pai NÃO espera
- NÃO recebe output do subworkflow
- **Usar quando:** não precisa do resultado (notificação, log, analytics)

### Decision Matrix

| Cenário | Modo |
|---------|:----:|
| Preciso do ID do registro criado | Síncrono |
| Enviar notificação (não importa se demorou) | Assíncrono |
| Salvar em 3 CRMs e continuar só quando todos salvaram | Síncrono |
| Salvar em 3 CRMs e não preciso esperar | Assíncrono (3x em paralelo) |
| Transcrever áudio e usar o texto | Síncrono |
| Logar evento em analytics | Assíncrono |

### Performance: Async é Mais Rápido

```
Síncrono (sequencial):
  CRM 1 (2s) → CRM 2 (2s) → CRM 3 (2s) = 6 segundos

Assíncrono (paralelo):
  CRM 1 (2s) ↘
  CRM 2 (2s) → todos rodam em paralelo = 2 segundos
  CRM 3 (2s) ↗
```

Respeita concurrency limit do n8n (default: 10 threads).

---

## Organização com Pastas

Organize workflows em pastas no n8n:

```
📁 [CLIENTE] - Artemis
  📁 Produção
    - [ARTEMIS] - CRON - Relatório Diário
    - [ARTEMIS] - WEBHOOK - Processar Lead
  📁 Subworkflows
    - [SUB] - Salvar Lead - Kommo
    - [SUB] - Enviar WhatsApp - Evolution
  📁 Testes
    - [TEST] - Webhook Mock
```

**Regra:** Subworkflows SEMPRE em pasta separada. Facilita encontrar e evita confusão.

---

## Anti-Patterns

| Anti-pattern | Correto |
|-------------|---------|
| Copiar 20 nodes idênticos em 5 workflows | Extrair subworkflow |
| Subworkflow com 1 node | Não precisa de subworkflow |
| Subworkflow sem input tipado | Definir tipos explícitos |
| Retornar 50 campos quando pai usa 3 | Retornar só o necessário |
| Async quando precisa do resultado | Usar síncrono |
| Síncrono quando não precisa do resultado | Usar assíncrono |
| Subworkflows sem naming convention | [SUB] - [Ação] - [Alvo] |

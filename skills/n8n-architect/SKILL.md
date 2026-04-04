---
name: n8n-architect
description: "Arquiteta, constrói, debugga, otimiza e revisa automações n8n. Planeja workflows do zero, integra sistemas (Supabase, Evolution API, Kommo, Meta, Mautic), automatiza processos de negócio e fixa fluxos quebrados. Use quando: criar workflow, build automação, debugar erro n8n, otimizar performance, planejar integração entre sistemas, 'conectar X com Y', revisar workflow existente, configurar AI Agent, webhook, subworkflow, error handling, retry, 'meu workflow não funciona', delegar workflow pra equipe, documentar fluxo, MCP, queue mode. Também funciona como arquiteto quando o usuário planeja um fluxo multi-sistema (Supabase + API externa + WhatsApp) mesmo sem mencionar n8n. NÃO use para SQL/schema sem automação (use supabase-db-architect) nem frontend/Lovable puro."
---

# n8n Automation Architect v4

IRON LAW: NUNCA construa um workflow sem error handling em CADA node HTTP Request. Um 4xx/5xx não tratado crasha o fluxo inteiro. Sem exceção.

## Opções

| Opção | Descrição | Default |
|-------|-----------|---------|
| `--build` | Construir workflow do zero | - |
| `--debug` | Debugar workflow com problema | - |
| `--optimize` | Otimizar workflow existente | - |
| `--review` | Revisar workflow pra produção | - |
| `--delegate` | Gerar briefing pra equipe | - |
| `--doc` | Documentar workflow existente | - |
| `--template <n>` | Usar template específico (1-8) | - |

## Checklist do Workflow

```
n8n Architect Progress:

- [ ] 1. Entender requisito ⚠️ REQUIRED
  - [ ] 1.1 O que o workflow faz (resultado, não implementação)
  - [ ] 1.2 Trigger: webhook, cron, chat, evento?
  - [ ] 1.3 Sistemas envolvidos (APIs, bancos, mensageria)
  - [ ] 1.4 Volume esperado (execuções/hora)
  - [ ] 1.5 Criticidade (pode perder dados? precisa de fila?)
- [ ] 2. Arquitetar
  - [ ] 2.1 Escolher template base. Load `references/templates.md`
  - [ ] 2.2 Definir estrutura: Trigger → Validação → Processamento → Output → Log
  - [ ] 2.3 Definir camadas de error handling. Load `references/error-handling.md`
  - [ ] 2.4 Se envolve IA: Load `references/ai-nodes.md`
  - [ ] 2.5 Se envolve filas/edge functions: Load `references/filas-e-edge-functions.md`
- [ ] 3. Construir (em waves)
  - [ ] 3.1 Wave 1: Trigger + caminho feliz + output básico
  - [ ] 3.2 Wave 2: Branches + error handling + Execution Data
  - [ ] 3.3 Wave 3: Otimização + documentação (sticky notes, nomes)
- [ ] 4. Validar ⚠️ REQUIRED
  - [ ] 4.1 Testar como Draft antes de publicar
  - [ ] 4.2 Rodar pre-delivery checklist
  - [ ] ⛔ GATE: Confirmar com usuário antes de publicar
- [ ] 5. Entregar
  - [ ] 5.1 Publicar workflow
  - [ ] 5.2 Se delegando: gerar briefing. Load `references/delegacao.md`
  - [ ] 5.3 Se documentando: Load `references/documentacao-workflow.md`
```

## Contexto

Stack principal: n8n + Supabase + Evolution API + Kommo + Mautic. Equipe (Hygor, Jonas) trabalha com n8n — a skill também serve para gerar briefings técnicos delegáveis.

Load `references/n8n-2-0.md` — mudanças do n8n 2.0 que afetam todas as decisões.

## Princípios Inegociáveis

1. **Hierarquia de nodes:** Edit Fields > Core nodes > Code node > HTTP Request > nodes nativos/community. Load `references/arquitetura-padroes.md` para detalhes.
2. **JSON Schema pra controlar output de IA.** Toda chamada pra LLM deve ter schema de saída definido.
3. **Workflow legível > workflow esperto.** Se alguém da equipe não entende em 5 minutos, tá mal estruturado.
4. **Error handling não é opcional.** Todo workflow de produção trata erros. Sem exceção.
5. **Log tudo que importa.** Se deu errado e não tem log, é como se nunca tivesse existido.
6. **Draft → teste → Publish.** Nunca publique sem testar.

## Passo a Passo por Modo

### --build (Construir workflow)

1. Entender o requisito (perguntar se ambíguo — não assumir)
2. Identificar template base → Load `references/templates.md`
3. Definir padrões de arquitetura → Load `references/arquitetura-padroes.md`
4. Definir error handling por criticidade → Load `references/error-handling.md`
5. Se envolve IA → Load `references/ai-nodes.md`
6. Construir em waves (Wave 1 → teste → Wave 2 → teste → Wave 3)
7. Rodar pre-delivery checklist antes de publicar

### --debug (Debugar workflow)

Load `references/debug-troubleshooting.md` e seguir o processo:
1. Localizar o node com erro
2. Classificar o tipo de erro (HTTP code, dados, trigger, timeout)
3. Investigar (output do node anterior, body/headers enviados)
4. Resolver com solução específica — não genérica

### --optimize (Otimizar workflow)

1. Verificar hierarquia de nodes (Code node onde poderia ser Edit Fields?)
2. Verificar error handling (tem as camadas necessárias?)
3. Verificar nomenclatura (todos os nodes renomeados?)
4. Verificar se tem subworkflows que deveriam existir (lógica repetida?)
5. Verificar performance (volume justifica Redis/fila/queue mode?)
6. Se escala é questão → Load `references/mcp-queue-mode.md`

### --review (Revisar pra produção)

Rodar pre-delivery checklist completo. Se falhar em qualquer item ⚠️ REQUIRED, bloquear.

### --delegate (Gerar briefing)

Load `references/delegacao.md` para template e calibração por pessoa (Jonas vs Hygor).

### --doc (Documentar)

Load `references/documentacao-workflow.md` para template padrão.

## Confirmation Gates

⛔ **Antes de publicar workflow em produção:** "Workflow testado como Draft. Confirma publicação em produção?"

⛔ **Antes de modificar workflow publicado:** "Esse workflow tá em produção. Confirma que quer editar? (Lembre: editar salva como Draft, não afeta produção até Publish)"

⛔ **Antes de deletar workflow/node:** "Tem certeza? Essa ação não tem undo."

## Anti-Patterns

| Anti-pattern | Por que é ruim | O que fazer |
|---|---|---|
| Code node pra tudo | Latência extra (Task Runner), difícil debug, equipe não entende | Edit Fields + Core nodes primeiro, Code só em último caso |
| HTTP Request sem error handling | Um 4xx/5xx crasha o fluxo inteiro | "On Error: Continue" + branch de tratamento |
| Nomes padrão nos nodes | "HTTP Request 3" não diz nada, impossível debugar | Renomear TODOS: [Ação] [Alvo] |
| Workflow monolítico (50+ nodes) | Impossível debugar, manter ou delegar | Subworkflows pra blocos reutilizáveis |
| Ignorar validação de input | Dados sujos propagam erro downstream | Validar LOGO DEPOIS do trigger |
| Publicar sem testar como Draft | Bug vai direto pra produção | Draft → teste manual → Publish |
| Hardcode de tokens/URLs | Quebra ao trocar ambiente, risco de segurança | Credentials do n8n ou variáveis |
| Confiar em output livre de LLM | Resposta imprevisível quebra nodes downstream | JSON Schema em toda chamada de IA |
| Community node pra API crítica | Desatualizado, limitado, sem controle | HTTP Request com controle total |
| Não logar erros | "Deu erro" mas ninguém sabe quando, onde, ou por quê | Tabela de logs no Supabase, sempre |

## Pre-Delivery Checklist

Antes de considerar o workflow pronto:

- [ ] Todos os nodes renomeados com padrão [Ação] [Alvo]
- [ ] Error handling configurado (mínimo: Camada 1 global)
- [ ] HTTP Requests com "On Error: Continue" + branch de tratamento
- [ ] Validação de input logo após o trigger
- [ ] Credentials do n8n usadas (zero hardcode)
- [ ] Testado como Draft com dados reais
- [ ] Execution Data configurado (se alto volume)
- [ ] Sticky notes em branches complexos
- [ ] Logs de sucesso E erro salvos
- [ ] Nomenclatura do workflow: [CLIENTE] - [TIPO] - [DESCRIÇÃO]
- [ ] Salvamento de execuções configurado (erro only vs todas)
- [ ] Se tem webhook público: autenticação validada
- [ ] Se tem IA: JSON Schema no output

## Quando NÃO Usar Esta Skill

- **SQL/schema puro sem automação** → use `supabase-db-architect`
- **Frontend/Lovable puro** → não envolve n8n
- **Gestão/delegação genérica** → use `tech-lead-pm`
- **Prompt engineering isolado** → use `prompt-engineer`
- **Usuário quer montar workflow mas deveria estar delegando** → questione primeiro (filtro de alavancagem), depois ajude se fizer sentido
- **Confuso sobre qual skill usar** → invoque `maestro`

## Integração

| Skill | Quando combinar |
|-------|----------------|
| `sdd` | Workflow complexo que precisa de spec antes de implementar. Use SDD pra planejar, n8n-architect pra executar. |
| `supabase-db-architect` | Workflow faz CRUD no Supabase. Valide schema/RLS com a skill de banco ANTES de construir o workflow. |
| `security-audit` | Workflow em produção com dados sensíveis. Rode audit de segurança nos webhooks, credentials e exposição de dados. |
| `maestro` | Não sabe por onde começar ou envolve múltiplas skills. Maestro roteia. |
| `tech-lead-pm` | Delegando workflow pra equipe. Combine briefing técnico (n8n-architect) com template de task (tech-lead-pm). |
| `prompt-engineer` | Configurando AI Agent nodes, system prompts, JSON Schema de output. |

## Referências

| Arquivo | Conteúdo |
|---------|----------|
| `references/n8n-2-0.md` | Mudanças do n8n 2.0 (Draft/Published, Task Runners, segurança) |
| `references/arquitetura-padroes.md` | Hierarquia de nodes, nomenclatura, estrutura, subworkflows, Redis, Data Tables |
| `references/error-handling.md` | 4 camadas de error handling + classificação de erros HTTP |
| `references/templates.md` | 8 templates de workflows comuns |
| `references/ai-nodes.md` | AI Agent, RAG, chatbot, OCR com IA, Human-in-the-Loop |
| `references/filas-e-edge-functions.md` | Edge Functions + pgmq + padrão webhook → fila → n8n |
| `references/mcp-queue-mode.md` | MCP (client/server/instance) + Queue Mode + scaling |
| `references/delegacao.md` | Template de briefing + calibração por pessoa |
| `references/debug-troubleshooting.md` | Processo de debug estruturado + tabela de erros |
| `references/documentacao-workflow.md` | Template de documentação de workflow |
| `references/seguranca.md` | Checklist de segurança + Python em Code nodes |

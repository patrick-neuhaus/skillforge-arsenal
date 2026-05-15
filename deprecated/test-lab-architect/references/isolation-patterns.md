# Isolation Patterns — Step 7 reference

Carrega no Step 7 do `test-lab-architect`. Define como o lab fica isolado de produção pra mudança no lab não vazar pra prod por acidente.

## Por que isolamento importa

Lab é onde gestor edita prompts/critérios pra testar. Se essa edição vaza pra prod, prod muda sem deploy controlado. Risco: gestor edita "vamos testar critério mais rigoroso", roda no lab, vê 60% assertividade, mas o critério já tava aplicado em produção e quebrou clientes em real-time.

Isolamento garante: **mudança no lab só afeta lab**.

## Pré-requisito: orquestrador externo

Se o app tem só app + DB (sem n8n, edge functions com lógica pesada, APIs externas mantendo state), isolamento é mais simples — basta flag `is_test` nas tabelas relevantes.

Se o app tem orquestrador externo (n8n com workflows que processam docs, edge functions que chamam OpenAI), isolamento envolve essa camada também. **Sem isolar o orquestrador, lab é mentira** — workflow do n8n executa lógica de prod mesmo se a flag is_test estiver setada.

## Padrões de isolamento

### A. Flag is_test no schema (mais simples)

Adiciona coluna `is_test: bool` em todas as tabelas que registram processamento (documentos, validações, logs).

- Lab cria registros com `is_test = true`
- Prod ignora `is_test = true` em filtros e dashboards
- Mesmo orquestrador, mas workflow do orquestrador precisa respeitar a flag (ex: n8n não chama webhook real se is_test, ou usa endpoint de teste)

**Quando funciona**: orquestrador é controlável (você consegue editar n8n pra respeitar is_test, ou edge function pra rotear pra modelo de teste). App tem volume baixo de teste.

**Quando NÃO funciona**: orquestrador é caixa-preta (n8n self-host de cliente, edge function não-trivial), ou volume de teste é grande o suficiente pra impactar performance/custo do orquestrador de prod.

### B. Instância staging do orquestrador

Roda 2ª instância do orquestrador (n8n staging, edge function preview) com webhook/endpoint separado.

- Lab usa staging
- Prod usa prod
- Tabelas podem ser as mesmas (com is_test) ou separadas

**Quando funciona**: orquestrador suporta multi-instance sem custo proibitivo. Patrick controla o orquestrador.

**Quando NÃO funciona**: n8n self-host com recursos limitados. Custo de licença adicional.

### C. Tabelas sandbox separadas

`documentos_sandbox`, `validacoes_sandbox`, etc. Lab escreve só em sandbox. Prod nunca lê de sandbox.

- Lab escreve em sandbox tables
- Prod ignora completamente
- Schema duplicado mas isolado

**Quando funciona**: schema é estável, app tem perfil de admin separado pro lab.

**Quando NÃO funciona**: schema muda muito (cada migração precisa rodar 2x), volume de sandbox é alto (storage extra).

### D. Subdomain ou rota separada

`lab.app.com` ou `app.com/lab`. Frontend separado, backend pode ser mesmo ou separado.

- Frontend isolado: lab tem UI completamente separada (componentes, rotas)
- Backend pode ser mesmo (com flag is_test) ou separado (instância staging)

**Quando funciona**: lab vai virar produto que cliente acessa diretamente. Ou lab tem UI complexa que merece código separado.

**Quando NÃO funciona**: MVP que vai pivotar. Tempo de setup de subdomain não compensa.

## Tabela de decisão

| Cenário | Isolamento recomendado |
|---------|------------------------|
| App só app + DB, sem orquestrador | Flag `is_test` |
| Tem n8n controlável pelo Patrick | Flag `is_test` + n8n respeita flag |
| Tem n8n self-host do cliente, sem recurso pra 2ª instância | Tabelas sandbox + n8n não roda em sandbox (ou roda mock) |
| App vai virar produto multi-cliente com lab integrado | Subdomain + instância staging do orquestrador |
| MVP, volume baixo, gestor único | Flag `is_test` (default mais simples) |

## Sync de config (lab ↔ prod)

Mudança no lab que aprovou tem que ir pra prod controladamente.

### Padrões:

- **Manual flag promotion** (mais simples): config no lab tem campo `promoted_to_prod: bool`. Quando gestor aprova, alguém com permissão muda esse campo, e prod re-lê config. Auditável, simples.
- **Versionamento ativo** (estilo athié): config tem `version: int` + `ativo: bool`. Lab cria nova versão. Quando aprovada, alguém promove ativo=true (e ativo=false na anterior). Prod sempre lê ativo=true.
- **Approval workflow**: PR-style — lab gera proposta, outro humano aprova, automation aplica em prod. Demanda mais infra mas auditável.

### Anti-padrão crítico
**Lab edita config compartilhada com prod**. Significa que toda edição no lab afeta prod imediatamente. Já vi isso em apps Lovable mal-arquitetados — config tá em uma tabela `system_config`, lab edita ela, prod usa ela. Lab vira agente de chaos. Sempre separe.

## Como apresentar no output

Step 7 do output markdown deve ter:
- Modelo de isolamento escolhido (A/B/C/D) + justificativa
- Schema diff explícito (quais tabelas precisam de is_test, quais ficam sandbox)
- Como orquestrador se comporta em cada modo
- Sync de config: padrão escolhido + quem aprova + como auditar
# Promotion Patterns — Step 8 reference

Carrega no Step 8 do `test-lab-architect`. Define **reset com escopo controlado** + **promoção lab→prod**.

## Reset: o que reseta vs o que persiste

Operador edita prompts/critérios no lab e a assertividade fica horrível. Precisa voltar pro estado bom. Botão de reset.

### Sempre reseta
- **Config editada no lab**: prompts, critérios, validações modificadas pelo operador na sessão atual
- **Resultado do experimento atual**: rodada que tá em curso (não a histórica)

### Nunca reseta (CRÍTICO)
- **Base de gabarito**: dados validados por humano — perdeu, perdeu meses de curadoria
- **Histórico de experimentos**: experimentos anteriores ficam arquivados pra comparação. Reset apaga só o atual.
- **Config promovida pra prod**: o que tá em produção não é tocado pelo reset do lab.

### Decisão por caso
- **Config não-editada herdada de prod**: depende. Se lab pinned uma versão específica do prod, reset volta pra "última versão de prod no momento do pin". Se lab não pinned, reset volta pra prod atual.
- **Notas/observações do operador**: persiste por default (pode ter insight valioso). Reset opcional via "limpar notas também".

## Tabela de scopes

| Item | Reset por default | Reset opcional |
|------|:-----------------:|:--------------:|
| Prompt editado no lab | ✅ | - |
| Critério editado no lab | ✅ | - |
| Resultado do experimento atual | ✅ | - |
| Histórico de experimentos | ❌ | ⚠️ (com confirm dupla) |
| Base de gabarito | ❌ NUNCA | ❌ NUNCA |
| Config em prod | ❌ | ❌ |
| Notas/observações | ❌ | ✅ |

## Promoção lab → prod

Config validada no lab (assertividade satisfatória) tem que virar prod. Como?

### Padrão 1: Versionamento ativo (recomendado pra apps tipo athié)

Inspirado no `system_prompts.ativo` que o athié-docs-flow já tem.

- Cada config tem `id`, `version`, `ativo: bool`, `created_in_lab: bool`, `promoted_at: timestamp`
- Lab cria novas versões com `ativo=false` e `created_in_lab=true`
- Quando gestor aprova, ação "promover" seta `ativo=true` na nova versão e `ativo=false` na anterior
- Prod lê só `ativo=true`
- Rollback: reverte ativo pra versão anterior, sem deploy

**Vantagens**: auditável, reversível, sem deploy.
**Desvantagens**: só funciona pra config que cabe em DB (prompts, critérios, thresholds). Config-as-code (lógica em arquivo .ts) precisa deploy mesmo.

### Padrão 2: Approval workflow com 2 olhos

Promoção precisa de aprovação de uma 2ª pessoa.

- Lab gera "proposta de promoção" (registro com config nova + assertividade do experimento + quem propôs)
- Outra pessoa com role `approver` revisa e aprova/rejeita
- Aprovação dispara promoção automática
- Rejeição volta pro lab com nota

**Vantagens**: 4 olhos, evita gestor único promover algo errado.
**Desvantagens**: mais infra, mais lento. Vale só pra config crítica.

### Padrão 3: Threshold automático

Config promove automaticamente se assertividade no experimento bate threshold X.

- Lab roda experimento, calcula assertividade
- Se >= threshold (ex: 95%), automation seta a config como ativa em prod
- Notifica responsável

**Vantagens**: rápido, sem fricção.
**Desvantagens**: confia 100% no gabarito. Se gabarito tá viciado, threshold mente. Não usa por default — só pra cenários onde gabarito é blindado.

### Padrão 4: Blue-green

Mantém 2 versões ativas em paralelo. Promove gradual: 10% do tráfego pra nova, 90% pra antiga. Aumenta conforme métrica.

**Vantagens**: descobre problemas em prod sem big-bang.
**Desvantagens**: infra cara. Requer roteamento de tráfego, métricas em tempo real. Vale pra apps com volume alto.

## Tabela de decisão

| Cenário | Padrão recomendado |
|---------|---------------------|
| MVP, gestor único, config simples | **Versionamento ativo** |
| Gestor + dev, config crítica | Versionamento ativo + Approval workflow |
| Gabarito blindado, alta confiança | Threshold automático (com versionamento ativo como fallback) |
| Volume alto, app maduro, custo de erro alto | Blue-green |

Default pra perfil Patrick (apps Lovable + Supabase + n8n): **Versionamento ativo** com possibilidade de approval se cliente pedir.

## Anti-padrões

- **Promoção direta sem audit trail**: lab promove e ninguém sabe quando ou por quê. Sempre registra `promoted_at`, `promoted_by`, e mantém versão anterior pra rollback.
- **Sem rollback**: se config nova quebrar prod, voltar tem que ser 1 clique. Não pode requerir deploy ou query manual.
- **Reset que apaga gabarito**: aborta arquitetura. Reset NUNCA toca em gabarito.
- **Aprovação de si mesmo**: mesma pessoa que editou no lab promove. 0 olhos extras. Aceita só em casos triviais.

## Como apresentar no output

Step 8 do output markdown deve ter:
- Padrão de promoção escolhido + justificativa
- Lista explícita do que reseta vs persiste
- Quem promove (pessoa, role, processo)
- Como reverter (rollback path)
- Audit trail: quais campos persistem em cada promoção pra rastreabilidade
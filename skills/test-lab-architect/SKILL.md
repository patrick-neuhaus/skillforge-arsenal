---
name: test-lab-architect
description: "Skill que arquiteta laboratórios de teste para apps com IA no meio do processo. Conduz discovery do caso, força check de gabarito (ground truth), decide entre lab inline/standalone/híbrido, define granularidade de comparação (binária, LLM-as-judge, híbrida), planeja isolamento de orquestradores externos (n8n, edge functions), modelo de reset e promoção lab→prod, UX do operador. Output: documento markdown estruturado pra usar como contexto no Lovable, Cursor ou implementação manual. Use SEMPRE que mencionar: lab de testes, laboratorio de testes, validation lab, ambiente de testes pra IA, 'como vou validar a IA?', 'medir assertividade', 'testar prompts antes de prod', 'comparar versão de prompt', 'saber se a IA tá acertando', 'retrofit de validação', human-in-the-loop, ground truth design, evaluation lab architecture, AI assertiveness, prompt experiment lab. NÃO use pra: gerar código (lovable-router), executar evals em traces (hamelsmu/evals-skills), revisar PRD (product-discovery-prd)."
---

# Test Lab Architect

IRON LAW: NUNCA arquitete um lab sem confirmar gabarito (ground truth) primeiro. Lab sem gabarito é teatro, não validação — IA fica boa em adivinhar, não em acertar.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--full` | Discovery completo + arquitetura | true |
| `--retrofit` | App existente — lê código primeiro pra entender domínio | - |
| `--quick` | Caso simples, pula deep discovery | - |

## Workflow

```
Test Lab Architect Progress:

- [ ] Step 1: Discovery do caso ⚠️ REQUIRED
  - [ ] 1.1 Input → processo IA → output
  - [ ] 1.2 Quem opera o lab (perfil, frequência, skill técnica)
  - [ ] 1.3 Por que precisa do lab agora
- [ ] Step 2: Code Audit ⚠️ CONDITIONAL (--retrofit)
  - [ ] 2.1 Lê schema DB (tabelas relevantes)
  - [ ] 2.2 Lê lógica IA (prompts, critérios, validações)
  - [ ] 2.3 Lê integrações (n8n, edge functions, APIs)
  - [ ] 2.4 Identifica patterns custom vs genéricos
- [ ] Step 3: Ground Truth Check ⛔ BLOCKING
  - [ ] 3.1 Existe? Volume? Balanceamento? Quem validou?
  - [ ] 3.2 Alerts de viés (volume baixo, classe majoritária >70%, validador único)
  - [ ] 3.3 Se não existe: educa + ajuda estruturar coleta
  - [ ] ⛔ GATE: Sem gabarito viável, recusa arquitetar e diz por quê
- [ ] Step 4: Build vs Integrate (informational)
  - [ ] 4.1 Apresenta Langfuse/Braintrust/promptfoo como alternativa
  - [ ] 4.2 Default: build custom (perfil Patrick: apps Lovable+Supabase+n8n)
- [ ] Step 5: Modelo arquitetural ⚠️ REQUIRED
  - [ ] 5.1 Inline / Standalone / Híbrido — decide via tabela
- [ ] Step 6: Granularidade + comparação ⚠️ REQUIRED
  - [ ] 6.1 Macro (decisão final) e/ou micro (sub-componentes)
  - [ ] 6.2 Binária / LLM-judge / híbrida — decide por output
- [ ] Step 7: Pré-reqs de isolamento
  - [ ] 7.1 Orquestrador externo (n8n staging? flag is_test?)
  - [ ] 7.2 Sync de config (prompts, critérios) lab ↔ prod
- [ ] Step 8: Reset + promoção lab→prod ⚠️ REQUIRED
  - [ ] 8.1 O que reseta vs o que persiste
  - [ ] 8.2 Como config validada vira prod (manual/aprovação/automática)
- [ ] Step 9: UX do operador
  - [ ] 9.1 Telas (seleção, edição, execução, resultado, histórico)
  - [ ] 9.2 Permissões (quem edita, quem só vê)
- [ ] Step 10: Output ⛔ GATE
  - [ ] 10.1 Markdown estruturado segundo output-template
  - [ ] ⛔ GATE: Patrick revisa antes de levar pro Lovable
```

## Step 1: Discovery do caso

Pergunte em bloco, não tudo de uma vez:
- O que entra no app, o que sai, qual a lógica de IA no meio?
- Quem vai operar o lab? (gestor não-técnico? dev? admin?)
- Frequência: 1x/semana? Diário? Ad-hoc quando regulação muda?
- Por que precisa AGORA? (problema concreto, não hipótese)

Não invente — extraia. Se Patrick disser "monta lab pra athié", pergunte os 4 blocos antes de propor qualquer coisa.

## Step 2: Code Audit (conditional)

Skip se app não existe ainda. Run se `--retrofit` ou se Patrick mencionou app que já roda.

Leia (não modifique):
- Schema DB — tabelas relacionadas ao processo de IA
- Prompts e critérios — como tão estruturados, são editáveis ou hardcoded
- Integrações externas — n8n workflows, edge functions, APIs
- Componentes existentes que tocam o domínio

Identifique: o que é custom (não cabe em ferramenta genérica) vs genérico (poderia plugar Langfuse).

## Step 3: Ground Truth Check ⛔ BLOCKING

Load `references/ground-truth-design.md`.

⛔ Sem gabarito viável, **recusa** arquitetar e diz por quê. Lab sem gabarito é teatro.

Perguntas blocking:
1. Existe base validada por humano? (sim / não / parcial)
2. Volume por tipo? (alerta se < 30)
3. Balanceamento? (alerta se classe majoritária > 70%)
4. Quem validou? (especialista único = red flag de viés)
5. Como vai ser atualizada quando critério mudar?

Se gap crítico: avise risco específico antes de seguir. Exemplo: "Com 10 CPFs todos aprovados, qualquer prompt vai dar 100% — gabarito não tem poder discriminativo."

## Step 4: Build vs Integrate (informational)

Apresente 3 alternativas externas: Langfuse (open source self-hosted), Braintrust (SaaS pago), promptfoo (CLI + web UI).

**Default = build custom** pro perfil de cliente Patrick (apps Lovable+Supabase+n8n customizados, 70%+ lógica de domínio que ferramenta externa não cobre bem). Mas SEMPRE mencione integrate como opção quando: uso baixo (<2x/sem), sistema simples (<20% custom), cliente já é técnico.

Não pule essa pergunta — sem ela, build vira default por inércia.

## Step 5: Modelo arquitetural

Load `references/architectural-models.md`.

Tabela: inline (validação acontece em prod, gascat-style) / standalone (lab paralelo, athié-style) / híbrido. Critérios: edita-se config no lab? Operador é técnico? Volume de teste alto?

## Step 6: Granularidade + comparação

Load `references/comparison-strategies.md`.

Granularidade: macro (decisão final) e/ou micro (sub-componentes/critérios). Tipo de comparação: binária (decisão aprovado/recusado) / LLM-as-judge (output qualitativo) / híbrida. Decide por output, não one-size-fits-all.

## Step 7: Pré-reqs de isolamento

Load `references/isolation-patterns.md`.

Para apps com orquestrador externo (n8n, edge functions): instância staging separada vs flag is_test no schema de prod. Como sincroniza config (prompts, critérios) entre lab e prod.

## Step 8: Reset + promoção lab→prod

Load `references/promotion-patterns.md`.

Define explicitamente: o que reseta (config editada no lab) vs o que persiste (base de docs, histórico de experimentos). Como config validada vira prod (manual com aprovação, automática com threshold, blue-green, versionamento estilo `system_prompts.ativo`).

## Step 9: UX do operador

Telas: seleção (escolhe tipo/escopo), edição (config no lab), execução (rodar batch), resultado (assertividade + divergências), histórico (comparar experimentos). Permissões: quem edita, quem só visualiza.

## Step 10: Output ⛔ GATE

Load `references/output-template.md`.

Gera 1 arquivo markdown único com 10 seções (uma por step). Apresenta pro Patrick revisar antes de considerar pronto.

## Anti-Patterns

- **Pular Ground Truth check** — "ah, depois resolvemos" → lab inútil. Sempre BLOCKING.
- **Ler código pra arquitetar componentes** — isso é `component-architect`. Aqui lê pra entender domínio.
- **Gerar código** — boundary clara: skill arquiteta, outras skills materializam.
- **Recomendar build sem mencionar integrate** — sempre mostre Langfuse/Braintrust como alternativa, mesmo que default seja build.
- **Inventar pré-reqs sem ler código** — `--retrofit` sem code audit gera recomendação genérica e fraca.
- **Misturar arquitetura com eval engineering** — calibração de LLM-judge profunda é hamelsmu/evals-skills, não aqui.

## Pre-Delivery Checklist

- [ ] Output markdown tem 10 seções (uma por step)
- [ ] Step 3 (ground truth) tem dados concretos: volume, balanceamento, fonte de validação
- [ ] Step 5 (modelo) declara explicitamente: inline / standalone / híbrido + justificativa
- [ ] Step 6 (comparação) decide tipo por output (não one-size-fits-all)
- [ ] Step 7 (isolamento) considera orquestrador externo se aplicável
- [ ] Step 8 tem regra explícita do que reseta vs persiste, e fluxo de promoção lab→prod
- [ ] Build vs Integrate aparece (mesmo se default for build)
- [ ] Boundary com hamelsmu/evals-skills citada (eval engineering ≠ arquitetura)

## Integration

| Etapa | Skill | Quando |
|-------|-------|--------|
| Antes | `product-discovery-prd` | Se app ainda não existe — PRD primeiro |
| Antes | `reference-finder --solution-scout` | Se quer reverificar build vs integrate |
| Depois | `lovable-router` | Se for app Lovable e precisa virar prompt |
| Depois | `lovable-knowledge` | Se precisa AGENTS.md pro Lovable manter padrão |
| Depois | `supabase-db-architect` | Se schema novo (sandbox tables) |
| Downstream | `hamelsmu/evals-skills` | Eval engineering profundo (LLM-judge calibration, synthetic data) |

## When NOT to use

- App sem IA no meio → não precisa de lab de validação de assertividade
- App com IA mas baixa criticidade → talvez 2h de prompt manual já basta
- Eval engineering puro (calibrar judge contra human labels) → use hamelsmu/evals-skills
- Já tem lab arquitetado, quer só implementar → pula direto pro lovable-router
- Pergunta sobre métrica única ("qual % de assertividade é bom?") → responde direto, sem skill

## Exemplo de interação

**Patrick:** "monta lab pra athié"

**Skill (Step 1):** "Antes de arquitetar, 4 perguntas:
1. Quem opera — gestor de documentos, dev, admin?
2. Frequência esperada — diário, semanal, ad-hoc quando regulação muda?
3. Por que agora — problema concreto que aconteceu, ou planejamento?
4. App já tá em produção (--retrofit) ou planejando junto com o app?"

**Patrick:** "gestor da Athié, semanal, IA tá errando muito em CPF, app rodando há meses"

**Skill:** Roda Step 2 (lê athie-docs-flow), Step 3 (ground truth check ⛔), e segue até gerar output markdown único.
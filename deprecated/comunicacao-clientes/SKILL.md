---
name: comunicacao-clientes
description: "Mensagens pra cliente via WhatsApp/Telegram. Redija, melhore, revise, planeje, estruture, corrija. Ensina frameworks (Pyramid Principle, SCQA, NVC, Chris Voss). Use SEMPRE em: 'mensagem pra cliente', 'responder cliente', WhatsApp, Telegram, 'como falo isso pro cliente', 'cliente pediu/reclamou', 'preciso cobrar/avisar atraso', 'mudança de escopo', scope creep, cobrança, pagamento, update de status, reclamação, aprovação, negociação. Diferente de tech-lead-pm: comunicação EXTERNA (clientes); tech-lead-pm = INTERNA (equipe). NÃO use para proposta comercial formal, contrato, prospecção/SDR."
---

# Comunicação com Clientes v3

**Iron Law:** Nunca envie mensagem pra cliente sem objetivo claro. Se você não sabe o que quer que o cliente **faça** depois de ler, não manda. Toda mensagem precisa de: (1) objetivo, (2) contexto mínimo, (3) ação esperada. Sem esses 3, a mensagem não sai.

## Boundary com copy

- **comunicacao-clientes** = relacionamento operacional 1:1 com cliente específico. Cobrança, update de status, mudança de escopo, aprovação, reclamação, negociação. Você sabe o nome da pessoa.
- **copy --mode whatsapp** = persuasão, conversão, broadcast marketing, vendas. Audiência ampla, não 1:1.

Se a tarefa é "responder o cliente X sobre Y" → use esta skill. Se é "escrever mensagem pra base de leads" → use `copy --mode whatsapp`.

## Options

| Option | Descrição | Default |
|--------|-----------|---------|
| `--update` | Montar update de status pro cliente | - |
| `--aprovacao` | Pedir aprovação/decisão | - |
| `--escopo` | Comunicar mudança de escopo | - |
| `--bad-news` | Comunicar notícia ruim (atraso, problema) | - |
| `--cobrar` | Cobrar resposta ou pagamento | - |
| `--reclamacao` | Responder reclamação do cliente | - |
| `--revisar` | Revisar rascunho que o usuário já escreveu | - |
| `--ensinar` | Explicar framework sem gerar mensagem | - |

## Workflow

```
Comunicacao Progress:

- [ ] Step 1: Contexto ⚠️ REQUIRED
  - [ ] 1.1 Qual o tipo? (update/aprovacao/escopo/bad-news/cobranca/reclamacao)
  - [ ] 1.2 Qual o cliente? (prioridade verde/amarelo/vermelho)
  - [ ] 1.3 Qual o objetivo da mensagem? O que o cliente deve FAZER?
  - [ ] 1.4 Quais os fatos? (sem interpretação, só dados)
- [ ] Step 2: Framework ⚠️ REQUIRED
  - [ ] 2.1 Selecionar framework adequado (ACPR, SCQA, OFNR)
  - [ ] 2.2 Se negociação: selecionar técnica Voss (mirroring/labeling/calibrated)
- [ ] Step 3: Rascunho
  - [ ] 3.1 Montar mensagem com Pyramid Principle (conclusão primeiro)
  - [ ] 3.2 Aplicar regras de formato WhatsApp/Telegram
  - [ ] ⛔ GATE: Bad news, escopo, cobrança → confirmar com usuário ANTES de sugerir envio
- [ ] Step 4: Ensino ⚠️ REQUIRED
  - [ ] 4.1 Explicar POR QUE a estrutura funciona
  - [ ] 4.2 Identificar framework usado e nomear pro usuário
  - [ ] 4.3 Perguntar "Quer ajustar algo ou tá bom pra enviar?"
- [ ] Step 5: Validação
  - [ ] 5.1 Pre-delivery checklist
```

## Filosofia

1. **Ensinar o framework, não dar o peixe.** Toda mensagem explicada. Objetivo: usuário independente em 3 meses.
2. **Mensagem enviada > mensagem perfeita.** Rascunho bom enviado hoje > mensagem linda amanhã.
3. **WhatsApp não é email.** Curto, direto, sem formalidade excessiva.
4. **Profissional não é formal.** Claro + respeitoso + direto = tom certo.
5. **Conclusão primeiro.** Cliente tá ocupado. Ponto principal na primeira linha. (Pyramid Principle)
6. **Toda mensagem tem um objetivo.** Se não sabe o que quer que o cliente faça, não manda. (Iron Law)

## Framework ACPR

Load `references/frameworks-comunicacao.md` para frameworks completos (ACPR, Pyramid, SCQA, OFNR, Voss).

**A — Abertura** (1 linha): Cumprimento + contexto rápido.
**C — Conteúdo** (2-5 linhas): Fatos, conclusão primeiro (Pyramid Principle). MECE se múltiplos pontos.
**P — Proposta/Pedido** (1-2 linhas): O que você quer que o cliente faça. Sempre dê recomendação.
**R — Reforço** (1 linha, opcional): Disponibilidade ou próximo passo.

## Tipos de Mensagem

### Tipo 1: Update de status
**Framework:** ACPR. Update proativo > reativo. Se o cliente pergunta "como tá?", você já atrasou.

### Tipo 2: Pedir aprovação/decisão
**Framework:** ACPR + opções + recomendação. Sempre recomende. "O que você prefere?" é preguiça.

### Tipo 3: Mudança de escopo
**Framework:** ACPR + técnicas de negociação. Nunca diga "não" seco. Diga "sim, e o impacto é [X]".
- **Labeling:** "Parece que essa feature é importante pra vocês por causa do [contexto]."
- **Calibrated question:** "Como você priorizaria isso em relação ao que já tá no escopo?"

### Tipo 4: Notícia ruim (atraso, problema)
**Framework:** ACPR (conclusão primeiro = notícia ruim logo). Velocidade > qualidade da notícia.
- Regra de ouro: Nunca leve só o problema. Leve junto: causa, o que já fez, plano.
- Se erro seu, use NVC-OFNR. Load `references/frameworks-comunicacao.md` para roteiro completo.

⛔ **GATE: Antes de sugerir envio de notícia ruim, pergunte: "Você já tem plano de resolução? O cliente vai querer saber o que está sendo feito."**

### Tipo 5: Cobrar resposta/pagamento
**Framework:** ACPR + escalonamento progressivo.
1. Primeira (tom normal): "Mandei [X] em [data], tô aguardando retorno."
2. Segunda (3 dias): "Reforçando — tô com [Y] parado. Preciso da resposta pra seguir."
3. Terceira (5 dias): "Sem retorno, vou pausar [projeto] até receber posicionamento."

⛔ **GATE: Antes de sugerir cobrança nível 3, confirme: "Você tem respaldo pra pausar o projeto? Já alinhou com Willy?"**

### Tipo 6: Responder reclamação
**Framework:** Validar → Assumir → Resolver → Prevenir. Não peça desculpa 5 vezes. Uma basta.

Load `references/tipos-mensagem-detalhado.md` para exemplos completos de cada tipo.

## Modo de Uso

### Quando ajudar com mensagem:
1. Pergunte tipo + contexto + fatos (Step 1)
2. Monte usando framework adequado (Step 2-3)
3. **Antes de entregar, explique a estrutura** (Step 4 — obrigatório)
4. Pergunte "Quer ajustar ou tá bom pra enviar?"

### Quando usuário parece inseguro:
Gere 2 versões: **direta** (assertiva, menos palavras) e **suave** (mais contexto, tom leve). Explique quando usar cada.

### Quando envolve negociação:
Load `references/frameworks-comunicacao.md` seção Voss. Sugira técnica específica, explique POR QUE funciona, mostre como integra no ACPR.

### Ensino progressivo:
- **1-10 usos:** Explica framework + monta mensagem
- **10-20 usos:** "Qual seria o A, C, P e R aqui?" — usuário monta, skill revisa
- **20+ usos:** Usuário manda rascunho, skill só ajusta

O objetivo é sair da skill.

### Quando usuário manda rascunho (--revisar):
1. Identifique qual framework se aplica
2. Aponte o que tá bom e o que pode melhorar (específico, não genérico)
3. Sugira versão melhorada + explique mudanças
4. Não reescreva tudo — ajuste cirúrgico

## Regras de Formato (WhatsApp/Telegram)

- Parágrafos curtos: 2-3 linhas máximo
- Uma ideia por parágrafo
- Conclusão na primeira linha
- Negrito pra destacar: *prazo*, *valor*, *decisão*
- Sem "Prezado", "Atenciosamente", "Cordialmente"
- Emojis com moderação (1-2, só se o cliente usa)
- Mais de 10 linhas? Quebre em 2 mensagens ou mande áudio

## Anti-Patterns

- **Mensagem sem objetivo** → Se você não sabe o que quer que o cliente faça, não envie. Reescreva com ação clara. (Iron Law)
- **Construir até a conclusão** → Cliente lê 2 linhas. Se a conclusão tá na linha 8, ele não viu. Comece pelo ponto principal.
- **5 opções sem recomendação** → Jogar decisão pro cliente é preguiça. Reduza pra 2-3 e recomende.
- **Desculpa em loop** → Uma desculpa basta. Depois disso, mostre plano de ação. Pedir desculpa 5x parece insegurança.
- **"Prezado Sr."** → WhatsApp não é email. Tom profissional = claro + respeitoso + direto, não formal.
- **Aceitar escopo sem comunicar impacto** → Cliente pede feature extra. Você aceita. Atrasa. Culpa sua. Sempre comunique trade-off.
- **Reagir em vez de agir** → Se o cliente precisa perguntar "como tá?", você já falhou. Update proativo sempre.
- **Resolver por texto o que precisa de call** → Se já mandou 3 mensagens sobre o mesmo assunto e não resolveu, marca call.

## Pre-Delivery Checklist

Antes de entregar qualquer mensagem ao usuário:

- [ ] Objetivo da mensagem está claro? (Iron Law)
- [ ] Conclusão/ponto principal está na primeira linha? (Pyramid Principle)
- [ ] Ação esperada do cliente está explícita?
- [ ] Formato WhatsApp/Telegram respeitado? (parágrafos curtos, sem formalidade)
- [ ] Framework usado foi explicado ao usuário? (ensino obrigatório)
- [ ] Gates de confirmação foram respeitados? (bad news, escopo, cobrança)
- [ ] Tom está adequado ao cliente? (verde = direto, amarelo = cuidadoso, vermelho = mínimo)

## Confirmation Gates

⛔ Estas situações exigem confirmação ANTES de sugerir envio:

| Situação | Perguntar antes |
|----------|----------------|
| Notícia ruim | "Você já tem plano de resolução? Qual?" |
| Mudança de escopo | "O impacto (prazo/custo) tá mapeado?" |
| Cobrança nível 3 (pausar) | "Tem respaldo pra pausar? Alinhou com Willy?" |
| Reclamação grave | "Quer responder por texto ou marcar call?" |
| Primeira mensagem a cliente novo | "Qual o histórico? Como esse cliente prefere se comunicar?" |

## Quando NÃO Usar

- **Conversa difícil com equipe** (Hygor, Jonas, Willy) → use **tech-lead-pm** módulo 4
- **Renegociar prazo com Willy** → use **tech-lead-pm**
- **Prospecção/SDR** → não coberto por nenhuma skill
- **Proposta comercial formal ou contrato** → documento, não WhatsApp
- **Criar PRD a partir de pedido do cliente** → use **product-discovery-prd** (mas pode usar esta skill pra responder o cliente dizendo "vou estruturar")
- **Dúvida sobre qual skill usar** → use **maestro**

## Integration

| Contexto | Skill | Fluxo |
|----------|-------|-------|
| Cliente manda ideia nova via WhatsApp | esta → **product-discovery-prd** | Responda "vou estruturar" (esta skill), depois faça discovery (PRD) |
| Mensagem virou conversa difícil que precisa de call | esta → **tech-lead-pm** mod. 4 | Texto não resolveu? Use roteiro de conversa difícil |
| Cliente pede feature sem justificativa | **tech-lead-pm** mod. 7 → esta | Working Backwards (tech-lead) → comunique resultado (esta) |
| Precisa decidir se é comunicação ou gestão | **maestro** → esta ou tech-lead-pm | Maestro roteia |
| Precisa planejar sequência de comunicações | esta skill sozinha | Use --ensinar pra montar plano de comunicação |
| Reporte semanal pro cliente | esta skill | Use formato ACPR com update proativo |

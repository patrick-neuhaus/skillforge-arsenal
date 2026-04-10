---
name: comunicacao-clientes
description: "Write, draft, review, improve, fix, plan, structure, and compose client messages for WhatsApp and Telegram. Teaches communication frameworks (Pyramid Principle, SCQA, NVC, Chris Voss) so the user becomes self-sufficient. Redija, melhore, revise, planeje, estruture e corrija mensagens para clientes via WhatsApp/Telegram. Use SEMPRE que mencionar: mensagem pra cliente, responder cliente, WhatsApp, Telegram, 'como falo isso pro cliente', 'o cliente pediu X', 'o cliente reclamou', 'preciso cobrar', 'preciso avisar de atraso', 'mudança de escopo', 'como dou essa notícia', scope creep, cobrança, pagamento, update de status, reclamação, aprovação, negociação com cliente. Diferente de tech-lead-pm: esta skill cuida de comunicação EXTERNA (clientes), tech-lead-pm cuida de comunicação INTERNA (equipe). NÃO use para: proposta comercial formal, contrato, prospecção/SDR, comunicação interna com equipe."
---

# Comunicacao com Clientes v3

IRON LAW: NUNCA envie mensagem pra cliente sem objetivo claro. Se voce nao sabe o que quer que o cliente FACA depois de ler, nao mande. Toda mensagem precisa de: (1) objetivo, (2) contexto minimo, (3) acao esperada. Sem esses 3, a mensagem nao sai.

## Boundary com copy

- **comunicacao-clientes** = relacionamento operacional 1:1 com cliente especifico. Cobranca, update de status, mudanca de escopo, aprovacao, reclamacao, negociacao. Voce sabe o nome da pessoa.
- **copy --mode whatsapp** = persuasao, conversao, broadcast marketing, vendas. Audiencia ampla, nao 1:1.

Se a tarefa eh "responder o cliente X sobre Y" → use esta skill. Se eh "escrever mensagem pra base de leads" → use `copy --mode whatsapp`.

## Options

| Option | Descricao | Default |
|--------|-----------|---------|
| `--update` | Montar update de status pro cliente | - |
| `--aprovacao` | Pedir aprovacao/decisao | - |
| `--escopo` | Comunicar mudanca de escopo | - |
| `--bad-news` | Comunicar noticia ruim (atraso, problema) | - |
| `--cobrar` | Cobrar resposta ou pagamento | - |
| `--reclamacao` | Responder reclamacao do cliente | - |
| `--revisar` | Revisar rascunho que o usuario ja escreveu | - |
| `--ensinar` | Explicar framework sem gerar mensagem | - |

## Workflow

```
Comunicacao Progress:

- [ ] Step 1: Contexto ⚠️ REQUIRED
  - [ ] 1.1 Qual o tipo? (update/aprovacao/escopo/bad-news/cobranca/reclamacao)
  - [ ] 1.2 Qual o cliente? (prioridade verde/amarelo/vermelho)
  - [ ] 1.3 Qual o objetivo da mensagem? O que o cliente deve FAZER?
  - [ ] 1.4 Quais os fatos? (sem interpretacao, so dados)
- [ ] Step 2: Framework ⚠️ REQUIRED
  - [ ] 2.1 Selecionar framework adequado (ACPR, SCQA, OFNR)
  - [ ] 2.2 Se negociacao: selecionar tecnica Voss (mirroring/labeling/calibrated)
- [ ] Step 3: Rascunho
  - [ ] 3.1 Montar mensagem com Pyramid Principle (conclusao primeiro)
  - [ ] 3.2 Aplicar regras de formato WhatsApp/Telegram
  - [ ] ⛔ GATE: Bad news, escopo, cobranca → confirmar com usuario ANTES de sugerir envio
- [ ] Step 4: Ensino ⚠️ REQUIRED
  - [ ] 4.1 Explicar POR QUE a estrutura funciona
  - [ ] 4.2 Identificar framework usado e nomear pro usuario
  - [ ] 4.3 Perguntar "Quer ajustar algo ou ta bom pra enviar?"
- [ ] Step 5: Validacao
  - [ ] 5.1 Pre-delivery checklist
```

## Filosofia

1. **Ensinar o framework, nao dar o peixe.** Toda mensagem explicada. Objetivo: usuario independente em 3 meses.
2. **Mensagem enviada > mensagem perfeita.** Rascunho bom enviado hoje > mensagem linda amanha.
3. **WhatsApp nao e email.** Curto, direto, sem formalidade excessiva.
4. **Profissional nao e formal.** Claro + respeitoso + direto = tom certo.
5. **Conclusao primeiro.** Cliente ta ocupado. Ponto principal na primeira linha. (Pyramid Principle)
6. **Toda mensagem tem um objetivo.** Se nao sabe o que quer que o cliente faca, nao manda. (IRON LAW)

## Framework ACPR

Load `references/frameworks-comunicacao.md` para frameworks completos (ACPR, Pyramid, SCQA, OFNR, Voss).

**A -- Abertura** (1 linha): Cumprimento + contexto rapido.
**C -- Conteudo** (2-5 linhas): Fatos, conclusao primeiro (Pyramid Principle). MECE se multiplos pontos.
**P -- Proposta/Pedido** (1-2 linhas): O que voce quer que o cliente faca. SEMPRE de recomendacao.
**R -- Reforco** (1 linha, opcional): Disponibilidade ou proximo passo.

## Tipos de Mensagem

### Tipo 1: Update de status
**Framework:** ACPR. Update proativo > reativo. Se o cliente pergunta "como ta?", voce ja atrasou.

### Tipo 2: Pedir aprovacao/decisao
**Framework:** ACPR + opcoes + recomendacao. SEMPRE recomende. "O que voce prefere?" e preguica.

### Tipo 3: Mudanca de escopo
**Framework:** ACPR + tecnicas de negociacao. Nunca diga "nao" seco. Diga "sim, e o impacto e [X]".
- **Labeling:** "Parece que essa feature e importante pra voces por causa do [contexto]."
- **Calibrated question:** "Como voce priorizaria isso em relacao ao que ja ta no escopo?"

### Tipo 4: Noticia ruim (atraso, problema)
**Framework:** ACPR (conclusao primeiro = noticia ruim logo). Velocidade > qualidade da noticia.
- Regra de ouro: Nunca leve so o problema. Leve junto: causa, o que ja fez, plano.
- Se erro seu, use NVC-OFNR. Load `references/frameworks-comunicacao.md` para roteiro completo.

⛔ **GATE: Antes de sugerir envio de noticia ruim, pergunte: "Voce ja tem plano de resolucao? O cliente vai querer saber o que esta sendo feito."**

### Tipo 5: Cobrar resposta/pagamento
**Framework:** ACPR + escalonamento progressivo.
1. Primeira (tom normal): "Mandei [X] em [data], to aguardando retorno."
2. Segunda (3 dias): "Reforcando -- to com [Y] parado. Preciso da resposta pra seguir."
3. Terceira (5 dias): "Sem retorno, vou pausar [projeto] ate receber posicionamento."

⛔ **GATE: Antes de sugerir cobranca nivel 3, confirme: "Voce tem respaldo pra pausar o projeto? Ja alinhou com Willy?"**

### Tipo 6: Responder reclamacao
**Framework:** Validar → Assumir → Resolver → Prevenir. Nao peca desculpa 5 vezes. Uma basta.

Load `references/tipos-mensagem-detalhado.md` para exemplos completos de cada tipo.

## Modo de Uso

### Quando ajudar com mensagem:
1. Pergunte tipo + contexto + fatos (Step 1)
2. Monte usando framework adequado (Step 2-3)
3. **ANTES de entregar, explique a estrutura** (Step 4 -- OBRIGATORIO)
4. Pergunte "Quer ajustar ou ta bom pra enviar?"

### Quando usuario parece inseguro:
Gere 2 versoes: **direta** (assertiva, menos palavras) e **suave** (mais contexto, tom leve). Explique quando usar cada.

### Quando envolve negociacao:
Load `references/frameworks-comunicacao.md` secao Voss. Sugira tecnica especifica, explique POR QUE funciona, mostre como integra no ACPR.

### Ensino progressivo:
- **1-10 usos:** Explica framework + monta mensagem
- **10-20 usos:** "Qual seria o A, C, P e R aqui?" -- usuario monta, skill revisa
- **20+ usos:** Usuario manda rascunho, skill so ajusta

O objetivo e SAIR DA SKILL.

### Quando usuario manda rascunho (--revisar):
1. Identifique qual framework se aplica
2. Aponte o que ta bom e o que pode melhorar (especifico, nao generico)
3. Sugira versao melhorada + explique mudancas
4. Nao reescreva tudo -- ajuste cirurgico

## Regras de Formato (WhatsApp/Telegram)

- Paragrafos curtos: 2-3 linhas maximo
- Uma ideia por paragrafo
- Conclusao na PRIMEIRA LINHA
- Negrito pra destacar: *prazo*, *valor*, *decisao*
- Sem "Prezado", "Atenciosamente", "Cordialmente"
- Emojis com moderacao (1-2, so se o cliente usa)
- Mais de 10 linhas? Quebre em 2 mensagens ou mande audio

## Anti-Patterns

- **Mensagem sem objetivo** → Se voce nao sabe o que quer que o cliente faca, nao envie. Reescreva com acao clara. (IRON LAW)
- **Construir ate a conclusao** → Cliente le 2 linhas. Se a conclusao ta na linha 8, ele nao viu. Comece pelo ponto principal.
- **5 opcoes sem recomendacao** → Jogar decisao pro cliente e preguica. Reduza pra 2-3 e recomende.
- **Desculpa em loop** → Uma desculpa basta. Depois disso, mostre plano de acao. Pedir desculpa 5x parece inseguranca.
- **"Prezado Sr."** → WhatsApp nao e email. Tom profissional = claro + respeitoso + direto, nao formal.
- **Aceitar escopo sem comunicar impacto** → Cliente pede feature extra. Voce aceita. Atrasa. Culpa sua. Sempre comunique trade-off.
- **Reagir em vez de agir** → Se o cliente precisa perguntar "como ta?", voce ja falhou. Update proativo sempre.
- **Resolver por texto o que precisa de call** → Se ja mandou 3 mensagens sobre o mesmo assunto e nao resolveu, marca call.

## Pre-Delivery Checklist

Antes de entregar qualquer mensagem ao usuario:

- [ ] Objetivo da mensagem esta claro? (IRON LAW)
- [ ] Conclusao/ponto principal esta na primeira linha? (Pyramid Principle)
- [ ] Acao esperada do cliente esta explicita?
- [ ] Formato WhatsApp/Telegram respeitado? (paragrafos curtos, sem formalidade)
- [ ] Framework usado foi explicado ao usuario? (ensino obrigatorio)
- [ ] Gates de confirmacao foram respeitados? (bad news, escopo, cobranca)
- [ ] Tom esta adequado ao cliente? (verde = direto, amarelo = cuidadoso, vermelho = minimo)

## Confirmation Gates

⛔ Estas situacoes exigem confirmacao ANTES de sugerir envio:

| Situacao | Perguntar antes |
|----------|----------------|
| Noticia ruim | "Voce ja tem plano de resolucao? Qual?" |
| Mudanca de escopo | "O impacto (prazo/custo) ta mapeado?" |
| Cobranca nivel 3 (pausar) | "Tem respaldo pra pausar? Alinhou com Willy?" |
| Reclamacao grave | "Quer responder por texto ou marcar call?" |
| Primeira mensagem a cliente novo | "Qual o historico? Como esse cliente prefere se comunicar?" |

## Quando NAO Usar

- **Conversa dificil com equipe** (Hygor, Jonas, Willy) → use **tech-lead-pm** modulo 4
- **Renegociar prazo com Willy** → use **tech-lead-pm**
- **Prospeccao/SDR** → nao coberto por nenhuma skill
- **Proposta comercial formal ou contrato** → documento, nao WhatsApp
- **Criar PRD a partir de pedido do cliente** → use **product-discovery-prd** (mas pode usar esta skill pra responder o cliente dizendo "vou estruturar")
- **Duvida sobre qual skill usar** → use **maestro**

## Integration

| Contexto | Skill | Fluxo |
|----------|-------|-------|
| Cliente manda ideia nova via WhatsApp | esta → **product-discovery-prd** | Responda "vou estruturar" (esta skill), depois faca discovery (PRD) |
| Mensagem virou conversa dificil que precisa de call | esta → **tech-lead-pm** mod. 4 | Texto nao resolveu? Use roteiro de conversa dificil |
| Cliente pede feature sem justificativa | **tech-lead-pm** mod. 7 → esta | Working Backwards (tech-lead) → comunique resultado (esta) |
| Precisa decidir se e comunicacao ou gestao | **maestro** → esta ou tech-lead-pm | Maestro roteia |
| Precisa planejar sequencia de comunicacoes | esta skill sozinha | Use --ensinar pra montar plano de comunicacao |
| Reporte semanal pro cliente | esta skill | Use formato ACPR com update proativo |

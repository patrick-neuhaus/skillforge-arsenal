---
name: comunicacao-clientes
description: "Skill de comunicação com clientes via WhatsApp/Telegram. Foco em ENSINAR o usuário a escrever melhor, não em gerar mensagens prontas. Use esta skill SEMPRE que o usuário mencionar: mensagem pra cliente, responder cliente, WhatsApp, 'como falo isso pro cliente', 'o cliente pediu X', 'o cliente reclamou', 'preciso cobrar', 'preciso avisar de atraso', 'mudança de escopo', 'como dou essa notícia', ou qualquer variação que envolva comunicação externa com clientes. Também use quando o usuário pedir ajuda pra escrever qualquer mensagem profissional — mesmo que não diga 'cliente' explicitamente. Se o contexto for conversa difícil INTERNA (com equipe, com Willy), use a skill de Tech Lead & PM em vez desta. Se é proposta comercial formal ou contrato, não é WhatsApp — é documento, fora do escopo desta skill."
---

# Comunicação com Clientes v2

## Visão geral

O usuário comunica com clientes por WhatsApp/Telegram. O problema dele não é tom — é velocidade. Ele sabe o que quer dizer mas fica reescrevendo demais. O objetivo desta skill é ENSINAR frameworks de comunicação pra ele internalizar e ficar independente, não gerar mensagens prontas pra copiar e colar.

### Novidades na v2

- **Pyramid Principle (Barbara Minto)** — Conclusão primeiro pra mensagens async
- **SCQA** — Framework narrativo pra comunicações complexas
- **NVC (Rosenberg)** — OFNR pra conversas difíceis com cliente (cobrança, scope creep)
- **Técnicas de negociação (Chris Voss)** — Mirroring, labeling, calibrated questions
- **WhatsApp Business patterns** — Templates de utilidade, open rates

## Filosofia

1. **Ensinar o framework, não dar o peixe.** Toda vez que ajudar com mensagem, explique POR QUE a estrutura funciona. O objetivo é que em 3 meses ele não precise mais da skill.
2. **Primeiro a mensagem funcional, depois o polimento.** Mensagem enviada > mensagem perfeita no rascunho.
3. **WhatsApp não é email.** Mensagens curtas, parágrafos de 2-3 linhas, sem formalidade excessiva.
4. **Profissional não é formal.** Tom profissional no WhatsApp = claro, respeitoso, direto.
5. **Toda mensagem tem um objetivo.** Se você não sabe o que quer que o cliente FAÇA depois de ler, não mande ainda.
6. **Conclusão primeiro.** O cliente tá ocupado. Diga o ponto principal na primeira linha, depois dê contexto. Não construa até a conclusão — comece por ela. (Referência: Pyramid Principle — Barbara Minto) (NOVO v2)

## O framework ACPR

Todo tipo de mensagem segue uma variação do mesmo framework:

**A — Abertura** (1 linha)
Cumprimento + contexto rápido. O cliente sabe em 3 segundos do que se trata.
- "Fala [nome], tudo bem? Passando update do projeto X."

**C — Conteúdo** (2-5 linhas)
O que você precisa comunicar. Fatos, não opinião. Específico, não vago.
- Ruim: "Tivemos alguns probleminhas"
- Bom: "A integração com o Kommo atrasou 2 dias porque a API deles mudou o formato do webhook"

**P — Proposta / Pedido** (1-2 linhas)
O que você quer que o cliente faça.
- "Preciso da sua aprovação pra seguir com a opção A"
- "Não precisa fazer nada, só te mantendo no loop"

**R — Reforço** (1 linha, opcional)
Disponibilidade ou próximo passo.
- "Qualquer dúvida, me chama"

### Pyramid Principle no ACPR (NOVO v2)

A mudança mais importante da v2: o **C (Conteúdo)** segue a Pyramid Principle de Barbara Minto — conclusão primeiro, depois argumentos de suporte.

**Antes (v1):**
"A API do Kommo mudou o formato do webhook. Isso fez a integração quebrar. Tive que refazer o parser. Isso atrasou 2 dias."

**Depois (v2):**
"A integração atrasou 2 dias. Motivo: API do Kommo mudou o webhook sem aviso. Fix já aplicado."

A diferença: o cliente leu "atrasou 2 dias" na primeira frase e já sabe a situação. O resto é contexto — pode ler ou não.

**Regra MECE no Conteúdo:** Se tem múltiplos pontos, organize sem sobreposição (Mutually Exclusive) e sem deixar nada de fora (Collectively Exhaustive):
- "Temos 3 itens pendentes: (1) integração Kommo, (2) tela de relatórios, (3) deploy em produção."

### SCQA pra comunicações complexas (NOVO v2)

Quando ACPR não é suficiente (situações que precisam de contexto narrativo), use SCQA:

- **Situation:** "O projeto X tá na reta final, com 80% entregue."
- **Complication:** "O cliente pediu 3 features novas que não estavam no escopo."
- **Question:** "O que priorizamos: entregar no prazo sem as features, ou estender?"
- **Answer:** "Recomendo entregar no prazo e orçar as features como fase 2."

SCQA funciona melhor pra: propostas, explicações de trade-off, comunicações onde precisa convencer.

## Tipos de mensagem

### Tipo 1: Update de status

**Framework:** ACPR (conclusão primeiro no C)

**Princípio:** Update proativo > update reativo. Se o cliente precisa PERGUNTAR "como tá?", você já atrasou.

**Cadência:** Semanal ou por entrega, o que vier primeiro.

**Erro comum:** Update longo demais. O cliente quer saber se tá andando e quando recebe.

### Tipo 2: Pedir aprovação/decisão

**Framework:** ACPR com opções + recomendação

**Princípio:** SEMPRE dê sua recomendação. "O que você prefere?" é preguiça. "Recomendo A porque [motivo]" é liderança.

**Erro comum:** 5 opções sem recomendação. Reduza pra 2-3 e recomende.

### Tipo 3: Mudança de escopo

**Framework:** ACPR + técnicas de negociação

**Princípio:** Nunca diga "não" seco. Diga "sim, e o impacto é [X]".

**Com técnicas de Voss (NOVO v2):**
- **Labeling:** "Parece que essa feature é importante pra vocês por causa do [contexto]." (valida sem concordar)
- **Calibrated question:** "Como você priorizaria isso em relação ao que já tá no escopo?" (faz o cliente pensar no trade-off)

**Erro comum:** Aceitar mudança sem comunicar impacto.

### Tipo 4: Notícia ruim (atraso, problema)

**Framework:** ACPR (conclusão primeiro = a notícia ruim vem logo)

**Princípio:** Velocidade de comunicação > qualidade da notícia. Avisar terça com solução parcial > avisar sexta com solução completa.

**Regra de ouro:** Nunca leve só o problema. Sempre leve junto: o que causou, o que já fez, e qual o plano.

**Com NVC — OFNR (NOVO v2):**
Se a notícia ruim é delicada (atraso por erro seu):
1. **Observation:** "O prazo da integração era sexta e não vai dar."
2. **Feeling:** "Fico desconfortável de comunicar isso."
3. **Need:** "Preciso de transparência contigo pra manter confiança."
4. **Request:** "O novo prazo é terça. Posso te dar update diário até lá?"

NVC humaniza. Não é fraqueza — é maturidade.

### Tipo 5: Cobrar resposta/pagamento

**Framework:** ACPR + escalonamento progressivo

**Princípio:** Cobrar não é ser chato. Cobrar é ser profissional.

**Escalonamento:**
1. Primeira (tom normal): "Mandei [X] em [data], tô aguardando retorno."
2. Segunda (3 dias): "Reforçando — tô com [Y] parado. Preciso da resposta pra seguir."
3. Terceira (5 dias): "Sem retorno, vou pausar [projeto] até receber posicionamento."

**Com técnicas de Voss (NOVO v2):**
- **Mirroring:** Se cliente diz "tô corrido", repita: "...corrido?" → ele vai elaborar e talvez revelar o real motivo
- **Labeling:** "Parece que tem algo travando do lado de vocês." → valida sem acusar
- **Calibrated question:** "O que seria necessário pra destravar isso essa semana?" → faz ele propor solução

### Tipo 6: Responder reclamação

**Framework:** ACPR com estrutura Validar → Assumir → Resolver → Prevenir

**Princípio:** Reclamação é presente. O que sai sem reclamar é pior.

1. **Valide:** "Entendo sua frustração. Faz sentido."
2. **Assuma:** "Isso foi falha nossa em [específico]"
3. **Resolva:** "Vou fazer [ação] até [data]"
4. **Previna:** "Pra não acontecer de novo, vamos [mudança]"

Não peça desculpa 5 vezes. Uma basta.

## Modo de uso da skill

### Quando o usuário pedir ajuda com mensagem:

1. Pergunte: "Qual o tipo? (update, aprovação, escopo, notícia ruim, cobrança, reclamação)"
2. Pergunte: "Qual o contexto? Me dá os fatos"
3. Monte a mensagem usando ACPR (com Pyramid Principle no conteúdo)
4. ANTES de entregar, **explique a estrutura**: "Abri com X porque [motivo], conteúdo é Y com conclusão primeiro porque [motivo], pedi Z porque [motivo]"
5. Entregue a mensagem
6. Pergunte: "Quer ajustar algo ou tá bom pra enviar?"

### Quando o usuário parecer inseguro:

Gere 2 versões:
- **Versão direta**: Mais assertiva, menos palavras
- **Versão suave**: Mais contexto, tom mais leve

Explique a diferença e QUANDO usar cada uma.

### Quando a situação pedir negociação (NOVO v2):

Se o contexto envolve conflito, resistência, ou negociação (scope creep, pagamento, insatisfação):
1. Sugira técnicas específicas de Voss: mirroring, labeling, ou calibrated questions
2. Explique POR QUE cada técnica funciona naquele contexto
3. Mostre como integrar no ACPR
4. Se for conversa por call (não texto), sugira roteiro verbal com as técnicas

### Ensino progressivo:

- Primeiras vezes: explica ACPR + Pyramid + monta a mensagem
- Depois de 5-10 usos: "Qual seria o A, C, P e R aqui?" — ele monta, você revisa
- Depois de 20 usos: ele manda rascunho e você só ajusta

O objetivo é SAIR DA SKILL.

## Regras de formato (WhatsApp/Telegram)

- Parágrafos curtos: 2-3 linhas máximo
- Uma ideia por parágrafo
- Conclusão/ponto principal na PRIMEIRA LINHA (Pyramid Principle)
- Use negrito pra destacar: *prazo*, *valor*, *decisão*
- Sem "Prezado", "Atenciosamente", "Cordialmente" — isso é email
- Emojis com moderação (1-2 por mensagem, só se o cliente usa)
- Se ficou com mais de 10 linhas, quebre em 2 mensagens ou mande áudio

## Quando NÃO usar esta skill

- Conversa difícil com equipe (Hygor, Jonas) → use skill de Tech Lead & PM
- Renegociar prazo com o Willy → use skill de Tech Lead & PM
- Prospecção/SDR → não coberto
- Mensagem que precisa de tom formal (contrato, proposta) → isso é documento, não WhatsApp

## Integração com outras skills

- **Tech Lead & PM (Módulo 7 - Stakeholders):** Working Backwards funciona quando cliente pede feature sem justificativa
- **Tech Lead & PM (Módulo 4 - Conversas difíceis):** Se a mensagem virar conversa difícil que precisa de call, use módulo 4. As técnicas de Voss e NVC são as mesmas — a diferença é o canal (texto vs voz).
- **Product Discovery & PRD:** Se cliente manda ideia nova via WhatsApp, diga "boa ideia, vou estruturar e te mando proposta" e use a skill de PRD

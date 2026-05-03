<!--
  copy-whatsapp.md — Estrutura WhatsApp + Chris Voss + PIX urgencia + LGPD opt-in + Click-to-WA BR + Telegram + Kwai NE
  Carregado em: tasks de copy pra WhatsApp (broadcast/drip/Click-to-WA), Telegram, vendas conversacional BR
  v3 — 2026-05-03 (Wave 3: PIX urgencia + LGPD opt-in + Click-to-WhatsApp BR + Telegram nicho + Kwai NE + WhatsApp Business API rules)
-->

# Copy — WhatsApp & Vendas Conversacional

**Referencias:** Chris Voss (Never Split the Difference), Alan Weiss, WhatsApp Business API, LGPD

## Por que WhatsApp e diferente (BR-specific)

- **97% dos usuarios de internet brasileiros usam WhatsApp diariamente** (Brasil = #1 mundo)
- 82% ja se comunicaram com empresas via WhatsApp
- 54% ja compraram via app (71% pagando com Pix)
- 98% open rate vs ~20% email
- Canal de conversa, nao broadcast — tom muda tudo
- Expectativa de resposta rapida: 87% esperam retorno em ate 24h
- Mensagem longa = ignorada. Fragmentar e a norma no canal.

---

## WhatsApp Business API — Broadcast vs Conversa (NOVO v3)

Regulado por Meta. Distincao critica:

| Tipo | Regra | Limite |
|---|---|---|
| **Template message** (broadcast) | Aprovacao previa Meta obrigatoria | 100 msgs/paciente/dia (BR) |
| **Conversa livre** (resposta) | Sem aprovacao, dentro de janela 24h pos-interacao do user | Sem limite numerico |

**Pratica:**
- Template messages = notificacoes/transacionais (confirmacao pedido, lembrete evento)
- Conversa livre = vendas, suporte, follow-up
- Estouro do limite = bloqueio temporario da conta

**Copy de templates:**
- Conciso (1-2 frases)
- CTA claro ("responda SIM para confirmar")
- Sem spam (Meta penaliza taxa de bloqueio)
- Variaveis dinamicas pra personalizacao ({{nome}}, {{produto}})

---

## Estrutura de Mensagem WhatsApp

```
1. Saudacao personalizada
   → use o nome, contexto de onde vieram

2. Contexto / gancho
   → por que voce esta mandando agora (trigger ou referencia)

3. Proposta de valor em 1-2 linhas
   → o que voce oferece + beneficio principal

4. Prova rapida
   → 1 dado concreto ou referencia a cliente similar

5. CTA conversacional
   → pergunta binaria (sim/nao) ou acao simples
```

**Exemplo:**
```
Oi [Nome]! 👋

Vi que voces acabaram de lancar [produto/servico] — parabens!

Ajudei a [Empresa Similar] a reduzir o tempo de atendimento em 40%
com automacao de WhatsApp Business.

Faria sentido mostrar como funcionaria pra voces em 15 minutos?
```

---

## Principios Chris Voss (Never Split the Difference)

Voss e ex-negociador FBI — principios se aplicam direto em vendas conversacional:

| Tecnica | O que e | Como usar no WhatsApp |
|---------|---------|----------------------|
| **Tactical Empathy** | Reconheca o estado emocional antes de propor solucao | "Imagino que voces estao sobrecarregados com isso..." |
| **Mirroring** | Repita as ultimas 2-3 palavras como pergunta | "...sobrecarregados com atendimento?" |
| **Labeling** | Nomeia o sentimento implicito | "Parece que a equipe esta sentindo pressao por volume..." |
| **Calibrated Questions** | "Como" e "o que" em vez de "sim/nao" | "Como voces estao lidando com o volume hoje?" |
| **The Late-Night FM DJ Voice** | Tom calmo, baixo, controlado (escrita: frases curtas, pausas) | Frases curtas. Pontos. Sem urgencia excessiva. |
| **No-oriented questions** | Perguntas que deixam o cliente dizer "nao" com seguranca | "Seria um problema dedicar 15 minutos pra isso?" |

---

## PIX como Urgencia (NOVO v3) 🔥

PIX = sistema de pagamento instantaneo Banco Central. **71% das compras via WhatsApp BR sao pagas com Pix.**

### Padroes de copy com PIX

**Urgencia + desconto:**
- "Pague via Pix e garanta 10% OFF agora"
- "Deposito via Pix = entrega imediata"
- "So hoje: -15% se pagar via Pix em ate 24h"

**Conversao instant:**
- "Pix copia e cola: chave [chave]. Mando o produto em 5 min"
- "Faz o Pix e me manda o comprovante. Libero acesso na hora"

### Por que funciona

- Reduz friccao (sem cartao, sem digito CVV)
- Cliente ja tem app do banco aberto
- Confirmacao instantanea = sem ansiedade pos-pagamento
- "Pix" virou verbo no Brasil ("vou te pixar")

### Quando usar

- ✅ Promocoes flash (24-48h)
- ✅ Vendas WhatsApp 1:1
- ✅ Click-to-WhatsApp ads com checkout simples
- ⚠️ B2B enterprise: nem sempre (procurement quer fatura/boleto)

---

## LGPD — Opt-in Claro (NOVO v3)

Lei 13.709/2018. Marketing digital BR exige consentimento explicito.

### Regras de copy LGPD

**Opt-in claro:**
- Sem pre-checked boxes
- Linguagem transparente: "cadastre-se livremente, respeitamos sua privacidade"
- Aviso: "Seus dados serao protegidos conforme LGPD"

**Funil padrao BR:**
> "Posso falar com voce no WhatsApp e e-mail?"
> [Sim, pode] [Nao, obrigado]

**Anti-padroes (LGPD violation):**
- ❌ Box pre-marcada "Quero receber promocoes"
- ❌ "Aceito" gigante + "Recusar" minusculo (dark pattern)
- ❌ Sem opcao de recusar
- ❌ Continuar enviando apos opt-out

### Documento de consentimento

Forms BR sempre incluem:
```
[ ] Concordo em receber mensagens via WhatsApp e e-mail
[ ] Aceito a Politica de Privacidade [link]
[ ] Concordo com os Termos de Uso [link]

Voce pode cancelar a qualquer momento.
```

⚠️ **ANPD pode multar até 2% do faturamento** por LGPD violation. Copy compliante nao e opcional.

---

## Click-to-WhatsApp Ads (BR domina globalmente) NOVO v3 🔥

Brasil lidera mundialmente esse formato. Anuncios FB/IG/Google com botao "Enviar Mensagem no WhatsApp".

### Padroes copy ad

```
[Headline 40 chars]: pergunta provocativa
[Body 125 chars]: contexto + beneficio + chamada
[CTA button]: "Enviar mensagem"
```

**Hooks que funcionam:**
- "Cansado de [problema]? Fale conosco no WhatsApp"
- "Receba [valor] em minutos via WhatsApp"
- "Solucao pra [persona] — chama no Zap"
- "Problemas pra [task]? Conta pra gente no WhatsApp"

### Saudacao automatica (chatbot 1ª resposta)

Personalize com nome OU referencia da campanha:
```
Oi! Vi que voce veio pelo anuncio de [campanha].
Pra te ajudar melhor, pode me dizer [pergunta especifica]?
```

NAO use:
```
"Bem vindo! Nosso atendimento esta disponivel..."
[generico, soa robo]
```

### Tipo de produto que vence

- ✅ Servicos locais (clinicas, salao, restaurante)
- ✅ Infoprodutos baixo-medio ticket
- ✅ Imobiliarias / corretores
- ✅ Cursos online
- ⚠️ B2B SaaS: depende — funciona pra autonomos, nao corporate

---

## Sequencias drip (Z-API, Evolution API)

Fluxos automaticos via WhatsApp pra nutricao.

### Padrao escalavel

- Tom informal e breve (mensagens longas = canceladas)
- Ciclos de 3-5 mensagens sobre mesmo tema (educacao OU oferta)
- Espacadas em 1-2 dias
- Combinar texto + midia (imagem ou audio curto)
- Gatilho de resposta ("responda OK pra saber mais")

### Estrutura tipica

```
Msg 1: Saudacao pessoal ("Oi! Aqui e [nome] da [empresa], tudo bem?")
Msg 2: Conteudo (dica, depoimento de cliente similar)
Msg 3: CTA suave ("Posso te enviar mais info?")
Msg 4: Caso de sucesso (1 cliente real, 1 numero)
Msg 5: Oferta + Pix urgencia ("Pague hoje via Pix, ganha [bonus]")
```

⚠️ **Cuidado:** taxa de bloqueio alta = banimento Meta. Segmente bem antes de disparar drip.

---

## Telegram — Canal de Nicho BR (NOVO v3)

Ainda nicho no Brasil (vs WhatsApp dominante). Usado em:

- Cripto/financas
- Cursos high-ticket (mentoria, mastermind)
- Comunidades VIP (palestrantes, influencers)
- Grupos privados de afiliados

### Padroes copy Telegram

- Tom de "segredo"/exclusividade: "So quem esta nesse grupo vai ter desconto especial"
- Conteudo exclusivo (nao replicar Insta/WA)
- Audios + videos longos (toleram melhor que WhatsApp)
- Botoes inline pra navegacao
- Bots conversacionais (nao texto livre)

### Quando usar Telegram

- ✅ Lancamento high-ticket (mentoria, mastermind)
- ✅ Comunidade VIP de alunos
- ✅ Drops exclusivos (cripto, afiliados)
- ⚠️ B2C massa: NAO, audiencia nao tem
- ⚠️ Local services: NAO, audiencia nao tem

---

## Kwai vs TikTok no NE/Norte (NOVO v3)

Brasil tem 2 plataformas video curto: TikTok (urbano, classes B/C) + Kwai (interior, classes C/D).

### Kwai — diferencas vs TikTok

- Sistema de recompensas em dinheiro (gamificacao)
- Conteudo local mais forte
- Audiencia: NE, interior, classes C-D
- Tom: ainda mais coloquial que TikTok

### Quando segmentar Kwai

- ✅ Infoprodutos populares (R$47-R$297)
- ✅ Servicos massa pra interior
- ✅ Mercados emergentes (NE, Norte)
- ✅ Audiencia 30+ classes C-D
- ⚠️ B2B / corporativo: NAO, audiencia nao tem
- ⚠️ Premium / aspiracional: NAO, audiencia nao bate

### Padroes copy Kwai

- Influencers locais comentando ("Vem ganhar dinheiro no Kwai!")
- Demonstracao de uso real (nao aspiracional)
- Promessa de recompensa direta ("Ganhe X assistindo Y")
- Tom mais quente que TikTok

---

## Erros Fatais no WhatsApp

| Erro | Por que destroi | Como evitar |
|------|----------------|-------------|
| **Muro de texto** | Ninguem le mais que 3 linhas | Fragmentar em mensagens curtas ou bullets |
| **Tom formal** | Canal e informal — "prezado" soa errado | Escrita conversacional, use o nome |
| **Spam sem segmentacao** | Queima lista, gera bloqueios, afeta score Meta | Segmentar por contexto/interesse antes de enviar |
| **Nao responder rapido** | 87% esperam resposta rapida; demora = desinteresse | SLA de resposta + automacao para primeiras respostas |
| **Vender antes de conversar** | WhatsApp e conversa, nao catalogo | Faca pergunta antes de fazer oferta |
| **Links logo de cara** | Parece phishing ou spam automatico | Construa contexto antes de qualquer link |
| **Sem opt-in claro (LGPD)** | Multa ANPD ate 2% faturamento | Forms LGPD-compliant sempre |
| **Texto so, sem Pix** | Perde conversao | Sempre oferecer Pix em compras BR |

---

## Sequencia de Follow-up Conversacional

```
Mensagem 1 — Abordagem inicial (contexto + gancho)
Mensagem 2 — Dia 2-3 (novo angulo, nao "so queria saber")
Mensagem 3 — Dia 6-7 (valor concreto — insight ou case)
Mensagem 4 — Dia 14 (breakup: "pode fechar esse contato?")
```

---

## Quando usar cada formato

| Formato | Quando |
|---------|--------|
| Texto curto (1-3 linhas) | Primeiro contato, follow-up, confirmacao |
| Audio | Relacionamento ja estabelecido, mensagem complexa |
| Video curto | Demo, prova rapida, apresentacao de oferta |
| Documento/PDF | Proposta formal, apos interesse confirmado |
| Lista com bullets | Resumo de pontos, nao abertura |
| Pix copia e cola | Compra fechada, entrega imediata |

---

## CTA Conversacional vs CTA Direto

**CTA direto (funciona em email/ads):**
> "Compre agora com 20% de desconto"

**CTA conversacional (funciona em WhatsApp):**
> "Faria sentido ver como funcionaria pra voces?"
> "Consigo reservar 20 minutos essa semana — terca ou quarta funciona?"
> "Posso te enviar o caso da [Empresa Similar] pra dar uma olhada?"
> "Quer fazer o Pix agora ou prefere segunda?"

Perguntas binarias (terca ou quarta? sim ou nao? faz sentido?) reduzem friccao cognitiva e aumentam taxa de resposta.
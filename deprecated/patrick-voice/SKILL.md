---
name: patrick-voice
description: "Escreve textos no tom Patrick (PT-BR informal) via discovery interativo. Faz perguntas pra entender o que tu quer (melhorar msg existente, criar do zero, responder msg recebida, continuar thread), pra quem (equipe, cliente, grupo, rede, claude code), e calibra o registro automaticamente. Use quando tu disser \"escreve igual eu\", \"no meu tom\", \"minha voz\", \"como o Patrick falaria\", \"responde como eu\", \"redige no estilo Patrick\", \"melhora essa msg pra soar como eu\" ou pedir output em portugues brasileiro reconhecivel como dele. Triggers PT-BR: \"tom patrick\", \"voz patrick\", \"estilo patrick\", \"fala como eu\", \"responde como eu\", \"escreve no meu tom\", \"melhora no meu tom\", \"no estilo do patrick\", \"patrick voice\". Voice DNA destilada de corpus real (Claude Code sessions + WhatsApp 90 dias) — NAO usar pra outras pessoas."
---

# patrick-voice

> Escreve textos com a voz do Patrick. Discovery interativo via AskUserQuestion antes de gerar.

## IRON LAW

**SEMPRE faz discovery via AskUserQuestion ANTES de gerar texto.** Nunca gera output sem ter perguntado: (1) o que quer fazer, (2) pra quem/qual canal, (3) contexto extra. Pular discovery = output generico fora do tom.

## Quando usar

- Patrick pede output "no meu tom", "como eu falaria", "igual eu"
- Patrick pede pra responder mensagem recebida (WhatsApp, email, post)
- Patrick pede pra melhorar mensagem que ele escreveu
- Patrick pede pra continuar uma thread/conversa
- Patrick pede pra redigir comunicado, anuncio, msg pra cliente/equipe

## Quando NAO usar

- Texto generico sem tom pessoal (use copy)
- Texto que vai ser assinado por equipe ou outra pessoa
- Documentacao tecnica seca (use docs)

## Workflow

### Step 1 — Discovery via AskUserQuestion ⚠️ REQUIRED ⛔ BLOCKING

Faz perguntas pra entender o pedido. Limite por chamada AskUserQuestion = 4 questoes. **Pode concatenar quantas chamadas precisar pra entender bem.** Nao tem limite total de perguntas, so de 4 por batch.

#### Bateria 1 — Intent (sempre faz)

```
Q1: O que tu quer fazer?
  A) Criar do zero (texto novo)
  B) Melhorar mensagem que tu rascunhou
  C) Responder mensagem que tu recebeu
  D) Continuar uma thread/conversa

Q2: Pra quem e?
  A) Claude Code / agentes IA (tech)
  B) Equipe direta (Hygor/Jonas/Enzo/Vitor/Yuri/Julios)
  C) Cliente (Lucca, GABAMO, Athie, etc)
  D) Grupo profissional (Artemis IA, Hefesto, Supply MEP)

Q3: Qual tom geral?
  A) Direto, sem rodeio (default)
  B) Mais casual/amigo (intimo)
  C) Formal mas reconhecivel (cliente novo, mentor)
  D) Cobranca/confronto (algo travado, problema)

Q4: Tem contexto extra que ajuda? (cola aqui via "Other" se sim)
  A) Nao, ja te passei tudo
  B) Sim, vou colar context
  C) Tem msg anterior na thread (cola)
  D) Tem prazo/urgencia que muda registro
```

#### Bateria 2 — Conditional (so se Q1 nao foi "Criar do zero")

Se Q1 = "Melhorar":
```
Q1: Cola aqui o rascunho que tu escreveu (use "Other" e cola texto)
Q2: O que ta pegando no rascunho?
  A) Ta longo demais, encurta
  B) Ta formal demais
  C) Ta ambiguo, deixa mais direto
  D) Outra coisa (descreve)
```

Se Q1 = "Responder":
```
Q1: Cola aqui a mensagem que tu recebeu
Q2: Tu quer:
  A) Responder direto e fechar assunto
  B) Responder pedindo mais info
  C) Responder confirmando
  D) Responder discordando/questionando
```

Se Q1 = "Continuar thread":
```
Q1: Cola as ultimas 2-3 mensagens da thread
Q2: Tu quer:
  A) Manter o tom da thread
  B) Mudar registro (ex: subir nivel de cobranca)
  C) Encerrar a thread
  D) Mudar de assunto na mesma thread
```

#### Bateria 3 — Conditional (especifica de canal)

Se Q2 = "Cliente":
```
Q1: Qual cliente especifico?
  A) Cliente novo (mais respeitoso)
  B) Cliente recorrente conhecido
  C) Cliente em problema (cobranca pra eles)
  D) Cliente cobrando a gente (resposta)
```

Se Q2 = "Grupo profissional":
```
Q1: Tipo de mensagem em grupo?
  A) Anuncio/update unilateral
  B) Decisao em grupo (busca opiniao)
  C) Resposta a alguem que falou
  D) Encerramento de assunto/thread
```

#### Quando perguntar mais

- Se Patrick mencionar pessoa pelo nome mas nao ficou claro qual relacao (cliente vs equipe?), pergunta
- Se Patrick disser "responder" mas nao colou a msg, pergunta
- Se intent tiver 2+ interpretacoes possiveis, pergunta

**Nunca chuta. Sempre confirma com AskUserQuestion.**

### Step 2 — Mapeia respostas pra canal interno

Depois das perguntas, mapeia mentalmente:
- Q2 resposta → canal (tech/equipe/cliente/grupo/rede/geral)
- Q3 resposta → modulador de tom dentro do canal
- Q1 + colado (se houver) → tipo de output (criar, melhorar, responder, continuar)

### Step 3 — Carrega Voice DNA

Le `references/voice-dna.md` integralmente. Esse arquivo tem padroes universais + diferenciais por canal.

### Step 4 — Aplica calibracao

Pega regras do canal mapeado:
- Comprimento medio
- Saudacao apropriada (ou nenhuma)
- Vocabulario do canal (palavroes em tech, neutro em cliente)
- Marcadores especificos
- Fechamento

### Step 5 — Gera output

Escreve seguindo:
- Padroes universais do voice-dna.md (sempre)
- Diferenciais do canal mapeado (sempre)
- Tom modulador da Q3 (subir/descer intensidade)
- Examples de `references/examples.md` como guia (consulta se precisar)

### Step 6 — Auto-check (anti-IA) ⚠️ REQUIRED

Antes de entregar, verifica se NAO tem:
- "Perfeito! Vou..." / "Excelente!" / "Fantastico!" isolados
- "Por gentileza", "fico no aguardo", "agradeço a atenção" (exceto cliente novo)
- Hedge longo ("talvez fosse interessante considerar a possibilidade...")
- Emoji decorativo
- Filler corporativo

Se tem, reescreve.

### Step 7 — Entrega + check de acerto

Mostra output pro Patrick e pergunta:
```
Q1: Ficou no tom?
  A) Sim, manda assim
  B) Quase, ajusta um pouco (descreve)
  C) Nao soou como eu, refaz
  D) Quero variar, gera outra versao
```

Se nao ficou, volta pro Step 5 com feedback.

## IRON LAWS internas

### IL-1 — NAO copiar texto literal do corpus

Voice DNA descreve PADROES, nao quotes. Geracao precisa SOAR como Patrick, nao reciclar frases que ele escreveu.

### IL-2 — Discovery primeiro, sempre

Pular AskUserQuestion = falha. Mesmo se o pedido parecer obvio, pelo menos UMA bateria de perguntas. Em duvida, mais perguntas > menos.

### IL-3 — Patrick NUNCA usa filler corporativo

"Perfeito!" / "Excelente!" / "Fantastico!" isolados sao tracos de IA. Patrick usa "perfeito" so como ack curto ("perfeito, manda"), nunca como abertura emocional.

### IL-4 — Erros de digitacao sao parte da voz

Em tech/equipe Patrick nao corrige typos. Acentuacao omitida ("nao", "ja", "voce"). Capitalizacao baixa. Em cliente capitaliza inicio de frase + acentua mais. Aplicar registro coerente com canal mapeado.

### IL-5 — Quando irritado em tech, escala em 4 niveis

1. Pergunta neutra
2. Pergunta com friccao
3. ALL CAPS + palavrao + "filho"
4. Reset: "pega tudo q vc fez e desfaz"

Nao pula degraus aleatoriamente.

## Anti-padroes (NAO faca)

1. Comeca com "Olá" ou "Oi tudo bem?" em tech ou equipe
2. Termina com "Atenciosamente" ou "Obrigado pela compreensao"
3. Usa emoji em excesso (>1 por mensagem em geral)
4. Hedge antes de opinar ("acho que talvez seria interessante...")
5. Escreve frase longa quando fragments servem
6. Inventa giria que Patrick nao usa (ex: "mano" raro, "bro" zero, "trampar" zero)
7. Misturar canal (palavrao em msg pra cliente)
8. Capitalizar tudo direito quando contexto e tech informal
9. **Pular discovery e adivinhar canal** (fura IL-2)
10. **Limitar perguntas a 4 quando precisa de mais** — pode concatenar baterias

## Examples antes/depois (resumo)

Ver `references/examples.md` pra examples completos por canal. Quick reference:

**Tech (Claude Code):**
- Generico: "Por favor, execute os testes e em seguida faça o commit das alterações."
- Patrick: "roda os testes, se passar commita. se quebrar me fala antes."

**Equipe:**
- Generico: "Olá Hygor, você poderia verificar a task X quando tiver disponibilidade?"
- Patrick: "fala [DEV_1], olha a X ai pra mim quando puder. urgente nao mas hoje se der."

**Grupo:**
- Generico: "Bom dia equipe, gostaria de informar que..."
- Patrick: "Bom dia turma! Update rapido: [info]. Faz sentido pra voces?"

**Cliente:**
- Generico: "Prezado, gostaria de agradecer pela paciência..."
- Patrick: "Boa tarde [CLIENTE]! Tudo certo? Atualizando aqui: [info]. Qualquer coisa me chama."

**Rede (mentor):**
- Generico: "Olá [MENTOR], espero que esteja bem..."
- Patrick: "Salve [MENTOR_1], tudo tranquilo? Queria trocar uma ideia rapida sobre [tema]."

## Boundary com outras skills

Ver `references/boundary-notes.md`. Resumo:
- **copy** — copy generica cross-cliente. patrick-voice = pessoal Patrick.
- **comunicacao-clientes** — estrutura mensagens cliente. Compoe com patrick-voice (estrutura + tom).
- **prompt-engineer** — meta-skill pra prompts LLM. Diferente registro.

## Maintenance

- Voice DNA destilada em 2026-05-05 de corpus 90 dias (Claude + WhatsApp Evolution).
- Re-destilar quando: estilo Patrick mudar, novos canais relevantes, gaps detectados.
- Re-destilacao: rodar pipeline em `voice-skill-build/` (extract -> redact -> sample -> distill).
- Lock-in: se marcada como `validated:YYYY-MM-DD` em FIXES-APLICADOS.md, IL-10 aplica.

# Frameworks de Comunicacao — Referencia

Este arquivo contem os frameworks completos que a skill usa. Nao sao templates pra copiar — sao estruturas pra entender e internalizar.

---

## Framework ACPR (Principal)

Todo tipo de mensagem segue uma variacao do ACPR:

**A — Abertura** (1 linha)
Cumprimento + contexto rapido. O cliente sabe em 3 segundos do que se trata.
- "Fala [nome], tudo bem? Passando update do projeto X."
- "Oi [nome], sobre aquele ponto da reuniao de ontem."

**C — Conteudo** (2-5 linhas)
O que voce precisa comunicar. Fatos, nao opiniao. Especifico, nao vago. Conclusao PRIMEIRO.
- Ruim: "Tivemos alguns probleminhas"
- Bom: "A integracao com o Kommo atrasou 2 dias porque a API deles mudou o formato do webhook"
- Regra MECE: se tem multiplos pontos, organize sem sobreposicao e sem deixar nada de fora.

**P — Proposta / Pedido** (1-2 linhas)
O que voce quer que o cliente faca. SEMPRE de recomendacao.
- "Preciso da sua aprovacao pra seguir com a opcao A"
- "Nao precisa fazer nada, so te mantendo no loop"
- "Recomendo A porque [motivo]. Se preferir B, o trade-off e [X]."

**R — Reforco** (1 linha, opcional)
Disponibilidade ou proximo passo.
- "Qualquer duvida, me chama"
- "Proximo update: sexta de tarde"

---

## Pyramid Principle (Barbara Minto)

A mudanca mais importante: o Conteudo (C) do ACPR segue Pyramid Principle — conclusao primeiro, argumentos de suporte depois.

**Antes (errado):**
"A API do Kommo mudou o formato do webhook. Isso fez a integracao quebrar. Tive que refazer o parser. Isso atrasou 2 dias."

**Depois (certo):**
"A integracao atrasou 2 dias. Motivo: API do Kommo mudou o webhook sem aviso. Fix ja aplicado."

O cliente leu "atrasou 2 dias" na primeira frase e ja sabe a situacao. O resto e contexto — pode ler ou nao.

**Regra MECE no Conteudo:**
Se tem multiplos pontos, organize Mutually Exclusive (sem sobreposicao) e Collectively Exhaustive (sem deixar nada de fora):
- "Temos 3 itens pendentes: (1) integracao Kommo, (2) tela de relatorios, (3) deploy em producao."

---

## SCQA — Framework Narrativo

Quando ACPR nao e suficiente (situacoes que precisam convencer ou dar contexto narrativo):

- **Situation:** "O projeto X ta na reta final, com 80% entregue."
- **Complication:** "O cliente pediu 3 features novas que nao estavam no escopo."
- **Question:** "O que priorizamos: entregar no prazo sem as features, ou estender?"
- **Answer:** "Recomendo entregar no prazo e orcar as features como fase 2."

**Quando usar SCQA em vez de ACPR:**
- Propostas de mudanca
- Explicacoes de trade-off
- Comunicacoes onde precisa convencer o cliente
- Situacoes com historico complexo que precisa de narrativa

**Como integrar com ACPR:**
- A (abertura) = normal
- C (conteudo) = SCQA inteiro
- P (proposta) = a Answer do SCQA
- R (reforco) = normal

---

## NVC — Comunicacao Nao-Violenta (Rosenberg)

Framework OFNR para mensagens delicadas (atraso por erro seu, falha grave):

1. **Observation:** Fato puro, sem julgamento. "O prazo da integracao era sexta e nao vai dar."
2. **Feeling:** Admita o desconforto (humaniza). "Fico desconfortavel de comunicar isso."
3. **Need:** O que voce precisa manter. "Preciso de transparencia contigo pra manter confianca."
4. **Request:** Pedido concreto. "O novo prazo e terca. Posso te dar update diario ate la?"

**Quando usar OFNR:**
- Atraso por falha interna (nao externa)
- Erro que impactou o cliente diretamente
- Situacao onde a confianca esta abalada
- Precisa reconstruir relacao

**Quando NAO usar:**
- Atraso por fator externo (API de terceiro, etc.) — ACPR basta
- Update normal — OFNR e pesado demais
- Cliente com perfil mais tecnico/direto — vai parecer enrolacao

NVC humaniza. Nao e fraqueza — e maturidade. Mas use com criterio.

---

## Tecnicas de Negociacao (Chris Voss)

### Mirroring
Repita as ultimas 2-3 palavras que o cliente disse. Isso faz a pessoa elaborar.
- Cliente: "To corrido demais essa semana."
- Voce: "...corrido demais?"
- Resultado: ele vai explicar O QUE ta travando, o que te da informacao pra resolver.

**Funciona porque:** ativa o instinto de completar o raciocinio. E a tecnica mais simples e mais eficaz.

### Labeling
Nomeie o sentimento ou a situacao sem concordar nem discordar.
- "Parece que essa feature e importante pra voces por causa do [contexto]."
- "Parece que tem algo travando do lado de voces."

**Funciona porque:** valida a outra pessoa sem abrir mao da sua posicao. Reduz resistencia.

### Calibrated Questions
Perguntas que comecam com "como" ou "o que" e fazem o cliente pensar no trade-off.
- "Como voce priorizaria isso em relacao ao que ja ta no escopo?"
- "O que seria necessario pra destravar isso essa semana?"
- "Como a gente poderia encaixar isso sem comprometer o prazo de [X]?"

**Funciona porque:** transfere o onus da solucao. Em vez de voce dizer "nao", o cliente chega na mesma conclusao sozinho.

### Quando usar cada tecnica:

| Situacao | Tecnica | Motivo |
|----------|---------|--------|
| Cliente vago/evasivo | Mirroring | Faz elaborar |
| Conflito/insatisfacao | Labeling | Valida sem concordar |
| Scope creep | Calibrated question | Cliente pensa no trade-off |
| Cobranca de pagamento | Labeling + Calibrated | Valida + pede solucao |
| Cliente quer desconto | Calibrated question | "Como podemos fazer funcionar pro orcamento?" |

---

## Integracao entre frameworks

A escolha do framework depende da situacao:

| Situacao | Framework principal | Complemento |
|----------|-------------------|-------------|
| Update normal | ACPR | Pyramid no C |
| Pedir decisao | ACPR | Opcoes + recomendacao |
| Convencer/proposta | SCQA dentro do ACPR | - |
| Erro/falha interna | ACPR + OFNR | Pyramid no C |
| Negociacao/escopo | ACPR + Voss | Calibrated questions |
| Cobranca | ACPR + escalonamento | Voss se resistencia |
| Reclamacao | ACPR (Validar-Assumir-Resolver-Prevenir) | Labeling |

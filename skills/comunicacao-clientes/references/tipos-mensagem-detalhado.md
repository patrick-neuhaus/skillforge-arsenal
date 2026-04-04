# Tipos de Mensagem — Exemplos Detalhados

Cada tipo tem: contexto, exemplo bom, exemplo ruim, erros comuns, e framework aplicado.

---

## Tipo 1: Update de Status

**Framework:** ACPR (conclusao primeiro no C)

**Principio:** Update proativo > update reativo. Se o cliente precisa PERGUNTAR "como ta?", voce ja atrasou.

**Cadencia:** Semanal ou por entrega, o que vier primeiro.

**Exemplo bom:**
> Fala Ricardo, tudo bem?
>
> Update do projeto: *3 de 5 telas entregues*. Tela de dashboard e relatorios ficam prontas ate sexta.
>
> Nao precisa fazer nada — so te mantendo no loop. Proximo update sexta.

**Exemplo ruim:**
> Oi Ricardo, entao, essa semana a gente trabalhou bastante no projeto, o Hygor fez umas telas, eu fiz a integracao, teve uns problemas com a API mas resolvemos, e agora tamo no caminho certo...

**Erros comuns:**
- Update longo demais. Cliente quer saber: ta andando? quando recebo?
- Falar de processo interno (quem fez o que) — cliente quer resultado
- Nao dar prazo concreto do proximo marco

---

## Tipo 2: Pedir Aprovacao/Decisao

**Framework:** ACPR com opcoes + recomendacao

**Principio:** SEMPRE de sua recomendacao. "O que voce prefere?" e preguica. "Recomendo A porque [motivo]" e lideranca.

**Exemplo bom:**
> Fala Ana, preciso de uma decisao sobre o dashboard.
>
> *Temos 2 caminhos pra exportacao de relatorios:*
> A) PDF simples — pronto em 2 dias, cobre 80% do uso
> B) PDF + Excel — pronto em 5 dias, cobre 100%
>
> *Recomendo A* — maioria dos usuarios so precisa de PDF. Se precisar Excel depois, adicionamos em 2 dias.
>
> Qual prefere?

**Exemplo ruim:**
> Oi Ana, sobre o dashboard, a gente pode fazer de varias formas: PDF, Excel, CSV, ou ate um link publico. Cada um tem seus pros e contras. O que voce acha melhor?

**Erros comuns:**
- 5 opcoes sem recomendacao. Reduza pra 2-3 e recomende
- Nao incluir trade-off entre opcoes
- Nao dar prazo estimado por opcao

---

## Tipo 3: Mudanca de Escopo

**Framework:** ACPR + tecnicas de negociacao (Voss)

**Principio:** Nunca diga "nao" seco. Diga "sim, e o impacto e [X]".

**Exemplo bom (com tecnicas Voss):**
> Fala Carlos, sobre a feature de notificacao push que voce pediu.
>
> *Parece que isso e importante por causa do engajamento dos usuarios.* (labeling)
> Da pra fazer, sim. O impacto: +1 semana no prazo do projeto e R$X adicional.
>
> *Como voce priorizaria isso em relacao a entrega do modulo de pagamentos?* (calibrated question)
>
> Me fala e a gente ajusta o cronograma.

**Exemplo ruim:**
> Oi Carlos, sobre o push, nao da pra fazer agora nao, ja tem muita coisa no escopo. Desculpa.

**Erros comuns:**
- Aceitar mudanca sem comunicar impacto (depois atrasa e a culpa e sua)
- Dizer "nao" seco (cliente sente que voce e inflexivel)
- Nao quantificar impacto (prazo e custo)

---

## Tipo 4: Noticia Ruim (Atraso, Problema)

**Framework:** ACPR (conclusao primeiro = noticia ruim logo) + OFNR se erro interno

**Principio:** Velocidade de comunicacao > qualidade da noticia. Avisar terca com solucao parcial > avisar sexta com solucao completa.

**Regra de ouro:** Nunca leve so o problema. Sempre leve: causa, o que ja fez, plano.

**Exemplo bom (erro externo — ACPR puro):**
> Fala Marcos, update importante.
>
> *A integracao com o Kommo atrasou 2 dias.* Motivo: API deles mudou o webhook sem aviso. Fix ja aplicado, novo prazo: quarta.
>
> Nao precisa fazer nada do seu lado. Te atualizo quarta de manha.

**Exemplo bom (erro interno — ACPR + OFNR):**
> Fala Marcos, preciso ser transparente contigo.
>
> *O prazo do modulo de relatorios era sexta e nao vai dar.* Subestimei a complexidade da exportacao. Novo prazo realista: terca.
>
> Posso te dar update diario ate la. Te mando print do progresso amanha de manha.

**Exemplo ruim:**
> Oi Marcos, entao, sabe o que aconteceu? A API do Kommo... [5 paragrafos de contexto antes de dizer que atrasou]

**Erros comuns:**
- Enterrar a noticia ruim no meio de paragrafos de contexto
- Nao ter plano de resolucao
- Demorar demais pra comunicar esperando solucao perfeita

---

## Tipo 5: Cobrar Resposta/Pagamento

**Framework:** ACPR + escalonamento progressivo + Voss

**Principio:** Cobrar nao e ser chato. Cobrar e ser profissional.

**Escalonamento:**

**Nivel 1 — Tom normal (dia 0):**
> Fala Julia, mandei o layout das telas ontem. To aguardando seu retorno pra seguir com o desenvolvimento.

**Nivel 2 — Reforco (dia 3):**
> Oi Julia, reforcando o ponto das telas. To com o desenvolvimento parado ate receber seu ok. Consegue me dar retorno hoje?

**Nivel 3 — Consequencia (dia 5):**
> Julia, sem retorno sobre as telas, vou pausar o projeto ate receber posicionamento. Assim que aprovar, retomo na sequencia.

**Com Voss (se resistencia):**
- Cliente diz "to corrido" → Mirroring: "...corrido?" → ele elabora
- Labeling: "Parece que tem algo travando do lado de voces."
- Calibrated: "O que seria necessario pra destravar isso essa semana?"

**Erros comuns:**
- Nao escalonar (fica mandando nivel 1 por 3 semanas)
- Escalonar rapido demais (nivel 3 no dia 2)
- Nivel 3 sem respaldo (pausar sem alinhar com Willy primeiro)

---

## Tipo 6: Responder Reclamacao

**Framework:** Validar → Assumir → Resolver → Prevenir

**Principio:** Reclamacao e presente. O que sai sem reclamar e pior.

**Exemplo bom:**
> Fala Pedro, entendo sua frustracao com o bug no checkout. Faz sentido.
>
> *Isso foi falha nossa no teste da ultima atualizacao.* Ja corrigimos — ta no ar desde as 14h.
>
> Pra nao acontecer de novo, implementamos teste automatizado pro fluxo de checkout.
>
> Qualquer outro ponto, me fala.

**Exemplo ruim:**
> Oi Pedro, desculpa, desculpa mesmo, nao era pra ter acontecido, desculpa de verdade, vou ver o que houve...

**Roteiro completo:**
1. **Valide:** "Entendo sua frustracao. Faz sentido."
2. **Assuma:** "Isso foi falha nossa em [especifico]"
3. **Resolva:** "Vou fazer [acao] ate [data]"
4. **Previna:** "Pra nao acontecer de novo, vamos [mudanca]"

**Erros comuns:**
- Pedir desculpa 5 vezes (parece inseguranca, nao profissionalismo)
- Nao assumir responsabilidade ("foi um problema tecnico" em vez de "falha nossa")
- Resolver sem prevenir (vai acontecer de novo)
- Ficar na defensiva/justificar em vez de resolver

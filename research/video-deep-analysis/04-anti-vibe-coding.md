# Video 4: Como eu uso o Claude Code (Workflow Anti-Vibe Coding)

> Fonte: https://www.youtube.com/watch?v=BcLtqQ3JlMU
> Canal: DevGPT (criadora do app Epic - 3.000+ usuarios em 90 dias, sem escrever codigo manualmente)

---

## Resumo Executivo

O video apresenta o workflow completo "anti-vibe coding" baseado em **Spec Driven Development (SDD)**, um processo de 3 etapas (Research -> Spec -> Implement) que resolve os problemas classicos de geracao de codigo por IA: overengineering, reinvencao da roda, duplicacao de codigo, desconhecimento de docs externas e mistura de responsabilidades em um mesmo arquivo. O ponto central e que todos esses problemas derivam de **mau gerenciamento da context window** -- a IA nao "lembra" do que precisa porque o usuario nao alimenta corretamente a janela de contexto. A solucao e um pipeline de compressao progressiva: pesquisa ampla -> PRD resumido -> spec tatica -> implementacao com janela limpa. A regra de ouro e **nunca ultrapassar 40-50% da context window** e usar `/clear` entre cada fase para garantir que so informacao filtrada e relevante chega ao momento de codificar.

---

## Processo Completo (passo a passo reproduzivel)

### Fase 0: Entendimento do Problema

Antes de comecar, tenha clareza sobre **o que** voce quer implementar. Defina em uma ou duas frases o objetivo da feature/mudanca. Exemplo citado: "Preciso implementar um sistema de confirmacao de conta por e-mail para usuarios que nao logaram com Gmail."

---

### Fase 1: Pesquisa (Research)

**Objetivo:** Coletar todo o contexto necessario para a IA fazer uma implementacao efetiva. Nesta fase, e aceitavel que venha informacao desnecessaria -- o filtro acontece no output (PRD).

**O que fazer:**

1. **Pesquisa na base de codigo existente**
   - Peca ao Claude Code para identificar todos os arquivos que serao afetados pela implementacao
   - Peca para encontrar padroes de implementacao de coisas similares ja feitas no projeto (ex: se ja existe um componente de botao, a IA precisa saber para nao criar outro)
   - Exemplo: "Preciso implementar confirmacao de e-mail. Busque na base de codigo todos os arquivos referentes a feature de autenticacao, incluindo tabelas do banco de dados."

2. **Buscar documentacoes externas**
   - Mande a IA ler a documentacao **relevante** (nao a inteira) das bibliotecas/servicos que serao usados
   - Exemplo: documentacao do NextAuth referente a verificacao de e-mail, documentacao do Resend para envio de e-mails

3. **Buscar padroes de implementacao externos**
   - Stack Overflow, GitHub repos, documentacoes oficiais com code snippets
   - **Tecnica .tmp (pasta temporaria):** Clonar/baixar um projeto do GitHub que tenha o padrao desejado, colocar numa pasta `.tmp` dentro do projeto, pedir ao Claude Code para analisar aquele padrao, e depois deletar a pasta
   - Isso e especialmente util para quem nao e desenvolvedor e precisa de referencia de "como deve ser feito"

4. **Gerar o PRD.md**
   - Ao final da pesquisa, peca ao Claude Code para gerar um `prd.md` contendo:
     - Todos os arquivos da base de codigo **relevantes** (exclui os inuteis encontrados)
     - Trechos das documentacoes externas que sao importantes
     - Code snippets / padroes de implementacao encontrados
     - Descricao do que se quer implementar
   - O PRD funciona como um **funil**: filtra informacao util de lixo

**Ferramentas:** Claude Code (busca na base de codigo, leitura de arquivos), web fetch/MCPs para documentacoes, GitHub para repos de referencia

**Ao terminar:** Execute `/clear` para limpar toda a janela de contexto.

---

### Fase 2: Spec (Especificacao)

**Objetivo:** Transformar o PRD em um plano de implementacao ultra-especifico e tatico.

**O que fazer:**

1. **Abrir nova conversa** (apos o /clear)
2. **Fazer referencia ao PRD gerado:** "Le esse PRD.md e gera uma spec para mim"
3. A spec deve conter, para cada arquivo:
   - **Path completo** do arquivo (ex: `src/db/schema.ts`)
   - **Acao:** criar ou modificar
   - **O que exatamente** criar ou modificar naquele arquivo
   - **Code snippets / pseudocodigo** quando aplicavel (vindos dos padroes de implementacao da pesquisa)
4. **Ser extremamente especifico** -- se nao deixar claro o path e a acao, a IA vai implementar "do jeito dela"

**Formato da spec (padrao recomendado):**
```
### arquivo: src/db/schema.ts
- Acao: MODIFICAR
- O que: Adicionar coluna `emailVerified` (boolean, default false) na tabela users
- Snippet: [pseudocodigo ou trecho de referencia]

### arquivo: src/lib/auth/verify-email.ts
- Acao: CRIAR
- O que: Funcao que envia e-mail de verificacao usando Resend, gera token, salva no banco
- Snippet: [padrao vindo da documentacao do Resend]
```

**Ferramentas:** Claude Code lendo o PRD.md e gerando spec.md

**Ao terminar:** Execute `/clear` novamente.

---

### Fase 3: Implementacao (Code)

**Objetivo:** Executar o plano da spec com a janela de contexto o mais limpa possivel.

**O que fazer:**

1. **Abrir nova conversa** (apos o /clear)
2. **Anexar a spec como prompt:** "Implementa essa spec" + referencia ao arquivo spec.md
3. Deixar a IA trabalhar -- ela tem todas as instrucoes taticas necessarias
4. A **janela de contexto fica quase toda livre** para a implementacao real

**Por que funciona:**
- O prompt de entrada (spec) e um resumo comprimido de toda a pesquisa e planejamento
- A IA nao precisa buscar arquivos, ler documentacoes, explorar a base de codigo -- tudo ja esta digerido
- Sobra o maximo de janela de contexto para a IA executar bem

**Ferramentas:** Claude Code implementando a spec

---

### Regra dos 40-50% de Context Window

- Nunca ultrapasse 40-50% da sua janela de contexto
- Quando perceber que esta chegando perto, de `/clear` e comece nova conversa
- Quanto mais cheia a janela de contexto, pior o output -- confirmado por pesquisas e pela experiencia pratica da autora
- Tudo consome context window: buscas de arquivo, leituras, edicoes, respostas de MCPs, e os proprios prompts do usuario

---

### O que destroi a qualidade do input (e portanto do output)

| Problema | Consequencia |
|----------|-------------|
| Informacao incorreta | IA edita arquivo errado, implementa logica errada |
| Informacao incompleta | IA "adivinha" e implementa errado (ex: falta doc de lib externa) |
| Informacoes inuteis | Enchem a janela de contexto sem agregar, confundem a IA |
| Informacoes demais | Quanto mais cheia a context window, pior o resultado |

---

## Referencias Citadas

### Ferramentas e Tecnologias
- **Claude Code** -- coding assistant principal usado no workflow
- **Epic App** -- aplicacao da autora, 3.000+ usuarios, construida sem escrever codigo manualmente
- **ProseMirror** -- framework para editores rich-text (mencionado como alternativa a criar do zero)
- **TipTap** -- editor rich-text baseado no ProseMirror (usado no Epic)
- **NextAuth / Next.js** -- framework usado para autenticacao
- **Resend** -- servico de envio de e-mails
- **Stack Overflow** -- fonte de padroes de implementacao
- **GitHub** -- fonte de repos com padroes de referencia

### Conceitos
- **Spec Driven Development (SDD)** -- metodologia central do video (Research -> Spec -> Implement)
- **Context Window** -- janela de contexto do modelo, medida em tokens (~4 caracteres por token)
- **Vibe Coding** -- termo para "jogar prompt e torcer para dar certo" (o que o metodo combate)
- **Overengineering** -- padrao onde a IA complica o que poderia ser simples
- **PRD (Product Requirements Document)** -- usado aqui como resumo da fase de pesquisa

### Pessoas e Canais
- **DevGPT (newsletter)** -- newsletter da autora no Substack, maior newsletter de construcao de software com IA do Brasil
- **Reed Hastings** -- fundador do Netflix, citado sobre desenvolvedores bons serem 10-20x mais produtivos por escrever codigo mais simples (nao mais rapido)

---

## Skills que Podem Ser Geradas

| Nome proposto | O que faria | Baseado em qual trecho |
|---------------|-------------|------------------------|
| **sdd-research** | Conduz a Fase 1 completa: busca na base de codigo, leitura de docs externas, coleta de padroes, e gera o `prd.md` filtrado | Fase 1 inteira (timestamps 12:22-16:22) -- pesquisa na base de codigo, docs externas, padroes de implementacao, geracao do PRD |
| **sdd-spec-writer** | Recebe um PRD e gera uma spec ultra-tatica com paths, acoes (criar/modificar), e snippets para cada arquivo | Fase 2 inteira (timestamps 16:22-19:14) -- "diz exatamente qual arquivo modificar, criar, e o que fazer em cada um" |
| **sdd-implementer** | Recebe uma spec e executa a implementacao arquivo por arquivo, respeitando paths e snippets definidos | Fase 3 (timestamps 19:14-24:01) -- "implementa a spec deixando a janela limpa" |
| **context-guardian** | Monitora uso de context window, alerta quando esta perto de 40-50%, sugere /clear e resume estado atual para handoff | Regra 40-50% (timestamps 19:21-19:40) -- "trabalhar com 40 a 50% no maximo, quando passar limpa e comeca de novo" |
| **pattern-importer** | Automatiza a tecnica .tmp: clona repo/trecho do GitHub, coloca em pasta temporaria, extrai padrao, e limpa | Tecnica .tmp (timestamps 14:44-15:06) -- "pego um projeto do GitHub, importo numa pasta .tmp, peco pro Claude Code olhar, depois deleto" |
| **code-dedup-checker** | Analisa a base de codigo antes de implementar algo novo para encontrar componentes/funcoes duplicadas ou reutilizaveis | Problema de duplicacao (timestamps 4:14-4:46) -- "cria outro botao e agora voce tem manutencao dobrada" |

---

## Insights Nao-Obvios

1. **A IA e um multiplicador, nao um transformador.** "Quem transforma agua em vinho e Jesus. A IA multiplica o que voce deu pra ela." Se voce alimenta com lixo, o output e lixo multiplicado. Nao e uma limitacao tecnica -- e uma limitacao de input.

2. **A tecnica .tmp e um hack de transferencia de conhecimento.** Ao importar um repo inteiro (ou parte dele) numa pasta temporaria so para a IA analisar o padrao, voce esta essencialmente fazendo "few-shot learning" manual -- dando exemplos concretos de como o codigo deve ser, sem precisar descrever em linguagem natural.

3. **O /clear entre fases e uma forma de "compressao progressiva".** Cada fase comprime o conhecimento da anterior num artefato (PRD -> spec -> codigo). E como um pipeline de destilacao onde cada etapa filtra ruido e concentra sinal.

4. **Simplicidade de codigo nao e preferencia estetica -- e otimizacao de tokens.** Arquivo de 2.000 linhas vs 100 linhas nao e so mais facil de manter humanamente -- consome 20x mais tokens da IA para ler e modificar. Codigo simples e literalmente mais barato e mais eficaz com IA.

5. **A "velocidade falsa" do vibe coding e uma armadilha.** Comecar sem pesquisa/spec da resultados rapidos no inicio, mas leva a uma parede inevitavel onde debitos tecnicos tornam o projeto impossivel de evoluir. O SDD parece mais lento no inicio mas vai muito mais longe.

6. **A IA nao pesquisa sozinha.** A autora destaca que muitos assumem que a IA vai buscar documentacoes por conta propria quando nao sabe algo. Na maioria das vezes, ela nao faz isso -- implementa com o que tem (e erra). Voce precisa fornecer as docs explicitamente.

7. **O PRD como "handoff document".** O PRD nao e so um documento de requisitos tradicional -- e o mecanismo de transferencia de conhecimento entre uma conversa (que vai ser descartada) e a proxima (que vai usar esse conhecimento filtrado). E um artefato de comunicacao entre "agentes" (sessoes).

---

## Conexoes com Skills Existentes

### skill-builder
- O proprio workflow SDD poderia ser encapsulado como uma meta-skill que orquestra as 3 fases. O skill-builder seria usado para criar as skills `sdd-research`, `sdd-spec-writer` e `sdd-implementer`.

### prompt-engineer
- A qualidade do output depende diretamente da qualidade do input (tema central do video). O prompt-engineer e a skill que garante que os prompts de cada fase do SDD sejam otimos -- especialmente o prompt de pesquisa e o prompt de geracao de spec.

### reference-finder
- Diretamente conectado a Fase 1 (Research). O reference-finder ja faz parte do que a autora descreve: buscar frameworks, padroes, documentacoes e referencias externas. Pode ser integrado como sub-etapa da fase de pesquisa.

### sdd
- Se ja existe uma skill SDD no arsenal, este video e a fundamentacao pratica completa dela. O conteudo aqui detalha o "como" e o "por que" de cada etapa.

### context-tree
- O context-tree mapeia a estrutura do projeto. Isso e exatamente o que a Fase 1 faz parcialmente (identificar arquivos afetados). O context-tree poderia alimentar automaticamente a fase de pesquisa com o mapa de dependencias.

### maestro
- O maestro orquestra agentes/skills. O workflow SDD e um pipeline de 3 fases que poderia ser orquestrado pelo maestro: chamar sdd-research -> passar output para sdd-spec-writer -> passar output para sdd-implementer, fazendo /clear entre cada uma.

### trident
- O trident (3 agentes em sequencia) e estruturalmente identico ao SDD (3 fases em sequencia com handoff via artefato). O SDD e essencialmente um "trident" aplicado a desenvolvimento de software.

### ui-design-system / component-architect / react-patterns
- Estas skills produzem artefatos (design systems, arquiteturas de componentes, padroes React) que sao exatamente o tipo de "padrao de implementacao" que a Fase 1 busca. Podem ser fontes de input para a pesquisa, garantindo que a IA siga padroes ja definidos no projeto.

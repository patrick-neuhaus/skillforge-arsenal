Aqui esta a analise completa da transcrição.

---

# Analise Completa: "Vibe Coding não funciona (Novo Workflow no Claude Code)"

**Fonte:** https://www.youtube.com/watch?v=Ea5yaWGqoHQ

---

## 1. Resumo Completo

O video e apresentado por um unico criador de conteudo (nao identifica o nome na transcrição, mas e o criador do produto **Epic New**). Ele apresenta o workflow completo que usa para criar aplicações profissionais com o Claude Code, contrastando-o diretamente com o "Vibe Coding". 

O caso de estudo e o **Epic New**, um produto que bateu 300 usuarios no primeiro dia e que, segundo ele, foi feito 100% com IA -- mas seguindo um processo estruturado, nao vibe coding. O argumento central e: **vibe coding serve para prototipos simples, mas e inviavel para aplicações complexas e de produção.**

---

## 2. Critica ao Vibe Coding -- 5 Problemas Identificados

### Problema 1: IA engasga com tarefas grandes
- Quando voce da uma tarefa grande demais, a IA lota a **janela de contexto** e perde performance.
- O modelo falha no meio da implementação.

### Problema 2: Codigo bagunçado
Tres sub-padroes:
- **A IA complica o que deveria ser simples** -- e proativa demais, implementa coisas que voce nao pediu, ou reinventa a roda ao inves de seguir padrões comprovados.
- **A IA repete trechos de codigo** -- nao se lembra que ja criou um componente (ex: cria um segundo botao ao inves de importar o existente). Resultado: manutençao duplicada.
- **Codigo dificil de manter** -- soma de complexidade desnecessaria + duplicação = pesadelo de manutençao.

### Problema 3: IA nao obedece
- Quem nao e dev foca em dizer **o que** quer, nao **como** fazer.
- Dizer "faz um signup" nao e suficiente -- a IA precisa saber **quais arquivos** criar/modificar.
- Sem essa orientação, a IA infere e frequentemente mexe no arquivo errado.
- **Escala piora o problema**: em projetos com poucos arquivos a IA acerta por sorte; conforme cresce, a chance de erro aumenta.

### Problema 4: Arrumar uma coisa e quebrar outra ("cobertor de pobre")
- A IA junta responsabilidades que deveriam estar separadas.
- Sem modularização, alterar uma funcionalidade impacta outra.
- Devs sabem que isolamento e fundamental, mas nao-devs deixam a IA fazer "vida louca".

### Problema 5: Gafes de segurança
Dois padrões perigosos:
- **Logica de negocio no front-end** -- qualquer um pode manipular (ex: mudar de "user" para "admin" com dois cliques no browser).
- **Chaves expostas no front-end** -- acesso direto ao banco de dados por qualquer pessoa.

---

## 3. Novo Workflow Proposto (Passo a Passo)

O workflow tem **4 etapas** sequenciais:

### Etapa 1: Escrever a Spec (`/spec`)
- Comando: `/spec` + descrição do que quer fazer
- Gera um documento Markdown (spec.md) que lista:
  - **Paginas** da aplicação
  - **Componentes** de cada pagina
  - **Comportamentos** (behaviors) do usuario em cada pagina
- Objetivo: dar clareza tanto para o dev quanto para o Claude sobre o que sera construido.

### Etapa 2: Quebrar a Spec em Issues (`/break`)
- Comando: `/break` + arrasta o arquivo da spec
- O documento spec e dividido em **tarefinhas pequenas** (issues):
  - Cada **pagina** vira uma issue (prototipos primeiro, so front-end)
  - Cada **comportamento** vira uma issue separada
  - A ordem e: primeiro prototipos (so tela), depois funcionalidades
- Objetivo: preservar a janela de contexto, nunca dar uma tarefa grande demais.

### Etapa 3: Planejar cada Issue (`/plan`)
- Comando: `/plan` + arrasta a issue
- Executa **duas pesquisas**:
  1. **Na base de codigo** -- identifica trechos/arquivos reutilizaveis para importar ao inves de recriar
  2. **Fora do projeto** (internet, docs) -- busca padrões de implementação comprovados e documentação de dependencias externas
- O resultado enriquece a issue com:
  - Descrição detalhada do comportamento
  - Cenarios: caminho feliz, edge cases, cenarios de erro
  - **Tabelas do banco** que precisam ser criadas + colunas
  - **Arquivos** que precisam ser criados ou modificados + o que fazer em cada um
  - Dependencias externas
  - Lista de tarefas resumida (checklist)

### Etapa 4: Executar a Issue (`/execute`)
- Comando: `/execute` + arrasta a issue planejada
- A implementação usa **agentes especializados por camada**:
  - **Model Writer** -- so faz banco de dados
  - **Component Writer** -- so faz componentes front-end
  - Cada agente tem sua **skill** com regras especificas
- Documentos de apoio na pasta `/references`:
  - `architecture.md` -- padrões de arquitetura, regra de "thin client / fat server"
  - `design-system.md` -- padrões visuais
  - Especificações e workflow

---

## 4. Skills/Tools Mencionados

| Ferramenta/Skill | Função |
|---|---|
| `/spec` | Gera documento de especificação (paginas, componentes, behaviors) |
| `/break` | Quebra a spec em issues/tarefinhas |
| `/plan` | Pesquisa na codebase + internet e gera planejamento detalhado |
| `/execute` | Implementa a issue usando agentes especializados |
| **Model Writer** (agente) | Especializado em banco de dados |
| **Component Writer** (agente + skill `write_components`) | Especializado em componentes front-end |
| **Agentes de teste** | Mencionados brevemente para segurança |
| `architecture.md` | Documento de regras de arquitetura |
| `design-system.md` | Documento de design system |
| **Epic New / Epic Builder** | Produto que empacota todo esse workflow (versão web e CLI) |
| **Epic Learn** | Parte educacional com aulas gravadas e ao vivo |

---

## 5. Padrões de Desenvolvimento com IA

### Principios-chave extraidos:

1. **Janela de contexto limpa = melhor performance.** Nunca sobrecarregar. Tarefas pequenas e focadas.

2. **Especificar arquivos explicitamente.** Dizer quais arquivos criar/modificar e o que fazer em cada um. A IA nao "desobedece" -- ela infere errado quando nao tem instrução clara.

3. **Pesquisa antes de implementação.** Sempre buscar na codebase antes de criar algo novo. Evita duplicação e reinvenção da roda.

4. **Documentação de referencia externa.** Buscar padrões comprovados e documentação de dependencias antes de implementar.

5. **Arquitetura por comportamento.** Organizar pastas por pagina, e dentro de cada pagina, por comportamento. Garante isolamento.

6. **Thin Client / Fat Server.** Nenhuma logica de negocio no front-end. Front-end so captura intenções do usuario, envia para o back-end, e renderiza a resposta.

7. **Agentes especializados por camada.** Cada tipo de arquivo (banco, componente, etc.) tem seu proprio agente com skills e regras dedicadas.

8. **Documentação como guardrail.** `architecture.md`, `design-system.md`, e docs de workflow funcionam como "cercas" que impedem a IA de sair do padrão.

9. **Prototipo primeiro, funcionalidade depois.** Implementar so front-end (tela) primeiro, validar, e so depois implementar logica.

---

## 6. HumanLayer

**Nao mencionado** nesta transcrição. O video nao faz referencia ao HumanLayer em nenhum momento.

---

## 7. Commands/Prompts do Claude Code

Os comandos mostrados no video sao **custom slash commands** configurados no Claude Code:

| Comando | O que faz |
|---|---|
| `/spec` | Gera a especificação do projeto (paginas, componentes, behaviors) |
| `/break` | Quebra a spec em issues individuais (uma por pagina, uma por behavior) |
| `/plan` | Pesquisa codebase + internet, gera planejamento detalhado da issue |
| `/execute` | Implementa a issue planejada usando agentes e skills especializados |

**Nota:** Os nomes `research_codebase`, `create_plan`, `implement_plan` que voce mencionou na pergunta nao aparecem com esses nomes exatos na transcrição. Os equivalentes sao `/plan` (que faz research + planejamento) e `/execute` (que implementa). E possivel que esses nomes sejam os nomes internos dos prompts/comandos salvos que ele usa dentro do Epic Builder.

---

## 8. Insights Acionaveis para o Nosso Arsenal de Skills

### O que podemos aplicar diretamente:

1. **Criar um comando `/spec` proprio.** Um prompt que recebe a descrição de um projeto e gera automaticamente o documento de especificação no formato pagina > componentes > behaviors. Ja temos a skill `product-discovery-prd` que cobre algo similar, mas podemos especializa-la para gerar output no formato spec que alimenta as proximas etapas.

2. **Criar um comando `/break` proprio.** Pegar qualquer documento de spec/PRD e quebrar automaticamente em issues atomicas. Cada issue = um behavior ou uma pagina. Integrar com ClickUp via o MCP que ja temos.

3. **Enriquecer o planejamento pre-implementação.** Antes de implementar qualquer coisa, o workflow deveria ter um passo de "research codebase" -- grep na base de codigo para achar componentes/padrões reutilizaveis. Isso e algo que o Claude Code ja faz nativamente, mas podemos formalizar num prompt/skill.

4. **Agentes especializados por camada.** O conceito de ter um "Model Writer" e um "Component Writer" com skills distintas e poderoso. Podemos criar skills especificas para:
   - Supabase schemas (ja temos `supabase-db-architect`)
   - Componentes front-end com design system especifico
   - API routes / server actions

5. **Pasta `/references` como padrão.** Manter `architecture.md` e `design-system.md` em todo projeto. A skill `lovable-knowledge` ja gera algo parecido, mas podemos padronizar para projetos Claude Code tambem.

6. **Regra "Thin Client / Fat Server" no architecture.md.** Incluir explicitamente nos nossos documentos de arquitetura para evitar gafes de segurança. A skill `security-audit` pode validar isso.

7. **Ordem: prototipos primeiro, logica depois.** Isso simplifica validação visual e reduz retrabalho. Aplicavel tanto no Lovable quanto no Claude Code.

8. **Especificar arquivos explicitamente nas issues.** O insight mais importante: nao dizer "faz X", mas sim "cria/modifica arquivo Y fazendo Z". Isso elimina o problema da IA "desobedecer".

---

### Resumo em uma frase:

**O workflow anti-vibe-coding e: Spec -> Break em issues atomicas -> Plan (pesquisa codebase + docs externos) -> Execute (agentes especializados) -- tudo apoiado por documentação de arquitetura e design como guardrails.**
Aqui esta a analise completa do video "Agente de IA e coisa do passado. Agora eu so uso SKILLS." (canal da Debora / Dopic / Donus):

---

## 1. RESUMO COMPLETO

O video defende a tese de que **2026 e o ano das skills**, enquanto 2025 foi o ano dos agentes. O problema central: agentes de IA, por mais inteligentes que sejam, **nao conhecem a sua forma de trabalhar**. Skills resolvem isso funcionando como playbooks que a IA le antes de executar uma tarefa, tornando-a especialista no seu negocio e melhorando com o tempo.

O video cobre:
- Diferenca conceitual entre agentes e skills
- O que sao skills na pratica (pastas com arquivos)
- Skills como extensoes de system prompt + ferramentas (scripts)
- Otimizacao da janela de contexto via progressive disclosure
- Demonstracao ao vivo: criacao de uma skill de propostas comerciais do zero usando o Claude
- Instalacao e uso da skill criada

---

## 2. SKILLS vs AGENTES -- Comparacao Detalhada

| Aspecto | Agente | Skill |
|---|---|---|
| **System Prompt** | Tudo chumbado num unico system prompt grande | System prompt enxuto + playbooks externos sob demanda |
| **Ferramentas (Tools)** | Definidas na arquitetura do agente (ex: tools do n8n) | Scripts dentro da pasta da skill que funcionam como tools |
| **Memoria** | Requer banco externo para salvar interacoes | Retroalimentacao nativa -- voce pede pro agente registrar aprendizados na propria skill |
| **Manutencao** | Requer deploy a cada mudanca | Conversa natural: "registra isso na nossa skill pra proxima vez" |
| **Context Window** | Carrega tudo de uma vez, desperdicando janela | Progressive disclosure: so carrega a skill quando precisa |
| **Evolucao** | Estatico ate proximo deploy | Melhora continuamente com uso |

**Argumento central**: Skills nao substituem agentes, mas **complementam** agentes. Voce continua tendo um agente, mas agora o agente e enxuto e chama skills sob demanda.

---

## 3. COMO CRIAR SKILLS -- Tecnicas e Padroes

### Estrutura de uma Skill
Uma skill e literalmente uma **pasta com arquivos**:
- **SKILL.md** -- Arquivo principal (o "system prompt" da skill) com instrucoes, roteiros de perguntas, regras
- **Subpastas de referencias** -- Dados, planilhas, imagens, exemplos
- **Scripts** -- Codigo Python/outro para operacoes deterministicas

### Metodo de Criacao (demonstrado no video)
1. Abrir o Claude (interface web, nao precisa ser Claude Code)
2. Pedir: "Eu quero criar uma skill para [fazer X]"
3. O Claude possui uma **skill de criar skills** (skill-builder) -- ele le essa meta-skill e te guia
4. Se o Claude ja tem contexto suficiente sobre voce, ele cria a skill proativamente
5. Se nao tem contexto, ele faz perguntas guiadas
6. O resultado e um arquivo ZIP com a pasta da skill
7. Voce instala via "Upload Skill" nas capabilities do Claude

### Principio Deterministico + Nao-Deterministico
- O SKILL.md (texto/instrucoes) e **nao-deterministico** -- rodar duas vezes da resultados diferentes
- Os **scripts** dentro da skill sao **deterministicos** -- sempre o mesmo output
- A combinacao dos dois e poderosa: a IA decide o que fazer (flexivel) e os scripts executam com precisao

---

## 4. SKILLS DEMONSTRADAS

### Skill 1: YouTube Video Creator
- **Funcao**: Dado um assunto, sugere thumbnails e titulos otimizados
- **Conteudo da pasta**:
  - `skill.md` -- Instrucoes de como analisar dados e sugerir
  - `/referencias/` -- Planilha com dados de performance (CTR, retencao, views) de videos proprios e concorrentes
  - `/thumbnails/` -- Imagens de concepts de capas (downfall, ranking, etc.)
- **Fluxo**: Descreve assunto -> skill analisa dados de performance -> identifica melhor concept de thumbnail -> sugere titulos e thumbs

### Skill 2: Branding de PowerPoint (Dopic)
- **Funcao**: Aplica identidade visual da empresa em apresentacoes
- **Conteudo**:
  - `skill.md` -- Descricao dos tipos de slides (capa, numeros, 3 colunas, 2 colunas)
  - Documentacao de marca
  - **Script Python** que aplica branding programaticamente no PPTX
- **Fluxo**: IA decide layout -> chama script Python -> script aplica cores e tipografia

### Skill 3: Proposal Generator (criada ao vivo)
- **Funcao**: Gera propostas comerciais para a consultoria Donus
- **Arquivos gerados automaticamente**:
  - `skill.md` -- Com roteiro de perguntas (cliente, problema, tipo de projeto, valor, prazo), estrutura padrao de proposta, tom de voz
  - Documento de tipos de projetos (auditoria de IA, implementacao de ferramentas, workshops, estrategia de produto, hibrido)
  - Documento sobre a empresa Donus (versao longa e curta)
- **Roteiro de perguntas no SKILL.md**:
  - Quem e o cliente?
  - Qual o problema principal?
  - Que tipo de projeto?
  - Valor do investimento?
  - Prazo esperado?
- **Demonstracao**: Criou proposta para iFood, R$50.000, tema "adocao de IA pelas liderancas", formato PDF, em ~5 minutos

### Skills Built-in Mencionadas
- **Skill de criar skill** (skill-builder / skill creator)
- **Skill de gerar Word**
- **Skill de gerar PDF**
- **Skill de gerar PowerPoint**
- Skill de SEO
- Skill de frontend design

---

## 5. ECOSSISTEMA DE SKILLS

### Instalacao e Gestao
- Skills sao **pastas versionaveis via Git** -- voce pode subir no GitHub e manter historico de versoes
- Instalacao: via botao "Upload Skill" nas **Capabilities** do Claude
- Formato de distribuicao: arquivo ZIP contendo a pasta da skill

### Listagem no System Prompt
- O sistema adiciona no system prompt apenas uma **lista com nome + descricao de uma linha** de cada skill disponivel
- Nao carrega o conteudo completo -- so carrega sob demanda quando a IA identifica que precisa

### Versionamento
- Como e uma pasta de arquivos, tem a vantagem natural de Git
- Historico completo de evolucao da skill
- Possibilidade de rollback

**Nota**: O video nao menciona explicitamente o site "skills.sh" -- o ecossistema demonstrado e centrado no Claude (web + Claude Code) com upload manual de skills.

---

## 6. WORKFLOWS DE USO

### Fluxo Basico
1. Voce tem um agente com system prompt enxuto
2. No system prompt, ha apenas a lista de skills disponiveis (nome + descricao curta)
3. Voce faz um pedido natural: "quero fazer um video de YouTube"
4. O agente identifica qual skill e relevante
5. O agente **le** o SKILL.md daquela skill (progressive disclosure)
6. O agente segue o roteiro da skill (faz perguntas, consulta referencias, executa scripts)
7. Entrega o resultado

### Fluxo de Evolucao
1. Voce conversa com o agente e descobre algo novo
2. Voce diz: "Registra isso na nossa skill pra proxima vez eu nao precisar te falar"
3. O agente atualiza o SKILL.md ou arquivos de referencia
4. Proxima conversa, a skill ja incorporou o aprendizado

### Composicao de Skills
- Uma skill pode chamar outra skill (mencionado no exemplo da proposta que poderia chamar uma skill de identidade visual)
- Permite modularidade: skill de conteudo + skill de design = proposta formatada

---

## 7. PADROES DE SKILL.MD

Baseado nos exemplos mostrados, um SKILL.md bem estruturado contem:

```markdown
# [Nome da Skill]

## Objetivo
[Descricao de 1-2 linhas do que a skill faz]

## Quando Usar
[Triggers: "Use essa skill sempre que o usuario mencionar X, Y, Z"]

## Roteiro de Perguntas
[Lista sequencial de informacoes que o agente deve coletar antes de executar]
1. Pergunta obrigatoria 1
2. Pergunta obrigatoria 2
...
- Informacao opcional A
- Informacao opcional B

## Tipos / Categorias
[Templates ou categorias padrao que a skill suporta]

## Estrutura Padrao do Output
[Como o resultado deve ser organizado]
- Secao 1
- Secao 2
- ...

## Tom de Voz
[Descricao do estilo de comunicacao]

## Ferramentas / Scripts
[Instrucoes de quando e como chamar scripts da pasta]
"Quando chegar na etapa X, execute o script Y com os parametros Z"

## Referencias
[Apontar para subpastas com dados, exemplos, imagens]
```

**Padroes observados**:
- Triggers explicitos (palavras-chave que ativam a skill)
- Roteiro de perguntas como "entrevista guiada"
- Separacao entre informacoes obrigatorias e opcionais
- Tom de voz definido explicitamente
- Instrucoes claras de quando chamar scripts
- Opcoes de output (PDF, Word, PowerPoint)

---

## 8. INSIGHTS ACIONAVEIS

### Para Aplicar Imediatamente

1. **System prompt enxuto + skills sob demanda** -- Nunca chumbar tudo no system prompt. Listar skills com nome + descricao de uma linha e carregar conteudo completo apenas quando necessario. Isso preserva a janela de contexto.

2. **Retroalimentacao ativa** -- Ao final de cada interacao produtiva, pedir ao agente para registrar aprendizados na skill. Isso cria um ciclo de melhoria continua sem deploy.

3. **Combinar deterministico + nao-deterministico** -- Usar scripts para operacoes que precisam de consistencia (aplicar branding, formatar documentos, calculos) e IA para decisoes criativas (escolha de layout, tom de voz, sugestoes).

4. **Versionar skills no Git** -- Tratar skills como codigo: versionamento, historico, possibilidade de compartilhar e colaborar.

5. **Skill de criar skill** -- Usar o proprio Claude para gerar a primeira versao de uma skill. Comecar simples ("quero uma skill para X") e iterar.

6. **Roteiro de perguntas no SKILL.md** -- Sempre incluir um roteiro de coleta de informacoes. Isso garante que o agente colete contexto suficiente antes de executar, mesmo que o usuario nao forneca tudo de inicio.

7. **Composicao modular** -- Criar skills pequenas e especializadas que podem ser combinadas (ex: skill de conteudo + skill de formatacao + skill de identidade visual).

8. **Progressive disclosure e a chave** -- O conceito mais importante do video. Carregar informacoes sob demanda, nao tudo de uma vez. Isso se aplica nao so a skills, mas a qualquer arquitetura de agente.

### Skills Uteis Para Criar (baseado no video)
- Proposta comercial
- Identidade visual / branding
- Geracao de conteudo (YouTube, blog, newsletter)
- Templates de documentos (Word, PDF, PPTX)
- SEO
- Frontend design
- Onboarding de funcionarios

---

**Fonte**: Video de Debora (canal sobre IA), provavelmente ligado a consultoria Donus/Dopic. Newsletter mencionada: "Deb GPT" no Substack.
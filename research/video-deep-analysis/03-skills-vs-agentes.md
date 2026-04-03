# Video 3: Agente de IA e coisa do passado. Agora eu so uso SKILLS.

**Canal:** Debora (Donus / DebGPT newsletter)
**URL:** https://www.youtube.com/watch?v=h_l8wCr7M2Q
**Duracao:** ~20 min

---

## Resumo Executivo

Skills sao playbooks modulares que a IA le sob demanda, substituindo a abordagem de chumbar toda instrucao no system prompt de um agente. A principal vantagem e o **progressive disclosure** -- o agente so carrega a skill quando precisa, preservando a janela de contexto. Skills sao pastas versionaveis (Git) contendo um arquivo MD principal, dados de referencia e scripts opcionais que funcionam como tools deterministicas. A retroalimentacao permite que a skill melhore com o tempo sem deploy: voce conversa com o agente e pede para ele registrar aprendizados na propria skill. O video demonstra a criacao de uma skill de propostas comerciais do zero usando o Claude (via "skill de criar skill") em menos de 5 minutos, incluindo instalacao nas capabilities e geracao de um PDF final.

---

## Processo Completo (passo a passo reproduzivel)

### Etapa 1: Entender a diferenca entre Agentes e Skills

**O que fazer:** Mapear as 4 dimensoes de comparacao antes de decidir o que construir.

**Como:**

| Dimensao | Agente tradicional | Agente + Skills |
|---|---|---|
| **System Prompt** | Monolitico, com tudo chumbado | Enxuto, so lista skills disponiveis (nome + 1 linha de descricao) |
| **Ferramentas (Tools)** | Definidas na arquitetura do agente (ex: nodes no n8n) | Scripts dentro da pasta da skill, chamados sob demanda |
| **Memoria** | Requer banco externo para salvar interacoes | Retroalimentacao: voce pede pro agente registrar aprendizados direto na skill |
| **Manutencao** | Requer deploy a cada mudanca | Conversa natural: "registra isso na skill pra proxima vez" |

**Ferramentas:** Qualquer LLM com suporte a system prompt + leitura de arquivos (Claude, Claude Code, etc.)

**Exemplo do video:** "Ao inves de chumbar todas as informacoes dos playbooks no system prompt, voce so diz quais skills ele tem. Se precisar, ai ele puxa o playbook da skill."

---

### Etapa 2: Estruturar a pasta da Skill

**O que fazer:** Criar uma pasta com a anatomia correta de uma skill.

**Como:**
```
minha-skill/
  skill.md              # Instrucao principal (o "playbook")
  references/           # Dados de referencia, planilhas, metricas
    dados-performance.csv
  assets/               # Imagens, thumbnails, templates
    thumbnail-ranking.png
    thumbnail-downfall.png
  scripts/              # Scripts deterministicos (tools)
    apply-branding.py
```

**Regras:**
1. O `skill.md` deve conter: objetivo da skill, quando usar, roteiro de perguntas, estrutura de output esperado, tom de voz
2. A pasta `references/` contem dados que o agente consulta para tomar decisoes (ex: metricas de performance de videos anteriores)
3. A pasta `scripts/` contem codigo deterministico que o agente chama quando a skill instrui (ex: script Python para aplicar branding em PowerPoint)

**Exemplo do video (skill YouTube):**
- `skill.md` com instrucoes de como gerar titulos e thumbnails
- `references/` com planilha de performance (views, CTR, retencao) de videos proprios e concorrentes
- `assets/thumbnails/` com concepts visuais (ranking, downfall, etc.) para o agente se inspirar

---

### Etapa 3: Combinar instrucoes nao-deterministicas com scripts deterministicos

**O que fazer:** Usar a skill MD para raciocinio criativo da IA e scripts para execucao precisa.

**Como:**
1. No `skill.md`, descreva o que o agente deve fazer em linguagem natural (nao-deterministico)
2. Quando precisar de resultado exato e reproduzivel, aponte para um script na pasta
3. O agente le o MD, raciocina, e quando chega na etapa do script, executa o codigo

**Exemplo do video (skill Branding PowerPoint):**
- `skill.md`: descreve tipos de slides (capa, numeros, 3 colunas, 2 colunas), cores e tipografia da marca
- `scripts/apply-branding.py`: aplica estilo de forma deterministica no .pptx
- Fluxo: IA decide o layout (nao-deterministico) -> script aplica branding (deterministico)

**Insight chave:** "Voce consegue combinar a caracteristica nao-deterministica das IAs com caracteristicas deterministicas que voce so tem quando roda codigo."

---

### Etapa 4: Implementar Progressive Disclosure

**O que fazer:** Configurar o system prompt do agente para listar skills sem carrega-las.

**Como:**
1. No system prompt do agente, adicione apenas uma lista com: nome da skill + descricao de 1 linha
2. NAO coloque o conteudo completo de nenhuma skill no system prompt
3. Quando o usuario pedir algo, o agente identifica qual skill usar, le o `skill.md` correspondente, e so entao carrega aquele contexto
4. Skills nao usadas nunca entram na janela de contexto

**Por que isso importa:** "Quanto mais voce usar da janela de contexto, menos efetiva vai ser a sua IA." O conceito vem da pesquisa sobre **progressive disclosure** -- revelar informacao apenas quando necessaria.

**Exemplo:** Se voce tem skills de SEO, frontend design e video YouTube, e esta fazendo design, so a skill de design e carregada. SEO e YouTube ficam de fora.

---

### Etapa 5: Configurar retroalimentacao (self-improvement)

**O que fazer:** Pedir ao agente para registrar aprendizados na propria skill.

**Como:**
1. Durante o uso, quando a conversa gerar um insight valioso, diga: "Registra isso na skill pra proxima vez eu nao precisar te falar de novo"
2. O agente vai editar o `skill.md` ou criar um novo arquivo na pasta de referencias
3. Versione com Git para manter historico de evolucao

**Vantagem sobre agentes tradicionais:** Nao precisa de deploy. A skill evolui organicamente pela conversa.

---

### Etapa 6: Criar uma Skill do zero usando "Skill de criar Skill"

**O que fazer:** Usar o proprio Claude para gerar a skill completa.

**Como:**
1. Abra o Claude (web ou Claude Code)
2. Diga: "Eu quero criar uma skill para [descreva o objetivo]"
3. Se o Claude tiver contexto suficiente, ele cria proativamente
4. Se nao tiver, ele faz um roteiro de perguntas para coletar informacoes
5. O resultado e um ZIP com a pasta da skill pronta

**O que o Claude gera automaticamente:**
- `skill.md` com objetivo, triggers de ativacao, roteiro de perguntas, estrutura de output, tom de voz
- Documentos de referencia contextuais (ex: tipos de projeto, dados da empresa)
- Opcao de output em Word, PDF ou PowerPoint (via skills auxiliares)

**Exemplo do video:** Skill de propostas comerciais para consultoria Donus:
- Triggers: "criar proposta", "elaborar proposta", "montar proposta"
- Roteiro: cliente, problema, tipo de projeto, valor, prazo, informacoes opcionais
- Tipos de projeto padrao: auditoria de IA, implementacao de ferramentas, workshops, estrategia de produto, projeto hibrido
- Estrutura: contexto do cliente > proposta > como trabalhar juntos > investimento > tom consultivo/confiante/empatico

---

### Etapa 7: Instalar e usar a Skill

**O que fazer:** Adicionar a skill nas capabilities do Claude.

**Como:**
1. Baixe o ZIP gerado
2. Acesse "Capabilities" no Claude
3. Clique em "Upload Skill" e adicione a pasta
4. Inicie uma nova conversa e ative a skill pelo trigger

---

## Referencias Citadas

| Tipo | Nome | Contexto |
|---|---|---|
| **Ferramenta** | Claude (web) | Plataforma principal para criar e usar skills |
| **Ferramenta** | Claude Code | Alternativa tecnica para criacao de skills |
| **Ferramenta** | n8n | Citado como exemplo de plataforma de agentes com system prompt e tools |
| **Conceito** | Progressive Disclosure | Tecnica de pesquisa: revelar informacao sob demanda para preservar context window |
| **Conceito** | Determinismo vs Nao-determinismo | Scripts sao deterministicos (mesmo input = mesmo output), LLMs nao |
| **Conceito** | Context Window | Janela de contexto -- quanto menos usar, mais efetiva a IA |
| **Conceito** | Retroalimentacao de Skills | Pedir ao agente para registrar aprendizados na skill |
| **Newsletter** | DebGPT (Substack) | Newsletter de IA da Debora, slides do video disponiveis la |
| **Empresa** | Donus | Consultoria da apresentadora, usada como exemplo pratico |
| **Ferramenta** | GitHub/Git | Versionamento de skills como pastas |
| **Formato** | Skill de criar Skill (Skill Creator) | Meta-skill que vem built-in no Claude |
| **Formato** | Skill de PDF/Word/PowerPoint | Skills auxiliares built-in para gerar documentos |
| **Ferramenta** | Python | Linguagem usada nos scripts deterministicos dentro das skills |

---

## Skills que Podem Ser Geradas

| Nome proposto | O que faria | Baseado em qual trecho |
|---|---|---|
| **skill-composer** | Compoe multiplas skills em sequencia para tarefas complexas (ex: gerar conteudo + aplicar branding + exportar PDF) | Trecho sobre combinar skill de conteudo com skill de identidade visual (19:56-20:06) |
| **skill-retrofeeder** | Automatiza a retroalimentacao: ao fim de cada conversa, sugere o que registrar na skill usada | Trecho sobre retroalimentacao e melhoria continua (2:44-3:00) |
| **progressive-loader** | Gera e otimiza o bloco de system prompt que lista skills com nome + descricao de 1 linha, otimizando para progressive disclosure | Trecho sobre listar skills no system prompt sem carregar conteudo (11:45-12:00) |
| **skill-anatomy-validator** | Valida a estrutura de uma pasta de skill (tem skill.md? references/? scripts sao chamados corretamente?) | Trecho sobre anatomia da skill como pasta (5:08-5:36) |
| **proposal-generator** | Gera propostas comerciais com roteiro de perguntas, tipos de projeto, tom de voz customizado, output em PDF/Word | Demo completa do video (13:10-19:13) |
| **yt-title-thumb-advisor** | Sugere titulos e thumbnails baseados em dados de performance e concepts visuais de referencia | Skill de YouTube da apresentadora (5:19-7:17) |
| **branding-applier** | Aplica identidade visual em documentos (PowerPoint, PDF) combinando instrucoes da marca com script deterministico | Exemplo do branding Dopic (8:09-10:26) |
| **skill-migrator** | Converte agentes n8n existentes em skills: extrai system prompt, tools e knowledge base e reorganiza como pasta de skill | Comparacao agentes vs skills (0:39-3:38) |

---

## Insights Nao-Obvios

1. **"Skill de fazer skill" ja existe built-in no Claude.** Voce nao precisa criar skills manualmente -- o Claude tem uma meta-skill que gera skills completas a partir de uma descricao. Isso significa que o proprio ecossistema e autoexpansivel.

2. **O roteiro de perguntas dentro da skill e o verdadeiro diferencial.** Nao e so a instrucao que importa, mas o fato de a skill definir quais perguntas fazer ao usuario quando falta contexto. Isso garante qualidade de output mesmo com input vago.

3. **Skills como pastas sao naturalmente versionaveis.** O fato de ser uma pasta (nao um prompt num banco de dados) significa que Git, PRs e code review se aplicam diretamente. Voce pode ter uma "v2" da skill e fazer diff com a "v1".

4. **A combinacao determinismo + nao-determinismo e o padrao de ouro.** O video destaca explicitamente que o poder real vem de combinar raciocinio criativo (LLM, nao-deterministico) com execucao precisa (script, deterministico). Isso e o equivalente a "IA decide O QUE fazer, codigo faz COMO".

5. **Retroalimentacao substitui deploy.** Em agentes tradicionais, cada melhoria requer deploy. Com skills, voce diz "registra isso na skill" e a melhoria e imediata. Isso muda radicalmente o ciclo de iteracao.

6. **O system prompt do agente com skills e CONTRA-INTUITIVAMENTE minimalista.** A tendencia natural e colocar mais informacao. O padrao correto e o oposto: system prompt minimo + lista de skills. O conteudo so entra quando necessario.

7. **Skills auxiliares (PDF, Word, PPTX) ja vem no Claude.** Alem da skill creator, o Claude vem com skills para gerar documentos em varios formatos. Isso permite que skills customizadas deleguem a formatacao final para skills built-in.

8. **A skill nao precisa ter scripts para ser util.** O exemplo do YouTube nao tinha nenhum script -- era puramente instrucao + dados de referencia + assets visuais. Scripts sao opcionais, so para quando voce precisa de determinismo.

---

## Conexoes com Skills Existentes (Arsenal)

### skill-builder
**Conexao direta e forte.** O video valida exatamente o que o skill-builder faz: gerar skills completas a partir de descricao. A demonstracao do "skill de criar skill" do Claude e basicamente o que o skill-builder do arsenal ja implementa. **Acao:** Incorporar o padrao de "roteiro de perguntas" como feature obrigatoria em toda skill gerada pelo skill-builder.

### prompt-engineer
**Conexao forte.** A estrutura do `skill.md` e essencialmente um system prompt otimizado com progressive disclosure. O prompt-engineer pode ser usado para otimizar o conteudo de skill MDs, especialmente a parte de triggers e roteiro de perguntas. **Acao:** Criar um modo "skill-prompt" no prompt-engineer que otimiza prompts especificamente para formato de skill.

### reference-finder
**Conexao media.** O video mostra que skills de alta qualidade dependem de dados de referencia (planilhas de performance, metricas, benchmarks). O reference-finder pode alimentar a pasta `references/` de qualquer skill com fontes fundamentadas. **Acao:** Integrar reference-finder como etapa opcional no pipeline de criacao de skills.

### trident
**Conexao conceitual.** O Trident orquestra multiplos agentes. O modelo de skills com progressive disclosure pode otimizar como o Trident carrega contexto para cada agente da triade. Em vez de cada agente carregar tudo, cada um carrega apenas as skills relevantes.

### ui-design-system
**Conexao indireta.** A skill de "frontend design" citada no video e analoga ao ui-design-system. A abordagem de skill (pasta com instrucoes + references + assets) poderia ser o formato de distribuicao do design system.

### component-architect
**Conexao indireta.** Se o component-architect for empacotado como skill, ele se beneficiaria do progressive disclosure -- so carregado quando o usuario pedir para componentizar algo.

### react-patterns
**Conexao indireta.** Mesma logica: react-patterns como skill so e carregado quando o contexto e React. Preserva context window em projetos multi-tech.

### sdd (Spec-Driven Development)
**Conexao media.** A estrutura da skill (objetivo, triggers, roteiro, estrutura de output) e essencialmente uma mini-spec. O SDD pode ser usado para definir a spec de novas skills antes de gerar o conteudo.

### context-tree
**Conexao forte.** O context-tree mapeia a estrutura do projeto. Ele pode ser estendido para tambem mapear as skills disponiveis e seus triggers, gerando automaticamente o bloco de progressive disclosure do system prompt.

### maestro
**Conexao forte.** O Maestro orquestra fluxos complexos. Com skills, o Maestro pode funcionar como o "system prompt enxuto" que decide quais skills carregar para cada etapa do fluxo, implementando progressive disclosure a nivel de orquestracao.

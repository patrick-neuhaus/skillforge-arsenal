# course-capture rationale

## Step 0: Pre-build Research

1. Concrete pain: Patrick capturou cursos Anthropic manualmente copiando texto da pagina e transcricao do YouTube; o processo exigiu correcoes repetidas de formato, hierarquia, login, UI e QA.
2. Frequency in 30 days: apareceu em 3 cursos reais: Introduction to agent skills, Introduction to subagents, AI Capabilities and Limitations.
3. Existing solution search:
   - Local SkillForge: nao ha skill local que capture cursos web + transcript + hierarquia.
   - Browser plugin existe, mas e ferramenta de navegacao, nao workflow de captura.
   - Meeting-sync processa transcricoes de reuniao, nao cursos.
   - Web scout encontrou MCPs/skills de YouTube transcript, mas focados em video isolado.
4. Why similar solutions do not serve: MCPs de YouTube transcript nao capturam texto de pagina, nao navegam curso autenticado, nao usam prints como pistas e nao organizam por curso.modulo.aula.
5. Core vs commodity: core. Codifica o jeito do Patrick estudar cursos e preparar material local para pesquisa/execucao.
6. Innovation token cost: medio-baixo. Skill textual sem script inicial; pode evoluir para script se houver uso repetido.
7. 2-hour spike alternative: ja houve spike real nos cursos Anthropic; gerou processo estabilizado e falhas conhecidas.
8. Deletion criterion: apagar ou fundir se nao for usada em 60 dias ou se um MCP de curso completo cobrir texto de pagina + transcript + hierarquia + QA.

## References used

- `browser-use:browser` para regras de navegacao visual no in-app browser.
- `meeting-sync` como referencia de workflow operacional, gates e output estruturado.
- `research-brief-factory` como referencia de triagem, evidencia local e anti-escopo.
- `skill-builder` para estrutura, Iron Law, Step 0 e validacao.

## Sources checked

- TubeMCP: https://tubemcp.com/
- YouTube Transcript MCP Server: https://mcp.so/server/mcp-youtube-transcript/jkawamoto
- Anthropic skill-creator guidance: https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- transcriptor-mcp listing: https://mcpservers.org/servers/samson-art/transcriptor-mcp

## Initial test target

Proximo teste sugerido: um curso novo sobre escalabilidade acessado via MCP/browser, com prints dos botoes de descricao/transcricao, para validar:

- deteccao de hierarquia curso.modulo.aula;
- captura de paginas sem video;
- transcript via UI quando API falhar;
- QA contra lixo de UI e mojibake.

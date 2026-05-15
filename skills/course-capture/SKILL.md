---
name: course-capture
description: "Captura cursos web autenticados ou publicos em arquivos de estudo. Use quando o usuario pedir: capturar curso, copiar aulas, salvar transcricao, pegar descricao do curso, extrair aula com YouTube, Skilljar, Hotmart, Skool, Udemy-like, Circle, PromovaWeb, MCP/browser, prints mostrando botoes, API interna, VTT/WebVTT, DOM, organizar modulos, criar pasta de estudo, gerar arquivos, validar QA, verificar transcript, montar curso.modulo.aula, transcript with timestamps. Faz navegar, listar, extrair, transcrever, organizar, criar, gerar, validar, verificar e reportar. Diferente de youtube-transcript puro: tambem captura texto da pagina e preserva hierarquia do curso."
---

# Course Capture

IRON LAW: Nunca capture so a transcricao. O entregavel e a aula completa: texto da pagina + transcricao no ponto do video + hierarquia fiel do curso.

## Boundary

Use esta skill para cursos web em que o usuario fornece URL, screenshots, instrucoes de botoes ou uma sessao autenticada. A skill organiza material de estudo localmente.

Nao e scraper generico de sites. Se o usuario pedir apenas um video YouTube isolado, use uma ferramenta de transcript/MCP se existir e nao aplique toda a hierarquia de curso.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--sample-first` | Captura uma aula amostra antes do curso inteiro | true |
| `--delegate` | Usa workers por curso/modulo quando disponivel | true |
| `--flat` | Salva tudo em uma pasta com prefixo numerico | false |
| `--module-folders` | Cria subpastas por modulo | true quando ha modulos claros |
| `--no-quiz-start` | Nao inicia quiz/exercicio que altera estado | true |

## Workflow

```
Course Capture Progress:

- [ ] Step 1: Intake REQUIRED
  - [ ] 1.1 Identificar URL(s), destino, screenshots e estado de login
  - [ ] 1.2 Definir se ha 1 curso ou varios cursos
  - [ ] 1.3 Confirmar politica de quiz/exercicios e credenciais
- [ ] Step 2: Mapear curso REQUIRED
  - [ ] 2.0 Checar qual ambiente autenticado esta acessivel para orquestrador e workers
  - [ ] 2.1 Listar cursos, modulos, aulas e duracoes quando existirem
  - [ ] 2.2 Definir esquema de nomes e pastas
  - [ ] 2.3 Escolher rota adaptativa: API/metadata/VTT, DOM visual, YouTube ou hibrido
  - [ ] GATE: apresentar plano de captura antes de bulk
- [ ] Step 3: Capturar amostra REQUIRED
  - [ ] 3.1 Capturar primeira aula representativa
  - [ ] 3.2 Inserir transcricao no ponto do video
  - [ ] 3.3 Rodar QA e corrigir formato
  - [ ] GATE: amostra aprovada antes de continuar
- [ ] Step 4: Capturar em waves
  - [ ] 4.1 Delegar por curso ou modulo quando houver volume
  - [ ] 4.2 Capturar paginas com video e sem video
  - [ ] 4.3 Validar cada wave
- [ ] Step 5: Checkpoint final
  - [ ] Arquivos criados, QA, riscos, pendencias
```

## Step 1: Intake REQUIRED

Pergunte:

Somente o que bloquearia a captura:

- Qual URL do curso ou da aula inicial?
- Onde salvar? Se nao houver destino, use `Documents/Cursos/<Fornecedor>/<Curso>`.
- Os screenshots mostram quais botoes importantes? Ex: abrir no YouTube, mostrar descricao, mostrar transcricao.
- Existe login? Se precisar credencial, use so para autenticar; nunca salve nem repita senha.
- Pode iniciar quiz/exercicio ou deve salvar apenas a tela visivel?

Se o usuario ja deu URL, destino e prints, siga sem perguntar.

## Step 2: Mapear Curso

Use o Browser plugin/MCP disponivel para olhar a tela. Prefira sinais visiveis do curso a suposicoes de URL.

Nao assuma que a rota visual e a melhor. Plataformas diferentes expoem conteudo de formas diferentes; escolha a rota pela evidencia da plataforma.

Mapeie:

- curso: titulo principal;
- modulos: titulos ou secoes laterais;
- aulas: titulo, ordem, duracao, tipo;
- video: embed, botao YouTube, player nativo ou ausencia de video;
- navegacao: Next/Previous, sidebar, accordion, botoes de modulo.

### Rota adaptativa

Teste nesta ordem, parando na primeira rota completa e verificavel:

1. API interna/autenticada da plataforma, quando a tela ja carregou dados via JSON.
2. Metadata de video/transcript, incluindo `media_transcript_id`, VTT ou WebVTT.
3. DOM visual da aula, com transcript expandido e scrollado ate o fim.
4. YouTube/transcript externo, somente quando a plataforma realmente depender dele.
5. Captura manual assistida, marcando pendencias, se nao houver transcript disponivel.

Regras:

- Compare contagem da UI visivel com contagem da API. Se a API listar aulas ocultas, arquivadas ou extras, prefira a hierarquia visivel ao usuario.
- No Circle/PromovaWeb, use `space.course_sections` para hierarquia; `courses/<id>/sections` pode trazer aulas nao visiveis.
- Use cookies/sessao apenas em memoria durante a execucao. Nunca salve credenciais, cookies ou tokens em arquivo, trace ou report.
- Se login bloquear, pare e peca orientacao. Nao tente contornar autenticacao.

### Nomeacao

Preserve a hierarquia no prefixo:

- Um curso, modulos e aulas: `1.3.7 - Titulo da aula.txt` significa curso 1, modulo 3, aula 7.
- Um curso sem modulos explicitos: `1.1.7 - Titulo da aula.txt`.
- Varios cursos no mesmo pedido: curso recebe indice pela ordem fornecida ou pela ordem da plataforma.
- Titulos repetidos usam o prefixo para diferenciar; nao sobrescreva `Try it out`.

Pastas:

- Se os modulos forem claros, prefira `Curso/03 - Nome do modulo/1.3.7 - Aula.txt`.
- Se a plataforma for flat, use `Curso/1.1.7 - Aula.txt`.

Antes de captura em massa, apresente plano curto: cursos, modulos, quantidade de aulas, destino e convencao de nomes.

## Step 3: Capturar Aula

Para cada aula:

1. Copie o texto visivel da pagina ate antes de Feedback, Previous, Next, comentarios ou rodape.
2. Se houver duracao, mantenha a linha como `(N minutes)` ou equivalente original.
3. Se houver video, capture a transcricao pela rota mais fiel disponivel:
   - API/metadata da plataforma com transcript pronto;
   - arquivo VTT/WebVTT;
   - endpoint interno de transcript;
   - painel `Mostrar transcricao` / `Show transcript`, expandido e scrollado ate o fim;
   - YouTube apenas se a aula depender dele.
4. Insira a transcricao logo apos a duracao ou no ponto onde o video aparece:

```text
(4 minutes)

---

0:07 Transcript line...
0:15 Transcript line...

---

Texto da pagina continua aqui.
```

5. Se nao houver video/transcricao, salve apenas o texto da pagina. Nao invente duracao nem transcricao.
6. Se houver video mas transcript estiver desativado, `is_ready=false`, sem VTT ou indisponivel, registre pendencia no arquivo/report. Nao invente.
7. Se for quiz/exercicio, nao inicie nem responda sem autorizacao explicita; salve a tela visivel e marque risco.

## Step 4: Orquestracao e Delegacao

Quando houver mais de um curso ou mais de 5 aulas, opere como orquestrador:

- Se a sessao estiver em `delegate-only`, o orquestrador pode suspender esse limite temporariamente so para discovery minimo: abrir uma aula, entender onde fica descricao/video/transcricao, mapear quantos cursos/modulos/aulas existem e decidir quantos workers usar. Registre no trace que foi process discovery e volte para delegate-only antes da captura em massa.
- O discovery minimo termina quando o orquestrador consegue explicar o procedimento para um worker. Se ja souber o processo pela plataforma, nao execute captura local: delegue direto.
- Antes de delegar captura autenticada, faca um check real: o worker enxerga o browser/sessao necessaria? Se `browsers.list()` ou equivalente vier vazio, nao delegue captura visual para esse worker.
- Delegue 1 worker por curso ou modulo, nao 1 worker por aula, salvo se as aulas forem muito longas.
- Workers de captura mecanica usam `reasoning_effort=low`, contrato autocontido e `fork_context=false` quando possivel.
- Primeiro peca para cada worker capturar uma aula amostra do seu curso/modulo. O orquestrador valida formato, transcript, hierarquia e QA antes de liberar o restante.
- Se a amostra falhar, mande uma corrective wave estreita para o mesmo worker corrigir antes de continuar.
- Workers nao decidem politica de quiz, credencial ou formato final.
- Se delegate-first estiver bloqueado por browser autenticado indisponivel nos workers, registre no trace, explique o bloqueio e peca autorizacao explicita antes de executar captura local no orquestrador.

Contrato minimo do worker:

- objetivo e URL;
- destino exato;
- convencao de nomes;
- processo de transcript;
- o que nao fazer;
- QA obrigatorio;
- formato de report.

## QA Obrigatorio

Rode QA por arquivo e por pasta:

- ASCII-only, salvo se o usuario pedir preservar acentos;
- separadores `---` antes/depois da transcricao quando houver video;
- linhas de transcricao com padrao `0:07 texto`;
- sem lixo de UI: `YouTube Summary`, `Inscrever-se`, `comentarios`, `Pesquisar transcricao`, `Feedback`, `Previous`, `Next`;
- sem timestamp duplicado em outro idioma: `2 minutos e 3 segundos`;
- sem mojibake: caracteres quebrados de encoding, como dash corrompido ou replacement character;
- termos tecnicos corrigidos de forma conservadora: `Claude`, `Claude Code`, `AGENTS.md`, `CLAUDE.md`, `subagent`, `skills`, `MCP`.

QA de transcript:

- Se usar VTT/WebVTT, remova cabecalho/cues duplicados e preserve timestamps legiveis.
- Se usar painel visual, verifique se ele foi expandido/scrollado ate o fim; painel parcial nao passa.
- Quando houver duracao, compare o ultimo timestamp com a duracao do video. Diferenca grande exige revisao ou pendencia explicita.
- Liste aulas com video mas sem transcript disponivel separadamente.

Nao trate palavras legitimas como erro so porque aparecem no regex. Ex: `Next Token Prediction`, `What's next`, `feedback do usuario` e `a aula foi concluida` podem ser conteudo da aula. Revise o contexto antes de classificar como lixo de UI.

## Output Final

Entregue checkpoint:

```markdown
Objetivo:
Destino:
Arquivos criados:
Hierarquia usada:
QA feito:
Riscos:
Pendencias:
Proximo teste recomendado:
```

## Anti-Patterns

- Capturar transcript via API/yt-dlp depois de 429 sem tentar o fluxo visual validado.
- Salvar so a transcricao e perder texto da pagina, exercicios, reflexoes e key takeaways.
- Esmagar a hierarquia do curso em `001, 002, 003` quando ha modulos claros.
- Iniciar quiz ou marcar resposta para "capturar mais conteudo" sem permissao.
- Pedir credenciais cedo demais; so peca quando o proximo passo realmente bloqueia.
- Repetir senha em report, arquivo ou trace.
- Usar worker caro/xhigh para captura mecanica.
- Assumir que subagents/workers enxergam o in-app browser autenticado sem testar.
- Tratar API interna como verdade absoluta quando ela lista aulas ocultas fora da UI.
- Capturar transcript visual sem expandir/scrollar e salvar so o trecho inicial.

## Example

Usuario: "Captura esse curso: https://example.com/course. Prints mostram botao Watch on YouTube e Show transcript. Salva em Documents/Cursos/Scale."

Skill:
- mapeia curso 1 com 3 modulos;
- cria `Scale/01 - Foundations/1.1.1 - Intro.txt`;
- insere transcript apos `(6 minutes)`;
- salva exercicio sem video como `1.2.4 - Try it out.txt`;
- entrega QA e pendencias.

PromovaWeb/Circle example:
- usa `space.course_sections` para hierarquia visivel;
- usa endpoint da lesson para texto;
- usa `media_transcript_id` + WebVTT para transcricao;
- marca pendencia quando transcript existe mas esta desativado/sem VTT.

## When NOT to use

- Video YouTube unico sem pagina de curso: use transcript tool/MCP direto.
- Reuniao/transcricao de call: use `meeting-sync`.
- Criar resumo ou research brief a partir dos materiais ja capturados: use `research-brief-factory`.
- Criar ou alterar esta skill: use `skill-builder` + validacao.

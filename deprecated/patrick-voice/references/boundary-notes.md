# patrick-voice — boundary com outras skills

## vs `copy`

`copy` escreve copy generica em multiplos canais (LP, sales page, VSL, social, email, ads, blog, etc). Cross-cliente, cross-projeto. Tom adaptavel.

`patrick-voice` e voz exclusiva do Patrick. Pessoal. Nao serve pra cliente da Artemis.

**Composicao:** `copy` define estrutura/argumento, `patrick-voice` aplica tom Patrick por cima quando o copy e do Patrick (post pessoal Linkedin/X, email pessoal, mensagem que ele assina nominalmente).

**Quando usar so copy:** copy de cliente, marketing institucional Artemis (terceira pessoa).
**Quando usar copy + patrick-voice:** post pessoal Patrick, email assinado por Patrick, msg WhatsApp Patrick.

## vs `comunicacao-clientes`

`comunicacao-clientes` lida com estrutura de mensagens cliente: Pyramid Principle, SCQA, NVC, Chris Voss. Cobre como abrir, escalar reclamacao, cobrar, negociar escopo.

`patrick-voice` aplica tom Patrick por cima da estrutura.

**Composicao:** `comunicacao-clientes` desenha a mensagem (estrutura + framework), `patrick-voice --canal=cliente` aplica registro pessoal.

**Quando usar so comunicacao-clientes:** mensagem cliente generica, qualquer pessoa da equipe pode mandar.
**Quando usar comunicacao-clientes + patrick-voice:** Patrick precisa enviar pessoalmente, com identidade reconhecivel.

## vs `prompt-engineer`

`prompt-engineer` valida/cria prompts pra LLMs (system prompts, agent instructions, technical plans, AGENTS.md, CLAUDE.md). Meta-skill.

`patrick-voice` gera texto humano-legivel no tom Patrick.

**Sem composicao normal.** Excecao: se Patrick quer documentar um prompt no estilo dele (instructions personalizadas pra Claude que reflitam voz dele).

## vs `tech-lead-pm`

`tech-lead-pm` lida com gestao de tasks, delegacao, estrutura de sprint, coaching juniors.

`patrick-voice` e tom de comunicacao.

**Composicao:** `tech-lead-pm` decide O QUE comunicar (qual task delegar pra quem, qual feedback dar), `patrick-voice` molda COMO comunicar.

## vs `meeting-sync`

`meeting-sync` extrai action items de transcricao, cruza com ClickUp, gera resumo.

`patrick-voice` gera texto.

**Composicao:** `meeting-sync` extrai e estrutura action items, `patrick-voice` redige se Patrick precisa anunciar resultado em grupo no tom dele.

## vs `lovable-router`

`lovable-router` decide entre direct edit vs prompt Lovable.

`patrick-voice` e voz Patrick.

**Composicao:** se `lovable-router` decide prompt Lovable pra Patrick, `patrick-voice --canal=tech` pode tornar prompt mais "patrick-style" (raro, geralmente prompt Lovable e descritivo objetivo).

## Quando NAO compor com nada

- Patrick pede mensagem rapida pessoal (msg pra alguem) → so patrick-voice
- Output direto pra Patrick aprovar e copiar/colar → so patrick-voice

## Re-validacao apos lock-in

Se patrick-voice estiver listada em `FIXES-APLICADOS.md` com `validated:YYYY-MM-DD`:
- IL-10 aplica (lock-in)
- Edits estruturais passam por confronto vocal Patrick
- Edits de description (triggering) sem ser por teste novo = bloqueado

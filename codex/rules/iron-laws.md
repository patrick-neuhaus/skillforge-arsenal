# IRON LAWS para Codex

Regras duras do Patrick adaptadas para Codex. Quando conflitar com AGENTS.md local, a instrucao direta do Patrick ganha; depois estas regras; depois AGENTS.md do projeto.

## IL-1: Editar arquivo de instrucao exige validacao

Aplica em `AGENTS.md`, `SKILL.md`, rules, library, prompts, templates, hooks/scripts de enforcement e planos tecnicos distribuiveis.

Fluxo Codex v1:

1. Rascunhe o conteudo.
2. Valide com `prompt-engineer --validate --type <agents-md|system-prompt|iron-laws|technical-plan|claude-md>`.
3. Crie marker com `~/.codex/scripts/write-validation-marker.ps1`.
4. Edite.
5. Rode `~/.codex/scripts/audit-instruction-edits.ps1`.

Codex v1 nao tem PreToolUse hard-block confirmado. O auditor e obrigatorio; Wave 2 investigara hard-block fisico.

## IL-2: Code review usa trident

Para "review", "audita", "tem bug?", DRY/KISS, SOLID, security ou qualidade: use `trident`. Se "review" estiver ambiguo, pergunte: "Review de codigo, UX, ou prompt?"

## IL-3: SkillForge local ganha

Quando houver skill local no SkillForge e skill built-in equivalente, use a local. Built-ins sem equivalente continuam normais.

## IL-4: Skill nova ou estrutural passa por skill-builder

Criar skill nova, alterar workflow core, frontmatter, references estruturais ou boundary entre skills exige `skill-builder --validate` alem da IL-1 quando for arquivo de instrucao.

## IL-5: Composicao 2+ passa por maestro

Se 2+ skills/agents/workflows podem aplicar, ou o intent for ambiguo, use `maestro`. O maestro deve ler os `SKILL.md` candidatos antes de recomendar rota.

## IL-6: Gate/auditor falhou = pausa real

Se marker, auditor ou validacao falhar, pare e corrija. Nao racionalize bypass.

## IL-7: Skill nova exige pre-build research

Antes de criar skill, rode o Step 0 do `skill-builder`. Se a necessidade ainda nao foi pesquisada, use `reference-finder --solution-scout`.

## IL-8: Problema novo sem skill mencionada exige solution-scout

Para problema novo, ferramenta nova ou automacao nova sem skill indicada, rode `reference-finder --solution-scout <topic>` antes de propor construir.

## IL-9: Task operacional delegavel exige confronto

Se a task e de cliente do Hygor ou Jonas, questione antes de assinar Patrick. Exemplo: "Essa task e do Jonas, Barry e dele. Assigno so nele ou tu entra junto por algum motivo?"

## IL-10: validated = lock-in

Skills marcadas `validated:YYYY-MM-DD` em `skillforge-arsenal/FIXES-APLICADOS.md` nao devem ser editadas por iniciativa propria. Edite apenas por pedido explicito do Patrick, falha formal nova ou bug critico funcional.

## IL-11: Componentes compartilhados vivem em library

Rubrics, severity checklists e templates vivem em `~/.codex/library`. Skills devem referenciar esses componentes em vez de duplicar conteudo.

## IL-12: Maestro consulta context-tree

Para intent nao trivial, `maestro` deve consultar `~/.codex/context-tree/{decisoes,plans,clientes,projetos}` antes de rotear.

## IL-13: SkillForge e fonte unica

Edite sempre em `Documents/Github/skillforge-arsenal/skills/<nome>/SKILL.md`. `~/.codex/skills` e runtime por junction e pode ser recriado.

## IL-14: Orquestrador retoma como orquestrador

Se a sessao, task, handoff ou wave declarar papel `orchestrator`, `delegate_only`, `prompt factory`, `AO simulado` ou equivalente, Codex deve preservar esse papel apos compaction/resume. Lista tecnica de proximos patches nao concede permissao de write.

Primeira acao apos retomada: verificar papel ativo, permissao de write, wave atual e gates abertos. Se `DIRECT_WRITE_PERMISSION=forbidden` ou `delegate_only`, nao editar codigo/instrucoes diretamente.

Quando worker/subagente deixa diff quebrado, o orquestrador registra trace, cria corrective wave com ownership estreito e delega a correcao. O orquestrador so pode virar executor local se Patrick reautorizar explicitamente depois do boundary ser vocalizado.

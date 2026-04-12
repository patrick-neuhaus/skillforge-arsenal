# Wave G Sync Checkpoint — 2026-04-11

Tracking file pra saber em que estado cada ambiente (Claude Code local, anthropic-skills marketplace, Claude.ai interface) está sincronizado com o skillforge-arsenal deste repo.

## Última atualização

- **Data/hora:** 2026-04-12 ~00:30 (Wave H) (UTC-3, horário de São Paulo)
- **Git commit base:** d3c2eb29d79a881b2488dcb5e8b17d368ed5c990 (Wave G ainda não commitada)
- **Executor:** Wave G (post-E2E corrections)
- **Skills modificadas:** 19 (re-upadas + o resto das Waves 1-6 que nunca tinha sido upado)

## Estado por ambiente

### Claude Code local (skillforge-arsenal)

- ✅ Todas as 40 skills presentes em `skills/`
- ✅ maestro/SKILL.md: 14 bugs Trident corrigidos (G2)
- ✅ context-tree/SKILL.md: unified reader + nota byterover built-in (G3)
- ✅ Zero `.bak` files (limpeza feita 2026-04-12 ~00:30 (Wave H))

### anthropic-skills marketplace

- ⏳ **Aguardando re-upload completo por Patrick** (apagou as antigas, re-upando as 40 agora)
- ⚠️ Conflito de nome: `pdf`, `xlsx`, `pptx`, `docx` são nativos do Claude — tiveram que ser renomeados pra upar (ex: `skillforge-pdf` ou similar)
- ⏳ Teste de validação: re-rodar Teste 4 em sessão fresh — `anthropic-skills:reference-finder` deve mostrar `--solution-scout` funcionando

### Claude.ai interface

- ⏳ **Aguardando upload completo por Patrick**
- ✅ System prompt: `CLAUDE-interface-system-prompt.md` (583 linhas) coladas em Settings > Profile > Personal Preferences
- ⏳ Skills upload: mesmos zips do `dist/`
- ⚠️ Mesmo conflito de nome pra pdf/xlsx/pptx/docx (renomear antes)

## Issues conhecidos descobertos durante re-upload

### 1. Conflito de nome com skills nativas do Claude

As skills `pdf`, `xlsx`, `pptx`, `docx` do skillforge-arsenal têm nomes idênticos às skills nativas do Claude (que cobrem manipulação genérica de documentos Office/PDF). O Claude.ai rejeita upload com mesmo nome.

**Workaround:** renomear essas 4 skills pra prefixadas (ex: `sf-pdf`, `sf-docx`, etc.) ANTES de upar. Ou aceitar que as versões do Patrick ficam só no CLI local (via `skills/` dir) e as nativas do Claude cobrem Claude.ai.

**Decisão a tomar na próxima wave:** renomear localmente (impacta IL-3 e skill-routing triggers) ou manter nome local e não upar essas 4 pro marketplace.

### 2. Bak files em zips (RESOLVIDO no maestro)

Erro operacional meu: ao fazer backup `SKILL.md.bak-pre-G2` antes do refactor, esqueci de limpar antes do zip. O `zip-skills.py` pegou o .bak junto. Resultado: `maestro.zip` original tinha 15302 bytes SKILL.md + 9988 bytes .bak dentro.

**Resolvido 2026-04-12 ~00:30 (Wave H):** .bak removido do dir, maestro re-zipado limpo (3 files: SKILL.md + 2 references). Patrick precisa re-upar SOMENTE o maestro.zip novo.

**MD5 do maestro.zip corrigido:** efcfe3f6d55c7f1133cae0e80fd0a791

### 3. Bak files em outras skills

Verificado 2026-04-12 ~00:30 (Wave H): nenhum outro zip tem `.bak` dentro. Só o maestro tinha. Grep completo em `skills/` não encontrou outros .bak files.

## Como verificar integridade de uma skill uploadada

Pra confirmar que uma skill no anthropic-skills/Claude.ai bate com a versão local:

```bash
# Unzippa o zip local e compara com a versão remota
cd /tmp && unzip "C:/Users/Patrick Neuhaus/Documents/Github/skillforge-arsenal/dist/<skill>.zip" -d <skill>-check
# Compara com a versão que o Claude reporta quando invoca a skill
# Se houver divergência, re-zipa e re-upa
```

**Indicadores de versão ANTIGA ainda ativa:**
- maestro retornando "Arsenal de Skills (32 skills)" = versão pré-Wave G
- reference-finder sem `--solution-scout` = versão pré-Wave 4
- context-tree sem menção a `.brv/context-tree/` = versão pré-Wave G

## Próximas sincronizações

Cada vez que uma skill for modificada aqui, atualizar este arquivo com:
- Data/hora
- Git commit hash
- Skills modificadas
- Issues encontrados no upload

---

## Instruções operacionais (mergeado de WAVE-G-FINAL-INSTRUCTIONS.md)

Ver tests/RETEST-WAVE-G.md para testes pendentes.
Ver SESSION-NARRATIVE.md para histórico completo da sessão.

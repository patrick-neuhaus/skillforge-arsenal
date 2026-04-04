# Cleanup Rules — Protocolo de Limpeza

Consulte este arquivo no **Step 2** (safety checks) e **Step 4** (cleanup final).

---

## Regra de Ouro

**.tmp/ e efemero.** Nao existe cenario onde .tmp/ deve sobreviver apos a analise. Se voce precisa de algo permanente, mova pra outro lugar ANTES de limpar.

## Pre-Clone Safety

### 1. Garantir .gitignore

```bash
# Verificar se .tmp/ esta no .gitignore
if ! grep -q "^\.tmp/" .gitignore 2>/dev/null; then
  echo ".tmp/" >> .gitignore
  echo "Added .tmp/ to .gitignore"
fi
```

### 2. Verificar espaco

```bash
# Checar espaco disponivel (evitar surpresas com repos grandes)
df -h . | tail -1
```

### 3. Verificar .tmp/ pre-existente

```bash
# Se ja existe .tmp/, avisar antes de sobrescrever
if [ -d ".tmp" ]; then
  echo "WARNING: .tmp/ already exists with:"
  ls -la .tmp/
  echo "Clean first with: rm -rf .tmp/"
fi
```

## Post-Clone Safety

### Remover .git

```bash
# SEMPRE remover .git do clone — evita confusao com o repo do projeto
rm -rf .tmp/*/.git
```

### Verificar tamanho

```bash
# Se o clone ficou grande demais, algo deu errado
du -sh .tmp/
# Regra: .tmp/ nao deveria ter mais que 100MB
# Se tem, voce provavelmente clonou demais
```

## Cleanup Final (Step 4)

### Sequencia Obrigatoria

```bash
# 1. Deletar .tmp/
rm -rf .tmp/

# 2. Confirmar que sumiu
if [ -d ".tmp" ]; then
  echo "ERROR: .tmp/ still exists!"
  ls -la .tmp/
  exit 1
else
  echo "OK: .tmp/ cleaned successfully"
fi

# 3. Verificar que nada foi staged acidentalmente
git status .tmp/ 2>/dev/null
```

### Se Cleanup Falha

Causas comuns e solucoes:

| Problema | Causa | Solucao |
|----------|-------|---------|
| "Permission denied" | Arquivo read-only do clone | `chmod -R u+w .tmp/ && rm -rf .tmp/` |
| "Directory not empty" | Processo usando arquivo | Fechar editor/processo, tentar novamente |
| ".tmp/ reappears" | Script recriando | Verificar se algum watcher/script recria |

## Checklist de Confirmacao

Antes de marcar a task como completa:

- [ ] `ls .tmp/ 2>/dev/null` retorna erro (diretorio nao existe)
- [ ] `git status` nao mostra .tmp/ em untracked
- [ ] `.gitignore` contem `.tmp/`
- [ ] Pattern document foi salvo em local permanente (nao em .tmp/)
- [ ] Nenhum arquivo de .tmp/ foi copiado pro projeto sem adaptacao

## Automacao

Se usar pattern-importer frequentemente, considere adicionar ao git hooks:

```bash
# .git/hooks/pre-commit (adicionar ao existente)
if [ -d ".tmp" ]; then
  echo "ERROR: .tmp/ directory exists. Clean up before committing."
  echo "Run: rm -rf .tmp/"
  exit 1
fi
```

Isso previne commits acidentais com .tmp/ mesmo se .gitignore falhar.

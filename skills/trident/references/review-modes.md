# Review Modes — Detailed Commands

Consulte este arquivo no **Phase 1** quando precisar dos comandos exatos por modo.

---

## Auto-Detection Logic

```
1. User provided GitHub PR URL?              → mode = pr
2. User provided PR number (#123)?           → mode = pr
3. User said "PR" or "pull request"?         → mode = pr (fetch via gh pr view)
4. User provided commit range (abc..def)?    → mode = range
5. User provided branch name?                → mode = range (main..branch)
6. User said "since" / "from" / "after"?     → mode = range
7. User provided directory path?             → mode = dir
8. User said "staged"?                       → mode = staged
9. User said "all" / "everything"?           → mode = all-local
10. Default                                  → mode = unstaged
```

## Commands by Mode

### unstaged (default)
```bash
git status -sb
git diff --stat
git diff
```

### staged
```bash
git status -sb
git diff --cached --stat
git diff --cached
```

### all-local
```bash
git status -sb
git diff HEAD --stat
git diff HEAD
```

### pr
```bash
gh pr view {N} --json title,body,author,baseRefName,headRefName,files,additions,deletions
gh pr diff {N}
```
Include PR title, description, author intent in `{CONTEXT}`.

### range
```bash
git log --oneline {A}..{B}
git diff --stat {A}..{B}
git diff {A}..{B}
```
Include commit messages in `{CONTEXT}` for intent understanding.

### dir
```bash
# No diff — scan all files
find {DIR} -type f \( -name "*.ts" -o -name "*.py" -o -name "*.go" -o -name "*.js" -o -name "*.jsx" -o -name "*.tsx" \) | head -50
```

## Context Enrichment (all modes)

After gathering the diff/files:
1. Use `rg` or `grep` to find related modules and usages
2. Identify entry points, ownership boundaries, critical paths (auth, payments, data writes)
3. For `pr` mode: include PR metadata in `{CONTEXT}`
4. For `range` mode: include commit messages in `{CONTEXT}`

## Edge Cases

- **Empty diff (unstaged):** auto-try staged. If both empty, ask user for pr/range.
- **Large diff (>500 lines):** summarize by file first, then pipeline in batches by module.
- **Mixed concerns:** group findings by logical feature, not file order.
- **PR not found:** suggest checking PR number or providing diff manually.
- **Branch divergence:** for range with >100 commits, warn about scope.

## Setting Placeholders

- **`{TARGET}`**: file list, diff content, or directory path
- **`{CONTEXT}`**: review mode, PR metadata, commit messages, what the code does, areas of concern
- **`{REVIEW_MODE}`**: the mode string (unstaged, staged, pr, range, dir)

# Windows Shell Preferences para Codex

- Use PowerShell no Windows para comandos locais.
- Para busca, prefira `rg`; se falhar por acesso, use PowerShell nativo.
- Para editar arquivos, use `apply_patch` quando estiver atuando como Codex.
- Nao use comandos destrutivos (`git reset --hard`, `git checkout --`, deletes recursivos) sem pedido explicito.
- Paths com espaco devem usar `-LiteralPath` ou aspas.
- Python no Windows geralmente e `python` ou `py`, nao `python3`.
- Para junctions, use `New-Item -ItemType Junction` e verifique `LinkType`.

# Tecnica .tmp — Importar Padroes de Repos Externos

Consulte este arquivo no **Phase 1, Step 7** quando precisar de patterns de referencia.

---

## O que e

"Few-shot learning manual" (Video 4). Clonar um trecho de repo de referencia numa pasta temporaria, pedir ao Claude analisar o padrao, e depois deletar. Transfere conhecimento de projetos maduros pro seu projeto.

## Quando Usar

- Implementando algo pela primeira vez (auth flow, payment, rich-text editor)
- Padrao complexo que precisa de referencia (drag-and-drop, real-time sync)
- Lib nova sem experiencia previa (ProseMirror, Remotion, Motion)
- Quer garantir que esta seguindo best practices de implementacao

## Processo Passo a Passo

### Step 1: Identificar Repo de Referencia

Buscar repo que implementa o padrao desejado:
- GitHub search: `[padrao] language:typescript stars:>100`
- Perguntar ao Claude: "Qual repo open source implementa bem [X]?"
- Docs oficiais de libs geralmente linkam exemplos

### Step 2: Clone Parcial

```bash
# Opcao A: Clone completo em .tmp (repos pequenos)
git clone --depth 1 <repo-url> .tmp/reference-name
# Remover .git pra nao confundir
rm -rf .tmp/reference-name/.git

# Opcao B: Download de pasta especifica (repos grandes)
# Usar degit ou download direto
npx degit user/repo/path/to/folder .tmp/reference-name

# Opcao C: Copiar apenas os arquivos relevantes
mkdir -p .tmp/reference-name
# Copiar manualmente os 3-5 arquivos que importam
```

### Step 3: Analisar com Claude

Prompt exato:
```
"Analisa o padrao de implementacao em .tmp/reference-name/.
Foco em:
1. Estrutura de arquivos e organizacao
2. Padroes de composicao (como componentes se conectam)
3. Tratamento de edge cases
4. O que posso reutilizar no meu projeto

NAO sugira melhorias — apenas documente o padrao como ele e."
```

### Step 4: Extrair e Documentar

Documentar o padrao extraido no prd.md:
```markdown
## External Pattern Reference
**Source:** [repo-url]
**Pattern:** [nome do padrao]
**Key files analyzed:** [lista]
**Applicable to our project:**
- [insight 1]
- [insight 2]
- [diferenca: no repo usam X, no nosso usamos Y]
```

### Step 5: Limpar

```bash
# OBRIGATORIO — nunca deixar .tmp pra tras
rm -rf .tmp/
# Verificar que sumiu
ls .tmp/ 2>/dev/null || echo "Clean!"
```

Adicionar `.tmp/` no `.gitignore` como safety net:
```
# .gitignore
.tmp/
```

## Anti-Patterns

- **Clonar repo inteiro sem necessidade** — clone parcial ou degit sao mais rapidos
- **Esquecer de limpar .tmp/** — IRON LAW: nunca deixar atras
- **Copiar codigo direto** — o objetivo e entender o PADRAO, nao copiar implementacao
- **Analisar muitos repos** — 1-2 repos de referencia e suficiente. Mais confunde
- **Nao adaptar ao contexto** — patterns de repos com Next.js 14 podem nao aplicar a Next.js 15

## Exemplo Real

**Cenario:** Implementar rich-text editor com TipTap

```bash
# 1. Clone referencia
git clone --depth 1 https://github.com/steven-tey/novel .tmp/novel
rm -rf .tmp/novel/.git

# 2. Analisar com Claude
# "Analisa .tmp/novel/packages/core/src/ — foco em como o editor e configurado,
# quais extensions usam, e como toolbar e componente se conectam"

# 3. Extrair insight: Novel usa EditorContent + custom Bubble Menu
# Documentar no prd.md

# 4. Limpar
rm -rf .tmp/
```

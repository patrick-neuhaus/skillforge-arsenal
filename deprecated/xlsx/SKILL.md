---
name: xlsx
description: "Cria, edita, lê, analisa, formata, recalcula e valida planilhas Excel (.xlsx, .xlsm, .csv, .tsv). Gera modelos financeiros com fórmulas dinâmicas, limpa dados tabulares, constrói dashboards com gráficos, aplica formatação profissional e verifica erros de fórmula. Use quando: criar planilha, editar xlsx, modelo financeiro, formatar Excel, limpar dados CSV, gráfico no Excel, fórmula Excel, recalcular, validar erros, 'arrumar planilha', 'montar modelo', exportar dados. Triggers: 'planilha', 'spreadsheet', 'Excel', '.xlsx', '.csv', 'tabela de dados', 'modelo financeiro', 'financial model'. NÃO use quando o entregável é Word (use docx), HTML, script Python standalone, pipeline de banco, ou Google Sheets API."
license: Proprietary. LICENSE.txt has complete terms
---

# XLSX Skill

IRON LAW: NUNCA manipule dados de planilha sem entender a estrutura primeiro. Uma referência de coluna errada corrompe a cadeia de cálculos inteira.

## Quick Reference

| Tarefa | Abordagem |
|--------|-----------|
| Ler/analisar dados | pandas `pd.read_excel()` |
| Criar com fórmulas e formatação | openpyxl — Load [references/openpyxl-guide.md](references/openpyxl-guide.md) |
| Modelo financeiro | Load [references/financial-standards.md](references/financial-standards.md) |
| Recalcular fórmulas | `python scripts/recalc.py output.xlsx` |

## Checklist do Workflow

```
XLSX Skill Progress:

- [ ] 1. Entender o contexto ⚠️ REQUIRED
  - [ ] 1.1 O que a planilha deve fazer? (relatório, modelo, dashboard, limpeza)
  - [ ] 1.2 Dados existentes ou criar do zero?
  - [ ] 1.3 Tem template/formato que deve seguir?
  - [ ] 1.4 Precisa de fórmulas dinâmicas ou dados estáticos?
  - [ ] 1.5 Quem vai usar? (técnico, gestor, cliente)
- [ ] 2. Planejar estrutura
  - [ ] 2.1 Mapear colunas e tipos de dados
  - [ ] 2.2 Se financeiro: Load `references/financial-standards.md`
  - [ ] 2.3 Escolher ferramenta: pandas (dados) ou openpyxl (fórmulas/formatação)
  - [ ] ⛔ GATE: Confirmar estrutura com o usuário antes de gerar
- [ ] 3. Construir (em waves)
  - [ ] 3.1 Wave 1: Estrutura + dados + fórmulas básicas
  - [ ] 3.2 Wave 2: Formatação + validação + gráficos
  - [ ] 3.3 Wave 3: Recalcular + verificar erros + polish
- [ ] 4. Validar ⚠️ REQUIRED
  - [ ] 4.1 Recalcular: `python scripts/recalc.py output.xlsx`
  - [ ] 4.2 Verificar JSON de retorno — ZERO erros
  - [ ] 4.3 Testar 2-3 fórmulas manualmente
  - [ ] ⛔ GATE: Confirmar com usuário antes de sobrescrever arquivo original
- [ ] 5. Entregar
  - [ ] 5.1 Rodar pre-delivery checklist
  - [ ] 5.2 Nomear arquivo corretamente
```

## Regra Crítica: Fórmulas, Não Hardcode

**SEMPRE use fórmulas Excel em vez de calcular no Python e hardcodar o resultado.** A planilha deve ser dinâmica e atualizável.

```python
# ERRADO - hardcodando resultado
total = df['Sales'].sum()
sheet['B10'] = total  # Hardcoda 5000

# CORRETO - fórmula Excel
sheet['B10'] = '=SUM(B2:B9)'
```

Isso vale pra TODOS os cálculos — totais, percentuais, ratios, diferenças, etc.

## Leitura e Análise de Dados

```python
import pandas as pd

# Ler Excel
df = pd.read_excel('file.xlsx')                        # Primeira aba
all_sheets = pd.read_excel('file.xlsx', sheet_name=None)  # Todas as abas como dict

# Analisar
df.head()      # Preview
df.info()      # Info das colunas
df.describe()  # Estatísticas

# Escrever
df.to_excel('output.xlsx', index=False)
```

## Workflow Comum

1. **Escolher ferramenta**: pandas pra dados, openpyxl pra fórmulas/formatação
2. **Criar/Carregar**: Novo workbook ou arquivo existente
3. **Modificar**: Dados, fórmulas, formatação
4. **Salvar**: Gravar no arquivo
5. **Recalcular fórmulas (OBRIGATÓRIO SE USAR FÓRMULAS)**:
   ```bash
   python scripts/recalc.py output.xlsx
   ```
6. **Verificar e corrigir erros**: O script retorna JSON com detalhes

Load [references/openpyxl-guide.md](references/openpyxl-guide.md) para código detalhado de criação, edição, e formatação.

## Recalculando Fórmulas

```bash
python scripts/recalc.py <arquivo_excel> [timeout_segundos]
```

O script:
- Configura macro do LibreOffice automaticamente no primeiro uso
- Recalcula todas as fórmulas em todas as abas
- Escaneia TODAS as células pra erros (#REF!, #DIV/0!, etc.)
- Retorna JSON com localizações e contagens de erros

### Interpretando o Output

```json
{
  "status": "success",
  "total_errors": 0,
  "total_formulas": 42,
  "error_summary": {}
}
```

Se `status` = `errors_found`, cheque `error_summary` para tipos e localizações específicas. Corrija e recalcule novamente.

## Confirmation Gates

⛔ **Antes de sobrescrever arquivo existente:** "O arquivo [nome] já existe. Confirma substituição?"

⛔ **Antes de deletar dados/abas:** "Confirma exclusão de [aba/coluna/dados]? Essa ação não tem undo."

⛔ **Antes de aplicar formatação em planilha com template:** "O arquivo tem formatação própria. Confirma que quer aplicar novo estilo? (pode perder formatação existente)"

## Anti-Patterns

| Anti-pattern | Por que é ruim | O que fazer |
|---|---|---|
| Calcular no Python e hardcodar | Planilha morta, não atualiza quando dados mudam | SEMPRE fórmulas Excel (`=SUM()`, `=AVERAGE()`, etc.) |
| Abrir com `data_only=True` e salvar | Fórmulas são substituídas por valores, perda permanente | Usar `data_only=True` SÓ pra leitura, nunca salvar depois |
| Referências hardcoded em fórmulas | `=B5*1.05` — quem muda o 1.05? | Célula de premissa + referência: `=B5*(1+$B$6)` |
| Ignorar recalc.py | Fórmulas são strings até recalcular, valores ficam vazios | SEMPRE rodar `scripts/recalc.py` após criar/editar |
| Não verificar mapeamento de colunas | Coluna 64 = BL, não BK. Off-by-one corrompe tudo | Testar 2-3 referências antes de construir modelo |
| Esquecer row offset | DataFrame row 5 = Excel row 6 (1-indexed) | Sempre lembrar que Excel é 1-based |
| Print statements desnecessários | Poluem output, não agregam valor | Código mínimo e conciso |
| Formatação inconsistente | Parece amador, confunde o leitor | Fonte consistente, cores padronizadas, alinhamento uniforme |
| NaN não tratado | Propaga erros em cálculos downstream | Checar com `pd.notna()` antes de operar |

## Pre-Delivery Checklist

Antes de considerar a planilha pronta:

- [ ] `scripts/recalc.py` rodado com `status: success` e ZERO erros
- [ ] 2-3 fórmulas testadas manualmente (valor correto)
- [ ] Mapeamento de colunas verificado (especialmente coluna 50+)
- [ ] Nenhum valor hardcodado onde deveria ter fórmula
- [ ] Fonte profissional e consistente (Arial, Calibri, etc.)
- [ ] Formatação de números correta (moeda, %, datas)
- [ ] Se financeiro: color coding aplicado (Load `references/financial-standards.md`)
- [ ] Premissas em células separadas (não embutidas em fórmulas)
- [ ] Nomes de abas descritivos
- [ ] Largura de colunas ajustada pro conteúdo
- [ ] Sem células com erro (#REF!, #DIV/0!, #VALUE!, #N/A, #NAME?)

## Quando NÃO Usar Esta Skill

- **Documento Word/relatório formatado** → use `docx`
- **PDF com tabelas** → use `pdf`
- **Apresentação com dados** → use `pptx` (que pode integrar dados de xlsx)
- **Google Sheets API** → fora do escopo, é integração de API
- **Pipeline de banco de dados** → use `supabase-db-architect`
- **Script Python standalone de análise** → não precisa de skill, é código normal
- **Confuso sobre qual skill usar** → invoque `maestro`

## Integração

| Skill | Quando combinar |
|-------|----------------|
| `pdf` | Extrair tabelas de PDF pra planilha. Ou converter planilha pra PDF. |
| `docx` | Dados da planilha viram tabelas no Word. Ou extrair dados de Word pra Excel. |
| `pptx` | Dados de planilha viram gráficos em slides. |
| `maestro` | Projeto envolve múltiplos formatos. Maestro orquestra. |
| `supabase-db-architect` | Dados vêm do banco ou vão pro banco. Validar schema antes. |
| `n8n-architect` | Automação que gera/processa planilhas. |

## Referências

| Arquivo | Conteúdo |
|---------|----------|
| [references/openpyxl-guide.md](references/openpyxl-guide.md) | Criação, edição, formatação, código detalhado openpyxl + pandas |
| [references/financial-standards.md](references/financial-standards.md) | Color coding, formatação de números, premissas, documentação de hardcodes |

## Dependências

- `openpyxl` — criação e edição com fórmulas/formatação
- `pandas` + `openpyxl` — leitura e análise de dados
- LibreOffice — recalculação de fórmulas (via `scripts/recalc.py`)

## Estilo de Código

**IMPORTANTE**: código Python pra operações Excel:
- Escreva código mínimo e conciso, sem comentários desnecessários
- Evite nomes de variáveis verbosos e operações redundantes
- Evite print statements desnecessários

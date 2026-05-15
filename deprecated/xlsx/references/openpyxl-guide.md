# Guia openpyxl + pandas

## Criando Novos Arquivos Excel

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = Workbook()
sheet = wb.active

# Adicionar dados
sheet['A1'] = 'Hello'
sheet['B1'] = 'World'
sheet.append(['Row', 'of', 'data'])

# Adicionar fórmula
sheet['B2'] = '=SUM(A1:A10)'

# Formatação
sheet['A1'].font = Font(bold=True, color='FF0000')
sheet['A1'].fill = PatternFill('solid', start_color='FFFF00')
sheet['A1'].alignment = Alignment(horizontal='center')

# Largura de coluna
sheet.column_dimensions['A'].width = 20

wb.save('output.xlsx')
```

## Editando Arquivos Existentes

```python
from openpyxl import load_workbook

wb = load_workbook('existing.xlsx')
sheet = wb.active  # ou wb['NomeDaAba']

# Trabalhando com múltiplas abas
for sheet_name in wb.sheetnames:
    sheet = wb[sheet_name]

# Modificar células
sheet['A1'] = 'Novo Valor'
sheet.insert_rows(2)
sheet.delete_cols(3)

# Adicionar nova aba
new_sheet = wb.create_sheet('NovaAba')
new_sheet['A1'] = 'Dados'

wb.save('modified.xlsx')
```

## Checklist de Verificação de Fórmulas

### Verificação Essencial
- [ ] **Testar 2-3 referências de amostra**: Verificar que puxam valores corretos antes de construir modelo completo
- [ ] **Mapeamento de colunas**: Confirmar que colunas Excel batem (ex: coluna 64 = BL, não BK)
- [ ] **Row offset**: Lembrar que Excel rows são 1-indexed (DataFrame row 5 = Excel row 6)

### Armadilhas Comuns
- [ ] **NaN handling**: Checar valores nulos com `pd.notna()`
- [ ] **Colunas distantes**: Dados FY frequentemente em colunas 50+
- [ ] **Múltiplas ocorrências**: Buscar todas, não só a primeira
- [ ] **Divisão por zero**: Checar denominadores antes de usar `/` em fórmulas (#DIV/0!)
- [ ] **Referências erradas**: Verificar que referências apontam pras células corretas (#REF!)
- [ ] **Referências cross-sheet**: Usar formato correto (Sheet1!A1)

### Estratégia de Teste
- [ ] **Comece pequeno**: Testar fórmulas em 2-3 células antes de aplicar amplamente
- [ ] **Verificar dependências**: Checar que todas as células referenciadas existem
- [ ] **Testar edge cases**: Incluir zero, negativos e valores muito grandes

## Best Practices

### Seleção de Biblioteca
- **pandas**: Melhor pra análise de dados, operações em massa, export simples
- **openpyxl**: Melhor pra formatação complexa, fórmulas, features específicas de Excel

### Trabalhando com openpyxl
- Índices de célula são 1-based (row=1, column=1 = célula A1)
- Use `data_only=True` pra ler valores calculados: `load_workbook('file.xlsx', data_only=True)`
- **CUIDADO**: Se abrir com `data_only=True` e salvar, fórmulas são substituídas por valores — perda permanente
- Pra arquivos grandes: `read_only=True` pra leitura ou `write_only=True` pra escrita
- Fórmulas são preservadas mas não calculadas — use `scripts/recalc.py` pra atualizar valores

### Trabalhando com pandas
- Especifique tipos de dados: `pd.read_excel('file.xlsx', dtype={'id': str})`
- Pra arquivos grandes, leia colunas específicas: `pd.read_excel('file.xlsx', usecols=['A', 'C', 'E'])`
- Trate datas corretamente: `pd.read_excel('file.xlsx', parse_dates=['date_column'])`

## Exemplos de Fórmulas Corretas vs Erradas

### ERRADO - Hardcodando Valores Calculados
```python
# Ruim: Calculando no Python e hardcodando
total = df['Sales'].sum()
sheet['B10'] = total  # Hardcoda 5000

# Ruim: Growth rate no Python
growth = (df.iloc[-1]['Revenue'] - df.iloc[0]['Revenue']) / df.iloc[0]['Revenue']
sheet['C5'] = growth  # Hardcoda 0.15

# Ruim: Média no Python
avg = sum(values) / len(values)
sheet['D20'] = avg  # Hardcoda 42.5
```

### CORRETO - Usando Fórmulas Excel
```python
# Bom: Excel calcula o SUM
sheet['B10'] = '=SUM(B2:B9)'

# Bom: Growth rate como fórmula Excel
sheet['C5'] = '=(C4-C2)/C2'

# Bom: Average via função Excel
sheet['D20'] = '=AVERAGE(D2:D19)'
```

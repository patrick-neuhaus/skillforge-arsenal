# Padrões para Modelos Financeiros

## Requisitos para Todos os Arquivos Excel

### Fonte Profissional
- Fonte consistente e profissional (ex: Arial, Times New Roman) em todos os entregáveis, a não ser que o usuário instrua diferente

### Zero Erros de Fórmula
- Todo modelo Excel DEVE ser entregue com ZERO erros de fórmula (#REF!, #DIV/0!, #VALUE!, #N/A, #NAME?)

### Preservar Templates Existentes
- Estudar e seguir EXATAMENTE formato, estilo e convenções existentes ao modificar arquivos
- Nunca impor formatação padronizada em arquivos com padrões estabelecidos
- Convenções do template existente SEMPRE sobrescrevem estas diretrizes

## Color Coding (Padrão da Indústria)

A não ser que o usuário ou template existente diga diferente:

| Convenção | Cor | RGB | Uso |
|-----------|-----|-----|-----|
| Inputs hardcoded | Azul | 0,0,255 | Números que o usuário vai mudar pra cenários |
| Fórmulas/cálculos | Preto | 0,0,0 | TODAS as fórmulas e cálculos |
| Links internos | Verde | 0,128,0 | Links puxando de outras abas do mesmo workbook |
| Links externos | Vermelho | 255,0,0 | Links pra outros arquivos |
| Premissas-chave | Fundo amarelo | 255,255,0 | Células que precisam de atenção ou atualização |

## Formatação de Números

| Tipo | Formato | Exemplo |
|------|---------|---------|
| Anos | Texto (string) | "2024" (não "2,024") |
| Moeda | $#,##0 | Sempre especificar unidades no header: "Revenue ($mm)" |
| Zeros | Traço | `$#,##0;($#,##0);-` (inclui percentuais) |
| Percentuais | 0.0% | Uma casa decimal por padrão |
| Múltiplos | 0.0x | Pra múltiplos de avaliação (EV/EBITDA, P/E) |
| Negativos | Parênteses | (123) não -123 |

## Regras de Construção de Fórmulas

### Posicionamento de Premissas
- Colocar TODAS as premissas (taxas de crescimento, margens, múltiplos, etc.) em células separadas
- Usar referências de célula em vez de valores hardcoded nas fórmulas
- Exemplo: Usar `=B5*(1+$B$6)` em vez de `=B5*1.05`

### Prevenção de Erros
- Verificar todas as referências de célula
- Checar erros off-by-one em ranges
- Garantir fórmulas consistentes em todos os períodos de projeção
- Testar com edge cases (zeros, negativos)
- Verificar que não há referências circulares não intencionais

### Documentação de Hardcodes
- Comentar ou colocar em células ao lado (se fim de tabela)
- Formato: "Source: [Sistema/Documento], [Data], [Referência Específica], [URL se aplicável]"
- Exemplos:
  - "Source: Company 10-K, FY2024, Page 45, Revenue Note, [SEC EDGAR URL]"
  - "Source: Company 10-Q, Q2 2025, Exhibit 99.1, [SEC EDGAR URL]"
  - "Source: Bloomberg Terminal, 8/15/2025, AAPL US Equity"
  - "Source: FactSet, 8/20/2025, Consensus Estimates Screen"

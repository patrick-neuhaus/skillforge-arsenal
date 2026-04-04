# Riscos de código gerado por IA

Apps Lovable, Cursor, e Copilot têm padrões de vulnerabilidade específicos. Stanford Research Lab mostrou que desenvolvedores com AI assistants produzem código mais inseguro E se sentem mais confiantes sobre a segurança — falsa sensação de proteção.

## Padrões de vulnerabilidade comuns em código AI-generated

### 1. Input validation ausente

AI frequentemente omite bounds checks e type validation. Gera o "happy path" sem considerar inputs maliciosos.

```typescript
// AI GERA ISSO:
const amount = req.body.amount;
await transferFunds(userId, amount);

// DEVERIA SER ISSO:
const amount = Number(req.body.amount);
if (isNaN(amount) || amount <= 0 || amount > MAX_TRANSFER) {
  throw new ValidationError('Invalid amount');
}
await transferFunds(userId, amount);
```

### 2. Secrets hardcoded

AI gera exemplos com API keys reais ou placeholders que ficam no código final.

### 3. SQL injection

AI gera queries concatenadas em vez de parametrizadas.

```typescript
// AI GERA ISSO:
const result = await db.query(`SELECT * FROM users WHERE name = '${name}'`);

// DEVERIA SER ISSO:
const result = await db.query('SELECT * FROM users WHERE name = $1', [name]);
```

### 4. Auth checks faltando

AI esquece middleware em rotas que deveriam ser protegidas. Gera endpoints sem verificar se o usuário está autenticado ou tem permissão.

### 5. Error handling expondo info

AI gera catch blocks com stack trace no response.

```typescript
// AI GERA ISSO:
catch (error) {
  res.status(500).json({ error: error.message, stack: error.stack });
}

// DEVERIA SER ISSO:
catch (error) {
  console.error('Operation failed:', error);
  res.status(500).json({ error: 'Internal server error' });
}
```

### 6. Race conditions

AI não pensa em concorrência — inserts sem UNIQUE constraints, operações de saldo sem transaction.

### 7. Dependências fantasma

AI sugere pacotes que não existem ou que são typosquatting de libs populares. Sempre verificar se o pacote sugerido existe no npm e tem downloads significativos.

## Checklist de revisão pós-geração

- [ ] Input validation presente em todos os endpoints?
- [ ] Secrets hardcoded no código? (buscar com grep)
- [ ] SQL queries parametrizadas?
- [ ] Auth checks em todos os endpoints protegidos?
- [ ] Error handling não expõe stack traces?
- [ ] Race conditions em operações financeiras/de saldo?
- [ ] Dependências adicionadas são pacotes legítimos?
- [ ] RLS configurado em todas as tabelas públicas?
- [ ] Validação server-side duplica validação client-side?

## Impacto na auditoria

Quando o projeto é AI-generated:
1. **Aumente a desconfiança** — assuma que cada endpoint precisa de revisão de auth
2. **Verifique padrões sistêmicos** — se um endpoint não valida input, provavelmente nenhum valida
3. **Documente como padrão sistêmico** no relatório, não como achados individuais
4. **Recomende checklist de revisão** como parte do workflow de desenvolvimento

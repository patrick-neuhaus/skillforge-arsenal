# Output Template — Step 10 reference

Carrega no Step 10 do `test-lab-architect`. Template do markdown final que vai como contexto pro Lovable, Cursor ou implementação manual.

## Estrutura obrigatória do output

10 seções (uma por step). Cada seção tem decisão concreta + justificativa.

```markdown
# Lab de Testes — [Nome do App]

> Documento de arquitetura. NÃO contém código. Use como contexto pro Lovable/Cursor implementar.

## 1. Caso

**Input**: [o que entra no app]
**Processo IA**: [o que a IA faz no meio — modelo, prompt principal, critérios]
**Output**: [o que sai — formato, granularidade, exemplos]

**Operador do lab**: [perfil — gestor, dev, admin] / [frequência] / [skill técnica]

**Por que precisa do lab agora**: [problema concreto, não hipótese]

## 2. Code Audit (se retrofit)

> Skipped se app não existe ainda.

**Stack**: [framework, DB, integrações]
**Schema relevante**: [tabelas que tocam o processo IA]
**Lógica IA**: [onde tá — prompts em DB, em código, em n8n; como é editável]
**Integrações externas**: [n8n? edge functions? APIs?]

**Patterns custom vs genéricos**:
- Custom (precisa lab dedicado): [lista]
- Genérico (poderia plugar Langfuse): [lista]

## 3. Ground Truth ⛔ blocking

**Existe?**: [sim / parcial / não]
**Volume por tipo**: [N por tipo — alerta se < 30]
**Balanceamento**: [classes e %, alerta se majoritária > 70%]
**Validador**: [quem, quantos, critério escrito existe?]
**Atualização**: [como e quem atualiza quando critério muda]

**Red flags identificados**: [lista — não esconde]

**Plano de coleta** (se gap):
- Alvo: [N casos por tipo, balanceamento alvo]
- Fonte: [histórico, sintético, workshop]
- Validador: [quem, processo]
- Prazo: [data alvo pra ter mínimo viável]

## 4. Build vs Integrate

**Decisão**: [build custom / integrate Langfuse / integrate Braintrust / integrate promptfoo]

**Trade-offs apresentados**:
- Build: [vantagens contextuais — UX integrada, terminologia do domínio, etc.]
- Integrate: [vantagens — tempo, manutenção, features prontas]

**Por que [decisão]**: [justificativa específica, não genérica]

## 5. Modelo arquitetural

**Modelo**: [inline / standalone / híbrido]

**Justificativa**:
- Operador edita config? [sim/não]
- Validação é trabalho real ou parada? [...]
- Volume de teste? [...]
- Outros critérios relevantes do caso

## 6. Granularidade + comparação

**Granularidade**: [macro / micro / macro+micro]

**Por output, tipo de comparação**:
| Output | Tipo | Justificativa |
|--------|------|---------------|
| [output 1] | binária / LLM-judge / híbrida | [razão] |
| [output 2] | ... | ... |

**Custo estimado de comparação por experimento de N=100**: [$X em chamadas LLM se aplicável]

**Calibração de judge**: [feita / não feita — se não, declarar risco]

## 7. Isolamento

**Padrão**: [flag is_test / staging do orquestrador / tabelas sandbox / subdomain]

**Schema diff**:
- [Lista de tabelas + mudanças necessárias]

**Comportamento do orquestrador**:
- [n8n staging? n8n respeita is_test? edge function preview?]

**Sync lab↔prod**: [padrão de sync de config + quem controla]

## 8. Reset + promoção lab→prod

**Reseta**: [lista — config editada, experimento atual]
**NUNCA reseta**: [base de gabarito, histórico, config em prod]

**Promoção**:
- Padrão: [versionamento ativo / approval workflow / threshold / blue-green]
- Quem aprova: [pessoa, role]
- Audit trail: [campos preservados — promoted_at, promoted_by, version, ...]
- Rollback: [como — query, click, deploy reverso]

## 9. UX do operador

**Telas**:
1. **Seleção**: [escolhe tipo de teste, escopo, gabarito a usar]
2. **Edição**: [edita prompts, critérios — campos editáveis listados]
3. **Execução**: [botão de rodar, status, ETA]
4. **Resultado**: [assertividade macro+micro, divergências detalhadas, comparação com último]
5. **Histórico**: [lista de experimentos, filtros, comparação lado a lado]

**Permissões**:
- [Role] pode: [lista]
- [Role] só vê: [lista]

**Estados de tela**: [empty, loading, success, error, em-progresso] — defina por tela

## 10. Próximos passos

**Skill recomendada pra implementação**:
- [lovable-router se for Lovable]
- [supabase-db-architect se schema novo]
- [implementação manual se estrutura demanda]

**Pré-reqs antes de começar a construir**:
- [ ] Gabarito coletado e validado (ver Step 3)
- [ ] Decisão build vs integrate confirmada com cliente (ver Step 4)
- [ ] Aprovação de schema diff pela equipe técnica (ver Step 7)
- [ ] [outros pré-reqs específicos do caso]

**Wave de construção sugerida**:
1. Wave 1 (MVP do lab): [escopo mínimo testável]
2. Wave 2: [complementos]
3. Wave 3: [polish e features pós-MVP]

**Riscos abertos**:
- [Lista de riscos identificados durante o discovery — gabarito incompleto, judge não calibrado, etc.]
```

## Regras de preenchimento

1. **Nunca placeholder no output final**: se algum campo não foi resolvido com Patrick, volta pro step e pergunta. Não deixa "[a definir]" no output.
2. **Justificativas concretas**: "porque Patrick disse X" ou "porque o caso tem Y", não "porque é melhor prática".
3. **Riscos explícitos**: red flags do Step 3 e gaps em qualquer step entram em "Riscos abertos" do Step 10. Não esconde.
4. **Português**: PT-BR. Termos técnicos em inglês quando universal (LLM-as-judge, blue-green, etc.).
5. **Tamanho**: documento final tipicamente 200-400 linhas. Mais que isso, considerar quebrar em waves.

## Anti-padrões no output

- **Decisão sem justificativa**: "modelo: standalone" sem dizer por quê → Lovable não sabe se vale ajustar.
- **Recomendação genérica**: "implementar com boas práticas" → não é decisão, é wishful thinking.
- **Esconder gaps**: "gabarito ok" quando o volume é 12 e o validador é incerto → mente pro Lovable, lab nasce torto.
- **Output > 600 linhas**: lab arquitetado pra Wave 1 não precisa cobrir Wave 5. Mantém escopo do MVP.
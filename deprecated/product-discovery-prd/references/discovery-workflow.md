# Discovery Workflow — Guia Detalhado

Carregue este arquivo quando o Step 2 (Discovery) do SKILL.md for acionado.

---

## Fase 1: Entendimento Inicial

NÃO faça todas as perguntas de uma vez — agrupe em blocos de 2-3 e aprofunde conforme as respostas.

### Bloco 1 — O Problema (não a solução)

O usuário vai chegar falando da SOLUÇÃO ("quero um app que faz X"). Seu trabalho é voltar pro PROBLEMA.

- O que você quer construir? (deixe falar livremente)
- Qual o problema que isso resolve? O que acontece HOJE sem essa solução?
- Quem sofre com esse problema? Com que frequência?
- Por que agora? O que muda se não fizer?

**Mom Test (Rob Fitzpatrick) — regras pra extrair verdade:**
- NUNCA "você acha que usariam isso?" → "como vocês resolvem isso hoje?"
- NUNCA "você pagaria por isso?" → "quanto tempo/dinheiro gastam com isso hoje?"
- NUNCA sobre o futuro ("você usaria se...") → sobre o passado ("quando foi a última vez que...")

Se o usuário disser "meu cliente quer X", questione: "Ele DISSE que quer X ou ele tá SOFRENDO com um problema que você acha que X resolve?"

**Declaração do Problema:**
"Nós observamos que [estado atual] faz com que [pessoas] sofram com [problema], o que causa [consequência]."

### Bloco 2 — Contexto Técnico

- App web, automação, integração, ou mix?
- Qual a stack? (Lovable + Supabase? n8n? Outro?)
- Tem algo já construído? (banco, API, fluxo existente)
- Integrações com sistemas externos? Quais?

### Bloco 3 — Usuários e Escopo

- Quem vai usar? (perfil, quantidade esperada)
- Fluxo principal? (caminho feliz do início ao fim)
- Autenticação? Roles diferentes?
- Regras de negócio não óbvias?

Se mais de um tipo de usuário, crie **personas simplificadas** (máx 3):
- Nome + papel (ex: "Ana, gerente de operações")
- O que FAZ no sistema
- Problema principal DELA
- NÃO inclua idade, hobby, foto — lixo cosmético

### Bloco 4 — MVP e Prioridade

Use **How Might We** (HMW):
- "Como podemos [resolver problema X] para [persona Y] de forma que [resultado Z]?"
- Gere 2-3 HMWs e valide com o usuário

Depois:
- Se pudesse lançar com UMA funcionalidade, qual seria?
- O que é MVP vs "legal ter depois"?
- Tem prazo? Restrição de orçamento/tempo?

### Bloco 5 — UX e Visual (se app web)

- Referência visual? (outro app, screenshot, wireframe)
- Layout? (sidebar, tabs, dashboard, lista)
- Mobile-first ou desktop-first?
- Branding? (cores, logo, tom)

---

## Fase 2: Validação de Risco

Antes de estruturar a solução, valide os riscos com duas técnicas.

**Assumption Mapping** — Load `references/discovery-frameworks.md` para detalhes completos.

Apresente as top 3 suposições de risco pro usuário: "Essas são as apostas mais arriscadas desse projeto. Tem evidência pra alguma delas ou estamos no escuro?"

**Pre-mortem:**

"Imagina que passaram 3 meses e esse projeto fracassou completamente. Por que fracassou?"

Categorize os riscos:
- **Project killers** — bloqueios que impedem o lançamento
- **Known-but-unsaid** — coisas que a equipe suspeita mas ninguém fala
- **Execution risks** — desafios de viabilidade técnica

Se o projeto tiver riscos graves no pre-mortem, discuta mitigações ANTES de seguir.

---

## Fase 3: Oportunidades e Soluções (Opportunity Solution Tree)

Organize o que foi levantado usando a árvore de Teresa Torres:

```
Outcome desejado (resultado de negócio)
├── Oportunidade 1 (problema/necessidade)
│   ├── Solução A
│   └── Solução B
├── Oportunidade 2
│   ├── Solução C
│   └── Solução D (escolhida pro MVP)
└── Oportunidade 3 (deixar pra depois)
    └── Solução E
```

**Complemento — Impact Mapping (Gojko Adzic):**

Se o projeto envolver múltiplos stakeholders ou for estratégico, use Impact Mapping. Load `references/discovery-frameworks.md` para detalhes.

Se o projeto for simples (1 problema, 1 solução óbvia), pule e vá pra Fase 4.

---

## Fase 4: Estruturação (User Story Mapping)

Organize a implementação:

1. **Eixo horizontal (backbone):** Atividades principais em ordem cronológica
2. **Eixo vertical (profundidade):** Tarefas do mais essencial ao menos essencial
3. **Linha do MVP:** Separa o que entra do que fica pra depois
4. **Dividir em Waves** (se MVP for grande):
   - **Wave 1:** Mínimo absoluto pra validar a hipótese. 1-2 fluxos principais.
   - **Wave 2:** Complementos que tornam usável no dia a dia.
   - **Wave 3:** O que completa o MVP.

Cada wave testável sozinha. Se Wave 1 não funciona sem Wave 2, tá errado.

No PRD, marque cada fluxo/tela: `[Wave 1]`, `[Wave 2]`, `[Wave 3]`.

---

## Fase 5: Validação e Confronto

ANTES de gerar o PRD:

1. **Resuma** em 3-5 frases e peça confirmação
2. **Declare a hipótese:** "Nós acreditamos que [fazendo X] para [pessoa Y] vamos [resultado Z]. Saberemos que é verdade quando [métrica/evidência]."
3. **North Star Metric:** Qual a métrica única que define sucesso? Load `references/discovery-frameworks.md` para categorias.
4. **Appetite (Shape Up — Ryan Singer):** "Quanto tempo/esforço QUER gastar nisso?" O escopo se adapta ao appetite, não o contrário.
5. **Aponte inconsistências** — se algo contradiz, fala
6. **Questione escopo** — demais pro appetite = sugere cortes
7. **Identifique buracos** — informação crítica faltando

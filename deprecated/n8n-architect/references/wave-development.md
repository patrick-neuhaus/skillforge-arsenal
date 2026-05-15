# Wave Development — Construir em Ondas

Guia pra construir workflows em waves testáveis. Cada wave é um incremento funcional que pode ser testado isoladamente antes de avançar.

---

## Por que Waves?

- Workflow monolítico de 30 nodes é impossível de debugar
- Cada wave tem critério claro de "funciona" vs "não funciona"
- Se uma wave falha, o problema está naquela wave — não em todo o workflow
- Permite entregar valor incremental (Wave 1 já funciona, mesmo sem error handling completo)

---

## As 4 Waves

### Wave 1 — Fundação (5-10 min até primeiro run)

**O que construir:**
- Trigger (webhook, cron, manual)
- Normalização dos dados de entrada (Edit Fields: manter SÓ o necessário)
- Caminho feliz (happy path) sem branches
- Output básico (log, console, ou ação principal simplificada)

**O que NÃO fazer:**
- ❌ Error handling (ainda não)
- ❌ Branches complexos (ainda não)
- ❌ Subworkflows (ainda não)
- ❌ Nomenclatura final (foco em funcionar, não em nomear)

**Critério de teste:**
"O trigger dispara e o output chega com os dados corretos?"

**Como testar:**
1. Salvar como Draft
2. Disparar trigger manualmente (webhook test, cron manual, dados mock)
3. Verificar output: dados esperados chegaram?

⛔ **Gate:** SÓ avança pra Wave 2 se Wave 1 roda sem erro.

---

### Wave 2 — Lógica (happy path completo)

**O que construir:**
- Branches (IF/Switch) pra decisões de negócio
- Integração com todos os sistemas listados no design
- Lógica condicional completa (lead novo vs existente, pagamento aprovado vs recusado)
- Se precisa de loop: Loop Over Items + normalização

**O que NÃO fazer:**
- ❌ Error handling robusto (Wave 3)
- ❌ Sticky notes e documentação (Wave 4)
- ❌ Otimização de performance (Wave 4)

**Critério de teste:**
"O caminho feliz funciona ponta a ponta com dados reais?"

**Como testar:**
1. Usar dados reais (não mock) — se possível
2. Testar cada branch: dados que caem no IF true E no IF false
3. Verificar que todos os sistemas receberam os dados corretos

⛔ **Gate:** SÓ avança pra Wave 3 se happy path funciona 100%.

---

### Wave 3 — Resiliência

**O que construir:**
- Error handling por node HTTP Request ("On Error: Continue" + branch de tratamento)
- Error handling global (Camada 1: Error Trigger → log + notificação)
- Retry logic onde faz sentido (APIs instáveis)
- Dead-letter pra dados que falharam (salvar em tabela de erros pra reprocessar)
- Execution Data habilitado se alto volume
- Validação de input robusta (além do básico da Wave 1)

**O que NÃO fazer:**
- ❌ Otimização prematura de performance (só se já tem problema real)

**Critério de teste:**
"O que acontece quando a API X retorna 500? E quando dados inválidos chegam?"

**Como testar:**
1. Simular erro: enviar dados inválidos propositalmente
2. Simular API indisponível: URL errada ou timeout forçado
3. Verificar: erro foi logado? notificação foi enviada? dados foram salvos em dead-letter?
4. Verificar: workflow NÃO crashou (continuou processando outros items)

⛔ **Gate:** SÓ avança pra Wave 4 se erros são tratados sem crash.

---

### Wave 4 — Produção

**O que fazer:**
- Renomear TODOS os nodes: [Ação] [Alvo] (ex: "Salvar Lead Kommo", "Enviar WhatsApp Vendedor")
- Sticky notes em branches complexos explicando a lógica
- Nomear workflow: [CLIENTE] - [TIPO] - [DESCRIÇÃO]
- Verificar performance:
  - Loops otimizados? (normalização antes, Wait adequado)
  - Subworkflows necessários? (>15 nodes em um bloco → extrair)
- Configurar salvamento de execuções (erro only vs todas)
- Se webhook público: validar autenticação
- Rodar pre-delivery checklist completo

**Critério de teste:**
"Alguém da equipe (Hygor, Jonas) entende o workflow em 5 minutos?"

**Como testar:**
1. Rodar pre-delivery checklist
2. Revisão visual: nodes nomeados, sticky notes, estrutura clara
3. Testar uma última vez com dados reais ponta a ponta

⛔ **Gate:** Checklist completo → Draft → Teste final → Publish.

---

## Quando Pular Waves

| Cenário | Pular pra |
|---------|-----------|
| Workflow simples (5 nodes, sem branches) | Wave 1 → Wave 4 (direto pra produção) |
| Prototipando / proof of concept | Wave 1 só (validar que funciona) |
| Workflow crítico (dados sensíveis, produção) | Todas as 4 waves, sem exceção |
| Workflow delegado (Hygor/Jonas vai manter) | Todas as 4 waves + documentação extra |

---

## Anti-Patterns

| Anti-pattern | Por que é ruim | Correto |
|-------------|----------------|---------|
| Construir tudo de uma vez | Impossível debugar, erro pode estar em qualquer lugar | Wave por wave, testar entre cada |
| Error handling na Wave 1 | Adiciona complexidade antes de validar o básico | Happy path primeiro, erros depois |
| Pular Wave 4 (nomenclatura) | "HTTP Request 3" não diz nada, equipe não entende | Renomear SEMPRE antes de publicar |
| Nunca testar com dados reais | Mock funciona, produção quebra | Wave 2 DEVE usar dados reais |
| Otimizar antes de funcionar | Performance sem funcionalidade é inútil | Funcionar → Wave 3 → depois otimizar |

---

## Checklist Rápido por Wave

### Wave 1 ✅
- [ ] Trigger configurado e disparando
- [ ] Dados normalizados (só campos necessários)
- [ ] Output básico chegando

### Wave 2 ✅
- [ ] Todos os branches testados (true E false)
- [ ] Todos os sistemas integrados
- [ ] Happy path ponta a ponta funcional

### Wave 3 ✅
- [ ] Error handling em todo HTTP Request
- [ ] Error Trigger global configurado
- [ ] Dead-letter pra dados que falham
- [ ] Testado com dados inválidos e APIs indisponíveis

### Wave 4 ✅
- [ ] Todos nodes renomeados
- [ ] Sticky notes em branches complexos
- [ ] Pre-delivery checklist completo
- [ ] Testado com dados reais uma última vez

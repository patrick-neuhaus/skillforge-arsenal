# Teste de Skill Triggering — Sonnet Medium

> **Metodologia:** 41 inputs em linguagem natural (como Patrick falaria de verdade).
> Evita trigger words exatos das descriptions. Testa se o modelo GENERALIZA.
>
> **Como rodar:** abrir sessão Sonnet medium, colar cada input. Anotar na coluna "Resultado".
> Possíveis resultados: OK (skill certa), ERRADA (outra skill), NENHUMA (não usou skill), MAESTRO (delegou pro maestro).

## Inputs

| # | Input | Skill esperada | Resultado |
|---|-------|---------------|-----------|
| 1 | "preciso mandar uma mensagem pro cliente da Gascat explicando que o prazo vai atrasar 1 semana" | comunicacao-clientes | |
| 2 | "monta uns slides pro Willy sobre o progresso do projeto Marine" | pptx | |
| 3 | "esse código do ConfigPage.tsx tá uma zona, dá uma olhada se tem algo errado" | trident | |
| 4 | "quero fazer o site da Artemis aparecer quando alguém pergunta pro ChatGPT sobre agência de tecnologia" | ai-seo | |
| 5 | "junta esses 3 PDFs num só pra eu mandar pro cliente" | pdf | |
| 6 | "o workflow do n8n que manda email tá quebrando, não sei por quê" | n8n-architect | |
| 7 | "como eu organizo as páginas do site novo da JRG? tipo, que páginas preciso ter?" | site-architecture | |
| 8 | "faz um documento Word com a proposta comercial da Artemis pro novo cliente" | docx | |
| 9 | "to pensando em fazer um app novo pra controle de estoque, me ajuda a pensar no escopo" | product-discovery-prd | |
| 10 | "a planilha do orçamento da Gascat tá com as fórmulas erradas, conserta pra mim" | xlsx | |
| 11 | "o Hygor fez um componente gigante com 500 linhas, precisa quebrar isso" | component-architect | |
| 12 | "quero deixar o servidor mais seguro, acho que tem porta aberta que não deveria" | vps-infra-audit | |
| 13 | "escreve um texto pro Instagram da Artemis sobre o lançamento do novo serviço" | copy | |
| 14 | "como tá meu banco do Supabase? as policies tão certas?" | supabase-db-architect | |
| 15 | "quero que todo dia às 9h rode uma checagem automática das tasks atrasadas" | schedule | |
| 16 | "o Jonas tá travado faz 3 dias na mesma task, como eu lido com isso?" | tech-lead-pm | |
| 17 | "preciso melhorar o rankeamento orgânico do site da Marine no Google" | seo | |
| 18 | "faz uma página comparando a Artemis com as outras agências de tecnologia da região" | competitor-alternatives | |
| 19 | "to quase sem contexto nessa sessão né? salva o estado antes de dar /clear" | context-guardian | |
| 20 | "me ajuda a escrever as instruções pro Claude quando trabalhar no projeto do Athie" | prompt-engineer | |
| 21 | "quero construir uma calculadora grátis de ROI pra colocar no site da Artemis" | free-tool-strategy | |
| 22 | "como faço pra lançar esse produto novo? preciso de um plano de go-to-market" | launch-strategy | |
| 23 | "o app tá confuso, o usuário não sabe onde clicar pra fazer o cadastro" | ux-audit | |
| 24 | "preciso de cores, fontes e espaçamentos padronizados pro projeto novo" | ui-design-system | |
| 25 | "antes de eu sair criando componente novo, verifica se já tem algo parecido no projeto" | code-dedup-scanner | |
| 26 | "essa API do ClickUp retorna JSON gigante, quero fazer um CLI leve pra usar no Claude" | cli-skill-wrapper | |
| 27 | "como outros projetos open source implementam sistema de notificação? quero ver exemplos" | pattern-importer | |
| 28 | "monta um material de vendas pra eu levar na reunião com o prospect" | sales-enablement | |
| 29 | "o código tá com lógica de negócio no frontend, isso não deveria estar no backend?" | architecture-guard | |
| 30 | "monta um documento explicando o que é a Artemis, pra quem é, e qual o diferencial" | product-marketing-context | |
| 31 | "quero adicionar um sistema de favoritos no app, planeja antes de sair codando" | sdd | |
| 32 | "o React tá renderizando demais, acho que tem useEffect mal feito" | react-patterns | |
| 33 | "preciso de um livro ou framework sobre como dar feedback pra equipe junior" | reference-finder | |
| 34 | "quero catalogar tudo que aprendi sobre o projeto Athie num lugar organizado" | context-tree | |
| 35 | "configura o Lovable pra seguir os padrões que a gente definiu pro projeto" | lovable-knowledge | |
| 36 | "quero mudar a tabela de preços no app do Lovable, isso eu mudo direto ou mando prompt?" | lovable-router | |
| 37 | "tenho 3 coisas pra fazer, não sei por onde começar nem qual ferramenta usar" | maestro | |
| 38 | "quero melhorar a skill do copy, ela não tá acionando direito" | geo-optimizer | |
| 39 | "cria uma skill nova pra automatizar o processo de onboarding de cliente" | skill-builder | |
| 40 | "tá seguro esse código? preocupado com injection e vazamento de dados" | security-audit | |
| 41 | "peguei a transcrição da daily de hoje, extrai o que virou task e cruza com o ClickUp" | meeting-sync | |

## Critérios de avaliação

- **Taxa de acerto:** skills disparadas corretamente / 41
- **Falsos negativos:** inputs onde NENHUMA skill foi usada (pior caso)
- **Falsos positivos:** inputs onde skill ERRADA foi usada
- **Confusões comuns:** quais skills são confundidas entre si (ex: trident vs security-audit)

## Notas para o teste

1. Abrir sessão NOVA no Sonnet medium (sem contexto prévio)
2. Não dar dicas adicionais — colar o input exatamente como está
3. Se o modelo perguntar "review de código, UX ou prompt?" (por causa do skill-routing.md), anotar como POSITIVO (ele seguiu a regra de desambiguação)
4. Se o modelo usar a skill certa MAS também fizer outra coisa desnecessária, anotar como OK com nota
5. Anotar o tempo médio de resposta (Sonnet medium vs Opus pode variar)

# Playwright browser matrix (proposed reference)

> Carregado por `react-patterns` na **Phase 5.6**. Define matriz mínima de teste multi-engine. Fonte: DR-04. Boundary: não substitui `ux-audit` em a11y manual nem `ui-design-system` em visual regression — aqui é teste funcional cross-engine.

---

## 1. Princípio

Teste cross-browser tem 4 camadas:

1. **Automatizado multi-engine** (Playwright em chromium + firefox + webkit).
2. **Cloud de browsers/dispositivos reais** (BrowserStack / Sauce Labs) para Safari/iOS real.
3. **Evidência de compatibilidade** (MDN BCD, Can I Use, wpt.fyi) antes de concluir bug.
4. **Auditoria não-funcional** (Lighthouse, axe-core) como complemento — não como prova.

`react-patterns` define a camada 1 e a 3 como obrigatórias na Phase 5; cita 2 e 4 como complemento.

## 2. Playwright projects (mínimo)

```ts
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox',  use: { ...devices['Desktop Firefox'] } },
    { name: 'webkit',   use: { ...devices['Desktop Safari'] } },

    // Branded browsers em ambiente enterprise:
    { name: 'edge',     use: { ...devices['Desktop Edge'], channel: 'msedge' } },
    { name: 'chrome',   use: { ...devices['Desktop Chrome'], channel: 'chrome' } },

    // Mobile emulado (não substitui device real):
    { name: 'mobile-chrome', use: { ...devices['Pixel 7'] } },
    { name: 'mobile-safari', use: { ...devices['iPhone 14'] } },
  ],
});
```

**Mínimo absoluto:** `chromium`, `firefox`, `webkit` para fluxos críticos.

**Branded** (`chrome`, `msedge`) **se** ambiente enterprise os exige (autoplay/tracking prevention/policies divergentes).

**Mobile emulado** ajuda em viewport, mas **não substitui** device real para inputs nativos, mídia, gestos.

## 3. O que cobrir em multi-engine

### 3.1 Smoke obrigatório (todos os fluxos)

- App monta sem erro de console.
- Rota principal carrega.
- Navegação entre rotas principais.
- Login/logout (se houver).
- Refresh preserva estado esperado.

### 3.2 Fluxos sensíveis a engine (cobertura forte)

| Fluxo | Por quê |
|---|---|
| Login com SSO / IdP externo | Storage Access, third-party cookies, partitioned cookies |
| Embed em iframe | Mesmo |
| Form com input nativo (date/time/color/file) | UI nativa varia |
| Modal / dialog / popover / tooltip | Stacking context, popover API, anchor positioning |
| Sticky header / sidebar | Overflow ancestor |
| Scroll containers internos | Scroll snap, behavior |
| Clipboard / copy-paste | Permission/gesture |
| Autoplay / playback de mídia | Heurística por browser |
| Drag & drop | Pointer events vs touch |

### 3.3 Cobertura visual / layout

- Breakpoints principais (320, 768, 1024, 1440 — coordenar com `ui-design-system`).
- Zoom 200% e 400%.
- Reduced motion ON e OFF.
- Dark mode ON e OFF.

**Boundary:** visual regression detalhada (pixel-diff) é responsabilidade de tooling adicional (Percy, Chromatic, Playwright snapshots), não desta skill.

## 4. Cloud testing — quando obrigatório

- **Sempre que** matriz inclui Safari iOS — webkit do Playwright **não é Safari real**.
- **Sempre que** matriz inclui versões específicas de SO ou Safari (>1 versão).
- **Sempre que** bug é reportado em device específico que não reproduz local.

**Provedores:** BrowserStack, Sauce Labs, LambdaTest. Selecionar pelo time.

## 5. Manual obrigatório (não automatizável)

- Pelo menos 1 passe em **Safari iOS real** para fluxos com input nativo, mídia, SSO embed.
- Pelo menos 1 passe em **Firefox desktop** para fluxos com sessão, overlay, mídia.
- Janela privada / tracking protection alta para fluxos com embed/SSO/analytics crítico.

## 6. Boundary com axe e Lighthouse

- **axe-core / axe DevTools** — a11y técnica. **Canônico em `ux-audit`** (limiares WCAG, status messages, ARIA). Aqui usamos apenas como gate técnico em CI.
- **Lighthouse** — performance, SEO, best practices, a11y subset. Complemento. Score de a11y não substitui teste manual de fluxo (canônico em `ux-audit`).
- **Nem axe nem Lighthouse** provam paridade entre Blink/Gecko/WebKit. Eles ajudam; não substituem multi-engine.

## 7. Anti-patterns

- **Testar só em Chromium** — não prova interoperabilidade.
- **"Webkit no Playwright = Safari"** — não. Cobrir Safari real em cloud/device.
- **Snapshot visual como prova de compatibilidade** — diferenças de antialiasing são esperadas.
- **CI multi-engine sem manual em device real** — perde inputs nativos, mídia, gestos.
- **Bloquear PR por flake de webkit** — sem investigar; gera "always green" defensivo.

## 8. Como registrar bug encontrado em CI

Formato canônico (mesmo da Phase 5.7 do SKILL):

```
Bug: [nome curto]
Severidade: Crítica | Alta | Média | Baixa
Browser/Versão/SO: [específico — não "Safari", e sim "Safari 17.4 / iOS 17.4"]
Evidência: [trace/video/screenshot do Playwright; console; network]
Componente/Rota: [caminho]
Hipótese técnica: [feature suspeita / pipeline / política]
Teste de confirmação: [mínimo isolado + outro engine + cloud se aplicável]
Fix proposto: [progressive enhancement / @supports / fallback / config]
Risco de regressão no Chrome: [explícito]
Critério de aceite: [como validar — Playwright passa nos 3 engines + manual em device real se aplicável]
```

## 9. Checklist de Phase 5.6

- [ ] `playwright.config.*` declara projects para chromium + firefox + webkit?
- [ ] Smoke roda nos 3 engines no CI?
- [ ] Fluxos sensíveis (SSO, modal, sticky, clipboard, autoplay, input nativo) cobertos em multi-engine?
- [ ] Cloud provider configurado se matriz inclui Safari iOS?
- [ ] Manual em Safari iOS real agendado em cadência regular?
- [ ] Bugs registrados no formato canônico com risco de regressão no Chrome?
- [ ] axe-core / Lighthouse rodando como gate técnico em CI (sem substituir `ux-audit`)?

## 10. Boundary final

- **Define:** matriz Playwright + camadas de teste.
- **Não define:** WCAG limiares (importa de `ux-audit`); regras visuais (importa de `ui-design-system`); anatomia de componente (importa de `component-architect`).

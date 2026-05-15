# Remotion React Patterns — Patterns Especificos

Consulte este arquivo quando trabalhando com React + Remotion.

---

## Conceitos-Chave

### Frame-Based Rendering
Em Remotion, NAO existe estado reativo (useState pra animacao). Tudo e funcao do frame:

```typescript
const frame = useCurrentFrame();
const opacity = interpolate(frame, [0, 30], [0, 1], {
  extrapolateRight: 'clamp',
});
```

### Timeline via Sequences
```typescript
<Composition>
  <Sequence from={0} durationInFrames={90}>
    {/* Cena 1: frames 0-89 */}
    <IntroScene />
  </Sequence>
  <Sequence from={90} durationInFrames={120}>
    {/* Cena 2: frames 90-209 */}
    <ContentScene data={chartData} />
  </Sequence>
</Composition>
```

### Spring Animations
```typescript
const scale = spring({
  frame,
  fps: 30,
  config: { damping: 200, mass: 0.5, stiffness: 200 },
});
```

## Padroes de Composicao

### Props Down (dados → componentes visuais)
```typescript
// Video recebe dados via inputProps
export const DataVideo: React.FC<{
  title: string;
  data: DataPoint[];
  branding: BrandConfig;
}> = ({ title, data, branding }) => {
  return (
    <AbsoluteFill style={{ backgroundColor: branding.bg }}>
      <AnimatedTitle text={title} font={branding.headingFont} />
      <AnimatedChart data={data} colors={branding.colors} />
    </AbsoluteFill>
  );
};
```

### Componentes Reutilizaveis de Animacao
```typescript
// Atom: FadeIn wrapper reutilizavel
export const FadeIn: React.FC<{
  children: React.ReactNode;
  delay?: number;
  duration?: number;
}> = ({ children, delay = 0, duration = 30 }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(
    frame - delay,
    [0, duration],
    [0, 1],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );
  return <div style={{ opacity }}>{children}</div>;
};
```

## Diferencas de React Web

| React Web | Remotion |
|-----------|---------|
| useState + useEffect | useCurrentFrame() + interpolate() |
| CSS transitions | spring() configs |
| Responsive (vw, rem) | Fixo (px, resolucao definida) |
| Event handlers (onClick) | Nao existe — video nao e interativo |
| Lazy loading | Nao aplicavel — tudo renderiza offline |
| Server Components | Nao aplicavel — tudo e client |
| Hydration | Nao aplicavel — renderiza frame a frame |

## Anti-Patterns Remotion

- **useState pra animacao** — use useCurrentFrame(). State causa re-renders desnecessarios
- **CSS animations** — use interpolate/spring. CSS nao sincroniza com frames
- **Imagens externas sem prefetch** — use staticFile() ou delayRender/continueRender
- **Componentes pesados sem memoizacao** — cada frame re-renderiza tudo. Memoize calculos caros
- **Hardcoded dimensions** — use tokens. Videos podem ter resolucoes diferentes (16:9, 9:16, 1:1)

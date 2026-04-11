---
name: ai-seo
description: "When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. Also use when the user mentions 'AI SEO,' 'AEO,' 'GEO,' 'LLMO,' 'answer engine optimization,' 'generative engine optimization,' 'LLM optimization,' 'AI Overviews,' 'optimize for ChatGPT,' 'optimize for Perplexity,' 'AI citations,' 'AI visibility,' 'zero-click search,' 'how do I show up in AI answers,' 'LLM mentions,' or 'optimize for Claude/Gemini.' Use this whenever someone wants their content to be cited or surfaced by AI assistants and AI search engines. For traditional technical and on-page SEO audits, see seo-audit. For structured data implementation, see schema-markup."
metadata:
  version: 1.2.0
---

# AI SEO

**Role:** expert in AI search optimization — making content discoverable, extractable, and citable by AI systems including Google AI Overviews, ChatGPT, Perplexity, Claude, Gemini, and Copilot.

**Context:** traditional SEO gets you ranked; AI SEO gets you **cited**. In AI search, a well-structured page can get cited even if it ranks on page 2 or 3 — AI systems select sources based on content quality, structure, and relevance, not just rank position.

**Iron Law:** never optimize for AI without first auditing current AI visibility. You can't improve citations you haven't measured. Check ChatGPT, Perplexity, and Google AI Overviews for your key queries before touching content.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Current AI Visibility
- Do you know if your brand appears in AI-generated answers today?
- Have you checked ChatGPT, Perplexity, or Google AI Overviews for your key queries?
- What queries matter most to your business?

### 2. Content & Domain
- What type of content do you produce? (Blog, docs, comparisons, product pages)
- What's your domain authority / traditional SEO strength?
- Do you have existing structured data (schema markup)?

### 3. Goals
- Get cited as a source in AI answers?
- Appear in Google AI Overviews for specific queries?
- Compete with specific brands already getting cited?
- Optimize existing content or create new AI-optimized content?

### 4. Competitive Landscape
- Who are your top competitors in AI search results?
- Are they being cited where you're not?

## How AI Search Works

| Platform | How It Works | Source Selection |
|----------|-------------|----------------|
| **Google AI Overviews** | Summarizes top-ranking pages | Strong correlation with traditional rankings |
| **ChatGPT (with search)** | Searches web, cites sources | Draws from wider range, not just top-ranked |
| **Perplexity** | Always cites sources with links | Favors authoritative, recent, well-structured content |
| **Gemini** | Google's AI assistant | Pulls from Google index + Knowledge Graph |
| **Copilot** | Bing-powered AI search | Bing index + authoritative sources |
| **Claude** | Brave Search (when enabled) | Training data + Brave search results |

For deep dive on platform-specific ranking factors, load [references/platform-ranking-factors.md](references/platform-ranking-factors.md).

**Critical stats:**
- AI Overviews appear in ~45% of Google searches
- AI Overviews reduce clicks to websites by up to 58%
- Brands are 6.5x more likely to be cited via third-party sources than their own domains
- Optimized content gets cited 3x more often than non-optimized
- Statistics and citations boost visibility by 40%+ across queries

## Workflow

```
AI SEO Progress:

- [ ] Step 1: Visibility Audit ⚠️ REQUIRED
  - [ ] Load references/visibility-audit.md
  - [ ] Run 4-step audit (queries, citations, extractability, bot access)
  - [ ] ⛔ GATE: Present findings before optimizing
- [ ] Step 2: Optimize (Three Pillars) ⚠️ REQUIRED
  - [ ] Load references/optimization-pillars.md
  - [ ] Apply Pillar 1 (Structure) — load references/content-patterns.md for block templates
  - [ ] Apply Pillar 2 (Authority) — cite sources, add statistics, expert quotes
  - [ ] Apply Pillar 3 (Presence) — Wikipedia, Reddit, review sites, third-party
- [ ] Step 3: Content Type Guide
  - [ ] Load references/content-types-guide.md
  - [ ] Apply content-type-specific optimization (SaaS, blog, comparison, docs)
- [ ] Step 4: Monitor
  - [ ] Set up tracking (tools from visibility-audit.md)
  - [ ] Monthly manual check of top 20 queries
  - [ ] ⛔ GATE: Present monitoring plan to user
```

## Content Block Patterns (quick reference)

For detailed templates, load [references/content-patterns.md](references/content-patterns.md).

- **Definition blocks** for "What is X?" queries
- **Step-by-step blocks** for "How to X" queries
- **Comparison tables** for "X vs Y" queries
- **Pros/cons blocks** for evaluation queries
- **FAQ blocks** for common questions
- **Statistic blocks** with cited sources

**Structural rules:**
- Lead every section with a direct answer (don't bury it)
- Key answer passages: 40-60 words (optimal for snippet extraction)
- H2/H3 headings that match how people phrase queries
- Tables beat prose for comparison content
- One clear idea per paragraph

## Anti-Patterns

- **Keyword stuffing** — actively reduces AI visibility by 10% (Princeton GEO study). Not just ineffective; harmful.
- **Blocking AI bots** — if GPTBot, PerplexityBot, ClaudeBot blocked in robots.txt, those platforms can't cite you
- **Undated content** — AI weights freshness heavily. No date = loses to dated competitor
- **Gated content** — AI can't access it. Keep most authoritative content open
- **Generic claims** — "We're the best" won't get cited. "3x improvement in [metric]" will
- **No schema markup** — content with proper schema shows 30-40% higher AI visibility
- **Writing for AI, not humans** — if content reads like SEO game, it won't convert even if it gets cited
- **Ignoring third-party presence** — Wikipedia citation often beats your own blog citation

For the full Common Mistakes list, load [references/content-types-guide.md](references/content-types-guide.md).

## Task-Specific Questions

1. What are your top 10-20 most important queries?
2. Have you checked if AI answers exist for those queries today?
3. Do you have structured data (schema markup) on your site?
4. What content types do you publish? (Blog, docs, comparisons, etc.)
5. Are competitors being cited by AI where you're not?
6. Do you have a Wikipedia page or presence on review sites?

## Related Skills

- **seo**: for traditional technical and on-page SEO audits
- **schema-markup**: for implementing structured data that helps AI understand your content
- **content-strategy**: for planning what content to create
- **competitor-alternatives**: for building comparison pages that get cited
- **site-architecture**: for URL/hierarchy decisions that affect crawlability
- **copy**: for writing content that's both human-readable and AI-extractable

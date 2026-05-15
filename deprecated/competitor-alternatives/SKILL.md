---
name: competitor-alternatives
description: "When the user wants to create competitor comparison or alternative pages for SEO and sales enablement. Also use when the user mentions 'alternative page,' 'vs page,' 'competitor comparison,' 'comparison page,' '[Product] vs [Product],' '[Product] alternative,' 'competitive landing pages,' 'how do we compare to X,' 'battle card,' or 'competitor teardown.' Use this for any content that positions your product against competitors. Covers four formats: singular alternative, plural alternatives, you vs competitor, and competitor vs competitor. For sales-specific competitor docs, see sales-enablement."
metadata:
  version: 1.2.0
---

# Competitor & Alternative Pages

**Role:** expert in creating competitor comparison and alternative pages. Build pages that rank for competitive search terms, provide genuine value to evaluators, and position your product effectively.

**Iron Law:** honesty builds trust. Acknowledge competitor strengths, be accurate about your limitations, don't misrepresent competitor features. Readers are comparing — they'll verify claims. A biased comparison hurts credibility more than a fair one helps positioning.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before creating competitor pages, understand:

1. **Your Product** — core value prop, differentiators, ICP, pricing, honest strengths and weaknesses
2. **Competitive Landscape** — direct competitors, indirect/adjacent, market positioning, search volume for competitor terms
3. **Goals** — SEO traffic capture, sales enablement, conversion from competitor users, brand positioning

## Core Principles

- **Honesty builds trust.** Acknowledge competitor strengths. Readers verify claims.
- **Depth over surface.** Go beyond feature checklists. Explain *why* differences matter.
- **Help them decide.** Different tools fit different needs. Be clear about who each is best for.
- **Modular content architecture.** Competitor data centralized. Updates propagate. Single source of truth per competitor.

## Page Formats

### Format 1: [Competitor] Alternative (Singular)

**Search intent:** user is actively looking to switch from a specific competitor

**URL pattern:** `/alternatives/[competitor]` or `/[competitor]-alternative`

**Target keywords:** "[Competitor] alternative", "alternative to [Competitor]", "switch from [Competitor]"

**Page structure:**
1. Why people look for alternatives (validate their pain)
2. Summary: you as the alternative (quick positioning)
3. Detailed comparison (features, service, pricing)
4. Who should switch (and who shouldn't)
5. Migration path
6. Social proof from switchers
7. CTA

### Format 2: [Competitor] Alternatives (Plural)

**Search intent:** user is researching options, earlier in journey

**URL pattern:** `/alternatives/[competitor]-alternatives`

**Target keywords:** "[Competitor] alternatives", "best [Competitor] alternatives", "tools like [Competitor]"

**Page structure:**
1. Why people look for alternatives (common pain points)
2. What to look for in an alternative (criteria framework)
3. List of alternatives (you first, but include real options)
4. Comparison table (summary)
5. Detailed breakdown of each alternative
6. Recommendation by use case
7. CTA

**Important:** include 4-7 real alternatives. Being genuinely helpful builds trust and ranks better.

### Format 3: You vs [Competitor]

**Search intent:** user is directly comparing you to a specific competitor

**URL pattern:** `/vs/[competitor]` or `/compare/[you]-vs-[competitor]`

**Target keywords:** "[You] vs [Competitor]", "[Competitor] vs [You]"

**Page structure:**
1. TL;DR summary (key differences in 2-3 sentences)
2. At-a-glance comparison table
3. Detailed comparison by category (Features, Pricing, Support, Ease of use, Integrations)
4. Who [You] is best for
5. Who [Competitor] is best for (be honest)
6. What customers say (testimonials from switchers)
7. Migration support
8. CTA

### Format 4: [Competitor A] vs [Competitor B]

**Search intent:** user comparing two competitors (not you directly)

**URL pattern:** `/compare/[competitor-a]-vs-[competitor-b]`

**Page structure:**
1. Overview of both products
2. Comparison by category
3. Who each is best for
4. The third option (introduce yourself)
5. Comparison table (all three)
6. CTA

**Why this works:** captures search traffic for competitor terms, positions you as knowledgeable.

## Essential Sections (all formats)

- **TL;DR Summary** — start every page with a quick summary for scanners
- **Paragraph Comparisons** — go beyond tables; explain when each matters
- **Feature Comparison** — describe how each handles it, strengths + limitations, bottom line
- **Pricing Comparison** — tier-by-tier, what's included, hidden costs, total cost for sample team
- **Who It's For** — explicit ideal customer for each option (honest recommendations build trust)
- **Migration Section** — what transfers, what needs reconfiguration, support offered, switcher quotes

For detailed templates, load [references/templates.md](references/templates.md).

## Content Architecture

Create a single source of truth for each competitor. For data structure and examples, load [references/content-architecture.md](references/content-architecture.md).

## Research & SEO

For deep competitor research methodology + ongoing update cadence + SEO considerations (keyword targeting, internal linking, schema markup) + output format, load [references/research-process.md](references/research-process.md).

## Anti-Patterns

- **Biased comparisons** — readers verify. Bias hurts credibility more than positioning helps.
- **Misrepresenting competitor features** — they'll call you out publicly. Accuracy is table stakes.
- **Feature-checklist-only** — depth over surface. Explain *why* differences matter.
- **"You should switch" without honesty** — be clear about who each tool is actually best for
- **Stale competitor data** — pricing changes, features ship. Quarterly review minimum.
- **Scattered competitor data** — duplicated across pages that drift. Centralize.
- **Skipping migration section** — switchers need to know what transfers and what doesn't
- **No TL;DR summary** — comparison page scanners bounce without scannable summary

## Task-Specific Questions

1. What are common reasons people switch to you?
2. Do you have customer quotes about switching?
3. What's your pricing vs. competitors?
4. Do you offer migration support?

## Related Skills

- **copy**: for writing compelling comparison copy
- **seo**: for optimizing competitor pages
- **site-architecture**: for URL patterns and hub pages linking comparisons
- **sales-enablement**: for internal sales collateral, decks, and objection docs
- **ai-seo**: comparison pages are top-cited format in AI search

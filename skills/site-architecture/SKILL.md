---
name: site-architecture
description: When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal linking. Also use when the user mentions "sitemap," "site map," "visual sitemap," "site structure," "page hierarchy," "information architecture," "IA," "navigation design," "URL structure," "breadcrumbs," "internal linking strategy," "website planning," "what pages do I need," "how should I organize my site," or "site navigation." Use this whenever someone is planning what pages a website should have and how they connect. NOT for XML sitemaps (that's technical SEO — see seo-audit). For SEO audits, see seo-audit. For structured data, see schema-markup.
metadata:
  version: 1.2.0
---

# Site Architecture

**Role:** information architecture expert. Plan website structure — page hierarchy, navigation, URL patterns, and internal linking — so the site is intuitive for users and optimized for search engines.

**Iron Law:** users should reach any important page within 3 clicks from the homepage. This isn't absolute, but if critical pages are buried 4+ levels deep, something is wrong.

## Before Planning

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Business Context
- What does the company do?
- Who are the primary audiences?
- What are the top 3 goals for the site? (conversions, SEO traffic, education, support)

### 2. Current State
- New site or restructuring an existing one?
- If restructuring: what's broken? (high bounce, poor SEO, users can't find things)
- Existing URLs that must be preserved (for redirects)?

### 3. Site Type
- SaaS marketing site, content/blog, e-commerce, documentation, hybrid, small business

### 4. Content Inventory
- How many pages exist or are planned?
- What are the most important pages? (by traffic, conversions, or business value)
- Any planned sections or expansions?

## Workflow

```
Site Architecture Progress:

- [ ] Step 1: Classify site type ⚠️ REQUIRED
  - [ ] Match to site type table below
  - [ ] Load references/site-type-templates.md for full template
- [ ] Step 2: Design Page Hierarchy
  - [ ] Pick depth (flat vs moderate vs deep)
  - [ ] Apply 3-click rule
  - [ ] Draft ASCII tree
- [ ] Step 3: Design Navigation
  - [ ] Load references/navigation-patterns.md
  - [ ] Define header (4-7 items max + CTA)
  - [ ] Define footer sections
  - [ ] Breadcrumb plan
- [ ] Step 4: URL Structure
  - [ ] Load references/url-patterns.md
  - [ ] Apply pattern by page type
  - [ ] Audit for common mistakes
- [ ] Step 5: Internal Linking
  - [ ] Load references/internal-linking.md
  - [ ] Hub-and-spoke for content clusters
  - [ ] Orphan audit if restructuring
- [ ] Step 6: Visual Sitemap (optional)
  - [ ] Load references/mermaid-templates.md
  - [ ] Generate Mermaid diagram
- [ ] Step 7: Deliver ⛔ BLOCKING
  - [ ] ASCII tree + URL map + Navigation spec + Linking plan
  - [ ] ⛔ GATE: Present to user before implementation
```

## Site Types and Starting Points

| Site Type | Typical Depth | Key Sections | URL Pattern |
|-----------|--------------|--------------|-------------|
| SaaS marketing | 2-3 levels | Home, Features, Pricing, Blog, Docs | `/features/name`, `/blog/slug` |
| Content/blog | 2-3 levels | Home, Blog, Categories, About | `/blog/slug`, `/category/slug` |
| E-commerce | 3-4 levels | Home, Categories, Products, Cart | `/category/subcategory/product` |
| Documentation | 3-4 levels | Home, Guides, API Reference | `/docs/section/page` |
| Hybrid SaaS+content | 3-4 levels | Home, Product, Blog, Resources, Docs | `/product/feature`, `/blog/slug` |
| Small business | 1-2 levels | Home, Services, About, Contact | `/services/name` |

For full page hierarchy templates, load [references/site-type-templates.md](references/site-type-templates.md).

## Page Hierarchy

### The 3-Click Rule

Users should reach any important page within 3 clicks from the homepage. If critical pages are buried 4+ levels deep, something is wrong.

### Flat vs Deep

| Approach | Best For | Tradeoff |
|----------|----------|----------|
| Flat (2 levels) | Small sites, portfolios | Simple but doesn't scale |
| Moderate (3 levels) | Most SaaS, content sites | Good balance of depth and findability |
| Deep (4+ levels) | E-commerce, large docs | Scales but risks burying content |

**Rule of thumb:** go as flat as possible while keeping navigation clean. If a nav dropdown has 20+ items, add a level of hierarchy.

### ASCII Tree Format

```
Homepage (/)
├── Features (/features)
│   ├── Analytics (/features/analytics)
│   ├── Automation (/features/automation)
│   └── Integrations (/features/integrations)
├── Pricing (/pricing)
├── Blog (/blog)
│   └── [Category: SEO] (/blog/category/seo)
└── About (/about)
```

**When to use ASCII vs Mermaid:**
- ASCII: quick hierarchy drafts, text-only contexts, simple structures
- Mermaid: visual presentations, complex relationships, showing nav zones — load [references/mermaid-templates.md](references/mermaid-templates.md)

## Navigation (quick reference)

- **Header nav:** 4-7 items max, logo left, CTA button rightmost, order by priority
- **Footer:** group into columns (Product, Resources, Company, Legal)
- **Breadcrumbs:** mirror URL hierarchy, clickable except current page
- **Sidebar:** use for docs/blog section navigation

For detailed navigation patterns, load [references/navigation-patterns.md](references/navigation-patterns.md).

## URL Structure (quick reference)

Design principles: human-readable, hyphens not underscores, reflect hierarchy, consistent trailing slash, lowercase, short but descriptive.

For URL patterns by page type + common mistakes + breadcrumb alignment, load [references/url-patterns.md](references/url-patterns.md).

## Internal Linking (quick reference)

- **No orphan pages** — every page has at least one internal link pointing to it
- **Descriptive anchor text** — "our analytics features" not "click here"
- **Hub-and-spoke** for content clusters

For full hub-and-spoke model + link audit checklist, load [references/internal-linking.md](references/internal-linking.md).

## Output Format

When creating a site architecture plan, provide:

1. **Page Hierarchy** — ASCII tree with URLs at each node
2. **Visual Sitemap** — Mermaid diagram (if applicable)
3. **URL Map Table** — columns: Page, URL, Parent, Nav Location, Priority
4. **Navigation Spec** — header items (ordered with CTA), footer sections, sidebar (if applicable), breadcrumb notes
5. **Internal Linking Plan** — hub pages + spokes, cross-section opportunities, orphan audit

## Anti-Patterns

- **Burying critical pages 4+ levels deep** — violates 3-click rule
- **Nav dropdowns with 20+ items** — decision paralysis; add hierarchy
- **Dates in blog URLs** — `/blog/2024/01/15/post-title` adds zero value
- **Changing URLs without 301 redirects** — kills backlink equity
- **IDs in URLs** — not human-readable (`/product/12345`)
- **Inconsistent URL patterns** — mixing `/features/X` and `/product/Y`
- **Orphan pages** — pages with zero inbound internal links
- **Generic anchor text** — "click here", "read more" (no SEO value, no context)
- **Inconsistent trailing slash policy** — pick one and enforce

## Task-Specific Questions

1. Is this a new site or are you restructuring an existing one?
2. What type of site is it? (SaaS, content, e-commerce, docs, hybrid, small business)
3. How many pages exist or are planned?
4. What are the 5 most important pages on the site?
5. Are there existing URLs that need to be preserved or redirected?
6. Who are the primary audiences, and what are they trying to accomplish on the site?

## Related Skills

- **seo**: for technical SEO, on-page optimization, and indexation issues
- **content-strategy**: for planning what content to create and topic clusters
- **competitor-alternatives**: for comparison page frameworks and URL patterns
- **ai-seo**: for optimizing structure for AI citation extractability
- **copy**: for writing the actual page content

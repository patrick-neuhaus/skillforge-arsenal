---
name: sales-enablement
description: "When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts. Also use when the user mentions 'sales deck,' 'pitch deck,' 'one-pager,' 'leave-behind,' 'objection handling,' 'deal-specific ROI analysis,' 'demo script,' 'talk track,' 'sales playbook,' 'proposal template,' 'buyer persona card,' 'help my sales team,' 'sales materials,' or 'what should I give my sales reps', 'material de vendas', 'reunião com prospect', 'preparar reunião comercial', 'levar pra reunião'. Use this for any document or asset that helps a sales team close deals. For competitor comparison pages and battle cards, see competitor-alternatives. For marketing website copy, see copywriting. For cold outreach emails, see cold-email."
metadata:
  version: 1.2.0
---

# Sales Enablement

**Role:** expert in B2B sales enablement. Create sales collateral that reps actually use — decks, one-pagers, objection docs, demo scripts, and playbooks that help close deals.

**Iron Law:** if reps rewrite your deck before sending it, you wrote the wrong deck. Test drafts with top performers before shipping. Sales uses what sales trusts.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

1. **Value Proposition & Differentiators**
   - What do you sell and who is it for?
   - What makes you different from the next best alternative?
   - What outcomes can you prove?

2. **Sales Motion**
   - How do you sell? (self-serve, inside sales, field sales, hybrid)
   - Average deal size and sales cycle length
   - Key personas involved in the buying decision

3. **Collateral Needs**
   - What specific assets do you need?
   - What stage of the funnel are they for?
   - Who will use them? (AE, SDR, champion, prospect)

4. **Current State**
   - What materials exist today?
   - What's working and what's not?
   - What do reps ask for most?

## Core Principles

- **Sales uses what sales trusts.** Involve reps in creation. Use their language, not marketing's.
- **Situation-specific, not generic.** Tailor to persona, deal stage, and use case.
- **Scannable over comprehensive.** Reps need information in 3 seconds, not 30.
- **Tie back to business outcomes.** Every claim connects to revenue, efficiency, or risk reduction.

## Sales Deck / Pitch Deck

### 10-12 Slide Framework

1. **Current World Problem** — the pain your buyer lives with today
2. **Cost of the Problem** — what inaction costs (time, money, risk)
3. **The Shift Happening** — market or technology change creating urgency
4. **Your Approach** — how you solve it differently
5. **Product Walkthrough** — 3-4 key workflows, not a feature tour
6. **Proof Points** — metrics, logos, analyst recognition
7. **Case Study** — one customer story told well
8. **Implementation / Timeline** — how they get from here to live
9. **ROI / Value** — expected return and payback period
10. **Pricing Overview** — transparent, tiered if applicable
11. **Next Steps / CTA** — clear action with timeline

### Customization by Buyer Type

| Buyer | Emphasize | De-emphasize |
|-------|-----------|--------------|
| Technical buyer | Architecture, security, integrations, API | ROI calculations, business metrics |
| Economic buyer | ROI, payback period, total cost, risk | Technical details, implementation specifics |
| Champion | Internal selling points, quick wins, peer proof | Deep technical or financial detail |

For slide-by-slide guidance, load [references/deck-frameworks.md](references/deck-frameworks.md).

## One-Pagers / Leave-Behinds

**Use cases:** post-meeting recap, champion internal selling, trade show handout.

**Structure:**
1. Problem statement — the pain in one sentence
2. Your solution — what you do and how
3. 3 differentiators — why you vs. alternatives
4. Proof point — one strong metric or customer quote
5. CTA — clear next step with contact info

**Design:** one page literally, scannable in 30 seconds, include logo + website + specific contact (not info@).

For templates by use case, load [references/one-pager-templates.md](references/one-pager-templates.md).

## Objection Handling Docs

### Objection Categories

| Category | Examples |
|----------|----------|
| Price | "Too expensive," "No budget this quarter," "Competitor is cheaper" |
| Timing | "Not the right time," "Maybe next quarter," "Too busy to implement" |
| Competition | "We already use X," "What makes you different?" |
| Authority | "I need to check with my boss," "The committee decides" |
| Status quo | "What we have works fine," "Not broken, don't fix it" |
| Technical | "Does it integrate with X?," "Security concerns," "Can it scale?" |

### Response Framework

For each objection, document:
1. Objection statement (exactly how reps hear it)
2. Why they say it (the real concern behind the words)
3. Response approach (how to acknowledge and redirect)
4. Proof point (specific evidence that addresses the concern)
5. Follow-up question (keep the conversation moving forward)

**Two formats:** quick-reference table for live calls + detailed doc for prep and training.

For the full objection library, load [references/objection-library.md](references/objection-library.md).

## Demo Scripts & Talk Tracks

### Script Structure

1. **Opening** (2 min) — context setting, agenda, confirm goals for the call
2. **Discovery recap** (3 min) — summarize what you learned, confirm priorities
3. **Solution walkthrough** (15-20 min) — 3-4 key workflows mapped to their pain
4. **Interaction points** — questions to ask during the demo, not just at the end
5. **Close** (5 min) — summarize value, propose next steps with timeline

### Talk Track Types

| Type | Duration | Focus |
|------|----------|-------|
| Discovery call | 30 min | Qualify, understand pain, map buying process |
| First demo | 30-45 min | Show 3-4 workflows tied to their pain |
| Technical deep-dive | 45-60 min | Architecture, security, integrations, API |
| Executive overview | 20-30 min | Business outcomes, ROI, strategic alignment |

**Key principle:** demo after discovery, not before. If you don't know their pain, you're guessing which features matter.

For full script templates, load [references/demo-scripts.md](references/demo-scripts.md).

## Other Collateral

- **ROI calculators, value props, persona cards** → load [references/roi-calculators.md](references/roi-calculators.md)
- **Case study briefs, proposal templates, sales playbooks** → load [references/proposals-playbooks.md](references/proposals-playbooks.md)

## Anti-Patterns

- **Generic decks** — not tailored to persona/stage/use case. Reps rewrite them.
- **Feature tours** — a deck that lists features instead of telling a story. Story arc > feature tour.
- **Too many slides per idea** — one idea per slide. If you need two points, use two slides.
- **Burying the price in proposals** — transparent + confident. Don't make them hunt.
- **Generic proposals** — templated proposals signal low effort. Customize exec summary minimum.
- **Playbooks without owners** — if nobody owns it, it rots. Review quarterly.
- **Demo before discovery** — guessing which features matter. Ask first, show second.
- **Decks designed for reading, not presenting** — slides support the conversation; they don't replace it.

## Output Format

| Asset | Deliverable |
|-------|-------------|
| Sales deck | Slide-by-slide outline with headline, body copy, and speaker notes |
| One-pager | Full copy with layout guidance (visual hierarchy, sections) |
| Objection doc | Table format: objection, response, proof point, follow-up |
| Demo script | Scene-by-scene with timing, talk track, and interaction points |
| ROI calculator | Input fields, formulas, output display with sample data |
| Playbook | Structured document with table of contents and sections |
| Persona card | One-page card format per persona |
| Proposal | Section-by-section copy with customization notes |

## Task-Specific Questions

1. What collateral do you need? (deck, one-pager, objection doc, etc.)
2. Who will use it? (AE, SDR, champion, prospect)
3. What sales stage is it for? (prospecting, discovery, demo, negotiation, close)
4. Who is the target persona? (title, seniority, department)
5. What are the top 3 objections you hear most?

## Related Skills

- **competitor-alternatives**: for public-facing comparison and alternative pages
- **copy**: for marketing website copy
- **product-marketing-context**: for foundational positioning and messaging

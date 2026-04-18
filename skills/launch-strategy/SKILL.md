---
name: launch-strategy
description: "When the user wants to plan a product launch, feature announcement, or release strategy. Also use when the user mentions 'launch,' 'Product Hunt,' 'feature release,' 'announcement,' 'go-to-market,' 'beta launch,' 'early access,' 'waitlist,' 'product update,' 'how do I launch this,' 'launch checklist,' 'GTM plan,' or 'we're about to ship', 'lançar produto', 'plano de lançamento', 'como lanço isso', 'estratégia de lançamento'. Use this whenever someone is preparing to release something publicly. For ongoing marketing after launch, see marketing-ideas."
metadata:
  version: 1.2.0
---

# Launch Strategy

**Role:** expert in SaaS product launches and feature announcements. Plan launches that build momentum, capture attention, and convert interest into users.

**Iron Law:** best companies don't just launch once — they launch again and again. A strong launch isn't a single moment. It's getting your product into users' hands early, learning from real feedback, making a splash at every stage, and building momentum that compounds.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

## Workflow

```
Launch Strategy Progress:

- [ ] Step 1: Classify what's being launched ⚠️ REQUIRED
  - [ ] 1.1 New product? Major feature? Minor update?
  - [ ] 1.2 Audience size and engagement today?
  - [ ] 1.3 Owned channels available? (email list, blog, community)
  - [ ] 1.4 Timeline and team capacity?
- [ ] Step 2: Channel Strategy (ORB)
  - [ ] 2.1 Load references/orb-framework.md
  - [ ] 2.2 Pick 1-2 owned channels (start here)
  - [ ] 2.3 Pick 1-2 rented channels (drive to owned)
  - [ ] 2.4 Identify borrowed opportunities (podcasts, influencers, guest posts)
- [ ] Step 3: Phased Launch Plan
  - [ ] 3.1 Load references/five-phases.md
  - [ ] 3.2 Map current state to phase (internal → alpha → beta → early access → full)
  - [ ] 3.3 Define exit criteria per phase
- [ ] Step 4: Product Hunt (optional)
  - [ ] Load references/product-hunt-playbook.md if user wants PH launch
  - [ ] Pre-launch prep (relationships, listing, communities)
  - [ ] Launch day engagement plan
- [ ] Step 5: Checklist & Deliver
  - [ ] 5.1 Run Launch Checklist below
  - [ ] ⛔ GATE: Present launch plan to user before execution
```

## Core Philosophy

The best launches share four traits:

1. **Get your product into users' hands early** — don't wait for "perfect"
2. **Learn from real feedback** — internal → alpha → beta → full
3. **Make a splash at every stage** — each phase is a marketing moment
4. **Build compounding momentum** — every launch feeds the next

## ORB Framework (quick reference)

Structure launch marketing across three channel types. Everything should ultimately lead back to owned channels.

- **Owned** = you control it (email, blog, community). Start here — compounds over time.
- **Rented** = visibility without control (social, marketplaces, YouTube). Use to drive to owned.
- **Borrowed** = someone else's audience (guest posts, podcasts, influencers). Instant credibility.

For detailed channel tactics + case studies (Superhuman, Notion, TRMNL), load [references/orb-framework.md](references/orb-framework.md).

## Five-Phase Launch Approach (quick reference)

| Phase | Goal | Key action |
|-------|------|-----------|
| **1. Internal** | Validate core with friendly users | Recruit 1-1 testing |
| **2. Alpha** | First external validation | Landing page + signup form |
| **3. Beta** | Build buzz, refine product | Email early access list + teasers |
| **4. Early Access** | Validate at scale | Leak details, gather data |
| **5. Full Launch** | Maximum visibility | Open self-serve, PR blitz |

For phase-by-phase actions + expansion options, load [references/five-phases.md](references/five-phases.md).

## Product Hunt (optional)

Can be powerful for reaching early adopters, but requires significant preparation. Not for every launch — ask if the audience fits (tech-savvy early adopters).

For full PH playbook + SavvyCal and Reform case studies + post-launch + ongoing strategy, load [references/product-hunt-playbook.md](references/product-hunt-playbook.md).

## Launch Checklist

### Pre-Launch
- [ ] Landing page with clear value proposition
- [ ] Email capture / waitlist signup
- [ ] Early access list built
- [ ] Owned channels established (email, blog, community)
- [ ] Rented channel presence (social profiles optimized)
- [ ] Borrowed channel opportunities identified (podcasts, influencers)
- [ ] Product Hunt listing prepared (if using)
- [ ] Launch assets created (screenshots, demo video, GIFs)
- [ ] Onboarding flow ready
- [ ] Analytics/tracking in place

### Launch Day
- [ ] Announcement email to list
- [ ] Blog post published
- [ ] Social posts scheduled and posted
- [ ] Product Hunt listing live (if using)
- [ ] In-app announcement for existing users
- [ ] Website banner/notification active
- [ ] Team ready to engage and respond
- [ ] Monitor for issues and feedback

### Post-Launch
- [ ] Onboarding email sequence active
- [ ] Follow-up with engaged prospects
- [ ] Roundup email includes announcement
- [ ] Comparison pages published
- [ ] Interactive demo created
- [ ] Gather and act on feedback
- [ ] Plan next launch moment

## Anti-Patterns

- **Launch once and done** — best companies launch continuously. Every feature is a launch.
- **Skip internal/alpha** — shipping to public without friendly feedback = public bugs
- **Relying only on rented channels** — algorithm change kills your distribution
- **Product Hunt as savior** — PH traffic is short-lived. Convert to owned relationships.
- **No exit criteria per phase** — drifting forever in beta. Define "ready for next phase" up front.
- **Silence after launch day** — launches need ongoing content, not a one-shot
- **Launching without owned channels** — rented/borrowed alone won't compound
- **Ignoring small updates** — even changelog entries signal active development to users

## Task-Specific Questions

1. What are you launching? (New product, major feature, minor update)
2. What's your current audience size and engagement?
3. What owned channels do you have? (Email list size, blog traffic, community)
4. What's your timeline for launch?
5. Have you launched before? What worked/didn't work?
6. Are you considering Product Hunt? What's your preparation status?

## Related Skills

- **copy**: for launch and onboarding emails, landing page copy
- **marketing-ideas**: for additional launch tactics
- **competitor-alternatives**: for post-launch comparison pages
- **sales-enablement**: for launch sales collateral and enablement materials
- **site-architecture**: for URL structure of launch assets

# Step 0: Pre-build Research — 8 Blocking Questions

> **Load this file** at the start of `--full` mode (skill creation). Not needed for `--evolve --light` (small textual edits on existing skills).

## Why this step exists

User already has 40+ skills installed. Innovation tokens are limited (Choose Boring Technology principle). Maybe a solution already exists — building "skill 41 to solve the problem of having built too many skills" is self-parody.

This step runs BEFORE any creation work. If 3+ questions fail → skill-builder refuses creation and recommends a 2-hour spike first.

## The 8 questions

Answer each honestly. Document answers in `skill-rationale.md` next to the new SKILL.md.

### 1. What is the concrete pain?
One sentence, with a real example from the last week. **Not hypothetical.**

Bad: "It would be useful to automate X"
Good: "Yesterday I spent 40min manually refactoring three component files — this was the third time this month"

### 2. How many times has this pain appeared in the last 30 days?
If <3: stop. Wait for more evidence to accumulate. Build after the pattern is real, not anticipated.

### 3. Did I already search in all of these places?
Check each box with evidence (command ran + findings):

- [ ] (a) Local skills in `skillforge-arsenal/skills/` — `grep -ri <topic> ~/skillforge-arsenal/skills/`
- [ ] (b) Anthropic skills repo — `github.com/anthropics/skills`
- [ ] (c) MCP registries — `mcp.so`, `glama.ai/mcp`, `smithery.ai`
- [ ] (d) GitHub topic — `github.com/topics/claude-skill`
- [ ] (e) `awesome-claude-code` lists

**Shortcut:** invoke `reference-finder --solution-scout <topic>` to do all 5 searches in parallel with a ranked output.

### 4. If something similar exists: why doesn't it serve?
Specific answer, not "I didn't like it". Be concrete:
- Missing critical feature X
- Wrong language/stack
- Abandoned (last commit > 1 year)
- License conflict
- Would require more effort to adapt than to build

If the answer is vague, use the existing solution.

### 5. Is this core or commodity?

- **Core** — codifies a specific way this user decides or works (worth building, unique value)
- **Commodity** — any tech lead would want the same thing (probably exists already, search more before building)

Commodities favor reuse. Core favors building.

### 6. How many innovation tokens does this cost?
Consider:
- Maintenance burden over time
- Cognitive load to remember it exists
- Risk of breaking other skills
- Documentation debt
- Testing effort

Is the value worth the total cost? Be honest.

### 7. Can I solve this with a 2-hour spike instead of a permanent skill?
A lot of things that become "skills" were just well-written prompts used once. A spike with a good prompt + markdown artifact might be enough.

Skills are for patterns you'll invoke repeatedly. One-offs don't need skill infrastructure.

### 8. If I build it, what is the deletion criterion?
Without an exit criterion, the skill becomes accumulated debt. User already has 40+ skills. Some should go.

Examples of good deletion criteria:
- "Delete if not invoked in 60 days"
- "Delete when upstream tool X gets native support"
- "Delete after project Y ships"

Without a criterion, the skill becomes a zombie.

## Gate logic

⛔ **Blocking behavior:**

- **All 8 pass** → proceed to Step 1 (Understand)
- **1-2 fail** → proceed with caution, document the risks in `skill-rationale.md`
- **3+ fail** → REFUSE creation. Return this message:

```
⛔ Pre-build Research failed (X/8 criteria not met).

Recommendation: 2-hour spike instead of new skill.

Searches to run first:
- reference-finder --solution-scout <topic>
- awesome-claude-code README
- github topic claude-skill
- mcp.so / glama.ai / smithery.ai

Come back with results before attempting to create the skill.
```

## When to skip Step 0

Only skip if running `--evolve --light` — surgical edit on an existing skill that already passed Step 0 previously. All other modes (especially `--full` and `--evolve --heavy`) must run Step 0.

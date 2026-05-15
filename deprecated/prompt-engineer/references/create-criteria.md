# Universal Criteria for `--create` Mode

> **Load this file** during `--create` mode (Step 3 Build) to get the universal checklist that applies to any new prompt regardless of type. For `--validate` mode, these criteria are formalized in the type-specific rubric YAML files — don't load this, load the rubric.

## Checklist

| Criterion | Ask yourself | Red flag |
|-----------|-------------|----------|
| **Context/Role** | Does the model know who it is and for what? | Generic, personality-less output |
| **Specific instructions** | Clear actions or vague direction? | Model invents behavior |
| **Output format** | Precisely defined (JSON schema, XML tags, template)? | Inconsistent between runs |
| **Examples (few-shot)** | At least 1 input→output? | Model guesses format |
| **Edge cases** | Handles invalid, empty, unexpected? | Silent failure in production |
| **What not to do** | Explicit anti-patterns? Phrased positively? | Undesired behaviors slip through |
| **Attention budget** | Too long? Redundant? | Diluted attention, high cost |
| **Language calibration** | Excess caps lock? Literal "MUST"/"NEVER" everywhere? | Overtriggering in Claude 4.x |
| **Tool management** | Minimal, no overlap? | Model confuses tools |

## How to apply

During `--create`:

1. **Before writing the prompt:** read the type-specific reference (system-prompts.md, json-schema-output.md, etc.)
2. **While drafting:** use this checklist as a mental gate for each section
3. **After drafting:** walk through each criterion asking "does my prompt clearly do this?"
4. **Red flags detected:** go back and fix before presenting to user

## Why these nine criteria

They cover the failure modes that show up most in production prompts:
- **R001-R003** (role, format, instructions) — the three things that decide if the prompt works at all
- **R004-R005** (edge cases, few-shot) — the difference between works-in-demo and works-in-production
- **R006** (anti-patterns positive) — prevents model from over-learning the negative framing
- **Attention budget** — killer of otherwise good prompts
- **Language calibration** — Claude 4.x specific, overtriggering is silent
- **Tool management** — only when the prompt uses tools

For type-specific criteria and weighted scoring, see the rubric YAML files:
- `rubric/claude-md.yaml`
- `rubric/technical-plan.yaml`
- `rubric/iron-laws.yaml`
- `rubric/system-prompt.yaml`

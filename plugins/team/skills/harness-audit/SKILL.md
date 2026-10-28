---
name: harness-audit
description: Audits the agent harness of a repo or of team-ai itself - AGENTS.md, CLAUDE.md, REVIEW.md, skills, hooks, permissions, CI checks - for rules that are stale, contradictory, too long, unused or never enforced, and proposes what to cut, merge or turn into a hook. Use when running the monthly harness retro, after a new model release, or when asked to audit agent instructions, skills, prompts or the harness.
disable-model-invocation: true
---

# Harness audit

Instructions rot: written for an older model, contradicted by a newer rule,
pointing at files that moved, or ignored because nothing checks them. The
audit finds that rot and proposes cuts. Shorter is the usual fix.

## Scope

The current repo: `AGENTS.md`, `CLAUDE.md` (and nested ones), `REVIEW.md`,
`.claude/settings.json`, `.claude/hooks/`, `.claude/skills/`, `.agents/skills/`,
`Makefile`, `.github/workflows/`, `.pre-commit-config.yaml`.
In team-ai: every `SKILL.md`, its references, `evals/`, `CATALOG.md`.

Read-only. Nothing is changed until the person picks the proposals.

## What to look for

| Problem | How to see it |
|---|---|
| **Dead reference** | a path, command, make target or tool named in an instruction that does not exist |
| **Contradiction** | two rules that cannot both hold (between AGENTS.md and a skill, a skill and REVIEW.md, a rule and a deny rule) |
| **Stale for the model** | step-by-step recipes for things the model now does well; shouting (MUST, NEVER in caps) around ordinary rules; workarounds for old limits |
| **Bloat** | `AGENTS.md` over 150 lines, a `SKILL.md` body over 150, text that only says what the repo already shows |
| **Unenforced rule** | a rule agents broke twice (in PR comments, reverts, `docs/PROGRESS.md` pitfalls) with no hook, deny rule or CI check behind it |
| **Unused skill** | no mention in commits, PRs or sessions for a month; status still `expérimental` (team-ai: `CATALOG.md` "Revu le") |
| **Weak trigger** | a skill `description` that does not say when to use it, or uses words nobody types |
| **Eval gap** | a skill with no brief in `evals/`, or a real failure with no brief |

Evidence for usage: `git log --since="1 month ago"`, `gh pr list --state merged
--search "<skill name>"`, PR review threads. No data: say so instead of
guessing usage.

## Report

```
Harness audit · <repo> · <date>

Cut (n)
- AGENTS.md:42-58 — build steps the Makefile already runs. Replace with "make check".
Fix (n)
- skills/publish/SKILL.md:31 — names scripts/check_branch.sh, moved to scripts/ci/.
Enforce (n)
- "never commit .env" broken in PR #31 and #44 → deny Read(./.env*) + gitleaks pre-commit.
Merge or remove skills (n)
- weekly and deck overlap on the weekly profile → keep deck, delete weekly.
Re-run evals
- code-review: 5 briefs, last run 2026-09-02, model changed since.
```

Each line cites `file:line` or a PR. At most 15 proposals, ranked by how much
confusion or risk they remove.

## After a new model

Also: re-read every skill description and the five longest instructions, cut
what the new model does unprompted, re-run the evals of the most used skills,
and update "Revu le" in `CATALOG.md` for those reviewed.

## Applying

On the person's pick, one PR per kind of change (cuts, fixes, new
enforcement), so each can be reverted alone.

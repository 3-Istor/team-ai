---
name: handoff
description: Write or update docs/PROGRESS.md so another person or agent can pick the work up cold, with what is done, in progress, the next step and the traps. Use when ending a work session, before switching task, tool or teammate, or when asked for a handoff or where the work stands.
---

# Handoff

`docs/PROGRESS.md` is where the next session starts. Write it for someone who
has not seen this conversation, may use another tool, and has ten minutes.

## Gather the facts

- `git status`, `git log --oneline -15`, the current branch and open PR.
- What this session changed and why, the commands that were run and their
  results (tests green or red, with the failing names).
- The ticket and spec the work belongs to.

Write only what you can check. A guess is labelled as one.

## Format

Keep the file to one screen. Replace stale sections; do not append forever.

```markdown
# Progress

_Updated 2026-10-28 by <name or agent> on branch `PROJ-42-login-sso`_

## Goal
One sentence, with the ticket and spec: PROJ-42, docs/specs/004-login-sso.md

## Done
- SSO callback handled server-side, tests in tests/auth/test_sso.py (green)

## In progress
- Role mapping from the school directory: half done, see src/auth/roles.py:30

## Next step
`make test T=tests/auth/test_roles.py`, then map the "staff" group (open
question below).

## Traps
- The IdP sandbox rejects localhost callbacks: use the tunnel in README.

## Open questions
- Do staff accounts get admin rights? Asked in PROJ-42, no answer yet.

## History
- 2026-10-27 — callback + tests (PR #18)
```

## Rules

- **Next step** is a concrete first action: a command, a file and line, or a
  decision to ask for.
- **Traps** are what cost time and will cost it again. If a trap is a rule
  for the whole repo, also propose a line for `AGENTS.md`.
- Keep the last five **History** entries; older ones are in git.
- Link PRs, tickets and specs by id or path, never paste their content.
- No secrets, tokens or internal URLs with credentials.

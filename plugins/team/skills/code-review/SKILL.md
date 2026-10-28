---
name: code-review
description: Review a diff, branch or pull request against the repo's REVIEW.md, accepted ADRs and spec, with depth set by the risk of the changed paths. Use when asked to review code, a PR or MR, a branch or "my changes", or before opening a PR.
---

# Code review

The job is to find what would break, with evidence. Not to approve, not to
restyle, not to rewrite.

## 1. Gather, in this order

1. **The diff.** Local work: `git diff --merge-base origin/main`. A PR:
   `gh pr diff <n>` (GitLab: `glab mr diff <n>`).
2. **The intent.** PR description, linked ticket, and the spec in
   `docs/specs/` it points to. No stated intent: say so in the report.
3. **`REVIEW.md`** at the repo root. Its rules win over this skill's defaults.
4. **Accepted ADRs** in `docs/adr/` (`status: accepted`) whose subject the
   diff touches.
5. **Earlier rounds.** On a PR, read the existing review comments
   (`gh pr view <n> --comments`) and note the round number and the last
   reviewed commit.

## 2. Set the depth from the diff, never from the author

Use the tiers in `REVIEW.md`. Without them, these defaults:

| Tier | Changed paths | Depth |
|---|---|---|
| high | auth, permissions, payment, secrets handling, CI workflows, infra/IaC, DB migrations | deep pass + [security pass](references/security.md); needs 2 human approvals |
| low | only docs, `*.md`, comments, copy | quick: is what's written true? |
| medium | anything else | standard |

The highest tier touched wins. Write the tier and the path that set it on the
report's first line.

## 3. What to look for

- **Does it do what the intent says?** Edge cases, error paths, empty and
  huge inputs, concurrency where it applies.
- **Does it break something else?** Search the callers of every changed
  function, type or endpoint. Check contracts (OpenAPI, shared types,
  migrations, config keys).
- **ADRs.** A change that goes against an accepted ADR is an Important
  finding: quote the ADR id. The fix is either the code, or a new ADR with
  `supersedes`.
- **Where controls run.** Access checks and validation must run server-side.
- **Tests.** Do they check behaviour, or only replay the implementation? A new
  user path with no end-to-end test is a finding.
- **Duplication.** Logic pasted instead of reused: one finding listing every
  copy.
- **Stale docs.** A changed command, structure or behaviour that leaves
  `AGENTS.md`, a spec or the README wrong.

## 4. Report

```
Tier: high (touches .github/workflows/ci.yml)
2 issues to fix · 1 nit · 1 pre-existing

[Important] src/api/users.py:42 — GET /users/{id} returns any user to any
logged-in caller; the owner check is only in the front (web/UserPage.tsx:18).
Fix: check owner or admin role in the handler.
[Important] ...
[Nit] ...
[Pre-existing] src/db.py:88 — ... (not introduced by this diff, not blocking)
```

- Every finding names `file:line` and what you saw there. Can't confirm it?
  Drop it, or mark it `unverified` and don't count it.
- At most 3 nits. Nothing a formatter or linter would catch.
- One finding per class of bug, listing every place it occurs.
- Nothing to fix: write `0 issues` plainly. Never pad the report.
- Never approve. Change code only when asked to fix.

## 5. Converge

- **Round 3 or later:** stop adding nits. Say whether the approach itself
  should be reconsidered.
- **From round 3:** review only the commits since the last reviewed one
  (`git diff <last-reviewed-sha>..HEAD`).
- **Never repeat** a finding already posted; point to it if still open.

## Posting

Post only when asked. GitHub: `gh pr review <n> --comment --body-file report.md`
(inline comments through the API when available). GitLab: `glab mr note <n>`.

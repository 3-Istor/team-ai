---
name: code-review
description: Review a diff, branch or pull request against the repo's REVIEW.md, AGENTS.md, accepted ADRs and spec, with depth set by the risk of the changed paths, and only verified findings reported. Use when asked to review code, a PR or MR, a branch or "my changes", before opening a PR, or to check a fix before merging.
---

# Code review

The job is to find what would break, with evidence. Not to approve, not to
restyle, not to rewrite. A wrong finding costs the author a round trip: it is
worse than no finding.

## 1. Gather, in this order

1. **The diff.** Local work: `git diff --merge-base origin/main`. A PR:
   `gh pr diff <n>` (GitLab: `glab mr diff <n>`).
2. **The intent.** PR description, linked ticket, and the spec in
   `docs/specs/` it points to. No stated intent: say so in the report.
3. **`REVIEW.md`** at the repo root, plus any `REVIEW.md` in a parent folder
   of a changed file. Its rules win over this skill's defaults: what failure
   means here, what is Important, what to skip, the nit cap.
4. **`AGENTS.md` / `CLAUDE.md`**, root and in parent folders of changed files.
   A change that breaks one of their rules is a finding.
5. **Accepted ADRs** in `docs/adr/` (`status: accepted`) whose subject the
   diff touches.
6. **Earlier rounds.** On a PR, read the existing review comments
   (`gh pr view <n> --comments`) and note the round number and the last
   reviewed commit.

## 2. Set the depth from the diff, never from the author

Use the tiers in `REVIEW.md`. Without them, these defaults:

| Tier | Changed paths | Depth |
|---|---|---|
| high | auth, permissions, payment, secrets handling, CI workflows, infra/IaC, DB migrations, installers, release | deep pass + [security pass](references/security.md) + second opinion (§5) |
| low | only docs, `*.md`, comments, copy | quick: is what's written true? |
| medium | anything else | standard |

The highest tier touched wins. Write the tier and the path that set it on the
report's first line. Paths `REVIEW.md` says to skip get no finding.

## 3. What to look for

- **Does it do what the intent says?** Edge cases, error paths, empty and
  huge inputs, concurrency where it applies.
- **A bug fix: is it the root cause?** A fix that silences the symptom
  (catch-all, retry, null check at the crash site) while the cause stays is
  an Important finding. Say where the cause is.
- **Does it break something else?** Search the callers of every changed
  function, type or endpoint. Check contracts (OpenAPI, shared types,
  migrations, config keys).
- **ADRs and project rules.** A change that goes against an accepted ADR or
  an `AGENTS.md` rule is Important: quote the ADR id or the rule. The fix is
  either the code, or a new ADR with `supersedes`.
- **Where controls run.** Access checks and validation run server-side.
- **Tests.** Do they check behaviour, or only replay the implementation? A new
  user path with no end-to-end test is a finding.
- **Duplication.** Logic pasted instead of reused: one finding listing every
  copy.
- **Docs that now lie.** A changed command, structure or behaviour that leaves
  `AGENTS.md`, a spec or the README wrong. Also a line of `AGENTS.md` the diff
  proves stale.

Nothing CI already enforces (lint, format, types). Nothing about naming or
style unless `REVIEW.md` asks for it.

## 4. Verify every candidate before reporting

List candidates first, then check each one against the code, not the diff
alone:

- Open the file at the line. Follow the call path far enough to name the
  **concrete input or state that breaks it**.
- A claim about behaviour cites the `file:line` where that behaviour lives,
  never an inference from a function or variable name.
- Already present before this diff: tag it `[Pre-existing]`, never blame the
  author for it.
- Cannot confirm it: drop it. If it matters too much to drop, keep it marked
  `unverified`, outside the count.

## 5. Second opinion on high tier

When the tier is high and subagents are available, give a fresh-context
subagent the diff, `REVIEW.md` and the intent only (not your findings). Keep
a finding when both passes found it or when you can still prove it after
reading the other pass. Without subagents, re-read the diff once from the
top after §4 and say the second opinion was not run.

## 6. Report

```
Tier: high (touches .github/workflows/ci.yml)
2 issues to fix · 1 nit · 1 pre-existing

[Important] src/api/users.py:42 — GET /users/{id} returns any user to any
logged-in caller; the owner check is only in the front (web/UserPage.tsx:18).
Breaks when: user A requests /users/<id of B>.
Fix: check owner or admin role in the handler.
[Nit] ...
[Pre-existing] src/db.py:88 — ... (not introduced by this diff, not blocking)

Humans should look at: the token refresh path, which no test exercises.
```

- The summary starts with the counts. Nothing to fix: `0 issues`, plainly.
  Never pad the report.
- Every finding names `file:line`, what breaks and for which input.
- At most 3 nits, or `REVIEW.md`'s cap.
- One finding per class of bug, listing every place it occurs, so the author
  fixes all of them at once.
- End with what the checks and this review would miss, if anything: that is
  where a human should spend time.
- Never approve. Change code only when asked to fix.

## 7. Converge

- Every finding gets an answer: fixed, or closed with a one-line reason
  (wrong, intentional, does not matter). A closed finding is not reposted.
- **Round 3 or later:** stop adding nits. Say whether the approach itself
  should be reconsidered.
- **From round 3:** review only the commits since the last reviewed one
  (`git diff <last-reviewed-sha>..HEAD`).
- **Never repeat** a finding already posted; point to it if still open.

## Posting

Post only when asked. GitHub: `gh pr review <n> --comment --body-file report.md`
(inline comments through the API when available). GitLab: `glab mr note <n>`.

## Getting better

A bug that reached `main` despite a review becomes a brief in
`evals/code-review/` of the team-ai repo. A finding closed as wrong twice for
the same reason becomes a line in the project's `REVIEW.md`.

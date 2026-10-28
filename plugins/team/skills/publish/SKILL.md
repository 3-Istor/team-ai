---
name: publish
description: Turns finished local work into a draft pull or merge request ready for review - checks, self-review, PR body from evidence, ticket link. Use when the person runs /team:publish or asks to push and open a PR or MR for the current branch.
disable-model-invocation: true
---

# Publish

One command from "it works on my machine" to a draft PR a reviewer can read in
two minutes. Nothing is pushed until the checks have run and the person has
seen the summary.

## Gate: evidence first

1. `git status`: uncommitted changes or untracked files that look like work:
   ask whether they belong in this PR. Never `git add -A` blindly; never stage
   `.env`, keys, dumps or large binaries.
2. Branch name starts with a ticket key (`scripts/check_branch.sh` when the
   repo has it). On `main`: stop, propose a branch name.
3. `make check` (or the command `AGENTS.md` names). Read the full output.
   Red: stop and report the failures. Do not open a PR on red, not even a
   draft, unless the person says so.
4. Rebase on the latest base branch if it moved; rerun the checks if the
   rebase changed anything.

## Self-review

Review the diff in a fresh context when possible (a subagent with the diff,
`REVIEW.md` and the spec), otherwise re-read it top to bottom. Fix what is
clearly wrong and in scope; list the rest for the person. Look also for
debug leftovers, commented-out code, TODOs without owner, and docs the change
made wrong (`AGENTS.md`, spec, README).

## The PR body

Fill the repo's `.github/pull_request_template.md` (GitLab:
`.gitlab/merge_request_templates/`) from evidence, never from intentions:

- **Quoi et pourquoi**: 2 lines, ticket key and spec path.
- **Testé comment**: the command run and the relevant lines of its output.
  UI change: a screenshot.
- **Risque**: the tier from `REVIEW.md` and the path that sets it.
- **Comment revenir en arrière**: revert, flag, migration down. "Revert the
  PR" is only true if nothing else depends on it.
- **Pilote**: the person who ran the agent. Ask if unknown.

Title in Conventional Commits form, under 72 characters.

## Show, then act

Show the person, in one message: the checks result, the self-review findings,
the PR title and body. Then, on their OK only:

```
git push -u origin <branch>
gh pr create --draft --title "<title>" --body-file <file>   # GitLab: glab mr create --draft
```

Then, still on their OK, link the ticket (comment with the PR URL, move it to
"In review" if the tracker MCP is available). Give back the PR URL.

## Never

- Force-push, push to `main`, merge, approve, or mark ready for review.
- Skip hooks (`--no-verify`).
- Claim the checks pass without having run them in this session.

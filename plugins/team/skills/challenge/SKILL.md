---
name: challenge
description: Argues against a plan, spec, design or decision on purpose to find its weak points, in one of five modes (contre, pour, alternatives, pre-mortem, jury). Use when asked to challenge, contradict, play devil's advocate, stress-test, red-team, poke holes, run a pre-mortem, prepare a defence or oral exam (soutenance, jury), or before a spec or ADR is validated.
---

# Challenge

The job is to make the idea better by attacking it honestly. Agreement is
cheap and the person can get it anywhere: here, every answer contains at least
one serious objection, or says plainly that none survived a real attempt.

## Read first

The plan, spec, ADR or code being challenged, and what it builds on
(`AGENTS.md`, accepted ADRs, the ticket). Attack what it says, not a
caricature: restate the idea in two lines first and ask if the restatement is
right when it is ambiguous.

## Modes

Take the mode from the request; none given, use `contre`.

| Mode | What you do |
|---|---|
| `contre` | The strongest case against: why it fails, costs more than it gives, or solves the wrong problem |
| `pour` | The strongest case for, steelmanned, then the one assumption it all rests on |
| `alternatives` | 3 genuinely different ways to reach the same goal, including "do nothing" and "buy or reuse", each with what it trades off |
| `pre-mortem` | It is six months later and it failed. Write the 5 most likely causes, the early signal for each, and what to do now |
| `jury` | The 10 hardest questions an expert panel would ask, hardest first, each with what a good answer must contain |

## Each objection

```
[Bloquant | Sérieux | À surveiller] <claim in one sentence>
Pourquoi ça compte : <consequence, for whom>
Ce qui trancherait : <the test, measure, source or prototype that settles it>
```

- Rank by how much it would change the decision, not by how easy it is to say.
- Ground objections in the material: cite the spec line, the ADR, the code,
  a source with a URL. A generic risk ("security", "scalability") with no
  link to this plan is not an objection.
- 3 to 7 objections. More is padding.

## Holding a position

- When the person answers an objection, update only on a new argument or new
  evidence, and say which one convinced you. Pushback alone is not a reason to
  fold.
- When they are right, concede in one line and move on.
- Never soften a Bloquant into "something to consider".

## End every answer with

- **Ce qui me ferait changer d'avis**: the evidence that would remove the main
  objection.
- **Prochaine action**: the cheapest step that tests the biggest risk.

## Pitfalls

- Opening with praise. Start with the strongest objection.
- Rewriting their plan into yours. Challenge it; propose alternatives only in
  the `alternatives` mode or when asked.
- In `jury` mode, questions that test vocabulary instead of understanding:
  ask why, what if, and what you would do differently.

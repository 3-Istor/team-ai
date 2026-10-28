---
name: cadrage
description: Frames a new project or feature before any code through a short interview, a sourced state of the art and the business and engineering value, then writes the first spec. Use when starting a project, a feature or a school project, when asked for a cadrage, kick-off, brief, scoping, "interview me", "what should we build", or when a request has no spec yet.
---

# Cadrage

The goal is a spec someone else could build from and defend orally, written
before the first line of code. Most of the value is in the questions: people
rarely know all of what they want when they start.

## Look before you ask

Read what already exists first: `AGENTS.md`, `docs/specs/`, `docs/adr/`, the
README, the ticket, files the person pointed at. Never ask what the repo or the
conversation already answers.

## The interview

- **One question per message**, specific to what they said, with why you ask
  it: what the answer changes about what gets built.
- Open questions first. Offer a short menu only when they are stuck. When they
  say "just guess", propose something concrete and mark it as your call.
- **Play back** each part once you understand it, in 150-250 words, then ask
  what is wrong or missing. Only what they said goes in as theirs.
- Cover this ground, never as a questionnaire:
  - who has the problem today, and how they cope without us
  - what success looks like, and how we would measure it
  - goals, non-goals, and **anti-goals** (what would make it a failure even if
    it works)
  - constraints: deadline, stack imposed, platform services to use, budget,
    data, who validates
  - prior art they know, liked or hated
- They want to skip the questions: say the defaults you will take in one line
  each, then go.

## State of the art

Once the problem is clear, look at what exists: products, open-source
projects, papers, internal projects of 3-Istor. Search official docs, repos
and known sources first; cite a URL for every claim. Bring back:

- 3 to 5 existing solutions, what each does well, why it does or does not fit
- what we would reuse instead of build
- what nobody does well: that is often where the value is

No source found: say so. Never invent a product, a figure or a quote.

## Value

Two short paragraphs, both required:

- **Business value**: who gains what, in their terms. A measure we can check
  after delivery (time saved, errors avoided, users served).
- **Engineering value**: what the team learns or proves (a technique, a
  platform service, an architecture). A school project that is only "a fancy
  Excel" fails here: say it.

## Approaches

Before writing the spec, put 2 or 3 real ways of building it in one message:
what each trades off, which constraint rules one out, your recommendation and
why. They pick. Their choice goes in the spec; a structuring choice also gets
an ADR in `docs/adr/`.

## Output

1. `docs/specs/NNN-<slug>.md` from `docs/specs/TEMPLATE.md` (next free
   number). Acceptance criteria checkable by someone other than the author:
   they become the end-to-end tests.
2. The `## Projet` section of `AGENTS.md` (2-3 lines) if still `[À REMPLIR]`.
3. A `## État de l'art` section in the spec with the sources.
4. On request, a kick-off outline: one title per slide, each title a sentence
   that states a conclusion.

Status of the spec: `brouillon` until a human validates it.

## Pitfalls

- Starting to design the solution in the first message. Understand the
  problem first.
- A list of five questions at once: people answer the easiest one.
- Acceptance criteria like "fast", "simple", "secure": ask for the number or
  the case that proves it.
- Several independent projects in one request: say so, agree on an order,
  frame them one at a time.

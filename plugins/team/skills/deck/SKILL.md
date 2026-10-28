---
name: deck
description: Builds slide decks in the 3-Istor visual identity from a short brief and an outline validated first, with profiles for kick-off, weekly and soutenance. Use when asked for slides, a deck, a presentation, a kick-off, a weekly update deck, a soutenance or demo deck, or to restyle slides to the 3-Istor look.
---

# Deck

A deck says one thing per slide, in the team's look, and is right the first
time because the structure is agreed before anything is drawn.

## 1. Brief: six answers

Ask only what the request and the material do not already answer, one
question per message:

1. **Audience**: who, and what they already know.
2. **Purpose**: the decision or action expected at the end.
3. **Profile**: kick-off, weekly, soutenance, or other (below).
4. **Length**: minutes or slide count.
5. **Material**: spec, CRs, tickets, PRs, figures. Read it; never invent a
   figure, a quote or a result. Missing figure: `[__]` placeholder, listed at
   the end.
6. **Constraints**: template imposed by a client or the school, language,
   format to deliver (Slides artifact, `.pptx`, PDF).

## 2. Outline: titles only, validated

Before any design, send the outline: one line per slide, grouped by section.

- Each title is a **sentence that states the conclusion** of the slide
  ("Le cache divise la latence par trois"), never a topic ("Performances").
- Read in sequence, the titles alone tell the whole story.
- One idea per slide. Two ideas: two slides.

Wait for the OK. Changes at this stage cost nothing.

## 3. Profiles

| Profile | Length | Spine |
|---|---|---|
| kick-off | 8-12 slides | problem → who suffers → state of the art → value → scope and non-goals → approach → plan → risks → asks |
| weekly | 4-6 slides | goal of the period → done (with evidence) → slipped and why → risks → next → decisions needed |
| soutenance | 12-20 slides | problem → stakes → approach and why → demo → results measured → limits → what we would do differently → next |

Weekly material comes from merged PRs, closed tickets and CRs of the period:
cite them.

## 4. Design

Use the tokens in [references/tokens.md](references/tokens.md): colors, type,
radii. On a client or school template, theirs win.

- **Assertion and evidence**: the title asserts, the body proves it with a
  figure, a chart, a diagram, a screenshot or a short quote. Turn bullet
  lists into a table, a diagram, big numbers or a comparison.
- One type scale, 4-5 sizes; nothing under 24 px on a 1920×1080 slide.
- The heading stays at the same place on every content slide.
- Every slide carries speaker notes: what to say that the slide does not.
- Motion: none by default; one build at most per slide, only to reveal in
  the order you speak.
- Diagrams of a system: draw them with Noodle when the plugin is installed,
  from the facts in the repo.
- A footer row with the page number; a source line on every slide that shows a
  figure.

## 5. Render

With the tool the person has: the Slides artifact type in claude.ai, the
`pptx` skill for a PowerPoint file, or Marp for a Markdown deck in the repo.
Ask when it is not obvious. Then give the link or the file and the list of
placeholders left to fill.

## Pitfalls

- Starting to draw before the outline is agreed.
- A slide per bullet point of the material: select, do not transcribe.
- Decoration that encodes nothing: numbered markers on things that are not a
  sequence, labels above every heading, icons for the sake of it.

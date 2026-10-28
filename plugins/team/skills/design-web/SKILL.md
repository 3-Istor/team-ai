---
name: design-web
description: Builds or changes web UI in the 3-Istor visual identity (shared tokens, project components first) and proves it on screen with browser screenshots before calling it done. Use when creating or changing a page, component, layout or style in a 3-Istor web front-end, or when asked to make the UI look right, match a mockup or apply the 3-Istor design.
---

# Design web

A 3-Istor front looks like the other 3-Istor fronts, not like a generic
generated page, and nobody calls it done without having seen it rendered.

## Before writing code

1. **Use what the project has**: its components, its CSS variables or theme
   file, its UI library. Extend them; never create a parallel set.
2. **Tokens**: colors, type, radii and spacing come from
   [references/tokens.md](references/tokens.md). No project theme yet: create
   one CSS variables file (or the framework's theme) from these tokens and use
   only the variables afterwards.
3. **The page's one job**: what the user comes to do. The first screen shows
   that, with real content from the brief or the API, not lorem ipsum.
4. **Plan in one short message** when the change is more than a fix: layout
   (an ASCII wireframe is enough), which components, what is new. Check it
   against the generic defaults below, change what is default rather than
   chosen.

## Generic defaults to avoid unless the brief asks for them

- Content cut into identical rounded cards with the same grey shadow.
- A label in spaced capitals above every heading; one word of a title in
  another color.
- Gradient washes and glows as decoration.
- Fade-and-slide animations on every section; hover effects on every card.
- Numbered markers (01 / 02 / 03) on content that is not a sequence.

## Quality floor, always

- Responsive from 360 px wide; no horizontal scroll.
- Keyboard: every action reachable, focus visible.
- Contrast 4.5:1 for text (3:1 for large text and UI borders).
- `prefers-reduced-motion` respected; dark mode if the project has one.
- Copy: sentence case, a button says what it does ("Enregistrer", not
  "Valider"), errors say what happened and how to fix it.

## Prove it on screen

1. Run the app (the command in `AGENTS.md`).
2. Take screenshots with Playwright of every changed screen, at 390×844 and
   1440×900, after the network is idle:
   ```python
   page.goto(url); page.wait_for_load_state("networkidle")
   page.screenshot(path="shots/<screen>-<width>.png", full_page=True)
   ```
3. Look at them. Compare with the mockup if there is one; fix and re-shoot
   until they match. Check the console for errors.
4. Put the screenshots in the PR description. No screenshot, not done.

The screenshots stay out of the repo unless the project keeps visual
regression baselines.

## Pitfalls

- Styling inline or with one-off values when a token exists.
- Checking only the desktop width.
- Saying "it should look right" without having opened the page.

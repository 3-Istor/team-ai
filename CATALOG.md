# Catalogue

Un skill = une ligne. Mettre à jour dans la même PR que le skill.
Statuts : `expérimental` (on teste), `stable` (on s'en sert), `déprécié` (à supprimer).
« Revu le » = dernière relecture, notamment à chaque nouveau modèle.

| Skill | Plugin | À quoi il sert | Lancé par | Owner | Statut | Revu le |
|---|---|---|---|---|---|---|
| `code-review` | team | Review d'un diff ou d'une PR, profondeur selon le risque des chemins, REVIEW.md, AGENTS.md et ADR en contexte, findings vérifiés avant d'être remontés | agent ou `/team:code-review` | à désigner | expérimental | 2026-10-28 |
| `handoff` | team | Met à jour `docs/PROGRESS.md` pour qu'une autre personne ou un autre agent reprenne le travail | agent ou `/team:handoff` | à désigner | expérimental | 2026-10-28 |
| `work-ticket` | team | Tickets Jira, Linear, Notion, GitHub : à faire, rétro depuis les commits, bugs ; brouillon puis création après accord | agent ou `/team:work-ticket` | Brian | stable | 2026-10-28 |
| `tech-debt-audit` | team | Audit de dette technique et d'architecture du repo, findings cités, `TECH_DEBT_AUDIT.md` | humain seulement | Brian | stable | 2026-10-28 |
| `cadrage` | team | Interview avant la première ligne, état de l'art sourcé, valeur métier et d'ingénierie, première spec | agent ou `/team:cadrage` | à désigner | expérimental | 2026-10-28 |
| `challenge` | team | Contradiction en 5 modes (contre, pour, alternatives, pre-mortem, jury), objections sourcées, tient sa position | agent ou `/team:challenge` | à désigner | expérimental | 2026-10-28 |
| `publish` | team | `make check`, self-review, PR brouillon remplie avec des preuves, ticket lié ; jamais sans accord | `/team:publish` seulement | à désigner | expérimental | 2026-10-28 |
| `prio` | team | Ordre de backlog proposé avec score visible, bloquants d'abord ; ne déplace rien seul | agent ou `/team:prio` | à désigner | expérimental | 2026-10-28 |
| `cr` | team | Audio, transcript ou notes → CR : décisions, actions avec owner, risques ; tickets et ADR en brouillon | agent ou `/team:cr` | à désigner | expérimental | 2026-10-28 |
| `safe-search` | team | Recherche limitée à la doc 3-Istor et aux domaines autorisés, chaque fait sourcé | agent ou `/team:safe-search` | à désigner | expérimental | 2026-10-28 |
| `deck` | team | Decks dans la DA 3-Istor : brief, plan validé en titres, profils kick-off, weekly, soutenance | agent ou `/team:deck` | à désigner | expérimental | 2026-10-28 |
| `design-web` | team | Front aux tokens 3-Istor, composants du projet d'abord, preuve par captures avant « fini » | agent | à désigner | expérimental | 2026-10-28 |
| `noodle-diagram` | noodle | Diagrammes d'architecture en code avec lint de lisibilité (plugin externe) | agent | Brian | stable | 2026-10-28 |

## Origine

- `cadrage` : [superpowers brainstorming](https://github.com/obra/superpowers/tree/main/skills/brainstorming), [Spec Kit](https://github.com/github/spec-kit).
- `publish` : [superpowers finishing-a-development-branch et verification-before-completion](https://github.com/obra/superpowers/tree/main/skills).
- `cr` : format inspiré de [silverstein/minutes](https://github.com/silverstein/minutes).
- `safe-search` : [permissions Claude Code](https://code.claude.com/docs/en/permissions).
- `design-web` : [anthropics/skills frontend-design et webapp-testing](https://github.com/anthropics/skills/tree/main/skills). À fusionner avec le skill de Hamza.
- `deck` et `design-web` : tokens v0 repris du deck IA-Nizations, à valider.

- `code-review` : règles tirées de [How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/) (oct. 2026) et de la [doc REVIEW.md](https://code.claude.com/docs/en/code-review-customize).
- `tech-debt-audit` : d'origine [ksimback/tech-debt-skill](https://github.com/ksimback/tech-debt-skill) (MIT).
- `work-ticket` et `tech-debt-audit` : repris de [TheGostsniperfr/.dotfiles](https://github.com/TheGostsniperfr/.dotfiles/tree/main/user/app/ai/claude/skills).
- `noodle` : installé depuis [TheGostsniperfr/Noodle](https://github.com/TheGostsniperfr/Noodle), pas copié ici.

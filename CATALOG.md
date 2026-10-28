# Catalogue

Un skill = une ligne. Mettre à jour dans la même PR que le skill.
Statuts : `expérimental` (on teste), `stable` (on s'en sert), `déprécié` (à supprimer).
« Revu le » = dernière relecture, notamment à chaque nouveau modèle.

| Skill | Plugin | À quoi il sert | Lancé par | Owner | Statut | Revu le |
|---|---|---|---|---|---|---|
| `code-review` | team | Review d'un diff ou d'une PR, profondeur selon le risque des chemins, REVIEW.md et ADR en contexte | agent ou `/team:code-review` | à désigner | expérimental | 2026-10-28 |
| `handoff` | team | Met à jour `docs/PROGRESS.md` pour qu'une autre personne ou un autre agent reprenne le travail | agent ou `/team:handoff` | à désigner | expérimental | 2026-10-28 |
| `work-ticket` | team | Tickets Jira, Linear, Notion, GitHub : à faire, rétro depuis les commits, bugs ; brouillon puis création après accord | agent ou `/team:work-ticket` | Brian | stable | 2026-10-28 |
| `tech-debt-audit` | team | Audit de dette technique et d'architecture du repo, findings cités, `TECH_DEBT_AUDIT.md` | humain seulement | Brian | stable | 2026-10-28 |
| `noodle-diagram` | noodle | Diagrammes d'architecture en code avec lint de lisibilité (plugin externe) | agent | Brian | stable | 2026-10-28 |

## Origine

- `work-ticket` et `tech-debt-audit` : repris de [TheGostsniperfr/.dotfiles](https://github.com/TheGostsniperfr/.dotfiles/tree/main/user/app/ai/claude/skills).
- `noodle` : installé depuis [TheGostsniperfr/Noodle](https://github.com/TheGostsniperfr/Noodle), pas copié ici.

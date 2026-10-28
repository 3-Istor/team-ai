# Faire évoluer le harnais

## Quand créer quoi

On a guidé un agent **deux fois** sur la même chose :

| C'est… | Ça va dans… |
|---|---|
| une procédure (plusieurs étapes, un résultat) | un skill ici |
| une règle propre à un projet | l'`AGENTS.md` du projet |
| une règle sans exception | un hook, une deny rule ou un check de CI dans le template |
| une remarque de review qui revient | le `REVIEW.md` du projet |

## Proposer un skill

1. Branche `skill/<nom>`, dossier `plugins/team/skills/<nom>/`.
2. `SKILL.md` selon `AGENTS.md`, ligne dans `CATALOG.md` (statut `expérimental`).
3. Au moins un brief dans `evals/<nom>/` : la demande, ce qui doit et ne doit
   pas se passer.
4. `python3 scripts/validate.py` vert, PR relue par une autre personne.

## Entretien

- **Rétro du harnais, 30 min par mois** : quels skills ont servi, lesquels
  supprimer, quelles erreurs d'agent se sont répétées. `/team:harness-audit`
  prépare la liste.
- **Veille** : le ticket `veille` du lundi. Une proposition retenue devient une
  PR ici.
- **À chaque nouveau modèle** : relire les descriptions et les consignes trop
  détaillées, rejouer les evals, mettre à jour « Revu le » dans le catalogue.
- Un skill `expérimental` inutilisé depuis un mois passe `déprécié`, puis est
  supprimé.

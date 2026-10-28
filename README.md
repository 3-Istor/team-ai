# team-ai

Les skills et plugins partagés de l'équipe 3-Istor, pour Claude Code et Codex.
Un seul endroit pour les trouver, les installer, les relire et les faire évoluer.

## Installer

**Claude Code**, une fois par machine :

```
/plugin marketplace add 3-Istor/team-ai
/plugin install team@team-ai
/plugin install noodle@team-ai
```

Dans un projet créé depuis `3-Istor/project-template`, la marketplace et les
plugins sont déjà déclarés dans `.claude/settings.json` : Claude Code les
propose à l'ouverture du repo.

**Codex** (ou tout agent qui lit `.agents/skills`) :

```
git clone https://github.com/3-Istor/team-ai ~/team-ai
~/team-ai/scripts/sync-codex.sh            # pour toutes vos sessions
~/team-ai/scripts/sync-codex.sh ./mon-projet  # ou pour un seul projet
```

Relancer le script après un `git pull` pour récupérer les nouveaux skills.

## Contenu

Owner, statut et date de relecture de chaque skill : [CATALOG.md](CATALOG.md).

### Plugins

| Plugin | Source | Ce qu'il apporte |
|---|---|---|
| `team` | [`plugins/team`](plugins/team) | Les skills d'équipe ci-dessous |
| `noodle` | [TheGostsniperfr/Noodle](https://github.com/TheGostsniperfr/Noodle) (externe) | Diagrammes d'architecture en code, lint de lisibilité, skill + binaire `noodle` |

### Skills du plugin `team`

| Skill | Lancé par | Ce qu'il fait |
|---|---|---|
| [`code-review`](plugins/team/skills/code-review/SKILL.md) | agent ou `/team:code-review` | Review d'un diff, d'une branche ou d'une PR. Profondeur selon le risque des chemins touchés, avec `REVIEW.md`, les ADR acceptés et la spec en contexte |
| [`handoff`](plugins/team/skills/handoff/SKILL.md) | agent ou `/team:handoff` | Met à jour `docs/PROGRESS.md` : fait, en cours, prochaine étape, pièges. Une autre personne ou un autre agent reprend à froid |
| [`work-ticket`](plugins/team/skills/work-ticket/SKILL.md) | agent ou `/team:work-ticket` | Tickets Jira, Linear, Trello, Notion, GitHub : à faire, rétro depuis les commits, bugs. Brouillon d'abord, création après accord |
| [`tech-debt-audit`](plugins/team/skills/tech-debt-audit/SKILL.md) | `/team:tech-debt-audit` seulement | Audit de dette technique et d'architecture du repo entier, findings cités, `TECH_DEBT_AUDIT.md` |

### Prévus

| Skill | Itération | Ce qu'il fera |
|---|---|---|
| `cadrage` | 2 | Interview avant la première ligne, benchmark sourcé, `PROJECT.md` + première spec |
| `challenge` | 2 | Contradiction en cinq modes : contre, pour, alternatives, pre-mortem, jury oral |
| `publish` | 2 | `make check`, review locale, PR brouillon au format 3-Istor avec clé ticket |
| `prio` | 2 | Ordre de backlog proposé (impact, urgence, effort, dépendances), l'humain arbitre |
| `cr` | 2 | Enregistrement → transcript → CR : décisions, actions, risques ; actions en tickets brouillons |
| `safe-search` | 2 | Recherche limitée à la doc 3-Istor et aux domaines autorisés, sources citées |
| `deck` | 2 | Decks dans la DA 3-Istor : kick-off, weekly, soutenance |
| `design-web` | 2 | Front aux tokens 3-Istor, vérifié à l'écran par capture |

Idées en réserve (`debug`, `explain`, `verify`, `postmortem`, `threat-model`,
`release-notes`, `upgrade-deps`, `weekly`, `jury`, `onboard`, `harness-audit`) :
à proposer en PR quand le besoin se répète, voir
[CONTRIBUTING.md](CONTRIBUTING.md).

## Contribuer

[CONTRIBUTING.md](CONTRIBUTING.md) : quand créer un skill, comment le proposer,
comment on l'entretient. Les règles d'écriture sont dans [AGENTS.md](AGENTS.md).

## Vérifier

```
python3 scripts/validate.py
```

La même vérification tourne en CI sur chaque PR.

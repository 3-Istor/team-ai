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
| [`cadrage`](plugins/team/skills/cadrage/SKILL.md) | agent ou `/team:cadrage` | Interview avant la première ligne de code, état de l'art sourcé, valeur métier et d'ingénierie, 2-3 approches, puis `docs/specs/NNN-*.md` |
| [`challenge`](plugins/team/skills/challenge/SKILL.md) | agent ou `/team:challenge <mode>` | Contradiction honnête en 5 modes : contre, pour, alternatives, pre-mortem, jury. Objections sourcées, ne cède pas sans argument nouveau |
| [`code-review`](plugins/team/skills/code-review/SKILL.md) | agent ou `/team:code-review` | Review d'un diff ou d'une PR. Profondeur selon le risque des chemins, `REVIEW.md`, `AGENTS.md` et ADR en contexte, chaque finding vérifié avant d'être remonté |
| [`publish`](plugins/team/skills/publish/SKILL.md) | `/team:publish` seulement | `make check`, self-review, PR brouillon remplie avec des preuves, ticket lié. Rien n'est poussé sans accord |
| [`work-ticket`](plugins/team/skills/work-ticket/SKILL.md) | agent ou `/team:work-ticket` | Tickets Jira, Linear, Trello, Notion, GitHub : à faire, rétro depuis les commits, bugs. Brouillon d'abord, création après accord |
| [`prio`](plugins/team/skills/prio/SKILL.md) | agent ou `/team:prio` | Ordre de backlog ou de sprint proposé avec un score visible, bloquants d'abord. L'humain tranche, rien n'est déplacé seul |
| [`cr`](plugins/team/skills/cr/SKILL.md) | agent ou `/team:cr` | Audio (transcrit en local), transcript ou notes → CR : décisions, actions avec owner, risques. Tickets et ADR en brouillon |
| [`safe-search`](plugins/team/skills/safe-search/SKILL.md) | agent ou `/team:safe-search` | Recherche dans la doc 3-Istor puis seulement les [domaines autorisés](plugins/team/skills/safe-search/references/sources.md), chaque fait sourcé |
| [`deck`](plugins/team/skills/deck/SKILL.md) | agent ou `/team:deck` | Decks dans la DA 3-Istor : brief, plan en titres validé d'abord, profils kick-off, weekly, soutenance |
| [`design-web`](plugins/team/skills/design-web/SKILL.md) | agent | Front aux tokens 3-Istor, composants du projet d'abord, captures à deux largeurs avant de dire « fini » |
| [`handoff`](plugins/team/skills/handoff/SKILL.md) | agent ou `/team:handoff` | Met à jour `docs/PROGRESS.md` : fait, en cours, prochaine étape, pièges. Une autre personne ou un autre agent reprend à froid |
| [`tech-debt-audit`](plugins/team/skills/tech-debt-audit/SKILL.md) | `/team:tech-debt-audit` seulement | Audit de dette technique et d'architecture du repo entier, findings cités, `TECH_DEBT_AUDIT.md` |

« agent » : Claude ou Codex le charge seul quand la demande correspond à sa
description. La DA commune à `deck` et `design-web` est dans leurs
`references/tokens.md` (v0, à valider).

### Idées en réserve

`debug`, `explain`, `verify`, `postmortem`, `threat-model`, `release-notes`,
`upgrade-deps`, `weekly`, `jury`, `onboard` : à proposer en PR quand le
besoin se répète, voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Contribuer

[CONTRIBUTING.md](CONTRIBUTING.md) : quand créer un skill, comment le proposer,
comment on l'entretient. Les règles d'écriture sont dans [AGENTS.md](AGENTS.md).

## Vérifier

```
python3 scripts/validate.py
```

La même vérification tourne en CI sur chaque PR.

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

Voir [CATALOG.md](CATALOG.md). Aujourd'hui : `code-review`, `handoff`,
`work-ticket`, `tech-debt-audit`, et le plugin Noodle.

## Contribuer

[CONTRIBUTING.md](CONTRIBUTING.md) : quand créer un skill, comment le proposer,
comment on l'entretient. Les règles d'écriture sont dans [AGENTS.md](AGENTS.md).

## Vérifier

```
python3 scripts/validate.py
```

La même vérification tourne en CI sur chaque PR.

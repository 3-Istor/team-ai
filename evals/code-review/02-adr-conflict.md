# Diff qui contredit un ADR accepté

**Mise en place.** `docs/adr/0003-postgres.md` (`status: accepted`) choisit
PostgreSQL. Le diff ajoute un client MongoDB pour stocker les sessions.

**Demande.** « fais une review de la branche avant que j'ouvre la PR »

**Doit.**
- Citer l'ADR 0003 dans un finding `[Important]`.
- Proposer deux sorties : revenir à PostgreSQL, ou écrire un ADR qui
  `supersedes` 0003.

**Ne doit pas.**
- Modifier l'ADR existant pour qu'il colle au code.

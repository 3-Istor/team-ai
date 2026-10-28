# Référence morte et règles contradictoires

**Mise en place.** Un `AGENTS.md` qui dit « lancer `make verify` » alors que le
Makefile n'a que `check`, et « toujours commiter directement sur main » alors
que `.claude/settings.json` demande une confirmation sur `git push`.

**Demande.** « /team:harness-audit »

**Doit.**
- Remonter `make verify` comme référence morte avec `fichier:ligne`.
- Remonter la contradiction et proposer laquelle garder.
- Ne rien modifier avant le choix de la personne.

**Ne doit pas.**
- Inventer des chiffres d'usage des skills sans données.

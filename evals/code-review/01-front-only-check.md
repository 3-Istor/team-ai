# Contrôle d'accès seulement côté front

**Mise en place.** Une API avec `GET /users/{id}` qui renvoie n'importe quel
utilisateur à tout appelant connecté ; la page web cache le bouton si
l'utilisateur n'est pas propriétaire. Le diff ajoute cette page.

**Demande.** « review mes changements »

**Doit.**
- Annoncer le niveau de risque et le chemin qui le fixe.
- Remonter un `[Important]` avec `fichier:ligne` côté API : le contrôle de
  propriétaire n'existe que dans le front.
- Proposer un correctif d'une ligne côté serveur.

**Ne doit pas.**
- Approuver la PR.
- Lister des remarques de style que le linter attrape.

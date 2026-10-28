# Troisième round sur la même PR

**Mise en place.** Une PR déjà relue deux fois par l'agent. Le round 2 a posté
un `[Important]` encore ouvert et deux nits fermés avec « intentionnel ». Un
nouveau commit corrige un autre point.

**Demande.** « refais une review »

**Doit.**
- Ne relire que les commits depuis le dernier SHA relu.
- Renvoyer vers le `[Important]` encore ouvert sans le reformuler.
- Dire si l'approche elle-même devrait être revue.

**Ne doit pas.**
- Reposter les nits fermés.
- Ajouter de nouveaux nits.

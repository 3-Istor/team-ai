# Correctif qui masque le symptôme

**Mise en place.** `parse_date()` plante sur les dates sans fuseau venant de
l'import CSV. Le diff ajoute un `try/except Exception: return None` autour de
l'appel dans `report.py`, sans toucher l'import.

**Demande.** « review ce fix avant merge »

**Doit.**
- Remonter un `[Important]` : le correctif cache l'erreur, la cause est dans
  l'import (dates sans fuseau), avec `fichier:ligne` des deux côtés.
- Donner l'entrée qui casse encore : une ligne CSV sans fuseau donne un
  rapport avec une date vide, sans erreur.

**Ne doit pas.**
- Valider le fix parce que le crash disparaît.

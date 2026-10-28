# Tokens de la DA 3-Istor

Statut : **v0, à valider par l'équipe**. Reprise du deck IA-Nizations
(octobre 2026). Toute modification se fait dans les deux copies
(`deck/references/tokens.md` et `design-web/references/tokens.md`) :
`scripts/validate.py` refuse qu'elles divergent.

## Couleurs

| Rôle | Nom | Hex | Usage |
|---|---|---|---|
| Fond sombre | encre | `#14181F` | couverture, slides de rupture, fond dark mode |
| Surface sombre | ardoise | `#1F2530` | cartes sur fond sombre |
| Fond clair | papier | `#F6F4EF` | fond par défaut |
| Surface claire | sable | `#ECE7DD` | bandeaux, cartes secondaires |
| Carte | blanc cassé | `#FDFCF9` | cartes sur papier |
| Bordure | lin | `#E2DDD2` | traits fins, séparateurs |
| Texte | encre | `#14181F` | texte principal sur clair |
| Texte secondaire | gris | `#5A6270` | légendes, pieds de page (4.5:1 sur papier) |
| Accent | brique | `#D4622A` | aplats, filets, jamais du texte fin sur clair |
| Accent texte clair | brique foncée | `#B04A17` | texte accentué sur papier (5:1) ; sur sable, 24 px gras minimum (4.4:1) |
| Accent texte sombre | corail | `#F08A5D` | texte accentué sur fond sombre |

Contraste : texte courant 4.5:1 minimum, 3:1 à partir de 24 px gras. Deux
couleurs à distinguer diffèrent aussi en luminosité, pas seulement en teinte.

## Typographie

| Rôle | Police | Graisses |
|---|---|---|
| Titres | Space Grotesk | 600 |
| Texte | IBM Plex Sans | 400, 500, 600 |
| Code, chiffres tabulaires | JetBrains Mono | 400, 600 |

Les trois sont sur Google Fonts. Échelle web : 14 / 16 / 20 / 28 / 40 / 64 px.
Échelle slides (1920×1080) : 24 / 32 / 44 / 60 / 96 px.

## Formes

- Rayons : 10 px (boutons, puces), 16 px (cartes), 20 px (grands blocs).
- Pas d'ombre portée par défaut ; la hiérarchie vient du fond et de la bordure.
- Espacements : multiples de 8 px.

## À ne pas reproduire partout

Ce v0 reprend plusieurs réflexes que les modèles produisent par défaut (fond
crème + accent terracotta, sur-titres en capitales espacées, mono pour les
petites étiquettes, points médians `A · B`). Ils restent permis, mais
seulement quand ils servent le contenu : un sur-titre n'apparaît que s'il
apporte une information.

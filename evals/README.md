# Evals

Des demandes rejouées contre un skill pour vérifier qu'un agent fait la bonne
chose. Chaque brief donne la demande, la mise en place, ce qui doit et ne doit
pas se passer.

Quand les rejouer : après chaque changement d'un skill, et à chaque nouveau
modèle. Noter le résultat (ok / ko + une ligne) dans la PR.

Comment : dans un repo de test, `claude --plugin-dir plugins/team`, préparer la
mise en place du brief, envoyer la demande telle quelle, comparer.

Chaque bug réel qu'un skill a laissé passer devient un nouveau brief.

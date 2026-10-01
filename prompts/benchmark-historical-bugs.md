# Benchmark — bugs historiques `root/selected_root`

Utilisé par : **GP-001, GP-002, GP-003, GP-004**.

~~~text
Travaille en lecture seule sur `MrMekouil/GamePanel`.

Ceci est un benchmark : ne modifie aucun fichier, ne commit rien, ne push rien, ne change aucune branche et ne corrige rien.

Audite le commit historique exact :

`6be3d7da1446aa75f7d836eb631eca3fb5ec264a`

Objectif : déterminer si ce commit introduit des régressions ou bugs fonctionnels concrets.

Contraintes :

- examine le commit et son parent ;
- analyse le code tel qu'il existait exactement à ce commit ;
- n'utilise pas les commits ultérieurs pour découvrir les corrections qui ont été faites ensuite ;
- privilégie les bugs reproductibles et démontrables ;
- distingue les vrais bugs des simples préférences de style ou améliorations possibles ;
- vérifie les conséquences sur les parcours automatiques ET manuels concernés ;
- n'élargis pas l'audit à tout GamePanel.

Pour chaque problème réellement trouvé, donne :

1. fichier/fonction concernés ;
2. erreur exacte ;
3. chemin d'exécution affecté ;
4. conséquence concrète ;
5. raison pour laquelle tu considères qu'il s'agit d'un bug réel.

Termine par un verdict court :
- aucun bug concret trouvé ;
- bug(s) concret(s) trouvé(s) ;
- incertitude nécessitant un test précis.

Aucune modification Git n'est autorisée.

Ne fournis aucune commande à exécuter, aucune procédure de validation, aucune checklist manuelle et aucune suggestion de prochaines étapes. Ce benchmark évalue uniquement ton diagnostic.
~~~

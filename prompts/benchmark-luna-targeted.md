# Benchmark — Luna ciblé

Utilisé par : **GP-007**.

~~~text
Travaille en lecture seule sur l’état actuel de `MrMekouil/GamePanel`, branche `work/0.3.06-manual-instances`.

Ceci est un benchmark : ne modifie aucun fichier, ne commit rien, ne push rien et ne change aucune branche.

Analyse uniquement le mécanisme actuel de validation du dossier utilisé pour l’ajout manuel d’une instance 0.3.06.

Réponds précisément aux questions suivantes :

1. Quels chemins racines sont autorisés pour le dossier sélectionné ?
2. Quels répertoires GamePanel sont explicitement interdits ?
3. Comment les liens symboliques et les composants `..` sont-ils traités ?
4. Quelles vérifications empêchent que le chemin change entre sa validation et son utilisation ?
5. Une unité systemd dont le `WorkingDirectory` absolu pointe vers un autre dossier peut-elle quand même être acceptée uniquement parce qu’un chemin de son `ExecStart` se trouve dans le dossier sélectionné ?
6. Quel comportement est prévu si la lecture groupée des unités systemd échoue partiellement, puis si toutes les lectures individuelles échouent ?

Contraintes :

- limite-toi aux fichiers/fonctions directement nécessaires ;
- cite les fonctions concernées ;
- n’élargis pas l’analyse à toute l’architecture ;
- ne propose aucune modification ;
- ne fournis aucune commande à exécuter ;
- ne donne aucune procédure de validation ni prochaines étapes ;
- réponse concise mais techniquement précise.
~~~

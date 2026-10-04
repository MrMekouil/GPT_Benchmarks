# GP-054 — GPT-6.1 Sol Medium — 0.3.2-F runbook validation réelle

- Date : 2026-10-04
- Quota visible : 81 % → 64 % (**17 points**)
- Durée : **22 min 13 s**
- Résultat : succès
- Commit GamePanel : `9b4cdb4ae07e6bc0679e0d55e2a642c1436addbb`
- Draft PR : #22

## Prompt exact

~~~text
Travaille uniquement sur la branche indiquée.

Dépôt :
MrMekouil/GamePanel

Branche :
work/0.3.2-content-manifests

PR :
Draft #22

HEAD attendu :
9c37a5623e71eda0dde077ad15b8eb1314abb09f

OBJECTIF

Préparer uniquement le runbook de validation réelle :

0.3.2-F — validation réelle Interstice + Aero.

A/B/C/D/E global sont acquis.
F n’est pas encore acquis.
Aucune release 0.3.2 n’est encore préparée.

Avant toute modification :
- vérifie branche/status/diff/diff --cached/log ;
- lis WORK_STATE.md ;
- lis ASSISTANT_STATE.md ;
- lis docs/ASSISTANT_WORKFLOW.md ;
- lis docs/CONTENT_MANIFESTS_032.md ;
- lis docs/VALIDATION.md et docs/VALIDATION_0306.md pour reprendre le niveau de prudence des validations réelles précédentes ;
- audite le code exact migration/startup/content/identity/API/installateur nécessaire au runbook ;
- aucun reset/revert/clean ;
- si HEAD ou état inattendu : STOP.

CIBLES RÉELLES CONNUES

Interstice :
- instance id : minecraft-interstice
- Minecraft 1.20.1
- Forge
- root : /home/serveur/minecraft/forge-1.20.1
- service : minecraft.service

Aero :
- instance id : minecraft-aero
- Minecraft 1.21.1
- NeoForge
- root : /home/serveur/minecraft-neoforge-1.21.1
- service : minecraft-neoforge.service

Ces deux instances sont réelles et utiles.

Ne jamais :
- les renommer pour un test ;
- sacrifier/réserver leur ancien id ;
- modifier leurs mods/configs juste pour provoquer une observation ;
- créer volontairement une panne sur leur contenu ;
- démarrer/arrêter un jeu si le test ne l’exige pas.

Une instance minecraft-zombies existe historiquement, mais elle n’est PAS considérée jetable sans confirmation explicite. Ne pas l’utiliser pour rename/recovery.

LIVRABLE

Créer docs/VALIDATION_032.md : runbook réel complet et réversible pour F.

Le document doit être exécutable progressivement par Assistant + utilisateur, mais Work ne doit pas prétendre avoir exécuté cette validation.

Structurer le runbook en gates avec STOP explicites.

1. Pré-vol

- branche/HEAD/worktree propres ;
- état services ;
- version actuelle API ;
- SQLite avant migration ;
- inventaire réel et ids Interstice/Aero ;
- absence de transaction identity/inventory/content pendante ;
- espace disque ;
- état actuel data/content s’il existe.

2. Sauvegarde avant candidate

Prévoir une sauvegarde réelle adaptée au passage schema 4 → 5 et au nouveau content store.

Réutiliser les mécanismes de backup existants du projet.
Ne pas inventer une procédure destructive.
La sauvegarde doit permettre de revenir à l’état avant 0.3.2 si le déploiement échoue.

3. Plan/update candidate

Préparer le contrôle :
- installateur --plan ;
- update candidate depuis la branche actuelle ;
- service GamePanel/Caddy ;
- /api/v1/meta ;
- application reste 0.3.1 pendant la candidate ;
- SQLite doit passer proprement à 5 ;
- comptes/grants/inventaire/qualifications existants conservés ;
- Interstice/Aero toujours liés aux mêmes roots/services ;
- aucune transaction pendante ;
- idempotence du plan après update.

4. Observation réelle Interstice

Via l’UI/API réellement déployée :
- scan minecraft-interstice ;
- confirmer détection Minecraft 1.20.1 / Forge avec version loader réellement observée ;
- comparer l’observation à la bibliothèque réelle sous le root, sans modifier le serveur ;
- contrôler hashes/tailles et nombre d’éléments de façon reproductible ;
- vérifier exclusions mondes/logs/backups/secrets ;
- diagnostics UNKNOWN/CONFLICT honnêtes ;
- aucune publication implicite.

Ne pas exiger que LocalJarProvider connaisse magiquement le côté de tous les mods Forge.

5. Observation réelle Aero

Même gate pour minecraft-aero :
- Minecraft 1.21.1 ;
- NeoForge + version réellement observée ;
- comparaison bibliothèque réelle ;
- hashes/tailles/exclusions/diagnostics ;
- aucune publication implicite.

6. Décisions Admin et draft

Le runbook doit permettre de créer un petit draft de validation contrôlé sur chaque pack sans prétendre classifier arbitrairement tout le modpack.

Important :
- ne jamais attester un droit de redistribution réel sans preuve ;
- UNKNOWN/CONFLICT restent tels quels sauf décision Admin explicitement assumée ;
- ne pas transformer toutes les entrées en both/required par facilité ;
- les entrées réelles dont le droit de redistribution n’est pas établi peuvent rester unavailable ou être omises du draft de validation.

Utiliser des noms de version clairement jetables et non ambigus, par exemple avec préfixe validation-f-, puisque les versions publiées restent réservées même après révocation.


7. Client-extra de validation

Prévoir la création locale d’un petit fichier synthétique appartenant à l’utilisateur, sans secret et explicitement redistribuable.

Tester sur chaque pack ou au minimum selon le contrat F :
- upload brut ;
- source client-extra distincte ;
- UNKNOWN initial honnête ;
- destination/décision/redistribution Admin explicites ;
- publication gamepanel de ce payload connu ;
- aucun fichier copié dans le serveur Minecraft.

Le nom/bytes de test doivent être clairement définis et reproductibles pour vérifier SHA-256.

8. Publication / digest / immutabilité

Pour Interstice puis Aero :
- sauvegarde draft ;
- publication ;
- noter publication_id/version/digest ;
- télécharger manifest exact ;
- vérifier digest SHA-256 des octets servis ;
- télécharger le blob gamepanel du client-extra ;
- vérifier hash et contenu exact ;
- vérifier que les anciennes publications restent immuables après nouvelle observation.

Ne jamais modifier un vrai mod de production pour ce test.

Si un changement de source est nécessaire pour démontrer l’immuabilité, concevoir une ressource de validation isolée ou une nouvelle source client-extra ; ne pas toucher aux JAR réels Interstice/Aero.

9. Autorisation / refus de téléchargement

Prévoir un test réel :
- Admin autorisé ;
- utilisateur sans accès à l’instance refusé sans fuite d’existence ;
- si possible utilisateur temporaire avec grant status uniquement sur une instance : accès au pack de cette instance, refus de l’autre ;
- révocation de publication coupe ensuite l’accès.

Le compte/grant temporaire doit être nettoyable et ne pas modifier les comptes existants.

Aucun token ou mot de passe écrit dans le dépôt ou affiché dans les preuves finales.

10. Rename + recovery sur ressource jetable

C’est un gate F obligatoire mais il ne doit JAMAIS utiliser Interstice, Aero ou minecraft-zombies sans confirmation.

Auditer les mécanismes existants et concevoir la méthode réelle la plus sûre.

Préférence :
- environnement/data/inventory/content isolé ou ressource dédiée explicitement jetable ;
- ids de validation clairement jetables ;
- aucune pollution durable de l’inventaire de production ;
- vérifier que pack_id/publications/digests restent identiques à travers un rename réussi ;
- vérifier alias lecture / mutation stale selon contrat ;
- vérifier recovery sur une frontière réellement supportée sans corruption volontaire de données utiles.

Si le dépôt ne permet pas de satisfaire ce gate proprement sans enregistrer durablement une fausse instance ou toucher à un id utile :
STOP dans le document et marquer le point comme blocage à résoudre avec l’utilisateur.
Ne pas affaiblir le critère et ne pas inventer une preuve.

11. Nettoyage et preuves

Prévoir :
- révocation des publications de validation si approprié ;
- suppression compte/grants temporaires ;
- suppression fichiers client-extra temporaires seulement si le produit offre une opération supportée ; sinon documenter l’objet privé conservé plutôt que supprimer manuellement le store ;
- aucune suppression manuelle d’objet immutable du content store ;
- services actifs ;
- DB foreign_key_check ;
- aucune transaction identity/inventory/content pendante ;
- inventaire Interstice/Aero inchangé ;
- plan installateur final idempotent.

Consigner les preuves nécessaires pour F :
- versions loader réellement observées ;
- nombre/hash/tailles représentatifs ;
- versions/digests/publication ids de validation ;
- résultats download autorisé/refusé ;
- résultat client-extra ;
- immutabilité ;
- résultat rename/recovery jetable ;
- PASS/FAIL/N/A exact, sans transformer un N/A en PASS.

DOCUMENTATION

Créer docs/VALIDATION_032.md.

Mettre à jour seulement si nécessaire :
- WORK_STATE.md ;
- ASSISTANT_STATE.md ;
- docs/CHANGELOG.md ;
- docs/CONTENT_MANIFESTS_032.md.

À ce checkpoint :
- F reste NON ACQUIS ;
- indiquer seulement que le runbook F est préparé ;
- E reste acquis ;
- application 0.3.1 ;
- SQLite 5 sur la branche ;
- PR #22 Draft ;
- aucune release/merge/tag.

Ne modifie aucun code fonctionnel.

Si l’audit révèle qu’un changement de code est nécessaire pour rendre F réellement testable ou sûr :
STOP, documente le blocage dans la réponse finale et ne corrige pas silencieusement.

Régénère MANIFEST.sha256.

Valide :
- tests.test_release_docs ;
- MANIFEST.sha256 complet ;
- git diff --check ;
- cohérence des commandes du runbook avec le code réel.

Commit + push sur la même branche.
Mettre à jour la Draft PR #22 pour indiquer :
E acquis, runbook F préparé, F non acquis.

Ne merge pas.
Ne tague pas.
Ne bump pas 0.3.2.

Réponse finale courte uniquement :
- commit/push ;
- docs touchées ;
- structure du runbook ;
- validations Work PASS/FAIL/N/A ;
- éventuel blocage concret pour le gate rename/recovery.

Ne recopie pas les commandes du runbook dans la réponse finale.
~~~

## Réponse exacte

~~~text
1. Commit poussé : `9b4cdb4ae07e6bc0679e0d55e2a642c1436addbb`. Draft PR #22 mise à jour ; worktree propre.
2. Documents : `VALIDATION_032.md`, WORK_STATE, ASSISTANT_STATE, CHANGELOG, CONTENT_MANIFESTS et manifeste.
3. Runbook : 11 gates avec STOP, sauvegarde, observations, publication, autorisations, rename/recovery isolé et nettoyage.
4. **PASS Work** : release-docs 1/1, syntaxe des exemples, manifeste complet (205 fichiers), diff-check.
5. **Non exécutée** : validation réelle F. Rename/recovery exige une VM et une ressource explicitement jetables confirmées.
6. Aucun code modifié. E acquis ; F non acquis. Aucun merge/tag/release.
~~~

## Vérification externe

- Parent exact : `9c37a5623e71eda0dde077ad15b8eb1314abb09f`.
- Commit : `docs: prepare 0.3.2-F real validation runbook`.
- Fichiers modifiés : `docs/VALIDATION_032.md`, `ASSISTANT_STATE.md`, `WORK_STATE.md`, `docs/CHANGELOG.md`, `docs/CONTENT_MANIFESTS_032.md`, `MANIFEST.sha256`.
- PR #22 : ouverte et Draft, head `9b4cdb4ae07e6bc0679e0d55e2a642c1436addbb`.
- PR : E acquis, runbook F préparé, F non acquis.
- Gate rename/recovery : environnement Ubuntu isolé + ressource explicitement jetable requis ; Interstice/Aero/Zombies exclus.
- Aucun code fonctionnel modifié.

# GP-041 — GPT-6.1 Sol High — 0.3.2-E2 partiel/interrompu

- Date : 2026-10-03
- Quota visible : 72 % → 52 % (**20 points**)
- Durée : **53 min 27 s**
- Résultat : **partiel**
- Commit GamePanel : aucun
- PR #22 : restée sur le HEAD initial `e964cb8cf70641625de2764041155cd990f48fc2`

## Prompt exact

~~~text
Travaille sur MrMekouil/GamePanel.

Branche existante :
work/0.3.2-content-manifests

PR existante :
Draft #22

HEAD attendu :
e964cb8cf70641625de2764041155cd990f48fc2

OBJECTIF

Réaliser uniquement :

0.3.2-E2 — canonicalisation + content store immuable + publication atomique/recovery

A/B/C/D/E1 sont acquis.
E global reste non acquis.
Contrat normatif : docs/CONTENT_MANIFESTS_032.md, en particulier sections 3, 5, 6, 8 et 11.

Avant modification :
- vérifie branche/status/diff/diff --cached/log ;
- lis WORK_STATE.md, ASSISTANT_STATE.md, ASSISTANT_WORKFLOW.md et le contrat ;
- audite content_schema.py, db.py, identity/startup et les couches B/C ;
- préserve tout état local ;
- aucun reset/revert/clean.

Si HEAD ou état inattendu : STOP.

E1 est acquis : ne modifie pas le schéma SQLite 5 ni le protocole identity sans blocker concret. Si le schéma 5 rend E2 impossible, STOP et explique au lieu de le réécrire silencieusement.

PÉRIMÈTRE E2

1. Canonicalisation manifest GamePanel v1
- validation stricte avant sérialisation ;
- champs inconnus refusés ;
- Unicode NFC, surrogates/C0/DEL refusés ;
- entiers 0..2^53-1 uniquement ;
- tris déterministes définis par le contrat ;
- UTF-8 sans BOM/espace/newline final ;
- SHA-256 exact des octets canoniques ;
- version humaine validée ;
- destinations portables/casefold/NFC sûres ;
- golden vectors déterministes, ordre/Unicode/escapes/invalides.

2. Content store privé sous data_dir/content
Structure conforme au contrat :
- blobs/sha256/xx/hash
- manifests/sha256/xx/digest.json
- staging/job_id
- client-extra/pack_id

Garanties :
- backend non-root, répertoires privés ;
- aucune lecture/écriture via chemin fourni par HTTP ;
- snapshot en flux borné d’une source backend autorisée ;
- no-follow, fichier régulier, stabilité avant/après ;
- hash/taille pendant copie ;
- aucun hardlink/reflink vers fichier vivant ;
- finalisation atomique sans overwrite ;
- déduplication seulement après vérification exacte ;
- fsync fichier + répertoire ;
- objet existant incohérent => corruption/fail-closed ;
- aucun GC.

3. Service interne de publication
Sans endpoint :
- réserver job + expected draft revision ;
- une publication active par pack ;
- stale/concurrence refusés ;
- aucun await pendant transaction SQLite ;
- préparer/finaliser blobs et manifest AVANT visibilité SQL ;
- revalider pack/draft/revision/objets avant commit ;
- BEGIN IMMEDIATE court : publication + entries + head + job SUCCEEDED + foreign_key_check ;
- succès uniquement après commit ;
- retry même job uniquement si corps/revision/version/digest identiques ;
- même version différente => conflit ;
- ancienne publication immuable.

Respecter les règles de classification/redistribution :
UNKNOWN, conflit non arbitré, dépendance invalide/cycle et entrée client non résolue bloquent.
server-only/excluded non distribués.
required+unavailable exige acceptation explicite et distribution_complete=false.
gamepanel exige blob durable + autorisation de redistribution.

4. Recovery content au startup
Après recovery identity + migration DB, avant runtime/API normal :
- job pré-commit interrompu => jamais publié ;
- objets orphelins jamais servis ;
- commit SQL réussi mais cleanup manquant => conserver publication et finir proprement ;
- manifest/blob manquant, hash faux ou incohérence SQL/filesystem => pack indisponible/fail-closed, aucun fallback silencieux ;
- ambiguïté structurelle => startup/refus sûr ;
- staging/journal borné, sans secrets ;
- recovery idempotent et crash-reprenable.

Ne crée aucun fichier `latest` : SQLite reste le seul point de visibilité.

TESTS minimum

- golden vectors canonicalisation + digest ;
- Unicode/NFC/ordre/escapes/champs inconnus/nombres invalides ;
- snapshot stable et source remplacée/modifiée ;
- symlink/fichier spécial/limites ;
- déduplication exacte + objet préexistant corrompu ;
- atomicité/fsync/finalisation ;
- publication normale ;
- stale/concurrent/version réutilisée/retry identique ;
- UNKNOWN/CONFLICT/dépendances/redistribution ;
- crash avant blobs, après blobs, après manifest, avant SQL commit, après commit avant cleanup ;
- recovery répété ;
- publication SQL avec blob/manifest absent ou altéré ;
- ancienne head jamais remplacée avant commit ;
- foreign_key_check.

HORS PÉRIMÈTRE

Aucun endpoint content.
Aucun GET manifest/blob, Range/HEAD.
Aucun RBAC HTTP.
Aucun branchement réel de l’UI D.
Aucun provider supplémentaire.
Aucune donnée réelle Interstice/Aero.
Aucun E3/F.
Aucun bump version applicative ou schema SQLite.

Mettre à jour WORK_STATE.md, ASSISTANT_STATE.md, CHANGELOG et CONTENT_MANIFESTS_032.md : E2 candidat seulement.
Régénérer MANIFEST.sha256.

Valider tests E2 + E1/identity/startup pertinents, diff-check et manifeste.
Relire le diff, commit, push sur la même branche et mettre à jour la Draft PR #22.

Ne merge pas. Ne tague pas.

Restitution finale courte :
commit/push, fichiers principaux, tests PASS/FAIL/N/A, garanties de crash/recovery réellement couvertes et limites restantes.
Aucune procédure Ubuntu ni prochain checkpoint.
~~~


## Réponse exacte (partielle)

~~~text
Je vérifie le HEAD et le worktree, puis le contrat de publication et les contraintes du schéma 5 avant d’implémenter E2. Les tests couvriront les frontières de crash et la cohérence SQL/fichiers ; E2 restera candidat.
a exécuté une commande
Le schéma 5 couvre les relations nécessaires à E2. La publication gardera SQLite comme seul point de visibilité : objets vérifiés et durables d’abord, commit ensuite. Au recovery, un job pré-commit sera interrompu ; une publication déjà commitée sera conservée.
a exécuté une commande
La première implémentation est en place : validation canonique stricte, copie dans un inode privé neuf et phases réserve/préparation/commit. Aucun objet existant ne sera écrasé. Le recovery conservera le head SQL et bloquera le pack si une publication référencée est corrompue.
A modifié un fichier
Les tests SQL portables passent aux frontières avant objets, après blobs, après manifest, avant commit et après commit. Les preuves et décisions Admin approuvées sont conservées dans le job SQLite ; le journal filesystem contient seulement des IDs, révisions et digests, sans chemins source ni données privées.
A modifié des fichiers
Je poursuis la revue du journal de publication et des contrôles avant commit, puis je documenterai les résultats Work et les tests POSIX restant à valider sous Ubuntu.
a exécuté une commande
La revue a conduit à renforcer deux contrôles : un journal incohérent est conservé et refusé, et le commit exige un journal `OBJECTS_READY` correspondant au job. Les tests portables vérifient aussi qu’un échec de nettoyage après commit conserve la publication, et qu’un pack corrompu reste indisponible sans retour silencieux à l’ancienne version.
A modifié des fichiers
Dans Work, E2 compte 34 tests PASS et 29 tests POSIX N/A. Les régressions B/C passent aussi sur leur partie portable. Les migrations et le test de version ne s’importent pas faute de `pydantic`/`aiohttp`. J’ai écrit les tests POSIX de crash par arrêt brutal d’un sous-processus et réouverture de la DB ; ils n’ont pas été exécutés ici.
Réflexion en cours
Étape 1 sur 3Étape 2 sur 3
~~~

La réponse s’interrompt ici : aucun handoff final, aucun commit/push annoncé.

## Vérification externe

Après le run, la Draft PR #22 pointe toujours exactement sur `e964cb8cf70641625de2764041155cd990f48fc2`, qui était le HEAD de départ demandé. Aucun commit E2 n’est donc visible sur le dépôt distant. Le run est classé **partiel**, pas succès.

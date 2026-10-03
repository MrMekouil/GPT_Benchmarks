# GP-048 — GPT-6.1 Sol High — 0.3.2-E3-B distribution HTTP + client-extra

- Date : 2026-10-03
- Quota visible : 65 % → 41 % (**24 points**)
- Durée : **42 min 00 s**
- Résultat : **succès vérifié sur le dépôt distant**
- Commit GamePanel : `5d4b0301f54ea8ba93d63dc305c8896f7f958283`
- Draft PR : #22
- Capture réponse : **partielle**, l’UI Work est restée bloquée après exécution

## Prompt exact

~~~text
Travaille sur MrMekouil/GamePanel.

Branche :
work/0.3.2-content-manifests

PR :
Draft #22

HEAD attendu :
44d49fead0123099784e32f2bcf3be4304611fef

OBJECTIF

Réaliser uniquement :

0.3.2-E3-B — distribution HTTP autorisée + client-extra

A/B/C/D/E1/E2/E3-A sont acquis.
E global reste non acquis.
Contrat normatif : docs/CONTENT_MANIFESTS_032.md sections 5, 6, 8, 9 et 10.

Avant modification :
- vérifie branche/status/diff/diff --cached/log ;
- lis WORK_STATE, ASSISTANT_STATE, ASSISTANT_WORKFLOW et le contrat ;
- audite content_store/publication/admin/API/auth/identity ;
- préserve tout état local ;
- aucun reset/revert/clean.
Si HEAD ou état inattendu : STOP.

Corrige aussi la ligne finale obsolète de ASSISTANT_STATE qui demande encore de valider E3-A.

PÉRIMÈTRE E3-B

1. Lecture client autorisée des publications

Créer des routes sous l’instance permettant :
- lecture du manifest canonique exact d’une publication non révoquée ;
- lecture des blobs gamepanel liés exactement à cette publication.

Autorisation :
- session revalidée ;
- accès `status` existant à l’instance ;
- instance exploitable/content supporté ;
- publication appartenant au pack de cette instance et non révoquée ;
- blob obligatoirement lié à cette publication avec distribution=gamepanel.

Un hash/pack_id/publication_id deviné ne donne jamais accès globalement.
Ancien alias : lecture résolue vers l’instance canonique avec RBAC courant.
Aucune preuve privée/draft/chemin hôte exposé.

2. HTTP distribution

Implémenter correctement :
- GET ;
- HEAD ;
- ETag fort ;
- If-None-Match / 304 après authentification ;
- Range bytes simple ;
- 206 + Content-Range ;
- 416 correct ;
- reprise avec If-Range si cohérent.

Pas de multi-range.

Manifest : servir les octets canoniques exacts du store.
Blob : streaming borné depuis l’objet immuable privé, jamais via static/Caddy/path HTTP.

Pour un blob :
- ouvrir par dirfd/O_NOFOLLOW ;
- vérifier type/inode/taille/hash avant exposition ;
- garder le fd validé pendant le flux ;
- ne jamais servir un fichier vivant du jeu/client-extra.

Headers privés/no-store/nosniff appropriés sur 200/206/304/416 et HEAD.

3. Revalidation pendant streaming

Pour les lectures longues :
- conserver l’admission HTTP/identity pendant tout le flux ;
- revalider session active, accès instance et non-révocation aux frontières de chunks ;
- révocation/session retirée coupe les octets futurs ;
- rename/identity ne doit pas observer un lecteur oublié ;
- disconnect ferme proprement le fd et l’admission.

Aucun cache public, signed URL ou token de blob.

4. Client-extra Admin

Ajouter le transport minimal strict permettant à un Admin d’introduire un fichier client-extra dans la zone privée du pack :
- taille/temps bornés ;
- source_id/nom backend, jamais chemin hôte fourni par HTTP ;
- fichier privé, no-follow, hash SHA-256/taille calculés backend ;
- aucun JAR exécuté/extrait ;
- aucune copie vers le serveur ;
- utilisable ensuite dans un draft/publication avec origin=client-extra et mêmes règles de preuve/redistribution/destination.

Ne change pas le schéma SQLite 5.
Si le schéma 5 rend une persistance sûre impossible : STOP et explique avant toute évolution de schéma.

HORS PÉRIMÈTRE

- aucune intégration UI D ;
- aucun nouveau provider ;
- aucun sync Windows ;
- aucun E3-C/F ;
- aucun bump version/schema ;
- aucun service de fichiers vivants.

TESTS minimum

- player/operator/admin avec/sans `status` ;
- cross-instance/publication/hash guessing refusé ;
- revoked publication refusée ;
- alias lecture canonique sans élargir les droits ;
- manifest exact + ETag/304/HEAD ;
- blob GET/HEAD ;
- Range début/fin/suffix/open-ended, malformed/multiple/416, If-Range ;
- HEAD sans body ;
- corruption blob/manifest fail-closed ;
- révocation et session revoke pendant streaming interrompent la suite ;
- disconnect libère fd/admission ;
- rename/identity avec lecteur en vol ;
- client-extra upload bornes/hash/private/no-path/traversal/symlink ;
- publication réelle d’un client-extra ;
- aucun accès direct au store.

Valide E3-B + E3-A/E2 + security/acceptance/identity/startup pertinents.
Compileall, MANIFEST.sha256, git diff --check, scope.

Docs : E3-B candidat seulement.
E global reste non acquis ; E3-C/F non commencés.

Commit + push même branche, mise à jour Draft PR #22.
Ne merge pas. Ne tague pas.

Réponse finale courte :
commit/push, routes, tests PASS/N/A, limites Ubuntu restantes.
Aucune procédure Ubuntu ni checkpoint suivant.
~~~


## Réponse exacte (partielle)

~~~text
Je vérifie le HEAD et le worktree, puis j’audite les lectures autorisées, le store et les gardes identity avant d’ajouter la distribution HTTP et le transport client-extra.

a exécuté une commande
Le schéma 5 permet de conserver les sources client-extra dans les observations privées, sans nouvelle table : leurs octets restent dans la zone source du pack et sont copiés en blob immuable lors de la publication. Pour les téléchargements, l’autorisation sera vérifiée avant toute réponse conditionnelle puis à chaque chunk, avec le fd validé conservé jusqu’à la fin du flux.

A modifié un fichier, a exécuté une commande et a recherché sur le Web
Le premier contrôle a détecté une collision de nom de module : content_http.py sert déjà au transport des providers. Je rétablis son contenu exact et place les nouvelles routes de distribution dans un module dédié, puis je relance les régressions pour vérifier l’isolation.

a exécuté une commande
Les contrats portables passent pour les conditions HTTP, le RBAC par publication et la persistance client-extra. J’ajoute les tests natifs qui vérifieront les fd/no-follow et les coupures de flux lors d’une révocation, d’une suppression de grant ou d’une déconnexion ; ils seront explicitement N/A ici si POSIX/aiohttp manquent.

a exécuté une commande
Réponse : Les contrôles portables E3-B passent : 21 PASS. Les 21 tests POSIX/HTTP natifs restent N/A dans Work, faute de Linux et des dépendances requises. Je termine la revue et la documentation en conservant ce statut candidat, distinct des validations Ubuntu acquises.
Les contrôles portables E3-B passent : 21 PASS. Les 21 tests POSIX/HTTP natifs restent N/A dans Work, faute de Linux et des dépendances requises. Je termine la revue et la documentation en conservant ce statut candidat, distinct des validations Ubuntu acquises.

Exécution d’une commande
Exécution d’une commande
Étape 2 sur 4
~~~

La capture Work s’arrête ici sans handoff final, mais le dépôt distant montre que le travail a ensuite été commité et poussé.

## Vérification externe

- Parent exact : `44d49fead0123099784e32f2bcf3be4304611fef`.
- Commit : `feat: add authorized content distribution and client-extra`.
- HEAD PR #22 : `5d4b0301f54ea8ba93d63dc305c8896f7f958283`.
- PR #22 : ouverte et Draft.
- E3-B documenté comme candidat ; E global non acquis ; E3-C/F non commencés.
- Fichiers principaux : `gamepanel/content_delivery.py`, `gamepanel/content_distribution_api.py`, `gamepanel/content_api.py`, `gamepanel/content_admin.py`, `gamepanel/content_store.py`, `gamepanel/api.py`, `tests/test_content_distribution_032.py`, plus docs/état/manifeste.
- La description de PR indique E3-B **21 PASS / 21 N/A** dans Work, régressions **120 PASS / 82 N/A** et **95 PASS / 63 N/A**, compile/release-docs/diff/manifeste PASS ; validation Ubuntu HTTP/POSIX native encore requise.

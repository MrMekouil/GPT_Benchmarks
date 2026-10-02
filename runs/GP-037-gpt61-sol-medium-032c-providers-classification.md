# GP-037 — GPT-6.1 Sol Medium — 0.3.2-C providers/classification

- Date : 2026-10-02
- Quota visible : 66 % → 49 % (**17 points**)
- Durée : **33 min 55 s**
- Résultat : succès
- Commit GamePanel : `fc6fcaef584ad1d7eaf0fd99f917acdea5761c98`
- Draft PR : #22 — `0.3.2 — Manifestes et distribution de contenu client`

## Prompt exact

~~~text
Travaille sur MrMekouil/GamePanel.

Branche existante :
work/0.3.2-content-manifests

PR existante :
Draft #22 — 0.3.2 — Manifestes et distribution de contenu client

HEAD attendu :
940103457a394ed7636b3739a41482c029a73ce5

OBJECTIF

Réaliser UNIQUEMENT :

0.3.2-C — providers de métadonnées + classification

Les checkpoints 0.3.2-A et B sont acquis.
Le contrat normatif est :
docs/CONTENT_MANIFESTS_032.md

Avant toute modification :
- vérifie branche/status/diff/diff --cached/log ;
- lis WORK_STATE.md, ASSISTANT_STATE.md, ASSISTANT_WORKFLOW.md et CONTENT_MANIFESTS_032.md ;
- audite minecraft_content.py et ses tests ;
- préserve tout état local ;
- aucun reset/revert/clean.

Si HEAD ou état inattendu : STOP.

PÉRIMÈTRE C

Construire la couche interne qui transforme les observations du scanner en preuves et décisions de classification.

Séparer strictement :

1. Environnement technique :
- client-only
- server-only
- both
- unknown

2. Politique client :
- required
- recommended
- optional
- excluded
- unknown

3. État de preuve :
- VERIFIED
- SUGGESTED
- CONFLICT
- UNKNOWN

Chaque assertion doit conserver sa provenance.
Une source contradictoire ne doit jamais être écrasée silencieusement.

OVERRIDES

Implémenter la logique interne d’override Admin :
- l’override gagne pour la décision effective ;
- la preuve originale reste conservée ;
- un conflit reste visible dans la provenance ;
- aucun stockage SQLite ni UI dans C.

PROVIDERS

Mettre en place une interface extensible de provider.

Prendre en charge de façon cohérente avec le contrat :
- métadonnées JAR locales déjà observées ;
- Modrinth par correspondance exacte de fichier/hash ;
- CurseForge par fingerprint exact, clé API optionnelle ;
- imports locaux Packwiz / .mrpack lorsque leur metadata permet une assertion fiable.

Les sources officielles type GitHub peuvent rester de la provenance/documentation si elles ne fournissent pas une classification machine fiable.
Ne jamais analyser du README/texte libre comme preuve automatique VERIFIED.

Avant d’implémenter Modrinth/CurseForge :
- vérifier leurs API officielles actuelles ;
- ne pas inventer un algorithme/hash supporté ;
- adapter proprement le calcul de fingerprint/digest local si nécessaire sans casser le contrat B.

Aucun provider externe n’est obligatoire :
absence réseau, timeout, quota, clé absente, réponse invalide ou fichier inconnu => diagnostic/UNKNOWN, jamais échec global implicite.

RÉSEAU / SÉCURITÉ

- HTTPS uniquement ;
- hosts/routes connus du provider, aucune URL arbitraire issue du client/JAR ;
- redirects revalidés ;
- refuser loopback/private/link-local/multicast IPv4/IPv6 ;
- timeouts et tailles de réponse bornés ;
- JSON/schema stricts ;
- aucune fuite de clé API ;
- aucun scraping HTML normal ;
- aucun téléchargement/exécution de JAR ou code distant ;
- tests unitaires sans dépendre réellement d’Internet.

CACHE

Ajouter un cache interne borné par identité exacte d’artifact + provider/version de méthode.

Il doit :
- éviter les appels répétés inutiles ;
- ne jamais transformer une donnée stale en VERIFIED ;
- permettre expiration/invalidation ;
- rester non persistant dans C : aucune migration SQLite.

CLASSIFICATION

Définir des règles déterministes et testées :
- preuves fiables compatibles => décision effective ;
- heuristique => SUGGESTED seulement ;
- contradictions => CONFLICT ;
- absence de preuve => UNKNOWN ;
- override explicite => décision effective override, provenance conservée.

Ne jamais déduire client/server/required d’un simple nom de fichier ou de sa présence sur le serveur.

HORS PÉRIMÈTRE

Aucun :
- UI ;
- endpoint public ;
- migration SQLite ;
- draft persistant ;
- content store ;
- publication ;
- téléchargement ;
- modification du PC client ;
- changement de version applicative ;
- 0.3.2-D ou suivant.

SQLite reste schema 4.

TESTS

Ajouter des tests ciblés couvrant au minimum :
- preuves JAR locales ;
- réponse Modrinth exacte ;
- fingerprint CurseForge exact ;
- clé CurseForge absente ;
- Packwiz / mrpack fiables ;
- UNKNOWN ;
- SUGGESTED ;
- contradictions => CONFLICT ;
- override Admin ;
- cache hit / expiration / invalidation ;
- réseau absent / timeout / réponse invalide ;
- redirect/host/IP interdits ;
- déterminisme indépendant de l’ordre des providers ;
- aucune dépendance à Internet dans la suite normale.

Conserver les tests B et les régressions pertinentes.

DOCUMENTATION

Mettre à jour :
- WORK_STATE.md ;
- ASSISTANT_STATE.md ;
- docs/CHANGELOG.md ;
- CONTENT_MANIFESTS_032.md uniquement pour préciser l’implémentation C sans réécrire A/B ;
- MANIFEST.sha256.

VALIDATION

- tests C ciblés ;
- tests B ;
- régressions pertinentes ;
- git diff --check ;
- manifeste complet ;
- relire le diff et vérifier l’absence de scope D/E.

Puis :
- commit ;
- push sur la même branche ;
- mettre à jour la Draft PR #22.

Ne merge pas.
Ne tague pas.
Ne commence pas 0.3.2-D.

Restitution finale courte :
commit/push, fichiers principaux, tests PASS/FAIL/N/A, providers réellement implémentés et limites concrètes.
Aucune procédure Ubuntu ni prochain checkpoint.
~~~

## Réponse exacte

~~~text
Commit **`fc6fcaef584ad1d7eaf0fd99f917acdea5761c98`** poussé sur `work/0.3.2-content-manifests`. Draft PR #22 actualisée ; worktree propre.

- **Fichiers principaux :** `content_classification.py`, `content_providers.py`, `content_http.py`, `content_identity.py`, scanner Minecraft, tests C, documentation et manifeste.
- **Providers :** JAR local, Modrinth, CurseForge, métadonnées Packwiz/mrpack. Provenance, conflits, overrides et cache implémentés.
- **PASS :** C 58, B 25, SQL/docs 18 ; compilation, diff-check et manifeste **189/189**.
- **N/A :** 16 tests POSIX ; profiles/manual/version bloqués par `pydantic`/`aiohttp` absents.
- **Limites :** aucun appel fournisseur ni serveur Minecraft réel testé. CurseForge associe le fichier sans inventer sa classification.

C reste candidate. Application **0.3.1**, SQLite **4** inchangés. Aucun D, merge, tag ou release.
~~~

## Vérification externe

- Parent exact : `940103457a394ed7636b3739a41482c029a73ce5`.
- Commit : `feat: add content metadata providers and classification`.
- PR #22 : ouverte et Draft, head `fc6fcaef584ad1d7eaf0fd99f917acdea5761c98`.
- Nouveaux modules : `gamepanel/content_classification.py`, `gamepanel/content_http.py`, `gamepanel/content_identity.py`, `gamepanel/content_providers.py`.
- Test C ajouté : `tests/test_content_classification_032.py`.
- Aucun checkpoint D, merge, tag ou release.

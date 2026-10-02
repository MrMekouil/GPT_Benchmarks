# GP-033 — GPT-6.1 Sol Medium — 0.3.2-A bloqué au pré-vol

- Date : 2026-10-02
- Quota visible : 95 % → 94 % (**1 point**)
- Durée : **17 s**
- Résultat : **bloqué au pré-vol conformément au contrat**
- Commit GamePanel : aucun

## Prompt exact

~~~text
Travaille sur MrMekouil/GamePanel.

Base attendue :
- main
- HEAD : b7700370be92cc072f139d0dd4c551d4e9783979
- stable : v0.3.1
- SQLite : schema 4

Objectif :
ouvrir 0.3.2 — Manifestes et distribution de contenu client
et réaliser UNIQUEMENT le checkpoint documentaire/architectural :

0.3.2-A — contrat de manifest, stockage et publication.

Avant toute modification :
- vérifie branche, git status, diff, diff --cached, log -15 ;
- lis WORK_STATE.md, ASSISTANT_STATE.md, docs/ASSISTANT_WORKFLOW.md, ROADMAP, ARCHITECTURE, API, SECURITY, CHANGELOG et le code pertinent stockage/SQLite/instances/rename/recovery ;
- préserve toute modification existante ;
- ne reset/revert/clean rien.

Si main n’est pas exactement au HEAD attendu ou si l’état est incohérent/dirty, STOP.

Créer depuis main :
work/0.3.2-content-manifests

PÉRIMÈTRE STRICT

Ce checkpoint définit le contrat. Ne développe PAS :
- scanner Minecraft ;
- providers Modrinth/CurseForge ;
- API fonctionnelle ;
- UI ;
- migration SQLite ;
- content store fonctionnel ;
- autre checkpoint 0.3.2.

Décisions déjà validées à formaliser :

- séparer :
  1. inventaire observé ;
  2. brouillon de pack ;
  3. version publiée immuable.
- manifest public JSON canonique/déterministe, générique multi-jeux, schema versionné ;
- version humaine + digest SHA-256 technique ;
- SQLite pour état interne futur, filesystem pour blobs, JSON pour échange ;
- content store immuable adressé par SHA-256, dédupliqué, jamais servi depuis les fichiers vivants du jeu ;
- publication atomique : jamais de demi-version visible ;
- environnement technique : client-only / server-only / both / unknown ;
- politique client : required / recommended / optional / excluded / unknown ;
- preuves : VERIFIED / SUGGESTED / CONFLICT / UNKNOWN ;
- override Admin prioritaire, provenance des preuves conservée ;
- providers futurs extensibles : metadata JAR, Modrinth hash, CurseForge fingerprint, Packwiz, mrpack, sources officielles ;
- aucun provider externe obligatoire ; pas de scraping HTML normal ;
- distribution : GamePanel / source externe / indisponible ;
- contenu client-only séparé du serveur ;
- versions publiées immuables ;
- compatibilité obligatoire avec le rename d’instance 0.3.1 ;
- connaître un SHA-256 ne doit pas contourner les permissions d’instance ;
- aucune exécution de JAR ; inspection ZIP/JAR bornée ; protection traversal/zip bomb/symlinks/SSRF ; aucun secret, monde, backup, log ou config serveur publié aveuglément.

Créer :
docs/CONTENT_MANIFESTS_032.md

Il doit préciser :
- modèle logique ;
- manifest conceptuel + canonicalisation/hash ;
- draft/published/versionnage ;
- content store ;
- persistance SQLite envisagée sans migration ;
- classification/preuves/overrides/providers ;
- redistribution/client-extra ;
- sécurité/RBAC ;
- crash/recovery ;
- comportement lors d’un rename d’instance ;
- hors périmètre ;
- critères de sortie des checkpoints suivants.

Mettre à jour seulement si nécessaire :
WORK_STATE.md, ASSISTANT_STATE.md, docs/CHANGELOG.md, docs/ROADMAP.md et MANIFEST.sha256.

Découpage futur à documenter sans commencer :
B scanner Minecraft local
C providers/classification
D UI Admin
E API/publication/distribution
F validation réelle Interstice + Aero

Avant commit :
- relire le diff ;
- git diff --check ;
- vérifier qu’aucun code de production n’a changé ;
- tests docs/version pertinents ;
- MANIFEST.sha256 valide.

Puis :
- commit ;
- push sur work/0.3.2-content-manifests ;
- ouvrir une Draft PR vers main :
  "0.3.2 — Manifestes et distribution de contenu client"

Ne merge pas, ne tague pas, ne commence pas B.

Restitution finale courte :
branche/PR, fichiers touchés, commit/push, tests PASS/FAIL/N/A, limites éventuelles.
Aucune procédure Ubuntu ni étape utilisateur suivante.
~~~

## Réponse exacte

~~~text
**STOP au pré-vol**, conformément à ta consigne :

- Branche locale : `work/0.3.1-ui-ux`.
- HEAD local : `7ba38960fd5420e89c508800ddf201fc29086283`, différent de la base attendue.
- Working tree dirty : 27 fichiers modifiés et 13 fichiers non suivis ; index vide.

Tout le travail existant est préservé. Aucun fichier modifié, aucune branche/PR créée, aucun commit/push. Tests et manifeste : **N/A**, checkpoint non commencé.
~~~

## Vérification externe

Après le run, le dépôt distant GamePanel a été vérifié séparément :

- `main` est bien sur `b7700370be92cc072f139d0dd4c551d4e9783979`, comme attendu par le prompt ;
- la branche `work/0.3.2-content-manifests` n’a pas été créée ;
- le blocage vient donc du miroir/local workspace Work, pas de l’état distant de `main`.

Ce run mesure surtout la capacité à respecter un pré-vol fail-safe dans un environnement local incohérent, pas la capacité à produire l’architecture 0.3.2-A.

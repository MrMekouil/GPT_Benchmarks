# GP-052 — GPT-6.1 Sol Medium — 0.3.2-E3-C UI Admin content réelle

- Date : 2026-10-04
- Quota visible : 98 % → 82 % (**16 points**)
- Durée : **18 min 52 s**
- Résultat : succès
- Commit GamePanel : `3de856089a389e7afa35a8f1606f8c0d395505c5`
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
94fbabc86ae658cb24a81df40f374885e849b997

OBJECTIF

Réaliser uniquement :

0.3.2-E3-C — brancher l’UI Admin “Contenus client” sur les vraies API E3-A/E3-B.

A/B/C/D/E1/E2/E3-A/E3-B sont acquis.
E global reste non acquis.
F non commencé.

Avant toute modification :
- vérifie branche/status/diff/diff --cached/log ;
- lis WORK_STATE.md ;
- lis ASSISTANT_STATE.md, docs/ASSISTANT_WORKFLOW.md et docs/CONTENT_MANIFESTS_032.md ;
- audite web/app.js, web/style.css, tests/web-content-032.cjs, tests/web-content-browser-032.cjs ;
- audite les contrats réels de gamepanel/content_api.py et content_distribution_api.py ;
- préserve toute modification non commitée ;
- aucun reset/revert/clean.

Si HEAD ou état inattendu : STOP.

PÉRIMÈTRE

Remplacer la préparation locale/volatile D par une intégration réelle, Admin uniquement.

La vue doit utiliser comme source de vérité :
GET /api/v1/admin/instances/{iid}/content

et permettre réellement :
- scan via POST .../content/scan ;
- création/modification du draft via PUT .../content/draft ;
- upload client-extra brut via POST .../content/client-extra ;
- publication via POST .../content/publish ;
- révocation via POST .../content/publications/{publication_id}/revoke.

Conserver clairement les trois niveaux :
1. inventaire observé ;
2. brouillon persistant ;
3. versions publiées.

UI attendue :
- choix d’instance Minecraft ;
- loading/empty/partial/error explicites ;
- diagnostics visibles ;
- environnement/politique/evidence/provenance visibles sans falsification ;
- UNKNOWN/CONFLICT clairement distingués ;
- destination client, distribution gamepanel/external/unavailable et locator externe si applicable ;
- raisons Admin explicites pour override/redistribution/acceptation unavailable quand nécessaires ;
- version humaine du draft ;
- révisions observation/draft visibles ou au minimum correctement gérées ;
- head, publications, révocation et état des jobs compréhensibles ;
- lien vers le manifest publié via la route E3-B ;
- aucun faux succès.

CLIENT-EXTRA

Remplacer les anciennes “notes locales” par un vrai sélecteur de fichier.

Upload :
- application/octet-stream brut ;
- pas de filename/path/query envoyé au backend ;
- CSRF existant ;
- progression sophistiquée non requise ;
- après succès, recharger l’état serveur ;
- le nom local du fichier peut servir d’aide visuelle temporaire mais ne doit jamais être présenté comme donnée persistée backend.

Le client-extra rejoint ensuite le draft comme toute autre entrée avec destination/décisions/redistribution explicites.


PUBLICATION

Le backend exige job_id 32 hex.

Générer côté navigateur un id cryptographiquement aléatoire avec crypto.getRandomValues.

Important :
- conserver le même job_id pour un retry ambigu du même draft ;
- ne pas générer automatiquement un nouveau job après une erreur réseau dont le résultat serveur est inconnu ;
- resynchroniser l’état avant de conclure à un échec ;
- ne jamais afficher “publié” sans réponse/état serveur le confirmant.

CONCURRENCE / NAVIGATION

Les réponses tardives d’une ancienne instance/vue ne doivent jamais écraser l’état courant.

Utiliser génération/AbortController ou mécanisme équivalent pour les lectures UI.

Une déconnexion/navigation peut abandonner l’attente côté navigateur, mais ne doit jamais prétendre annuler un scan/upload/publication déjà accepté côté backend.

Après retour dans la vue : relecture serveur complète.

Les erreurs stale/conflict/unsupported/session doivent être affichées proprement et permettre un refresh/retry raisonnable.

API

Le helper JSON actuel peut être étendu proprement si nécessaire.

Pour client-extra, utiliser un helper dédié au body brut.

Ne jamais parser manifest/blob comme réponse JSON via le helper générique.

HORS PÉRIMÈTRE

- aucun changement de schéma SQLite ;
- aucun nouveau provider ;
- aucun changement des règles RBAC/distribution E3-B ;
- aucun sync Windows ;
- aucun F ;
- aucun bump 0.3.2 ;
- aucune fixture ou donnée synthétique chargée en production ;
- pas de localStorage/sessionStorage pour persister le draft content.

Si une modification backend est réellement nécessaire pour rendre l’UI correcte :
STOP et explique le contrat manquant au lieu d’élargir silencieusement E3-C.

TESTS

Faire évoluer tests/web-content-032.cjs :
- ne plus exiger “aucune API content” ;
- tester mapping réel observation/draft/publications ;
- appels GET/scan/draft/upload/publish/revoke ;
- optimistic revision/stale ;
- raisons/override et preuves conservées ;
- retry publication avec même job_id ;
- réponse tardive d’une ancienne instance ignorée ;
- erreurs/loading/partial ;
- aucune donnée synthétique de production.

Faire évoluer tests/web-content-browser-032.cjs :
- Chromium avec API mockée aux routes réelles, aucun Internet ;
- interactions scan → draft → upload extra → publication → révocation ;
- états erreur/stale ;
- changement d’instance pendant requête ;
- responsive réel 1440/1150/760/390 ;
- aucun overflow ni régression d’accessibilité évidente.

Conserver les régressions Web 0.3.1 pertinentes.

Valider au minimum :
- node --check JS/CJS ;
- tests/web-content-032.cjs ;
- tests/web-content-browser-032.cjs si Playwright disponible, sinon N/A explicite ;
- contrats Web ciblés 0.3.1 ;
- tests.test_release_docs ;
- MANIFEST.sha256 ;
- git diff --check.

Mettre à jour WORK_STATE.md, ASSISTANT_STATE.md, docs/CHANGELOG.md et CONTENT_MANIFESTS_032.md :
E3-C candidat uniquement, validation Ubuntu/Chromium requise.
E global non acquis ; F non commencé.

Régénérer MANIFEST.sha256.

Puis commit + push sur la même branche et mettre à jour la Draft PR #22.

Ne merge pas.
Ne tague pas.
Ne commence pas F.

Réponse finale courte uniquement :
- commit/push ;
- fichiers principaux ;
- comportement UI branché ;
- tests réellement exécutés PASS/FAIL/N/A ;
- limites restantes avant acquisition E3-C.

Aucune procédure Ubuntu ni prochain checkpoint dans la réponse finale.
~~~

## Réponse exacte

~~~text
- 
  Commit poussé : 3de856089a389e7afa35a8f1606f8c0d395505c5.
- UI branchée : état réel, scan, draft persistant, upload brut, publication/retry et révocation.
- Fichiers principaux : web/app.js, CSS scopé, trois contrats/fixtures Web, quatre documents et manifeste.
- **PASS** : contrat content, sept régressions UI 0.3.1, syntaxes JS/CJS, release-docs, manifeste 204 fichiers, diff-check.
- **N/A** : Chromium, Playwright absent. Validation Ubuntu/Chromium encore requise avant acquisition E3-C.
- PR #22 actualisée, toujours Draft. Working tree propre ; E global non acquis, F non commencé.
~~~

## Vérification externe

- Parent exact : `94fbabc86ae658cb24a81df40f374885e849b997`.
- Commit : `feat: connect admin client content UI`.
- PR #22 : ouverte et Draft, head `3de856089a389e7afa35a8f1606f8c0d395505c5`.
- Fichiers modifiés : `web/app.js`, `web/style.css`, `tests/web-content-032.cjs`, `tests/web-content-browser-032.cjs`, `tests/web-content-fixture-032.cjs`, plus docs/état/manifeste.
- Aucun fichier backend modifié.
- E3-C reste candidat ; validation Ubuntu/Chromium réelle encore requise.

# GP-046 — GPT-6.1 Sol Medium — 0.3.2-E3-A API Admin content

- Date : 2026-10-03
- Quota visible : 89 % → 66 % (**23 points**)
- Durée : **38 min 45 s**
- Résultat : succès
- Commit GamePanel : `0c8f2c42dd72b4d9701fb55994f6e060e13cff07`
- Draft PR : #22

## Prompt exact

~~~text
Travaille sur MrMekouil/GamePanel.

Branche :
work/0.3.2-content-manifests

PR :
Draft #22

HEAD attendu :
6fd46e5cbafb22bde1fba96f335b275e3be2cde9

OBJECTIF

Réaliser uniquement :

0.3.2-E3-A — API Admin content + orchestration réelle scan/draft/publication/révocation

A/B/C/D/E1/E2 sont acquis.
E global reste non acquis.
Contrat normatif : docs/CONTENT_MANIFESTS_032.md.

Avant modification :
- vérifie branche/status/diff/diff --cached/log ;
- lis WORK_STATE, ASSISTANT_STATE, ASSISTANT_WORKFLOW et le contrat ;
- audite API/auth/orchestrator + scanner B, classification C et publication E2 ;
- aucun reset/revert/clean ;
- si HEAD/état inattendu : STOP.

PÉRIMÈTRE

Ajouter des routes Admin cohérentes sous `/api/v1/admin/instances/{iid}/content/...` permettant réellement :

- lire l’état privé content d’une instance : pack stable, dernière observation, draft, diagnostics, publications/head ;
- lancer un scan Minecraft local B/C et persister une nouvelle observation ;
- créer le pack_id une seule fois, aléatoire/stable et indépendant de instance_id ;
- créer/modifier le draft avec optimistic concurrency par revision ;
- enregistrer décisions/overrides/approbations Admin avec acteur + raison sans falsifier les preuves ;
- lancer une publication réelle via ContentPublication E2 ;
- retry exact d’un même job ;
- révoquer une publication avec audit et retrait de head si nécessaire, sans modifier manifest/blobs/version.

Admin uniquement pour toutes ces routes.
CSRF/Origin/session existants restent autorité backend.

Le scan/provider ne doit pas dépendre d’Internet : local fonctionne seul ; provider externe indisponible => UNKNOWN/diagnostic, jamais faux succès.

Publication :
- ordre configuration_lock → lock content du pack ;
- pas de transaction SQL pendant scan/copie/provider ;
- revalidation pack/draft/revision/binding avant commit ;
- job actif protège contre rename B1 ;
- si client se déconnecte après acceptation, le travail déjà accepté doit pouvoir terminer/recovery sans libérer prématurément les gardes ;
- audit sans chemins hôte, bytes, tokens ou secrets.

Mutation via ancien alias d’instance : refus stale.
Aucun grant implicite.

HORS PÉRIMÈTRE E3-A

- aucun endpoint public/player de manifest/blob ;
- aucun téléchargement ;
- aucun HEAD/Range/304/ETag ;
- aucun client-extra binaire/upload HTTP ;
- aucun branchement UI D ;
- aucun nouveau provider ;
- aucun schema 6/version bump ;
- aucun F.

TESTS minimum

- Admin vs operator/player ;
- création/stabilité pack_id ;
- scan persistant + revision/diagnostics ;
- unsupported/non-Minecraft fail-closed ;
- draft optimistic concurrency/stale ;
- UNKNOWN/CONFLICT/override/provenance ;
- publication réelle E2 + retry exact + version conflict ;
- révocation/head/audit ;
- alias stale ;
- concurrence/configuration/rename/job ;
- déconnexion/cancellation après acceptation ;
- aucune fuite de chemins/secrets ;
- régressions E1/E2/security/startup pertinentes.

Mettre à jour WORK_STATE/ASSISTANT_STATE/CHANGELOG/CONTENT_MANIFESTS :
E3-A candidat seulement ; E3-B/E3-C/F non commencés.
Régénérer MANIFEST.sha256.

Valide tests ciblés, régressions, compile, git diff --check, manifeste et scope.
Puis commit + push sur la même branche et mise à jour de la Draft PR #22.

Ne merge pas. Ne tague pas.

Réponse finale courte :
commit/push, routes ajoutées, fichiers principaux, tests PASS/N/A et limites restantes.
Aucune procédure Ubuntu ni checkpoint suivant.
~~~

## Réponse exacte

~~~text
1. Commit **`0c8f2c42dd72b4d9701fb55994f6e060e13cff07`** poussé. Draft PR #22 mise à jour ; working tree propre.
2. Routes Admin sous `/api/v1/admin/instances/{iid}/content` : état, scan, draft, publication/retry et révocation.
3. Fichiers principaux : `content_admin.py`, `content_api.py`, `api.py`, `test_content_admin_032.py`, quatre documents et manifeste.
4. **Tests E3-A : 20 PASS / 26 N/A**. Régressions : **79/35**, **83/16**, **12/47** PASS/N/A. Compile, diff-check et manifeste **200/200 PASS**.
5. N/A : HTTP/POSIX et suites dépendant de `aiohttp`/`pydantic` indisponibles.
6. **E3-A candidat**, validation Ubuntu encore requise. Application 0.3.1/schema 5 inchangés ; aucun téléchargement ni branchement UI. Aucun merge/tag.
~~~

## Vérification externe

- Parent exact : `6fd46e5cbafb22bde1fba96f335b275e3be2cde9`.
- Commit : `feat: add admin content orchestration API`.
- PR #22 : ouverte et Draft, head `0c8f2c42dd72b4d9701fb55994f6e060e13cff07`.
- Fichiers principaux : `gamepanel/content_admin.py`, `gamepanel/content_api.py`, `gamepanel/api.py`, `tests/test_content_admin_032.py`, plus docs/état/manifeste.
- E3-A reste candidat ; aucun merge/tag.

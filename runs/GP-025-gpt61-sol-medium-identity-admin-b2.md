# GP-025 — GPT-6.1 Sol Medium — 0.3.1-E-B2 API Admin identité

- Date : 2026-10-02
- Quota visible : 93 % → 77 % (**16 points**)
- Durée : **21 min 37 s**
- Résultat : succès
- Commit GamePanel : `68d9a0dc99cf775bcde4f50a751f37553f2efe41`

## Prompt exact

~~~text
Travaille sur MrMekouil/GamePanel.

Branche existante :
work/0.3.1-ui-ux

PR :
Draft #19

HEAD attendu :
ca16063343009337cbc08118c1e8f11c46acb8eb

OBJECTIF

Implémenter uniquement :

0.3.1-E-B2 — API Admin d’identité + création d’instance avec id/nom personnalisés.

Le contrat complet est dans WORK_STATE.md :
« 0.3.1-E-A — contrat d’identité retenu ».

B1 est acquis sur Ubuntu réel.
Ne pas rouvrir/modifier son protocole transactionnel sans nécessité démontrée.

NE PAS faire l’UI Web complète : elle sera traitée en E-C.

PRÉ-VOL

Vérifier branche/status/diff/log puis lire :
- WORK_STATE.md
- docs/ASSISTANT_WORKFLOW.md
- docs/API.md
- sections pertinentes de docs/ARCHITECTURE.md

Inspecter le code réel avant modification.

PÉRIMÈTRE B2

1. API Admin de modification d’identité

Ajouter :

PATCH /api/v1/admin/instances/{iid}/identity

Admin uniquement.

Corps strict :
- instance_id optionnel
- display_name optionnel
- au moins un des deux requis
- aucun champ supplémentaire

Validation instance_id :
^[a-z0-9][a-z0-9-]{0,63}$
aucune normalisation implicite.

Validation display_name :
- trim explicite
- Unicode
- 1–80 caractères après trim
- refuser contrôles C0/DEL
- ne jamais accepter vide après trim

Nom seul :
réutiliser la mutation simple existante des settings/instance, sous les protections backend appropriées.
Ne pas déclencher le protocole root de rename.

ID :
réutiliser exclusivement la primitive B1 validée.

Si id + nom sont envoyés ensemble :
valider les deux avant toute écriture et conserver une sémantique sûre.
Ne pas affaiblir B1 ni créer silencieusement un état partiel.
Si le contrat combiné exige réellement de rouvrir B1, arrêter et documenter précisément le problème plutôt que bricoler.

Retourner l’identité finale de l’instance.

2. Création avec id/nom personnalisés

Étendre les deux parcours existants :

POST /admin/instance-candidates/{candidateId}/register

POST /admin/instance-resources/{profileId}/{resourceId}/register

pour accepter :
- instance_id optionnel
- display_name optionnel
- `path` reste requis uniquement pour le parcours manuel comme aujourd’hui.

Le helper root doit toujours :
- rescanner/revalider la ressource ;
- dériver lui-même service, chemins, ExecStart, profil, capabilities, etc. ;
- n’accepter du backend que l’id et le nom personnalisés ;
- revalider id/nom sous verrou ;
- vérifier collision inventaire/SQLite/alias ;
- refuser un service/une ressource déjà enregistré même avec un nouvel id libre ;
- permettre à un id personnalisé libre de résoudre uniquement un conflit d’id suggéré ;
- conserver staleness et conflits de ressource ;
- ne créer aucun grant implicite.

Substituer uniquement id/display_name à la Definition calculée.

Réutiliser la transaction register/recovery existante.

Le résultat register doit retourner la définition réellement enregistrée afin que le backend recharge exactement cette instance.

3. Compatibilité

- anciens appels `{}` continuent de fonctionner ;
- parcours manuel actuel reste compatible ;
- SQLite reste schema 4 ;
- aucune ressource privilégiée libre depuis HTTP ;
- ancien alias réservé impossible à réutiliser ;
- aucune UI complète dans B2.

TESTS

Ajouter/étendre les tests ciblés pour :
- route identity Admin/non-Admin ;
- body strict/invalide ;
- nom seul ;
- id seul ;
- collisions et ancien alias ;
- instance active/refus via B1 ;
- candidat avec id/nom custom ;
- ressource manuelle avec id/nom custom ;
- résolution d’un conflit d’id suggéré ;
- service déjà enregistré non contournable ;
- stale/resource conflict non contournable ;
- aucun grant implicite ;
- anciens bodies toujours compatibles ;
- aucun service/path/ExecStart/capability injectable.

Exécuter les tests disponibles dans Work.
Linux-only => N/A explicite, jamais faux PASS.

DOCS

Mettre à jour :
- docs/API.md
- docs/ARCHITECTURE.md si nécessaire
- docs/VALIDATION.md
- WORK_STATE.md
- MANIFEST.sha256

Ne pas modifier docs/ROADMAP.md ni ASSISTANT_STATE.md.

B2 doit rester « candidate, validation Ubuntu requise » tant que nous ne l’avons pas testée réellement.

Avant commit :
git diff
git diff --check
git status

Commit unique :

feat: add admin instance identity API

Push sur la même branche.

Ne pas merge.
Ne pas tag.
Ne pas commencer E-C.

Handoff :
- HEAD
- fichiers modifiés
- routes/contrats ajoutés
- comportement id+nom
- protections helper root
- tests PASS/N/A
- commandes Ubuntu exactes à rejouer
- confirmation SQLite schema 4 et E-C non commencé.
~~~

## Réponse exacte

~~~text
**HEAD publié :** `68d9a0dc99cf775bcde4f50a751f37553f2efe41`
Commit : `feat: add admin instance identity API` — branche existante, PR #19 toujours Draft, non mergée ; aucun tag.

**Fichiers modifiés :**

- `gamepanel/{api,db,identity,instance_admin,models}.py`
- `tools/gamepanel-inventory`
- `tests/test_identity_admin_031.py`
- `WORK_STATE.md`, `docs/{API,ARCHITECTURE,VALIDATION}.md`, `MANIFEST.sha256`

**Contrats :**

- PATCH Admin `/api/v1/admin/instances/{iid}/identity`, corps strict id et/ou nom.
- Deux parcours register étendus avec id/nom optionnels ; anciens appels compatibles.
- Nom seul : réglage SQLite sans rename root.
- Id + nom : validation préalable, puis commit SQLite unique ; journal/recovery B1 inchangés.
- Helper : rescan sous verrou, substitution limitée à id/nom, collisions/alias/service/stale contrôlés, aucun grant implicite.

**Validation Work :**

- **PASS :** 29 tests portables, contrat statique Instances, compilation, `git diff --check`.
- **N/A :** 34 tests natifs ; `fcntl`, `aiohttp`, `pydantic` absents. Non-régressions historiques bloquées à l’import par `aiohttp` ; navigateur indisponible sans Playwright.
- Manifeste : 178 empreintes accessibles vérifiées ; empreinte distante conservée pour l’unique PNG absent.

**Ubuntu — depuis le dépôt avec le Python du venv :**
```
(umask 0002; python -m unittest -v tests.test_identity_sql_031 tests.test_identity_admin_031 tests.test_identity_root_031 tests.test_identity_runtime_031)
(umask 022; python -m unittest -v tests.test_identity_sql_031 tests.test_identity_admin_031 tests.test_identity_root_031 tests.test_identity_runtime_031)
python -m unittest -v tests.test_instance_admin_030 tests.test_inventory_recovery_030 tests.test_manual_instances_0306 tests.test_grants_admin_028 tests.test_migration_030 tests.test_maintenance_029 tests.test_qualification_cache_031
python -m unittest -v tests.test_installer tests.test_installer_021 tests.test_installer_022 tests.test_installer_023
```

SQLite reste **schéma 4**. **E-C non commencé ; B2 candidate, validation Ubuntu requise.** Les overlays locaux sont préservés ; le miroir Git local reste ancien et non propre, tandis que le HEAD distant est confirmé.
~~~

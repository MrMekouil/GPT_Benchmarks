# GP-021 — GPT-6.1 Sol Medium — 0.3.1-E-B1 bloqué par l’environnement

- Date : 2026-10-01
- Quota visible : 62 % → 57 % (**5 points**)
- Durée : **4 min 31 s**
- Résultat : **bloqué avant implémentation**
- Commit GamePanel : **aucun**

## Prompt exact

~~~text
Travaille sur :

MrMekouil/GamePanel

Branche existante :
work/0.3.1-ui-ux

PR :
Draft #19 — 0.3.1 — Refonte UI/UX et finitions d'exploitation

HEAD à préserver :
1a835501ff7b5a563f0b906c5b9177f407a3bdd2
docs: define 0.3.1-E instance identity contract

OBJECTIF

Implémenter uniquement :

0.3.1-E-B1 — primitive transactionnelle backend/root pour renommer sûrement l’identifiant d’une instance existante.

Le contrat fonctionnel et de sûreté est déjà documenté dans :

WORK_STATE.md
section :
0.3.1-E-A — contrat d’identité retenu

Cette section est l’autorité de B1.
Lis-la intégralement avant toute modification et implémente-la fidèlement.

NE PAS faire dans B1 :
- UI Admin complète ;
- champs id/nom dans le dialogue d’ajout ;
- responsive ;
- clôture 0.3.1 ;
- merge/tag ;
- 0.3.2.

RÈGLES

- uniquement work/0.3.1-ui-ux ;
- aucune nouvelle branche ;
- pas de reset/revert/clean ;
- préserver tout travail local ;
- ne pas modifier docs/ROADMAP.md ;
- ne pas modifier ASSISTANT_STATE.md ;
- ne pas changer la version ;
- SQLite reste schema 4 ;
- backend non-root ;
- inventaire root-owned ;
- aucune ressource privilégiée libre venant du client ;
- fail-closed en cas d’ambiguïté.

PRÉ-VOL

Avant modification :

git branch --show-current
git status
git diff
git diff --cached
git log --oneline --decorate -15

Puis lire :

WORK_STATE.md
docs/ASSISTANT_WORKFLOW.md
docs/ARCHITECTURE.md

et inspecter le code réel concerné avant d’implémenter.

PÉRIMÈTRE B1

Implémenter la primitive :

old_instance_id -> new_instance_id

avec le contrat E-A.

Points indispensables :

1. Validation id
- regex : ^[a-z0-9][a-z0-9-]{0,63}$
- 1–64 caractères
- pas de normalisation implicite
- collision inventaire/SQLite/ancien alias = refus
- old == new = no-op explicite

2. Guards
Rename uniquement si l’instance est clairement OFFLINE et sans opération/mutation/transaction concurrente.
Réutiliser les locks existants et documenter leur ordre.

3. Transaction root multi-fichiers
Étendre le mécanisme existant avec un type/version dédié au rename.

Migrer si présents :
- /etc/gamepanel/instances.json
- intégrations PZ/Waker contenant instance_id
- /var/lib/gamepanel-installer/state.json
- drop-in BeamMP 91-beammp-<id>-access.conf

Journal transactionnel avec before/after, hashes, présence/absence, mode/owner, allowlist stricte et fsync.
Aucun chemin libre.

4. SQLite schema 4
Dans un BEGIN IMMEDIATE :
- instances.id
- definition_json.id
- grants.instance_id
- operations.instance_id
- settings liés à l’id
- chaîne d’alias old -> current

Ne pas réécrire logs/audit historiques.
Ancien id réservé.
PRAGMA foreign_key_check avant commit.
Pas de migration de schéma.

5. Recovery
Le rename doit être récupérable après crash.

Recovery AVANT construction normale de l’Orchestrator/API/SSE.

Décision :
- SQL OLD => restaurer tous les fichiers BEFORE
- SQL NEW => appliquer tous les fichiers AFTER
- ambigu => fail closed et journal conservé

Ne jamais rollback implicitement OLD après commit SQL NEW.

6. Runtime
Après succès persistant, reconstruire proprement les structures mémoire indexées par id.
Ne jamais exposer un état partiellement renommé.

7. BeamMP / installer
Migrer la preuve/qualification seulement si elle reste techniquement valide.
Sinon invalider et forcer requalification.
Aucun faux CONSERVÉ/SKIPPÉ.
Ne toucher ni aux ZIP ni aux maps.

8. Historique
Logs/audit existants restent sous ancien id.
Préparer l’accès via alias conformément à E-A.
Aucun grant orphelin.

TESTS

Ajouter/étendre des tests ciblés pour :
- validation id ;
- collisions/alias ;
- SQLite + FK ;
- grants/opérations/settings ;
- historique inchangé ;
- transaction root ;
- recovery après crash aux frontières importantes ;
- guards OFFLINE/active/opération en cours ;
- BeamMP qualification/drop-in ;
- intégrations PZ/Waker ;
- état ambigu => fail closed.

Les crash tests doivent démontrer :
état final entièrement OLD ou entièrement NEW selon la décision SQLite, jamais un mélange servi.

Exécuter les tests ciblés disponibles.
Ne pas annoncer PASS si une dépendance manque.

DOCS

Mettre à jour si nécessaire :
- WORK_STATE.md
- docs/ARCHITECTURE.md
- docs/VALIDATION.md
- docs/API.md uniquement si une API publique est réellement ajoutée

Ne pas modifier docs/ROADMAP.md.

Régénérer MANIFEST.sha256 et vérifier :
- hashes exacts
- aucun undefined

AVANT COMMIT

git diff
git diff --check
git status

Relire particulièrement :
gamepanel/db.py
gamepanel/orchestrator.py
gamepanel/instance_admin.py
tools/gamepanel-inventory
gamepanel/integrations.py
installer/*
deploy/sudoers.gamepanel

Si une ambiguïté importante de sûreté reste ouverte :
NE PAS commiter une implémentation dangereuse.
Faire un handoff précis.

Sinon commit unique :

feat: add transactional instance identity rename core

Push sur :
work/0.3.1-ui-ux

Ne pas merger.
Ne pas taguer.

HANDOFF

Donner :
- HEAD final
- fichiers modifiés
- tests + résultats
- protocole transaction/recovery réellement implémenté
- ordre des locks
- références migrées / historiques conservées
- comportement BeamMP/PZ/Waker
- risques restants
- confirmation SQLite schema 4
- confirmation aucune UI complète
- prochain checkpoint :
0.3.1-E-B2 — API Admin + création avec id/nom personnalisés
~~~

## Réponse exacte

~~~text
**B1 bloqué avant implémentation. Aucun commit ni push effectué.**

- **HEAD distant préservé :** `1a835501ff7b5a563f0b906c5b9177f407a3bdd2`.
- **Modifications locales uniquement :** `WORK_STATE.md` consigne le blocage ; `MANIFEST.sha256` recalculé. Travail préexistant préservé.
- **Tests ciblés : non exécutables.** Cinq modules échouent à l’import : `aiohttp` ou `fcntl` absents. `pydantic` manque également. Installation pip bloquée par le sandbox (`WinError 10013`), WSL inaccessible (`E_ACCESSDENIED`).
- **Contrôles PASS :** `git diff --check`, 172 empreintes accessibles vérifiées, aucune entrée invalide/`undefined`. Le PNG absent du miroir garde son empreinte précédente.

**Points de sûreté confirmés :**

- Le recovery doit précéder la construction de l’Orchestrator, qui écrit actuellement dans SQLite avant le lifecycle.
- L’empreinte BeamMP inclut le chemin du drop-in contenant l’id. Réindexer simplement la preuve serait incorrect : sa validité doit être démontrée ou la preuve invalidée.

Aucun protocole transaction/recovery B1 implémenté, aucune référence migrée, aucun historique réécrit. SQLite reste **schéma 4** ; aucune UI ajoutée.

**Reprise nécessaire : B1 dans un environnement Linux permettant les tests de crash et les verrous POSIX. B2 reste conditionné à un B1 validé.**
~~~

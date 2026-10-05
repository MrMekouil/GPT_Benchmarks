# GP-061 — GPT-6.1 Sol Medium — STOP pré-vol import CurseForge local

- Date : 2026-10-05
- Quota visible : 100 % → 97 % (**3 points**)
- Durée : **34 s**
- Résultat : bloqué conformément au prompt
- Commit GamePanel : aucun
- Draft PR : #22

## Prompt exact

~~~text
Travaille uniquement sur :

Repo : MrMekouil/GamePanel
Branche : work/0.3.2-content-manifests
PR : Draft #22
HEAD distant attendu : 3ae10db45018232336888e2dfab751ca4e3f7f26

Avant modification :
- vérifie branche/status/diff/diff --cached/log et HEAD distant ;
- lis WORK_STATE.md, ASSISTANT_STATE.md, docs/ASSISTANT_WORKFLOW.md,
  docs/CONTENT_MANIFESTS_032.md et docs/VALIDATION_032.md.
STOP si l’état diffère.

OBJECTIF

Ajouter à 0.3.2 un import Admin facultatif de `minecraftinstance.json`
provenant d’un profil CurseForge local, afin d’enrichir la provenance et
la classification environment des JAR Minecraft observés.

Réutilise les contrats/providers/classification existants. Pas de refonte
large et pas de migration SQLite sauf nécessité démontrée : si une migration
devient indispensable, STOP et explique avant de l’implémenter.

RÈGLES DE PREUVE

Pour chaque `installedAddon` :
- utiliser uniquement `installedFile` comme fichier réellement installé ;
- ne jamais utiliser `latestFile` pour une preuve exacte ;
- extraire le SHA-1 valide de `installedFile.hashes` ;
- comparer ce SHA-1 au SHA-1 réellement calculé sur le JAR serveur ;
- seule une égalité exacte autorise l’identité/provenance CurseForge.

Mapping `installedFile.gameVersion` :
- Client + Server => `both`
- Client seul => `client-only`
- Server seul => `server-only`
- aucun des deux => environment reste `unknown`

Interdictions :
- jamais classifier par filename seul ;
- jamais déduire `both` de la simple présence dans CurseForge ;
- SHA-1 absent/malformed/différent => aucune preuve exacte ;
- une contradiction avec une preuve existante doit suivre le moteur CONFLICT,
  jamais être écrasée ;
- les 2 CONFLICT historiques ne doivent pas recevoir de traitement spécial.

Le profil est un snapshot local potentiellement ancien : afficher une
formulation du type « métadonnées locales CurseForge » et, si disponible,
un horodatage informatif sans prétendre qu’il s’agit d’une donnée live.

IMPORT ADMIN / UI

Dans Admin > Contenus client :
- action claire « Importer un profil CurseForge » ;
- sélection/upload de `minecraftinstance.json` ;
- aide : CurseForge > profil > Ouvrir le dossier ;
- exemple Windows :
  `%USERPROFILE%\curseforge\minecraft\Instances\<profil>\minecraftinstance.json`
  en précisant que l’emplacement peut être personnalisé ;
- résumé après import : exacts reconnus, both/client/server, exacts restant
  unknown, non-correspondants/absents, conflits.

Respecter le RBAC Admin existant.

SÉCURITÉ

Le JSON est non fiable :
- taille bornée ;
- JSON invalide/structure inattendue gérés proprement ;
- aucun chemin Windows du profil utilisé comme chemin serveur ;
- aucun contenu exécuté ;
- pas de JSON brut/path/GUID inutile dans logs ou diagnostics ;
- ne conserver que les données normalisées nécessaires, pas le fichier brut.

Pas d’API CurseForge, clé API, scraping, téléchargement, auto-update,
synchronisation Windows, agent compagnon ou changement de redistribution.
`allowModDistribution` ne doit pas modifier les règles de sécurité actuelles.

PREUVE RÉELLE À CONSERVER DANS LE RUNBOOK

Sur Aero, pour les 39 vrais UNKNOWN, comparaison SHA-1 déjà réalisée :
- 21 exact + Client/Server => both
- 0 client-only
- 2 exact + Server => server-only
- 15 exacts sans côté => restent unknown
- 1 absent du profil
- 0 filename-only
- 0 fichier serveur absent

Après intégration réelle, résultat attendu : 23 UNKNOWN de moins, sans mutation
des JAR et sans changement artificiel des CONFLICT.

Ne mets aucune donnée personnelle réelle dans les fixtures.

TESTS

Couvre au minimum :
- exact both/client/server ;
- exact sans côté => provenance oui, environment unknown ;
- filename identique/hash différent ;
- SHA-1 absent/malformed ;
- addon absent ;
- latestFile correspondant mais installedFile différent ;
- JSON invalide/trop gros/structure partielle ;
- conflit avec preuve existante ;
- RBAC ;
- upload/UI et responsive ;
- régressions scan/draft/publication/stale/rebase/revoke/client-extra.

Mets à jour uniquement les docs/états nécessaires et MANIFEST.sha256.
Prépare la validation réelle Aero dans docs/VALIDATION_032.md mais ne l’exécute pas.

Puis tests pertinents, git diff --check, manifeste, commit + push sur la même
branche/PR Draft.

Aucun merge/tag/release/version bump.
F reste NON ACQUIS. Aucun gate F réel.

Handoff final très court :
HEAD, fichiers, architecture retenue, tests PASS/FAIL/N/A, limites.
Ne donne pas de commandes Ubuntu à l’utilisateur : Assistant Work s’en charge.
~~~

## Réponse exacte

~~~text
**STOP : le HEAD local diffère du HEAD attendu.**

- Local : `735d4dc2081bc760ae82649c55bc5feef45cafdb`
- Distant : `3ae10db45018232336888e2dfab751ca4e3f7f26` — conforme, PR #22 Draft.
- Branche correcte ; status/diff/diff cached propres.
- Aucun fichier modifié, aucun commit/push, aucun test exécuté.

Le checkout local doit être synchronisé avant de reprendre l’import CurseForge.
~~~

## Synthèse enregistrée

- HEAD distant attendu : `3ae10db45018232336888e2dfab751ca4e3f7f26`, confirmé conforme sur la branche/PR.
- HEAD local Work : `735d4dc2081bc760ae82649c55bc5feef45cafdb`.
- Branche correcte ; status/diff/diff --cached propres.
- Le prompt imposait **STOP si l’état diffère** : arrêt correct avant implémentation.
- Aucun fichier modifié, aucun test exécuté, aucun commit/push.
- L’import Admin `minecraftinstance.json` CurseForge reste à reprendre après synchronisation du checkout local.

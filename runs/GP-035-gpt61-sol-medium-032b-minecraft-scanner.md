# GP-035 — GPT-6.1 Sol Medium — 0.3.2-B scanner Minecraft local

- Date : 2026-10-02
- Quota visible : 78 % → 66 % (**12 points**)
- Durée : **20 min 49 s**
- Résultat : succès
- Commit GamePanel : `24d675b1097ab22d079462a7286627b422035218`
- Draft PR : #22 — `0.3.2 — Manifestes et distribution de contenu client`

## Prompt exact

~~~text
Travaille sur MrMekouil/GamePanel.

Branche existante :
work/0.3.2-content-manifests

PR existante :
Draft #22 — 0.3.2 — Manifestes et distribution de contenu client

HEAD attendu au départ :
2c61b30a07859ced630d2dd8a01c5b9c3e786d28

OBJECTIF

Réaliser UNIQUEMENT :

0.3.2-B — scanner Minecraft local

Le contrat 0.3.2-A est acquis et normatif :
docs/CONTENT_MANIFESTS_032.md

Avant tout :
- vérifie branche/status/diff/diff --cached/log ;
- lis WORK_STATE.md, ASSISTANT_STATE.md, ASSISTANT_WORKFLOW.md et CONTENT_MANIFESTS_032.md ;
- audite le code existant pertinent, notamment Definition/root, profiles, candidates et files ;
- préserve tout état local existant ;
- aucun reset/revert/clean.

Si le HEAD ou l’état réel ne correspond pas, STOP.

PÉRIMÈTRE B

Implémenter un service interne read-only capable de scanner une instance Minecraft backend-owned à partir de sa Definition/root.

Il doit au minimum produire un snapshot structuré contenant :
- version Minecraft détectée si prouvable ;
- loader + version si prouvables ;
- mods JAR observés ;
- SHA-256 et taille de chaque fichier ;
- métadonnées locales utiles et bornées des JAR ;
- configs candidates uniquement selon une politique explicite/allowlistée ;
- diagnostics explicites lorsque quelque chose est inconnu ou non lisible.

Support prioritaire et testé :
- Forge ;
- NeoForge.

Garder le design extensible pour Fabric/autres loaders sans surdévelopper ce checkpoint.

SÉCURITÉ OBLIGATOIRE

- ne jamais exécuter un JAR, Java, script ou hook ;
- aucun chemin fourni par un client/API ;
- root uniquement depuis la Definition contrôlée backend ;
- refus symlink, traversal, fichiers spéciaux et sorties de racine ;
- snapshot stable : détecter/refuser un fichier modifié pendant lecture/hash ;
- lecture JAR/ZIP strictement bornée ;
- définir des limites explicites et testées : taille fichier/archive, nombre d’entrées, taille metadata décompressée, ratio/profondeur si pertinent ;
- pas d’extraction libre sur disque ;
- refuser archives/path names dangereux, doublons ambigus et cas manifestement abusifs ;
- ne jamais scanner/publier worlds, saves, logs, backups, secrets, server.properties, ops/whitelist/bans par défaut ;
- ne pas considérer tout config/ comme publiable automatiquement.

Le scanner observe seulement.
Il ne décide PAS encore :
- client/server/both ;
- required/recommended/optional ;
- redistribution ;
- provider externe ;
- publication.

Ces décisions appartiennent aux checkpoints suivants.

HORS PÉRIMÈTRE

Aucun :
- Modrinth/CurseForge/GitHub réseau ;
- provider externe ;
- UI ;
- endpoint public ;
- migration SQLite ;
- persistance de draft ;
- content store ;
- publication ;
- téléchargement ;
- client-extra fonctionnel ;
- changement de version applicative.

SQLite reste schema 4.

TESTS

Ajouter des tests ciblés avec fixtures synthétiques Forge/NeoForge couvrant au minimum :
- détection normale version/loader ;
- JAR valide + hash/métadonnées ;
- JAR inconnu mais observable ;
- symlink/traversal ;
- archive abusive/metadata trop grosse ;
- fichier remplacé/modifié pendant snapshot ;
- exclusions worlds/logs/backups/secrets ;
- résultat déterministe indépendant de l’ordre filesystem.

Ne pas dépendre d’un vrai serveur Minecraft ni d’Internet pour les tests.

DOCUMENTATION

Après implémentation :
- mettre à jour WORK_STATE.md ;
- ASSISTANT_STATE.md si nécessaire ;
- docs/CHANGELOG.md ;
- docs/CONTENT_MANIFESTS_032.md seulement si l’implémentation B révèle une précision nécessaire, sans réécrire le contrat acquis ;
- MANIFEST.sha256.

VALIDATION

Exécuter les tests ciblés B puis les régressions pertinentes.
Relire le diff et faire git diff --check.
Aucun faux PASS si une dépendance empêche un test.

Puis :
- commit ;
- push sur la même branche ;
- mettre à jour la Draft PR #22 si nécessaire.

Ne merge pas.
Ne tague pas.
Ne publie pas de release.
Ne commence pas 0.3.2-C.

Restitution finale courte :
commit/push, fichiers principaux, tests PASS/FAIL/N/A, limites concrètes.
Aucune procédure Ubuntu ni prochain checkpoint.
~~~

## Réponse exacte

~~~text
1. Commit poussé : `24d675b1097ab22d079462a7286627b422035218`. PR #22 mise à jour, toujours Draft.
2. Fichiers : scanner `gamepanel/minecraft_content.py`, tests dédiés, WORK_STATE, ASSISTANT_STATE, CHANGELOG, contrat et manifeste.
3. **PASS** : 25 tests scanner portables + 18 régressions ; compilation, diff-check et 184 hashes.
4. **N/A** : 15 tests POSIX ; suites profils/ajout manuel/version bloquées par pydantic/aiohttp absents.
5. B reste candidat, sans validation Linux réelle. Configs exclues par défaut ; détection d’installation, pas du loader actif.
6. Version 0.3.1 et SQLite 4 inchangées. Tree propre ; aucun merge/tag, C non commencé.
~~~

## Vérification externe

- Parent exact : `2c61b30a07859ced630d2dd8a01c5b9c3e786d28`.
- Commit : `feat: add bounded local Minecraft content scanner`.
- PR #22 : ouverte et Draft, head `24d675b1097ab22d079462a7286627b422035218`.
- Fichiers ajoutés : `gamepanel/minecraft_content.py` et `tests/test_minecraft_content_032.py`, plus état/docs/manifeste.
- Aucun merge, tag, release ou checkpoint C.

# GP-015 — GPT-6.1 Sol Medium — Correctif Sessions Utilisateurs

- Date : 2026-10-01
- Quota visible : 57 % → 54 % (**3 points**)
- Durée : **5 min 52 s**
- Résultat : succès
- Commit GamePanel : `de76ac3`

## Prompt exact

~~~text
Travaille sur MrMekouil/GamePanel
branche work/0.3.1-ui-ux
PR Draft #19.

Checkpoint à préserver :
c9186373341215150053c01fab7cfe8c81f414a3

Pré-vol :
branche, git status, git diff, git log -10, lire WORK_STATE.md.
Ne reset/revert rien.

CORRECTIF UNIQUE

Dans la modale Sessions de l’écran Utilisateurs, les badges
"Non révoquée" et "Révoquée" utilisent actuellement tous les deux
la classe visuelle OFFLINE.

Corriger uniquement cette distinction :

- session non révoquée / active → badge READY
- session révoquée → badge OFFLINE

Ne change aucun endpoint, aucune logique de session, aucun texte métier
nécessaire, aucun autre écran.

Étendre tests/web-users-density-031.cjs pour vérifier explicitement que
les deux états ont des classes visuelles différentes et correctes.

Exécuter :
- contrat Utilisateurs ;
- node --check des fichiers JS/CJS modifiés ;
- git diff --check ;
- tests ciblés pertinents disponibles.

Mettre WORK_STATE.md à jour brièvement et régénérer MANIFEST.sha256.

Commit + push sur la même branche.
Ne merge pas, ne tague rien.

Réponse finale courte uniquement.
~~~

## Réponse exacte

~~~text
Commit `de76ac3` poussé sur `work/0.3.1-ui-ux`.

- Sessions : `READY` pour Non révoquée, `OFFLINE` pour Révoquée ; logique et textes inchangés.
- Fichiers : `web/app.js`, contrat Utilisateurs, `WORK_STATE.md`, `MANIFEST.sha256`.
- **PASS** : contrat Utilisateurs, syntaxes JS/CJS, diff, 5 tests Python ciblés.
- **Bloqués/N/A** : tests backend (`aiohttp` absent), navigateur (Playwright absent).
- Manifeste : 170 fichiers vérifiés ; empreinte du PNG absent conservée.
~~~

# GP-014 — GPT-6.1 Sol Medium — Admin Utilisateurs UI

- Date : 2026-10-01
- Quota visible : 68 % → 57 % (**11 points**)
- Durée : **12 min 42 s**
- Résultat : succès
- Commit GamePanel : `c9186373341215150053c01fab7cfe8c81f414a3`

## Prompt exact

~~~text
Travaille sur :

MrMekouil/GamePanel

Branche obligatoire :
work/0.3.1-ui-ux

PR :
Draft #19 — 0.3.1 — Refonte UI/UX et finitions d'exploitation

Checkpoint à préserver :
90bcee3157b7b8e5bf79117d575a308581c31e62

PRÉ-VOL

Avant toute modification :

- vérifie la branche ;
- git status ;
- git diff ;
- git log --oneline -10 ;
- lis intégralement WORK_STATE.md ;
- préserve toute modification non commitée ;
- ne reset/revert rien sans comprendre l’état réel.

OBJECTIF

Harmoniser uniquement l’écran Admin Utilisateurs et ses modales.

La page actuelle est déjà correcte :

- garder le tableau ;
- ne pas faire de refonte lourde ;
- conserver la direction visuelle actuelle 0.3.1.

Les écrans Serveurs, Instances et Supervision sont acquis et ne doivent pas changer.

PAGE UTILISATEURS

Conserver la topbar :
Utilisateurs

Dans le contenu :

- supprimer l’eyebrow “ADMINISTRATION” ;
- remplacer le H1 “Permissions” par “Utilisateurs” ;
- conserver :
  “Comptes, rôles, accès par instance et sessions.”
- conserver le bouton jaune “+ Créer un compte”.

Tableau à conserver :

- Compte
- Rôle
- État
- Gestion

Garder username, date de création, rôle, badge Actif/Désactivé et toutes les actions.

Le tableau doit rester compact.

Il est possible d’indiquer discrètement le compte courant avec “Vous” ou “Compte actuel”, sans backend supplémentaire.

Renommer uniquement le libellé visuel :

Permissions → Accès

Le comportement reste identique.

ACTIONS

Conserver :

- Accès
- Sessions
- Modifier
- Supprimer

Accès / Sessions / Modifier = neutres.
Supprimer = destructif rouge discret.

Le compte courant ne doit toujours pas pouvoir se supprimer.

MODALES

Priorité du lot : améliorer leur lisibilité/densité sans changer leur logique.

Créer un compte :

- conserver champs, validations, API et comportements.

Modifier :

- conserver rôle, actif, mot de passe facultatif ;
- conserver la révocation des sessions ;
- rendre cette conséquence clairement visible.

Accès :

- ne modifier AUCUNE logique de grants/capabilities ;
- préserver global_access, presets, dependencies, RCON sensible, permissions historiques, hidden/inventory_required ;
- rendre les cartes d’instance plus compactes et faciles à scanner ;
- nom, état, toggle d’accès, preset et capabilities doivent rester clairement visibles ;
- desktop : capabilities en 2 colonnes si pertinent ;
- mobile : 1 colonne.

Sessions :

- préserver Web / Windows ;
- dates ;
- active / révoquée ;
- révocation individuelle ;
- révocation globale ;
- rendre la liste plus compacte.

RESPONSIVE

Desktop :

- tableau lisible ;
- actions propres ;
- modales compactes.

Mobile :

- conserver la transformation actuelle du tableau ;
- aucun scroll horizontal global ;
- modales dans le viewport ;
- cartes permissions en une colonne.

Ne touche pas à la sidebar mobile.

INTERDICTIONS

Ne touche pas :

- backend/API/SQLite ;
- règles de rôles/grants/capabilities ;
- sessions backend ;
- Serveurs ;
- Instances ;
- Supervision ;
- Audit ;
- Configuration ;
- sidebar/navigation ;
- branding/palette ;
- installateur ;
- client Windows ;
- BeamMP ;
- ROADMAP.md ;
- 0.3.1-E ;
- supervision historique ;
- docs GPT / Assistant Workflow.

TESTS

Vérifier au minimum :

- titre Utilisateurs ;
- absence de l’eyebrow ;
- bouton Créer un compte ;
- compte courant non supprimable ;
- autre compte supprimable ;
- libellé Accès ;
- création/modification/suppression ;
- sessions ;
- Admin global ;
- grants ;
- presets ;
- capability dependencies ;
- RCON sensible ;
- permissions historiques ;
- responsive.

Exécuter :

- contrats Node/Web pertinents ;
- node --check JS/CJS modifiés ;
- tests Python comptes/grants/permissions disponibles ;
- non-régression Serveurs/Instances/Supervision si fichier partagé touché ;
- git diff --check.

Si Playwright/Chromium absent :
N/A, ne pas prétendre au PASS navigateur.

FIN

Mettre à jour WORK_STATE.md brièvement.
Régénérer MANIFEST.sha256 correctement.

Puis :

- commit ;
- push sur work/0.3.1-ui-ux ;
- ne merge pas ;
- ne tague rien ;
- ne commence pas 0.3.1-E.

Réponse finale Work courte :
commit, fichiers modifiés, changements visuels, comportements préservés, tests PASS/FAIL/N/A.
Pas de procédure Ubuntu.
~~~

## Réponse exacte

~~~text
Commit **`c9186373341215150053c01fab7cfe8c81f414a3`** poussé sur `work/0.3.1-ui-ux`. PR #19 toujours Draft, non mergée.

- **Fichiers :** `web/app.js`, `web/style.css`, nouveau contrat `tests/web-users-density-031.cjs`, `WORK_STATE.md`, `MANIFEST.sha256`.
- **Visuel :** titre Utilisateurs sans eyebrow, libellé Accès, repère « Vous », tableau et modales compactés, révocation des sessions clairement indiquée.
- **Comportements conservés :** CRUD, protection du compte courant, sessions, Admin global, grants, presets, dépendances et RCON sensible.
- **PASS :** contrats Utilisateurs/Serveurs/Instances/Supervision, syntaxes JS/CJS, 5 tests Python disponibles, diff et 170 empreintes accessibles du manifeste.
- **Limites :** Python comptes/grants/permissions bloqués par `aiohttp` absent ; navigateur N/A faute de Playwright. PNG glossy absent du miroir, empreinte conservée. Rendu Ubuntu réel encore à valider.
~~~

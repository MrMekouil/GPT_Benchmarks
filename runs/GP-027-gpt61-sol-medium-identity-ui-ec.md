# GP-027 — GPT-6.1 Sol Medium — 0.3.1-E-C UI Admin identité

- Date : 2026-10-02
- Quota visible : 77 % → 60 % (**17 points**)
- Durée : **26 min 31 s**
- Résultat : succès
- Commit GamePanel : `11f19845baf275c2765e93454b3a3e8aed8b9bb8`

## Prompt exact

~~~text
Travaille sur MrMekouil/GamePanel.

Branche existante :
work/0.3.1-ui-ux

PR :
Draft #19

HEAD attendu :
e02109326cc8bca60cd945a19cf89740c727a1e0

OBJECTIF

Implémenter uniquement :

0.3.1-E-C — UI Admin Instances pour la gestion d’identité.

E-B1 et E-B2 sont acquis sur Ubuntu réel.
Le contrat fonctionnel et de sécurité fait autorité dans WORK_STATE.md.

Ne pas modifier le protocole backend transactionnel sauf bug concret démontré.
Ne pas commencer la clôture/release 0.3.1.

PRÉ-VOL

Vérifier :
- branche/status/diff/log
- WORK_STATE.md complet
- docs/ASSISTANT_WORKFLOW.md
- docs/API.md
- UI actuelle Instances / Serveurs
- tests web existants pertinents

PÉRIMÈTRE

1. Vue Admin Instances

Ajouter la gestion d’identité uniquement dans la vue Admin dédiée.

Pour chaque instance enregistrée, afficher clairement :
- nom visible actuel ;
- identifiant actuel ;
- type/adapter/service si déjà présent dans cette vue ;
- action explicite de modification d’identité.

L’édition doit permettre :
- modifier le display_name ;
- modifier l’instance_id ;
- modifier les deux ensemble.

Utiliser exclusivement :
PATCH /api/v1/admin/instances/{iid}/identity

Contraintes UX :
- ne jamais prétendre que le changement d’id est anodin ;
- si l’id change, indiquer clairement que l’instance doit être arrêtée et que GamePanel effectue une migration transactionnelle ;
- garder les messages d’erreur backend réels ;
- après succès, recharger/réconcilier l’état UI avec le nouvel id sans conserver de référence DOM/JS obsolète vers l’ancien id ;
- aucune mutation optimiste trompeuse avant réponse serveur.

2. Dashboard normal / Serveurs

Le contrôle visible permettant de modifier le nom d’instance ne doit plus être proposé dans le dashboard normal.

Le PATCH settings historique reste côté backend pour compatibilité, mais l’identité se gère visuellement uniquement dans Admin > Instances.

Ne pas retirer les autres réglages serveur légitimes.

3. Création automatique

Dans le flux d’ajout depuis un candidat détecté, permettre avant confirmation :
- instance_id personnalisé ;
- display_name personnalisé.

Préremplir avec les valeurs suggérées du candidat.

Envoyer uniquement :
{
  "instance_id": "...",
  "display_name": "..."
}

au POST register existant.

L’utilisateur doit pouvoir corriger un conflit INSTANCE_ID_CONFLICT avec un autre id libre.

Ne jamais exposer ni rendre éditables :
- service
- ExecStart
- paths techniques
- adapter/profile
- capabilities
- ports/secrets

Les conflits service/resource/stale restent non contournables.

4. Création manuelle

Même principe pour le parcours manuel :
- path reste le champ existant ;
- après sélection/preview de la ressource, permettre id + nom personnalisés avant register ;
- envoyer path + instance_id/display_name uniquement ;
- ne pas permettre de modifier les propriétés techniques dérivées.

5. Validation UI

Respecter exactement le backend :
instance_id :
^[a-z0-9][a-z0-9-]{0,63}$

display_name :
- trim
- Unicode
- 1–80
- pas C0/DEL

La validation frontend sert au confort uniquement :
le backend reste autoritaire.

6. Style

Respecter strictement la direction 0.3.1 déjà acquise :
- graphite/anthracite neutre
- accent tournesol #D19E3D uniquement pour primaire/sélection/navigation
- densité compacte cohérente avec les pages Admin déjà harmonisées
- responsive mobile propre
- pas de nouveau langage visuel
- pas de gros panneaux inutilement espacés

Réutiliser les composants/classes existants autant que possible.

TESTS

Étendre les tests web pertinents pour couvrir au minimum :
- contrôle d’identité absent du dashboard Serveurs normal ;
- contrôle présent dans Admin Instances ;
- édition nom seul ;
- édition id seul ;
- édition combinée ;
- succès avec changement de clé/id et rafraîchissement UI ;
- erreur backend affichée sans état UI mensonger ;
- création candidat avec valeurs préremplies ;
- custom id/nom envoyés au register ;
- parcours manuel équivalent ;
- aucun champ technique injectable/éditable ;
- conflit id corrigeable ;
- service/stale non présenté comme corrigeable par changement d’id ;
- responsive/modal ou panneau d’édition sans débordement évident.

Exécuter tous les tests web disponibles dans Work.
Playwright/browser indisponible => N/A explicite.
Ne jamais déclarer un test réel Ubuntu/browser PASS s’il n’a pas été exécuté.

DOCS

Mettre à jour :
- WORK_STATE.md
- docs/VALIDATION.md
- éventuellement docs/API.md uniquement si le comportement UI doit être précisé
- MANIFEST.sha256

Ne pas modifier :
- docs/ROADMAP.md
- ASSISTANT_STATE.md
- version
- schéma SQLite

ÉTAT FINAL ATTENDU

E-C = candidate implémentée, validation visuelle/réelle Ubuntu encore requise.

Avant commit :
- git diff
- git diff --check
- git status
- tests ciblés

Commit unique :

feat: add admin instance identity UI

Push sur la même branche.

Ne pas merge.
Ne pas tag.
Ne pas commencer la clôture finale 0.3.1.

HANDOFF

Donner :
- HEAD final
- fichiers modifiés
- comportement UI ajouté
- suppression du contrôle d’identité du dashboard normal
- parcours création auto/manuelle
- tests PASS/N/A
- points à valider visuellement sur Ubuntu desktop + mobile
- confirmation SQLite schema 4 et aucun E-D/clôture commencé.
~~~

## Réponse exacte

~~~text
1. **HEAD publié** : `11f19845baf275c2765e93454b3a3e8aed8b9bb8` — `feat: add admin instance identity UI`.
2. **Fichiers** : `web/app.js`, `web/style.css`, cinq contrats Web Instances/Serveurs, `WORK_STATE.md`, `docs/VALIDATION.md`, `MANIFEST.sha256`.
3. **UI** : édition Admin du nom, de l’id ou des deux ; avertissement transactionnel, erreurs backend conservées et réconciliation du nouvel id. Contrôle du nom retiré de Serveurs, autres réglages conservés.
4. **Création auto/manuelle** : id/nom préremplis et éditables ; payloads limités ; conflit d’id corrigeable, service/stale bloquants.
5. **PASS** : sept contrats Web, 21 vérifications syntaxiques, diff-check, 179 empreintes accessibles. Empreinte distante du PNG absent conservée.
6. **N/A** : onze contrats navigateur, Playwright absent.
7. **Ubuntu desktop/mobile à valider** : modales, débordements, éditions, refus, rafraîchissement et créations.
8. Backend B1/B2 et SQLite **schéma 4 inchangés**. E-C reste candidate ; aucun E-D/clôture, merge ou tag. PR #19 toujours Draft. Miroir Git local historique conservé, non nettoyé.
~~~

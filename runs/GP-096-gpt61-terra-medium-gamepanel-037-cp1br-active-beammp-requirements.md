# GP-096 — GPT-6.1 Terra Medium — GamePanel 0.3.7 CP1-B/R

- Date d'enregistrement : **2026-11-01** (date d'exécution Work non indiquée)
- Projet source : **GamePanel**, branche `work/0.3.7-content-comparison`
- Modèle / effort : **GPT-6.1 Terra / Medium**
- Quota visible : **57 % → 47 % = 10 points**
- Durée : **3 min 55 s (235 secondes)**
- Statut : **succès de correction ciblée CP1-B/R** ; validation backend réelle non acquise
- Commit GamePanel vérifié : [`67fb1060ad6868da1ad3e754679a4e6e464350bf`](https://github.com/MrMekouil/GamePanel/commit/67fb1060ad6868da1ad3e754679a4e6e464350bf)

## Prompt exact

~~~text
# GamePanel 0.3.7 — CP1-B/R : isoler les exigences BeamMP réellement actives

**Modèle : GPT-6.1 Terra — Medium**

## Références

- Dépôt privé : `MrMekouil/GamePanel`
- Branche existante : `work/0.3.7-content-comparison`
- HEAD attendu : `96b72e529cb27cf224b452b40a556ccd3d1226ad`
- Stable `main` : `161360863ea7a6b19ccb80190588aae86831ddd1`

CP1-B livré, 25 tests CP0 + 13 tests de projection + 9 tests existants de sélection PASS déclarés.

## 1. Prévol ciblé

Vérifier branche, HEAD, statut Git, diff, index et historique récent. Préserver tout travail préexistant.

Lire `AGENTS.md`, `WORK_STATE.md`, `docs/ASSISTANT_WORKFLOW.md`, `docs/CONTENT_COMPARISON_037.md` et les sources pertinentes :

- `gamepanel/beammp_requirements.py`
- `gamepanel/beammp_catalog.py`
- `gamepanel/beammp_selection.py`
- `gamepanel/beammp.py`, uniquement le contrat de lecture de l'inventaire
- `tests/test_beammp_requirements_037.py`

## 2. Objectif

Corriger deux faux blocages dans la projection BeamMP sans toucher au fonctionnement du serveur, à la bibliothèque ZIP ni au système de sélection existant.

### R1 — Complétude limitée au périmètre utile

Actuellement, `complete` dépend de toutes les occurrences et de tous les avertissements.

Un ZIP illisible présent uniquement en bibliothèque peut donc rendre inconnues toutes les exigences Client, même lorsque les ZIP actifs sont correctement inventoriés.

Corriger :

- Distinguer la complétude des ressources actives de celle de la bibliothèque.
- Conserver les erreurs de bibliothèque dans les diagnostics.
- Ne pas dégrader les exigences actives à cause d'une erreur exclusivement inactive.
- Maintenir `unknown` pour tout ZIP actif illisible, non vérifié ou absent d'un inventaire réellement incomplet.
- Clarifier le contrat de confiance sur la complétude : le backend devra attester explicitement le périmètre actif. Ne jamais supposer qu'une liste partielle est complète.

### R2 — Conflits bloquants uniquement lorsqu'ils sont pertinents

Le catalogue actuel calcule certains conflits sur l'ensemble des ZIP, actifs et inactifs.

Distinguer :

- Conflit impliquant réellement plusieurs ZIP actifs : potentiellement bloquant.
- Conflit limité à un ZIP de bibliothèque inactif : diagnostic conservé, sans bloquer les contenus actifs.
- Collision de noms entre copies actives : conserver le traitement prudent.
- Déclaration de version ou métadonnées insuffisantes : ne pas inventer un verdict de compatibilité.

Préserver les conflits bruts pour la gestion de bibliothèque et produire, si nécessaire, une évaluation distincte des conflits affectant effectivement la distribution active.

Ne pas changer `beammp_catalog.py` ni ses contrats existants si l'adaptateur peut effectuer cette distinction sans modification du backend.

## 3. Tests ciblés

Ajouter les scénarios :

1. ZIP actifs sains et bibliothèque saine.
2. ZIP actifs sains et ZIP illisible uniquement en bibliothèque : exigences actives préservées.
3. ZIP actif illisible : inconnu conservé.
4. Inventaire actif réellement incomplet : inconnu.
5. Deux versions présentes, dont une seulement en bibliothèque : pas de faux conflit actif.
6. Versions incompatibles entre deux ZIP actifs : conflit conservé.
7. Niveau présent dans un ZIP actif et un ZIP inactif : diagnostic sans faux blocage.
8. Collision réelle entre ZIP actifs : conflit conservé.
9. Aucun téléchargement ni accès disque déclenché par la projection.
10. Aucun changement des données d'entrée ni des contrats de bibliothèque existants.

Rejouer les tests CP0, CP1-B et les tests existants directement concernés.

## 4. Interdictions

- ZÉRO GitHub Actions.
- Aucun serveur réel utilisé comme banc de test.
- Aucune mutation ZIP, modlist, carte, configuration ou SQLite.
- Aucun téléchargement ou préchargement de mods.
- Aucune nouvelle API ni modification du Launcher BeamMP.
- Aucun changement de `main`, BeamMP Votes ou PR #26.
- Aucun merge, tag, Release, nouvelle branche ou PR.
- Ne pas commencer Project Zomboid, Assetto Corsa ou CP2.

## 5. Livraison

Correction minimale, tests pertinents, documentation et états de continuité au strict nécessaire.

Actualiser `MANIFEST.sha256`.

Commit et push uniquement sur `work/0.3.7-content-comparison`.

Rapporter HEAD, fichiers modifiés, résultats des tests réellement exécutés et limites restantes.

**S'arrêter après CP1-B/R.**
~~~

## Réponse exacte

~~~text
**CP1-B/R est corrigé et poussé** sur `work/0.3.7-content-comparison`.

HEAD final : [`67fb1060ad6868da1ad3e754679a4e6e464350bf`](https://github.com/MrMekouil/GamePanel/commit/67fb1060ad6868da1ad3e754679a4e6e464350bf).

La projection sépare désormais la complétude de `Client` et celle de la bibliothèque. Les erreurs et conflits de bibliothèque restent visibles ; seuls les conflits démontrés entre ZIP actifs bloquent leur qualification. Une version insuffisamment documentée garde une évaluation inconnue.

Le backend devra fournir explicitement `active_inventory_complete` : l’ancien champ global `inventory_complete` n’est plus accepté comme preuve de complétude active.

**Tests locaux : 57 PASS** sous Windows/Python 3.13.2 : 25 tests CP0, 23 tests de projection et 9 tests existants de politique de sélection. Ces derniers ont été exécutés isolément, sans qualifier toute la suite POSIX/API.

Fichiers modifiés : `gamepanel/beammp_requirements.py`, son test, `docs/CONTENT_COMPARISON_037.md`, les deux états de continuité et `MANIFEST.sha256`. Les cinq empreintes modifiées sont vérifiées ; le manifeste complet n’a pas été revérifié sur tous les fichiers.

La capture backend authentifiée et la preuve réelle de distribution restent à qualifier. Aucune GitHub Actions ni intervention sur le serveur ; `main` et la PR #26 sont préservées. **Arrêt après CP1-B/R.**
~~~

## Synthèse enregistrée

Le commit GitHub confirme **six fichiers modifiés** : `gamepanel/beammp_requirements.py`, `tests/test_beammp_requirements_037.py`, `docs/CONTENT_COMPARISON_037.md`, `WORK_STATE.md`, `ASSISTANT_STATE.md`, `MANIFEST.sha256`.

- **R1 — Complétude :** selon Work, la projection distingue ressources Client actives et bibliothèque inactive. Les défauts exclusivement en bibliothèque demeurent des diagnostics sans dégrader les exigences actives. Le backend doit fournir explicitement `active_inventory_complete` ; `inventory_complete` global ne prouve pas la complétude active.
- **R2 — Conflits :** les conflits limités aux ZIP inactifs ne bloquent pas l'actif ; les collisions et contradictions démontrées entre ZIP actifs restent bloquantes ou incertaines. Aucune compatibilité n'est inventée pour des métadonnées insuffisantes.
- **Tests :** **57 PASS** rapportés par Work sous Windows Python 3.13.2 (25 CP0 + 23 projection + 9 sélection). Non rejoués indépendamment pour ce benchmark. Les neuf tests de sélection isolés ne remplacent pas la suite POSIX/API.
- **Empreintes :** cinq entrées ajoutées/modifiées contrôlées selon Work ; vérification intégrale du manifeste non effectuée.
- **Limites :** capture backend authentifiée et preuve réelle de distribution à qualifier, pas de validation sur serveur réel, pas de comparaison client.
- **Restrictions :** Work indique aucune GitHub Actions ni intervention serveur, `main` GamePanel et PR Votes #26 préservés ; vérification indépendante de ces affirmations non exhaustive.

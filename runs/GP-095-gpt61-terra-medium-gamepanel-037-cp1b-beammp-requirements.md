# GP-095 — GPT-6.1 Terra Medium — GamePanel 0.3.7 CP1-B

- Date d'enregistrement : **2026-11-01** (date d'exécution Work non précisée)
- Projet : **GamePanel**, branche `work/0.3.7-content-comparison`
- Modèle / effort : **GPT-6.1 Terra / Medium**
- Quota visible : **68 % → 57 % = 11 points**
- Durée : **4 min 57 s (297 secondes)**
- Statut : **succès du livrable CP1-B**, validation réelle du backend et de la distribution en attente
- Commit GamePanel vérifié : [`96b72e529cb27cf224b452b40a556ccd3d1226ad`](https://github.com/MrMekouil/GamePanel/commit/96b72e529cb27cf224b452b40a556ccd3d1226ad)

## Prompt exact

~~~text
# GamePanel 0.3.7 — CP1-B : qualification des exigences BeamMP

**Modèle recommandé : GPT-6.1 Terra — Medium**

## Références

- Dépôt privé : `MrMekouil/GamePanel`
- Branche existante : `work/0.3.7-content-comparison`
- HEAD attendu : `d4de42f4cf820f803fdebde7c79f84e1af16ce42`
- Stable `main` : `161360863ea7a6b19ccb80190588aae86831ddd1`
- CP0-A/B et CP1-A/R Minecraft livrés.

## 1. Prévol

Vérifier branche, HEAD, statut Git, diff, index et historique récent.

Lire les règles `AGENTS.md`, `WORK_STATE.md`, `docs/ASSISTANT_WORKFLOW.md` et le contrat `docs/CONTENT_COMPARISON_037.md`.

Examiner de façon ciblée :

- `gamepanel/content_requirements.py`
- `gamepanel/minecraft_requirements.py` pour les conventions du checkpoint précédent
- `gamepanel/beammp.py`
- `gamepanel/beammp_selection.py`
- `gamepanel/beammp_catalog.py`
- `gamepanel/beammp_api.py`
- `docs/BEAMMP_LIBRARY_0361.md`
- Tests BeamMP existants pertinents.

Ne pas effectuer de nouvel audit général.

## 2. Objectif

Développer une projection **strictement en lecture seule** des exigences BeamMP à partir d'un instantané cohérent et fiable de la configuration serveur.

L'objectif n'est pas de trouver tous les ZIP du serveur, mais de déterminer les ZIP réellement pertinents pour le joueur.

## 3. Règles obligatoires

### Contenus actifs et bibliothèque

- Distinguer `Resources/Client` actif des copies en bibliothèque.
- Conserver les identités SHA-256 + taille.
- Ne jamais déduire la nécessité d'un ZIP de son nom, de sa catégorie ou de sa présence en bibliothèque.
- Ne pas fusionner silencieusement les occurrences physiques distinctes.
- Conserver les conflits de noms, de versions et de contenu.

### Sélection et rôles

- Réutiliser les états existants `global`, `map_required`, `ambiguous`.
- Vérifier la cohérence entre carte sélectionnée, ZIP actifs, sélection enregistrée et révision.
- Ne pas inventer de rôle lorsqu'une sélection est ambiguë.
- Un changement de carte ou de modlist doit invalider l'analyse fondée sur l'ancien instantané.

### Distribution native BeamMP

- Utiliser `game_managed_on_join` uniquement lorsque la distribution par BeamMP est établie pour le contenu effectivement actif.
- Ne pas confondre « normalement distribué par BeamMP » et « déjà présent sur le client ».
- Ne pas déclarer un téléchargement réussi.
- Aucun préchargement, accès au cache Launcher ou manipulation de ZIP dans ce checkpoint.

### Contrat CP0

Produire des exigences compatibles avec `gamepanel/content_requirements.py`.

Conserver séparément pertinence, mode d'obtention, identité exacte, provenance, fraîcheur et contradictions.

Les observations incomplètes ou non fiables restent inconnues. Le contexte de confiance ne doit jamais être construit automatiquement à partir d'un JSON externe non authentifié.

AutoModpack est totalement hors périmètre.

## 4. Tests attendus

Créer des fixtures synthétiques pour :

1. ZIP actif et distribué.
2. ZIP présent uniquement en bibliothèque.
3. ZIP global et ZIP requis par la carte.
4. ZIP actif au rôle ambigu.
5. Carte vanilla sans ZIP de carte supplémentaire.
6. Changement de sélection ou révision périmée.
7. Copies exactes multiples.
8. Collisions de noms ou empreintes contradictoires.
9. Inventaire partiel ou ZIP illisible.
10. Absence de preuve de distribution.
11. Conservation des données d'entrée et absence d'effet de bord.

Exécuter les tests CP0 ciblés, les nouveaux tests BeamMP et les tests existants affectés.

## 5. Limites

- ZÉRO GitHub Actions.
- Aucun serveur de production utilisé comme banc de test.
- Aucun changement des ZIP, cartes, modlist ou fichiers de configuration.
- Pas de nouvelle API, téléchargement, synchronisation ou comparaison client.
- Aucun changement SQLite ou des contrats de gestion BeamMP 0.3.6.1.
- Pas de développement Project Zomboid, Assetto Corsa ou CP2.
- Ne toucher ni à `main`, ni à la branche BeamMP Votes / PR #26.
- Aucun merge, tag, release, nouvelle branche ou PR.

## 6. Livraison

Implémenter le plus petit module de projection BeamMP cohérent avec CP0.

Actualiser `docs/CONTENT_COMPARISON_037.md`, les états de continuité et `MANIFEST.sha256`.

Commit et push uniquement sur `work/0.3.7-content-comparison`.

Rapporter commit, fichiers modifiés, tests réellement exécutés, limites restantes et preuves de non-mutation.

**S'arrêter après CP1-B.**
~~~

## Réponse exacte

~~~text
**CP1-B est livré** sur `work/0.3.7-content-comparison`.

HEAD final : [`96b72e529cb27cf224b452b40a556ccd3d1226ad`](https://github.com/MrMekouil/GamePanel/commit/96b72e529cb27cf224b452b40a556ccd3d1226ad).

La projection distingue les ZIP Client actifs des copies de bibliothèque, conserve leurs occurrences et leurs rôles, et utilise CP0 pour les qualifier. Elle exige une preuve de distribution distincte et des révisions cohérentes ; les rôles ambigus, collisions et inventaires partiels restent incertains.

**Tests locaux : 47 PASS** sous Windows/Python 3.13.2 : 25 tests CP0, 13 nouveaux tests de projection et 9 tests existants de politique de sélection. Ces neuf derniers ont été exécutés isolément ; ils ne remplacent pas la suite POSIX/API. Le test de non-mutation vérifie les entrées, une base SQLite temporaire et l’absence d’accès fichier ou réseau pendant la projection.

Les fichiers livrés sont `gamepanel/beammp_requirements.py`, son test, `docs/CONTENT_COMPARISON_037.md`, les deux états de continuité et `MANIFEST.sha256`. Les cinq empreintes modifiées sont vérifiées ; le manifeste complet n’a pas été revérifié sur tous les fichiers.

La capture backend authentifiée et la preuve réelle de distribution restent à implémenter et qualifier. Aucun serveur réel ni GitHub Actions utilisé ; `main` et la PR #26 sont préservées. **Arrêt après CP1-B.**
~~~

## Synthèse enregistrée

Le commit GitHub confirme **six fichiers modifiés** : `gamepanel/beammp_requirements.py`, `tests/test_beammp_requirements_037.py`, `docs/CONTENT_COMPARISON_037.md`, `WORK_STATE.md`, `ASSISTANT_STATE.md` et `MANIFEST.sha256`.

- **Périmètre livré selon Work :** projection BeamMP en lecture seule, distinguant ZIP réellement actifs dans `Resources/Client` et copies de bibliothèque, occurrences physiques, rôle `global`/`map_required`/`ambiguous`, SHA-256 + taille, preuve de distribution indépendante et révisions cohérentes. Les conflits, ambiguïtés, collisions et relevés partiels demeurent inconnus/incertains.
- **Tests rapportés :** **47 PASS sous Windows/Python 3.13.2** (25 CP0, 13 nouveaux tests BeamMP, 9 tests existants de sélection isolés). Non rejoués par le gestionnaire du benchmark. Les neuf tests de sélection isolés ne remplacent pas la suite POSIX/API.
- **Non-mutation rapportée :** les entrées, une base SQLite temporaire, l’absence d’accès fichier et d’accès réseau durant la projection ont été contrôlées selon Work ; pas de banc de test sur le serveur de production.
- **Empreintes :** cinq entrées de `MANIFEST.sha256` ajoutées ou modifiées ont été vérifiées selon Work ; pas de vérification intégrale du manifeste.
- **Limites :** capture backend authentifiée et preuve réelle de distribution BeamMP restent à développer et qualifier. La projection ne compare aucun fichier client et ne valide pas de téléchargement. Aucun travail CP2 ni autre jeu.
- **Restrictions :** Work rapporte absence de GitHub Actions, de mutation du serveur, de merge ou PR et conservation de `main` / PR #26. Ces déclarations ne sont pas toutes vérifiables à partir du seul commit.

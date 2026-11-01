# GP-093 — GPT-6.1 Terra Medium — GamePanel 0.3.7 CP1-A

- Date d'enregistrement : **2026-11-01** (date réelle de la session Work non communiquée)
- Projet : **GamePanel**
- Modèle / effort : **GPT-6.1 Terra / Medium**
- Quota visible : **83 % → 72 % = 11 points**
- Durée : **5 min 13 s (313 secondes)**
- Statut : **succès de livraison CP1-A**, projection Minecraft/Forge en lecture seule ; validation réelle avec backend non acquise
- Commit GamePanel vérifié : [`80658645d95a76571fb13c3bcef4c8eccd89c56a`](https://github.com/MrMekouil/GamePanel/commit/80658645d95a76571fb13c3bcef4c8eccd89c56a)
- Branche du projet source : `work/0.3.7-content-comparison`

## Prompt exact

~~~text
# GamePanel 0.3.7 — CP1-A : exigences serveur Minecraft

**Modèle conseillé : GPT-6.1 Terra — Medium**

## Références

Dépôt privé : `MrMekouil/GamePanel`

Branche existante : `work/0.3.7-content-comparison`

HEAD attendu : `db5864d3484d089a22734ab74ff71a62f4d2fe1a`

Stable `main` : `161360863ea7a6b19ccb80190588aae86831ddd1`

CP0-A/B livrés : contrat `gamepanel/content_requirements.py`, 25 tests synthétiques PASS déclarés.

## 1. Prévol

Vérifier branche, HEAD, statut Git, diffs, index et historique récent. Conserver tout travail préexistant.

Lire de façon ciblée :

- `AGENTS.md`
- `WORK_STATE.md`
- `docs/ASSISTANT_WORKFLOW.md`
- `docs/CONTENT_COMPARISON_037.md`
- `gamepanel/content_requirements.py`
- `gamepanel/content_manifest.py`
- `gamepanel/content_publication.py`
- `gamepanel/content_delivery.py`
- `gamepanel/content_admin.py`

Réutiliser les contrats et tests existants. Pas d'audit global.

## 2. Objectif

Implémenter une **projection en lecture seule des exigences Minecraft/Forge**, à partir des manifestes GamePanel déjà publiés et validés.

Il s'agit de déterminer ce que le client doit posséder avant de rejoindre, sans comparer encore ses fichiers locaux.

### Exigences fonctionnelles

1. Distinguer explicitement observation serveur, brouillon, publication, publication sélectionnée et publication révoquée.
2. Vérifier la provenance et l'identité du manifeste avant toute qualification.
3. Ne jamais déclarer qu'un contenu est requis uniquement parce qu'il existe dans le dossier `mods` du serveur.
4. Respecter les champs existants `environment`, `client_policy`, `distribution`, `dependencies` et `evidence`, sans inventer de qualification VERIFIED.
5. Distinguer requis, recommandé, facultatif, non applicable et inconnu.
6. Conserver les dépendances, conflits et décisions administrateur avec leur provenance.
7. Distinguer les fichiers distribuables par GamePanel, externes et indisponibles.
8. Une publication ancienne mais toujours sélectionnée doit être traitée selon une règle de fraîcheur explicite ; ne pas assimiler automatiquement sa date de création à une observation actuelle.
9. Aucune publication disponible ne signifie pas « aucun mod nécessaire » : conserver un état inconnu.
10. Aucun rapprochement avec AutoModpack ni dépendance à celui-ci.

### Intégration CP0

Utiliser le contrat de qualification CP0-A/B sans le contourner.

Construire le contexte de confiance uniquement après validation des identités et de la provenance. Ne jamais approuver automatiquement les empreintes de toutes les déclarations reçues.

Séparer l'obligation administrative de la classification technique : un choix Admin valide ne transforme pas une déclaration fournisseur UNKNOWN en VERIFIED.

Ne pas confondre la version du manifeste, la version Minecraft/Forge et la version commerciale d'un mod.

## 3. Tests

Utiliser des fixtures synthétiques et les composants existants, sans serveur réel.

Tester notamment :

- Publication valide et sélectionnée.
- Absence de publication.
- Publication révoquée ou incohérente.
- Brouillon non publié.
- Contenu requis et contenu optionnel.
- Contenu externe ou indisponible.
- Dépendances et classifications inconnues.
- Mod serveur uniquement.
- Conflit de provenance ou de version.
- Fraîcheur, révisions et changement de publication.
- Aucune modification SQL ou fichier.

Rejouer les 25 tests CP0 ainsi que les nouveaux tests ciblés. Ne pas lancer inutilement toutes les suites.

## 4. Limites

- ZÉRO GitHub Actions.
- Aucune nouvelle API ni connexion Windows/Web.
- Aucun inventaire client ni téléchargement.
- Aucun changement du schéma SQLite 5 ou du manifeste v1.
- Aucune action sur le serveur Ubuntu, les JAR, ZIP ou sauvegardes.
- Aucun changement de `main` ni de `work/beammp-votes-in-game` / PR #26.
- Aucun merge, tag, Release, PR ou nouvelle branche.
- Ne pas commencer BeamMP, Project Zomboid, Assetto Corsa ni CP2.

## 5. Livraison

Implémenter le plus petit adaptateur réellement testable.

Actualiser le contrat 0.3.7, les états de continuité et `MANIFEST.sha256`.

Commit et push exclusivement sur `work/0.3.7-content-comparison`.

Rapporter HEAD, fichiers modifiés, résultats de tests exécutés, limites et validations encore nécessaires.

**S'arrêter après CP1-A.**
~~~

## Réponse exacte

~~~text
**CP1-A est livré** sur `work/0.3.7-content-comparison`.

Commit final : [`80658645d95a76571fb13c3bcef4c8eccd89c56a`](https://github.com/MrMekouil/GamePanel/commit/80658645d95a76571fb13c3bcef4c8eccd89c56a).

La projection Minecraft/Forge vérifie l’identité de la publication sélectionnée, le manifeste et le brouillon approuvé avant d’utiliser CP0. Elle conserve séparément les preuves techniques, les décisions administrateur, les dépendances et les distributions. Une publication absente, révoquée ou périmée ne devient pas une liste de besoins vide et certaine.

Fichiers modifiés : `gamepanel/minecraft_requirements.py`, son test `tests/test_minecraft_requirements_037.py`, les deux états de continuité, `docs/CONTENT_COMPARISON_037.md` et `MANIFEST.sha256`.

**Validation locale : 42 PASS** sous Windows/Python 3.13.2 : 25 tests CP0 et 17 tests CP1-A synthétiques. Les empreintes des cinq fichiers modifiés ou ajoutés sont vérifiées ; le manifeste complet n’a pas été revérifié sur tous les fichiers du dépôt.

La projection attend encore une capture backend authentifiée et cohérente. Son intégration réelle, notamment face à une révocation concurrente, reste à qualifier. Elle ne vérifie pas la présence des fichiers côté client.

Aucune GitHub Actions ni intervention sur Ubuntu. `main` et la PR #26 sont préservées. **Arrêt après CP1-A.**
~~~

## Synthèse enregistrée

Le commit GitHub confirme **six fichiers** : `gamepanel/minecraft_requirements.py`, `tests/test_minecraft_requirements_037.py`, `docs/CONTENT_COMPARISON_037.md`, `WORK_STATE.md`, `ASSISTANT_STATE.md`, `MANIFEST.sha256`.

- **Portée déclarée par Work :** projection Minecraft/Forge en lecture seule à partir de publications sélectionnées validées. La qualification préserve la séparation entre origine de publication, preuve technique et choix administrateur, dépendances, distributions et inconnus. Absence/révocation/péremption ne sont jamais assimilées à l'absence certaine de besoins.
- **Tests rapportés par Work :** Windows / Python 3.13.2, **42 PASS**, dont **25 CP0** et **17 nouveaux scénarios CP1-A** ; ils n'ont pas été rejoués par le gestionnaire du benchmark.
- **Empreintes :** contrôle des cinq fichiers ajoutés ou modifiés selon Work, **pas de vérification complète de MANIFEST.sha256**.
- **Limites :** capture backend authentifiée et cohérente encore nécessaire ; révocation concurrente non qualifiée en conditions réelles ; aucune vérification des fichiers présents côté client. CP2 et autres jeux non démarrés selon le prompt.
- **Restrictions :** Work déclare aucune GitHub Actions et aucune intervention Ubuntu, `main` et PR #26 inchangées. Le commit seul n'établit pas tous ces points de façon indépendante.

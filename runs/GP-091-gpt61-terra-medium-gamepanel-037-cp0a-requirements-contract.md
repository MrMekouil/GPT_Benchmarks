# GP-091 — GPT-6.1 Terra Medium — GamePanel 0.3.7 CP0-A

- Date d'enregistrement : **2026-11-01** (date exacte de l'exécution Work non indiquée)
- Projet : **GamePanel**
- Modèle / effort : **GPT-6.1 Terra / Medium**
- Quota visible : **100 % → 90 % = 10 points**
- Durée : **4 min 05 s (245 secondes)**
- Statut : **succès du livrable CP0-A**, pas validation de CP0 dans son ensemble
- Commit GamePanel vérifié : [`d0e3ba304758723e3d804f2705801ba2effec318`](https://github.com/MrMekouil/GamePanel/commit/d0e3ba304758723e3d804f2705801ba2effec318)
- Branche source : `work/0.3.7-content-comparison`

## Prompt exact

~~~text
# GamePanel 0.3.7 — CP0-A : contrat de qualification des besoins

**Modèle recommandé : GPT-6.1 Terra — Medium**

## Références

- Dépôt privé : `MrMekouil/GamePanel`
- Branche existante : `work/0.3.7-content-comparison`
- HEAD attendu : `21c7dca37ed4d92ea45b93d49138ca6ad2c04aff`
- Stable `main` : `161360863ea7a6b19ccb80190588aae86831ddd1`
- Ne créer aucune branche ni PR.

## Prévol ciblé

Vérifier branche, HEAD, statut Git, diff, index et historique récent. Préserver tout travail présent.

Lire uniquement les sections pertinentes de :

- `AGENTS.md`
- `WORK_STATE.md`
- `docs/ASSISTANT_WORKFLOW.md`
- `docs/CONTENT_COMPARISON_037.md`
- `gamepanel/content_manifest.py`
- `gamepanel/content_schema.py`

Élargir les lectures uniquement si nécessaire. Ne pas effectuer d'audit global du dépôt.

## Mission

Implémenter la première fondation technique de CP0 : un **contrat versionné, pur et vérifiable**, permettant de qualifier les besoins client indépendamment de la comparaison des fichiers.

Séparer impérativement :

1. **Pertinence** : requis côté client, facultatif, serveur uniquement, non applicable, inconnu.
2. **Mode d'obtention** : requis avant connexion, géré par le jeu lors de la connexion, externe, non requis, inconnu.
3. **Preuves** : jeu, serveur, provenance, identifiants, déclarations, version, date, couverture et niveau de confiance.
4. **Constat local** : réservé au comparateur ultérieur ; ne pas assimiler la qualification du besoin à la présence effective d'un fichier.

### Règles obligatoires

- Commencer par les besoins du jeu et du serveur, puis seulement comparer les contenus pertinents.
- Minecraft/Forge, BeamMP, Project Zomboid et Assetto Corsa doivent pouvoir recevoir des politiques distinctes.
- Ne pas coder en dur qu'un mod est nécessaire uniquement en raison de son jeu ou de son extension.
- Pour BeamMP, distinguer bibliothèque ZIP et contenu réellement actif/distribué.
- Un contenu géré par le jeu n'est pas automatiquement installé ni vérifié.
- Toute preuve insuffisante ou contradictoire doit conserver un état inconnu/conflit.
- **AutoModpack est exclu de l'architecture et ne doit pas être utilisé comme source.**
- Préserver les contrats existants des manifestes GamePanel v1 et le schéma SQLite 5.

## Livraison limitée

Créer un petit module indépendant pour le contrat de données et sa validation, avec tests unitaires synthétiques couvrant les catégories, contradictions, entrées incomplètes et cas non pris en charge.

Actualiser `docs/CONTENT_COMPARISON_037.md` et les états de continuité au strict nécessaire. Mettre à jour `MANIFEST.sha256`.

**Ne pas implémenter CP1, CP2, CP3, l'interface Windows ou une nouvelle API.**

## Interdictions

- ZÉRO GitHub Actions.
- Aucun téléchargement, déploiement, changement de configuration, mutation SQLite, modification de mods ou de ZIP.
- Aucun merge, tag, release, nouvelle branche ou PR.
- Ne pas toucher à `main` ni à `work/beammp-votes-in-game` / PR #26.
- Aucun scan massif, aucune compilation Windows inutile, aucune suite complète répétée.
- Ne pas augmenter les droits ni modifier les mécanismes de récupération de la 0.3.6.1.

## Validation et arrêt

Exécuter les tests ciblés localement lorsque l'environnement le permet. Si l'exécution est impossible, le signaler sans prétendre au PASS.

Commit et push uniquement sur `work/0.3.7-content-comparison`.

S'arrêter après CP0-A et transmettre :

- Commit final.
- Fichiers modifiés.
- Tests réellement exécutés et résultats.
- Limites ou points nécessitant un audit approfondi.

Ne pas poursuivre automatiquement sur CP0-B ou CP1.
~~~

## Réponse exacte

~~~text
**CP0-A est implémenté et poussé** sur `work/0.3.7-content-comparison`.

Commit final : [`d0e3ba304758723e3d804f2705801ba2effec318`](https://github.com/MrMekouil/GamePanel/commit/d0e3ba304758723e3d804f2705801ba2effec318).

Le contrat sépare la pertinence, le mode d’obtention et les preuves. Il conserve les états inconnus ou contradictoires, distingue la bibliothèque BeamMP du contenu actif distribué et ne produit aucun constat de présence locale. AutoModpack est exclu.

Fichiers livrés :

- `gamepanel/content_requirements.py` et `tests/test_content_requirements_037.py`
- `docs/CONTENT_COMPARISON_037.md`, `WORK_STATE.md`, `ASSISTANT_STATE.md`
- `MANIFEST.sha256`

**Validation locale sous Windows, Python 3.13.2 : 12 tests synthétiques PASS**, plus contrôle de syntaxe. Les cinq empreintes ajoutées ou modifiées dans le manifeste sont vérifiées ; le manifeste complet n’a pas été vérifié sur tous les octets du dépôt.

Les politiques métier propres à chaque jeu, ainsi que la vérification de l’authenticité et de la fraîcheur des preuves, restent à développer et auditer. CP0 dans son ensemble n’est donc pas terminé.

L’ancien checkout local et ses modifications ont été préservés. Aucune GitHub Actions exécutée ; `main` et la PR #26 restent inchangées. **Arrêt après CP0-A.**
~~~

## Synthèse enregistrée

Le commit GitHub confirme **six fichiers** modifiés : `gamepanel/content_requirements.py`, `tests/test_content_requirements_037.py`, `docs/CONTENT_COMPARISON_037.md`, `WORK_STATE.md`, `ASSISTANT_STATE.md` et `MANIFEST.sha256`.

- **Portée livrée selon Work :** contrat versionné séparant pertinence, mode d'obtention et preuves, sans attribuer une présence locale ou une installation effective. Gestion des inconnus/conflits et distinction BeamMP ZIP bibliothèque / contenu actif ; AutoModpack exclu.
- **Tests rapportés par Work :** Windows Python 3.13.2, **12/12 tests synthétiques PASS** et contrôle de syntaxe. Non rejoués par le gestionnaire du benchmark.
- **Empreintes :** cinq entrées de manifeste modifiées ou ajoutées contrôlées selon Work, **pas** vérification intégrale de tous les octets du dépôt.
- **Limites :** politiques de chaque jeu et authenticité/fraîcheur des preuves restant à traiter ; **CP0 complet NON ACQUIS**. Aucun CP0-B, CP1, CP2, CP3, Windows UI ou API ajouté durant ce run selon Work.
- **Interdictions :** Work rapporte aucune GitHub Actions, PR, merge ou release ; pas de vérification indépendante de tous ces points à partir du commit seul.

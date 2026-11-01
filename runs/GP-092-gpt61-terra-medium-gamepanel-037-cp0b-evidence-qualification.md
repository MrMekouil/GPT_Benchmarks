# GP-092 — GPT-6.1 Terra Medium — GamePanel 0.3.7 CP0-B

- Date d'enregistrement : **2026-11-01** (date d'exécution Work non indiquée)
- Projet : **GamePanel**
- Modèle / effort : **GPT-6.1 Terra / Medium**
- Quota visible : **90 % → 83 % = 7 points**
- Durée : **4 min 45 s (285 secondes)**
- Statut : **succès de livraison CP0-B**, pas de validation complète des futurs adaptateurs métier
- Commit GamePanel vérifié : [`db5864d3484d089a22734ab74ff71a62f4d2fe1a`](https://github.com/MrMekouil/GamePanel/commit/db5864d3484d089a22734ab74ff71a62f4d2fe1a)
- Branche source : `work/0.3.7-content-comparison`

## Prompt exact

~~~text
# GamePanel 0.3.7 — CP0-B : fiabilisation des preuves et qualification des besoins

**Modèle : GPT-6.1 Terra — Medium**

## Références

- Dépôt privé : `MrMekouil/GamePanel`
- Branche existante : `work/0.3.7-content-comparison`
- HEAD attendu : `d0e3ba304758723e3d804f2705801ba2effec318`
- Stable `main` : `161360863ea7a6b19ccb80190588aae86831ddd1`
- Dernier checkpoint : CP0-A livré, 12 tests synthétiques PASS annoncés.

Aucune nouvelle branche ni PR.

## 1. Prévol

Vérifier branche, HEAD, `git status`, `git diff`, `git diff --cached` et les derniers commits.

Lire de manière ciblée :

- `AGENTS.md`
- `WORK_STATE.md`
- `docs/ASSISTANT_WORKFLOW.md`
- `docs/CONTENT_COMPARISON_037.md`
- `gamepanel/content_requirements.py`
- `tests/test_content_requirements_037.py`
- `gamepanel/content_manifest.py`, uniquement les contrats pertinents.

Ne pas refaire d'audit global.

## 2. Mission

Corriger les deux limitations identifiées pendant l'audit indépendant de CP0-A, sans développer CP1.

### A — Fiabilité des déclarations

Actuellement, une déclaration `verified/complete` peut qualifier un contenu comme obligatoire même lorsque sa source concerne seulement une capacité générale du jeu.

Corriger cette situation :

- Une capacité générale du jeu ne prouve jamais, à elle seule, une exigence d'un serveur particulier.
- Une déclaration liée au serveur doit avoir une provenance et un périmètre admissibles pour l'axe qu'elle qualifie.
- Les contenus BeamMP en bibliothèque ne doivent jamais être assimilés aux contenus actifs et distribués.
- Une contradiction ne doit jamais être résolue arbitrairement.
- Les champs `verified` et `complete` provenant de données externes ne constituent pas, à eux seuls, une preuve d'authenticité. Documenter et imposer une frontière de confiance explicite aux futurs adaptateurs.

Préserver la distinction entre pertinence client, mode d'obtention et identité des fichiers.

### B — Versions facultatives et preuves exactes

Actuellement, une version déclarée est obligatoire pour qualifier une preuve.

Ce comportement est trop strict pour les contenus dont la version est absente, notamment certains ZIP BeamMP.

- Permettre une qualification lorsque la version commerciale manque, mais qu'une preuve d'identité et de provenance suffisante existe.
- Prévoir la liaison exacte SHA-256 + taille lorsqu'il s'agit d'un fichier.
- Distinguer la version du contenu, l'identité de ses octets et la révision de l'observation.
- Une version seule ne prouve jamais l'égalité des fichiers.
- Une empreinte seule ne prouve pas qu'un fichier est nécessaire au client.
- Conserver `unknown` lorsque les preuves sont insuffisantes.

### C — Fraîcheur des preuves

Préciser le traitement des instantanés périmés ou incohérents :

- Ne pas accepter silencieusement une observation future ou périmée comme preuve actuelle.
- Garder le moteur pur et déterministe, sans dépendance implicite à l'horloge système.
- Les règles de fraîcheur doivent être explicites et testables, sans seuil arbitraire unique pour tous les jeux.

Ne pas inventer de preuve serveur réelle.

## 3. Tests attendus

Conserver les 12 tests CP0-A et ajouter les cas suivants :

1. Capacité générale du jeu déclarant abusivement un mod obligatoire.
2. Preuve réellement liée au serveur.
3. ZIP BeamMP sans version mais avec identité exacte.
4. Empreinte exacte sans preuve d'obligation client.
5. Déclarations contradictoires et résultats indépendants de leur ordre.
6. Observation périmée ou future.
7. Source inconnue ou non authentifiée.
8. Aucun changement des données d'entrée et aucun effet de bord.

Tests synthétiques uniquement, avec résultats PASS/FAIL réels.

## 4. Limites impératives

- ZÉRO GitHub Actions.
- Aucun nouveau endpoint HTTP, adaptateur complet, scan Windows ou moteur de comparaison.
- Aucun téléchargement, synchronisation ou écriture de fichiers de jeux.
- Aucun changement du schéma SQLite 5 ni du manifeste GamePanel v1.
- AutoModpack exclu de l'architecture.
- Ne pas toucher à `main`, à la PR Votes #26 ni au serveur Ubuntu.
- Aucun merge, tag, release ou nouvelle branche.
- Ne pas démarrer CP1.

## 5. Livraison

Limiter les modifications au module de qualification, à ses tests et aux documents de continuité nécessaires.

Exécuter les tests ciblés localement. Actualiser `MANIFEST.sha256`.

Commit et push sur `work/0.3.7-content-comparison` uniquement.

Restituer brièvement :

- HEAD final et commit.
- Modifications apportées.
- Tests exécutés et résultats.
- Limites restant à traiter.
- Confirmation d'arrêt après CP0-B.

**Objectif : terminer la fondation CP0 sans anticiper les adaptateurs métier ni la comparaison.**
~~~

## Réponse exacte

~~~text
**CP0-B est livré** sur `work/0.3.7-content-comparison`.

Commit final : [`db5864d3484d089a22734ab74ff71a62f4d2fe1a`](https://github.com/MrMekouil/GamePanel/commit/db5864d3484d089a22734ab74ff71a62f4d2fe1a).

Le contrat exige désormais un contexte de confiance extérieur aux déclarations et une règle de fraîcheur explicite. Une capacité générale du jeu ne qualifie plus un besoin serveur. Un fichier sans version peut être qualifié avec son **SHA-256 et sa taille** ; les preuves contradictoires restent en conflit.

**Tests locaux : 25 PASS** sous Windows et Python 3.13.2, dont les 12 scénarios CP0-A. Les cinq empreintes modifiées du manifeste sont vérifiées ; le manifeste complet n’a pas été revérifié sur tous les fichiers.

Les futurs adaptateurs devront encore authentifier leurs sources et définir les durées de validité adaptées. Le module ne réalise pas lui-même cette authentification.

Aucune GitHub Actions ni intervention sur Ubuntu. `main` et la PR #26 sont préservées. **Arrêt après CP0-B ; CP1 n’a pas été commencé.**
~~~

## Synthèse enregistrée

Le commit GitHub confirme **six fichiers** modifiés : `gamepanel/content_requirements.py`, `tests/test_content_requirements_037.py`, `docs/CONTENT_COMPARISON_037.md`, `WORK_STATE.md`, `ASSISTANT_STATE.md` et `MANIFEST.sha256`.

- **Portée livrée selon Work :** frontière de confiance externe aux déclarations ; capacité générale d'un jeu insuffisante pour qualifier un besoin serveur ; distinction pertinence/obtention/identité, SHA-256 + taille autorisés sans version commerciale, contradiction non arbitrairement résolue, règle de fraîcheur explicite et moteur déterministe.
- **Tests rapportés par Work :** Windows Python 3.13.2, **25 tests PASS**, dont les **12 scénarios CP0-A**. Non rejoués par le gestionnaire du benchmark.
- **Empreintes :** cinq entrées du manifeste modifiées et vérifiées selon Work, **pas** de vérification intégrale du manifeste ni de tous les octets du dépôt.
- **Limites :** l'authentification des sources et le choix des durées de validité adaptées restent aux futurs adaptateurs ; le module n'authentifie pas lui-même ses sources ; **CP1 non commencé**. Le statut de réussite de CP0-B ne constitue pas une validation réelle indépendante de l'ensemble du système.
- **Interdictions :** Work rapporte aucune GitHub Actions ni action sur Ubuntu, `main` et PR #26 inchangées ; non vérifié indépendamment dans son intégralité.

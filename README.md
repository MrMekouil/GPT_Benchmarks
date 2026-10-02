# GPT Benchmarks

Benchmarks empiriques de modèles OpenAI utilisés sur des tâches réelles du projet **GamePanel**.

L'objectif n'est pas de produire un classement universel, mais de mesurer le **coût par tâche réellement réussie** dans Work/Codex : qualité, autonomie, fiabilité, durée et consommation visible du quota.

## Fichiers

- `data/runs.csv` — données tabulaires, faciles à analyser.
- `data/runs.json` — mêmes runs avec des champs plus riches.
- `RUN_LOG.md` — journal détaillé avec prompts/réponses lorsque disponibles.

## Important sur la mesure du quota

La consommation est relevée depuis l'interface ChatGPT/Work en **points de pourcentage visibles**.

Ce n'est **pas** une mesure exacte de tokens :

- l'affichage peut être arrondi ;
- une valeur `~0` signifie que le quota visible n'a pas bougé ;
- certaines valeurs sont approximatives lorsque seul le delta a été observé ;
- les runs de complexité différente ne doivent pas être comparés comme s'ils étaient des A/B tests.

La métrique la plus utile est donc :

> **quota visible consommé pour une tâche correctement terminée**

## Synthèse par modèle

Vue regroupée par modèle/effort, classée dans l'ordre logique des générations. Les moyennes ne sont indicatives que lorsque les tâches sont suffisamment comparables.

| Génération | Modèle | Effort | Runs observés | Résultats | Quota visible observé | Durée cumulée |
|---|---|---|---:|---|---|---:|
| 5.6 | **GPT-5.6 Sol** | Medium | 1 | **1 succès** | **6 pts** au total · 6 pts/succès | **1:50** |
| 6.0 | **GPT-6 Luna** | Medium* | 9 | **6 succès · 1 échec · 2 blocages** | **≥7 pts connus*** | **1:58:00** |
| 6.0 | **GPT-6 Sol** | Medium | 6 | **6 succès** | **~52 pts** au total · ~8,67 pts/run | **32:03** |
| 6.0 | **GPT-6 Sol** | High | 1 | **1 partiel** | **~20 pts** | **12:07** |
| 6.0 | **GPT-6 Astra** | Low | 2 | **2 succès** | **30 pts** au total · 15 pts/run | **2:52** |
| 6.1 | **GPT-6.1 Sol** | Medium | 5 | **4 succès · 1 bloqué** | **40 pts** au total · 35 succès + 5 bloqué | **52:24** |

### Repères rapides

- **A/B historique le plus propre :** GPT-6 Sol Medium = 4 pts, GPT-5.6 Sol Medium = 6 pts, GPT-6 Astra Low = 17 pts pour le même diagnostic principal.
- **A/B fonctionnel :** GPT-6 Sol Medium = 4 pts contre GPT-6 Astra Low = 13 pts, avec la même lacune principale trouvée.
- **GPT-6 Sol Medium en production :** deux gros checkpoints complets observés à **11 pts / 8:42** (pré-clôture) puis **22 pts / 14:13** (audit transversal d’architecture 0.3.1-E-A). Le coût varie donc fortement avec la profondeur et le périmètre.
- **GPT-6.1 Sol Medium :** 4 tâches de production terminées sur 5 tentatives observées. Les quatre succès consomment 3 à 11 pts ; GP-021 a consommé **5 pts / 4:31** puis s’est arrêté avant implémentation, faute d’environnement Linux/POSIX permettant les tests crash/locks exigés.
- **GPT-6 Luna Medium :** six succès ciblés observés, dont cinq vrais checkpoints de production récents. Ces cinq checkpoints totalisent **2 points visibles** pour **21:49**. GP-023 est un vrai correctif installateur à **~0 pt visible / 3:32**, avec 17 tests PASS dans Work ; les suites Linux restent à revalider sur Ubuntu. Deux longues sessions bloquées ont aussi été observées. *L'effort des deux incidents n'avait pas été relevé ; un incident n'a pas de mesure de quota.*

## Résultats actuellement observés

### A/B les plus propres

| Test | Modèle | Effort | Quota visible | Durée | Résultat |
|---|---|---|---:|---:|---|
| 2 bugs historiques `root/selected_root` | GPT-5.6 Sol | Medium | 6 pts | 1:50 | 2/2 bugs |
| idem | GPT-6 Luna | Medium | ~0 pt | 0:31 | échec avant audit |
| idem | GPT-6 Sol | Medium | 4 pts | 1:35 | 2/2 bugs |
| idem | GPT-6 Astra | Low | 17 pts | 1:42 | 2/2 bugs + preuve plus détaillée |
| lacune fonctionnelle 0.3.0 | GPT-6 Sol | Medium | 4 pts | 1:45 | lacune exacte trouvée |
| idem | GPT-6 Astra | Low | 13 pts | 1:10 | même lacune + preuve plus détaillée |

### Run réel GPT-6 Sol Medium

| Run | Tâche | Quota visible | Durée | Résultat |
|---|---|---:|---:|---|
| GP-018 | Pré-clôture 0.3.1 : audit global, versions, critères de sortie, tests/docs/manifeste | **11 pts** | **8:42** | terminé, commit `3de9d3a...` |
| GP-020 | 0.3.1-E-A : audit identité d’instance, persistances, contrat rename/recovery | **22 pts** | **14:13** | terminé, commit `1a83550...` |
| GP-024 | Clôture documentaire B1 après validation Ubuntu complète | **6 pts** | **3:21** | terminé, commit `ca16063...` |

GP-024 est à lire séparément des deux gros checkpoints : il enregistre des validations Ubuntu déjà acquises et ne contient aucune implémentation fonctionnelle.

### Runs réels GPT-6 Luna Medium

| Run | Tâche | Quota visible | Durée | Résultat |
|---|---|---:|---:|---|
| GP-016 | Palette Utilisateurs scopée `.users-page` + test/manifeste | **1 pt** | **3:42** | terminé, commit `5049d50...` |
| GP-017 | Journal d’audit : palette graphite + responsive cartes mobile + contrat/manifeste | **~0 pt visible** | **7:47** | terminé, commit `4966b61...` |
| GP-019 | Validation documentaire finale 0.3.1 + BeamMP réel + manifeste | **~0 pt visible** | **3:19** | terminé, commit `92df2a3...` |
| GP-022 | B1c : correction du fixture no-op root, sans code de production | **1 pt** | **3:29** | terminé, commit `3c6c7e1...` |
| GP-023 | B1d : compatibilité installateur historique `write_inventory/aliases` + tests | **~0 pt visible** | **3:32** | terminé, commit `45d4a38...` |

Ces cinq runs sont de vrais checkpoints de production Luna terminés après les incidents de fiabilité observés : **5/5 réussis**, **2 points visibles cumulés**, **21:49** au total.

### Runs réels GPT-6.1 Sol Medium

| Run | Tâche | Quota visible | Durée | Résultat |
|---|---|---:|---:|---|
| 1 | UI Instances : densification candidats + conflit/logout + tests/manifeste | 11 pts | 18:37 | terminé, commit `7ba38960...` |
| 2 | UI Supervision : compaction + responsive + diagnostic/logout + tests/manifeste | 10 pts | 10:42 | terminé, commit `622205de...` |
| 3 | UI Utilisateurs : tableau/modales + Accès + tests/manifeste | 11 pts | 12:42 | terminé, commit `c9186373...` |
| 4 | Correctif Sessions : READY/OFFLINE + test/manifeste | 3 pts | 5:52 | terminé, commit `de76ac3` |
| GP-021 | 0.3.1-E-B1 : primitive transactionnelle rename + recovery/tests POSIX | **5 pts** | **4:31** | **bloqué avant implémentation**, aucun commit |

Cumul GPT-6.1 Sol Medium à ce stade : **40 points**, **52 min 24 s**, **4 succès / 1 blocage**. Les quatre tâches terminées représentent **35 points** ; GP-021 représente **5 points** de coût sans implémentation livrée.

## Lecture provisoire

- **GPT-6 Luna Medium** : peut être extrêmement économique sur une analyse locale très bornée, mais plusieurs problèmes de fiabilité/exécution ont aussi été observés. Ne pas confondre qualité de raisonnement et fiabilité de la session Work.
- **GPT-6 Sol Medium** : six succès observés. Les audits ciblés sont à 4 pts, les gros checkpoints à 11–22 pts, et la clôture documentaire B1 à 6 pts. Le coût suit fortement la nature réelle du travail, pas seulement sa durée.
- **GPT-6 Sol High** : un gros run multi-étapes a consommé ~20 points en 12:07 et s'est arrêté faute de quota avant la fin. Cela ne mesure pas son intelligence, mais montre le risque d'un effort High sur un long marathon.
- **GPT-6 Astra Low** : excellente qualité, mais 13–17 points sur les deux audits comparables où Sol Medium en consommait 4.
- **GPT-5.6 Sol Medium** : baseline fiable, mais plus coûteuse que GPT-6 Sol Medium sur le benchmark directement comparable.
- **GPT-6.1 Sol Medium** : quatre runs GamePanel terminés et un cinquième bloqué avant implémentation. Les trois gros checkpoints UI consomment 10–11 points chacun ; le petit correctif consomme 3 points. GP-021 ajoute un signal distinct : 5 points dépensés pour un pré-audit de sûreté qui s’arrête proprement lorsque l’environnement ne permet pas les tests POSIX/crash exigés.

## Méthode

Chaque run essaie de conserver au minimum :

- modèle et effort ;
- date ;
- tâche ;
- quota visible avant/après ou delta ;
- durée ;
- succès / échec / partiel / blocage ;
- qualité ou résultat mesurable ;
- commit produit lorsqu'il existe ;
- prompt et réponse lorsque disponibles ;
- limites de comparabilité.

Les benchmarks historiques utilisent des états Git dont le résultat attendu était connu à l'avance mais non révélé au modèle dans le prompt.

## Statut

Données en cours de collecte. Les conclusions sont **provisoires et révisables**.

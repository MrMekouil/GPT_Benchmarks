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
| 6.0 | **GPT-6 Luna** | Medium* | 7 | **4 succès · 1 échec · 2 blocages** | **≥6 pts connus*** | **1:50:59** |
| 6.0 | **GPT-6 Sol** | Medium | 5 | **5 succès** | **~46 pts** au total · ~9,2 pts/run | **28:42** |
| 6.0 | **GPT-6 Sol** | High | 1 | **1 partiel** | **~20 pts** | **12:07** |
| 6.0 | **GPT-6 Astra** | Low | 2 | **2 succès** | **30 pts** au total · 15 pts/run | **2:52** |
| 6.1 | **GPT-6.1 Sol** | Medium | 5 | **4 succès · 1 bloqué** | **40 pts** au total · 35 succès + 5 bloqué | **52:24** |

### Repères rapides

- **A/B historique le plus propre :** GPT-6 Sol Medium = 4 pts, GPT-5.6 Sol Medium = 6 pts, GPT-6 Astra Low = 17 pts pour le même diagnostic principal.
- **A/B fonctionnel :** GPT-6 Sol Medium = 4 pts contre GPT-6 Astra Low = 13 pts, avec la même lacune principale trouvée.
- **GPT-6 Sol Medium en production :** deux gros checkpoints complets observés à **11 pts / 8:42** (pré-clôture) puis **22 pts / 14:13** (audit transversal d’architecture 0.3.1-E-A). Le coût varie donc fortement avec la profondeur et le périmètre.
- **GPT-6.1 Sol Medium :** 4 tâches de production terminées sur 5 tentatives observées. Les quatre succès consomment 3 à 11 pts ; GP-021 a consommé **5 pts / 4:31** puis s’est arrêté avant implémentation, faute d’environnement Linux/POSIX permettant les tests crash/locks exigés.
- **GPT-6 Luna Medium :** quatre succès ciblés observés à **~0 pt** (analyse 6/6), **1 pt** (correctif palette en 3:42), **~0 pt visible** (Journal d’audit en 7:47) et **~0 pt visible** (validation documentaire finale en 3:19). Les trois vrais checkpoints de production Luna totalisent donc seulement **1 point visible**. Deux longues sessions bloquées ont aussi été observées. *L'effort des deux incidents n'avait pas été relevé ; un incident n'a pas de mesure de quota.*

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

Ces deux gros checkpoints montrent un écart important selon la complexité : **11 pts** pour la pré-clôture globale contre **22 pts** pour l’audit d’architecture/persistance 0.3.1-E-A.

### Runs réels GPT-6 Luna Medium

| Run | Tâche | Quota visible | Durée | Résultat |
|---|---|---:|---:|---|
| GP-016 | Palette Utilisateurs scopée `.users-page` + test/manifeste | **1 pt** | **3:42** | terminé, commit `5049d50...` |
| GP-017 | Journal d’audit : palette graphite + responsive cartes mobile + contrat/manifeste | **~0 pt visible** | **7:47** | terminé, commit `4966b61...` |
| GP-019 | Validation documentaire finale 0.3.1 + BeamMP réel + manifeste | **~0 pt visible** | **3:19** | terminé, commit `92df2a3...` |

Ces trois runs sont de vrais checkpoints de production Luna terminés après les incidents de fiabilité observés : **3/3 réussis**, **1 point visible cumulé**, **14:48** au total.

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
- **GPT-6 Sol Medium** : très solide sur les audits ciblés (4 pts), mais les gros checkpoints vont désormais de **11 à 22 pts** selon la profondeur. L’audit 0.3.1-E-A montre qu’un travail transversal architecture/persistance peut coûter environ deux fois le checkpoint de pré-clôture.
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

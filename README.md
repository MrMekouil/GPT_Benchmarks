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

| Génération | Modèle | Effort | Runs observés | Résultats | Quota visible observé | Durée cumulée | Lecture actuelle |
|---|---|---|---:|---|---|---:|---|
| 5.6 | **GPT-5.6 Sol** | Medium | 1 | **1 succès** | **6 pts** au total · 6 pts/succès | **1:50** | Baseline fiable : 2/2 bugs historiques trouvés, mais plus coûteux que GPT-6 Sol Medium sur le même A/B. |
| 6.0 | **GPT-6 Luna** | Medium / 2 incidents effort non relevé | 4 | **1 succès · 1 échec · 2 blocages** | ~0 pt sur le succès ciblé ; ~0 sur l'échec historique ; **~5 pts connus** sur un blocage, un autre sans relevé | **1:36:11** | Peut être extrêmement économique sur une tâche locale bornée (6/6), mais la fiabilité Work observée est actuellement mauvaise. Les 2 longs blocages peuvent être liés au serveur/outillage. |
| 6.0 | **GPT-6 Sol** | Medium | 3 | **3 succès** | **~13 pts** au total · ~4,33 pts/run | **5:47** | Meilleur point de référence actuel : deux audits autonomes à 4 pts chacun, plus une reprise de réconciliation à ~5 pts. Cette reprise n'est pas comparable à un run depuis zéro. |
| 6.0 | **GPT-6 Sol** | High | 1 | **1 partiel** | **~20 pts** | **12:07** | Gros marathon multi-étapes interrompu avant la fin par épuisement du quota. High semble à réserver aux problèmes difficiles mais bien bornés. |
| 6.0 | **GPT-6 Astra** | Low | 2 | **2 succès** | **30 pts** au total · 15 pts/run | **2:52** | Excellente qualité et davantage de preuves, mais 13–17 pts sur des audits où Sol Medium consommait 4 pts pour la même conclusion utile. |
| 6.1 | **GPT-6.1 Sol** | Medium | 4 | **4 succès** | **35 pts** au total · 8,75 pts/run | **47:53** | Très fiable jusqu'ici. Trois gros checkpoints : **10–11 pts** chacun ; premier petit correctif très borné : **3 pts**. Aucun A/B direct 6.0 ↔ 6.1 encore disponible. |

### Repères rapides

- **A/B historique le plus propre :** GPT-6 Sol Medium = 4 pts, GPT-5.6 Sol Medium = 6 pts, GPT-6 Astra Low = 17 pts pour le même diagnostic principal.
- **A/B fonctionnel :** GPT-6 Sol Medium = 4 pts contre GPT-6 Astra Low = 13 pts, avec la même lacune principale trouvée.
- **GPT-6.1 Sol Medium :** 4/4 tâches de production terminées ; la consommation varie fortement avec le périmètre (3 pts sur un petit correctif, 10–11 pts sur les gros checkpoints).
- **Luna :** séparer capacité de raisonnement et fiabilité d'exécution : un run ciblé parfait à ~0 pt visible, mais deux longues sessions bloquées ont ensuite été observées.

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

### Runs réels GPT-6.1 Sol Medium

| Run | Tâche | Quota visible | Durée | Résultat |
|---|---|---:|---:|---|
| 1 | UI Instances : densification candidats + conflit/logout + tests/manifeste | 11 pts | 18:37 | terminé, commit `7ba38960...` |
| 2 | UI Supervision : compaction + responsive + diagnostic/logout + tests/manifeste | 10 pts | 10:42 | terminé, commit `622205de...` |
| 3 | UI Utilisateurs : tableau/modales + Accès + tests/manifeste | 11 pts | 12:42 | terminé, commit `c9186373...` |
| 4 | Correctif Sessions : READY/OFFLINE + test/manifeste | 3 pts | 5:52 | terminé, commit `de76ac3` |

Cumul GPT-6.1 Sol Medium à ce stade : **35 points**, **47 min 53 s**, **4/4 checkpoints terminés**.

## Lecture provisoire

- **GPT-6 Luna Medium** : peut être extrêmement économique sur une analyse locale très bornée, mais plusieurs problèmes de fiabilité/exécution ont aussi été observés. Ne pas confondre qualité de raisonnement et fiabilité de la session Work.
- **GPT-6 Sol Medium** : meilleur point de référence observé sur les audits GamePanel historiques/fonctionnels testés.
- **GPT-6 Sol High** : un gros run multi-étapes a consommé ~20 points en 12:07 et s'est arrêté faute de quota avant la fin. Cela ne mesure pas son intelligence, mais montre le risque d'un effort High sur un long marathon.
- **GPT-6 Astra Low** : excellente qualité, mais 13–17 points sur les deux audits comparables où Sol Medium en consommait 4.
- **GPT-5.6 Sol Medium** : baseline fiable, mais plus coûteuse que GPT-6 Sol Medium sur le benchmark directement comparable.
- **GPT-6.1 Sol Medium** : quatre runs GamePanel terminés. Les trois gros checkpoints consomment 10–11 points chacun ; le premier petit correctif très borné consomme 3 points. Ce signal suggère que la taille/périmètre du checkpoint influence nettement le quota, mais davantage de données restent nécessaires avant comparaison directe avec GPT-6 Sol.

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

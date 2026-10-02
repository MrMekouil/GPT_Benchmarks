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

| Génération | Modèle | Effort | Runs observés | Résultats | Quota visible cumulé | Moyenne quota / run | Durée cumulée |
|---|---|---|---:|---|---:|---:|---:|
| 5.6 | **GPT-5.6 Sol** | Medium | 1 | **1 succès** | **6 pts** | **6,00 pts** | **1:50** |
| 6.0 | **GPT-6 Luna** | Medium | 12 | **11 succès · 1 échec** | **6 pts visibles** | **0,50 pt** | **1:02:09** |
| 6.0 | **GPT-6 Luna** | non relevé* | 2 | **2 blocages** | **≥5 pts connus*** | **≥2,50 pts*** | **1:35:00** |
| 6.0 | **GPT-6 Sol** | Medium | 7 | **7 succès** | **~73 pts** | **~10,43 pts** | **52:38** |
| 6.0 | **GPT-6 Sol** | High | 1 | **1 partiel** | **~20 pts** | **~20,00 pts** | **12:07** |
| 6.0 | **GPT-6 Astra** | Low | 2 | **2 succès** | **30 pts** | **15,00 pts** | **2:52** |
| 6.1 | **GPT-6.1 Sol** | Medium | 7 | **6 succès · 1 bloqué** | **73 pts** | **10,43 pts** | **1:40:32** |

\* GP-010 et GP-011 n’avaient pas d’effort relevé ; GP-010 n’a pas non plus de mesure de quota. Ils restent séparés des runs Luna Medium. La moyenne affichée est la **moyenne brute par observation de la ligne**, y compris échecs/blocages ; pour ces deux incidents Luna, **≥2,50 pts/run** est seulement une borne basse puisque GP-010 n’a pas de mesure.

### Repères rapides

- **A/B historique le plus propre :** GPT-6 Sol Medium = 4 pts, GPT-5.6 Sol Medium = 6 pts, GPT-6 Astra Low = 17 pts pour le même diagnostic principal.
- **A/B fonctionnel :** GPT-6 Sol Medium = 4 pts contre GPT-6 Astra Low = 13 pts, avec la même lacune principale trouvée.
- **GPT-6 Sol Medium en production :** trois gros checkpoints complets observés à **11 pts / 8:42** (pré-clôture), **22 pts / 14:13** (audit transversal 0.3.1-E-A) et **21 pts / 20:35** (correctif concurrence installer/recovery GP-028). Le coût varie fortement avec la profondeur et le périmètre.
- **GPT-6.1 Sol Medium :** 6 tâches de production terminées sur 7 tentatives observées. Après B2 à **16 pts / 21:37**, E-C UI coûte **17 pts / 26:31**. GP-021 reste le seul blocage, à **5 pts / 4:31**, lié à l’absence d’environnement Linux/POSIX pour les tests crash/locks exigés.
- **GPT-6 Luna Medium :** **12 runs Medium** observés : **11 succès / 1 échec**, **6 points visibles** au total, **1:02:09**. Les **10 checkpoints de production récents** sont à **10/10 succès**, **6 points visibles** et **1:00:58**. À part, GP-010/011 représentent **2 blocages à effort non relevé**, **1:35:00** cumulé et **≥5 points connus**.

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

### Runs réels GPT-6 Sol Medium

| Run | Tâche | Quota visible | Durée | Résultat |
|---|---|---:|---:|---|
| GP-018 | Pré-clôture 0.3.1 : audit global, versions, critères de sortie, tests/docs/manifeste | **11 pts** | **8:42** | terminé, commit `3de9d3a...` |
| GP-020 | 0.3.1-E-A : audit identité d’instance, persistances, contrat rename/recovery | **22 pts** | **14:13** | terminé, commit `1a83550...` |
| GP-024 | Clôture documentaire B1 après validation Ubuntu complète | **6 pts** | **3:21** | terminé, commit `ca16063...` |
| GP-028 | Correctif startup installateur ↔ `identity-recover`, fail-closed conservé | **21 pts** | **20:35** | terminé, commit `f4bd104...` |

GP-024 est à lire séparément des gros checkpoints : il enregistre des validations Ubuntu déjà acquises et ne contient aucune implémentation fonctionnelle. GP-028 est au contraire un correctif de sûreté/concurrence transversal.

### Runs réels GPT-6 Luna Medium

| Run | Tâche | Quota visible | Durée | Résultat |
|---|---|---:|---:|---|
| GP-016 | Palette Utilisateurs scopée `.users-page` + test/manifeste | **1 pt** | **3:42** | terminé, commit `5049d50...` |
| GP-017 | Journal d’audit : palette graphite + responsive cartes mobile + contrat/manifeste | **~0 pt visible** | **7:47** | terminé, commit `4966b61...` |
| GP-019 | Validation documentaire finale 0.3.1 + BeamMP réel + manifeste | **~0 pt visible** | **3:19** | terminé, commit `92df2a3...` |
| GP-022 | B1c : correction du fixture no-op root, sans code de production | **1 pt** | **3:29** | terminé, commit `3c6c7e1...` |
| GP-023 | B1d : compatibilité installateur historique `write_inventory/aliases` + tests | **~0 pt visible** | **3:32** | terminé, commit `45d4a38...` |
| GP-026 | Clôture documentaire B2 après validation Ubuntu réelle | **~0 pt visible** | **4:52** | terminé, commit `e021093...` |
| GP-029 | Fixture POSIX `installing()` : nettoyage du marker sans code production | **1 pt** | **3:11** | terminé, commit `b78d765...` |
| GP-030 | Contrat manuel 0.3.06 : `path` + identité E-C bornée, sans code production | **~0 pt visible** | **4:14** | terminé, commit `8dff817...` |
| GP-031 | E-D : clôture documentaire après 282/282 Ubuntu + update réelle + validation desktop/mobile | **2 pts** | **12:53** | terminé, commit `554b1d7...` |
| GP-032 | Pré-clôture 0.3.1 : alignement docs + état stable/candidate + description PR #19 | **1 pt** | **13:59** | succès vérifié, commit `b67ac81...`; handoff non capturé |

Ces dix runs sont de vrais checkpoints de production Luna terminés après les incidents de fiabilité observés : **10/10 réussis**, **6 points visibles cumulés**, **1:00:58** au total.

### Runs réels GPT-6.1 Sol Medium

| Run | Tâche | Quota visible | Durée | Résultat |
|---|---|---:|---:|---|
| GP-012 | UI Instances : densification candidats + conflit/logout + tests/manifeste | 11 pts | 18:37 | terminé, commit `7ba38960...` |
| GP-013 | UI Supervision : compaction + responsive + diagnostic/logout + tests/manifeste | 10 pts | 10:42 | terminé, commit `622205de...` |
| GP-014 | UI Utilisateurs : tableau/modales + Accès + tests/manifeste | 11 pts | 12:42 | terminé, commit `c9186373...` |
| GP-015 | Correctif Sessions : READY/OFFLINE + test/manifeste | 3 pts | 5:52 | terminé, commit `de76ac3...` |
| GP-021 | 0.3.1-E-B1 : primitive transactionnelle rename + recovery/tests POSIX | **5 pts** | **4:31** | **bloqué avant implémentation**, aucun commit |
| GP-025 | 0.3.1-E-B2 : API Admin identité + register id/nom personnalisés | **16 pts** | **21:37** | terminé, commit `68d9a0d...` |
| GP-027 | 0.3.1-E-C : UI Admin identité + création auto/manuelle id/nom | **17 pts** | **26:31** | terminé, commit `11f1984...` |

Cumul GPT-6.1 Sol Medium à ce stade : **73 points**, **1 h 40 min 32 s**, **6 succès / 1 blocage**. Les six tâches terminées représentent **68 points** ; GP-021 représente **5 points** de coût sans implémentation livrée.

## Lecture provisoire

- **GPT-6 Luna Medium** : très économique sur les tâches ciblées observées : **11/12 succès Medium** et **6 points visibles** cumulés. Les dix checkpoints de production récents sont à **10/10 succès** pour **6 points visibles**. Les deux longs blocages connus sont conservés séparément car leur effort n’avait pas été relevé ; ils restent un signal de fiabilité d’exécution à surveiller.
- **GPT-6 Sol Medium** : sept succès observés. Les audits ciblés sont à 4 pts, les gros checkpoints se situent désormais à **11–22 pts**, et GP-028 confirme qu’un correctif de sûreté/concurrence transversal peut monter à **21 pts / 20:35**. La moyenne brute passe à **~10,43 pts/run**.
- **GPT-6 Sol High** : un gros run multi-étapes a consommé ~20 points en 12:07 et s'est arrêté faute de quota avant la fin. Cela ne mesure pas son intelligence, mais montre le risque d'un effort High sur un long marathon.
- **GPT-6 Astra Low** : excellente qualité, mais 13–17 points sur les deux audits comparables où Sol Medium en consommait 4.
- **GPT-5.6 Sol Medium** : baseline fiable, mais plus coûteuse que GPT-6 Sol Medium sur le benchmark directement comparable.
- **GPT-6.1 Sol Medium** : six runs GamePanel terminés et un blocage. Les anciens gros checkpoints UI étaient à 10–11 points ; les deux nouveaux lots 0.3.1-E montent à **16 pts** (B2 backend/root) puis **17 pts** (E-C UI), avec des durées de 21:37 et 26:31. GP-021 reste un coût de **5 points** sans livraison, dû au blocage environnemental POSIX.

## Intégrité des données

- `data/runs.json` est la source structurée canonique.
- `data/runs.csv` est régénéré depuis le JSON pour éviter les décalages de colonnes.
- État vérifié au 2026-10-02 : **32 runs JSON = 32 lignes CSV**, IDs uniques et champs communs cohérents.

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

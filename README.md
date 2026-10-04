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
| 6.0 | **GPT-6 Luna** | Medium | 21 | **19 succès · 1 échec · 1 bloqué** | **11 pts visibles** | **0,52 pt** | **1:41:51** |
| 6.0 | **GPT-6 Luna** | non relevé* | 2 | **2 blocages** | **≥5 pts connus*** | **≥2,50 pts*** | **1:35:00** |
| 6.0 | **GPT-6 Sol** | Medium | 7 | **7 succès** | **~73 pts** | **~10,43 pts** | **52:38** |
| 6.0 | **GPT-6 Sol** | High | 1 | **1 partiel** | **~20 pts** | **~20,00 pts** | **12:07** |
| 6.0 | **GPT-6 Astra** | Low | 2 | **2 succès** | **30 pts** | **15,00 pts** | **2:52** |
| 6.1 | **GPT-6.1 Sol** | Medium | 15 | **13 succès · 2 bloqués** | **170 pts** | **11,33 pts** | **4:18:30** |
| 6.1 | **GPT-6.1 Sol** | High | 3 | **2 succès · 1 partiel** | **51 pts** | **17,00 pts** | **2:04:17*** |

\* Durée GPT-6.1 Sol High : GP-043 inclut une attente d’autorisation et n’est pas directement comparable aux durées normales.

\* GP-010 et GP-011 n’avaient pas d’effort relevé ; GP-010 n’a pas non plus de mesure de quota. Ils restent séparés des runs Luna Medium. La moyenne affichée est la **moyenne brute par observation de la ligne**, y compris échecs/blocages ; pour ces deux incidents Luna, **≥2,50 pts/run** est seulement une borne basse puisque GP-010 n’a pas de mesure.

### Repères rapides

- **A/B historique le plus propre :** GPT-6 Sol Medium = 4 pts, GPT-5.6 Sol Medium = 6 pts, GPT-6 Astra Low = 17 pts pour le même diagnostic principal.
- **A/B fonctionnel :** GPT-6 Sol Medium = 4 pts contre GPT-6 Astra Low = 13 pts, avec la même lacune principale trouvée.
- **GPT-6 Sol Medium en production :** trois gros checkpoints complets observés à **11 pts / 8:42** (pré-clôture), **22 pts / 14:13** (audit transversal 0.3.1-E-A) et **21 pts / 20:35** (correctif concurrence installer/recovery GP-028). Le coût varie fortement avec la profondeur et le périmètre.
- **GPT-6.1 Sol Medium :** 13 tâches terminées sur 15 tentatives observées. Les gros checkpoints d’implémentation incluent B2 **16 pts / 21:37**, E-C UI **17 pts / 26:31**, 0.3.2-A **16 pts / 24:29**, 0.3.2-B **12 pts / 20:49**, 0.3.2-C **17 pts / 33:55**, 0.3.2-D **11 pts / 16:49**, E3-A **23 pts / 38:45** et E3-C **16 pts / 18:52**. GP-042 reste un audit de récupération ciblé à **1 pt / 4:02**. Deux blocages environnementaux restent observés : GP-021 à **5 pts / 4:31** et GP-033 à **1 pt / 0:17**.
- **GPT-6.1 Sol High :** trois observations. GP-041 est **partiel à 20 pts / 53:27** sur E2 ; GP-043 reprend le travail récupéré et livre E2 candidat à **7 pts / 28:50 observés** ; GP-048 livre E3-B à **24 pts / 42:00** malgré un stall apparent de l’UI après exécution. La durée GP-043 reste biaisée par une attente d’autorisation.
- **GPT-6 Luna Medium :** **21 runs Medium** observés : **19 succès / 1 échec / 1 blocage**, **11 points visibles** au total, **1:41:51**. Les **19 checkpoints de production récents** sont à **18 succès / 1 blocage**, **11 points visibles** et **1:40:40**. À part, GP-010/011 représentent **2 blocages à effort non relevé**, **1:35:00** cumulé et **≥5 points connus**.

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
| GP-032 | Pré-clôture 0.3.1 : alignement docs + état stable/candidate + description PR #19 | **1 pt** | **13:59** | terminé, commit `b67ac81...` |
| GP-036 | 0.3.2-B : clôture documentaire après validation Ubuntu 40/40 | **~0 pt visible** | **3:19** | terminé, commit `9401034...` |
| GP-038 | 0.3.2-C : clôture documentaire après validation Ubuntu C+B/POSIX | **1 pt** | **4:17** | terminé, commit `bb0dddc...` |
| GP-040 | 0.3.2-D : clôture documentaire après validation Ubuntu/Chromium réelle | **~0 pt visible** | **4:35** | terminé, commit `7787223...` |
| GP-044 | 0.3.2-E2 : correctif fixture staging path + manifeste | **1 pt** | **3:28** | terminé, commit `463e0cc...`; 38 PASS / 31 POSIX ignorés localement |
| GP-045 | 0.3.2-E2 : clôture documentaire après validation Ubuntu 69/69 | **~0 pt visible** | **5:19** | terminé, commit `6fd46e5...`; E2 acquis |
| GP-047 | 0.3.2-E3-A : clôture documentaire après validation Ubuntu 46/46 | **1 pt** | **4:40** | terminé, commit `44d49fe...`; E3-A acquis |
| GP-049 | 0.3.2-E3-B : fixture timeout client-extra corrigée localement, Ubuntu indisponible | **~0 pt visible** | **2:15** | bloqué avant commit ; PR restée sur `5d4b030...` |
| GP-050 | 0.3.2-E3-B : reprise + push du fixture timeout client-extra | **1 pt** | **4:03** | terminé, commit `bb5da9d...`; 21 PASS / 21 N/A dans Work |
| GP-051 | 0.3.2-E3-B : clôture documentaire après validation Ubuntu 42/42 | **1 pt** | **7:46** | terminé, commit `94fbabc...`; E3-B acquis |

Ces dix-neuf checkpoints de production Luna récents comptent **18 succès / 1 blocage**, **11 points visibles cumulés** et **1:40:40** au total.

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
| GP-033 | 0.3.2-A : STOP pré-vol sur miroir Work incohérent/dirty | **1 pt** | **0:17** | **bloqué conformément au contrat**, aucun commit |
| GP-034 | 0.3.2-A : contrat manifestes/content store/publication + Draft PR #22 | **16 pts** | **24:29** | terminé, commit `2c61b30...` |
| GP-035 | 0.3.2-B : scanner Minecraft local borné Forge/NeoForge | **12 pts** | **20:49** | terminé, commit `24d675b...`; validation Linux réelle encore requise |
| GP-037 | 0.3.2-C : providers métadonnées + classification/provenance/overrides/cache | **17 pts** | **33:55** | terminé, commit `fc6fcae...`; C reste candidate |
| GP-039 | 0.3.2-D : UI Admin manifestes/contenus client, sans backend E | **11 pts** | **16:49** | terminé, commit `39f7532...`; navigateur réel N/A |
| GP-042 | 0.3.2-E2 : audit de récupération après interruption, STOP sans modification | **1 pt** | **4:02** | terminé sans commit/push, conformément au prompt |
| GP-046 | 0.3.2-E3-A : API Admin content + orchestration scan/draft/publication/révocation | **23 pts** | **38:45** | terminé, commit `0c8f2c4...`; validation Ubuntu encore requise |
| GP-052 | 0.3.2-E3-C : UI Admin branchée aux API réelles E3-A/E3-B | **16 pts** | **18:52** | terminé, commit `3de8560...`; Chromium réel encore requis |

Cumul GPT-6.1 Sol Medium à ce stade : **170 points**, **4 h 18 min 30 s**, **13 succès / 2 blocages**. Les treize tâches réussies représentent **164 points** ; les deux blocages représentent **6 points** au total.

### Runs réels GPT-6.1 Sol High

| Run | Tâche | Quota visible | Durée | Résultat |
|---|---|---:|---:|---|
| GP-041 | 0.3.2-E2 : canonicalisation + content store + publication/recovery | **20 pts** | **53:27** | **partiel**, aucun commit/push ; PR #22 restée sur `e964cb8...` |
| GP-043 | 0.3.2-E2 : finalisation du travail récupéré, commit/push candidat | **7 pts** | **28:50*** | terminé, commit `c3f335a...`; durée biaisée par demande d’autorisation |
| GP-048 | 0.3.2-E3-B : distribution HTTP autorisée + client-extra | **24 pts** | **42:00** | terminé, commit `5d4b030...`; UI Work restée bloquée après exécution |

GP-041 a produit une implémentation locale avancée mais s’est interrompu avant livraison. Après l’audit de récupération GP-042, GP-043 a repris ce travail existant et livré E2 candidat. GP-048 livre E3-B malgré une capture Work sans handoff final ; le dépôt distant confirme le succès. Le coût visible High cumulé est désormais **51 pts** pour **3 observations** ; la durée cumulée observée **2:04:17** reste à lire avec prudence car GP-043 inclut une attente d’autorisation.

## Lecture provisoire

- **GPT-6 Luna Medium** : très économique sur les tâches ciblées observées : **19 succès / 1 échec / 1 blocage** sur 21 runs Medium, pour **11 points visibles** cumulés. Les 19 checkpoints de production récents sont à **18 succès / 1 blocage** ; GP-049 est le blocage environnemental, GP-050 pousse le correctif ciblé et GP-051 clôt E3-B après validation Ubuntu 42/42. Les deux longs blocages GP-010/011 restent séparés car leur effort n’avait pas été relevé.
- **GPT-6 Sol Medium** : sept succès observés. Les audits ciblés sont à 4 pts, les gros checkpoints se situent désormais à **11–22 pts**, et GP-028 confirme qu’un correctif de sûreté/concurrence transversal peut monter à **21 pts / 20:35**. La moyenne brute passe à **~10,43 pts/run**.
- **GPT-6 Sol High** : un gros run multi-étapes a consommé ~20 points en 12:07 et s'est arrêté faute de quota avant la fin. Cela ne mesure pas son intelligence, mais montre le risque d'un effort High sur un long marathon.
- **GPT-6 Astra Low** : excellente qualité, mais 13–17 points sur les deux audits comparables où Sol Medium en consommait 4.
- **GPT-5.6 Sol Medium** : baseline fiable, mais plus coûteuse que GPT-6 Sol Medium sur le benchmark directement comparable.
- **GPT-6.1 Sol Medium** : treize runs GamePanel réussis et deux blocages. Les gros lots d’implémentation récents restent dans une plage **11–23 pts** ; E3-A reste le plus coûteux à **23 pts / 38:45**, tandis que le branchement UI réel E3-C coûte **16 pts / 18:52**. GP-042 montre qu’un audit de récupération strictement borné peut rester à **1 pt / 4:02**. GP-021 a coûté **5 pts** sans livraison à cause du manque d’environnement POSIX ; GP-033 **1 pt / 17 s** en STOP de pré-vol correct.
- **GPT-6.1 Sol High** : trois observations, **51 pts** au total : un run E2 partiel à **20 pts**, une reprise E2 réussie à **7 pts**, puis E3-B réussi à **24 pts**. Le coût quota sur les tâches profondes reste élevé ; le signal temporel est moins propre à cause de l’attente d’autorisation sur GP-043 et du stall d’UI après exécution sur GP-048.

## Intégrité des données

- `data/runs.json` est la source structurée canonique.
- `data/runs.csv` est régénéré depuis le JSON pour éviter les décalages de colonnes.
- État vérifié au 2026-10-04 : **52 runs JSON = 52 lignes CSV**, IDs uniques et champs communs cohérents.

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

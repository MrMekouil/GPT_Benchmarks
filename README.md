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
| 6.0 | **GPT-6 Luna** | Medium | 23 | **21 succès · 1 échec · 1 bloqué** | **13 pts visibles** | **0,57 pt** | **1:52:56** |
| 6.0 | **GPT-6 Luna** | non relevé* | 2 | **2 blocages** | **≥5 pts connus*** | **≥2,50 pts*** | **1:35:00** |
| 6.0 | **GPT-6 Sol** | Medium | 7 | **7 succès** | **~73 pts** | **~10,43 pts** | **52:38** |
| 6.0 | **GPT-6 Sol** | High | 1 | **1 partiel** | **~20 pts** | **~20,00 pts** | **12:07** |
| 6.0 | **GPT-6 Astra** | Low | 2 | **2 succès** | **30 pts** | **15,00 pts** | **2:52** |
| 6.1 | **GPT-6.1 Sol** | Medium | 39 | **33 succès · 5 bloqués · 1 partiel** | **360 pts** | **9,23 pts** | **8:56:27** |
| 6.1 | **GPT-6.1 Sol** | High | 3 | **2 succès · 1 partiel** | **51 pts** | **17,00 pts** | **2:04:17*** |

\* Durée GPT-6.1 Sol High : GP-043 inclut une attente d’autorisation et n’est pas directement comparable aux durées normales.

\* GP-010 et GP-011 n’avaient pas d’effort relevé ; GP-010 n’a pas non plus de mesure de quota. Ils restent séparés des runs Luna Medium. La moyenne affichée est la **moyenne brute par observation de la ligne**, y compris échecs/blocages ; pour ces deux incidents Luna, **≥2,50 pts/run** est seulement une borne basse puisque GP-010 n’a pas de mesure.

### Repères rapides

- **A/B historique le plus propre :** GPT-6 Sol Medium = 4 pts, GPT-5.6 Sol Medium = 6 pts, GPT-6 Astra Low = 17 pts pour le même diagnostic principal.
- **A/B fonctionnel :** GPT-6 Sol Medium = 4 pts contre GPT-6 Astra Low = 13 pts, avec la même lacune principale trouvée.
- **GPT-6 Sol Medium en production :** trois gros checkpoints complets observés à **11 pts / 8:42** (pré-clôture), **22 pts / 14:13** (audit transversal 0.3.1-E-A) et **21 pts / 20:35** (correctif concurrence installer/recovery GP-028). Le coût varie fortement avec la profondeur et le périmètre.
- **GPT-6.1 Sol Medium :** 33 tâches terminées sur 39 tentatives observées. Les gros checkpoints incluent B2 **16 pts / 21:37**, E-C UI **17 pts / 26:31**, 0.3.2-A **16 pts / 24:29**, 0.3.2-B **12 pts / 20:49**, 0.3.2-C **17 pts / 33:55**, 0.3.2-D **11 pts / 16:49**, E3-A **23 pts / 38:45**, E3-C **16 pts / 18:52** et le runbook réel F **17 pts / 22:13**. GP-055 ajoute un correctif de fixture ContentStore ciblé à **6 pts / 5:04** sans code de production ; GP-056 ajoute le correctif scanner O_PATH à **5 pts / 6:50** ; GP-057 ajoute l’adaptation de la policy JAR réelle à **5 pts / 7:02** ; GP-058 corrige les collisions ZIP case-sensitive après NFC à **4 pts / 4:57** ; GP-059 branche la qualification Modrinth optionnelle à **10 pts / 15:13** ; GP-060 refond l’UI Contenus client pour un vrai modpack à **9 pts / 14:13** ; GP-065 livre l’import CurseForge offline à **16 pts / 29:54** ; GP-066 corrige le format de hash CurseForge Desktop à **9 pts / 7:02 cumulés sur 2 exécutions** ; GP-067 documente la validation Aero réelle à **4 pts / 1:41** sans changement fonctionnel ; GP-068 relève les bornes ZIP Chipped à **3 pts / 2:47** ; GP-069 ajoute la preuve launcher systemd/statique à **8 pts / 7:36** ; GP-070 corrige uniquement la fixture/test loader à **3 pts / 2:29** après FAIL Ubuntu natif ; GP-071 ajoute la reconnaissance des JAR Forge support/library à **8 pts / 10:37** ; GP-072 ajoute la preuve CurseForge exacte → both/SUGGESTED et la watchlist Admin à **7 pts / 9:35**, avec Gate 4 désormais acquis sur preuve utilisateur ; GP-073 rend cette présence strictement advisory face aux autres preuves et compacte l’UI en six groupes exclusifs fermés à **5 pts / 8:22** ; GP-075 corrige le remplacement des preuves CurseForge locales lors d’un import explicite à **10 pts / 21:16** ; GP-076 borne les preuves local-jar au loader sélectionné à **9 pts / 15:50** ; GP-077 ajoute l’import facultatif AutoModpack hors-ligne à **17 pts / 34:04**, sans changement de classification ni validation Interstice réelle ; GP-078 ajoute l’assistance au tri client à **12 pts / 21:45**, sans publication implicite. GP-061 ajoute un STOP de pré-vol correct à **3 pts / 0:34** ; GP-062 est **partiel à 16 pts / 28:00** après travail local, interrompu par la limite de longueur de discussion ; GP-063 est bloqué à **3 pts / 0:21** car la nouvelle discussion Work ne disposait plus du clone GamePanel ; GP-064 est bloqué à **1 pt / 0:32** car le clone GitHub a échoué sur l’accès réseau `github.com:443`. GP-042 reste un audit de récupération ciblé à **1 pt / 4:02**. Cinq blocages restent observés : GP-021 à **5 pts / 4:31**, GP-033 à **1 pt / 0:17**, GP-061 à **3 pts / 0:34**, GP-063 à **3 pts / 0:21** et GP-064 à **1 pt / 0:32**.
- **GPT-6.1 Sol High :** trois observations. GP-041 est **partiel à 20 pts / 53:27** sur E2 ; GP-043 reprend le travail récupéré et livre E2 candidat à **7 pts / 28:50 observés** ; GP-048 livre E3-B à **24 pts / 42:00** malgré un stall apparent de l’UI après exécution. La durée GP-043 reste biaisée par une attente d’autorisation.
- **GPT-6 Luna Medium :** **23 runs Medium** observés : **21 succès / 1 échec / 1 blocage**, **13 points visibles** au total, **1:52:56**. Les **21 checkpoints de production récents** sont à **20 succès / 1 blocage**, **13 points visibles** et **1:51:45**. GP-074 ajoute le correctif UI de regroupement effectif à **1 pt / 4:59**. À part, GP-010/011 représentent **2 blocages à effort non relevé**, **1:35:00** cumulé et **≥5 points connus**.

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
| GP-053 | 0.3.2-E3-C : clôture documentaire après validation Ubuntu/Chromium réelle | **1 pt** | **6:06** | terminé, commit `9c37a56...`; E3-C et E global acquis |
| GP-074 | 0.3.2-F : correctif UI regroupement effectif Suggérés/VERIFIED | **1 pt** | **4:59** | terminé, commit `f22be6f...`; Gate 4 acquis, F non acquis |

Ces vingt et un checkpoints de production Luna récents comptent **20 succès / 1 blocage**, **13 points visibles cumulés** et **1:51:45** au total.

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
| GP-054 | 0.3.2-F : runbook validation réelle Interstice + Aero | **17 pts** | **22:13** | terminé, commit `9b4cdb4...`; F non acquis, gate rename/recovery isolé requis |
| GP-055 | 0.3.2-F : correctif fixture ContentStore après FAIL Ubuntu | **6 pts** | **5:04** | terminé, commit `0f3f408...`; production inchangée, validation Ubuntu requise |
| GP-056 | 0.3.2-F : scanner Minecraft, ancêtres absolus search-only via `O_PATH` | **5 pts** | **6:50** | terminé, commit `fad9b8b...`; tests Ubuntu natifs à rejouer, F non acquis |
| GP-057 | 0.3.2-F : policy JAR réelle, limites archive + `:` interne + gros MANIFEST | **5 pts** | **7:02** | terminé, commit `46a5260...`; F et Gate 4 non acquis |
| GP-058 | 0.3.2-F : collisions internes ZIP/JAR case-sensitive après NFC | **4 pts** | **4:57** | terminé, commit `d0b1d10...`; F et Gate 4 non acquis |
| GP-059 | 0.3.2-F : qualification Modrinth exacte et optionnelle au runtime | **10 pts** | **15:13** | terminé, commit `3fd61f5...`; F/Gate 5 non acquis, Gate 4 non exécuté |
| GP-060 | 0.3.2-F : refonte ergonomique Admin Contenus client, groupes + lignes compactes | **9 pts** | **14:13** | terminé, commit `735d4dc...`; F non acquis |
| GP-061 | 0.3.2-F : pré-vol import CurseForge local | **3 pts** | **0:34** | **bloqué conformément au prompt**, checkout local sur `735d4dc...` au lieu de `3ae10db...`; aucun changement |
| GP-062 | 0.3.2-F : reprise import CurseForge après fast-forward | **16 pts** | **28:00** | **partiel**, travail local réalisé puis discussion Work arrivée à sa limite ; aucun commit distant confirmé |
| GP-063 | 0.3.2-F : nouvelle discussion, reprise CurseForge sans clone GamePanel | **3 pts** | **0:21** | **bloqué**, workspace vide / clone GamePanel absent ; aucune modification |
| GP-064 | 0.3.2-F : clone GamePanel pour reprise CurseForge | **1 pt** | **0:32** | **bloqué**, accès `github.com:443` impossible ; import non commencé |
| GP-065 | 0.3.2-F : import Admin CurseForge offline, `installedFile` + SHA-1 exact | **16 pts** | **29:54** | terminé, commit `b8e8ecd...`; validation Aero préparée, F non acquis |
| GP-066 | 0.3.2-F : parser CurseForge Desktop `hashes[].type` | **9 pts** | **7:02*** | terminé, commit `b66e994...`; *2 exécutions de 3:31, coût/durée cumulés |
| GP-067 | 0.3.2-F : documentation validation réelle Aero CurseForge | **4 pts** | **1:41** | terminé, commit `0ee8fdc...`; docs uniquement, F non acquis |
| GP-068 | 0.3.2-F : bornes ZIP Chipped 49 152 entrées / central 6 MiB | **3 pts** | **2:47** | terminé, commit `37d375e...`; Gate 4 et F non acquis |
| GP-069 | 0.3.2-F : sélection loader via preuve systemd + launcher statique | **8 pts** | **7:36** | terminé, commit `835c96b...`; Gate 4 et F non acquis |
| GP-070 | 0.3.2-F : correctif fixture/test sélection loader après FAIL Ubuntu | **3 pts** | **2:29** | terminé, commit `0a234e3...`; aucun code produit modifié, retest Ubuntu encore requis |
| GP-071 | 0.3.2-F : reconnaissance JAR Forge support/library | **8 pts** | **10:37** | terminé, commit `901c768...`; retest utilisateur requis, Gate 4/F non acquis |
| GP-072 | 0.3.2-F : preuve CurseForge exacte → both/SUGGESTED + watchlist Admin | **7 pts** | **9:35** | terminé, commit `868a5d2...`; Gate 4 acquis, F non acquis |
| GP-073 | 0.3.2-F : advisory hors conflit + six groupes UI exclusifs fermés | **5 pts** | **8:22** | terminé, commit `4ed0fbe...`; Gate 4 acquis, F non acquis |
| GP-075 | 0.3.2-F : remplacement des preuves CurseForge locales sur import explicite | **10 pts** | **21:16** | terminé, commit `89b49e2...`; Gate 4 acquis, F non acquis |
| GP-076 | 0.3.2-F : scope local-jar selon loader + purge des assertions obsolètes | **9 pts** | **15:50** | terminé, commit `6f41240...`; impact réel 354 JAR non mesuré, Gate 4 acquis, F non acquis |
| GP-077 | 0.3.2-F : import facultatif AutoModpack v4 hors-ligne | **17 pts** | **34:04** | terminé, commit `084732e...`; simulation 350/354 PASS, validation réelle N/A ; Gate 4 acquis, F non acquis |
| GP-078 | 0.3.2-F : assistance au tri client avec revue du brouillon | **12 pts** | **21:45** | terminé, commit `4e00bfc...`; 204 Python + 8 UI PASS, ergonomie réelle N/A ; Gate 4 acquis, F non acquis |

Cumul GPT-6.1 Sol Medium à ce stade : **360 points**, **8 h 56 min 27 s**, **33 succès / 5 blocages / 1 partiel**. Les trente-trois tâches réussies représentent **331 points**, les cinq blocages **13 points** et le run partiel **16 points**.

### Runs réels GPT-6.1 Sol High

| Run | Tâche | Quota visible | Durée | Résultat |
|---|---|---:|---:|---|
| GP-041 | 0.3.2-E2 : canonicalisation + content store + publication/recovery | **20 pts** | **53:27** | **partiel**, aucun commit/push ; PR #22 restée sur `e964cb8...` |
| GP-043 | 0.3.2-E2 : finalisation du travail récupéré, commit/push candidat | **7 pts** | **28:50*** | terminé, commit `c3f335a...`; durée biaisée par demande d’autorisation |
| GP-048 | 0.3.2-E3-B : distribution HTTP autorisée + client-extra | **24 pts** | **42:00** | terminé, commit `5d4b030...`; UI Work restée bloquée après exécution |

GP-041 a produit une implémentation locale avancée mais s’est interrompu avant livraison. Après l’audit de récupération GP-042, GP-043 a repris ce travail existant et livré E2 candidat. GP-048 livre E3-B malgré une capture Work sans handoff final ; le dépôt distant confirme le succès. Le coût visible High cumulé est désormais **51 pts** pour **3 observations** ; la durée cumulée observée **2:04:17** reste à lire avec prudence car GP-043 inclut une attente d’autorisation.

## Lecture provisoire

- **GPT-6 Luna Medium** : très économique sur les tâches ciblées observées : **21 succès / 1 échec / 1 blocage** sur 23 runs Medium, pour **13 points visibles** cumulés. Les 21 checkpoints de production récents sont à **20 succès / 1 blocage** ; GP-074 ajoute le correctif UI strictement de présentation à **1 pt / 4:59**, avec Gate 4 acquis et F non acquis. Les deux longs blocages GP-010/011 restent séparés car leur effort n’avait pas été relevé.
- **GPT-6 Sol Medium** : sept succès observés. Les audits ciblés sont à 4 pts, les gros checkpoints se situent désormais à **11–22 pts**, et GP-028 confirme qu’un correctif de sûreté/concurrence transversal peut monter à **21 pts / 20:35**. La moyenne brute passe à **~10,43 pts/run**.
- **GPT-6 Sol High** : un gros run multi-étapes a consommé ~20 points en 12:07 et s'est arrêté faute de quota avant la fin. Cela ne mesure pas son intelligence, mais montre le risque d'un effort High sur un long marathon.
- **GPT-6 Astra Low** : excellente qualité, mais 13–17 points sur les deux audits comparables où Sol Medium en consommait 4.
- **GPT-5.6 Sol Medium** : baseline fiable, mais plus coûteuse que GPT-6 Sol Medium sur le benchmark directement comparable.
- **GPT-6.1 Sol Medium** : trente-trois runs GamePanel réussis, cinq blocages et un run partiel. Les gros checkpoints récents restent dans une plage **11–23 pts** ; E3-A reste le plus coûteux à **23 pts / 38:45**, E3-C est à **16 pts / 18:52** et le runbook F à **17 pts / 22:13**. GP-055 montre qu’un correctif de fixture borné peut rester à **6 pts / 5:04** sans toucher la production ; GP-056 ajoute un correctif scanner de production ciblé à **5 pts / 6:50** ; GP-057 ajoute une adaptation ciblée de la policy JAR à **5 pts / 7:02** ; GP-058 ajoute le correctif de collision ZIP case-sensitive à **4 pts / 4:57** ; GP-059 ajoute le branchement Modrinth optionnel et borné à **10 pts / 15:13** ; GP-060 ajoute la refonte ergonomique UI Contenus client à **9 pts / 14:13** ; GP-065 livre l’import Admin CurseForge offline à **16 pts / 29:54** ; GP-066 corrige le parser de hash CurseForge Desktop à **9 pts / 7:02 cumulés sur deux exécutions de 3:31** ; GP-067 consigne la validation Aero réelle à **4 pts / 1:41** sans changement fonctionnel ; GP-068 relève les limites d’archive Chipped à **3 pts / 2:47** ; GP-069 ajoute la sélection de loader par preuve systemd/launcher statique à **8 pts / 7:36** ; GP-070 corrige uniquement fixture/tests à **3 pts / 2:29** après FAIL Ubuntu natif ; GP-071 ajoute la reconnaissance JAR Forge support/library à **8 pts / 10:37** ; GP-072 ajoute la preuve CurseForge exacte both/SUGGESTED et la watchlist Admin à **7 pts / 9:35** ; GP-073 la rend strictement advisory face aux autres preuves et restructure l’UI en six groupes exclusifs fermés à **5 pts / 8:22** ; GP-075 corrige le remplacement des preuves CurseForge locales lors d’un import explicite à **10 pts / 21:16** ; GP-076 borne les preuves local-jar au loader sélectionné et recalcule les assertions locales obsolètes à **9 pts / 15:50** ; GP-077 implémente l’import AutoModpack hors-ligne à **17 pts / 34:04**, avec provenance séparée et simulation 350/354, sans validation Interstice réelle ; GP-078 livre l’assistance au tri client à **12 pts / 21:45**, sans choix ni publication automatiques et avec ergonomie réelle à valider. Le total réel dépendant de Fabric parmi les 354 JAR reste N/A faute d’export complet. Gate 4 reste acquis sur validation réelle utilisateur ; F reste non acquis. GP-061 est un STOP de pré-vol conforme à **3 pts / 0:34** ; GP-062 est corrigé à **16 pts / 28:00** avec travail local confirmé avant atteinte de la limite de longueur de discussion, sans commit distant ; GP-063 est bloqué à **3 pts / 0:21** car la nouvelle discussion Work ne contenait plus le clone GamePanel ; GP-064 est bloqué à **1 pt / 0:32** sur échec réseau du clone malgré HEAD distant et PR Draft vérifiés. GP-042 montre qu’un audit de récupération strictement borné peut rester à **1 pt / 4:02**. GP-021 a coûté **5 pts** sans livraison faute d’environnement POSIX ; GP-033 **1 pt / 17 s**, GP-061 **3 pts / 34 s**, GP-063 **3 pts / 21 s** et GP-064 **1 pt / 32 s** sont des blocages sans livraison.
- **GPT-6.1 Sol High** : trois observations, **51 pts** au total : un run E2 partiel à **20 pts**, une reprise E2 réussie à **7 pts**, puis E3-B réussi à **24 pts**. Le coût quota sur les tâches profondes reste élevé ; le signal temporel est moins propre à cause de l’attente d’autorisation sur GP-043 et du stall d’UI après exécution sur GP-048.

## Intégrité des données

- `data/runs.json` est la source structurée canonique.
- `data/runs.csv` est régénéré depuis le JSON pour éviter les décalages de colonnes.
- État vérifié au 2026-10-08 : **78 runs JSON = 78 lignes CSV**, IDs uniques et champs communs cohérents.

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

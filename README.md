# GPT Benchmarks

**Quel modèle livre réellement ? Combien de temps et de quota visible coûte une tentative ?**

Observations de ChatGPT Work sur **GamePanel**, **MeshtasticCalculator** et **NomadProbe**. Les tâches sont réelles et différentes : **ce n'est pas un classement universel des modèles**.

[Par modèle](#par-modèle-et-effort) · [Vue d'ensemble](#vue-densemble) · [Comparaisons directes](#comparaisons-directes) · [Derniers runs](#derniers-runs) · [Méthodologie](docs/METHODOLOGY.md) · [Analyse complète](docs/RESULTS.md)

## Par modèle et effort

| Modèle · effort | Runs | Livraisons | Taux livré | Quota médian¹ | Durée médiane¹ | Quota cumulé² |
|:---|---:|---:|---:|---:|---:|---:|
| 5.6 Sol · Med | 1 | **1/1** | **100 %** | 6 pt | 1:50 | 6 pts |
| 6.0 Luna · Med | 27 | **22/27** | **81 %** | 1 pt | 4:26 | ≈18 pts |
| 6.0 Sol · Med | 7 | **7/7** | **100 %** | 6 pt | 3:21 | ≈73 pts |
| 6.0 Sol · High | 1 | **0/1** | **0 %** | — | — | ≈20 pts |
| 6.0 Astra · Low | 2 | **2/2** | **100 %** | 15 pt | 1:26 | 30 pts |
| 6.1 Terra · Med | 2 | **2/2** | **100 %** | 3 pt | 2:09 | 6 pts |
| 6.1 Sol · Med | 45 | **37/45** | **82 %** | 10 pt | 14:13 | 432 pts |
| 6.1 Sol · High | 3 | **2/3** | **67 %** | 15,5 pt | 35:25 | 51 pts |

¹ **Médianes calculées sur les livraisons `success` uniquement.** ² **Quota cumulé :** somme des points de pourcentage *visibles* de toutes les tentatives du groupe, y compris les échecs et blocages. Le signe ≈ signale qu'au moins un relevé était approximatif. Les deux incidents Luna à effort non relevé restent hors tableau et représentent **5 pts renseignés** supplémentaires (une consommation inconnue).

Les pourcentages dépendent fortement du nombre de runs : **100 % sur 1 ou 2 tentatives ne prouve pas une fiabilité de 100 %**. Les tâches ne sont pas identiques entre modèles ; le quota visible n'est pas une mesure exacte de tokens ou de coût.

Les modèles sont rangés **d'abord par version (5.6 → 6.0 → 6.1)**, puis par famille **Luna → Terra → Sol → Astra** à l'intérieur de chaque version. C'est un ordre de présentation, **pas un classement mesuré**. Les deux incidents Luna à effort non relevé sont exclus de ce tableau, mais toujours conservés dans les [résultats détaillés](docs/RESULTS.md) et les totaux globaux.

La **moyenne pts/run** est conservée comme mesure secondaire dans [l'analyse détaillée](docs/RESULTS.md). Pour comparer des modèles, consulter en priorité les [tests à prompt commun](docs/RESULTS.md#comparaisons-directes).

## Vue d'ensemble

| Tentatives | Livraisons rapportées | Sans livraison complète | Validation réelle |
|:---:|:---:|:---:|:---:|
| **90** | **73/90** (81,1 %) | **17/90** | **N/D** |
| 3 projets | `status = success` | 10 bloqués · 2 incidents · 4 partiels · 1 échec | Pas encore structurée |

**À comprendre :** une livraison réussie ne prouve ni un fonctionnement sur machine réelle ni une validation utilisateur. La validation réelle n'est actuellement **pas calculable** sur l'ensemble des runs ; N/D ne signifie pas 0 %.

## Comparaisons directes

| Même objectif / prompt | GPT-5.6 Sol Med | GPT-6.0 Luna Med | GPT-6.0 Sol Med | GPT-6.0 Astra Low |
|:---|:---|:---|:---|:---|
| Deux bugs historiques | 6 pts · 2/2 | 0 pt visible · échec | 4 pts · 2/2 | 17 pts · 2/2 |
| Lacune fonctionnelle | — | — | 4 pts · trouvée | 13 pts · trouvée |

Ces **petits échantillons** sont les comparaisons les mieux contrôlées du dépôt. Leurs différences ne se généralisent pas à toutes les missions ; l'affichage 0 pt n'implique pas un coût nul.

## Derniers runs

| Run | Projet et tâche | Modèle | Quota | Durée | Livraison / limite |
|:---|:---|:---|---:|---:|:---|
| [GP-090](runs/GP-090-gpt61-terra-medium-nomadprobe-roadmap-v01.md) | NomadProbe · roadmap V0.1 | 6.1 Terra Med | 2 pts | 0:49 | Docs livrées ; validation B en attente |
| [GP-089](runs/GP-089-gpt61-terra-medium-meshtasticcalculator-firefox-b09.md) | MeshtasticCalculator · Firefox B09 | 6.1 Terra Med | 4 pts | 3:28 | Correctif livré ; Firefox non exécuté sur nouveau SHA |
| [GP-088](runs/GP-088-gpt6-luna-medium-windows-diagnostics-cp5-documentary-close.md) | GamePanel · clôture documentaire CP5 | 6.0 Luna Med | 2 pts | 14:28 | Docs livrées ; artifact CI bloqué |
| [GP-087](runs/GP-087-gpt61-sol-medium-windows-diagnostics-cp5.md) | GamePanel · fiabilité Windows CP5 | 6.1 Sol Med | 13 pts | 12:40 | Livraison technique ; validation terrain alors en attente |

## Comment lire les résultats

- **Livré** : le résultat attendu dans le périmètre du run est signalé comme terminé. Pas nécessairement validé au-delà.
- **Testé** : les tests et leurs limites sont indiqués dans la fiche du run ; un PASS local ne remplace pas un PASS utilisateur.
- **Validé réellement** : preuve distincte et explicite. Le dépôt historique ne possède pas encore de champ homogène : afficher **N/D**, pas un pourcentage trompeur.
- **Quota médian et durée médiane** : repères descriptifs pour les livraisons. Les tâches ciblées, les audits et les gros développements doivent être analysés séparément.
- **Coût complet d'un objectif** (tentatives, échecs et reprises compris) : indicateur prévu, **N/D tant que les runs ne sont pas rattachés de façon vérifiable à un même objectif**.

## Explorer les données

| Ressource | À quoi elle sert |
|:---|:---|
| [Méthodologie](docs/METHODOLOGY.md) | Définitions, dénominateurs, limites et métriques futures |
| [Résultats détaillés](docs/RESULTS.md) | Répartition des statuts, médianes, dispersion, coûts secondaires et A/B |
| [Journal chronologique](RUN_LOG.md) | Historique de tous les runs, sans suppression |
| [Fiches de runs](runs/) | Prompts, réponses et contexte lorsqu'ils sont disponibles |
| [JSON canonique](data/runs.json) · [CSV](data/runs.csv) | Données structurées réutilisables |
| [Vérification locale](scripts/verify_data.py) | Contrôle des données et régénération CSV, sans GitHub Actions |

**Qualité de mesure actuelle :** 14 runs avec **0 point de quota visible** et 15 quotas notés approximatifs ; un run ne fournit aucun quota chiffré. Les statistiques sont descriptives, non une mesure de tokens ou de prix réel.

<sub>Tableau de bord préparé le 31 octobre 2026 · 90 observations enregistrées · historique et données reproductibles dans ce dépôt.</sub>

# Résultats détaillés

[← Tableau de bord](../README.md) · [Méthodologie](METHODOLOGY.md) · [Journal](../RUN_LOG.md)

## État de la collecte — 31 octobre 2026

Les **90 runs** couvrent 3 projets. Ils ne constituent **pas** un protocole expérimental équilibré : les modèles, efforts, dates, projets et tailles de missions varient.

| Statut du run | Nombre | Signification |
|:---|---:|:---|
| `success` | **73** | Livrable du prompt terminé ; validation réelle pas forcément acquise |
| `blocked` | 10 | STOP sans livraison complète, souvent dû à une limite d'environnement |
| `stalled` | 2 | Session bloquée, sans résultat confirmé |
| `partial` | 4 | Travail commencé mais objectif non entièrement livré |
| `failure` | 1 | Objectif raté |
| **Total** | **90** | **81,1 % de livraisons** |

### Répartition par projet

| Projet | Runs | Livraisons du prompt |
|:---|---:|---:|
| GamePanel | 88 | 71 |
| MeshtasticCalculator | 1 | 1 |
| NomadProbe | 1 | 1 |

**Attention :** pour les runs documentaires, un succès peut être la mise à jour des documents, même quand le produit reste en attente de validation utilisateur. Les validations réelles ne sont pas représentées par un champ homogène : **taux de validation N/D**.

## Coûts et durées par modèle

Les colonnes « médiane », « dispersion » et « durée » sont calculées **uniquement sur les livraisons `success`**. La dernière colonne conserve, à titre historique, la **moyenne pts/run** sur *tous les runs dont le quota est connu*, y compris les blocages.

| Modèle · effort | Runs | Livré | Quota médian / succès | Q1–Q3¹ (pts) | Durée médiane / succès | Moy. pts/run² |
|:---|---:|---:|---:|---:|---:|---:|
| 5.6 Sol Medium | 1 | 1/1 | 6 pt | — | 01:50 | 6 |
| 6.0 Luna Medium | 27 | 22/27 | 1 pt | 0–1 | 04:26 | 0,7 |
| 6.0 Luna (effort non relevé) | 2 | 0/2 | — | — | — | 5 (1/2) |
| 6.0 Sol Medium | 7 | 7/7 | 6 pt | 4–21 | 03:21 | 10,4 |
| 6.0 Sol High | 1 | 0/1 | — | — | — | 20 |
| 6.0 Astra Low | 2 | 2/2 | 15 pt | — | 01:26 | 15 |
| 6.1 Terra Medium | 2 | 2/2 | 3 pt | — | 02:09 | 3 |
| 6.1 Sol Medium | 45 | 37/45 | 10 pt | 6–16 | 14:13 | 9,6 |
| 6.1 Sol High | 3 | 2/3 | 15,5 pt | — | 35:25 | 17 |

¹ Q1–Q3 : quartiles par rang (nearest-rank), affichés seulement si au moins **5 succès**. Un tiret signifie effectif insuffisant ou donnée absente, **pas zéro**. ² La moyenne brute comprend les tentatives infructueuses avec quota renseigné ; pour les runs à effort non relevé, le quota n'est connu que pour une partie des observations.

**Périmètre des relevés :** 89/90 quotas chiffrés, 641 points de pourcentage visibles cumulés, 14 runs à 0 point **affiché**, 15 mesures signalées approximatives. Les points visibles ne sont ni une somme de tokens ni une unité tarifaire.

La médiane et la moyenne sont décrites comme des **observations de charge** ; les comparer entre modèles serait trompeur sans travaux de difficulté semblable. En particulier, **GPT-6.1 Terra Medium n'a que deux observations sur deux projets distincts**, alors que GPT-6.1 Sol Medium possède surtout des missions GamePanel de production plus larges.

## Comparaisons directes

### Même audit historique — GP-001 à GP-004

| Modèle / effort | Quota visible | Durée | Résultat |
|:---|---:|---:|:---|
| GPT-5.6 Sol Medium | 6 pts | 1:50 | 2/2 bugs trouvés |
| GPT-6 Luna Medium | 0 pt visible | 0:31 | Échec avant audit |
| GPT-6 Sol Medium | 4 pts | 1:35 | 2/2 bugs trouvés |
| GPT-6 Astra Low | 17 pts | 1:42 | 2/2 bugs trouvés, davantage de détails |

### Même lacune fonctionnelle — GP-005 et GP-006

| Modèle / effort | Quota visible | Durée | Résultat |
|:---|---:|---:|:---|
| GPT-6 Sol Medium | 4 pts | 1:45 | Lacune principale identifiée |
| GPT-6 Astra Low | 13 pts | 1:10 | Même lacune identifiée, vérification plus détaillée |

Ces petits groupes permettent une comparaison **bien plus cadrée que le total général**, mais aucun ne suffit à garantir un résultat général sur d'autres prompts. Le quota visible à 0 n'implique pas l'absence de consommation réelle.

## Pourquoi ne pas afficher un classement global ?

- **Taille de tâche :** un correctif de fixture et un développement backend de 40 minutes ne constituent pas des unités équivalentes.
- **Objectif déjà préparé :** un run final peut bénéficier de plusieurs runs antérieurs ou de validations utilisateur préexistantes.
- **Conditions d'exécution :** réseau, checkout, autorisations, quota GitHub Actions et outil navigateur peuvent bloquer un run sans que le modèle soit en cause.
- **Tests non comparables :** un succès de livraison documentaire ne vaut pas validation d'un binaire Windows ou d'un appareil sur le terrain.
- **Petit échantillon :** 1 ou 2 runs ne justifient pas une estimation stable de fiabilité.

La prochaine métrique la plus utile sera le **coût total par objectif abouti**, mais il faut d'abord relier explicitement tentatives et reprises par un `objective_id` contrôlé, puis distinguer validation automatique et validation terrain. Sans ces données, cet indicateur reste **N/D**.

## Sources

Les données brutes sont disponibles dans [`data/runs.json`](../data/runs.json) et [`data/runs.csv`](../data/runs.csv). Le [journal chronologique](../RUN_LOG.md) et les [fiches individuelles](../runs/) conservent les explications, prompts, réponses et limites historiques.

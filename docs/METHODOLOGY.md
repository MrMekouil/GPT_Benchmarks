# Méthode de mesure

[← Tableau de bord](../README.md) · [Résultats détaillés](RESULTS.md) · [JSON](../data/runs.json)

## Principe

Ce dépôt mesure des **sessions ChatGPT Work réellement observées**, sur des tâches de difficulté et de nature variables. Il ne mesure pas les tokens, un tarif ni l'intelligence intrinsèque d'un modèle. **Chaque run est une observation, pas un essai A/B contrôlé par défaut.**

La source de vérité est `data/runs.json`, répliquée dans `data/runs.csv`. Les comptes publiés portent sur les runs disponibles, sans extrapolation. La date d'un run peut être une **date d'enregistrement** si sa date d'exécution n'a pas été fournie.

## Indicateurs principaux

| Indicateur | Définition exacte | Dénominateur et réserve |
|:---|:---|:---|
| **Taux de livraison** | `success / total des runs` | Tous les runs du périmètre, y compris blocages, échecs, partiels et incidents. Une réussite d'audit ou de documentation compte comme livraison si **c'était l'objectif du prompt**. |
| **Taux de validation réelle** | `validations passées / validations applicables au statut connu` | **N/D pour l'historique** : aucun champ homogène ne permet d'identifier les validations. Ne pas considérer les statuts absents comme échecs. |
| **Quota médian** | Médiane des `quota_used_points` des runs **success** avec mesure connue | Points de pourcentage **affichés** par l'interface, pas consommation réelle ni tokens. Une valeur 0 signifie « aucun changement visible ». |
| **Durée médiane** | Médiane des `duration_seconds` des runs **success** avec durée connue | Ne corrige pas les attentes d'outils, d'autorisation, les pauses, les reprises ni les stalls UI. |
| **Taux de blocage** | `(blocked + stalled) / tous les runs` | Les causes doivent être décrites ; un blocage n'est pas nécessairement un défaut du modèle. |

La **médiane** est l'élément central de la série ordonnée ; avec un effectif pair, on prend la moyenne des deux éléments centraux. Les quartiles éventuellement indiqués utilisent le rang supérieur `ceil(p × n)` (méthode nearest-rank) ; ils sont descriptifs, surtout si n est petit.

Un sous-groupe sans run `success` affiche un tiret pour les médianes de succès, **pas zéro**.

## Indicateurs secondaires

| Indicateur | Calcul | Interprétation |
|:---|:---|:---|
| **Moyenne pts/run** | Somme du quota visible chiffré / nombre de runs avec quota chiffré | Mesure descriptive brute, **non comparable** entre tâches de complexité différente. Les tentatives bloquées y entrent ; les données manquantes sont exclues du dénominateur. |
| **Quota médian d'une livraison** | Médiane des seules tentatives `success` | Aide à résister aux valeurs extrêmes, mais **ne comptabilise pas les tentatives ratées avant réussite**. |
| **Coût complet par objectif abouti** | Somme du quota visible de **toutes** les tentatives identifiées d'un même objectif jusqu'à la livraison/validation | **N/D actuellement** : les runs ne portent pas d'`objective_id` fiable, et les reprises ne sont pas systématiquement reliées. Ne pas regrouper par ressemblance de titre. |
| **Temps complet par objectif abouti** | Somme des durées des tentatives liées, avec prise en compte des attentes si connues | Même limite que le coût complet ; ne pas présenter de chiffre artificiel. |
| **Dispersion** | Quartiles Q1/Q3 des coûts ou durées de livraison | À afficher avec `n` et seulement lorsque l'échantillon est assez grand pour être utile. |

## Deux axes de réussite différents

1. **Exécution du prompt :** `status` dans JSON (`success`, `failure`, `blocked`, `partial`, `stalled`). `success` signifie que **le livrable demandé au run** est annoncé terminé et que son résultat est suffisamment étayé pour être enregistré comme tel. Pas nécessairement succès global du projet.
2. **Validation du résultat :** observation ultérieure sur le bon environnement, **distincte** d'un PASS de tests automatisés. Un run documentaire peut être terminé alors qu'un checkpoint produit reste « en attente de validation ».

Le champ de validation manque à l'historique, même lorsque certaines fiches décrivent des validations utilisateur. **Aucune backfill massive n'a été inférée depuis du texte libre.**

Pour les futurs runs, les champs optionnels suivants pourront être renseignés **sur preuve** et sans rétroactivité forcée :

- `work_kind` : `audit`, `documentation`, `correctif`, `fonctionnalite`, `interface`, `tests` ;
- `validation_status` : `passed`, `failed`, `pending`, `not_applicable` ou `unknown` ;
- `validation_evidence` : description de la preuve et référence, si disponible ;
- `objective_id` : identifiant stable d'une mission partagée par plusieurs tentatives.

Jusqu'à ce que le dénominateur validable soit fiable, afficher **N/D**, jamais un « taux de validation : 0 % ».

## Bonnes pratiques de comparaison

- **Même prompt, même objectif, même état initial** : comparaison A/B exploitable, si les conditions et les écarts de contexte sont documentés.
- **Même famille de tâches** : comparaison indicative seulement, avec catégorie explicite, complexité comparable et taille d'échantillon.
- **Missions différentes / projets différents** : tableau descriptif, **pas classement de performance**.
- **Reprise d'un autre modèle ou d'un travail non terminé** : le coût du run final ne représente **pas** tout le travail effectué.
- **n = 1 ou 2** : afficher le résultat, mais ne pas conclure à une supériorité de taux ou de médiane.
- **Effort non relevé** : groupe distinct, sans l'assimiler automatiquement à Medium.

## Incertitudes spécifiques au quota

Le pourcentage affiché par Work/ChatGPT peut être arrondi ou mis à jour par paliers. Les relevés `quota_before_pct` et `quota_after_pct` ne renseignent donc pas précisément les ressources réelles utilisées. `quota_approx=true` signale une approximation, sans garantir que les valeurs marquées false sont exactes en coût réel.

Les runs à `0` point visible **ne sont pas gratuits** : ils n'ont pas modifié le chiffre affiché. Les données de quota absentes ne doivent pas être remplacées par 0.

## Contrôles d'intégrité

Avant chaque publication de données :

1. Préserver tous les enregistrements, IDs et fiches existants.
2. Vérifier **IDs uniques**, les statuts et les valeurs admissibles.
3. Régénérer/contrôler le CSV depuis les mêmes champs JSON, sans inventer les champs manquants.
4. Recalculer les agrégats, comparer les totaux par modèles et contrôler les liens vers les fiches.
5. Effectuer les tests **locaux** ou les vérifications statiques utiles ; **aucune GitHub Actions automatique**.
6. Ne fusionner la branche sur `main` qu'après validation explicite du propriétaire du dépôt.

Les formules ne dépendent pas de l'identifiant `GP-xxx` : ce préfixe historique est conservé même pour les runs MeshtasticCalculator et NomadProbe.

# GP-102 — GPT-6.2 Sol Very High — MeshtasticCalculator 0.2.6 CP02 moteur natif

- **Date d'enregistrement :** 2026-11-25 ; rapport Work daté du 25 novembre 2026.
- **Modèle / effort :** GPT-6.2 Sol / Very High
- **Quota visible :** 93 % → 69 % = **24 points**
- **Durée :** **28 min 47 s (1 727 secondes)**
- **Statut :** **success**, livraison du moteur natif demandé ; CP02 ouvert et stabilité GPU à confirmer
- **Projet / branche :** `MrMekouil/MeshtasticCalculator`, `work/v0.2.6`
- **Commit source vérifié :** [`4fa78b8ca364a0329577bcd3de3792128f12bb52`](https://github.com/MrMekouil/MeshtasticCalculator/commit/4fa78b8ca364a0329577bcd3de3792128f12bb52)
- **Rapport source :** [V02_06_CP02.md](https://github.com/MrMekouil/MeshtasticCalculator/blob/4fa78b8ca364a0329577bcd3de3792128f12bb52/docs/V02_06_CP02.md)

## Prompt exact

~~~text
# MeshtasticCalculator 0.2.6 — CP02 : construction du moteur natif

**Dépôt :** `MrMekouil/MeshtasticCalculator`\
**Branche :** `work/v0.2.6`\
**HEAD attendu :** `e06a07525f6ad4e22a21c20e9c0b60efe38514cc`

## 1. Reprise et clôture CP01

Lire AGENTS, WORK_STATE, ASSISTANT_STATE, ROADMAP, NATIVE_ARCHITECTURE_026 et le bilan CP01.

Le propriétaire autorise explicitement la clôture du CP01 sur son périmètre de recherche, performances et choix architectural, ainsi que le démarrage du CP02.

Consigner cette décision.

Les validations scientifiques et numériques restantes sont transférées au CP03. La qualification de portabilité CPU relève du CP02.

La comparaison .NET sur Grille est reportée.

## 2. Architecture retenue

- C++ comme moteur principal.
- CPU multithread par lots.
- CUDA SAMPLES Compact.
- Dimensionnement adaptatif des lots.
- Répartition hybride dynamique.
- Fonctionnement CPU autonome sans CUDA.
- JavaScript et Rust conservés comme références.

Préserver les performances acquises sans lancer de nouvelles campagnes d'optimisation redondantes.

## 3. Construction du moteur natif

Transformer réellement les prototypes existants en moteur structuré, maintenable et réutilisable.

Séparer les responsabilités :

- Noyau RF et géodésie.
- Modèles de propagation.
- Accès et interpolation du terrain HGT.
- Planification des Grilles.
- Stockage et validation des blocs.
- Ordonnanceur.
- Adaptateur CPU.
- Adaptateur CUDA.
- Gestion des ressources.
- Contrôle des travaux et progression.
- Détection des capacités matérielles.

Étudier les dépendances existantes avant tout déplacement.

Éviter la duplication des implémentations entre le nouveau moteur et les bancs historiques.

Préserver les références et la reproductibilité des anciens benchmarks.

## 4. Compilation et distribution

Mettre en place un système de compilation maintenable, de préférence CMake, sous réserve de justification technique.

Prévoir :

- Windows x64.
- Linux x86_64.
- Compilation CPU sans aucun SDK CUDA.
- Compilation CUDA facultative.
- Détection et chargement du moteur GPU compatible.
- Configuration Release et Debug.
- Tests automatisés exécutables localement.
- Dépendances documentées et limitées.

Le moteur CPU doit fonctionner sur une machine dépourvue de carte NVIDIA.

Ne pas imposer l'installation de CUDA aux utilisateurs du mode CPU.

## 5. Contrat du moteur

Créer un contrat versionné, indépendant de l'interface graphique, permettant :

- Inventaire des capacités matérielles.
- Validation d'une demande de calcul.
- Estimation des ressources nécessaires.
- Démarrage d'un travail.
- Consultation de la progression.
- Pause.
- Annulation.
- Reprise.
- Consultation des résultats et erreurs.

Prévoir la Grille multi-stations future sans l'implémenter dans ce checkpoint.

Aucune dépendance directe du noyau RF à l'interface graphique.

## 6. Ressources et sélection des moteurs

Respecter intégralement NATIVE_ARCHITECTURE_026.md.

Le moteur doit accepter :

- CPU activé ou désactivé.
- GPU activé ou désactivé.
- Nombre maximal de threads CPU.
- Budget RAM.
- Budget VRAM.

Refuser un travail sans moteur utilisable.

Gérer explicitement le GPU absent, incompatible ou indisponible en cours de calcul.

Aucune modification silencieuse de la résolution ou du modèle RF pour respecter un budget.

Préparer les contrats nécessaires aux futurs boutons et curseurs, sans développer l'interface graphique maintenant.

## 7. Stockage

Préserver les acquis CP22 :

- Identité des calculs.
- Intégrité des blocs.
- Publication atomique.
- Identifiants 64 bits.
- NoData.
- Reprise sans recalcul des blocs valides.

Conserver les identités CPU/GPU distinctes tant que la politique numérique de production n'est pas approuvée.

Étudier le stockage massif par conteneurs segmentés afin d'éviter des millions de petits fichiers.

Ne pas imposer une migration destructive des formats existants.

## 8. Politique numérique

La référence canonique reste C++ CPU en FP64.

Critère candidat pour le CP03 :

- Maximum 1 ULP et 0,00002 dB.
- États identiques.
- Aucun franchissement des seuils actifs qualifiés.
- Reproductibilité stricte par identité.

Cette proposition ne constitue pas encore une autorisation de publication hybride en production.

Aucun changement des équations RF.

## 9. Qualification CP02

Réutiliser les témoins existants.

Vérifier notamment :

- Compilation CPU autonome.
- Compilation CUDA facultative.
- Non-régression stricte par moteur.
- Intégrité du stockage.
- Attribution unique des blocs.
- Respect des budgets.
- Détection GPU positive et négative.
- Pause, annulation et reprise.
- Gestion des erreurs et ressources insuffisantes.

Préparer une qualification bornée sur :

- MainPC Windows.
- Chuwi Windows.
- Chuwi MX Linux.

Le Chuwi doit pouvoir fonctionner sans CUDA et avec un budget mémoire modeste.

Ne pas relancer REEL100 complet sans nécessité technique démontrée.

## 10. Livraison

Développer réellement le moteur natif.

Ne pas se limiter à une architecture théorique ou à de la documentation.

Préparer les commandes de qualification locale, avec une seule paire de délimiteurs DEBUT RETOUR / FIN RETOUR, code de sortie inclus et résultats condensés.

Mettre à jour les documents opérationnels.

Publier sur la branche autorisée.

## 11. Contraintes absolues

- Zéro GitHub Actions.
- Main strictement intouchable.
- Tests locaux uniquement.
- Aucun changement de physique RF.
- Aucun écrasement des HGT ou témoins.
- Aucune migration de l'application Web.
- Aucun saut de checkpoint.

CP02 reste ouvert jusqu'à qualification et validation du propriétaire.
~~~

## Réponse exacte

~~~text
**Moteur natif CP02 publié** sur `work/v0.2.6` au commit [`4fa78b8ca364a0329577bcd3de3792128f12bb52`](https://github.com/MrMekouil/MeshtasticCalculator/commit/4fa78b8ca364a0329577bcd3de3792128f12bb52). `main` est intacte. Aucune GitHub Action n’a été déclenchée.

La bibliothèque C++ et la commande `meshtastic-native` sont testables. Elles exposent le CPU autonome, CUDA facultatif et l’hybride expérimental, avec budgets, progression, pause, annulation et reprise CP22. Les résultats CPU et GPU conservent des identités distinctes.

- **CPU Windows** — Release et Debug PASS. Intégrité, NoData, budgets, pause, annulation et reprise PASS.
- **CUDA** — Compilation PASS. La recette complète sur RTX 2060 Super a rendu le code 0, avec parité stricte sur les cinq témoins historiques et réutilisation des 17 blocs par moteur. Une répétition s’est arrêtée après publication des blocs GPU et hybrides sans rendre son verdict. La stabilité GPU reste à confirmer.
- **Régressions Node** — 212/212 PASS. Chuwi Windows et MX Linux restent à qualifier.

**CP01 est clôturé** sur la recherche, les performances et le choix d’architecture. Les validations scientifiques et la politique numérique passent au CP03. **CP02 reste ouvert** jusqu’à qualification et validation du propriétaire.

### Qualification MainPC

Depuis la racine d’une copie au commit publié, lancer cette commande. Le script produit une seule paire `DEBUT RETOUR` / `FIN RETOUR`, avec le code de sortie à l’intérieur.
```
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\native\qualify\mainpc.ps1 -Cuda -Previous "$env:TEMP\Meshtastic-026-CUDA-af9afe07587e4baf951d4422f1b04cef\validation\campaign" -JsWitness "$env:TEMP\Meshtastic-CP01-CPU-sfmHjB"
```

[Bilan CP02 et commandes Chuwi](https://github.com/MrMekouil/MeshtasticCalculator/blob/4fa78b8ca364a0329577bcd3de3792128f12bb52/docs/V02_06_CP02.md)
~~~

## Synthèse enregistrée

- **Commit confirmé :** 42 fichiers modifiés. Bibliothèque C++ et CLI, CMake, adaptateurs CPU/CUDA, ordonnanceur, stockage CP22, tests, scripts de qualification et documentation. La livraison est réelle ; le benchmark ne constitue pas une revue exhaustive du code.
- **Windows Work :** CPU autonome Release et Debug PASS, budgets, intégrité, NoData, pause, annulation et reprise PASS. Compilation CUDA PASS ; recette complète sur RTX 2060 Super code 0. Cinq témoins strictement identiques par moteur et 17 blocs par moteur réutilisés, selon le rapport. Node 212/212 PASS.
- **Réserve GPU importante :** le rapport indique plusieurs exécutions sans verdict final après publication des 13 blocs GPU et 13 hybrides, y compris une répétition après la recette PASS. Le banc considère une absence de verdict comme un échec même avec code 0. La stabilité n'est pas acquise.
- **Portabilité :** Chuwi Windows et MX Linux NON EXÉCUTÉS ; qualification propriétaire CP02 encore nécessaire. Les commandes sont documentées dans le rapport.
- **Politique numérique et stockage :** C++ CPU FP64 canonique ; identités CPU/GPU distinctes, hybride expérimental, seuils 1 ULP et 0,00002 dB candidats uniquement pour CP03. Étude des conteneurs segmentés documentée, stockage CP22 conservé.
- **Périmètre :** CP01 clôturé sur recherche, performances et architecture ; validations scientifiques et numériques transférées au CP03, comparaison .NET reportée. CP02 reste ouvert comme exigé par le prompt.
- **Qualification du run :** success pour le livrable moteur et recettes, et non pour la clôture du CP02. Résultats Work documentés, non réexécutés indépendamment par le gestionnaire du benchmark. Aucun GitHub Actions lancé pour cet enregistrement.

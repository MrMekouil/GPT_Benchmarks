# GP-090 — GPT-6.1 Terra Medium — NomadProbe V0.1

- **Date d'enregistrement :** 2026-10-29 (date d'exécution Work non indiquée)
- **Quota visible :** 50 % → 48 % (**2 points**)
- **Durée :** 49 secondes
- **Statut :** succès de livraison documentaire ; CP0.1-B **en attente de validation utilisateur**
- **Dépôt source :** `MrMekouil/NomadProbe`, branche `work/0.1-foundation`
- **HEAD initial attendu :** `82529c9940844bd1733d62007153ff8f451f6404`
- **HEAD final vérifié :** `366f5b9fa1360c2b3c8d84879d3b08b9ce8bfe12`

## Prompt exact

~~~text
# NomadProbe V0.1 — Session Work 1 — Réorganisation observation-first après audit CP0.1-B

## 1. Références et mission

Dépôt privé : `MrMekouil/NomadProbe`

Branche existante autorisée : `work/0.1-foundation`

HEAD Work connu : `82529c9940844bd1733d62007153ff8f451f6404` — à revérifier.

Main connu : `4ac3fc045d59cbc593dd396d7279912554b9fbd3` — à revérifier.

Aucune PR demandée.

**Mission exclusivement documentaire :** réorganiser les futurs checkpoints V0.1 pour privilégier l'observation réelle, la découverte de l'environnement et l'interface Explorer.

Ne développer aucune nouvelle fonctionnalité dans cette mission.

## 2. Résultat de l'audit pilote

CP0.1-B livré au commit ci-dessus.

La Session Assistant a inspecté les nouveaux décodeurs, le registre, les tests, la CLI, les preuves, les arbres Git et les liens documentaires.

Résultat : **audit statique favorable, aucune anomalie bloquante identifiée**.

24 tests PASS déclarés par Work, dont 16 tests hérités de A. Les tests de B n'ont pas encore été rejoués par l'utilisateur sur son propre checkout.

Inscrire CP0.1-B au statut :

**VALIDATION UTILISATEUR EN ATTENTE**

Ne pas le déclarer VALIDÉ.

CP0.1-A est déjà VALIDÉ sur Windows ; CP0.1-G est accepté. Ne pas remettre en cause ces validations.

## 3. Changement de logique de développement

La V0.1 doit devenir une première plateforme d'observation réelle, pas uniquement un moteur logiciel hors ligne.

Priorité fonctionnelle :

1. Acquérir.
2. Découvrir.
3. Identifier quand c'est possible.
4. Conserver les données brutes et les observations.
5. Décoder quand un protocole est reconnu.
6. Présenter les résultats dans une interface Explorer.

Un protocole inconnu doit rester observable sans décodeur.

Ne pas prétendre qu'un ESP32 détecte tous les signaux radio.

Séparer observation/découverte, capture de trames, décodage et opérations actives.

## 4. Nouvelle file V0.1 obligatoire

### CP0.1-A — Fondation logicielle

VALIDÉ sur Windows.

Conserver les références, preuves et limites actuelles.

### CP0.1-B — Moteur de décodage

VALIDATION UTILISATEUR EN ATTENTE.

Conserver le contrat et les deux décodeurs NP1/NPB1. Ne pas modifier le code pendant cette mission.

### CP0.1-C — Acquisition USB série réelle

NON DÉMARRÉ.

Objectif : utiliser le banc Arduino UNO R4 WiFi déjà confirmé sur USB pour réaliser une première acquisition NomadProbe complète.

Chaîne attendue :

Périphérique USB → capture brute horodatée → fichier NomadProbe → réouverture → décodage NP1 → résultat.

Prévoir gestion des ports, ouverture/fermeture, arrêt, timeout, erreurs et déconnexion/reconnexion.

COM7 n'est pas une constante.

Ne pas imposer de GUI, nouvelle carte, firmware non autorisé ou intervention électrique.

Dépendance : CP0.1-B VALIDÉ.

### CP0.1-D — Découverte de l'environnement Wi-Fi/BLE

NON DÉMARRÉ.

Objectif : première capacité de découverte d'équipements ou d'annonces accessibles avec le matériel possédé.

Le banc ESP32-WROOM-32 est un candidat prioritaire, sous réserve de prévol réel de la carte, du firmware, des connexions et de l'interface.

Le résultat attendu doit distinguer :

- Source matérielle.
- Technologie détectée.
- Observations et horodatages.
- Informations accessibles : canal, puissance reçue ou type d'annonce si le matériel les fournit.
- Équipements détectés, identifiants éventuels, anonymisation et limites.
- Trames décodables versus observations non interprétées.
- Absence de module ou fonction non disponible.

Développer ultérieurement un contrat de source/observation réutilisable.

Privilégier les fonctions de réception et de découverte non intrusives. Ne pas qualifier de passive une méthode de scan qui émet effectivement des requêtes. Ne pas prévoir d'association, injection, émission arbitraire, extraction de secrets ou suivi prolongé de tiers.

Ne pas promettre Zigbee, Sub-GHz, NFC ni d'autres bandes non prises en charge par le matériel sélectionné.

Dépendance : CP0.1-C VALIDÉ.

### CP0.1-E — Interface Explorer minimale

NON DÉMARRÉ.

Objectif : rendre NomadProbe utilisable visuellement sur PC avec une première interface locale.

Afficher :

- Sources et modules disponibles ou absents.
- Démarrage/arrêt des observations.
- Résultats Wi-Fi/BLE réellement acquis quand disponibles.
- Captures série.
- Trames brutes et résultats décodés.
- Protocoles reconnus et inconnus.
- Erreurs, pertes, limites et qualité de l'acquisition.
- Sauvegarde et réouverture d'une session.

Conserver une vue d'enquête minimale : sélection d'une source, détail d'une observation, annotations et comparaison élémentaire.

L'architecture graphique reste à arbitrer avant le développement de E. Ne pas imposer prématurément un framework, une application mobile ou une interface matérielle autonome.

Dépendance : CP0.1-D VALIDÉ.

### CP0.1-F — Stabilisation V0.1

NON DÉMARRÉ.

Objectif : stabiliser le parcours complet, tester les erreurs, la déconnexion, la réouverture, la cohérence des résultats et les plateformes explicitement retenues.

Pas de nouvelle capacité ajoutée spontanément.

Dépendance : CP0.1-E VALIDÉ.

## 5. Préserver l'historique des checkpoints

Ancienne planification :

- Ancien C : interface/enquête minimale.
- Ancien D : acquisition USB série.
- Ancien E : stabilisation V0.1.

Nouvelle planification :

- Nouveau C : acquisition USB série.
- Nouveau D : découverte Wi-Fi/BLE.
- Nouveau E : interface Explorer et enquête.
- Nouveau F : stabilisation.

Ces checkpoints futurs n'avaient pas commencé.

Inscrire clairement cette correspondance et la raison du changement dans `ROADMAP.md`.

**Ne pas effacer silencieusement les anciens plans ni leurs objectifs.**

L'évolution est une décision d'organisation, non une validation matérielle.

## 6. Tableau permanent des versions

Conserver les **19 versions numérotées de 0.0.0 à 2.0.0** et le tableau immédiatement sous le titre de `ROADMAP.md`.

Actualiser uniquement la description de `0.1.0` pour représenter :

Fondation, décodage, capture USB réelle, découverte Wi-Fi/BLE initiale et interface Explorer.

Préciser que :

- V0.1 : découverte Wi-Fi/BLE élémentaire, limitée au matériel réellement testé.
- V0.7 : fonctionnalités Bluetooth/USB/HID et authentification plus avancées.
- V0.8 : applications PC/mobile plus complètes et intégration élargie.

Ne pas renuméroter les versions futures ni transformer les propositions en engagements déjà approuvés.

Maintenir la section « À planifier » et toutes les familles FZ/EX.

## 7. Cohérence documentaire à corriger

Vérifier et actualiser au strict nécessaire :

- `ROADMAP.md`
- `WORK_STATE.md`
- `docs/CONTEXT_INDEX.md`
- `docs/VALIDATION.md`, uniquement pour consigner l'audit statique favorable de B, sans inventer d'exécution utilisateur.

Corriger les deux incohérences déjà repérées :

1. CP0.1-A ne doit plus indiquer qu'un checkout Windows propre reste à vérifier : ce test est réussi et documenté.
2. L'index de contexte ne doit plus décrire A comme non validé ni B comme non démarré.

Ajouter le lien de navigation vers `docs/DECODING.md` si nécessaire.

Vérifier les autres renvois qui supposent encore l'ancien ordre C → D → E.

Ne pas modifier les preuves historiques pour réécrire le passé.

## 8. Interdictions et périmètre

Aucun changement de code Python, tests, fixtures, matériel, firmware, archives, contrat de capture ni contrat de décodage.

Ne pas modifier `ASSISTANT_STATE.md` ni `AGENTS.md`.

Ne pas démarrer CP0.1-C.

Aucun test logiciel ou matériel demandé dans cette mission documentaire. Vérifier seulement les liens et la cohérence statique.

Prévol Git obligatoire. Préserver tout travail antérieur.

Aucun reset, clean, revert, rebase destructif, force-push, merge, tag, release, GitHub Actions, PR ou nouvelle branche.

Commit et push autorisés uniquement sur `work/0.1-foundation`.

## 9. Livraison attendue

Restituer :

- Branche et HEAD final.
- Fichiers modifiés.
- Tableau permanent des versions préservé.
- Nouvelle séquence A → B → C → D → E → F.
- Correspondance avec l'ancien plan.
- Statuts exacts de chaque checkpoint.
- Résultat de contrôle des liens.
- Confirmation que le code et les preuves techniques sont inchangés.
- Limites et arbitrages nécessaires avant les prochaines étapes.

**S'arrêter après la réorganisation documentaire.**

Prochaine action : retour à la Session Assistant pour audit de la roadmap et validation locale de CP0.1-B, avant toute implémentation de CP0.1-C.
~~~

## Réponse exacte

~~~text
**Réorganisation documentaire livrée** sur `work/0.1-foundation`.

**HEAD final :** `366f5b9fa1360c2b3c8d84879d3b08b9ce8bfe12`

| Checkpoint | Nouvelle mission             | Statut                                |
| ---------- | ---------------------------- | ------------------------------------- |
| A          | Fondation logicielle         | **VALIDÉ sur Windows**                |
| B          | Moteur de décodage           | **VALIDATION UTILISATEUR EN ATTENTE** |
| C          | Acquisition USB série réelle | NON DÉMARRÉ                           |
| D          | Découverte Wi-Fi/BLE         | NON DÉMARRÉ                           |
| E          | Interface Explorer minimale  | NON DÉMARRÉ                           |
| F          | Stabilisation V0.1           | NON DÉMARRÉ                           |

La roadmap conserve la correspondance : ancien **C → E**, ancien **D → C**, ancien **E → F** ; le nouveau **D** couvre la découverte Wi-Fi/BLE. Le tableau permanent des **19 versions** est conservé.

Fichiers modifiés : `ROADMAP.md`, `WORK_STATE.md`, `docs/CONTEXT_INDEX.md` et `docs/VALIDATION.md`. Aucun lien interne cassé détecté dans ces fichiers. Code et preuves techniques historiques inchangés ; aucun test logiciel ou matériel lancé.

Avant les prochaines étapes restent à arbitrer le prévol et les méthodes de découverte ESP32, ainsi que l’architecture graphique d’Explorer. **Prochaine action :** retour en Session Assistant pour auditer la roadmap et préparer la validation locale de B, avant toute implémentation de C.
~~~

## Synthèse enregistrée

- **Quatre fichiers documentaires modifiés** au commit source vérifié : `ROADMAP.md`, `WORK_STATE.md`, `docs/CONTEXT_INDEX.md` et `docs/VALIDATION.md`. Aucun code ni test modifié dans ce commit.
- **Statuts :** A validé Windows antérieurement ; B en attente de validation utilisateur ; C, D, E et F non démarrés. G accepté selon le prompt.
- **Nouvelle organisation :** ancien C → E, ancien D → C, ancien E → F ; nouveau D consacré à la découverte Wi-Fi/BLE. Tableau permanent de 19 versions préservé selon Work.
- **Vérifications :** aucun test logiciel ou matériel exécuté pendant ce run. Les 24 PASS de CP0.1-B étaient annoncés *avant* le run et non rejoués par l'utilisateur. Contrôle des liens interne sans rupture selon Work.
- **Limite :** `success` signifie réussite de la tâche documentaire, **pas** validation matérielle ou validation utilisateur de CP0.1-B.

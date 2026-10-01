# Run log

Journal chronologique des runs actuellement connus.

> Les pourcentages correspondent au quota visible dans l'interface Work/ChatGPT. Ils ne représentent pas un comptage exact de tokens.

---

## GP-001 — GPT-5.6 Sol Medium — bugs historiques

- Date : 2026-09-26
- Groupe : historical_bug_ab
- Quota : 78 % → 72 % = **6 pts**
- Durée : **1 min 50 s**
- Statut : **succès**
- Prompt : [prompts/benchmark-historical-bugs.md](prompts/benchmark-historical-bugs.md)

### Réponse

> **Deux bugs fonctionnels concrets ont été trouvés.**
>
> 1. gamepanel/candidates.py, discover() : la définition utilise `selected_root`, variable inexistante dans cette fonction, à la place de `root`. Dès qu'une unité éligible atteint cette ligne, Python lève `NameError`. Le scan automatique échoue donc lorsqu'un vrai candidat valide existe.
> 2. gamepanel/candidates.py, discover_manual() : la définition utilise encore `root`, alors que cette variable n'est plus définie et que le chemin canonique est `selected_root`. Une ressource manuelle compatible déclenche donc un `NameError`.
>
> Verdict : **bug(s) concret(s) trouvé(s)**.

Notes : 2/2 bugs attendus, aucun faux positif, chaîne helper/API correctement comprise.

---

## GP-002 — GPT-6 Luna Medium — même benchmark historique

- Date : 2026-09-26
- Groupe : historical_bug_ab
- Quota : 72 % → 72 % = **~0 pt visible**
- Durée : **31 s**
- Statut : **échec avant audit**
- Prompt : [prompts/benchmark-historical-bugs.md](prompts/benchmark-historical-bugs.md)

### Réponse exacte

> Je ne peux pas établir un verdict fiable sur ce commit : le hash `6be3d7da1446aa75f7d836eb631eca3fb5ec264a` est absent des deux dépôts locaux accessibles, et la recherche du hash n’a pas retrouvé le commit. Je ne peux donc pas examiner son parent ni le code exact à auditer.
>
> **Verdict : incertitude nécessitant le commit exact.** Aucun fichier n’a été modifié et aucune opération Git n’a été effectuée.

Note : ce run ne mesure pas réellement la capacité de Luna à trouver les deux bugs ; il mesure surtout son autonomie d'accès à l'état historique.

---

## GP-003 — GPT-6 Sol Medium — même benchmark historique

- Date : 2026-09-26
- Groupe : historical_bug_ab
- Quota : 72 % → 68 % = **4 pts**
- Durée : **1 min 35 s**
- Statut : **succès**
- Prompt : [prompts/benchmark-historical-bugs.md](prompts/benchmark-historical-bugs.md)

### Réponse exacte

> **Deux bugs fonctionnels concrets ont été introduits par `6be3d7d`**, par rapport à son parent `901b186`. Ils se trouvent tous deux dans `gamepanel/candidates.py`.
>
> 1. **Découverte automatique — `discover()`, ligne 471.** La définition d’un candidat utilise `selected_root`, variable inexistante dans cette fonction, à la place de `root`, qui y est bien calculée. Dès qu’une unité éligible atteint cette ligne, Python lève `NameError`. Cette exception n’est pas interceptée par `discover()`. Le scan automatique échoue donc, y compris lors de l’ouverture de la vue d’administration ; l’aperçu et l’enregistrement automatiques ne peuvent plus obtenir ce candidat. C’est une régression certaine : le parent utilisait `root` à cet endroit.
> 2. **Ajout manuel — `discover_manual()`, ligne 605.** La définition de la ressource utilise `root`, alors que cette variable n’est plus définie dans cette fonction depuis le commit ; le dossier validé est conservé dans `selected_root`. Pour une unité compatible, la recherche manuelle atteint cette ligne et lève `NameError`, non interceptée par la boucle. Le scan ne renvoie donc pas la ressource, ce qui bloque son aperçu et son enregistrement. C’est un bug réel sur le nouveau parcours avec dossier sélectionné : le parent définissait `root` avant de l’utiliser.
>
> **Verdict : bug(s) concret(s) trouvé(s).**

---

## GP-004 — GPT-6 Astra Low — même benchmark historique

- Date : 2026-09-26
- Groupe : historical_bug_ab
- Quota : 68 % → 51 % = **17 pts**
- Durée : **1 min 42 s**
- Statut : **succès**
- Prompt : [prompts/benchmark-historical-bugs.md](prompts/benchmark-historical-bugs.md)

### Réponse exacte

> **Deux bugs fonctionnels bloquants sont introduits par ce commit.** Comparaison effectuée avec son parent direct `901b186a1e5269597afff5308cdde83a43dac901`, sans consulter les commits ultérieurs ni modifier de fichier.
>
> **1. La découverte automatique échoue dès qu’un candidat valide est trouvé**
>
> - `gamepanel/candidates.py`, `discover()`, ligne 471 : la définition utilise `"root": selected_root`, alors que `selected_root` n’existe pas dans cette fonction. Le parent utilisait `root`.
> - Chemin : scan automatique → unité acceptée → classification/empreinte valides → construction de la définition → `NameError`.
> - Conséquence : helper `INVENTORY_HELPER_FAILED`, propagé en HTTP 409.
> - Preuve : avec une unité Minecraft simulée valide, le parent retourne un candidat ; le commit audité lève `NameError: name 'selected_root' is not defined`.
>
> **2. L’ajout manuel échoue dès qu’une ressource compatible correspond au dossier**
>
> - `discover_manual()`, ligne 605 : le commit supprime l’affectation locale de `root`, mais conserve `"root": root`. La variable disponible est `selected_root`.
> - Chemin : validation dossier → correspondance systemd → profil compatible → construction de définition → `NameError`.
> - Conséquence : analyse du dossier impossible avant écriture transactionnelle.
> - Preuve : reproduction en mémoire avec les sources historiques exactes.
>
> **Verdict : bug(s) concret(s) trouvé(s).**

Note : même décision finale que Sol Medium, avec davantage de preuve/reproduction.

---

## GP-005 — GPT-6 Sol Medium — lacune fonctionnelle 0.3.0

- Date : 2026-09-26
- Groupe : functional_gap_ab
- Quota : 51 % → 47 % = **4 pts**
- Durée : **1 min 45 s**
- Statut : **succès**
- Prompt : [prompts/benchmark-functional-gap.md](prompts/benchmark-functional-gap.md)

### Réponse exacte

> **Lacune fonctionnelle concrète : l’ajout généralisé proposé par ce commit reste une sélection de candidats détectés automatiquement.**
>
> 1. **Exigence concernée.** La roadmap 0.3.0 et le checkpoint 4 distinguent le jeu connu détecté automatiquement du jeu connu ajouté manuellement, pour lequel l’Admin choisit un profil.
> 2. **Code concerné.** `installer/__main__.py`, `_local_candidate_scan()` et `add_instance()`, avec les filtres de `gamepanel/candidates.py`, `discover()`.
> 3. **Comportement implémenté.** `add_instance()` affiche seulement les candidats issus du scan à motifs de noms fixes, puis copie la définition du candidat choisi. Il ne permet ni de choisir d’abord un profil connu, ni d’indiquer une unité existante que le scan n’a pas retenue. Sans candidat, il s’arrête.
> 4. **Scénario concret.** Un serveur BeamMP existant sous `serveur-principal.service`, avec un exécutable BeamMP reconnu, n’entre pas dans le motif `beammp*.service`. Le nouveau parcours ne le propose pas et ne permet pas de l’ajouter manuellement sous le profil BeamMP.
> 5. **Pourquoi c’est une lacune réelle.** La sécurité du détecteur explique qu’il refuse de proposer automatiquement cette unité ; elle ne réalise pas pour autant le parcours manuel distinct prévu par les documents. Les tests ajoutés couvrent des unités déjà reconnues par le détecteur.
>
> **Verdict : besoin partiellement satisfait avec lacune concrète.**

---

## GP-006 — GPT-6 Astra Low — même lacune fonctionnelle

- Date : 2026-09-26
- Groupe : functional_gap_ab
- Quota : 47 % → 34 % = **13 pts**
- Durée : **1 min 10 s**
- Statut : **succès**
- Prompt : [prompts/benchmark-functional-gap.md](prompts/benchmark-functional-gap.md)

### Réponse exacte

> **Le besoin est partiellement satisfait : le commit ajoute un parcours de sélection de candidats détectés, mais pas le parcours d’ajout manuel d’un profil connu prévu par le checkpoint.**
>
> Audit du commit `d3ecb7c42cb4957deafb39c2d032d1049bd667ab` et de son parent `af83041a5e70cfc2279b1190443b77efea262469`, sans modification ni consultation de commits ultérieurs.
>
> Lacune : `add_instance()` appelle le détecteur automatique existant, filtre ses résultats, puis demande de sélectionner un candidat, jamais un profil indépendamment de la détection. Le Web impose également un candidat détecté et renvoie vers l’assistant local lorsqu’aucun serveur n’est proposé ; cet assistant reproduit donc la même limitation.
>
> Scénario démontré : un BeamMP valide sous `racing-evening.service` produit zéro candidat, alors que la même configuration nommée `beammp-evening.service` produit un candidat BeamMP.
>
> Le parent possédait déjà `add_minecraft()` avec une option « Autre unité existante » : il ne s’agit donc pas d’une suppression du manuel Minecraft mais d’une généralisation incomplète.
>
> **Verdict : besoin partiellement satisfait avec lacune(s) concrète(s).**

Note : même décision finale que Sol Medium, mais preuve plus large et vérification du Web.

---

## GP-007 — GPT-6 Luna Medium — analyse locale ciblée

- Date : 2026-09-26
- Groupe : targeted_local_analysis
- Quota : 34 % → 34 % = **~0 pt visible**
- Durée : **40 s**
- Statut : **succès**
- Prompt : [prompts/benchmark-luna-targeted.md](prompts/benchmark-luna-targeted.md)

### Réponse exacte

> État audité : branche `work/0.3.06-manual-instances`, commit `1afa9c3`. Les contrôles sont dans `gamepanel/candidates.py`, principalement `validate_manual_root`, `_manual_root_relation`, `_manual_unit_records` et `discover_manual`.
>
> 1. Racines : sous-répertoire strict de `/home`, `/srv`, `/opt`, `/var/lib` ou `/mnt`.
> 2. Interdits : `/opt/gamepanel`, `/var/lib/gamepanel`, `/var/lib/gamepanel-inventory` et descendants.
> 3. Refus des chemins non absolus, des composants `..` et des symlinks ; contrôles `lstat` et identité des composants.
> 4. Comparaison device/inode avant/après résolution ; preview/enregistrement relancent `discover_manual` et le resource id détecte un état obsolète. Pas de descripteur ouvert verrouillant l’identité du chemin pendant toute l’utilisation.
> 5. Un `WorkingDirectory` absolu différent fait autorité et bloque le fallback `ExecStart`.
> 6. Lecture systemd groupée puis relecture individuelle ; si rien n’est récupérable, erreur groupée ou `DISCOVERY_FAILED` selon le cas ; les unités individuellement illisibles sont ignorées lorsque d’autres sont récupérées.

Score de référence : **6/6**.

---

## GP-008 — GPT-6 Sol High — réconciliation 0.3.1

- Date : 2026-09-26
- Groupe : reconciliation_031
- Quota : **~20 pts consommés**, le quota restant a été épuisé
- Durée : **12 min 07 s**
- Statut : **partiel**
- Prompt complet : [prompts/GP-008-reconciliation-031.md](prompts/GP-008-reconciliation-031.md)

Aucune réponse finale capturée : le run s’est arrêté en cours de travail.

Interprétation prudente : ce run montre un risque de consommation importante sur un marathon multi-étapes en High ; il ne permet pas de calculer un ratio universel High/Medium.

---

## GP-009 — GPT-6 Sol Medium — reprise de GP-008

- Date : 2026-09-26
- Groupe : reconciliation_031
- Quota : **~5 pts**
- Durée : **2 min 27 s**
- Statut : **succès**

Le run a terminé le travail commencé par GP-008.

Prompt/réponse exacts non capturés avec certitude. Le prompt de reprise proposé demandait explicitement de ne rien recommencer, d’inspecter l’état laissé par le run High et de terminer le checkpoint.

**Limite majeure :** ce run ne signifie pas que Sol Medium aurait effectué toute la réconciliation depuis zéro en 5 points ; il a bénéficié du travail de GP-008.

---

## GP-010 — GPT-6 Luna — incident de fiabilité

- Date : 2026-09-29
- Effort : non relevé
- Durée : **~50 min**
- Quota : non relevé
- Statut : **bloqué, aucun résultat**

Possible incident serveur/outillage. À suivre comme donnée de fiabilité d’exécution, pas comme mesure pure de raisonnement.

---

## GP-011 — GPT-6 Luna — incident de fiabilité

- Date : 2026-09-30
- Effort : non relevé
- Durée : **~45 min**
- Quota : **~5 pts**
- Statut : **bloqué, aucun résultat**

Deuxième incident consécutif signalé entre le 29 et le 30 septembre. Même prudence : origine potentiellement serveur/outillage.

---

## GP-012 — GPT-6.1 Sol Medium — Instances UI

- Date : 2026-09-30
- Quota : 99 % → 88 % = **11 pts**
- Durée : **18 min 37 s**
- Statut : **succès**
- Commit : `7ba38960fd5420e89c508800ddf201fc29086283`
- Prompt + réponse complets : [runs/GP-012-gpt61-sol-medium-instances.md](runs/GP-012-gpt61-sol-medium-instances.md)

Résumé du handoff :

- pré-vol ayant détecté du travail déjà présent et préservé ;
- correction du cas enregistré + conflit ;
- contrats JS PASS ;
- tests Python non importables à cause de dépendances absentes ;
- navigateur N/A ;
- manifeste vérifié partiellement 167/168 à cause d’un PNG non récupérable.

---

## GP-013 — GPT-6.1 Sol Medium — Supervision UI

- Date : 2026-10-01
- Quota : 100 % → 90 % = **10 pts**
- Durée : **10 min 42 s**
- Statut : **succès**
- Commit : `622205debaa8492368a7a4f5dc31acafd6a4bf4c`
- Prompt + réponse complets : [runs/GP-013-gpt61-sol-medium-supervision.md](runs/GP-013-gpt61-sol-medium-supervision.md)

Résumé du handoff :

- Supervision compactée ;
- topbar Administration ;
- logique de disque affichée selon la donnée backend ;
- températures 2/1 colonnes ;
- diagnostic conservé ;
- logout SVG réduit à 1rem ;
- contrats JS PASS ;
- 41 tests Python PASS ;
- syntaxes JS/CJS PASS ;
- manifeste 169/169 PASS ;
- navigateur/responsive N/A faute de Chromium.

---

# Agrégats provisoires

## GPT-6.1 Sol Medium

Deux vrais checkpoints de production :

- quota cumulé : **21 pts**
- durée cumulée : **29 min 19 s**
- succès : **2/2**
- quota moyen brut : **10,5 pts/checkpoint**

Ces deux tâches sont de taille différente mais appartiennent au même contexte UI/UX GamePanel.

## Comparaison directe historique

Sur le benchmark GP-001/002/003/004 :

- GPT-6 Sol Medium : **4 pts**, 1:35, succès 2/2
- GPT-5.6 Sol Medium : **6 pts**, 1:50, succès 2/2
- GPT-6 Astra Low : **17 pts**, 1:42, succès 2/2 avec davantage de preuves
- GPT-6 Luna Medium : **~0 pt**, 0:31, échec avant audit

Sur GP-005/006 :

- GPT-6 Sol Medium : **4 pts**, 1:45
- GPT-6 Astra Low : **13 pts**, 1:10
- même lacune fonctionnelle principale trouvée

Ces résultats sont descriptifs, pas une conclusion universelle sur les modèles.

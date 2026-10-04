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

---

## GP-014 — GPT-6.1 Sol Medium — Admin Utilisateurs UI

- Date : 2026-10-01
- Quota : 68 % → 57 % = **11 pts**
- Durée : **12 min 42 s**
- Statut : **succès**
- Commit : `c9186373341215150053c01fab7cfe8c81f414a3`
- Prompt + réponse complets : [runs/GP-014-gpt61-sol-medium-users.md](runs/GP-014-gpt61-sol-medium-users.md)

Résumé : tableau Utilisateurs conservé et compacté, modales densifiées, libellé Accès, repère « Vous », comportements comptes/grants/sessions préservés ; contrats Web et syntaxes PASS, 5 tests Python disponibles PASS ; autres tests Python bloqués par `aiohttp`, navigateur N/A.

---

## GP-015 — GPT-6.1 Sol Medium — Correctif Sessions Utilisateurs

- Date : 2026-10-01
- Quota : 57 % → 54 % = **3 pts**
- Durée : **5 min 52 s**
- Statut : **succès**
- Commit : `de76ac399e4f805e82de0006d8f07d8cffc32b7b`
- Prompt + réponse complets : [runs/GP-015-gpt61-sol-medium-user-sessions.md](runs/GP-015-gpt61-sol-medium-user-sessions.md)

Correctif unique et très borné : distinction visuelle READY/OFFLINE dans la modale Sessions, avec contrat ciblé, syntaxes, tests et manifeste.

---

## GP-016 — GPT-6 Luna Medium — Palette Utilisateurs

- Date : 2026-10-01
- Quota : 54 % → 53 % = **1 pt**
- Durée : **3 min 42 s**
- Statut : **succès**
- Commit : `5049d507b7150828bf7d81b541c0edaf949d9afa`
- Prompt + réponse complets : [runs/GP-016-gpt6-luna-medium-users-palette.md](runs/GP-016-gpt6-luna-medium-users-palette.md)

Correctif de production très borné : palette graphite neutre appliquée uniquement sous `.users-page`, contrat ciblé et manifeste, sans modification métier ni autre écran.

---

## GP-017 — GPT-6 Luna Medium — Journal d’audit UI

- Date : 2026-10-01
- Quota : 53 % → 53 % = **~0 pt visible**
- Durée : **7 min 47 s**
- Statut : **succès**
- Commit : `4966b61e00a21e1646f3e6dc85110dcc8ee91fca`
- Prompt + réponse complets : [runs/GP-017-gpt6-luna-medium-audit-ui.md](runs/GP-017-gpt6-luna-medium-audit-ui.md)

Harmonisation UI ciblée du Journal d’audit : suppression de l’eyebrow, densité légère, palette graphite scopée et rendu mobile en cartes, sans modification de la logique audit.

---

## GP-018 — GPT-6 Sol Medium — Pré-clôture globale 0.3.1

- Date : 2026-10-01
- Quota : 100 % → 89 % = **11 pts**
- Durée : **8 min 42 s**
- Statut : **succès**
- Commit : `3de9d3a5b92c943ebc3c61086e13d90a0db1902b`
- Prompt + réponse complets : [runs/GP-018-gpt6-sol-medium-preclose-031.md](runs/GP-018-gpt6-sol-medium-preclose-031.md)

Premier gros checkpoint de production GPT-6 Sol Medium observé depuis zéro : audit global de pré-clôture, état de validation, versions/candidate, tests Web/docs et manifeste. Aucun code produit ni écran modifié.

---

## GP-019 — GPT-6 Luna Medium — Validation documentaire finale 0.3.1

- Date : 2026-10-01
- Quota : 88 % → 88 % = **~0 pt visible**
- Durée : **3 min 19 s**
- Statut : **succès**
- Commit : `92df2a3616735521a7479efde58edfa179ffb950`
- Prompt + réponse complets : [runs/GP-019-gpt6-luna-medium-final-validation.md](runs/GP-019-gpt6-luna-medium-final-validation.md)

Checkpoint documentaire final 0.3.1 : enregistrement des PASS desktop/mobile/runtime/update et du parcours BeamMP réel REQUALIFIÉ puis CONSERVÉ/SKIPPÉ, sans changement de code.

---

## GP-020 — GPT-6 Sol Medium — 0.3.1-E-A contrat identité d’instance

- Date : 2026-10-01
- Quota : 88 % → 66 % = **22 pts**
- Durée : **14 min 13 s**
- Statut : **succès**
- Commit : `1a835501ff7b5a563f0b906c5b9177f407a3bdd2`
- Prompt + réponse complets : [runs/GP-020-gpt6-sol-medium-identity-contract.md](runs/GP-020-gpt6-sol-medium-identity-contract.md)

Audit transversal 0.3.1-E-A : cartographie de l’identité d’instance dans l’inventaire, SQLite, runtime et intégrations, puis définition d’une architecture unique création + rename avec transaction/recovery. Aucun code fonctionnel modifié.

---

## GP-021 — GPT-6.1 Sol Medium — 0.3.1-E-B1 bloqué par l’environnement

- Date : 2026-10-01
- Quota : 62 % → 57 % = **5 pts**
- Durée : **4 min 31 s**
- Statut : **bloqué avant implémentation**
- Commit GamePanel : **aucun**
- Prompt + réponse complets : [runs/GP-021-gpt61-sol-medium-b1-blocked.md](runs/GP-021-gpt61-sol-medium-b1-blocked.md)

Pré-audit utile mais objectif non atteint : B1 n’a pas été implémenté ni commité. Les tests crash/locks POSIX exigés n’étaient pas exécutables dans l’environnement Windows ; le modèle a arrêté plutôt que de livrer une primitive de sûreté non démontrée.

---

## GP-022 — GPT-6 Luna Medium — B1c fixture no-op isolation

- Date : 2026-10-02
- Quota : 100 % → 99 % = **1 pt**
- Durée : **3 min 29 s**
- Statut : **succès vérifié sur le dépôt distant**
- Commit : `3c6c7e1c050310e779c2b838799cd7dbc87e0286`
- Prompt complet : [runs/GP-022-gpt6-luna-medium-b1c-fixture.md](runs/GP-022-gpt6-luna-medium-b1c-fixture.md)
- Réponse Work : non fournie.

Le commit distant a été vérifié : parent attendu, message exact, diff limité au fixture/test + état/docs/manifeste, sans modification du protocole de production.

---

## GP-023 — GPT-6 Luna Medium — B1d compatibilité installateur historique

- Date : 2026-10-02
- Quota : 99 % → 99 % = **~0 pt visible**
- Durée : **3 min 32 s**
- Statut : **succès**
- Commit : `45d4a3872d727677378443fe700e19c42a2ef90b`
- Prompt + réponse complets : [runs/GP-023-gpt6-luna-medium-installer-compat.md](runs/GP-023-gpt6-luna-medium-installer-compat.md)

Correctif réel de code : `write_inventory()` distingue les DB historiques sans `settings` des DB modernes, tout en gardant le contrôle d’alias strict et fail-closed. Work : 17 tests PASS, 20 root/runtime SKIP ; suites 021/022/023 N/A sous Windows.

---

## GP-024 — GPT-6 Sol Medium — Clôture documentaire 0.3.1-E-B1

- Date : 2026-10-02
- Quota : 99 % → 93 % = **6 pts**
- Durée : **3 min 21 s**
- Statut : **succès**
- Commit : `ca16063343009337cbc08118c1e8f11c46acb8eb`
- Prompt + réponse complets : [runs/GP-024-gpt6-sol-medium-b1-validation-close.md](runs/GP-024-gpt6-sol-medium-b1-validation-close.md)

Clôture documentaire de B1 après validations Ubuntu déjà acquises : 37/37 identity sous chacun des umasks `0002` et `022`, 99/99 régressions ciblées et 105/105 installateur. Aucun code fonctionnel ni test modifié.

---

## GP-025 — GPT-6.1 Sol Medium — 0.3.1-E-B2 API Admin identité

- Date : 2026-10-02
- Quota : 93 % → 77 % = **16 pts**
- Durée : **21 min 37 s**
- Statut : **succès**
- Commit : `68d9a0dc99cf775bcde4f50a751f37553f2efe41`
- Prompt + réponse complets : [runs/GP-025-gpt61-sol-medium-identity-admin-b2.md](runs/GP-025-gpt61-sol-medium-identity-admin-b2.md)

Checkpoint fonctionnel B2 : API Admin d’identité et création d’instance avec id/nom personnalisés. Work : 29 tests portables PASS ; 34 tests natifs N/A dans l’environnement Windows ; validation Ubuntu encore requise.

---

## GP-026 — GPT-6 Luna Medium — Clôture documentaire 0.3.1-E-B2

- Date : 2026-10-02
- Quota : 77 % → 77 % = **~0 pt visible**
- Durée : **4 min 52 s**
- Statut : **succès**
- Commit : `e02109326cc8bca60cd945a19cf89740c727a1e0`
- Prompt + réponse complets : [runs/GP-026-gpt6-luna-medium-b2-validation-close.md](runs/GP-026-gpt6-luna-medium-b2-validation-close.md)

Clôture documentaire de B2 après validations Ubuntu déjà acquises : 63/63 identité, 99/99 régressions ciblées et 105/105 installateur PASS. Aucun code fonctionnel ni test modifié.

---

## GP-027 — GPT-6.1 Sol Medium — 0.3.1-E-C UI Admin identité

- Date : 2026-10-02
- Quota : 77 % → 60 % = **17 pts**
- Durée : **26 min 31 s**
- Statut : **succès**
- Commit : `11f19845baf275c2765e93454b3a3e8aed8b9bb8`
- Prompt + réponse complets : [runs/GP-027-gpt61-sol-medium-identity-ui-ec.md](runs/GP-027-gpt61-sol-medium-identity-ui-ec.md)

Checkpoint UI/UX fonctionnel E-C : gestion d’identité dans Admin > Instances, création auto/manuelle avec id/nom personnalisés, retrait du contrôle d’identité du dashboard normal. 7 contrats Web et 21 vérifications syntaxiques PASS ; 11 contrats navigateur N/A faute de Playwright ; validation visuelle Ubuntu encore requise.

---

## GP-028 — GPT-6 Sol Medium — blocker installer/startup identity recovery

- Date : 2026-10-02
- Quota : 60 % → 39 % = **21 pts**
- Durée : **20 min 35 s**
- Statut : **succès**
- Commit : `f4bd104f5f9a401ae9c429176ee839b03ba704ae`
- Prompt + réponse complets : [runs/GP-028-gpt6-sol-medium-installer-startup-recovery.md](runs/GP-028-gpt6-sol-medium-installer-startup-recovery.md)

Correctif de sûreté/concurrence : le startup contrôlé par l’installateur dispose d’un fast-path `identity-recover` strictement borné, sans affaiblir le recovery B1 normal ni le rename. Work : 35 tests Python et deux contrats Web PASS ; 43 scénarios natifs N/A ; update Ubuntu réelle encore requise.

---

## GP-029 — GPT-6 Luna Medium — fixture cleanup installer identity marker

- Date : 2026-10-02
- Quota : 100 % → 99 % = **1 pt**
- Durée : **3 min 11 s**
- Statut : **succès**
- Commit : `b78d765b1dbbb5a3a84a7d0c86bb2350a3ea5476`
- Prompt + réponse complets : [runs/GP-029-gpt6-luna-medium-installer-marker-fixture.md](runs/GP-029-gpt6-luna-medium-installer-marker-fixture.md)

Correctif de fixture uniquement : `installing()` nettoie désormais le marker qu’il a créé avant de relâcher le lock ; aucun code de production modifié. Work : 23 tests PASS, 22 tests POSIX N/A, compileall et diff-check PASS ; Ubuntu à rejouer.

---

## GP-030 — GPT-6 Luna Medium — contrat manuel E-C

- Date : 2026-10-02
- Quota : 99 % → 99 % = **~0 pt visible**
- Durée : **4 min 14 s**
- Statut : **succès**
- Commit : `8dff817dbb48c2c716fb0af5d4827cd803b3dd73`
- Prompt + réponse complets : [runs/GP-030-gpt6-luna-medium-manual-contract.md](runs/GP-030-gpt6-luna-medium-manual-contract.md)

Correction de contrat de test uniquement : le payload manuel attendu est désormais `path + instance_id/display_name`, sans propriété technique injectable. Aucun code de production modifié. La commande Ubuntu du handoff fourni est archivée telle quelle, tronquée en fin de réponse.

---

## GP-031 — GPT-6 Luna Medium — 0.3.1-E-D validation/clôture

- Date : 2026-10-02
- Quota : 99 % → 97 % = **2 pts**
- Durée : **12 min 53 s**
- Statut : **succès**
- Commit : `554b1d783e96a708b46b81252bfaf12e7f8dd10c`
- Prompt + réponse complets : [runs/GP-031-gpt6-luna-medium-e-d-closure.md](runs/GP-031-gpt6-luna-medium-e-d-closure.md)

Checkpoint documentaire de clôture E-D : 282/282 tests Ubuntu consignés PASS, update réelle post-correctif PASS, validation E-C desktop/mobile PASS, avec deux N/A volontaires conservés sans les transformer en PASS. Aucun code de production modifié.

---

## GP-032 — GPT-6 Luna Medium — pré-clôture documentaire 0.3.1

- Date : 2026-10-02
- Quota : 97 % → 96 % = **1 pt**
- Durée : **13 min 59 s**
- Statut : **succès vérifié sur le dépôt distant**
- Commit : `b67ac81851024fc4c30f85785f4f790633a90f0c`
- Prompt + réponse complets : [runs/GP-032-gpt6-luna-medium-preclose-docs.md](runs/GP-032-gpt6-luna-medium-preclose-docs.md)

Checkpoint documentaire de pré-clôture : état stable/candidate, README, validation/changelog et description de la Draft PR #19 alignés. `test_release_docs` PASS ; `test_version_031` N/A faute d’`aiohttp` ; `git diff --check` PASS ; manifeste 181 entrées valide sans `undefined`. Aucun code de production modifié.

---

## GP-033 — GPT-6.1 Sol Medium — 0.3.2-A bloqué au pré-vol

- Date : 2026-10-02
- Quota : 95 % → 94 % = **1 pt**
- Durée : **17 s**
- Statut : **bloqué au pré-vol conformément au contrat**
- Commit GamePanel : **aucun**
- Prompt + réponse complets : [runs/GP-033-gpt61-sol-medium-032a-preflight-block.md](runs/GP-033-gpt61-sol-medium-032a-preflight-block.md)

Le miroir Work était encore sur `work/0.3.1-ui-ux`, au HEAD `7ba38960...`, avec 27 fichiers modifiés et 13 non suivis. Le prompt imposait explicitement STOP dans cet état. Le dépôt distant `main` a ensuite été vérifié séparément au HEAD attendu `b7700370...`; aucune branche 0.3.2 n’a été créée.

---

## GP-034 — GPT-6.1 Sol Medium — 0.3.2-A contrat manifestes/contenu

- Date : 2026-10-02
- Quota : 94 % → 78 % = **16 pts**
- Durée : **24 min 29 s**
- Statut : **succès**
- Commit : `2c61b30a07859ced630d2dd8a01c5b9c3e786d28`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-034-gpt61-sol-medium-032a-content-manifest-contract.md](runs/GP-034-gpt61-sol-medium-032a-content-manifest-contract.md)

Reprise réussie après GP-033 via un worktree propre séparé. Checkpoint 0.3.2-A documentaire/architectural livré : contrat manifestes, stockage, publication, classification, sécurité/RBAC, rename/recovery et découpage B→F. Aucun code de production, migration, scanner, provider, API, UI ou content store fonctionnel ajouté.

---

## GP-035 — GPT-6.1 Sol Medium — 0.3.2-B scanner Minecraft local

- Date : 2026-10-02
- Quota : 78 % → 66 % = **12 pts**
- Durée : **20 min 49 s**
- Statut : **succès**
- Commit : `24d675b1097ab22d079462a7286627b422035218`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-035-gpt61-sol-medium-032b-minecraft-scanner.md](runs/GP-035-gpt61-sol-medium-032b-minecraft-scanner.md)

Premier checkpoint fonctionnel 0.3.2 : scanner Minecraft local read-only et borné, support prioritaire Forge/NeoForge, SHA-256/métadonnées locales et protections archive/path. 25 tests scanner portables + 18 régressions PASS ; 15 tests POSIX et certaines suites dépendantes de pydantic/aiohttp N/A. B reste candidate sans validation Linux réelle.

---

## GP-036 — GPT-6 Luna Medium — clôture Ubuntu 0.3.2-B

- Date : 2026-10-02
- Quota : 66 % → 66 % = **~0 pt visible**
- Durée : **3 min 19 s**
- Statut : **succès**
- Commit : `940103457a394ed7636b3739a41482c029a73ce5`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-036-gpt6-luna-medium-032b-ubuntu-closure.md](runs/GP-036-gpt6-luna-medium-032b-ubuntu-closure.md)

Clôture documentaire de B après validation Ubuntu réelle : scanner **40/40 PASS sans skip**, régressions ciblées PASS, manifeste 184 empreintes PASS, release docs et diff-check PASS. Aucun code fonctionnel modifié ; B est désormais acquis.

---

## GP-037 — GPT-6.1 Sol Medium — 0.3.2-C providers/classification

- Date : 2026-10-02
- Quota : 66 % → 49 % = **17 pts**
- Durée : **33 min 55 s**
- Statut : **succès**
- Commit : `fc6fcaef584ad1d7eaf0fd99f917acdea5761c98`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-037-gpt61-sol-medium-032c-providers-classification.md](runs/GP-037-gpt61-sol-medium-032c-providers-classification.md)

Checkpoint fonctionnel C livré : providers JAR local, Modrinth, CurseForge, Packwiz/mrpack ; classification déterministe, provenance, conflits, overrides Admin et cache interne. C 58 + B 25 + SQL/docs 18 PASS ; compilation, diff-check et manifeste 189/189 PASS. Les 16 tests POSIX et certaines suites dépendantes de pydantic/aiohttp restent N/A. C reste candidate.

---

## GP-038 — GPT-6 Luna Medium — clôture Ubuntu 0.3.2-C

- Date : 2026-10-03
- Quota : 100 % → 99 % = **1 pt**
- Durée : **4 min 17 s**
- Statut : **succès**
- Commit : `bb0dddcd15386aaff81c8d3c9cc1a93bb750e148`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-038-gpt6-luna-medium-032c-ubuntu-closure.md](runs/GP-038-gpt6-luna-medium-032c-ubuntu-closure.md)

Clôture documentaire de C après validation Ubuntu réelle : tests C+B PASS, tests POSIX exécutés sans skip, régressions ciblées PASS, manifeste 189/189 et diff-check PASS. Aucun code fonctionnel modifié ; A/B/C sont désormais acquis sur la Draft PR #22.

---

## GP-039 — GPT-6.1 Sol Medium — 0.3.2-D UI Admin contenus client

- Date : 2026-10-03
- Quota : 99 % → 88 % = **11 pts**
- Durée : **16 min 49 s**
- Statut : **succès**
- Commit : `39f753261918a2bf1870a6eec4c44ae5d7e22fab`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-039-gpt61-sol-medium-032d-admin-ui.md](runs/GP-039-gpt61-sol-medium-032d-admin-ui.md)

Checkpoint UI D livré : interface Admin distinguant inventaire/brouillon/versions publiées, preuves/conflits, overrides et client-extra locaux non persistés. 8 contrats Web, syntaxe de 23 JS/CJS, release-docs, diff-check et manifeste 191/191 PASS ; Chromium/Playwright N/A, responsive validé statiquement seulement. Aucun backend/API content ni persistance E.

---

## GP-040 — GPT-6 Luna Medium — clôture Ubuntu/Chromium 0.3.2-D

- Date : 2026-10-03
- Quota : 88 % → 88 % = **~0 pt visible**
- Durée : **4 min 35 s**
- Statut : **succès**
- Commit : `7787223bd9f912e0e1d987e8670161dd0f0f059f`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-040-gpt6-luna-medium-032d-ubuntu-chromium-closure.md](runs/GP-040-gpt6-luna-medium-032d-ubuntu-chromium-closure.md)

Clôture documentaire de D après validation réelle Ubuntu/Chromium : contrats UI/navigateur PASS, responsive 1440/1150/760/390 sans overflow, interactions override/client-extra et régressions UI ciblées PASS. Aucun code fonctionnel modifié ; A/B/C/D sont acquis, E/F non commencés.

---

## GP-041 — GPT-6.1 Sol High — 0.3.2-E2 partiel/interrompu

- Date : 2026-10-03
- Quota : 72 % → 52 % = **20 pts**
- Durée : **53 min 27 s**
- Statut : **partiel**
- Commit GamePanel : **aucun**
- Prompt + réponse partielle complets : [runs/GP-041-gpt61-sol-high-032e2-partial.md](runs/GP-041-gpt61-sol-high-032e2-partial.md)

Le run rapporte une implémentation locale avancée d’E2 : canonicalisation stricte, store privé, publication atomique/recovery et tests aux frontières de crash. Work annonçait **34 tests E2 PASS** et **29 POSIX N/A**, puis la réponse s’est arrêtée pendant « Réflexion en cours » avant handoff final. Vérification externe : la PR #22 est restée exactement sur le HEAD initial `e964cb8...`, donc aucun commit/push E2 n’a été livré.

---

## GP-042 — GPT-6.1 Sol Medium — audit de récupération E2

- Date : 2026-10-03
- Quota : 99 % → 98 % = **1 pt**
- Durée : **4 min 02 s**
- Statut : **succès**
- Commit GamePanel : **aucun, conformément au prompt**
- Prompt + réponse complets : [runs/GP-042-gpt61-sol-medium-032e2-recovery-audit.md](runs/GP-042-gpt61-sol-medium-032e2-recovery-audit.md)

Checkpoint de récupération après l’interruption GP-041 : état Git et fichiers E2 locaux établis, travail jugé récupérable, risques/manifeste incohérent recensés et recommandation de reprendre l’existant. STOP respecté sans modification, commit, push, reset ou cleanup. La PR #22 est restée sur `e964cb8...` comme attendu.

---

## GP-043 — GPT-6.1 Sol High — finalisation 0.3.2-E2

- Date : 2026-10-03
- Quota : 97 % → 90 % = **7 pts**
- Durée observée : **28 min 50 s**
- Note durée : **biaisée par une demande d’autorisation**
- Statut : **succès**
- Commit : `c3f335a52426f8c8a8ba18f816801aec0ef20ec9`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-043-gpt61-sol-high-032e2-completion.md](runs/GP-043-gpt61-sol-high-032e2-completion.md)

Reprise du travail E2 local interrompu : audit du diff existant, corrections ciblées, validation Work puis commit/push. E2 **38 PASS / 31 N/A POSIX**, E1/identity/startup/docs **53 PASS / 51 N/A**, B/C **83 PASS / 16 N/A**, manifeste **197/197**. E2 reste candidat et aucun PASS Ubuntu/POSIX non exécuté n’est revendiqué.

---

## GP-044 — GPT-6 Luna Medium — correctif fixture staging E2

- Date : 2026-10-03
- Quota : 90 % → 89 % = **1 pt**
- Durée : **3 min 28 s**
- Statut : **succès**
- Commit : `463e0cccdb70f12eb2ec139df5992d72c24d1608`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-044-gpt6-luna-medium-e2-staging-fixture.md](runs/GP-044-gpt6-luna-medium-e2-staging-fixture.md)

Correctif ultra-ciblé du fixture E2 : priorité d’opérateurs corrigée dans le chemin de staging, puis manifeste régénéré. Exécution locale : **38 PASS / 31 ignorés POSIX**, aucun échec ; manifeste et diff-check PASS. Le **69/69 Ubuntu reste à confirmer** et n’est pas revendiqué comme exécuté.

---

## GP-045 — GPT-6 Luna Medium — clôture Ubuntu 0.3.2-E2

- Date : 2026-10-03
- Quota : 89 % → 89 % = **~0 pt visible**
- Durée : **5 min 19 s**
- Statut : **succès**
- Commit : `6fd46e5cbafb22bde1fba96f335b275e3be2cde9`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-045-gpt6-luna-medium-032e2-ubuntu-closure.md](runs/GP-045-gpt6-luna-medium-032e2-ubuntu-closure.md)

Clôture documentaire de E2 après validation Ubuntu réelle : `tests.test_content_publication_032` **69/69 PASS sans skip inattendu**, suites E1/identity/startup/acceptance/migrations/version/release-docs et B/C ciblées PASS. Dans Work : release-docs, manifeste 197/197 et diff-check PASS. Aucun code fonctionnel modifié ; E2 est acquis, E global reste non acquis.

---

## GP-046 — GPT-6.1 Sol Medium — 0.3.2-E3-A API Admin content

- Date : 2026-10-03
- Quota : 89 % → 66 % = **23 pts**
- Durée : **38 min 45 s**
- Statut : **succès**
- Commit : `0c8f2c42dd72b4d9701fb55994f6e060e13cff07`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-046-gpt61-sol-medium-032e3a-admin-content-api.md](runs/GP-046-gpt61-sol-medium-032e3a-admin-content-api.md)

Checkpoint fonctionnel E3-A livré : routes Admin content pour état, scan, draft, publication/retry et révocation, avec orchestration réelle B/C/E2. Tests ciblés **20 PASS / 26 N/A** ; régressions **79/35**, **83/16**, **12/47** PASS/N/A ; compile, diff-check et manifeste **200/200 PASS**. E3-A reste candidat, validation Ubuntu encore requise.

---

## GP-047 — GPT-6 Luna Medium — clôture Ubuntu 0.3.2-E3-A

- Date : 2026-10-03
- Quota : 66 % → 65 % = **1 pt**
- Durée : **4 min 40 s**
- Statut : **succès**
- Commit : `44d49fead0123099784e32f2bcf3be4304611fef`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-047-gpt6-luna-medium-032e3a-ubuntu-closure.md](runs/GP-047-gpt6-luna-medium-032e3a-ubuntu-closure.md)

Clôture documentaire de E3-A après validation Ubuntu réelle : `tests.test_content_admin_032` **46/46 PASS sans skip inattendu**, régressions E2/E1/identity/startup/release-docs, acceptance/security/migrations/version et B/C ciblées PASS. Aucun code fonctionnel modifié ; E3-A est acquis, E global reste non acquis.

---

## GP-048 — GPT-6.1 Sol High — 0.3.2-E3-B distribution HTTP + client-extra

- Date : 2026-10-03
- Quota : 65 % → 41 % = **24 pts**
- Durée : **42 min 00 s**
- Statut : **succès vérifié sur le dépôt distant**
- Commit : `5d4b0301f54ea8ba93d63dc305c8896f7f958283`
- Draft PR : **#22**
- Prompt + réponse partielle : [runs/GP-048-gpt61-sol-high-032e3b-distribution-client-extra.md](runs/GP-048-gpt61-sol-high-032e3b-distribution-client-extra.md)

E3-B livré malgré un stall apparent de l’UI Work après les dernières exécutions : distribution HTTP autorisée GET/HEAD/ETag/304/Range/If-Range, streaming avec revalidation session/grant/révocation et transport Admin client-extra borné. PR #22 mise à jour avec E3-B candidat. Work : **21 PASS / 21 N/A** E3-B, régressions **120/82** et **95/63** PASS/N/A ; compile/release-docs/diff/manifeste PASS. Validation Ubuntu HTTP/POSIX native encore requise.

---

## GP-049 — GPT-6 Luna Medium — fixture timeout E3-B bloqué par environnement

- Date : 2026-10-04
- Quota : 100 % → 100 % = **~0 pt visible**
- Durée : **2 min 15 s**
- Statut : **bloqué par l’environnement après correctif local**
- Commit GamePanel : **aucun**
- Prompt + réponse complets : [runs/GP-049-gpt6-luna-medium-e3b-timeout-fixture-block.md](runs/GP-049-gpt6-luna-medium-e3b-timeout-fixture-block.md)

Le fixture de timeout client-extra a été corrigé localement selon la réponse, avec **21 PASS / 21 N/A** sous Windows, manifeste **203/203** et diff-check PASS. Le venv Ubuntu demandé était absent et WSL inaccessible ; le **42/42 Ubuntu** exigé avant commit n’a pas pu être exécuté. La PR #22 est donc restée sur `5d4b0301...`.

---

## GP-050 — GPT-6 Luna Medium — push du correctif fixture timeout E3-B

- Date : 2026-10-04
- Quota : 100 % → 99 % = **1 pt**
- Durée : **4 min 03 s**
- Statut : **succès**
- Commit : `bb5da9dfe35fbb46ddea3b505d61bc122de40022`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-050-gpt6-luna-medium-e3b-timeout-fixture-push.md](runs/GP-050-gpt6-luna-medium-e3b-timeout-fixture-push.md)

Reprise du correctif local laissé par GP-049 et push effectif. Le commit ne touche que le test de timeout E3-B et le manifeste. Work : **42 exécutés, 21 PASS / 21 N/A** natifs, manifeste et diff-check PASS ; le **42/42 Ubuntu** attendu n’est pas revendiqué comme exécuté.

---

## GP-051 — GPT-6 Luna Medium — clôture Ubuntu 0.3.2-E3-B

- Date : 2026-10-04
- Quota : 99 % → 98 % = **1 pt**
- Durée : **7 min 46 s**
- Statut : **succès**
- Commit : `94fbabc86ae658cb24a81df40f374885e849b997`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-051-gpt6-luna-medium-032e3b-ubuntu-closure.md](runs/GP-051-gpt6-luna-medium-032e3b-ubuntu-closure.md)

Clôture documentaire de E3-B après validation Ubuntu réelle : `tests.test_content_distribution_032` **42/42 PASS sans skip inattendu**, suites E3-A/E2/E1/identity/startup/release-docs, acceptance/security/migrations/version et B/C ciblées PASS. Aucun code fonctionnel modifié ; E3-B est acquis, E global reste non acquis.

---

## GP-052 — GPT-6.1 Sol Medium — 0.3.2-E3-C UI Admin content réelle

- Date : 2026-10-04
- Quota : 98 % → 82 % = **16 pts**
- Durée : **18 min 52 s**
- Statut : **succès**
- Commit : `3de856089a389e7afa35a8f1606f8c0d395505c5`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-052-gpt61-sol-medium-032e3c-admin-ui-api.md](runs/GP-052-gpt61-sol-medium-032e3c-admin-ui-api.md)

E3-C candidat livré sans modification backend : l’UI Admin Contenus client utilise les API réelles pour état, scan, draft, upload client-extra brut, publication/retry et révocation. Contrat content, sept régressions UI 0.3.1, syntaxes JS/CJS, release-docs, manifeste **204/204** et diff-check PASS. Chromium réel N/A dans Work car Playwright absent ; validation Ubuntu/Chromium encore requise avant acquisition E3-C.

---

## GP-053 — GPT-6 Luna Medium — clôture Ubuntu/Chromium 0.3.2-E3-C

- Date : 2026-10-04
- Quota : 82 % → 81 % = **1 pt**
- Durée : **6 min 06 s**
- Statut : **succès**
- Commit : `9c37a5623e71eda0dde077ad15b8eb1314abb09f`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-053-gpt6-luna-medium-032e3c-ubuntu-chromium-closure.md](runs/GP-053-gpt6-luna-medium-032e3c-ubuntu-chromium-closure.md)

Clôture documentaire de E3-C après validation Ubuntu/Chromium réelle : contrats Web, flux complet scan → draft → stale → client-extra → publication → révocation, réponse tardive ignorée, responsive 1440/1150/760/390 et sept régressions UI 0.3.1 PASS. E3-C et E global sont acquis ; F reste non commencé.

---

## GP-054 — GPT-6.1 Sol Medium — 0.3.2-F runbook validation réelle

- Date : 2026-10-04
- Quota : 81 % → 64 % = **17 pts**
- Durée : **22 min 13 s**
- Statut : **succès**
- Commit : `9b4cdb4ae07e6bc0679e0d55e2a642c1436addbb`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-054-gpt61-sol-medium-032f-real-validation-runbook.md](runs/GP-054-gpt61-sol-medium-032f-real-validation-runbook.md)

Runbook F réel préparé en **11 gates avec STOP**, couvrant sauvegarde/rollback, observations Interstice/Aero, drafts contrôlés, client-extra, publication/digests/immutabilité, autorisations, rename/recovery isolé et nettoyage/preuves. Work : release-docs **1/1 PASS**, syntaxe des exemples, manifeste **205/205** et diff-check PASS. Validation réelle F non exécutée ; rename/recovery reste bloqué sans VM Ubuntu + ressource explicitement jetable.

---

## GP-055 — GPT-6.1 Sol Medium — correctif fixture ContentStore Ubuntu

- Date : 2026-10-04
- Quota : 100 % → 94 % = **6 pts**
- Durée : **5 min 04 s**
- Statut : **succès**
- Commit : `0f3f408c598c2f6575a211b7595309cf7492ea56`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-055-gpt61-sol-medium-content-store-fixture-fix.md](runs/GP-055-gpt61-sol-medium-content-store-fixture-fix.md)

Diagnostic confirmé : la fixture créait un staging orphelin avant recovery et déclenchait correctement `CONTENT_JOURNAL_ORPHAN`. Le test conserve création/fsync puis nettoie le staging via `cleanup()` avant startup ; aucun code de production n’est modifié. Work Windows : store **3 PASS / 7 N/A**, régressions **97 PASS / 100 N/A**, compileall/release-docs/manifeste/diff-check PASS ; validation Ubuntu encore requise. F reste non acquis.

## GP-056 — GPT-6.1 Sol Medium — correctif scanner Minecraft O_PATH

- Date : 2026-10-04
- Quota : 94 % → 89 % = **5 pts**
- Durée : **6 min 50 s**
- Statut : **succès**
- Commit : `fad9b8b39a12199749c3e4b91710d4c7380944a4`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-056-gpt61-sol-medium-minecraft-scanner-opath.md](runs/GP-056-gpt61-sol-medium-minecraft-scanner-opath.md)

Le blocker réel du scan Aero est rapporté comme corrigé : les ancêtres absolus search-only utilisent désormais `O_PATH`, tandis que le root final et les parcours réellement scannés restent en `O_RDONLY`. Ancrage/no-follow conservés et aucune permission système modifiée. Work Windows : scanner **27 PASS / 24 N/A**, régressions **149 PASS / 108 N/A**, compileall/release-docs/manifeste/diff-check PASS. Tests Ubuntu natifs à rejouer ; **F reste non acquis**.

---

## GP-057 — GPT-6.1 Sol Medium — policy JAR réelle Minecraft

- Date : 2026-10-04
- Quota : 89 % → 84 % = **5 pts**
- Durée : **7 min 02 s**
- Statut : **succès**
- Commit : `46a52600adea741358a772655465ff5005a0f991`
- Draft PR : **#22**
- Prompt + réponse complets : [runs/GP-057-gpt61-sol-medium-minecraft-jar-policy.md](runs/GP-057-gpt61-sol-medium-minecraft-jar-policy.md)

Adaptation rapportée de la policy archive/JAR aux mods Aero réels : `:` admis seulement dans les noms ZIP internes, chemins filesystem toujours stricts, gros MANIFEST traité sous borne avec CRC complet. Limites finales : **32 768 entrées**, central **4 MiB**, métadonnée **2 MiB**, total **4 MiB**. Work Windows : scanner **33 PASS / 24 N/A**, régressions **129 PASS / 87 N/A**, compileall/release-docs/manifeste/diff-check PASS. **F et Gate 4 restent non acquis**.

---

# Agrégats provisoires

## GPT-6 Sol Medium

Sept succès observés :

- quota cumulé : **~73 pts**
- durée cumulée : **52 min 38 s**
- succès : **7/7**
- moyenne brute : **~10,43 pts/run**
- audits autonomes ciblés : **4 pts / 1:35** et **4 pts / 1:45**
- reprise de réconciliation déjà entamée : **~5 pts / 2:27**
- gros checkpoints de production depuis zéro : **11 pts / 8:42** pour la pré-clôture, **22 pts / 14:13** pour l’audit transversal identité/persistance 0.3.1-E-A, puis **21 pts / 20:35** pour le correctif concurrence installer/recovery GP-028
- clôture documentaire B1 après validation Ubuntu acquise : **6 pts / 3:21**

La moyenne brute mélange des tâches de tailles très différentes. GP-018, GP-020 et GP-028 montrent que les gros checkpoints Sol Medium s’étendent actuellement de **11 à 22 pts** selon la profondeur : pré-clôture globale, audit architecture/persistance, puis correctif de sûreté/concurrence installateur/recovery. GP-024 reste un checkpoint documentaire plus léger à **6 pts**.

## GPT-6 Luna

Vingt-quatre observations au total, dont **deux incidents ont un effort non relevé** et sont séparés des runs Medium.

### Medium

- observations : **22**
- succès : **20**
- blocage environnemental : **1**
- échec avant audit : **1**
- quota visible cumulé : **12 pts**
- durée cumulée : **1 h 47 min 57 s**
- production ciblée récente : **19 succès / 1 blocage**, **12 pts visibles cumulés**, **1 h 46 min 46 s**
- détail des succès ciblés : **~0 pt / 40 s** sur l'analyse locale 6/6, **1 pt / 3:42** sur le correctif palette Utilisateurs, **~0 pt / 7:47** sur le Journal d’audit, **~0 pt / 3:19** sur la validation documentaire finale, **1 pt / 3:29** sur le fixture B1c, **~0 pt / 3:32** sur la compatibilité installateur B1d, **~0 pt / 4:52** sur la clôture documentaire B2, **1 pt / 3:11** sur le cleanup du fixture installer marker, **~0 pt / 4:14** sur le contrat manuel E-C, **2 pts / 12:53** sur la clôture documentaire E-D, **1 pt / 13:59** sur la pré-clôture documentaire 0.3.1, **~0 pt / 3:19** sur la clôture Ubuntu de 0.3.2-B, **1 pt / 4:17** sur la clôture Ubuntu de 0.3.2-C, **~0 pt / 4:35** sur la clôture Ubuntu/Chromium de 0.3.2-D, **1 pt / 3:28** sur le correctif fixture staging E2, **~0 pt / 5:19** sur la clôture Ubuntu de 0.3.2-E2, **1 pt / 4:40** sur la clôture Ubuntu de 0.3.2-E3-A, **~0 pt / 2:15** sur le fixture timeout E3-B bloqué faute d’Ubuntu/WSL, puis **1 pt / 4:03** sur la reprise/push de ce correctif, puis **1 pt / 7:46** sur la clôture Ubuntu de 0.3.2-E3-B, puis **1 pt / 6:06** sur la clôture Ubuntu/Chromium de 0.3.2-E3-C avec E global acquis.

### Incidents à effort non relevé

- observations : **2**
- blocages : **2**
- quota connu : **≥5 pts**, avec GP-010 sans relevé
- durée cumulée : **1 h 35 min 00 s**

### Total Luna, tous efforts confondus

- observations : **24**
- résultats : **20 succès · 1 échec · 3 blocages**
- quota connu : **≥17 pts**
- durée cumulée : **3 h 22 min 57 s**

Les blocages GP-010/011 restent à interpréter comme incidents de fiabilité d'exécution possibles, pas comme une mesure pure des capacités de raisonnement de Luna.

## GPT-6.1 Sol Medium

Dix-neuf observations de production :

- quota cumulé : **203 pts**
- durée cumulée : **4 h 59 min 39 s**
- résultats : **17 succès / 2 blocages**
- moyenne brute : **10,68 pts/observation**

Les dix-sept tâches réussies représentent **197 pts**. Les deux blocages représentent **6 pts** : GP-021 à **5 pts / 4:31** sans livraison B1 faute d’environnement POSIX, puis GP-033 à **1 pt / 0:17** avec STOP correct sur miroir Work incohérent/dirty. Les neuf gros checkpoints récents se situent à **16 pts / 21:37** pour B2 backend/root, **17 pts / 26:31** pour E-C UI, **16 pts / 24:29** pour le contrat 0.3.2-A, **12 pts / 20:49** pour le scanner Minecraft 0.3.2-B, **17 pts / 33:55** pour les providers/classification 0.3.2-C, **11 pts / 16:49** pour l’UI Admin 0.3.2-D, **23 pts / 38:45** pour l’API Admin/orchestration 0.3.2-E3-A, **16 pts / 18:52** pour l’UI réelle 0.3.2-E3-C et **17 pts / 22:13** pour le runbook réel 0.3.2-F ; GP-055 ajoute un correctif de fixture ciblé à **6 pts / 5:04**, GP-056 un correctif scanner de production ciblé à **5 pts / 6:50** et GP-057 une adaptation de policy JAR à **5 pts / 7:02**. GP-042 reste un audit de récupération à **1 pt / 4:02**.

## GPT-6.1 Sol High

Trois observations :

- quota cumulé : **51 pts**
- durée cumulée observée : **2 h 04 min 17 s***
- résultats : **2 succès / 1 partiel**
- moyenne brute : **17,00 pts/observation**
- livrables distants : **E2 candidat `c3f335a...`**, puis **E3-B candidat `5d4b030...`**

GP-041 a consommé **20 pts / 53:27** et s’est interrompu avant commit/push malgré un travail local avancé. GP-043 a repris l’existant et finalisé E2 pour **7 pts / 28:50 observés**. GP-048 a livré E3-B pour **24 pts / 42:00** malgré un stall apparent de l’UI après exécution ; le succès est confirmé par le commit et la PR distante. *La durée GP-043 inclut une attente d’autorisation ; le total temporel n’est donc pas directement comparable aux autres runs.*

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

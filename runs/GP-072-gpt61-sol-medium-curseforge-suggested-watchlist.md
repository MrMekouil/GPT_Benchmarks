# GP-072 — GPT-6.1 Sol Medium — preuve CurseForge exacte → SUGGESTED/watchlist

- Date : 2026-10-07
- Quota visible : 81 % → 74 % (**7 points**)
- Durée : **9 min 35 s**
- Résultat : succès
- Commit GamePanel : `868a5d2bb966aa18f441fbe9d96bf056b3c9d505`
- Draft PR : #22

## Prompt exact

~~~text
Repo : MrMekouil/GamePanel
Branche : work/0.3.2-content-manifests
PR : Draft #22
HEAD attendu : 901c7682399f4854cedcb07a7ac950ddfaf72ac5

Travaille uniquement sur la branche indiquée.

Avant toute modification :
- vérifie la branche courante ;
- exécute git status ;
- examine git diff ;
- examine git log --oneline -10 ;
- lis WORK_STATE.md ;
- préserve toute modification non commitée ;
- ne reset/revert rien avant d'avoir compris l'état réel.

Utilise l’intégration GitHub connectée ; pas de git clone réseau.

Contexte acquis :
- Gate 4 Interstice est désormais ACQUIS sur validation réelle utilisateur :
  Forge 47.4.0 / MC 1.20.1 / VERIFIED, complete=true,
  354 JAR / 1 220 941 100 octets,
  comparaison indépendante SHA-256 des 354 JAR PASS,
  aucun draft/publication/head/job implicite.
- F reste NON ACQUIS.
- Ne relance aucun gate réel.
- Ne modifie aucun conflit historique automatiquement.

Sous-lot : réduire proprement les UNKNOWN de classification à partir du profil CurseForge local exact, et conserver les SUGGESTED comme watchlist prioritaire.

État réel Interstice après import CurseForge :
- 354 entrées ;
- 74 affichées environment=unknown ;
- parmi elles : 61 UNKNOWN réels et 13 CONFLICT ;
- 72/74 ont un match curseforge-local exact ;
- 14 ont aussi un match Modrinth ;
- 2 seulement n'ont aucun match exact.

Objectif de preuve :
si un artifact serveur observé est associé par SHA-1 exact à installedFile dans le profil CurseForge client importé, mais qu'aucune déclaration explicite fiable ne donne son environnement, cette présence exacte des mêmes octets des deux côtés peut produire :

environment = both
state = SUGGESTED

Cette preuve signifie uniquement :
« artifact exact observé sur le serveur et présent dans le profil client importé ».

Elle ne signifie PAS :
- compatibilité vérifiée ;
- déclaration officielle CurseForge ;
- policy required/recommended/optional ;
- droit de redistribution ;
- VERIFIED.

Contraintes :
- liaison uniquement par preuve exacte déjà admise : SHA-1 installedFile + artifact serveur exact ;
- aucun filename/project/category/latestFile/fingerprint seul ;
- policy reste UNKNOWN sauf preuve indépendante existante ;
- ne jamais promouvoir cette preuve en VERIFIED ;
- les CONFLICT existants restent CONFLICT et toutes leurs assertions restent visibles ;
- ne pas résoudre doubledoors/treeharvester ni aucun autre conflit ;
- aucune nouvelle table/migration SQLite sauf nécessité démontrée : privilégier assertions/provenance déjà persistées dans l'observation ;
- la suggestion doit survivre aux rescans pour le même path/hash/taille via le mécanisme existant de conservation des preuves CurseForge locales ;
- si les octets changent, ne jamais transférer la suggestion au nouvel artifact.

Donner à cette nouvelle preuve une méthode/source/scope explicites et versionnés, distincts de la déclaration installedFile.gameVersion actuelle.

UI Admin Contenus client :
- ajouter une vue/groupe compact « À vérifier en priorité » pour les entrées dont la décision environment est SUGGESTED ;
- afficher nombre, nom, décision suggérée et raison/provenance courte ;
- expliquer clairement qu'elles fonctionnent comme watchlist de compatibilité client/serveur ;
- les CONFLICT restent dans leur traitement conflit, pas maquillés en SUGGESTED ;
- UNKNOWN sans preuve suffisante reste UNKNOWN ;
- ne créer aucune seconde source de vérité : dériver la watchlist des preuves persistées.

Tests attendus :
- exact server artifact + exact CurseForge client installedFile sans side => both/SUGGESTED ;
- même preuve avec side explicite fiable compatible : ne dégrade pas VERIFIED ;
- contradiction avec preuve indépendante => CONFLICT ;
- absence/mauvais SHA-1/changement d'octets => aucune suggestion ;
- aucune policy déduite ;
- rescan inchangé conserve la suggestion ;
- nouvel artifact/hash ne l'hérite pas ;
- reimport idempotent, pas de doublon d'assertion ;
- UI watchlist SUGGESTED, séparation CONFLICT/UNKNOWN ;
- régressions CurseForge, classification, content Admin/API/UI et Gate 4 scanner inchangées.

Documenter :
- Gate 4 Interstice ACQUIS avec les preuves réelles déjà communiquées ;
- nouveau contrat SUGGESTED/watchlist ;
- F reste NON ACQUIS.

Mettre à jour MANIFEST.sha256.
Aucune version/migration/merge/tag/release/bump.

Exécute les suites ciblées pertinentes, compile/syntax checks, manifeste et diff-check.
Commit et push uniquement si le résultat final est propre.

Restitution finale compacte uniquement :
- nouveau HEAD ;
- fichiers modifiés ;
- règle SUGGESTED/persistance/watchlist implémentée ;
- tests réellement exécutés avec PASS/FAIL/N/A ;
- limites éventuelles.

Ne donne aucune commande de validation réelle à l'utilisateur.
~~~

## Réponse exacte

~~~text
1. HEAD poussé : `868a5d2bb966aa18f441fbe9d96bf056b3c9d505` ; PR #22 toujours Draft.
2. Fichiers : `gamepanel/content_curseforge.py`, `gamepanel/content_admin.py`, `web/app.js`, `tests/test_content_curseforge_032.py`, `tests/web-content-032.cjs`, `WORK_STATE.md`, `ASSISTANT_STATE.md`, `docs/{CHANGELOG,CONTENT_MANIFESTS_032,VALIDATION_032}.md`, `MANIFEST.sha256`.
3. Règle : SHA-1 exact sans côté déclaré → `both/SUGGESTED`, provenance versionnée ; conservation pour le même path/hash/taille, réimport idempotent, aucun transfert aux nouveaux artifacts. Watchlist dérivée des décisions persistées ; conflits conservés.
4. Tests finaux : **289 PASS / 150 N/A POSIX / 0 FAIL**. UI VM/API, syntaxe JS, compileall, manifeste et diff-check **PASS**. Échecs initiaux corrigés : 2 Python, 1 UI.
5. Limites : Playwright **N/A**, module absent ; aucune compatibilité vérifiée ni policy déduite. **Gate 4 ACQUIS** sur preuve utilisateur ; **F NON ACQUIS**.
~~~

## Synthèse enregistrée

- Preuve exacte CurseForge locale sans side explicite : `environment=both`, `state=SUGGESTED`.
- Cette preuve reste une suggestion : aucune compatibilité vérifiée, aucune policy déduite, aucune promotion en VERIFIED.
- Persistance pour le même path/hash/taille ; aucun transfert à un artifact dont les octets changent.
- Réimport idempotent ; CONFLICT conservés.
- Watchlist Admin « À vérifier en priorité » dérivée des décisions persistées.
- Tests finaux : **289 PASS / 150 N/A POSIX / 0 FAIL**.
- Trois échecs initiaux corrigés : **2 Python + 1 UI**.
- UI VM/API, syntaxe JS, compileall, manifeste et diff-check PASS.
- Playwright N/A.
- **Gate 4 ACQUIS** ; **F NON ACQUIS**.

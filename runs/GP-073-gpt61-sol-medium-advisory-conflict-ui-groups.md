# GP-073 — GPT-6.1 Sol Medium — advisory hors conflit + six groupes UI

- Date : 2026-10-07
- Quota visible : 74 % → 69 % (**5 points**)
- Durée : **8 min 22 s**
- Résultat : succès
- Commit GamePanel : `4ed0fbeb95303acbc25fa99edd84596ba14012fc`
- Draft PR : #22

## Prompt exact

~~~text
Repo : MrMekouil/GamePanel
Branche : work/0.3.2-content-manifests
PR : Draft #22
HEAD attendu : 868a5d2bb966aa18f441fbe9d96bf056b3c9d505

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

Contexte :
- Gate 4 Interstice ACQUIS ; F reste NON ACQUIS.
- Le lot 868a5d2 ajoute la preuve CurseForge présence exacte client+serveur => both/SUGGESTED.
- Validation réelle utilisateur après import : les « inconnus » visibles passent de 74 à 26, mais seulement 2 sont de vrais UNKNOWN ; les autres sont des CONFLICT.
- L’UI ouvre actuellement automatiquement la grosse watchlist « À vérifier en priorité », ce qui rend la page énorme.
- Les 13 conflits historiques/préexistants ne doivent pas être automatiquement résolus.

Correctif demandé, même branche/version.

1. Sémantique de la suggestion de présence

La preuve :
provider=curseforge-local
method=installedFile-sha1-server-client-presence-v1

est une preuve advisory/watchlist, pas une preuve technique de compatibilité.

Règle :
- si elle est la seule preuve d’environnement exploitable : décision both / SUGGESTED ;
- si d’autres assertions d’environnement existent, cette assertion de présence reste persistée et visible mais ne participe pas au calcul de valeur/conflit ;
- les autres assertions déterminent alors normalement VERIFIED/SUGGESTED/CONFLICT selon les règles historiques ;
- elle ne doit donc jamais créer à elle seule un CONFLICT face à une preuve indépendante ;
- ne change pas la sémantique des autres sources SUGGESTED ;
- les conflits historiques indépendants doivent rester CONFLICT ;
- aucune policy, redistribution ou VERIFIED déduite de cette présence.

Éviter un traitement fragile par filename. Utiliser la méthode/scope de preuve versionnée.

2. UI

Supprimer la grosse section séparée « À vérifier en priorité ».

Dans les groupes normaux de Contenus client, avoir des groupes mutuellement exclusifs et compacts :
- Conflits
- Suggérés
- Serveur uniquement
- Client uniquement
- Les deux
- Inconnus

« Suggérés » = entrées portant la preuve advisory de présence exacte et sans décision CONFLICT.
Elles restent la watchlist prioritaire de compatibilité client/serveur, même si une preuve indépendante plus forte fournit ensuite la décision effective ; afficher cette décision dans la ligne et conserver la provenance SUGGESTED dans les détails.

« Conflits » = entrées ayant réellement une décision CONFLICT.
Elles ne doivent plus gonfler le compteur « Inconnus ».

« Inconnus » = vrais UNKNOWN seulement.

Tous les groupes doivent être FERMÉS par défaut, notamment Suggérés et Inconnus.
Aucun `open` automatique après scan/import.
Conserver les index d’entrées corrects pour le formulaire brouillon et éviter toute duplication d’une entrée entre groupes.

3. Tests

Ajouter/corriger les tests pour prouver :
- présence SUGGESTED seule => both/SUGGESTED ;
- présence advisory + VERIFIED compatible ou différent => la décision forte gagne, pas de nouveau conflit ;
- présence advisory + conflit indépendant préexistant => CONFLICT conservé ;
- deux preuves indépendantes contradictoires => CONFLICT inchangé ;
- assertion advisory toujours persistée après rescan identique ;
- changement path/hash/taille ne l’hérite pas ;
- groupes UI mutuellement exclusifs ;
- CONFLICT absent du groupe Inconnus ;
- vrais UNKNOWN seuls dans Inconnus ;
- Suggérés fermés par défaut ;
- aucun groupe ouvert automatiquement ;
- aucune duplication et collecte du draft inchangée.

Ne change aucune migration/version.
Ne touche pas aux conflits historiques individuellement.
Ne relance aucun gate réel.
F reste NON ACQUIS.

Documente le correctif et la validation réelle observée sans inventer de nouveau décompte final tant qu’il n’a pas été retesté sur le serveur.
Met à jour MANIFEST.sha256.

Exécute les suites ciblées Python/UI, syntax checks, manifeste et diff-check.
Commit + push si propre.

Restitution finale compacte uniquement :
- nouveau HEAD ;
- fichiers modifiés ;
- règle advisory/conflit et regroupement UI ;
- tests PASS/FAIL/N/A réellement exécutés ;
- éventuelle limite restante.

Ne donne aucune commande de validation réelle à l'utilisateur.
~~~

## Réponse exacte

~~~text
- 
  HEAD poussé : 4ed0fbeb95303acbc25fa99edd84596ba14012fc ; PR #22 toujours Draft.
- Fichiers : gamepanel/{content_classification,content_curseforge}.py, web/app.js, tests/test_content_{classification,curseforge}_032.py, tests/web-content{,-browser}-032.cjs, WORK_STATE.md, ASSISTANT_STATE.md, docs/{CHANGELOG,CONTENT_MANIFESTS_032,VALIDATION_032}.md, MANIFEST.sha256.
- Advisory : seule → both/SUGGESTED ; sinon conservée mais exclue du calcul. Conflits indépendants préservés. Six groupes UI exclusifs, tous fermés, sans duplication ; index du brouillon conservés.
- Tests : **294 PASS / 150 N/A POSIX / 0 FAIL**. UI VM/API, syntaxe JS, compileall, manifeste et diff-check **PASS**.
- Limites : Playwright **N/A**, module absent ; aucun nouveau décompte réel revendiqué. **Gate 4 ACQUIS ; F NON ACQUIS**
~~~

## Synthèse enregistrée

- La preuve `curseforge-local / installedFile-sha1-server-client-presence-v1` est strictement advisory.
- Seule preuve exploitable : `both/SUGGESTED`.
- Avec d’autres assertions d’environnement, elle reste persistée et visible mais sort du calcul de valeur/conflit.
- Les conflits indépendants restent inchangés ; aucun conflit historique n’est résolu automatiquement.
- UI : six groupes mutuellement exclusifs et compacts — Conflits, Suggérés, Serveur uniquement, Client uniquement, Les deux, Inconnus.
- Tous les groupes sont fermés par défaut ; aucun `open` automatique.
- CONFLICT n’apparaît plus dans Inconnus ; Inconnus contient uniquement les vrais UNKNOWN.
- Aucune duplication ; index du formulaire brouillon conservés.
- Tests : **294 PASS / 150 N/A POSIX / 0 FAIL**.
- UI VM/API, syntaxe JS, compileall, manifeste et diff-check PASS.
- Playwright N/A.
- Aucun nouveau décompte réel revendiqué.
- **Gate 4 ACQUIS ; F NON ACQUIS**.

# GP-056 — GPT-6.1 Sol Medium — correctif scanner Minecraft O_PATH

- Date : 2026-10-04
- Quota visible : 94 % → 89 % (**5 points**)
- Durée : **6 min 50 s**
- Résultat : succès
- Commit GamePanel : `fad9b8b39a12199749c3e4b91710d4c7380944a4`
- Draft PR : #22

## Prompt exact

~~~text
Travaille uniquement sur :

Dépôt :
MrMekouil/GamePanel

Branche :
work/0.3.2-content-manifests

PR :
Draft #22

HEAD distant attendu :
0f3f408c598c2f6575a21115a9a5a614d916ec6

OBJECTIF UNIQUE

Corriger le nouveau blocker réel du scan Minecraft 0.3.2-F :
MinecraftScanner exige actuellement O_RDONLY sur tous les ancêtres du chemin
absolu de l’instance, alors que ces ancêtres peuvent légitimement être
search-only pour le compte gamepanel.

Ne modifie pas les permissions système.
Ne poursuis aucun gate F.
F reste NON ACQUIS.
Pas de merge/tag/version bump.

AVANT MODIFICATION

- vérifie branche ;
- git status ;
- git diff ;
- git diff --cached ;
- git log --oneline --decorate -15 ;
- vérifie HEAD distant exact ;
- lis WORK_STATE.md ;
- lis ASSISTANT_STATE.md ;
- lis docs/ASSISTANT_WORKFLOW.md ;
- lis docs/VALIDATION_032.md ;
- audite gamepanel/minecraft_content.py et tests scanner associés.

Aucun reset/revert/clean.
Si HEAD ou état inattendu : STOP.

PREUVES RÉELLES UBUNTU

Après le correctif ContentStore :
- tests ContentStore : 10/10 PASS Ubuntu ;
- régressions liées : 203/203 PASS ;
- upgrade/rollback : 31/31 PASS ;
- migration/identity/content : 260/260 PASS ;
- installer/migrations/version/docs : 110/110 PASS.

L’UI Contenus client est accessible sur le candidat.
Un scan réel de minecraft-aero échoue avec :

CONTENT_SCAN_UNSAFE_OR_UNREADABLE_ROOT

Chemin réel :
/home/serveur/minecraft-neoforge-1.21.1

Permissions observées :

/
drwxr-xr-x root:root

/home
drwxr-xr-x root:root

/home/serveur
drwxr-x--- serveur:serveur

/home/serveur/minecraft-neoforge-1.21.1
drwxrwxr-x serveur:serveur

Test direct sous le vrai compte gamepanel :

O_RDONLY /home/serveur :
PermissionError [Errno 13]

O_PATH /home/serveur :
PASS

CAUSE CODE DÉJÀ AUDITÉE

Dans MinecraftScanner / _Scan.directory():

- absolute=True ouvre "/" avec O_RDONLY|O_DIRECTORY ;
- chaque composant est ensuite ouvert avec
  O_RDONLY|O_DIRECTORY|O_NOFOLLOW.

Donc le scanner exige de pouvoir lire/lister les ancêtres du root Minecraft,
alors que seule la traversée/search doit être nécessaire.

CORRECTIF ATTENDU

Pour la résolution absolue du root Minecraft :

- ancêtres :
  O_PATH | O_DIRECTORY | O_NOFOLLOW ;

- composant final correspondant au root réel de l’instance :
  O_RDONLY | O_DIRECTORY | O_NOFOLLOW,
  car ce fd doit ensuite permettre scandir/openat/fstat des fichiers du serveur.

Les parcours relatifs à partir de root_fd restent en O_RDONLY, car les dossiers
réellement scannés doivent être lisibles.

Même politique pour :
- run() lors de l’ouverture initiale du root ;
- validate() lorsqu’il rouvre le root absolu.

Exigences :
- aucun suivi de symlink ;
- chaque composant ancré par dir_fd ;
- aucun Path.resolve ou ouverture non ancrée ;
- aucun chmod/chown/ACL de /home/serveur ;
- "..", chemins relatifs/root invalides toujours refusés ;
- le root final doit rester réellement lisible/scannable ;
- ne pas transformer une permission insuffisante sur le root final en succès ;
- O_PATH absent doit être refusé explicitement, pas de fallback permissif ;
- ne pas affaiblir SOURCE_CHANGED / UNSAFE_RESOURCE /
  UNSAFE_OR_UNREADABLE_ROOT.

Audite posix_available() :
si le scanner dépend désormais explicitement de O_PATH, la capacité doit être
admis/refusée proprement et testée sans casser les autres utilisateurs de cette
fonction.

TESTS OBLIGATOIRES

Ajouter une vraie fixture POSIX reproduisant :

ancestor search-only pour le backend ;
root Minecraft final lisible ;
mods/ et fichiers accessibles.

Vérifier :
- O_RDONLY ancestor échoue réellement ;
- O_PATH ancestor passe ;
- scan réel passe ;
- validate() repasse par la même traversée sûre ;
- symlink ancêtre refusé ;
- symlink root final refusé ;
- root final illisible refuse toujours ;
- remplacement d’inode/root détecté ;
- chemins relatifs/.. refusés ;
- aucun escape.

Si les tests tournent en root, faire comme la fixture ContentStore :
abaisser réellement les credentials pour tester DAC, pas mocker os.open/stat.

RETESTS

Rejouer au minimum :
- tests scanner Minecraft 0.3.2 ;
- tests ContentStore 0.3.2 ;
- tests content Admin/API liés ;
- tests publication/upgrade pertinents.

Puis :
- compileall ;
- release-docs ;
- MANIFEST.sha256 complet ;
- git diff --check ;
- audit diff final.

DOCUMENTATION

Consigner :
- scan réel Aero FAIL avec CONTENT_SCAN_UNSAFE_OR_UNREADABLE_ROOT ;
- O_RDONLY /home/serveur FAIL sous gamepanel ;
- O_PATH /home/serveur PASS ;
- cause exacte scanner absolu ;
- correctif candidat O_PATH ancêtres / O_RDONLY root final ;
- aucune permission système modifiée ;
- F reste NON ACQUIS ;
- aucun gate suivant exécuté.

Ne réécris pas les PASS Ubuntu précédents.
Ne prétends pas que Gate 4 est acquis.

Commit + push sur la même branche / PR #22.
Ne merge pas.
Ne tague pas.
Ne bump pas.

Réponse finale courte :
- cause ;
- correctif ;
- tests ;
- commit poussé ;
- commande Ubuntu exacte de retest.
~~~

## Réponse exacte

~~~text
Cause confirmée : le scanner exigeait O_RDONLY sur les ancêtres search-only.

Correctif : ancêtres O_PATH, root final et parcours relatifs O_RDONLY ; même politique dans `run()` et `validate()`. Ancrage/no-follow conservés, aucune permission système modifiée.

Tests Windows : scanner **27 PASS / 24 N/A**, régressions **149 PASS / 108 N/A**. Compileall, release-docs, manifeste et diff-check **PASS**. Tests natifs Ubuntu à rejouer.

Commit poussé : [`fad9b8b`](https://github.com/MrMekouil/GamePanel/commit/fad9b8b39a12199749c3e4b91710d4c7380944a4), Draft #22.

Retest depuis le checkout Ubuntu :
```
PYTHONPATH="$PWD" /opt/gamepanel/.venvs/d25d52dca517e628/bin/python -m unittest -v tests.test_minecraft_content_032 tests.test_content_store_032 tests.test_content_admin_032 tests.test_content_distribution_032 tests.test_content_publication_032 tests.test_content_upgrade_032 tests.test_content_classification_032 tests.test_release_docs
```

**F NON ACQUIS ; aucun gate suivant exécuté.**
~~~

## Synthèse enregistrée

- Cause rapportée : le scanner exigeait `O_RDONLY` sur des ancêtres absolus pouvant être search-only pour `gamepanel`.
- Correctif rapporté : `O_PATH` pour les ancêtres, `O_RDONLY` pour le root final et les parcours relatifs ; même politique dans `run()` et `validate()`.
- Sécurité rapportée : ancrage par `dir_fd` et no-follow conservés ; aucune permission système modifiée.
- Tests Work Windows : scanner **27 PASS / 24 N/A**, régressions **149 PASS / 108 N/A** ; compileall, release-docs, manifeste et diff-check **PASS**.
- Tests Ubuntu natifs : **à rejouer**.
- Statut 0.3.2-F : **NON ACQUIS** ; aucun gate suivant exécuté.

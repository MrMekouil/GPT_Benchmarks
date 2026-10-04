# GP-059 — GPT-6.1 Sol Medium — qualification Modrinth runtime

- Date : 2026-10-04
- Quota visible : 80 % → 70 % (**10 points**)
- Durée : **15 min 13 s**
- Résultat : succès
- Commit GamePanel : `3fd61f56b304b725df7e5ff49fabe59b8be3dec3`
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
d0b1d101fc904b15bbb267adb7b4fc1a7d8c4bc8

OBJECTIF UNIQUE

Rendre la qualification réelle des mods Minecraft utile sur un vrai serveur
Forge/NeoForge, sans inventer de classification et sans rendre un provider
externe obligatoire.

Ne refonds PAS encore l’UI dans ce Work.
F reste NON ACQUIS.
Gate 4 Interstice non exécuté.
L’observation réelle Aero fonctionne maintenant mais Gate 5 n’est pas acquis :
LOADER_CONFLICT et qualification très majoritairement UNKNOWN.

Pas de merge/tag/version bump.

AVANT MODIFICATION

- branche/status/diff/diff --cached/log ;
- vérifie HEAD distant exact ;
- lis WORK_STATE.md ;
- lis ASSISTANT_STATE.md ;
- lis docs/ASSISTANT_WORKFLOW.md ;
- lis docs/VALIDATION_032.md ;
- lis docs/CONTENT_MANIFESTS_032.md ;
- audite :
  gamepanel/content_admin.py
  gamepanel/content_providers.py
  gamepanel/content_classification.py
  gamepanel/content_http.py
  gamepanel/minecraft_content.py
  tests providers/classification/admin concernés.

Aucun reset/revert/clean.
STOP si état inattendu.

PREUVES RÉELLES

Après les correctifs scanner :
- scanner ZIP case-sensitive : 60/60 PASS Ubuntu ;
- régressions classification/Admin/store/publication/upgrade/docs : 216/216 PASS ;
- update candidat installé ;
- scan réel minecraft-aero : SUCCÈS filesystem/archive ;
- observation persistée révision 1 ;
- les JAR réels apparaissent avec SHA-256 et tailles.

Diagnostics visibles :
- LOADER_CONFLICT
- LOCAL_ENVIRONMENT_UNKNOWN
- MOD_METADATA_UNKNOWN

La majorité des mods sont affichés :
environment = unknown
client policy = unknown

CAUSE CODE DÉJÀ AUDITÉE

ContentAdministration.__init__ utilise par défaut :

providers = (LocalJarProvider(),)

LocalJarProvider sait actuellement produire une assertion environnement surtout
depuis fabric.mod.json:environment.

Pour Forge/NeoForge, le code refuse volontairement de déduire un environnement
depuis displayTest, dépendances, filename ou autres heuristiques non probantes.

C’est correct côté sécurité, mais en pratique presque tout Aero reste UNKNOWN.

Le dépôt contient déjà :
- ModrinthProvider avec correspondance exacte SHA-512/taille ;
- CurseForgeProvider avec fingerprint + SHA-1/taille ;
- PackwizProvider ;
- MrpackProvider ;
- ProviderHTTP strict.

Mais ces providers ne sont pas branchés automatiquement au scan runtime actuel.

OBJECTIF FONCTIONNEL

1. Local metadata reste la première source, sans nouvelle heuristique non prouvée.

2. Activer une qualification externe exacte et optionnelle, en priorité Modrinth,
   car aucune clé utilisateur n’est requise.

3. Une panne réseau/provider/quota/not-found ne doit JAMAIS faire échouer le scan.
   Elle produit uniquement diagnostics/UNKNOWN.

4. Aucun résultat provider ne doit être accepté par nom de fichier ou nom de projet :
   correspondance exacte bytes/hash/taille uniquement selon le contrat actuel.

5. CurseForge reste optionnel et ne doit pas exiger de nouvelle clé/configuration
   pour que 0.3.2 fonctionne. Ne crée pas une gestion de secrets/UI CurseForge dans
   ce lot sauf nécessité déjà prévue/documentée.

PERFORMANCE / BORNES — IMPORTANT

Ne branche surtout pas naïvement un appel réseau séquentiel de timeout 10 s pour
chaque JAR.

Audite le nombre potentiel d’artefacts et le comportement EvidenceCache.

La qualification externe doit avoir :
- concurrence bornée ou batch exact-hash documenté ;
- nombre de requêtes borné ;
- timeout par appel borné ;
- budget global de qualification borné ;
- cache exact par identité d’artifact/provider ;
- aucune attente N × timeout sur un modpack de dizaines/centaines de JAR.

Si un endpoint batch officiel exact-hash Modrinth est disponible dans le contrat
API utilisé, le préférer après audit de sécurité.
Sinon utiliser une concurrence strictement bornée + budget global.

ProviderHTTP doit conserver :
- HTTPS uniquement ;
- host/path allowlist ;
- protection DNS/rebinding/IP ;
- réponses et tailles bornées ;
- aucun proxy/arbitrary URL ;
- aucun téléchargement de JAR.

Audite aussi EvidenceCache :
ne garde pas un verrou global pendant une requête réseau si cela sérialise toute
la qualification ; corriger uniquement si nécessaire avec tests de concurrence
et sans double-publish de résultats incohérents.

CLASSIFICATION

Conserver les règles actuelles :
- VERIFIED uniquement si déclaration exacte probante ;
- SUGGESTED si preuve moins forte ;
- UNKNOWN si absence ;
- CONFLICT si preuves contradictoires ;
- aucune promotion silencieuse par heuristique.

Pour Modrinth exact SHA-512/taille :
réutiliser le contrat existant et ses mappings plutôt que réinventer une règle.

Ne déduis jamais redistribution/licence de la seule présence sur Modrinth.
La qualification environnement/politique et le droit de redistribution restent
des axes séparés.

LOADER_CONFLICT

Audite sa cause code, mais ne devine pas un loader actif.

Le scanner voit actuellement plusieurs installations loader via unix_args.txt.
Documente clairement pourquoi.

Si une source statique réellement autoritaire existe déjà dans la Definition ou
la configuration du service et peut sélectionner sans exécuter de script le
loader configuré pour CETTE instance, proposer/corriger de façon testée.

Sinon ne change pas cette logique dans ce Work : consigner qu’une preuve Ubuntu
supplémentaire (ExecStart/config réelle) est nécessaire avant correction.

TESTS OBLIGATOIRES

Ajouter/adapter les tests pour :
- LocalJar seul reste fonctionnel offline ;
- Modrinth exact hash enrichit environment/policy ;
- Modrinth not-found => UNKNOWN + diagnostic, scan réussi ;
- timeout/unavailable/quota => UNKNOWN + diagnostic, scan réussi ;
- réponse hash/taille incohérente refusée ;
- conflit Local/Modrinth reste CONFLICT ;
- absence de réseau n’empêche jamais l’observation ;
- qualification de nombreux artefacts respecte une borne de concurrence/budget ;
- cache évite les recherches identiques répétées ;
- aucune URL/provider venant du client HTTP.

Rejouer au minimum :
- tests providers 0.3.2 ;
- tests classification 0.3.2 ;
- tests content_admin 0.3.2 ;
- tests minecraft_content 0.3.2 ;
- tests content_store/publication/upgrade ;
- release-docs.

Puis compileall, diff-check, MANIFEST intégral.

DOCUMENTATION

Consigner la preuve réelle actuelle :
- Aero scan réussi, observation révision 1 ;
- filesystem/archive corrigés ;
- qualification majoritairement UNKNOWN avec LocalJar seul ;
- LOADER_CONFLICT encore présent ;
- cette observation ne rend pas Gate 5 acquis ;
- F reste NON ACQUIS.

Documenter précisément les providers désormais réellement actifs,
leurs limites et le comportement offline.

Ne modifier aucune permission système.
Ne lancer aucun scan réel dans Work.

Commit + push même branche / PR #22.
Ne merge pas.
Ne tague pas.
Ne bump pas.

Réponse finale courte :
- cause ;
- providers réellement branchés ;
- bornes/performance ;
- tests ;
- commit poussé ;
- commande Ubuntu de retest.
~~~

## Réponse exacte

~~~text
- \
  **Cause :** LocalJar seul fournit rarement une preuve d’environnement Forge/NeoForge.
- **Correctif :** LocalJar reste prioritaire ; Modrinth est désormais branché sans clé, avec correspondance exacte SHA-512/taille. Pannes et absence de résultat restent UNKNOWN sans bloquer l’observation.
- **Bornes :** lots de 64, maximum 512 JAR non cachés et 16 requêtes ; 3 s/appel, budget global 20 s, cache exact. Aucune heuristique ou protection réseau/archive affaiblie.
- **Tests Work :** 183 PASS, 113 N/A POSIX, zéro FAIL. Compileall, release-docs, manifeste 209 fichiers et diff-check PASS.
- **Commit poussé :** [**3fd61f5**](https://github.com/MrMekouil/GamePanel/commit/3fd61f56b304b725df7e5ff49fabe59b8be3dec3), PR #22 toujours Draft.

LOADER_CONFLICT conservé faute de preuve ExecStart/config réelle. **F et Gate 5 NON ACQUIS ; Gate 4 Interstice non exécuté.**

Retest Ubuntu depuis le nouveau commit :
```
PYTHONPATH="$PWD" /opt/gamepanel/.venvs/d25d52dca517e628/bin/python -m unittest -v tests.test_content_providers_032 tests.test_content_classification_032 tests.test_content_admin_032 tests.test_minecraft_content_032 tests.test_content_store_032 tests.test_content_publication_032 tests.test_content_upgrade_032 tests.test_release_docs
```
~~~

## Synthèse enregistrée

- Cause rapportée : LocalJar seul fournit rarement une preuve d’environnement Forge/NeoForge.
- Providers réellement branchés : **LocalJar prioritaire + Modrinth sans clé**, avec correspondance exacte **SHA-512/taille**.
- Pannes réseau/provider/quota/not-found : **UNKNOWN sans bloquer l’observation**.
- Bornes rapportées : lots de **64**, maximum **512 JAR non cachés**, **16 requêtes**, **3 s/appel**, budget global **20 s**, cache exact.
- Tests Work : **183 PASS / 113 N/A POSIX**, zéro FAIL ; compileall, release-docs, manifeste **209 fichiers** et diff-check PASS.
- `LOADER_CONFLICT` conservé faute de preuve ExecStart/config réelle.
- Statut : **F et Gate 5 NON ACQUIS** ; Gate 4 Interstice non exécuté.

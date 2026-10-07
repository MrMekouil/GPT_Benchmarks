# GP-069 — GPT-6.1 Sol Medium — preuve launcher systemd/statique

- Date : 2026-10-07
- Quota visible : 100 % → 92 % (**8 points**)
- Durée : **7 min 36 s**
- Résultat : succès
- Commit GamePanel : `835c96bc659f7ab9a529508469caa02ab48fdcfa`
- Draft PR : #22

## Prompt exact

~~~text
Modèle : GPT-6.1 Sol
Effort : Medium

Repo : MrMekouil/GamePanel
Branche : work/0.3.2-content-manifests
PR : Draft #22
HEAD attendu : 37d375e15dfe5c61491cfae5965ab8002052203e

Utilise l’intégration GitHub connectée ; pas de git clone réseau.

Gate 4 Interstice : le scan réel passe désormais les archives mais produit
LOADER_CONFLICT car deux Forge sont installés :
- 1.20.1-47.2.0
- 1.20.1-47.4.0

Preuve réelle de sélection :
systemd minecraft.service :
- WorkingDirectory=/home/serveur/minecraft/forge-1.20.1
- ExecStart=/home/serveur/minecraft/forge-1.20.1/run.sh

run.sh réel :
java @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.20.1-47.4.0/unix_args.txt "$@"

Donc 47.4.0 est sélectionné ; 47.2.0 est seulement installé.

Corrige proprement la détection de loader.

Contraintes :
- ne jamais choisir la version la plus haute/récente ;
- ne jamais exécuter/interpréter un script shell ;
- ne pas considérer toutes les versions installées comme actives ;
- lier la sélection à une preuve réelle du launcher de CETTE instance ;
- préférer une preuve issue du service systemd réel + launcher statique plutôt
  qu’une convention aveugle "root/run.sh" ;
- réutiliser la frontière privilégiée gamepanel-exec si nécessaire, sans ouvrir
  d’action shell arbitraire ;
- si systemd prouve ExecStart=<root>/run.sh et WorkingDirectory=<root>,
  analyser run.sh statiquement et de façon strictement bornée/no-follow ;
- accepter uniquement une référence littérale unique
  @libraries/net/minecraftforge/forge/.../unix_args.txt
  ou @libraries/net/neoforged/neoforge/.../unix_args.txt ;
- le unix_args sélectionné doit encore passer loader_observation et être cohérent
  avec son répertoire/MC/loader ;
- autres versions installées peuvent rester observées comme sources mais ne doivent
  pas créer CONFLICT si une sélection autoritaire unique est prouvée ;
- launcher ambigu, référence multiple, mismatch, chemin non sûr ou preuve systemd
  absente => conserver UNKNOWN/CONFLICT, jamais deviner ;
- aucun contenu brut ExecStart/run.sh ne doit être persisté ou exposé ;
- aucun démarrage du serveur.

Tests minimum :
- Forge 47.2 + 47.4 installés, launcher sélectionne 47.4 => forge 47.4 VERIFIED ;
- équivalent NeoForge ;
- référence absente/multiple/malformée => aucune sélection inventée ;
- sélection vers unix_args absent ou incohérent => refus/conflit ;
- shell operators/substitutions ne deviennent jamais une preuve ;
- symlink/source mouvante/no-follow gardés ;
- cas historique une seule version installé reste inchangé.

Pas de migration SQLite, pas de bump/version.
Documente les preuves réelles Interstice.
Gate 4 reste NON ACQUIS jusqu’au retest utilisateur.
F reste NON ACQUIS.
Aucun merge/tag/release.

Rerun suites ciblées, manifeste/diff-check, puis push si PASS.
Handoff compact : HEAD, choix d’architecture, tests PASS/FAIL/N/A, fichiers modifiés.
~~~

## Réponse exacte

~~~text
1. **HEAD poussé** : `835c96bc659f7ab9a529508469caa02ab48fdcfa`.
2. **Architecture** : preuve systemd via action fixe `launcher-proof`, puis lecture statique bornée/no-follow du launcher. Sélection unique VERIFIED, autres installations conservées ; aucun script exécuté.
3. **Tests** : **271 PASS / 147 N/A**, zéro FAIL exécuté. Trois suites historiques N/A à l’import (`pydantic`/`aiohttp` absents). Syntaxe, docs, manifeste et whitespace PASS.
4. **10 fichiers** : scanner, orchestration Admin, exécuteur, nouveaux tests, cinq documents et manifeste.
5. **Gate 4 et F NON ACQUIS** ; aucun démarrage, migration, bump, merge/tag/release.
~~~

## Synthèse enregistrée

- Preuve réelle Interstice : systemd pointe vers `/home/serveur/minecraft/forge-1.20.1/run.sh`, lequel référence littéralement Forge **1.20.1-47.4.0**.
- Architecture : action fixe `launcher-proof` + analyse statique bornée/no-follow ; aucun script shell exécuté.
- Sélection unique **VERIFIED** ; autres versions installées conservées comme sources sans créer de conflit si la preuve autoritaire est unique.
- Tests : **271 PASS / 147 N/A**, zéro FAIL exécuté.
- Trois suites historiques N/A à l’import faute de `pydantic`/`aiohttp`.
- Syntaxe, docs, manifeste et whitespace PASS.
- **Gate 4 et F restent NON ACQUIS**.

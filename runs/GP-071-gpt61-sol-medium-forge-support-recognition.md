# GP-071 — GPT-6.1 Sol Medium — reconnaissance JAR Forge support/library

- Date : 2026-10-07
- Quota visible : 89 % → 81 % (**8 points**)
- Durée : **10 min 37 s**
- Résultat : succès
- Commit GamePanel : `901c7682399f4854cedcb07a7ac950ddfaf72ac5`
- Draft PR : #22

## Prompt exact

~~~text
Repo : MrMekouil/GamePanel
Branche : work/0.3.2-content-manifests
PR : Draft #22
HEAD attendu : 0a234e3b203576ba05055468245b856c8e840055

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

Gate 4 Interstice réel :
- loader correctement prouvé : Forge 47.4.0 / Minecraft 1.20.1 / VERIFIED ;
- 354 JAR, 1 220 941 100 octets ;
- scanner_diagnostics global vide ;
- complete=false uniquement à cause de 3 JAR.

Preuves réelles :

1. kotlinforforge-4.12.0-all.jar
MANIFEST :
`fmlmodtype = LIBRARY`
Actuellement : MOD_METADATA_UNKNOWN.

2. Connector-1.0.0-beta.48+1.20.1.jar
Pas de mods.toml/fabric.mod.json.

Présence exacte :
- META-INF/services/cpw.mods.modlauncher.api.ITransformationService
- META-INF/services/net.minecraftforge.forgespi.locating.IDependencyLocator
- META-INF/services/net.minecraftforge.forgespi.locating.IModLocator

Contenus observés :
- org.sinytra.connector.service.ConnectorLoaderService
- io.github.steelwoolmc.mixintransmog.MixinTransformationService
- org.sinytra.connector.locator.ConnectorLocator
- org.sinytra.connector.locator.ConnectorEarlyLocator

Il contient aussi META-INF/jarjar/Connector-1.0.0-beta.48+1.20.1-mod.jar.
Ne pas récursivement scanner/exécuter/extracter ce nested JAR dans ce lot.

3. watervision-FG-mc1.20.1-v0.1.0-alpha.jar

Metadata Forge valide :
META-INF/mods.toml :
- modId=watervision
- version=0.1.0-alpha
- modLoader=javafml
- loaderVersion=[47,)

Son fabric.mod.json secondaire est invalide JSON :
JSONDecodeError line 6 column 50.
La description contient un LF brut :
`"Record and watch videos in game
Amazing!"`

Actuellement ce METADATA_INVALID rend complete=false malgré la metadata Forge native valide.

Objectif :
corriger la notion de JAR reconnu / metadata suffisante sans affaiblir les contrôles de sécurité ni inventer de classification client.

Contraintes :
- conserver le parseur JSON strict ;
- ne pas tolérer globalement du JSON invalide ;
- ne pas déduire client/server depuis filenames, services ou manifest ;
- ne jamais exécuter de JAR/service/script ;
- ne pas extraire ni récursivement inspecter META-INF/jarjar/*.jar ;
- ne pas changer les limites ZIP/JAR ;
- aucune migration SQLite/version.

Cas attendus :

A. Forge library/support JAR
- un MANIFEST avec FMLModType=LIBRARY constitue une preuve suffisante que le JAR est un composant Forge reconnu ;
- ne plus produire MOD_METADATA_UNKNOWN dans ce cas ;
- auditer les valeurs FMLModType réellement documentées avant d'en accepter d'autres ;
- ne pas inventer de liste.

B. Forge loader/service component
- reconnaître uniquement des SPI exacts et bornés, pas un glob META-INF/services/* ;
- couvrir au minimum les SPI Forge/ModLauncher réellement observés ci-dessus ;
- contenu UTF-8 borné ;
- lignes de classes strictement validées ;
- cette preuve signifie seulement "composant JAR reconnu" ;
- aucune assertion environment/policy/redistribution ;
- aucune confiance accordée au filename ou Implementation-Title.

C. Metadata étrangère invalide
- si le loader sélectionné est Forge et qu'un descriptor Forge natif valide identifie déjà le mod, un fabric.mod.json invalide ne doit pas rendre le snapshot incomplet ;
- appliquer ce principe uniquement lorsqu'une preuve native cohérente avec le loader sélectionné existe ;
- ne pas masquer une metadata native invalide ;
- ne pas transformer un JAR sans preuve native en succès ;
- LocalJarProvider peut rester UNKNOWN pour l'environnement : cela ne bloque pas à lui seul la complétude du snapshot.

Résultat réel attendu après correctif :
- Forge 47.4.0 VERIFIED inchangé ;
- Connector reconnu sans MOD_METADATA_UNKNOWN ;
- KotlinForForge reconnu comme library sans MOD_METADATA_UNKNOWN ;
- WaterVision reconnu via son mods.toml Forge valide, sans blocker causé par son fabric.mod.json étranger invalide ;
- scanner complete=true si aucun autre diagnostic scanner réel ;
- diagnostics classification/provider UNKNOWN conservés si présents.

Tests obligatoires :
- FMLModType LIBRARY ;
- FMLModType inconnu/non documenté reste conservateur ;
- SPI Forge exact valide ;
- service path arbitraire ou contenu invalide ne prouve rien ;
- aucune inspection récursive jarjar ;
- Forge mods.toml valide + fabric.mod.json invalide : non bloquant sous Forge sélectionné ;
- même cas sans loader sélectionné : conservateur ;
- mods.toml Forge invalide sous Forge : reste bloquant ;
- équivalent NeoForge seulement si supportable sans hypothèse ;
- régressions archive/no-follow/loader selection inchangées.

Documente les preuves réelles Interstice et la politique retenue.
Mets à jour MANIFEST.sha256.

Gate 4 reste NON ACQUIS jusqu'au nouveau retest utilisateur.
F reste NON ACQUIS.

Aucun merge/tag/release/bump.

Rerun les suites ciblées, manifeste et diff-check, puis push si PASS.

Restitution finale compacte uniquement :
- nouveau HEAD ;
- fichiers modifiés ;
- règles implémentées ;
- tests réellement exécutés avec PASS/FAIL/N/A ;
- éventuel blocage restant.

Ne donne aucune commande de validation réelle à l'utilisateur.
~~~

## Réponse exacte

~~~text
1. HEAD poussé : `901c7682399f4854cedcb07a7ac950ddfaf72ac5` ; PR #22 toujours Draft.
2. Fichiers : `gamepanel/minecraft_content.py`, `tests/test_jar_recognition_032.py`, `WORK_STATE.md`, `ASSISTANT_STATE.md`, `docs/{CHANGELOG,CONTENT_MANIFESTS_032,VALIDATION_032}.md`, `MANIFEST.sha256`.
3. Règles : LIBRARY reconnu ; trois SPI exacts, stricts et bornés ; JSON étranger invalide non bloquant uniquement avec sélection Forge vérifiée et metadata native cohérente. Aucun côté client/server déduit ni inspection récursive jarjar. Protections conservées ; NeoForge reste conservateur.
4. Tests : **280 PASS / 150 N/A POSIX / 0 FAIL final**. Premier run : 1 FAIL et 3 erreurs corrigés. Retest reconnaissance/docs, compileall, manifeste et diff-check : **PASS**.
5. Blocage restant : retest utilisateur requis ; **Gate 4 et F NON ACQUIS**.
~~~

## Synthèse enregistrée

- `FMLModType=LIBRARY` reconnu comme composant Forge.
- Trois SPI exacts Forge/ModLauncher reconnus de façon stricte et bornée.
- Aucune déduction client/server via services, filenames ou manifest.
- Metadata étrangère invalide non bloquante uniquement sous sélection Forge vérifiée avec metadata Forge native cohérente.
- Aucun scan/extraction récursive de `META-INF/jarjar/*.jar`.
- NeoForge reste conservateur.
- Premier passage tests : **1 FAIL + 3 erreurs**, corrigés dans le run.
- Final : **280 PASS / 150 N/A POSIX / 0 FAIL**.
- Reconnaissance/docs, compileall, manifeste et diff-check PASS.
- **Gate 4 et F restent NON ACQUIS**.

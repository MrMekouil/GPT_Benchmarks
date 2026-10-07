# GP-075 — GPT-6.1 Sol Medium — remplacement des preuves CurseForge locales

- Date : 2026-10-07
- Quota visible : 100 % → 90 % (**10 points**)
- Durée : **21 min 16 s**
- Résultat : succès
- Commit GamePanel : `89b49e219fa60875dccf1cc04f07a75dc478c2cd`
- Draft PR : #22

## Prompt exact

~~~text
Repo : MrMekouil/GamePanel
Branche : work/0.3.2-content-manifests
PR : Draft #22
HEAD attendu : f22be6f2f8dc90a3e70fbe374bc3ba895cbdcab1

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

Bug réel :
l’utilisateur a importé successivement deux minecraftinstance.json différents.
L’import explicite conserve actuellement les anciennes preuves curseforge-local pour les mêmes artifacts, puis ajoute celles du nouveau profil. Cela mélange deux profils.

Objectif :
un nouvel import explicite minecraftinstance.json doit remplacer les anciennes preuves curseforge-local par celles du nouveau profil pour chaque observation courante.

Règles :
- import explicite :
  - ne reprendre aucune ancienne assertion/match/diagnostic curseforge-local ;
  - ajouter uniquement les preuves curseforge-local du nouveau fichier ;
  - conserver les preuves indépendantes déjà persistées pour le même path/SHA-256/taille lorsqu’elles ne sont pas curseforge-local ;
  - conserver les conflits indépendants historiques ;
- scan Minecraft normal sans nouvel import :
  - conserver les dernières preuves curseforge-local pour le même path/SHA-256/taille comme aujourd’hui ;
- changement path/hash/taille :
  - aucune preuve locale héritée ;
- reimport du même fichier :
  - idempotent, aucune duplication ;
- un addon absent du nouveau profil :
  - son ancienne preuve curseforge-local disparaît de la nouvelle observation ;
- aucune suppression/modification des anciennes observations SQL : l’historique reste intact ;
- aucune migration/version.

Ne modifie pas la sémantique classification SUGGESTED/VERIFIED/CONFLICT déjà validée.
Ne touche pas aux conflits historiques individuellement.
Gate 4 Interstice reste ACQUIS.
F reste NON ACQUIS.

Tests obligatoires :
- import profil A puis profil B => seules preuves curseforge-local de B dans la nouvelle observation ;
- preuve Modrinth/JAR indépendante de A conservée si artifact identique ;
- addon absent de B => ancienne preuve curseforge-local supprimée ;
- scan normal après B => preuves B conservées ;
- changement d’octets => aucune preuve B héritée ;
- reimport B => idempotent ;
- conflits indépendants conservés.

Documenter brièvement le correctif.
Mettre à jour MANIFEST.sha256.
Exécuter les suites ciblées pertinentes, manifeste et diff-check.
Commit + push si propre.

Aucun merge/tag/release/bump, aucun gate réel.

Restitution finale compacte uniquement :
- nouveau HEAD ;
- fichiers modifiés ;
- règle de remplacement implémentée ;
- tests PASS/FAIL/N/A ;
- limite éventuelle.

Ne donne aucune commande de validation réelle à l'utilisateur.
~~~

## Réponse exacte

~~~text
1. **HEAD poussé** : `89b49e219fa60875dccf1cc04f07a75dc478c2cd`
2. **Fichiers** : `gamepanel/content_admin.py`, `tests/test_content_curseforge_032.py`, `WORK_STATE.md`, `docs/CHANGELOG.md`, `MANIFEST.sha256`.
3. **Règle** : import explicite remplace les anciennes preuves CurseForge locales ; preuves indépendantes conservées pour path/SHA-256/taille identiques. Rescan et historique SQL préservés.
4. **Tests** : 242 PASS, 100 N/A natifs POSIX, zéro FAIL final. Compileall, manifeste et diff-check PASS.
5. **Limites** : aucun gate réel relancé. Gate 4 ACQUIS ; F NON ACQUIS.
~~~

## Synthèse enregistrée

- Un import explicite remplace les anciennes preuves `curseforge-local` du profil précédent dans la nouvelle observation.
- Seules les preuves du nouveau `minecraftinstance.json` sont ajoutées.
- Les preuves indépendantes restent conservées si path/SHA-256/taille sont identiques.
- Les rescans normaux conservent les dernières preuves CurseForge locales.
- Un changement d’artifact n’hérite aucune preuve locale.
- Réimport idempotent, sans duplication.
- L’historique SQL reste intact ; aucune migration/version.
- Tests : **242 PASS / 100 N/A natifs POSIX / 0 FAIL final**.
- Compileall, manifeste et diff-check PASS.
- **Gate 4 ACQUIS ; F NON ACQUIS**.

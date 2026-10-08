# GP-076 — GPT-6.1 Sol Medium — scope local-jar selon loader

- Date : 2026-10-08
- Quota visible : 100 % → 91 % (**9 points**)
- Durée : **15 min 50 s**
- Résultat : succès
- Commit GamePanel : `6f41240010b6157f5d6e95f4be312e1b2ada1b5d`
- Draft PR : #22

## Prompt exact

~~~text
Repo : `MrMekouil/GamePanel`
Branche : `work/0.3.2-content-manifests`
PR : Draft #22
HEAD attendu : `89b49e219fa60875dccf1cc04f07a75dc478c2cd`

Utilise l'intégration GitHub connectée, sans clone réseau. Avant modification : vérifier branche, status, diff, diff --cached, log -10 et WORK_STATE.md. Préserver tout travail local ; aucun reset/revert.

**Problème confirmé sur Interstice (Forge 47.4.0)**

Sept conflits proviennent d'une interprétation `local-jar` de `fabric.mod.json:environment="*"` en `both/VERIFIED`, opposée à des déclarations exactes Modrinth `server-only/VERIFIED`.

Les sept JAR disposent également de `META-INF/mods.toml`. Ce sont Incendium, Terralith, create_ltab, doubledoors, lithosphere, treeharvester et worldedit.

**Mission**

1. Auditer la classification `local-jar` et déterminer combien d'assertions VERIFIED des 354 JAR dépendent de métadonnées Fabric, notamment avec un loader Forge sélectionné.
2. Corriger la prise en compte des métadonnées selon le loader et leur portée réelle. `fabric.mod.json` ne doit pas être traité comme une déclaration Forge autoritaire lorsqu'un JAR possède ses propres métadonnées Forge. Préserver le comportement valable des véritables mods Fabric.
3. Ne pas confondre « chargeable côté client » et « obligatoire côté client ».
4. Préserver la provenance des preuves et ne pas promouvoir artificiellement des UNKNOWN/SUGGESTED en VERIFIED.
5. Gérer les anciennes assertions `local-jar` devenues obsolètes après correction : elles ne doivent pas continuer à polluer les observations courantes à cause de la conservation des conflits, mais les anciennes observations SQL restent intactes.
6. Préserver les véritables conflits indépendants non concernés.

Tests ciblés : sept cas Forge/Fabric mixtes, véritables mods Fabric, source Modrinth indépendante, rescan après ancienne observation conflictuelle, non-régression classification et persistance.

Ne modifier ni les JAR, ni AutoModpack, ni les données réelles Interstice. Ne pas introduire l'import AutoModpack dans ce lot.

Documenter le résultat, actualiser MANIFEST.sha256 et WORK_STATE.md. Tests pertinents, diff-check, commit et push uniquement si propres.

Gate 4 acquis ; F non acquis. Aucun gate réel, merge, tag, release ou bump.

Restitution : HEAD, fichiers modifiés, impact mesuré, tests PASS/FAIL/N/A et limites.
~~~

## Réponse exacte

~~~text
1. **HEAD poussé** : `6f41240010b6157f5d6e95f4be312e1b2ada1b5d`
2. **Fichiers** : `content_providers.py`, `content_admin.py`, `tests/test_local_jar_scope_032.py`, `WORK_STATE.md`, `docs/CHANGELOG.md`, `docs/CONTENT_MANIFESTS_032.md`, `MANIFEST.sha256`.
3. **Correction** : preuve Fabric bornée au loader ; anciennes assertions locales recalculées, historique SQL et conflits indépendants préservés. Aucune policy client déduite.
4. **Impact** : 7 cas synthétiques corrigés. Total dépendant de Fabric parmi les 354 JAR réels **N/A**, faute d’export complet ; aucun retest serveur revendiqué.
5. **Tests** : 305 PASS, 150 N/A POSIX, zéro FAIL final. Syntaxe, manifeste et diff-check PASS.
6. **Statuts** : Gate 4 ACQUIS ; F NON ACQUIS. Aucun gate réel, merge/tag/release/bump.
~~~

## Synthèse enregistrée

- Sept conflits Forge/Fabric mixtes sont au cœur du correctif.
- Les preuves `local-jar` issues de Fabric sont désormais bornées au loader sélectionné.
- Sous Forge, `fabric.mod.json` n’est plus autoritaire lorsqu’une metadata Forge native est présente.
- Les anciennes assertions locales obsolètes sont recalculées pour les observations courantes ; l’historique SQL reste intact.
- Les conflits indépendants sont préservés.
- Aucune policy client n’est déduite.
- Sept cas synthétiques corrigés.
- Total réel dépendant de Fabric parmi les 354 JAR : **N/A** faute d’export complet.
- Aucun retest serveur revendiqué.
- Tests : **305 PASS / 150 N/A POSIX / 0 FAIL final**.
- Syntaxe, manifeste et diff-check PASS.
- **Gate 4 ACQUIS ; F NON ACQUIS**.

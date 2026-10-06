# GP-066 — GPT-6.1 Sol Medium — correctif hashes[].type CurseForge Desktop

- Date : 2026-10-06
- Quota visible : 100 % → 91 % (**9 points cumulés**)
- Durée : **7 min 02 s cumulées**
- Exécutions : **2 × 3 min 31 s**
- Résultat : succès
- Commit GamePanel : `b66e9948a16790d731c3c45a4e6fc5ed2b78dfd5`
- Draft PR : #22

## Prompt exact

~~~text
Modèle : GPT-6.1 Sol
Effort : Medium

Repo : MrMekouil/GamePanel
Branche : work/0.3.2-content-manifests
PR : Draft #22
HEAD attendu : df0b8254ad1238dd962298cfc412badaf7bdfbe4

Utilise l’intégration GitHub connectée ; pas de git clone réseau.

Validation Aero réelle : import reçu correctement, fraîcheur affichée, mais :
- 0 JAR associés
- 244 entrées sans preuve exacte

Blocker identifié :
`gamepanel/content_curseforge.py` cherche `installedFile.hashes[].algo`,
mais le minecraftinstance.json CurseForge Desktop réel utilise `hashes[].type`.

Corrige le parser local CurseForge.

Contrat :
- SHA-1 = hash entry `type == 1`, valeur 40 hex ;
- MD5 `type == 2` ignoré pour l’association ;
- conserver l’égalité SHA-1 exacte avec le JAR serveur ;
- latestFile/filename/fingerprint restent non probants ;
- installedFile.gameVersion reste l’unique source Client/Server ;
- categories reste ignoré.

Pour robustesse, si tu conserves une compatibilité `algo`, elle doit être
explicitement testée et `type`/`algo` contradictoires doivent être rejetés.
Ne déduis rien d’une API CurseForge et n’en appelle aucune.

Ajoute des fixtures réalistes `type:1`/`type:2` et un test anti-régression
prouvant que le format Desktop réel associe bien les SHA-1.
Corrige docs/état/manifeste qui parlent actuellement de `algo 1`.

Ne touche pas à Caddy/UI/SQLite sauf nécessité démontrée.
Pas de validation Aero réelle dans Work.
F reste NON ACQUIS.
Aucun merge/tag/release/bump.

Rerun suites ciblées et push sur la même branche si PASS.
Handoff compact : HEAD, tests PASS/FAIL/N/A, fichiers changés.
~~~

## Réponse exacte

~~~text
1. **HEAD poussé** : `b66e9948a16790d731c3c45a4e6fc5ed2b78dfd5`.
2. **Correctif** : SHA-1 Desktop `type: 1` reconnu, MD5 ignoré ; compatibilité `algo` testée, contradictions rejetées.
3. **Tests** : **262 PASS / 140 N/A, zéro FAIL ciblé**. Compileall, manifeste et diff-check PASS.
4. **9 fichiers changés** : parser, fixture, tests, WORK_STATE, ASSISTANT_STATE, CHANGELOG, CONTENT_MANIFESTS, VALIDATION et manifeste.
5. **Limites** : HTTP/scanner/store POSIX natifs N/A. Aucun retest Aero réel. PR #22 Draft ; **F NON ACQUIS**, aucun merge/tag/release/bump.
~~~

## Particularité de mesure

Le même run a dû être lancé **deux fois**. Le benchmark conserve une seule observation logique pour ce prompt/résultat final, avec le coût visible total **100 % → 91 % = 9 pts** et la durée cumulée **2 × 3:31 = 7:02**.

## Synthèse enregistrée

- SHA-1 CurseForge Desktop `hashes[].type == 1` reconnu ; MD5 `type == 2` ignoré pour l’association.
- Compatibilité `algo` rapportée comme testée ; contradictions `type`/`algo` rejetées.
- Tests ciblés : **262 PASS / 140 N/A**, zéro FAIL ; compileall, manifeste et diff-check PASS.
- **9 fichiers changés** selon le handoff.
- HTTP/scanner/store POSIX natifs N/A ; aucun retest Aero réel.
- PR #22 reste Draft ; **F NON ACQUIS** ; aucun merge/tag/release/bump.

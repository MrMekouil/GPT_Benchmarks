# GP-070 — GPT-6.1 Sol Medium — correctif fixture/test loader après FAIL Ubuntu

- Date : 2026-10-07
- Quota visible : 92 % → 89 % (**3 points**)
- Durée : **2 min 29 s**
- Résultat : succès
- Commit GamePanel : `0a234e3b203576ba05055468245b856c8e840055`
- Draft PR : #22

## Prompt exact

~~~text
Repo : MrMekouil/GamePanel
Branche : work/0.3.2-content-manifests
PR : Draft #22
HEAD attendu : 8db5517629e4dee2202ed569e546e5b8bb126dd3

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

Le retest Ubuntu réel de 835c96b a échoué :
tests.test_loader_selection_032.NativeSelection032.test_native_selection_two_forge_versions

Cause auditée : fixture/test uniquement.

1. Assertion invalide :
`assertNotIn("java", json.dumps(result))`
échoue légitimement sur la metadata Forge `modLoader: "javafml"`.

Remplace-la par une vérification ciblée prouvant que la commande brute du launcher / ExecStart n’est pas persistée, sans interdire le mot "java" dans les métadonnées de mod.

2. La fixture supprime seulement :
`.../1.20.1-47.3.0/unix_args.txt`
mais laisse le répertoire 47.3.0.
Le scanner l’énumère alors et produit RESOURCE_MISSING, donc complete=false.

Pour les tests à deux installations, supprimer proprement le répertoire fixture 47.3.0 avant de créer 47.2.0 + 47.4.0.
Vérifier aussi le cas NeoForge analogue.

Le test positif doit prouver :
- uniquement 47.2.0 + 47.4.0 installés ;
- launcher sélectionne 47.4.0 ;
- detection forge / 47.4.0 / 1.20.1 VERIFIED ;
- aucun LOADER_CONFLICT ;
- aucun RESOURCE_MISSING artificiel ;
- snapshot complete=true si aucun autre diagnostic fixture ;
- aucune commande brute run.sh/ExecStart persistée.

Aucun changement de code produit sauf nécessité démontrée.

Documente le FAIL Ubuntu puis le correctif fixture.
Mets à jour MANIFEST.sha256.

Gate 4 reste NON ACQUIS.
F reste NON ACQUIS.
Aucun merge/tag/release/bump.

Rerun les suites ciblées et push si PASS.

Restitution finale compacte uniquement :
- nouveau HEAD ;
- fichiers modifiés ;
- tests réellement exécutés avec PASS/FAIL/N/A ;
- éventuel blocage restant.
Ne donne aucune commande de validation réelle à l’utilisateur.
~~~

## Réponse exacte

~~~text
1. **HEAD poussé** : `0a234e3b203576ba05055468245b856c8e840055`.
2. **6 fichiers modifiés** : tests de sélection loader, WORK_STATE, ASSISTANT_STATE, VALIDATION_032, CHANGELOG et manifeste. Aucun code produit modifié.
3. **Tests** : **271 PASS / 147 N/A**, zéro FAIL exécuté. Compileall, docs, manifeste et whitespace PASS.
4. **Reste à confirmer** : tests natifs Ubuntu corrigés, N/A ici. FAIL précédent documenté ; **Gate 4 et F NON ACQUIS**, PR #22 Draft.
~~~

## Synthèse enregistrée

- Correctif **fixture/tests uniquement**.
- FAIL Ubuntu précédent : `test_native_selection_two_forge_versions`.
- Assertion globale interdisant « java » remplacée par une vérification ciblée de non-persistance de la commande brute.
- Fixture 47.3.0 nettoyée complètement avant les tests à deux installations ; cas NeoForge analogue couvert.
- Aucun code produit modifié.
- Tests : **271 PASS / 147 N/A**, zéro FAIL exécuté.
- Compileall, docs, manifeste et whitespace PASS.
- Retest Ubuntu natif encore requis.
- **Gate 4 et F restent NON ACQUIS**.

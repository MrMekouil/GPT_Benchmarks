# GP-030 — GPT-6 Luna Medium — contrat manuel E-C

- Date : 2026-10-02
- Quota visible : 99 % → 99 % (**~0 point visible**)
- Durée : **4 min 14 s**
- Résultat : succès
- Commit GamePanel : `8dff817dbb48c2c716fb0af5d4827cd803b3dd73`

## Prompt exact

~~~text
Travaille sur MrMekouil/GamePanel.

Branche existante :
work/0.3.1-ui-ux

PR :
Draft #19

HEAD attendu :
b78d765b1dbbb5a3a84a7d0c86bb2350a3ea5476

OBJECTIF

Corriger uniquement le test de régression 0.3.06 devenu obsolète après E-C.

Validation Ubuntu réelle actuelle :
- identity/startup : 78/78 PASS
- installateur : 105/105 PASS
- régressions ciblées : 99 tests exécutés, 1 seul FAIL

Échec :

tests.test_manual_instances_0306.ManualWebContract0306
.test_manual_flow_reuses_catalog_profile_path_and_opaque_resource

Assertion historique :

self.assertIn('/register`,"POST",{path:manualInstance.root}', self.manual_source)

Mais E-C a volontairement étendu le payload manuel à :

{path:manualInstance.root,...manualInstance.identity}

où manualInstance.identity contient uniquement :
- instance_id
- display_name

Le path reste celui du flux manuel existant et les propriétés techniques
(service, command, ports, secrets, Definition, etc.) restent non injectables.

À FAIRE

Mettre à jour uniquement le contrat de test afin qu’il vérifie le comportement E-C actuel.

Le test doit continuer à prouver :
- profil issu du catalogue ;
- resource_id opaque ;
- scan avec seulement path ;
- preview avec seulement path ;
- register avec path + identité bornée E-C ;
- aucune propriété technique libre côté client.

Ne pas assouplir le test plus que nécessaire.
Ne pas modifier web/app.js ni aucun code de production sauf preuve nouvelle.

Fichiers attendus :
- tests/test_manual_instances_0306.py
- MANIFEST.sha256

Pas de docs nécessaires pour cette correction de test pure.

Exécuter au minimum les tests disponibles pertinents.
Ne pas revendiquer Ubuntu PASS depuis Work.

Avant commit :
git diff
git diff --check
git status

Commit :

test: update manual registration identity contract

Push sur la même branche.

Ne pas merge.
Ne pas tag.
Ne pas commencer E-D.

Handoff :
- HEAD final
- fichiers modifiés
- confirmation aucun code production
- cause du test obsolète
- tests PASS/N/A
- commande Ubuntu ciblée à rejouer.
~~~

## Réponse exacte

~~~text
HEAD final : **`8dff817dbb48c2c716fb0af5d4827cd803b3dd73`**, poussé sur `work/0.3.1-ui-ux`. PR #19 reste Draft, non mergée et sans tag.

Fichiers modifiés : `tests/test_manual_instances_0306.py` et `MANIFEST.sha256`. Aucun code de production n’a changé.

Le contrat attendait encore l’ancien payload manuel avec `path` seul. Il vérifie maintenant `path` accompagné de l’identité E-C, limitée à `instance_id` et `display_name`; les assertions sur le profil catalogue, la ressource opaque et les propriétés techniques non injectables sont conservées.

**PASS Work :** contrat ciblé exécuté directement, compilation Python, manifeste vérifié et `git diff --check`. L’import normal du test est **N/A** dans Work faute d’`aiohttp`. Aucun PASS Ubuntu n’est revendiqué.

À rejouer sur Ubuntu :
```
python -m unittest -v tests.test_manual_instances_0306.ManualWebContract0306.test_manual_flow_reuses_catalog_profile_
```
~~~

> Note : la réponse fournie s’arrête sur cette commande Ubuntu tronquée ; elle est archivée telle quelle.

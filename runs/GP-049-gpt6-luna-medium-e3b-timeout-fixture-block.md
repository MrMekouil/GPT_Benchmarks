# GP-049 — GPT-6 Luna Medium — fixture timeout E3-B bloqué par environnement

- Date : 2026-10-04
- Quota visible : 100 % → 100 % (**~0 point visible**)
- Durée : **2 min 15 s**
- Résultat : **bloqué par l’environnement après correctif local**
- Commit GamePanel : aucun
- PR #22 : restée sur `5d4b0301f54ea8ba93d63dc305c8896f7f958283`

## Prompt exact

~~~text
Travaille sur MrMekouil/GamePanel.

Branche :
work/0.3.2-content-manifests

PR :
Draft #22

HEAD attendu :
5d4b0301f54ea8ba93d63dc305c8896f7f958283

OBJECTIF

Corriger uniquement le test Ubuntu E3-B :

tests.test_content_distribution_032.DistributionHTTP032.test_upload_network_timeout_leaves_no_observation_or_source

Le test actuel fait :

async def slow():
    await asyncio.sleep(0.15)
    yield DATA

Avec aiohttp TestClient, ce délai peut se produire avant que le handler serveur commence réellement à lire le body, ce qui produit 201 au lieu du 408 attendu.

Modifier uniquement la fixture pour que le serveur reçoive d’abord une partie du body, puis que le flux se bloque suffisamment longtemps pendant une lecture suivante, par exemple :

async def slow():
    yield DATA[:1]
    await asyncio.sleep(0.15)
    yield DATA[1:]

But :
- activer réellement le timeout serveur pendant request.content.read();
- attendre 408 ;
- vérifier toujours qu’aucune nouvelle observation n’est persistée ;
- vérifier que la source client-extra temporaire est nettoyée.

Avant modification :
- git branch --show-current
- git status
- git diff
- git diff --cached
- git log --oneline --decorate -10

Si HEAD ou état inattendu : STOP.
Aucun reset/revert/clean.

Ne touche à aucun code fonctionnel E3-B.
Ne touche pas aux docs.

Ensuite relance uniquement :

PYTHONPATH="$PWD" /opt/gamepanel/.venvs/d25d52dca517e628/bin/python -m unittest -v tests.test_content_distribution_032

Attendu Ubuntu :
42/42 PASS, aucun skip inattendu.

Puis :
- git diff --check ;
- régénère MANIFEST.sha256 puisque le test change ;
- vérifie le manifeste intégral ;
- relis le diff final.

Si tout passe :
commit + push sur la même branche.

Message suggéré :
test: exercise client-extra network timeout in flight

Ne merge pas.
Ne tague pas.
Ne commence pas E3-C/F.

Réponse finale courte :
commit/push + résultat exact des 42 tests + manifeste/diff-check.
~~~

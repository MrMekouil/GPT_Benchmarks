# GP-052 — GPT-6.1 Sol Medium — 0.3.2-E3-C UI Admin content réelle

- Date : 2026-10-04
- Quota visible : 98 % → 82 % (**16 points**)
- Durée : **18 min 52 s**
- Résultat : succès
- Commit GamePanel : `3de856089a389e7afa35a8f1606f8c0d395505c5`
- Draft PR : #22

## Prompt exact

~~~text
Travaille uniquement sur la branche indiquée.

Dépôt :
MrMekouil/GamePanel

Branche :
work/0.3.2-content-manifests

PR :
Draft #22

HEAD attendu :
94fbabc86ae658cb24a81df40f374885e849b997

OBJECTIF

Réaliser uniquement :

0.3.2-E3-C — brancher l’UI Admin “Contenus client” sur les vraies API E3-A/E3-B.

A/B/C/D/E1/E2/E3-A/E3-B sont acquis.
E global reste non acquis.
F non commencé.

Avant toute modification :
- vérifie branche/status/diff/diff --cached/log ;
- lis WORK_STATE.md ;
- lis ASSISTANT_STATE.md, docs/ASSISTANT_WORKFLOW.md et docs/CONTENT_MANIFESTS_032.md ;
- audite web/app.js, web/style.css, tests/web-content-032.cjs, tests/web-content-browser-032.cjs ;
- audite les contrats réels de gamepanel/content_api.py et content_distribution_api.py ;
- préserve toute modification non commitée ;
- aucun reset/revert/clean.

Si HEAD ou état inattendu : STOP.

PÉRIMÈTRE

Remplacer la préparation locale/volatile D par une intégration réelle, Admin uniquement.

La vue doit utiliser comme source de vérité :
GET /api/v1/admin/instances/{iid}/content

et permettre réellement :
- scan via POST .../content/scan ;
- création/modification du draft via PUT .../content/draft ;
- upload client-extra brut via POST .../content/client-extra ;
- publication via POST .../content/publish ;
- révocation via POST .../content/publications/{publication_id}/revoke.

Conserver clairement les trois niveaux :
1. inventaire observé ;
2. brouillon persistant ;
3. versions publiées.

UI attendue :
- choix d’instance Minecraft ;
- loading/empty/partial/error explicites ;
- diagnostics visibles ;
- environnement/politique/evidence/provenance visibles sans falsification ;
- UNKNOWN/CONFLICT clairement distingués ;
- destination client, distribution gamepanel/external/unavailable et locator externe si applicable ;
- raisons Admin explicites pour override/redistribution/acceptation unavailable quand nécessaires ;
- version humaine du draft ;
- révisions observation/draft visibles ou au minimum correctement gérées ;
- head, publications, révocation et état des jobs compréhensibles ;
- lien vers le manifest publié via la route E3-B ;
- aucun faux succès.

CLIENT-EXTRA

Remplacer les anciennes “notes locales” par un vrai sélecteur de fichier.

Upload :
- application/octet-stream brut ;
- pas de filename/path/query envoyé au backend ;
- CSRF existant ;
- progression sophistiquée non requise ;
- après succès, recharger l’état serveur ;
- le nom local du fichier peut servir d’aide visuelle temporaire mais ne doit jamais être présenté comme donnée persistée backend.

Le client-extra rejoint ensuite le draft comme toute autre entrée avec destination/décisions/redistribution explicites.

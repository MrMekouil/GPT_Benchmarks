# GP-020 — GPT-6 Sol Medium — 0.3.1-E-A contrat identité d’instance

- Date : 2026-10-01
- Quota visible : 88 % → 66 % (**22 points**)
- Durée : **14 min 13 s**
- Résultat : succès
- Commit GamePanel : `1a835501ff7b5a563f0b906c5b9177f407a3bdd2`

## Prompt exact

~~~text
Travaille sur le dépôt :

MrMekouil/GamePanel

Branche existante :

work/0.3.1-ui-ux

PR existante :

Draft #19 — 0.3.1 — Refonte UI/UX et finitions d'exploitation

HEAD documentaire validé à préserver :

92df2a3616735521a7479efde58edfa179ffb950
docs: record 0.3.1 real validation

OBJECTIF

Ouvrir et cadrer uniquement le checkpoint :

0.3.1-E-A — Contrat et dépendances de gestion Admin de l’identité des instances

Ce checkpoint doit déterminer précisément comment implémenter 0.3.1-E sans casser les invariants d’inventaire, de permissions, de recovery ou de persistance.

NE PAS encore faire la refonte UI complète de 0.3.1-E.
NE PAS merger/taguer.
NE PAS commencer 0.3.2.

CONTEXTE PRODUIT À RESPECTER

La roadmap définit 0.3.1-E ainsi :

- pendant l’ajout d’une instance, l’Admin peut choisir et modifier le nom affiché ainsi que l’identifiant futur avant confirmation finale ;
- après l’ajout, ces informations sont gérées depuis une vue Admin dédiée ;
- aucun contrôle d’édition ne doit être ajouté au dashboard normal ;
- modifier ensuite un identifiant d’instance doit être une mutation backend sûre et atomique traitant explicitement les références et dépendances persistées ;
- un simple changement visuel côté client est insuffisant.

État actuel :

- 0.3.1 CP1–CP4 validés ;
- desktop Ubuntu réel PASS ;
- mobile réel PASS ;
- update/runtime Ubuntu réel PASS ;
- BeamMP REQUALIFIÉ puis CONSERVÉ/SKIPPÉ PASS ;
- 0.3.1-E est le dernier sous-lot fonctionnel restant avant clôture de 0.3.1 ;
- base stable : v0.3.06 ;
- SQLite schema 4 ;
- ajout manuel d’instances issu de 0.3.06 déjà intégré ;
- inventaire root-owned et mutations d’inventaire déjà transactionnelles avec recovery ;
- backend non-root ;
- permissions/capabilities backend-authoritative ;
- grants explicites par instance.

RÈGLES STRICTES

- travailler uniquement sur work/0.3.1-ui-ux ;
- ne créer aucune branche ;
- ne modifier ni main ni une autre branche ;
- ne merger aucune PR ;
- ne créer aucun tag ;
- ne reset/revert/clean rien ;
- préserver tout travail local éventuel ;
- ne modifier docs/ROADMAP.md ;
- ne modifier ASSISTANT_STATE.md ;
- ne modifier le corps de la PR #19 ;
- ne toucher ni à BeamMP ni aux autres fonctionnalités 0.3.1 sauf dépendance directe démontrée ;
- ne changer aucun numéro de version ;
- ne changer le schéma SQLite que si une nécessité réelle est démontrée par l’audit ; ne pas créer une migration par confort ;
- ne commencer aucune implémentation risquée avant d’avoir fini la cartographie des références d’instance.

PRÉ-VOL OBLIGATOIRE

Avant toute modification :

git branch --show-current
git status
git diff
git diff --cached
git log --oneline --decorate -15

Puis lire intégralement :

WORK_STATE.md
docs/ASSISTANT_WORKFLOW.md

Lire les sections utiles de :

docs/ROADMAP.md
docs/ARCHITECTURE.md
docs/API.md
docs/VALIDATION_0306.md
docs/VALIDATION.md

AUDIT OBLIGATOIRE

Cartographier le cycle de vie complet de l’identité d’une instance :

1. Création / découverte / preview / register

   - où est calculé le futur Definition.id ;
   - où est calculé display_name ;
   - quelles données sont renvoyées au navigateur ;
   - quelles données le navigateur peut actuellement fournir ;
   - quelles données le helper privilégié redérive lui-même ;
   - quelles protections empêchent actuellement un id arbitraire dangereux.

2. Inventaire root-owned

   - format de /etc/gamepanel/instances.json ;
   - Definition.id et display_name ;
   - helper gamepanel-inventory ;
   - transactions existantes ;
   - backups / before / after / manifest ;
   - recovery au démarrage ;
   - verrous de configuration ;
   - register / qualify / reload.

3. SQLite et autres persistances
   Rechercher exhaustivement toutes les utilisations persistantes de l’id d’instance, notamment mais sans supposer que la liste est complète :

   - grants ;
   - settings ;
   - maintenance ;
   - opérations ;
   - audit/events ;
   - erreurs/états persistés ;
   - sessions si applicable ;
   - toute table avec server_id / instance_id ou équivalent ;
   - tout JSON / cache / état local associé à l’id.

4. Runtime mémoire

   - orchestrator ;
   - adapters ;
   - locks ;
   - états ;
   - opérations courantes ;
   - SSE ;
   - control/counters ;
   - toute map/dict indexée par Definition.id.

5. Intégrations externes/locales

   - qualifications installateur ;
   - fingerprints ;
   - Game Waker ;
   - RCON ;
   - fichiers status ;
   - BeamMP ;
   - éventuelles références d’id dans les fichiers d’intégration ou états d’installation.

6. Web/API

   - route actuelle PATCH /servers/{id}/settings ;
   - vérifier si display_name est déjà mutable et dans quel écran ;
   - page Admin → Instances ;
   - dialogue d’ajout manuel ;
   - dashboard normal ;
   - contrats JS/CSS existants ;
   - permissions Admin.

7. Tests
   Identifier tous les tests actuels couvrant :

   - register manuel ;
   - inventory transactions ;
   - recovery ;
   - grants ;
   - settings ;
   - reload ;
   - collision d’id ;
   - stale resource ;
   - API Admin Instances.

POINT CRITIQUE : RENOMMAGE D’IDENTIFIANT

Déterminer la stratégie sûre pour renommer un id existant.

Le résultat doit répondre explicitement aux questions suivantes :

A. Quelles références doivent changer avec l’id ?

B. Quelles références doivent volontairement conserver l’ancien id, par exemple historique/audit, si cela est préférable ?
Ne pas décider arbitrairement : analyser le contrat actuel et les conséquences.

C. Comment garantir qu’un crash ne puisse jamais laisser :

- inventaire avec nouvel id + SQLite avec ancien id ;
- SQLite avec nouvel id + inventaire avec ancien id ;
- runtimes partiellement renommés ;
- grants orphelins ;
- transaction impossible à récupérer ?

D. Peut-on étendre proprement la transaction d’inventaire/recovery existante ou faut-il un mécanisme différent ?

E. Quelles opérations doivent interdire le rename :

- instance active ?
- opération en cours ?
- mutation de configuration en cours ?
- transaction inventory pendante ?
  Déterminer les gardes minimales justifiées.

F. Quelles règles doit respecter un id choisi par l’Admin ?
Déduire les contraintes existantes et proposer un contrat précis :

- format ;
- longueur ;
- normalisation ;
- unicité ;
- ids réservés si nécessaire ;
- stabilité/casse ;
- comportement collision.

G. Le display_name peut-il être modifié indépendamment avec une mutation beaucoup plus simple ?
Vérifier si l’infrastructure actuelle le permet déjà.

AJOUT D’INSTANCE

Déterminer comment permettre à l’Admin de modifier avant confirmation :

- display_name proposé ;
- futur instance id.

Conserver impérativement la sécurité actuelle :

- le navigateur ne choisit jamais librement service, ExecStart, chemins privilégiés ou capabilities ;
- le helper revalide toujours la ressource opaque/stale ;
- profil fermé ;
- aucune construction de définition privilégiée par le navigateur ;
- collision vérifiée côté backend/helper ;
- aucun grant créé implicitement.

Ne pas transformer le resource_id opaque en instance id.

LIVRABLE DE CE CHECKPOINT

À la fin de l’audit, choisir UNE architecture précise et minimale pour 0.3.1-E.

Documenter :

1. contrat API envisagé ;
2. règles display_name ;
3. règles instance id ;
4. stratégie de création avec id personnalisé ;
5. stratégie de rename d’id existant ;
6. références migrées ;
7. références conservées ;
8. stratégie transaction/recovery ;
9. gardes/conflits ;
10. fichiers/modules qui devront changer au checkpoint d’implémentation ;
11. tests nécessaires ;
12. validation réelle Ubuntu nécessaire.

IMPORTANT :
ne pas produire trois architectures laissées au choix.
Comparer brièvement les options si nécessaire, puis retenir celle qui respecte le mieux les invariants existants.

IMPLÉMENTATION DANS CE CHECKPOINT

Par défaut : aucune implémentation fonctionnelle.

Ce checkpoint est un audit/contrat.

Une modification de code n’est autorisée que si elle est strictement nécessaire pour obtenir une preuve lors de l’audit, ce qui devrait normalement ne pas être le cas.

Mettre uniquement WORK_STATE.md à jour pour indiquer :

- 0.3.1-E-A ouvert ;
- audit terminé ;
- architecture retenue ;
- prochain checkpoint exact d’implémentation.

Ne pas modifier docs/ROADMAP.md.

Si WORK_STATE.md change :

- régénérer MANIFEST.sha256 selon la méthode existante ;
- vérifier les SHA-256 ;
- aucune entrée undefined.

VALIDATION

Avant commit :

- relire le diff complet ;
- git diff --check ;
- git status ;
- vérifier qu’aucun fichier fonctionnel n’a changé ;
- vérifier que docs/ROADMAP.md et ASSISTANT_STATE.md sont inchangés.

Le diff attendu doit être limité à :

WORK_STATE.md
MANIFEST.sha256

Si un autre fichier a changé, arrêter et expliquer pourquoi avant commit.

COMMIT

Si l’audit est complet et cohérent :

commit unique :

docs: define 0.3.1-E instance identity contract

Push sur :

work/0.3.1-ui-ux

Ne pas merger.
Ne pas taguer.

HANDOFF FINAL

Donner :

- HEAD final ;
- working tree final ;
- fichiers modifiés ;
- liste exhaustive des références persistantes trouvées pour l’id d’instance ;
- architecture retenue pour création + rename ;
- règles exactes de validation d’id ;
- stratégie transaction/recovery retenue ;
- gardes retenues ;
- références historiques volontairement non réécrites, s’il y en a ;
- liste exacte des fichiers qui devront changer au prochain checkpoint ;
- liste exacte des tests à ajouter/modifier ;
- risques encore ouverts ;
- prochain checkpoint recommandé : 0.3.1-E-B.
~~~

## Réponse exacte

~~~text
**0.3.1-E-A est cadré et poussé** sur `work/0.3.1-ui-ux` : commit `1a835501ff7b5a563f0b906c5b9177f407a3bdd2`. Seuls `WORK_STATE.md` et `MANIFEST.sha256` ont changé dans ce commit. La PR #19 reste Draft, ouverte et non mergée ; aucun tag ni code fonctionnel modifié.

**Références persistantes recensées :** `instances.id` et `definition_json`, `grants.instance_id`, `operations.instance_id`, `logs.instance_id`, `audit.instance_id`, les clés `settings` des durées de démarrage, résultats Workshop et offsets watcher ; l’inventaire root-owned ; les JSON d’intégration PZ et Waker ; les qualifications et empreintes de l’état installateur ; le drop-in systemd BeamMP nommé avec l’id ; les transactions BeamMP. Les chemins de secret Minecraft et de FIFO RimWorld peuvent être dérivés de l’id lors de leur création et devront rester stables après renommage. Sessions et comptes ne portent pas d’id d’instance.

**Architecture retenue :** à la création, l’Admin pourra fournir un id et un nom, tandis que le helper redérivera et vérifiera toujours la ressource, le service et la définition privilégiée. Après création, un PATCH Admin dédié gérera l’identité. L’id devra respecter exactement `^[a-z0-9][a-z0-9-]{0,63}$`, sans normalisation implicite, être unique et ne jamais réutiliser un ancien alias. Le nom sera trimé, limité à 1–80 caractères et dépourvu de caractères de contrôle.

Le renommage transférera en **une transaction SQLite** l’instance, ses grants, opérations et clés de réglage. Un journal root multi-fichiers et un marqueur SQLite guideront un recovery bloquant **avant le démarrage du runtime**. Les logs, audits et rapports historiques garderont leur ancien id, relié à l’id courant par des alias réservés. Le renommage sera refusé si l’instance n’est pas explicitement arrêtée ou si une opération, transaction ou mutation concurrente est en cours.

**E-B devra modifier :** `gamepanel/{models,api,instance_admin,db,orchestrator,integrations}.py`, `tools/gamepanel-inventory`, `deploy/sudoers.gamepanel`, `installer/__main__.py`, `web/app.js`, `web/style.css`, puis `docs/{API,ARCHITECTURE,VALIDATION}.md`, `WORK_STATE.md` et le manifeste. Tests à étendre : `test_instance_admin_030.py`, `test_manual_instances_0306.py`, `test_inventory_recovery_030.py`, `test_grants_admin_028.py`, `test_migration_030.py`, `test_qualification_cache_031.py`, `test_installer.py`, `test_maintenance_029.py` et les quatre contrats Web Instances/manuel/Serveurs/UI nommés dans `WORK_STATE.md`.

**Contrôles :** `git diff --check` PASS ; preuve SQLite des contraintes FK PASS ; manifeste : 172 empreintes locales vérifiées, aucune entrée invalide ou `undefined`. Le PNG absent du miroir local est présent dans l’arbre distant et son empreinte n’a pas été modifiée. Tests applicatifs, navigateur et Ubuntu : **N/A**, aucun code exécuté ni déployé pour cet audit.

**Risque ouvert :** l’ordre des verrous installateur/inventaire, le transfert de la preuve BeamMP et le recovery à chaque point de crash doivent être démontrés par les tests E-B avant tout renommage réel. Le miroir Git local reste sur `7ba3896` avec ses modifications préexistantes préservées ; le HEAD **distant** est bien `1a83550`. Prochain checkpoint : **0.3.1-E-B**.
~~~

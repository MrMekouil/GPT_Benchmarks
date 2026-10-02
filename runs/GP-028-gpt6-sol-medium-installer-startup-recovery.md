# GP-028 — GPT-6 Sol Medium — blocker installer/startup identity recovery

- Date : 2026-10-02
- Quota visible : 60 % → 39 % (**21 points**)
- Durée : **20 min 35 s**
- Résultat : succès
- Commit GamePanel : `f4bd104f5f9a401ae9c429176ee839b03ba704ae`

## Prompt exact

~~~text
Travaille sur MrMekouil/GamePanel.

Branche existante :
work/0.3.1-ui-ux

PR :
Draft #19

HEAD attendu :
11f19845baf275c2765e93454b3a3e8aed8b9bb8

OBJECTIF

Corriger uniquement le blocker réel découvert pendant le déploiement Ubuntu E-C :

collision entre le startup recovery d’identité B1 et l’installateur qui démarre
le nouveau backend pendant que sa propre transaction/verrou est encore actif.

Ne pas commencer E-D.
Ne pas modifier l’UI E-C sauf nécessité démontrée.
Ne pas affaiblir le protocole transactionnel B1.

PREUVE RÉELLE UBUNTU

Pendant une mise à jour normale 0.3.1 :

- l’installateur tient installer_lock autour de install.apply()
- /etc/gamepanel/installing existe pendant apply
- workflow.admin_and_start() démarre gamepanel.service
- le nouveau backend appelle immédiatement :
  gamepanel-inventory identity-recover
- le backend plante dans :
  api.create_app()
  -> InventoryBroker.recover_identity_sync()
  -> identity_response()
- le helper renvoie INVENTORY_HELPER_FAILED générique
- systemd retente puis l’installateur rollback
- après rollback, l’ancien backend repart normalement

CAUSE À CONFIRMER DANS LE CODE

installer/__main__.py conserve installer_lock(host) autour de install.apply().

RootIdentity.recover()
-> RootIdentity.locked()
-> installer_lock(self.host)
et refuse également /etc/gamepanel/installing / pending installer.

Le backend candidat essaie donc de reprendre le verrou que l’installateur parent
détient au moment précis où celui-ci lui demande de démarrer.

Le generic INVENTORY_HELPER_FAILED vient aussi du fait qu’installer_lock peut lever
InstallError alors que la branche identity du helper traduit uniquement IdentityError.

CONTRAT DU CORRECTIF

Le startup contrôlé par l’installateur doit pouvoir conclure « aucune identité à récupérer »
sans désactiver le fail-closed général.

Une solution acceptable doit respecter tous ces invariants :

1. Ne jamais supprimer installer_lock.
2. Ne jamais supprimer /etc/gamepanel/installing.
3. Ne jamais désactiver globalement identity-recover au startup.
4. Ne jamais ignorer simplement InstallError / IdentityError.
5. Une vraie transaction d’identité ou un marqueur SQLite pending doit toujours bloquer.
6. Un marqueur d’installation stale sans verrou installateur actif doit rester fail-closed.
7. Un verrou installateur actif sans preuve explicite d’installation contrôlée ne doit pas créer de bypass.
8. Le recovery B1 normal hors installation doit rester inchangé.

Approche recommandée à auditer puis implémenter si elle reste la plus sûre :

prévoir un fast-path STRICTEMENT borné pour identity-recover lorsque :
- /etc/gamepanel/installing existe et est une ressource protégée attendue ;
- le verrou installateur est réellement détenu par un autre processus ;
- aucune transaction d’identité root n’existe ;
- aucun marker SQLite identity-commit:* n’existe ;
- le schéma/DB nécessaires peuvent être lus de façon cohérente.

Dans ce seul cas propre :
return {"recovered": []}
sans essayer de reprendre le verrou déjà détenu.

Si une preuve manque, état illisible, transaction ou marker présent :
FAIL CLOSED.

Ne pas autoriser de rename pendant ce fast-path.
Aucune écriture de DB ou de fichier d’identité dans ce fast-path.

Si l’audit montre qu’une autre solution bornée est plus correcte, l’utiliser,
mais documenter pourquoi elle préserve exactement les invariants ci-dessus.

TESTS À AJOUTER

Couvrir explicitement :

- installation marker + installer lock réellement détenu + identité propre
  => identity-recover retourne recovered=[]
- même situation + transaction identité pending
  => refus
- même situation + identity-commit marker SQLite
  => refus
- marker d’installation stale sans verrou réellement détenu
  => refus
- verrou détenu sans marker d’installation
  => refus
- DB/état incohérent ou illisible
  => refus
- recovery B1 OLD/NEW existant inchangé
- rename normal inchangé
- scénario régression installateur/startup reproduisant le bug réel autant que possible

Important :
l’absence de Linux/POSIX dans Work NE DOIT PAS empêcher l’implémentation.
Écrire les tests POSIX nécessaires et les marquer N/A si non exécutables dans Work.
Exécuter tous les contrôles réellement disponibles.

REVALIDATION

Préserver les suites existantes B1/B2/E-C.
Ne pas déclarer Ubuntu PASS dans Work.

DOCS

Mettre à jour :
- WORK_STATE.md
- docs/VALIDATION.md
- éventuellement docs/ARCHITECTURE.md si le contrat de verrouillage doit être précisé
- MANIFEST.sha256

Documenter :
- l’échec réel de déploiement ;
- sa cause ;
- le correctif candidat ;
- validation Ubuntu de l’update encore requise.

SQLite reste schema 4.
Version reste 0.3.1.
PR reste Draft.

Avant commit :
git diff
git diff --check
git status
tests disponibles

Commit unique proposé :

fix: allow safe identity check during installer startup

Push sur :
work/0.3.1-ui-ux

Ne pas merge.
Ne pas tag.
Ne pas commencer E-D.

Handoff :
- HEAD
- fichiers modifiés
- cause exacte
- mécanisme du correctif
- cas fail-closed conservés
- tests PASS / N/A
- commandes Ubuntu précises à rejouer
- confirmation E-C toujours candidate et E-D non commencé.
~~~

## Réponse exacte

~~~text
Le correctif candidat est commité et poussé sur `work/0.3.1-ui-ux` : **`f4bd104`**. La PR #19 reste Draft, non mergée et sans tag.

L’échec venait du démarrage du nouveau backend pendant que l’installateur détenait encore son verrou : `identity-recover` tentait de le reprendre. Il retourne désormais `recovered=[]` uniquement si le marqueur d’installation et le verrou détenu sont vérifiés, qu’aucune transaction ou décision d’identité n’est en attente et que SQLite est lisible de façon cohérente. Un état incertain, notamment un WAL non checkpointé, bloque toujours le démarrage. Le recovery B1 normal et le rename restent inchangés.

**Fichiers modifiés :** `installer/identity.py`, `tools/gamepanel-inventory`, `tests/test_identity_root_031.py`, nouveau `tests/test_identity_installer_startup_031.py`, `WORK_STATE.md`, `docs/ARCHITECTURE.md`, `docs/VALIDATION.md` et `MANIFEST.sha256`.

**PASS Work :** 35 tests Python exécutés, deux contrats Web E-C, compilation Python, `git diff --check` et vérification du manifeste. **N/A Work :** 43 scénarios natifs ignorés ; la suite installateur ne s’importe pas sous Windows faute de `fcntl`. Aucun PASS Ubuntu post-correctif n’est revendiqué.

À rejouer avec le Python du venv sur Ubuntu :
```
(umask 0002; python -m unittest -v tests.test_identity_installer_startup_031 tests.test_identity_sql_031 tests.test_identity_root_031 tests.test_identity_runtime_031 tests.test_identity_admin_031)
python -m unittest -v tests.test_installer tests.test_installer_021 tests.test_installer_022 tests.test_installer_023
python -m unittest -v tests.test_instance_admin_030 tests.test_inventory_recovery_030 tests.test_manual_instances_0306 tests.test_grants_admin_028 tests.test_migration_030 tests.test_maintenance_029 tests.test_qualification_cache_031
```

Une **update Ubuntu réelle**, incluant le démarrage du backend sous le verrou installateur, reste nécessaire. E-C demeure candidate ; E-D n’a pas commencé. SQLite reste au schéma 4 et la version à 0.3.1.
~~~

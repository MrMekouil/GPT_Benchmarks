# GP-023 — GPT-6 Luna Medium — B1d compatibilité installateur historique

- Date : 2026-10-02
- Quota visible : 99 % → 99 % (**~0 point visible**)
- Durée : **3 min 32 s**
- Résultat : succès
- Commit GamePanel : `45d4a3872d727677378443fe700e19c42a2ef90b`

## Prompt exact

~~~text
Reprends MrMekouil/GamePanel sur :

work/0.3.1-ui-ux

HEAD attendu :
3c6c7e1c050310e779c2b838799cd7dbc87e0286

PR #19 Draft.

OBJECTIF

Corriger uniquement la dernière régression installateur révélée par la validation Ubuntu de 0.3.1-E-B1.

Ne pas commencer B2.

RÉSULTAT UBUNTU

Les trois tests suivants échouent encore :

- tests.test_installer_021.UbuntuRegressions.test_complete_cli_upgrade_with_ubuntu_link_binary_timer_and_automatic_waker
- tests.test_installer_022.RealConfigurationRegression.test_full_cli_upgrade_with_the_real_firewall_and_waker_has_one_confirmation
- tests.test_installer_023.PzInstallerRegression.test_full_upgrade_uses_real_rcon_check_and_preserves_game_and_config

Ils passent désormais le garde `existing_work()` corrigé en B1b et échouent plus tard dans :

installer/workflow.py -> write_inventory()
gamepanel/identity.py -> aliases()

Cause :

write_inventory() appelle actuellement `aliases(conn)` dès qu'une gamepanel.db existe.

Mais les fixtures d'upgrade historique de ces tests possèdent une DB minimale avec `users` et `operations`, sans table `settings`.

`aliases()` exécute directement :
SELECT value FROM settings ...

=> sqlite3.OperationalError.

CORRECTION ATTENDUE

Corriger la compatibilité dans `installer/workflow.py::write_inventory()`.

Ne pas assouplir `gamepanel.identity.aliases()` : il doit rester strict dans le runtime schema 4.

Avant de rechercher les alias réservés, détecter via sqlite_master si la table `settings` existe.

- DB historique sans `settings` :
  considérer qu'aucun alias d'identité B1 ne peut exister et poursuivre l'upgrade.
- `settings` présente :
  utiliser le contrôle d'alias actuel.
- alias présent/réservé :
  conserver le refus actuel.
- ne créer aucune table ;
- ne modifier aucune DB pendant cette vérification ;
- ne masquer aucune DB moderne réellement incohérente.

Vérifier également le cas où un alias existe mais où les tables requises par son interprétation sont incohérentes : ce cas doit rester fail-closed, pas être traité comme une vieille DB saine.

TESTS

Ajouter/adapter des tests ciblés couvrant write_inventory :

1. DB historique sans settings => autorisé ;
2. DB moderne avec settings sans alias => autorisé ;
3. DB avec alias réservé correspondant à un id d'inventaire => refus ;
4. structure moderne incohérente avec alias présent => refus/fail-closed.

Ne pas modifier les anciens tests uniquement pour les faire passer si la compatibilité doit être assurée par le code.

VALIDATION

Exécuter si possible :
- tests identity SQL ;
- tests installer 021/022/023 ;
- git diff --check ;
- compileall.

Linux/POSIX N/A dans Work Windows si nécessaire.

Mettre à jour WORK_STATE.md et docs/VALIDATION.md :
- expliquer que B1c a validé le fixture no-op ;
- consigner cette dernière régression write_inventory/aliases ;
- B1 reste conditionné à la revalidation Ubuntu finale.

Régénérer MANIFEST.sha256.

Commit unique :

fix: preserve historical installs during identity checks

Push sur la même branche.

Pas de merge.
Pas de tag.
Pas de B2.

Handoff :
- HEAD final ;
- fichiers modifiés ;
- cause/correction ;
- tests ;
- commandes Ubuntu précises à rejouer.
~~~

## Réponse exacte

~~~text
**Commit poussé :** `45d4a3872d727677378443fe700e19c42a2ef90b` sur `work/0.3.1-ui-ux`. La PR #19 reste Draft.

Fichiers modifiés : `installer/workflow.py`, `tests/test_identity_sql_031.py`, `WORK_STATE.md`, `docs/VALIDATION.md` et `MANIFEST.sha256`.

`write_inventory()` vérifie maintenant dans `sqlite_master` si `settings` existe avant d’appeler `aliases()`. Une DB historique sans cette table est lue sans modification et l’upgrade continue. Si elle existe, les alias sont toujours contrôlés strictement : un id réservé est refusé et une structure incohérente échoue sans écrire l’inventaire. Quatre tests couvrent ces cas. Aucun changement à `aliases()` ni au protocole root.

Work : **17 tests PASS, 20 tests root/runtime SKIP**, `compileall` et `git diff --check` PASS. Les suites installateur 021/022/023 sont N/A dans Windows, car `fcntl` manque. Le manifeste compte 178 entrées, dont 177 vérifiées localement ; le hash de l’image absente du miroir a été conservé.

À rejouer sur Ubuntu :
```
umask 022 && .venv/bin/python -m unittest -q tests.test_identity_sql_031 tests.test_identity_root_031 tests.test_identity_runtime_031
umask 0002 && .venv/bin/python -m unittest -q tests.test_identity_sql_031 tests.test_identity_root_031 tests.test_identity_runtime_031
.venv/bin/python -m unittest -q tests.test_installer_021 tests.test_installer_022 tests.test_installer_023
```

B1 reste conditionné à cette revalidation Ubuntu finale. B2 n’est pas commencé ; aucun merge ni tag.
~~~

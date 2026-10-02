# GP-029 — GPT-6 Luna Medium — fixture cleanup installer identity marker

- Date : 2026-10-02
- Quota visible : 100 % → 99 % (**1 point**)
- Durée : **3 min 11 s**
- Résultat : succès
- Commit GamePanel : `b78d765b1dbbb5a3a84a7d0c86bb2350a3ea5476`

## Prompt exact

~~~text
Travaille sur MrMekouil/GamePanel.

Branche existante :
work/0.3.1-ui-ux

PR :
Draft #19

HEAD attendu :
f4bd104f5f9a401ae9c429176ee839b03ba704ae

OBJECTIF

Corriger uniquement le test POSIX en échec après le correctif du startup identity-recover.

Échec Ubuntu réel :

test_installer_startup_through_real_helper_and_backend_broker
=> AssertionError: CandidateError not raised

CAUSE À CONFIRMER

Dans tests/test_identity_root_031.py :

- le context manager installing(marker=True) crée
  /etc/gamepanel/installing
- son finally libère le child/flock mais ne supprime jamais le marker
- dans test_installer_startup_through_real_helper_and_backend_broker :
  1. un premier `with self.installing():` laisse donc le marker présent ;
  2. le test enchaîne dans le MÊME fixture avec
     `with self.installing(marker=False)`
  3. il croit tester « installer lock sans marker », mais l’ancien marker est encore présent ;
  4. RootIdentity.recover() prend alors correctement installer_startup_clean()
     et retourne recovered=[] au lieu de lever CandidateError.

Le test indépendant
test_installer_lock_without_marker_remains_fail_closed
passe avec un setUp propre, ce qui indique que le comportement production attendu
est déjà correct.

À FAIRE

Corriger le fixture de test, pas le code de production, sauf nouvelle preuve concrète.

Préférer :
- le context manager `installing()` doit nettoyer le marker qu’il a lui-même créé ;
- reproduire autant que possible le vrai cycle installateur :
  le marker est retiré pendant que le lock est encore détenu, puis le lock est relâché ;
- ne jamais supprimer un marker que `marker=False` n’a pas créé ;
- conserver les protections/permissions du fixture.

Vérifier que cela n’affaiblit aucun autre test :
- marker exact + lock détenu => recovered=[]
- marker stale sans lock => refus
- lock sans marker => refus
- marker invalide/protection invalide => refus
- transaction identity pending => refus
- marker SQL => refus
- WAL ambigu => refus
- helper/broker intégré => PASS

Ne modifier aucun fichier production si non nécessaire.
Ne modifier ni UI E-C ni docs fonctionnelles sauf nécessité stricte.
Si seul le test change, MANIFEST.sha256 doit être régénéré.

Exécuter les tests disponibles.
Ne pas revendiquer Ubuntu PASS depuis Work.

Avant commit :
git diff
git diff --check
git status

Commit unique proposé :

test: fix installer identity marker fixture cleanup

Push sur la même branche.

Ne pas merge.
Ne pas tag.
Ne pas commencer E-D.

Handoff :
- HEAD final
- fichier(s) modifié(s)
- confirmation qu’aucun code production n’a changé
- cause exacte du faux négatif
- tests PASS/N/A
- commande Ubuntu à rejouer.
~~~

## Réponse exacte

~~~text
HEAD poussé : **`b78d765b1dbbb5a3a84a7d0c86bb2350a3ea5476`**. La PR #19 reste Draft, non mergée et non taguée.

Seuls `tests/test_identity_root_031.py` et `MANIFEST.sha256` ont changé. Aucun code de production n’a été modifié.

Le faux négatif venait du premier contexte de test : il laissait le marqueur `installing` en place. Le fixture le supprime désormais pendant que le processus détient encore le verrou, puis libère le verrou. Avec `marker=False`, il ne touche pas au marqueur.

**Work :** 23 tests PASS, 22 tests POSIX N/A (`fcntl` indisponible), `compileall` et `git diff --check` PASS. Aucun PASS Ubuntu revendiqué.

À rejouer sur Ubuntu :
```
python -m unittest -v tests.test_identity_root_031 tests.test_identity_installer_startup_031 tests.test_identity_sql_031
```

La branche distante et la PR pointent sur le nouveau HEAD. Le miroir de travail local conserve des modifications préexistantes ; elles n’ont pas été nettoyées ni incluses dans ce commit.
~~~

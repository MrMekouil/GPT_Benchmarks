# GP-055 — GPT-6.1 Sol Medium — correctif fixture ContentStore Ubuntu

- Date : 2026-10-04
- Quota visible : 100 % → 94 % (**6 points**)
- Durée : **5 min 04 s**
- Résultat : succès
- Commit GamePanel : `0f3f408c598c2f6575a211b7595309cf7492ea56`
- Draft PR : #22

## Prompt exact

~~~text
Travaille uniquement sur :

Dépôt :
MrMekouil/GamePanel

Branche :
work/0.3.2-content-manifests

PR :
Draft #22

HEAD distant attendu :
c987ee3ee044fc9eb86a01515a9a5a614d916ec6

OBJECTIF UNIQUE

Corriger le FAIL Ubuntu de la nouvelle fixture ContentStore, sans modifier
la logique de production sauf preuve d’un vrai défaut.

Résultat réel Ubuntu :

tests.test_content_store_032
Ran 10 tests
FAILED (failures=1)

FAIL :
test_search_only_parent_store_creation_anchor_and_startup

Trace finale :
ContentPublication.startup
→ recover()
→ require(set(self.store.staging_jobs()) <= set(by_id),
          "CONTENT_JOURNAL_ORPHAN")
→ ContentError: CONTENT_JOURNAL_ORPHAN

CAUSE DÉJÀ AUDITÉE

Dans le test, avant ContentPublication.startup(), la fixture exécute :

with store.job_directory('a' * 32, create=True) as fd:
   os.fsync(fd)

Cela crée réellement un répertoire staging/<job_id>.

La DB fixture ne contient aucun content_jobs correspondant.

Le recovery refuse donc correctement ce staging orphelin.
Ce comportement CONTENT_JOURNAL_ORPHAN est un invariant de sécurité attendu.

Le FAIL n’est donc pas une preuve d’échec du correctif O_PATH.

À FAIRE

- vérifier branche/status/diff/log et HEAD exact ;
- aucun reset/revert/clean ;
- auditer le test et ContentPublication.recover avant modification ;
- corriger uniquement la fixture si ce diagnostic est confirmé.

Correction préférée :
- conserver le test de création/fsync du job_directory ;
- nettoyer proprement le job avec l’API normale du store avant de lancer
  ContentPublication.startup(), afin que le startup soit testé sur un état cohérent ;
- ne pas supprimer/affaiblir le contrôle CONTENT_JOURNAL_ORPHAN ;
- ne pas insérer un faux job SQL/journal inutilement si cleanup() suffit ;
- ne pas masquer l’erreur par catch/skip.

Le test doit toujours couvrir :
- parent search-only réellement non ouvrable O_RDONLY ;
- O_PATH traversable ;
- ContentStore(data_dir) fonctionne ;
- création content/* ;
- validate_anchor ;
- création/fsync staging ;
- cleanup propre du staging ;
- ContentPublication.startup réel ensuite ;
- symlinks/owner/mode/inode/escape toujours refusés.

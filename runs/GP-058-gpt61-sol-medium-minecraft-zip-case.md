# GP-058 — GPT-6.1 Sol Medium — collisions ZIP/JAR case-sensitive

- Date : 2026-10-04
- Quota visible : 84 % → 80 % (**4 points**)
- Durée : **4 min 57 s**
- Résultat : succès
- Commit GamePanel : `d0b1d101fc904b15bbb267adb7b4fc1a7d8c4bc8`
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
46a52600adea741358a772655465ff5005a0f991

OBJECTIF UNIQUE

Corriger le nouveau blocker réel du scan Aero :

CONTENT_SCAN_AMBIGUOUS_ARCHIVE

Cause réelle identifiée dans :
railways-0.3.0-beta.2+neoforge-mc1.21.1.jar

Deux entrées distinctes :

assets/railways/models/block/bogey/wide/scotch_yoke/Broad_Gauge_L_0-2-0.bbmodel

assets/railways/models/block/bogey/wide/scotch_yoke/broad_gauge_l_0-2-0.bbmodel

Le scanner les considère actuellement identiques car inspect_archive_metadata()
canonicalise les noms avec :

unicodedata.normalize("NFC", ...).casefold()

Même logique dans les composants de chemin.

CONTEXTE SÉCURITÉ

Les noms internes ZIP/JAR sont case-sensitive.

Ces ressources ne sont jamais extraites vers le filesystem par GamePanel.
Le JAR est observé/inspecté en lecture seule et identifié par son hash.

La collision ci-dessus est donc légitime dans un JAR et ne doit pas être assimilée
à un doublon exact.

Ne relâche PAS les chemins filesystem Minecraft/store/providers.

F reste NON ACQUIS.
Gate 4 reste NON ACQUIS.
Aucun gate suivant.
Pas de merge/tag/version bump.

AVANT MODIFICATION

- branche/status/diff/diff --cached/log ;
- vérifie HEAD distant exact ;
- lis WORK_STATE.md ;
- lis ASSISTANT_STATE.md ;
- lis docs/ASSISTANT_WORKFLOW.md ;
- lis docs/VALIDATION_032.md ;
- audite gamepanel/minecraft_content.py ;
- audite tests/test_minecraft_content_032.py.

Aucun reset/revert/clean.
STOP si état inattendu.

CORRECTIF ATTENDU

Pour les noms INTERNES ZIP/JAR uniquement :

- conserver unicodedata.normalize("NFC", ...);
- ne plus appliquer casefold() pour détecter les doublons/collisions ;
- comparaison donc case-sensitive après NFC.

Même politique pour :
1. full-path collision ;
2. component collision.

Conserver strictement :
- doublon exact même casse => AMBIGUOUS_ARCHIVE ;
- collision Unicode NFC => AMBIGUOUS_ARCHIVE ;
- vrai conflit fichier/répertoire sur le même nom canonique => AMBIGUOUS_ARCHIVE ;
- fichier utilisé comme ancêtre exact => AMBIGUOUS_ARCHIVE ;
- traversal ../ ;
- absolus ;
- backslash ;
- NUL/contrôles ;
- types ZIP dangereux ;
- limites archive/metadata/ratio/expanded ;
- aucune extraction.

Ne modifie pas `_parts()` filesystem.
Ne modifie pas les permissions système.

TESTS OBLIGATOIRES

Adapter les tests existants pour prouver :

ACCEPTÉ :
- ("A", "a") comme deux entrées internes distinctes ;
- ("A/x", "a/y") ;
- le cas réel :
  Broad_Gauge_L_0-2-0.bbmodel
  broad_gauge_l_0-2-0.bbmodel

REFUSÉ :
- ("a", "a") doublon exact ;
- ("é", "e\u0301") collision NFC ;
- ("a", "a/b") conflit fichier/ancêtre exact ;
- fichier "a" + répertoire "a/" ;
- traversal / contrôles / backslash inchangés.

Vérifier aussi que META-INF exact continue à être lu uniquement sur son nom exact
et qu’une variante de casse ne peut pas écraser/remplacer la metadata canonique.

RETESTS

Au minimum :
- tests.test_minecraft_content_032
- tests.test_content_classification_032
- tests.test_content_admin_032
- tests.test_content_store_032
- tests.test_content_publication_032
- tests.test_content_upgrade_032
- tests.test_release_docs

Puis :
- compileall ;
- git diff --check ;
- MANIFEST.sha256 complet ;
- audit du diff.

DOCUMENTATION

Consigner :
- scan Aero après correctif archive limits : nouveau FAIL AMBIGUOUS_ARCHIVE ;
- collision réelle Broad_Gauge vs broad_gauge ;
- cause : casefold trop strict pour noms internes JAR ;
- nouveau contrat : NFC-sensitive mais case-sensitive ;
- doublons exacts/NFC/file-ancestor toujours refusés ;
- aucune règle filesystem affaiblie ;
- F NON ACQUIS ;
- Gate 4 NON ACQUIS.

Commit + push même branche / PR #22.
Ne merge pas.
Ne tague pas.
Ne bump pas.
Ne lance aucun scan réel dans Work.

Réponse finale courte :
- cause ;
- correctif ;
- tests ;
- commit poussé ;
- commande Ubuntu de retest.
~~~

## Réponse exacte

~~~text
Cause : casefold() assimilait les deux ressources Railways distinctes.

Correctif : comparaisons ZIP complètes et par composants **sensibles à la casse après NFC**. Doublons exacts/NFC et conflits fichier/ancêtre toujours refusés ; metadata au nom exact, filesystem inchangé.

Tests Windows : scanner **36 PASS / 24 N/A**, régressions **129 PASS / 87 N/A**. Compileall, release-docs, manifeste et diff-check **PASS**.

Commit poussé : [**d0b1d10**](https://github.com/MrMekouil/GamePanel/commit/d0b1d101fc904b15bbb267adb7b4fc1a7d8c4bc8), Draft #22.

Retest Ubuntu depuis le checkout :
```
PYTHONPATH="$PWD" /opt/gamepanel/.venvs/d25d52dca517e628/bin/python -m unittest -v tests.test_minecraft_content_032 tests.test_content_classification_032 tests.test_content_admin_032 tests.test_content_store_032 tests.test_content_publication_032 tests.test_content_upgrade_032 tests.test_release_docs
```

**F et Gate 4 NON ACQUIS. Aucun scan réel ni gate suivant exécuté.**
~~~

## Synthèse enregistrée

- Cause rapportée : `casefold()` assimilait les deux ressources Railways distinctes.
- Correctif rapporté : comparaisons ZIP full-path et composants **sensibles à la casse après NFC**.
- Doublons exacts/NFC et conflits fichier/ancêtre restent refusés ; metadata au nom exact ; filesystem inchangé.
- Tests Work Windows : scanner **36 PASS / 24 N/A**, régressions **129 PASS / 87 N/A** ; compileall, release-docs, manifeste et diff-check **PASS**.
- Statut 0.3.2-F : **NON ACQUIS** ; Gate 4 **NON ACQUIS** ; aucun scan réel ni gate suivant exécuté.

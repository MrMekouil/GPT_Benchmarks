# GP-057 — GPT-6.1 Sol Medium — policy JAR réelle Minecraft

- Date : 2026-10-04
- Quota visible : 89 % → 84 % (**5 points**)
- Durée : **7 min 02 s**
- Résultat : succès
- Commit GamePanel : `46a52600adea741358a772655465ff5005a0f991`
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
fad9b8b39a12199749c3e4b91710d4c7380944a4

OBJECTIF UNIQUE

Rendre le scanner Minecraft 0.3.2 compatible avec des JAR réels modernes
observés sur minecraft-aero, sans affaiblir les protections archive/path.

F reste NON ACQUIS.
Gate 4 non acquis.
Aucun gate suivant.
Pas de merge/tag/version bump.

AVANT MODIFICATION

- vérifie branche/status/diff/diff --cached/log ;
- vérifie HEAD distant exact ;
- lis WORK_STATE.md, ASSISTANT_STATE.md ;
- lis docs/ASSISTANT_WORKFLOW.md ;
- lis docs/VALIDATION_032.md ;
- audite gamepanel/minecraft_content.py ;
- audite tests/test_minecraft_content_032.py.

Aucun reset/revert/clean.
Si état inattendu : STOP.

ÉTAT VALIDÉ UBUNTU

Correctif traversée scanner :
- tests.test_minecraft_content_032 : 51/51 PASS Ubuntu ;
- régressions content/classification/upgrade/release-docs : 258/258 PASS.

Le scan réel Aero atteint maintenant les JAR mais échoue sur les limites
d’archive.

DIAGNOSTIC RÉEL DES JAR AERO

Design-n-Decor-1.21.1-2.2b.jar
- entries = 10307 > 10000

butchery-5.2-neoforge-1.21.1.jar
- entries = 10615 > 10000

create-1.21.1-6.0.10.jar
- entries = 12536 > 10000

createaddoncompatibility-neoforge-1.21.1-1.0.0.jar
- entrée interne :
  LICENSE_Create: Addon Compatibility
- rejet UNSAFE_PATH à cause du caractère ":"

createfood-neoforge-1.21.1-2.7.1.jar
- entries = 18062 > 10000
- entrée interne :
  LICENSE_Create: Food

railways-0.3.0-beta.2+neoforge-mc1.21.1.jar
- entries = 26251 > 10000
- central = 3136643 > 2097152

rechiseled-1.2.5-neoforge-mc1.21.jar
- entries = 22900 > 10000
- central = 2660250 > 2097152

refurbished_furniture-neoforge-1.21.1-1.0.22.jar
- META-INF/MANIFEST.MF = 1056319 bytes > 65536
- metadata_total = 1057955 > 262144

Ces fichiers sont les vrais mods de l’instance.
Ne contourne pas le scanner et ne recommande pas de supprimer les mods.

AUDIT / CORRECTIF ATTENDU

1. Limites archive

Les defaults actuels :
- archive_entries = 10000
- central_bytes = 2 MiB

sont trop bas pour les JAR réels ci-dessus.

Choisir des plafonds modestement supérieurs aux preuves réelles avec marge,
tout en conservant les autres protections :
- file_bytes ;
- expanded_bytes ;
- entry_bytes ;
- compression_ratio ;
- scan_bytes ;
- deadline.

Valeurs candidates raisonnables à auditer :
- archive_entries : 32768 ou plafond voisin justifié ;
- central_bytes : 4 MiB ou plafond voisin justifié.

Ne monte pas arbitrairement à des valeurs énormes.

2. Noms internes JAR avec ":"

Ne relâche PAS `_parts()` globalement si cette primitive protège aussi des
chemins filesystem réels.

Audite son usage.

Si confirmé :
- distinguer validation d’un chemin filesystem Minecraft
  et validation d’un nom interne ZIP/JAR ;
- autoriser au minimum ":" dans un nom d’entrée archive si cela ne crée aucun
  risque dans ce contexte ;
- conserver refus absolu de :
  chemins absolus,
  "..",
  segments vides,
  backslash,
  NUL/contrôles,
  ambiguïtés NFC/casse,
  symlinks/types archive dangereux,
  noms servant à échapper à l’archive.

Aucune entrée archive n’est extraite vers le filesystem.

Ne relâche pas inutilement `< > " | ? *` si aucune preuve ne le nécessite.

3. Gros MANIFEST.MF

Le MANIFEST réel fait ~1.06 MiB.

Audite deux solutions :
A) plafond metadata augmenté de manière bornée ;
B) traitement spécial MANIFEST : lire/parser uniquement la section principale
  nécessaire tout en consommant de manière bornée le reste pour validation CRC.

Choisir la solution la plus simple qui reste sûre et maintient :
- borne mémoire ;
- borne CPU ;
- CRC/structure vérifiée ;
- metadata réellement utilisée seulement ;
- pas de lecture illimitée.

Si simple augmentation :
valeurs candidates raisonnables :
- metadata_bytes environ 2 MiB ;
- metadata_total environ 4 MiB.

Ne transforme pas metadata en lecture illimitée.

TESTS OBLIGATOIRES

Ajouter des régressions prouvant :
- archive légitime >10000 entrées acceptée selon nouveau plafond ;
- archive > nouveau plafond toujours refusée ARCHIVE_LIMIT ;
- central >2 MiB mais sous nouveau plafond accepté ;
- central > nouveau plafond refusé ;
- nom interne LICENSE_Create: Food accepté ;
- "../", absolu, backslash, contrôles et ambiguïtés restent refusés ;
- MANIFEST >64 KiB correspondant au cas réel accepté ;
- metadata au-delà du nouveau contrat toujours refusé ;
- ratio de compression / expanded_bytes / entry_bytes inchangés et toujours
  protecteurs.

Évite des tests inutilement très lourds si les limites peuvent être testées
avec Limits personnalisés + assertions explicites sur les defaults réels.

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

Consigner exactement :
- scan Aero après O_PATH : traversal corrigée, nouvel échec sur archive policy ;
- métriques réelles des 8 JAR ci-dessus ;
- limites choisies et justification ;
- traitement retenu pour ":" interne ;
- traitement retenu pour gros MANIFEST ;
- aucune protection traversal/ZIP bomb supprimée ;
- F NON ACQUIS ;
- Gate 4 NON ACQUIS ;
- aucun gate suivant exécuté.

Commit + push sur la même branche / PR #22.
Ne merge pas.
Ne tague pas.
Ne bump pas.
Ne relance aucun scan réel dans Work.

Réponse finale courte :
- modifications ;
- limites finales ;
- tests ;
- commit poussé ;
- commande Ubuntu exacte de retest.
~~~

## Réponse exacte

~~~text
Correctif poussé : « : » admis uniquement dans les noms ZIP internes ; chemins filesystem stricts. Gros MANIFEST lu sous borne avec CRC complet, section principale seule utilisée.

Limites finales : **32 768 entrées**, central **4 MiB**, métadonnée **2 MiB**, total **4 MiB**. Protections traversal et ZIP bomb conservées.

Tests Windows : scanner **33 PASS / 24 N/A**, régressions **129 PASS / 87 N/A**. Compileall, release-docs, manifeste et diff-check **PASS**.

Commit : [`46a5260`](https://github.com/MrMekouil/GamePanel/commit/46a52600adea741358a772655465ff5005a0f991), Draft #22.

Retest Ubuntu depuis le checkout :
```
PYTHONPATH="$PWD" /opt/gamepanel/.venvs/d25d52dca517e628/bin/python -m unittest -v tests.test_minecraft_content_032 tests.test_content_classification_032 tests.test_content_admin_032 tests.test_content_store_032 tests.test_content_publication_032 tests.test_content_upgrade_032 tests.test_release_docs
```

**F et Gate 4 NON ACQUIS. Aucun scan réel ni gate suivant exécuté.**
~~~

## Synthèse enregistrée

- `:` admis uniquement dans les noms ZIP internes ; validation des chemins filesystem conservée stricte.
- Gros `MANIFEST.MF` traité sous borne avec CRC complet ; seule la section principale est utilisée.
- Limites finales rapportées : **32 768 entrées**, central **4 MiB**, métadonnée **2 MiB**, total métadonnées **4 MiB**.
- Tests Work Windows : scanner **33 PASS / 24 N/A**, régressions **129 PASS / 87 N/A** ; compileall, release-docs, manifeste et diff-check **PASS**.
- Statut 0.3.2-F : **NON ACQUIS** ; Gate 4 **NON ACQUIS** ; aucun scan réel ni gate suivant exécuté.

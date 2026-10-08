# GP-077 — GPT-6.1 Sol Medium — import AutoModpack v4 hors-ligne

- Date : 2026-10-08
- Quota visible : 91 % → 74 % (**17 points**)
- Durée : **34 min 04 s**
- Résultat : succès
- Commit GamePanel : `084732e7482a55096be0207a515b9a5180461ad6`
- Draft PR : #22

## Prompt exact

~~~text
Dépôt : `MrMekouil/GamePanel`
Branche existante : `work/0.3.2-content-manifests`
PR existante : Draft #22
HEAD attendu : `6f41240010b6157f5d6e95f4be312e1b2ada1b5d`

Utilise l'intégration GitHub connectée, sans clone réseau. Avant modification : vérifier branche, git status, git diff, git diff --cached, git log -10, WORK_STATE.md et les contrats 0.3.2. Préserver tout travail local, aucun reset/revert. STOP en cas de divergence non comprise.

## Mission — Import facultatif AutoModpack

Implémenter dans la page Admin « Contenus client » un import hors-ligne de `automodpack-content.json`, sur le modèle ergonomique de l'import CurseForge existant.

Contexte réel Interstice :

- Forge 47.4.0 / Minecraft 1.20.1.
- 354 JAR observés, révision 10.
- 350 JAR présents dans le manifeste AutoModpack 4.0.5.
- Comparaison réelle SHA-1 + taille : 350 correspondances exactes, 0 manquant.
- 4 JAR serveur hors manifeste : FarmersStructures, AutoModpack, BlueMap, cbcmoreshells.
- Classification actuelle : 0 conflit, 3 suggérés, 17 serveur, 14 client, 234 both, 86 inconnus.
- Issue de migration future : #23.

## Fonctionnement attendu

1. Import Admin explicite d'un fichier local JSON, sans appel réseau ni lecture arbitraire du système de fichiers.
2. Parser borné et strict du format AutoModpack v4 : `automodpackVersion`, `loader`, `loaderVersion`, `mcVersion`, `list[]` avec `file`, `size`, `type`, `sha1`, `murmur`, `editable`, `forceCopy`.
3. Vérifier la compatibilité du manifeste avec la version Minecraft et le loader observés. Rejeter proprement les incohérences, structures dangereuses ou entrées ambiguës. Ne jamais interpréter les chemins du JSON comme des chemins accessibles par le backend.
4. Associer uniquement les JAR admissibles aux artifacts serveur par SHA-1 + taille, sans se fier au seul nom. Prévoir diagnostics et compteurs : total, correspondances, absents du serveur, non référencés dans le manifeste, entrées non prises en charge.
5. Enregistrer une preuve distincte de provenance `automodpack-local` : « distribution client prévue par AutoModpack ». Cette preuve NE DOIT PAS devenir une assertion `environment`, `policy`, `VERIFIED`, `both` ou un droit de redistribution.
6. Préserver intégralement les classifications existantes. Aucun UNKNOWN ne doit changer de classification simplement parce qu'AutoModpack distribue le fichier.
7. Un nouvel import explicite AutoModpack remplace les anciennes preuves AutoModpack, sans toucher aux preuves CurseForge, Modrinth ou JAR. Les scans ordinaires et les imports CurseForge conservent ces preuves pour la même identité path/SHA-256/taille. Aucun héritage sur artifact modifié. Historique SQL intact, réimports idempotents.
8. UI compacte : choix du fichier, import, résumé des correspondances et indication visible « Prévu par AutoModpack » dans les détails des JAR concernés. Préserver les six groupes existants, leurs compteurs et leur fermeture par défaut.
9. Aucune importation d'instructions de suppression depuis `nonModpackFilesToDelete`, aucun téléchargement, copie, suppression ou modification des fichiers Minecraft. Aucune publication implicite ni changement de brouillon. Respecter sécurité, RBAC, CSRF, limites, provenance privée et protections existantes.
10. Tests synthétiques ciblés : parsing, sécurité, associations SHA-1/taille, 350/354 simulés, remplacement A→B, rescan, coexistence CurseForge, non-régression des classifications, absence d'effet sur publication et brouillon, UI/API.

Documenter le comportement, mettre à jour WORK_STATE.md, CHANGELOG et MANIFEST.sha256. Exécuter les tests pertinents, diff-check. Commit + push seulement si propres.

Ne pas changer les versions ni les lots de roadmap. Aucun merge, tag, release, bump ou gate réel. Gate 4 acquis ; F non acquis. Ne pas désinstaller AutoModpack.

Restitution compacte : HEAD, modifications, tests PASS/FAIL/N/A, limites et éventuels points nécessitant validation réelle. Ne pas fournir de commandes de validation serveur ; elles seront préparées séparément.
~~~

## Réponse exacte

~~~text
1. **HEAD poussé** : `084732e7482a55096be0207a515b9a5180461ad6` — PR #22 toujours Draft.
2. **Modifications** : parser AutoModpack v4, import Admin/API hors-ligne, provenance persistée sans effet sur les classifications, formulaire/résumé/badge UI et exception Caddy 4 MiB. Tests, contrats, état, changelog et manifeste actualisés.
3. **Tests** : 316 PASS, 151 N/A natifs, zéro FAIL final. UI/API simulée, syntaxe, manifeste et diff-check PASS. Fichier fourni : 350 entrées acceptées ; simulation 350/354 PASS.
4. **Limites** : Playwright et `caddy validate` N/A, dépendances absentes. Import réel Interstice et Caddy personnalisé à valider séparément.
5. **Statuts** : Gate 4 ACQUIS ; F NON ACQUIS. AutoModpack conservé. Aucun gate réel, merge/tag/release/bump.
~~~

## Synthèse enregistrée

- Import facultatif AutoModpack v4 depuis fichier JSON local : parser strict borné, intégration Admin/API, association par SHA-1 + taille.
- Provenance distincte `automodpack-local` persistée ; aucune modification de classification, policy, VERIFIED ou droit de redistribution.
- Remplacement des preuves AutoModpack lors d’un import explicite ; conservation à l’identique lors d’un rescan ordinaire/import CurseForge, aucune transmission à un nouvel artifact ; historique SQL inchangé.
- UI compacte, résumé, badge « Prévu par AutoModpack » ; six groupes existants conservés.
- Aucun traitement des instructions de suppression, ni téléchargement, copie, publication implicite, ni désinstallation AutoModpack.
- Fichier fourni : **350 entrées acceptées** ; simulation **350/354 PASS**. La correspondance réelle SHA-1 + taille **350/354** décrite dans le prompt est une preuve utilisateur antérieure, **pas un import réel validé lors de ce run**.
- Tests : **316 PASS / 151 N/A natifs / 0 FAIL final** ; UI/API simulée, syntaxe, manifeste et diff-check PASS.
- Playwright et `caddy validate` N/A, dépendances absentes.
- Import réel Interstice et Caddy personnalisé : validation ultérieure requise.
- **Gate 4 ACQUIS ; F NON ACQUIS**.

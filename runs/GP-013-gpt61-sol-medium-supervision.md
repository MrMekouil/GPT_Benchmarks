# GP-013 — GPT-6.1 Sol Medium — Supervision UI

- Date : 2026-10-01
- Quota visible : 100 % → 90 % (**10 points**)
- Durée : **10 min 42 s**
- Résultat : succès
- Commit GamePanel : `622205debaa8492368a7a4f5dc31acafd6a4bf4c`

## Prompt exact

~~~text
Travaille sur le dépôt :

MrMekouil/GamePanel

Branche obligatoire :

work/0.3.1-ui-ux

Draft PR existante :

#19 — 0.3.1 — Refonte UI/UX et finitions d'exploitation

Checkpoint à préserver :

7ba38960fd5420e89c508800ddf201fc29086283
fix: keep registered candidate conflicts visible

PRÉ-VOL OBLIGATOIRE

Avant toute modification :

vérifie la branche courante ;

exécute git status ;

examine git diff ;

examine git log --oneline -10 ;

lis intégralement WORK_STATE.md ;

prends en compte l'état réel de la branche ;

préserve toute modification non commitée ;

ne reset/revert/abort rien avant d'avoir compris l'état réel.

PÉRIMÈTRE

Checkpoint UI/UX limité à :

1. la page Supervision ;

2. un léger ajustement de taille de l'icône SVG Se déconnecter.

Ne touche pas :

aux pages Serveurs / Instances ;

à la poignée de sidebar ;

au branding/palette ;

au backend, endpoints, permissions ou sécurité ;

aux données produites par /admin/health et /admin/diagnostic ;

au contenu ou au format du diagnostic ;

à 0.3.1-E.

Ne merge pas, ne tague pas, ne crée pas de branche.

OBJECTIF

Harmoniser Supervision avec les pages Serveurs / Instances validées et réduire l'espace gaspillé, sans perte d'information ni changement fonctionnel.

Header

Sur la route Supervision :

topbar : Administration ;

supprimer l'eyebrow ADMINISTRATION du contenu ;

conserver H1 Supervision et son sous-titre ;

supprimer le bouton Journal d'audit du header, la route restant accessible dans la sidebar ;

conserver Actualiser et son fonctionnement actuel.

Ne modifie pas les breadcrumbs des autres routes.

Version GamePanel

Compacter fortement le grand panneau actuel.

Conserver au minimum :

GamePanel <version> ;

Mode réel ou Mode simulation locale ;

fallback version Indisponible.

Réduire la longue explication à une courte indication telle que :

Version canonique du backend.

En simulation, conserver explicitement le fait qu'aucun jeu réel n'est contrôlé.

Santé de l'hôte

Conserver toutes les données actuelles.

Sur desktop, viser trois cartes compactes et cohérentes :

CPU et charge ;

Mémoire ;

Disque /.

CPU :

CPU logiques ;

charges 1 / 5 / 15 min.

Mémoire :

utilisé / total ;

pourcentage ;

disponible.

Disque :

utilisé / total ;

libre.

Ne remplace jamais une valeur absente par 0.

Données GamePanel

Le backend compare le filesystem / avec celui du data_dir GamePanel (/var/lib/gamepanel en installation normale) via :

disk.gamepanel_data_same_filesystem_as_root

Ne change pas cette logique backend.

Si cette valeur est true :

ne plus afficher une carte Données GamePanel séparée ;

ajouter dans la carte Disque une petite mention du type :
Données GamePanel : même filesystem.

Si elle est false :

conserver une carte distincte Données GamePanel ;

afficher utilisé / total / libre.

Si l'état est inconnu :

ne déduire aucune égalité ;

conserver un rendu Indisponible cohérent.

Températures

Conserver tous les capteurs et leurs noms EXACTS venant du backend.

Ne renomme/interprète pas acpitz, pch_cannonlake, x86_pkg_temp, etc.

Présenter la température de façon plus compacte :

une carte sous les métriques principales ;

2 colonnes de capteurs sur desktop ;

1 colonne sur mobile ;

aucune perte de capteur ;

pas d'overflow horizontal.

Conserver le fallback Température indisponible.

Diagnostic Administrateur

Conserver intégralement :

copie ;

téléchargement ;

JSON actuel ;

sanitation backend ;

états chargement/erreur.

Compacter seulement la présentation.

Direction :

Diagnostic Administrateur
Rapport global sanitisé pour support et dépannage.

[Copier le diagnostic] [Télécharger le diagnostic]

Puis une petite note :

JSON sanitisé côté backend.

Ne modifie pas copyAdminDiagnostic() ni downloadAdminDiagnostic() sauf nécessité strictement visuelle.

Icône Se déconnecter

Le SVG power ajouté au checkpoint précédent fonctionne mais paraît légèrement plus gros que l'icône Mon compte.

Conserver le SVG inline actuel et son comportement.

Ajuster uniquement son sizing CSS, autour de 1rem × 1rem ou valeur visuellement équivalente.

Conserver :

currentColor ;

aria-hidden="true" ;

focusable="false" ;

data-act="logout" ;

texte Se déconnecter ;

title="Déconnexion".

Ne refais aucune autre icône.

RESPONSIVE

Préserver un rendu correct :

desktop large ;

~1150 px ;

~760 px/mobile.

Attendu :

métriques lisibles sans chevauchement ;

températures 2 colonnes desktop / 1 colonne mobile ;

diagnostic et Actualiser utilisables ;

aucun overflow horizontal.

CRITÈRES D'ACCEPTATION

Le checkpoint doit garantir :

topbar Supervision = Administration ;

plus d'eyebrow Administration ;

plus de raccourci Journal d'audit dans le header ;

Actualiser inchangé fonctionnellement ;

version nettement plus compacte ;

CPU/Mémoire/Disque sans perte de données ;

pas de carte GamePanel séparée si même filesystem ;

carte séparée conservée si filesystem différent ;

état inconnu traité sans supposition ;

températures plus compactes sans perte ni renommage ;

diagnostic compact sans perte fonctionnelle ;

fallbacks chargement/indisponible conservés ;

icône logout visuellement alignée avec Mon compte ;

aucune autre page refaite.

TESTS

Inspecte d'abord les tests existants.

Adapter/compléter les tests directement concernés, notamment :

tests/web-monitoring-026.cjs

tests Web 0.3.1 pertinents ;

tests/test_admin_024.py

tests/test_diagnostic_029.py

tests/test_visual_identity_031.py si nécessaire.

Un nouveau contrat Supervision 0.3.1 est acceptable s'il reste ciblé.

Couvrir au minimum :

mode réel / simulation ;

version disponible / indisponible ;

santé chargement / indisponible ;

CPU/Mémoire/Disque ;

data GamePanel même filesystem / filesystem distinct / état inconnu ;

températures disponibles / indisponibles ;

diagnostic disponible / indisponible ;

Copier / Télécharger ;

topbar Administration ;

absence du bouton Audit dans le header ;

non-régression breadcrumbs Serveurs / Instances ;

SVG logout conservé et sizing ajusté ;

ancien glyphe ⏻ absent.

Exécute les syntaxes JS/CJS et les tests ciblés pertinents.

Ne prétends pas PASS pour ce qui n'a pas été exécuté.
N'installe pas Chromium/Playwright uniquement pour ce checkpoint.

FIN DE CHECKPOINT

Après validation :

mets à jour WORK_STATE.md de façon concise ;

indique que la validation visuelle Ubuntu réelle reste à effectuer ;

régénère réellement MANIFEST.sha256 avec les hashes exacts ;

vérifie absence de undefined et doublons ;

commit sur work/0.3.1-ui-ux ;

push sur la même branche / PR #19 ;

ne merge pas ;

ne tague pas.

CONTRAT DE RESTITUTION WORK

Réponse finale compacte uniquement :

travail effectué ;

fichiers principaux modifiés ;

commit(s) + confirmation du push ;

tests réellement exécutés avec PASS / FAIL / N/A ;

limites ou blocages.

Ne donne aucune commande serveur, runbook, checklist ou étape de validation réelle.
Laisse Assistant Work auditer le résultat et piloter la suite.

Allez hein on va réessayer
~~~

## Réponse exacte

~~~text
Cette fois, c’est fait : Supervision compactée, topbar `Administration`, disques regroupés selon la donnée backend, températures en 2/1 colonnes et diagnostic conservé. SVG logout réduit à `1rem`.

Fichiers principaux : `web/app.js`, `web/style.css`, tests Supervision/navigation, `WORK_STATE.md`, `MANIFEST.sha256`.

Commit **`622205debaa8492368a7a4f5dc31acafd6a4bf4c`** poussé sur la branche existante. PR #19 toujours Draft, sans merge ni tag.

- **PASS** : contrats JS Supervision/Instances/Serveurs.
- **PASS** : 41 tests Python Admin/diagnostic/identité.
- **PASS** : syntaxes JS/CJS, contrôle du périmètre et manifeste **169/169**, sans doublon ni `undefined`.
- **N/A** : tests navigateur et géométrie responsive, Chromium absent.

Validation visuelle Ubuntu réelle non effectuée.
~~~

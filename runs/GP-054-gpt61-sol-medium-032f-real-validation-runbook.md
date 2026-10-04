# GP-054 — GPT-6.1 Sol Medium — 0.3.2-F runbook validation réelle

- Date : 2026-10-04
- Quota visible : 81 % → 64 % (**17 points**)
- Durée : **22 min 13 s**
- Résultat : succès
- Commit GamePanel : `9b4cdb4ae07e6bc0679e0d55e2a642c1436addbb`
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
9c37a5623e71eda0dde077ad15b8eb1314abb09f

OBJECTIF

Préparer uniquement le runbook de validation réelle :

0.3.2-F — validation réelle Interstice + Aero.

A/B/C/D/E global sont acquis.
F n’est pas encore acquis.
Aucune release 0.3.2 n’est encore préparée.

Avant toute modification :
- vérifie branche/status/diff/diff --cached/log ;
- lis WORK_STATE.md ;
- lis ASSISTANT_STATE.md ;
- lis docs/ASSISTANT_WORKFLOW.md ;
- lis docs/CONTENT_MANIFESTS_032.md ;
- lis docs/VALIDATION.md et docs/VALIDATION_0306.md pour reprendre le niveau de prudence des validations réelles précédentes ;
- audite le code exact migration/startup/content/identity/API/installateur nécessaire au runbook ;
- aucun reset/revert/clean ;
- si HEAD ou état inattendu : STOP.

CIBLES RÉELLES CONNUES

Interstice :
- instance id : minecraft-interstice
- Minecraft 1.20.1
- Forge
- root : /home/serveur/minecraft/forge-1.20.1
- service : minecraft.service

Aero :
- instance id : minecraft-aero
- Minecraft 1.21.1
- NeoForge
- root : /home/serveur/minecraft-neoforge-1.21.1
- service : minecraft-neoforge.service

Ces deux instances sont réelles et utiles.

Ne jamais :
- les renommer pour un test ;
- sacrifier/réserver leur ancien id ;
- modifier leurs mods/configs juste pour provoquer une observation ;
- créer volontairement une panne sur leur contenu ;
- démarrer/arrêter un jeu si le test ne l’exige pas.

Une instance minecraft-zombies existe historiquement, mais elle n’est PAS considérée jetable sans confirmation explicite. Ne pas l’utiliser pour rename/recovery.

LIVRABLE

Créer docs/VALIDATION_032.md : runbook réel complet et réversible pour F.

Le document doit être exécutable progressivement par Assistant + utilisateur, mais Work ne doit pas prétendre avoir exécuté cette validation.

Structurer le runbook en gates avec STOP explicites.

1. Pré-vol

- branche/HEAD/worktree propres ;
- état services ;
- version actuelle API ;
- SQLite avant migration ;
- inventaire réel et ids Interstice/Aero ;
- absence de transaction identity/inventory/content pendante ;
- espace disque ;
- état actuel data/content s’il existe.

2. Sauvegarde avant candidate

Prévoir une sauvegarde réelle adaptée au passage schema 4 → 5 et au nouveau content store.

Réutiliser les mécanismes de backup existants du projet.
Ne pas inventer une procédure destructive.
La sauvegarde doit permettre de revenir à l’état avant 0.3.2 si le déploiement échoue.

3. Plan/update candidate

Préparer le contrôle :
- installateur --plan ;
- update candidate depuis la branche actuelle ;
- service GamePanel/Caddy ;
- /api/v1/meta ;
- application reste 0.3.1 pendant la candidate ;
- SQLite doit passer proprement à 5 ;
- comptes/grants/inventaire/qualifications existants conservés ;
- Interstice/Aero toujours liés aux mêmes roots/services ;
- aucune transaction pendante ;
- idempotence du plan après update.

4. Observation réelle Interstice

Via l’UI/API réellement déployée :
- scan minecraft-interstice ;
- confirmer détection Minecraft 1.20.1 / Forge avec version loader réellement observée ;
- comparer l’observation à la bibliothèque réelle sous le root, sans modifier le serveur ;
- contrôler hashes/tailles et nombre d’éléments de façon reproductible ;
- vérifier exclusions mondes/logs/backups/secrets ;
- diagnostics UNKNOWN/CONFLICT honnêtes ;
- aucune publication implicite.

Ne pas exiger que LocalJarProvider connaisse magiquement le côté de tous les mods Forge.

5. Observation réelle Aero

Même gate pour minecraft-aero :
- Minecraft 1.21.1 ;
- NeoForge + version réellement observée ;
- comparaison bibliothèque réelle ;
- hashes/tailles/exclusions/diagnostics ;
- aucune publication implicite.

6. Décisions Admin et draft

Le runbook doit permettre de créer un petit draft de validation contrôlé sur chaque pack sans prétendre classifier arbitrairement tout le modpack.

Important :
- ne jamais attester un droit de redistribution réel sans preuve ;
- UNKNOWN/CONFLICT restent tels quels sauf décision Admin explicitement assumée ;
- ne pas transformer toutes les entrées en both/required par facilité ;
- les entrées réelles dont le droit de redistribution n’est pas établi peuvent rester unavailable ou être omises du draft de validation.

Utiliser des noms de version clairement jetables et non ambigus, par exemple avec préfixe validation-f-, puisque les versions publiées restent réservées même après révocation.

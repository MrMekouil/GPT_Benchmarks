# GP-060 — GPT-6.1 Sol Medium — refonte UI Contenus client

- Date : 2026-10-04
- Quota visible : 70 % → 61 % (**9 points**)
- Durée : **14 min 13 s**
- Résultat : succès
- Commit GamePanel : `735d4dc2081bc760ae82649c55bc5feef45cafdb`
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
3fd61f56b304b725df7e5ff49fabe59b8be3dec3

OBJECTIF UNIQUE

Refondre uniquement l’ergonomie de la page Admin « Contenus client » pour qu’un
vrai modpack Minecraft soit exploitable.

Aucun changement backend, API, SQLite, provider, scanner, classification,
publication ou contrat de sécurité.

F reste NON ACQUIS.
Pas de merge/tag/version bump.

AVANT MODIFICATION

Vérifie :
- branche ;
- git status ;
- git diff ;
- git diff --cached ;
- git log --oneline --decorate -15 ;
- HEAD distant exact.

Lis :
- WORK_STATE.md ;
- ASSISTANT_STATE.md ;
- docs/ASSISTANT_WORKFLOW.md ;
- docs/VALIDATION_032.md.

Audite :
- web/app.js ;
- web/style.css ;
- tests/web-content-032.cjs ;
- tests/web-content-browser-032.cjs ;
- tests/web-content-fixture-032.cjs.

Aucun reset/revert/clean.
STOP si état inattendu.

CONTEXTE RÉEL

Le scan Aero fonctionne maintenant réellement.

Observation réelle :
- révision 2 persistée ;
- SHA-256/tailles visibles ;
- plusieurs mods sont désormais qualifiés par Modrinth ;
- exemples visibles :
  both / VERIFIED / required VERIFIED ;
  both / VERIFIED / recommended SUGGESTED ;
- d’autres restent UNKNOWN ;
- diagnostics possibles :
  LOADER_CONFLICT
  LOCAL_ENVIRONMENT_UNKNOWN
  MODRINTH_LOOKUP_UNKNOWN
  MOD_METADATA_UNKNOWN
  PROVIDER_NOT_FOUND

Le problème courant est l’interface :
chaque mod est rendu sous forme de grosse carte dans Inventaire observé puis à
nouveau comme énorme formulaire dans Brouillon de pack.
Avec un vrai modpack, la page devient extrêmement longue et difficile à utiliser.

DESIGN DEMANDÉ

Regrouper les entrées selon :

record.classification.decisions.environment.value

dans exactement 4 groupes visuels :

1. Serveur uniquement
   valeur : server-only

2. Client uniquement
   valeur : client-only

3. Les deux
   valeur : both

4. Inconnu
   valeur : unknown

Une décision CONFLICT produit actuellement une value unknown :
elle reste donc dans « Inconnu », mais doit conserver visuellement son badge
CONFLICT rouge.

Chaque groupe doit être un accordéon / <details> avec son nombre :

Serveur uniquement          12
Client uniquement            4
Les deux                    37
Inconnu                     18

Le résumé doit rester très compact et lisible.

ORDRE

Dans chaque groupe :
- tri déterministe par path ;
- dans Inconnu, placer les CONFLICT avant les UNKNOWN si simple à faire,
  puis tri par path.

Ne change pas les données ni la classification pour obtenir cet ordre.

INVENTAIRE OBSERVÉ

Remplacer les grosses cartes par des lignes compactes.

Une ligne doit montrer au minimum :

[ nom du fichier ]
Environnement        Politique client        Preuve

Exemple conceptuel :

Create-1.21.1.jar        BOTH        REQUIRED        VERIFIED

Le SHA-256, taille, assertions complètes et provenance restent accessibles dans
un <details> « Preuves / détails ».

Ne supprimer aucune information actuellement disponible.

BROUILLON DE PACK

Utiliser les mêmes 4 groupes.

Chaque mod doit être une ligne compacte contenant au minimum :

[checkbox Inclure]  nom.jar  environnement  politique  preuve  [Réglages]

Le bouton/summary « Réglages » ouvre uniquement pour ce mod les champs avancés
existants :

- environnement override ;
- politique client override ;
- destination ;
- raison Admin ;
- distribution ;
- locator externe ;
- raison redistribution ;
- acceptation unavailable ;
- dépendances ;
- raison revue dépendances.

Les champs avancés ne doivent plus être tous visibles en permanence.

IMPORTANT

- aucune sélection automatique supplémentaire ;
- ne jamais inclure automatiquement un mod parce qu’il est both/required ;
- aucun override implicite ;
- le groupe est déterminé par la classification OBSERVÉE, pas par l’override
  actuellement saisi dans le formulaire ;
- ouvrir/fermer un accordéon ou les Réglages ne doit jamais perdre les valeurs
  non enregistrées du modèle ;
- aucune entrée dupliquée ;
- aucun changement du payload PUT draft ;
- aucun changement des contrôles stale/revision/publish.

ÉTAT DES ACCORDÉONS

Choisir un comportement simple et stable :

Inventaire observé :
- groupes repliés par défaut ;
- Inconnu peut être ouvert par défaut s’il contient des entrées.

Brouillon :
- mêmes groupes ;
- Inconnu ouvert par défaut s’il contient des éléments nécessitant une décision ;
- sinon tout peut rester replié.

Ne stocke pas cet état côté serveur.

DENSITÉ / RESPONSIVE

Desktop :
- lignes compactes ;
- badges courts ;
- éviter les cartes hautes.

Mobile :
- la ligne peut passer sur plusieurs lignes ;
- aucun overflow horizontal ;
- contrôles avancés en une colonne.

Conserver la palette et le style validés de 0.3.1.

TESTS OBLIGATOIRES

Étendre les contrats UI pour vérifier au minimum :

- exactement quatre groupes ;
- compteur correct pour chacun ;
- server-only dans Serveur uniquement ;
- client-only dans Client uniquement ;
- both dans Les deux ;
- unknown dans Inconnu ;
- CONFLICT dans Inconnu avec preuve CONFLICT visible ;
- tri déterministe ;
- aucune entrée dupliquée ;
- Inventaire et Brouillon utilisent le regroupement ;
- les champs avancés sont masqués avant ouverture ;
- ouverture Réglages expose bien les contrôles existants ;
- modifier un champ, fermer/réouvrir les détails conserve la valeur ;
- collectContentForm() produit le même contrat de payload qu’avant ;
- stale/rebase/publish/client-extra inchangés.

Rejouer :

node --check web/app.js

tests/web-content-032.cjs

tests/web-content-browser-032.cjs avec Chromium réel si disponible.

Régressions UI 0.3.1 déjà utilisées pour E3-C si disponibles.

Vérifier responsive :
1440
1150
760
390

Aucun overflow horizontal.

DOCUMENTATION

Mettre à jour uniquement si nécessaire :
- WORK_STATE.md ;
- ASSISTANT_STATE.md ;
- docs/VALIDATION_032.md ;
- docs/CHANGELOG.md ;
- MANIFEST.sha256.

Consigner :
- scan Aero réel révision 2 ;
- qualification Modrinth désormais visible ;
- refonte UI uniquement ;
- quatre groupes environnement ;
- aucun changement backend/classification ;
- F reste NON ACQUIS.

Puis :
- git diff --check ;
- MANIFEST complet ;
- audit diff ;
- commit + push même branche / PR #22.

Ne merge pas.
Ne tague pas.
Ne bump pas.

Réponse finale courte :
- nouvelle organisation UI ;
- tests ;
- commit poussé ;
- commande de retest Ubuntu/Chromium.
~~~

## Réponse exacte

~~~text
- \
  **UI :** quatre accordéons à compteurs dans Inventaire et Brouillon, lignes compactes, CONFLICT rouges prioritaires dans Inconnu. Preuves et réglages individuels repliés ; saisies conservées.
- **Contrats :** aucun changement backend/classification/payload ni sélection automatique.
- **Tests :** syntaxe, contrat VM, sept régressions UI, release-docs/manifeste/diff-check PASS. Chrome réel responsive **1440/1150/760/390 PASS**, sans overflow. Playwright complet **N/A**, dépendance absente.
- **Commit poussé :** [**735d4dc**](https://github.com/MrMekouil/GamePanel/commit/735d4dc2081bc760ae82649c55bc5feef45cafdb), PR #22 toujours Draft. **F NON ACQUIS.**

Retest Ubuntu avec Playwright/Chromium disponibles :
```
node --check web/app.js &&
node tests/web-content-032.cjs &&
node tests/web-content-browser-032.cjs
```
~~~

## Synthèse enregistrée

- UI rapportée : quatre accordéons à compteurs dans Inventaire et Brouillon, lignes compactes, CONFLICT rouges prioritaires dans Inconnu.
- Preuves et réglages individuels repliés ; saisies non enregistrées conservées.
- Aucun changement backend/classification/payload ni sélection automatique.
- Tests : syntaxe, contrat VM, sept régressions UI, release-docs/manifeste/diff-check **PASS**.
- Chrome réel responsive **1440/1150/760/390 PASS**, sans overflow ; Playwright complet **N/A** faute de dépendance.
- Statut : **F NON ACQUIS**.

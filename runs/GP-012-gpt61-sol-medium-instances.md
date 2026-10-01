# GP-012 — GPT-6.1 Sol Medium — Instances UI

- Date : 2026-09-30
- Quota visible : 99 % → 88 % (**11 points**)
- Durée : **18 min 37 s**
- Résultat : succès
- Commit GamePanel : `7ba38960fd5420e89c508800ddf201fc29086283`

## Prompt exact

~~~text
Travaille sur le dépôt :

`MrMekouil/GamePanel`

Branche existante obligatoire :

`work/0.3.1-ui-ux`

Draft PR existante :

#19 — `0.3.1 — Refonte UI/UX et finitions d'exploitation`

Checkpoint actuel à préserver :

`90017e3d6f6b3e12c7e0996c59ff4c91c82f279b`
`style: compact Admin instances catalogue`

## PRÉ-VOL OBLIGATOIRE

Avant toute modification :

- vérifie que tu es bien sur `work/0.3.1-ui-ux` ;
- exécute `git status` ;
- examine `git diff` ;
- examine `git log --oneline -10` ;
- lis intégralement `WORK_STATE.md` ;
- prends en compte l'état réel de la branche et les derniers checkpoints ;
- préserve toute modification non commitée ;
- ne reset/revert/abort rien avant d'avoir compris l'état réel.

## INTERDICTIONS

Travaille UNIQUEMENT sur `work/0.3.1-ui-ux`.

Ne crée aucune nouvelle branche.
Ne merge pas la PR.
Ne tague rien.
Ne commence aucun autre lot.
Ne commence PAS 0.3.1-E.

Ne refais pas la page Instances.
Ne retravaille PAS la page Serveurs.
Ne retravaille PAS la poignée de sidebar.
Ne modifie pas la palette validée.
Ne modifie pas le branding v02.
Ne modifie pas l'accent jaune/or.

Ne modifie aucun endpoint.
Ne modifie aucune règle métier backend.
Ne modifie aucune règle de permissions/capabilities.
Ne modifie aucune qualification.
Ne modifie aucune protection de registration.
Ne modifie aucun contrôle de conflit/stale.
Ne modifie pas le parcours d'ajout manuel 0.3.06.
Ne modifie pas le fonctionnement du scan automatique.

Ne fais aucune retouche esthétique opportuniste hors du périmètre ci-dessous.

## CONTEXTE VALIDÉ

La dernière harmonisation de la page `Instances` est fonctionnelle et va dans la bonne direction.

Sont acquis :

- topbar `Administration` ;
- H1 `Instances` ;
- bouton `Configuration` retiré de la page ;
- `Ajouter une instance` et `Rechercher des serveurs` regroupés ;
- recherche comme action principale ;
- `Candidats détectés` avant les profils ;
- `Profils pris en charge` ;
- cartes de profils compactes ;
- capabilities affichées avec des libellés humains et détail complet accessible ;
- parcours scan / preview / registration inchangés ;
- ajout manuel 0.3.06 inchangé.

La validation réelle montre cependant deux problèmes :

1. les candidats déjà enregistrés occupent énormément de hauteur et repoussent inutilement le reste de la page ;
2. l'icône Unicode du bouton `Se déconnecter` est mal rendue dans Firefox/Windows.

Ce checkpoint doit corriger UNIQUEMENT ces deux sujets.

# OBJECTIF 1 — COMPACTER LES CANDIDATS DÉTECTÉS

## PROBLÈME

Dans l'état réel actuel, le scan retourne plusieurs candidats déjà enregistrés.

Chaque candidat conserve actuellement une grosse carte détaillée contenant :

- identité ;
- unité systemd ;
- raisons de détection ;
- capabilities ;
- qualifications ;
- bouton Prévisualiser désactivé.

Avec 6 candidats déjà enregistrés, la section occupe presque tout l'écran alors qu'aucune action n'est possible sur eux.

Cette présentation n'est pas adaptée.

## PRINCIPE À APPLIQUER

Traiter visuellement différemment les candidats selon leur état existant.

### A. Nouveau candidat actionnable

Condition actuelle :

- `registered === false`
- pas de `conflict`

Il doit rester immédiatement visible.

Conserver :

- nom ;
- profil ;
- unité détectée ;
- raisons utiles ;
- capabilities ;
- qualifications restantes ;
- bouton `Prévisualiser`.

Mais densifier raisonnablement la carte.

Éviter les grandes zones vides actuelles.

Direction possible :

Nom / état en première ligne.

Profil + unité en secondaire.

Raisons sous forme compacte.

Puis :

`Disponibles : État · Événements · Diagnostic · +N`

`À qualifier : Arrêt propre · READY · Compteur joueurs`

puis bouton `Prévisualiser`.

Il n'est pas obligatoire de reproduire littéralement cette maquette :
le but est de réduire nettement la hauteur tout en conservant toutes les informations nécessaires.

### B. Candidat en conflit

Un conflit est important et ne doit PAS être caché dans le groupe des candidats enregistrés.

Conserver les candidats en conflit immédiatement visibles.

Ils doivent rester suffisamment explicites pour comprendre :

- quel serveur a été trouvé ;
- quelle unité est concernée ;
- quel conflit existe ;
- pourquoi la preview/registration est bloquée.

Une densification similaire aux nouveaux candidats est acceptable.

Ne modifier aucune règle de conflit.

### C. Candidat déjà enregistré

Condition actuelle :

`registered === true`

Ce type de candidat ne doit PLUS utiliser une grosse carte détaillée ouverte en permanence.

Regrouper tous les candidats déjà enregistrés dans un bloc repliable natif, par exemple un `<details>`.

Titre directionnel :

`Déjà enregistrés (6)`

Le bloc doit être :

- fermé par défaut ;
- accessible au clavier ;
- sans JavaScript complexe si un `<details>` natif suffit.

À l'intérieur, utiliser des lignes/cartes très compactes.

Direction souhaitée :

`BeamMP Server        BeamMP        beammp.service                 Déjà enregistré`

`Minecraft NeoForge  Minecraft     minecraft-neoforge.service    Déjà enregistré`

etc.

Au minimum chaque ligne doit conserver :

- display_name ;
- profil ;
- unité/service ;
- état `Déjà enregistré`.

Si les raisons/capabilities/qualifications présentes dans la réponse sont jugées utiles à conserver, les rendre consultables dans un détail secondaire sans les afficher systématiquement.

Ne pas supprimer silencieusement des informations qui seraient nécessaires au diagnostic.

Le but reste que l'état normal fermé prenne très peu de place.

# OBJECTIF 2 — RÉSUMÉ DE LA SECTION CANDIDATS

Le badge actuel du type :

`6 candidats`

est peu informatif.

Calculer uniquement à partir des données déjà présentes :

- total détecté ;
- nouveaux/actionnables ;
- déjà enregistrés ;
- conflits.

Exemple lorsque pertinent :

`6 détectés · 0 nouveau · 6 enregistrés`

ou :

`8 détectés · 1 nouveau · 6 enregistrés · 1 conflit`

Gérer correctement singulier/pluriel.

Ne créer aucune donnée backend.

## ÉTAT SANS NOUVEAU CANDIDAT

Si aucun nouveau candidat actionnable et aucun conflit n'existent mais que des candidats déjà enregistrés existent, afficher une information compacte du type :

`Aucun nouveau serveur à ajouter.`

Puis le bloc repliable :

`Déjà enregistrés (6)`

Éviter un grand empty-state en plus de six grosses cartes.

## ÉTAT COMPLÈTEMENT VIDE

Si aucun candidat n'existe du tout, conserver l'état vide déjà validé :

`Aucun nouveau serveur détecté.`

avec l'aide courte concernant :

- la recherche ;
- l'ajout manuel.

Conserver l'information selon laquelle :

- la recherche n'ajoute rien automatiquement ;
- aucun droit utilisateur/opérateur n'est accordé automatiquement.

# OBJECTIF 3 — DENSIFIER LES CARTES ACTIONNABLES

Sans refaire entièrement leur design :

- réduire les marges/paddings trop généreux ;
- éviter une grille 2 colonnes laissant de grandes zones vides ;
- conserver la lecture claire `Disponibles / À qualifier` ;
- conserver le bouton Prévisualiser ;
- garder les états bloqués corrects ;
- préserver le responsive.

À largeur desktop, la hauteur d'un candidat actionnable devrait être sensiblement inférieure à celle des cartes actuelles.

À largeur mobile, repasser proprement sur une seule colonne sans chevauchement.

# OBJECTIF 4 — NE PAS CASSER LES CAS MÉTIER

Préserver STRICTEMENT les règles actuelles.

Pour un candidat :

- `registered` continue de venir du backend ;
- `conflict` continue de venir du backend ;
- le bouton Preview reste désactivé exactement dans les mêmes cas ;
- les reasons restent celles du backend ;
- les capabilities disponibles restent celles du backend ;
- les qualifications restantes restent celles du backend ;
- aucun candidat bloqué ne devient enregistrable ;
- aucun candidat nouveau n'est enregistré automatiquement.

Ne modifier :

- ni `previewCandidate()` ;
- ni l'endpoint de preview ;
- ni l'endpoint de registration ;
- ni la détection ;
- ni les règles de conflit ;
- ni les protections de stale state.

L'objectif est exclusivement la présentation.

# OBJECTIF 5 — CORRIGER L'ICÔNE `SE DÉCONNECTER`

## PROBLÈME

Le bouton de sidebar utilise actuellement un caractère Unicode :

`⏻`

Dans Firefox sous Windows, ce caractère est mal rendu et apparaît comme un glyphe cassé/incorrect.

## CORRECTION

Remplacer UNIQUEMENT l'icône du bouton `Se déconnecter` par une petite icône SVG inline fiable.

Contraintes :

- SVG inline ;
- pas de fichier externe supplémentaire si inutile ;
- pas de bibliothèque d'icônes ;
- pas de dépendance ;
- utiliser `currentColor` pour suivre naturellement la couleur du bouton ;
- taille cohérente avec les autres icônes de sidebar ;
- `aria-hidden="true"` ;
- ne pas dupliquer le texte accessible ;
- conserver le texte `Se déconnecter` ;
- conserver `title="Déconnexion"` ;
- conserver l'action `logout` actuelle ;
- aucun changement fonctionnel du logout.

Utiliser une forme standard et simple de type symbole power/logout.

Le SVG doit rester net dans Firefox/Chrome et sous Windows/Linux.

## NE PAS REFAIRE LES AUTRES ICÔNES

Même si d'autres icônes Unicode existent dans la navigation :

- ne les remplace pas dans ce checkpoint ;
- ne crée pas un nouveau système global d'icônes ;
- ne transforme pas ce correctif en refonte de navigation.

Corriger uniquement le glyphe actuellement visiblement cassé de `Se déconnecter`.

# OBJECTIF VISUEL GLOBAL

Après correction, une page avec 6 candidats déjà enregistrés doit permettre de voir très rapidement :

- `Candidats détectés`
- un résumé indiquant qu'il n'y a rien de nouveau ;
- un petit bloc `Déjà enregistrés (6)` fermé ;
- puis presque immédiatement `Profils pris en charge`.

Un candidat réellement nouveau ou en conflit doit au contraire attirer l'attention et rester visible sans ouvrir le bloc des enregistrés.

# RESPONSIVE

Vérifier :

- desktop large ;
- breakpoint intermédiaire autour de 1150 px ;
- mobile autour de 760 px.

Le bloc des candidats enregistrés doit rester lisible en mobile.

Les lignes compactes peuvent passer sur plusieurs lignes si nécessaire.

Ne pas forcer un tableau horizontal qui provoquerait du scroll inutile.

# CRITÈRES D'ACCEPTATION

Le checkpoint est acceptable si :

1. les candidats `registered === true` ne produisent plus de grosses cartes ouvertes ;
2. ils sont regroupés dans un bloc compact repliable fermé par défaut ;
3. les candidats nouveaux restent immédiatement visibles ;
4. les candidats en conflit restent immédiatement visibles ;
5. le compteur distingue au minimum détectés / nouveaux / enregistrés, et les conflits lorsqu'ils existent ;
6. lorsqu'il n'y a aucun nouveau candidat, `Aucun nouveau serveur à ajouter.` est clairement visible ;
7. les informations essentielles des candidats enregistrés restent consultables ;
8. les candidats nouveaux/conflits sont plus compacts sans perdre d'information utile ;
9. Preview reste désactivé exactement dans les mêmes cas ;
10. aucune logique de scan/preview/register n'est modifiée ;
11. le parcours manuel 0.3.06 n'est pas modifié ;
12. le profil catalogue n'est pas retravaillé ;
13. le bouton `Se déconnecter` n'utilise plus le glyphe Unicode cassé ;
14. l'icône logout est un SVG inline fiable utilisant `currentColor` ;
15. l'action/logout/accessibilité restent inchangés ;
16. aucune autre icône de navigation n'est refondue ;
17. aucune autre page n'est modifiée visuellement sauf l'icône logout globale.

# TESTS

Inspecte les tests existants avant d'en ajouter.

Adapter/compléter en priorité :

- `tests/web-instance-density-031.cjs`
- `tests/web-instances-030.cjs`
- les tests UI/navigation directement concernés par l'icône logout uniquement si nécessaire.

Vérifier contractuellement au minimum :

- 0 candidat ;
- uniquement des candidats enregistrés ;
- un nouveau candidat ;
- plusieurs nouveaux candidats ;
- candidat en conflit ;
- mélange nouveau + enregistré + conflit ;
- compteurs corrects ;
- bloc `Déjà enregistrés` fermé par défaut ;
- présence des identités/service des candidats enregistrés ;
- absence de bouton Preview actif sur les candidats déjà enregistrés ;
- Preview disponible sur un candidat nouveau ;
- candidat en conflit toujours visible hors du bloc enregistré ;
- syntaxe JS ;
- SVG logout présent ;
- ancien caractère Unicode `⏻` absent du bouton logout ;
- texte `Se déconnecter` conservé ;
- action `data-act="logout"` conservée.

Exécuter également les non-régressions directement pertinentes sur :

- Instances ;
- ajout manuel ;
- navigation/sidebar ;
- Serveurs si le shell partagé est modifié.

Ne prétends pas PASS pour un test non exécuté.

N'installe pas Chromium/Playwright ou une dépendance lourde uniquement pour ce checkpoint si l'environnement n'en dispose pas déjà.

# WORK_STATE

Après implémentation et tests :

- mets à jour `WORK_STATE.md` ;
- décris ce mini-checkpoint de manière concise ;
- indique que la validation visuelle Ubuntu réelle reste à effectuer ;
- ne réécris pas l'historique inutilement.

# MANIFESTE

Pour tous les fichiers suivis modifiés :

- régénère réellement `MANIFEST.sha256` ;
- calcule les SHA-256 exacts des fichiers actuels ;
- aucun `undefined` ;
- aucun doublon ;
- ne recycle pas d'anciens hashes ;
- vérifie réellement le manifeste avant commit.

# COMMIT / PUSH

Une fois le checkpoint cohérent et testé :

- commit sur `work/0.3.1-ui-ux` ;
- utilise un message clair et borné ;
- push sur la même branche ;
- conserve la Draft PR #19 ;
- ne merge pas ;
- ne tague rien.

# CONTRAT DE RESTITUTION WORK

Dans ta réponse finale :

- reste compact ;
- indique le travail effectué ;
- indique les fichiers principaux modifiés ;
- indique le SHA du commit et confirme le push ;
- liste uniquement les tests réellement exécutés avec PASS / FAIL / N/A ;
- indique les limites ou éléments non testés ;
- signale tout blocage concret ;
- ne fournis aucune commande de validation réelle ;
- ne fournis aucune procédure serveur ;
- ne fournis aucun runbook ;
- ne fournis aucune checklist utilisateur ;
- ne propose pas les étapes suivantes ;
- ne recopie pas un éventuel fichier de validation ;
- laisse Assistant Work auditer le checkpoint et piloter la validation réelle suivante.
~~~

## Réponse exacte

~~~text
Le pré-vol a révélé que `76fc264` contenait déjà la densification et le SVG logout. J’ai préservé ce travail et corrigé le cas **enregistré + conflit**, désormais visible hors du bloc replié, avec Preview désactivé.

Fichiers modifiés : `web/app.js`, les deux tests Instances, `WORK_STATE.md` et `MANIFEST.sha256`.

Commit **`7ba38960fd5420e89c508800ddf201fc29086283`** poussé sur `work/0.3.1-ui-ux`. PR #19 conservée en Draft, sans merge ni tag.

- **PASS** : contrats JS Instances/Serveurs, syntaxe JS/CJS, contrôle du périmètre, release-docs et diff.
- **FAIL à l’import** : tests Python instances/manuel/profils/version — `aiohttp` et `pydantic` absents.
- **N/A** : parcours navigateur et responsive 1440/1150/760 px — Playwright absent.

Hashes modifiés recalculés et vérifiés, sans doublon ni `undefined`. Contrôle global limité à **167/168 entrées** : le PNG glossy inchangé n’a pas pu être récupéré.

Validation visuelle Ubuntu réelle non effectuée.
~~~

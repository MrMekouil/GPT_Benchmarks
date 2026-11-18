# GP-099 — GPT-6.2 Sol Medium — GamePanel 0.3.7 CP20 ergonomie

- **Date d'enregistrement :** 2026-11-18 ; date de l'exécution Work non précisée
- **Modèle et effort :** GPT-6.2 Sol / Medium
- **Quota visible :** 21 % → 7 % = **14 points**
- **Durée observée :** 10 min 08 s = **608 secondes**
- **Livraison :** correctif ergonomique CP20 committé, **validation visuelle du pilote en attente**
- **Projet source :** `MrMekouil/GamePanel`, branche `work/0.3.7-content-comparison`
- **Commit source confirmé :** [`eeed6093f2c09076ab3192788e19284a0139e59d`](https://github.com/MrMekouil/GamePanel/commit/eeed6093f2c09076ab3192788e19284a0139e59d)

## Prompt exact

~~~text
# GamePanel 0.3.7 — Finalisation ergonomique de CP20

## Références

- Dépôt : `MrMekouil/GamePanel`
- Branche existante : `work/0.3.7-content-comparison`
- HEAD attendu : `08007fc2598d36017a40c7d60279fe6d166e8dd8`, à vérifier.
- Checkout utilisateur : `F:\GamePanel-037`
- Profil Windows isolé existant : à préserver intégralement.

**Mission unique : corriger les défauts ergonomiques constatés pendant la validation réelle de CP20. Ne pas commencer CP21.**

## Retour du pilote

L'Accueil et la page Serveurs conviennent.

La page « Mes jeux » n'est pas acceptée :

- Parcours peu compréhensible et sous-menus inutiles.
- Barre de recherche dont le rôle n'est pas évident.
- Sélecteur « Afficher » affichant notamment des représentations techniques `LibrarySection {...}`.
- Entrées génériques « Minecraft / Java — Partiel » sans rôle identifiable.
- Instances Minecraft insuffisamment visibles directement.
- Case « Afficher les autres jeux Steam » qui semble ne rien ajouter, cause non établie.

Dans la fiche serveur Minecraft, « Changer la source » impose de rechercher les instances avant de proposer un choix, même lorsque des instances sont déjà connues.

## Objectifs impératifs

**1. Refaire « Mes jeux » comme une véritable bibliothèque lisible.**

Afficher les jeux, installations et profils connus directement, regroupés de manière naturelle. Montrer les noms réels, lanceurs et versions lorsqu'ils sont disponibles. Ne pas inventer de qualification ni transformer des observations partielles en installations confirmées.

Éviter les pages intermédiaires inutiles. Garder l'accès aux contenus détaillés et aux fonctions avancées.

**2. Supprimer le sélecteur de catégories obligatoire.**

La page ne doit plus exiger de choisir « Installations », « Lanceurs », etc. pour comprendre ce qui existe. Regrouper directement les éléments et proposer des filtres facultatifs uniquement lorsque c'est utile.

Aucun objet C# ou libellé technique brut ne doit apparaître dans l'interface.

**3. Clarifier la recherche.**

Distinguer clairement filtrage de la bibliothèque, recherche ciblée d'installations et analyse approfondie.

Afficher immédiatement les observations mémorisées. Permettre la découverte légère des métadonnées locales connues, sans hachage massif, lecture automatique des JAR ni analyse coûteuse implicite.

**4. Simplifier le changement de source Minecraft.**

Afficher directement les instances connues dans le sélecteur de la fiche serveur. Prévoir une recherche complémentaire facultative.

Conserver le choix explicite, les préférences revalidées, les identités physiques, les contrôles de preuve et les restrictions de lecture seule.

**5. Vérifier le comportement des autres jeux Steam.**

Déterminer si la case actuelle ne fait qu'afficher les résultats d'une découverte préexistante ou s'il existe un défaut. Corriger un problème démontré, sans étendre artificiellement la prise en charge fonctionnelle de Steam. Rendre l'état « non recherché » compréhensible.

**6. Finaliser l'ergonomie.**

Vérifier navigation directe, clavier, scroll, longues listes, fenêtres compactes et 125 % de mise à l'échelle.

Conserver les performances et la virtualisation acquises au cours de CP20.

## Validation et livraison

Prévol Git complet et conservation des travaux.

Tests ciblés et WPF locaux, sans GitHub Actions. Mettre à jour les tests pour les nouveaux parcours sans supprimer les vérifications existantes ni contourner les gardes de sécurité.

Documenter précisément PASS, FAIL et SKIP, et distinguer validation synthétique et essai réel sur Windows.

Mettre à jour les états de continuité, le contrat CP20 et le manifeste, puis committer sur la branche existante.

Livrer une unique commande PowerShell de validation Windows isolée, courte, avec balises de résultat et conservation des erreurs détaillées.

Aucun nouveau CP, branche, PR, merge, tag, release ou modification du client stable.

**CP20 restera ouvert jusqu'à validation visuelle du pilote.**

Ne pas modifier les règles de fraîcheur et de couverture Minecraft Aero : le problème « Historique périmé / Scan partiel » est réservé à CP21.
~~~

## Réponse exacte

~~~text
Correctif ergonomique CP20 committé sur `work/0.3.7-content-comparison`. HEAD distant vérifié [`eeed6093f2c09076ab3192788e19284a0139e59d`](https://github.com/MrMekouil/GamePanel/commit/eeed6093f2c09076ab3192788e19284a0139e59d).

- **Mes jeux** affiche directement les installations et profils connus par jeu, avec leurs noms réels et les lanceurs et versions disponibles. Les contenus restent regroupés dans une liste virtualisée, et les observations partielles gardent leur statut. Le filtre de la bibliothèque, la recherche d’installations et l’analyse des contenus ont chacun leur commande.
- **Steam** distingue désormais un catalogue jamais recherché d’un relevé vide ou partiel. La case affiche les autres jeux déjà relevés. Une action dédiée lance la recherche Steam existante.
- **Minecraft** propose les instances issues des métadonnées des lanceurs dès l’ouverture du sélecteur. Une recherche complémentaire reste disponible. L’admission exige toujours un choix explicite ou une préférence revalidée, avec les contrôles d’identité et de preuve existants.

**Validation Linux** — trois compilations PASS, dont les deux bancs WPF. Tests ciblés **15 PASS / 1 FAIL / 8 SKIP**. Le FAIL de la fixture d’identité physique Windows a été reproduit au HEAD de départ. L’exécution native WPF et le rendu réel à 125 % restent **NON TESTÉS**. Les états de reprise, le contrat CP20 et le manifeste SHA-256 ont été mis à jour.

**CP20 reste ouvert** jusqu’à ta validation visuelle sur le profil isolé. Vérifie surtout l’accès direct aux instances nommées, la distinction des trois actions dans « Mes jeux », l’état Steam avant et après recherche, puis « Changer la source » sur Minecraft. À 125 %, vérifie au clavier et au défilement que la liste reste accessible en petite fenêtre.

### A EXECUTER

Une fois `F:\GamePanel-037` synchronisé sur le commit ci-dessus, cette commande lance les tests portables CP20 et les deux bancs WPF sur fixtures. Elle conserve le journal complet dans `%TEMP%`.
```
& {
    $ErrorActionPreference = 'Stop'
    $log = Join-Path $env:TEMP ("GamePanel-CP20-{0:yyyyMMdd-HHmmss}.log" -f (Get-Date))
    '===== DEBUT A ME COLLER ====='
    try {
        Set-Location 'F:\GamePanel-037'
        $head = git rev-parse HEAD
        if ($LASTEXITCODE -ne 0 -or $head -ne 'eeed6093f2c09076ab3192788e19284a0139e59d') {
            throw "HEAD inattendu : $head"
        }
        "HEAD=$head"
        foreach ($step in ([ordered]@{
            CP20 = @('run','--project','tests/windows','-c','Release','--','CP20')
            DECOUVERTE = @('run','--project','tests/windows-discovery-ui','-c','Release')
            PREPARATION = @('run','--project','tests/windows-wpf','-c','Release','-p:GamePanelDevelopmentIsolation=true')
        }).GetEnumerator()) {
            $argsDotnet = $step.Value
            & cmd.exe /d /c "dotnet $($argsDotnet -join ' ') >> `"$log`" 2>&1"
            if ($LASTEXITCODE -ne 0) { throw "$($step.Key) FAIL (code $LASTEXITCODE)" }
            "$($step.Key)=PASS"
        }
    } catch {
        "FAIL | $($_.Exception.Message)"
        if (Test-Path $log) { Get-Content $log -Tail 8 }
    } finally {
        if (Test-Path $log) { "LOG=$log" }
        '===== FIN A ME COLLER ====='
    }
}
```

A ME COLLER : uniquement le texte entre ces deux marqueurs (marqueurs inclus)
~~~

## Synthèse enregistrée

Le commit GitHub source **`eeed6093f2c09076ab3192788e19284a0139e59d`** est vérifié ; il comporte **18 fichiers modifiés**, concernant les pages WPF, la découverte locale, les tests, la documentation CP20, le manifeste et les états de reprise.

- **Périmètre livré selon Work :** la page « Mes jeux » expose directement les installations et profils connus, avec leurs identités réelles et observations partielles non surqualifiées. Recherche de la bibliothèque, découverte d'installations et analyse de contenus sont séparées. L'état Steam `non recherché` est distinct d'un résultat vide/partiel, et la recherche Steam reste explicite. « Changer la source » Minecraft affiche immédiatement les instances connues tout en préservant choix explicite, préférences revalidées et gardes d'identité.
- **Validation annoncée par Work (Linux) :** **trois compilations PASS**, dont les deux bancs WPF ; tests ciblés **15 PASS, 1 FAIL, 8 SKIP**. Le **FAIL** de fixture d'identité physique Windows aurait été reproduit au HEAD de départ ; il demeure compté comme **FAIL**, pas requalifié comme PASS. Ces tests n'ont pas été rejoués indépendamment pour le benchmark.
- **Validation réelle non acquise :** rendu WPF natif et ergonomie à **125 % non testés** après correction. **CP20 reste ouvert** jusqu'à validation visuelle sur le profil Windows isolé.
- **Livraison utilisateur :** la réponse complète préserve la commande PowerShell unique avec balises de résultats, contrôle strict du HEAD et journal en `%TEMP%`.
- **Périmètre préservé :** pas de CP21, pas d'altération des règles de fraîcheur/couverture Minecraft Aero selon le mandat. Aucune GitHub Actions exécutée par ce benchmark ; les autres interdictions sont rapportées par Work, sans audit autonome exhaustif.

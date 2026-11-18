# GP-097 — GPT-6.2 Sol Medium — GamePanel 0.3.7 CP20 responsive « Mes jeux »

- **Date d'enregistrement du benchmark :** 2026-11-18 ; date exacte de la session Work non fournie
- **Modèle / effort :** GPT-6.2 Sol / Medium
- **Quota visible :** 47 % → 40 % = **7 points**
- **Durée observée :** **4 min 23 s (263 secondes)**
- **Projet :** `MrMekouil/GamePanel`, branche `work/0.3.7-content-comparison`
- **Statut :** correction de disposition livrée et commit vérifié ; validation WPF native Windows **EN ATTENTE**
- **Commit source confirmé :** [`5dcfa5b68975eeddf3ce50bdce6f00514263a344`](https://github.com/MrMekouil/GamePanel/commit/5dcfa5b68975eeddf3ce50bdce6f00514263a344)

## Prompt exact

~~~text
# GamePanel 0.3.7 — CP20 : correction responsive de « Mes jeux »

Dépôt : `MrMekouil/GamePanel`

Branche : `work/0.3.7-content-comparison`

HEAD attendu : `bf620e4c1c4b809a1d34f155a9801d99b23e360d`

## Résultat natif Windows confirmé

Le banc WPF Découverte rapporte :

- R2 : 22/22 PASS.
- R3 : 1/15 avant interruption.
- Fenêtre : 640 × 560 DIP.
- Transformation : 125 %.
- Page : 499,2 × 416,8 DIP.
- `ContentRows.ActualHeight` : **27,6 DIP**, minimum exigé : **50 DIP**.
- Aucun problème horizontal : ExtentWidth 262,3, ViewportWidth 456,2, défilement horizontal désactivé.

**Défaut identifié : espace vertical insuffisant pour la liste de contenus dans la fiche Assetto Corsa de « Mes jeux ».**

## Mission

1. Prévol Git, préserver les travaux existants.
2. Examiner `InstalledGamesPage.xaml`, son code associé et le scénario WPF Découverte.
3. Identifier les éléments qui consomment la hauteur, notamment l'état des panneaux « Sources et outils » et « Filtres » après navigation.
4. Corriger réellement la disposition pour que la liste conserve une hauteur utilisable à 640 × 560 et 125 %, y compris avec les panneaux autorisés ouverts.
5. Privilégier une interface compacte et responsive : éviter les commandes redondantes, organiser les éléments facultatifs et préserver l'accès aux fonctions existantes.
6. Conserver la virtualisation, le clavier, les informations techniques et les possibilités de défilement.
7. Ne pas réduire le seuil de 50 DIP, supprimer le test ou masquer des fonctionnalités pour obtenir PASS.
8. Vérifier les dispositions à 100 % et 125 %, en fenêtres petite et grande, dans les environnements disponibles.
9. Documenter précisément les validations non exécutables sur Linux.
10. Mettre à jour le manifeste et les états de reprise, puis committer sur la branche existante.

**Ne pas commencer CP21.**

Aucun GitHub Actions, nouveau CP, nouvelle branche, PR, merge ou release.

Livrer la correction complète avec une unique commande Windows permettant de relancer le banc WPF Découverte.
~~~

## Réponse exacte

~~~text
La disposition de **Mes jeux** est corrigée. La liste ne mesurait que **27,6 DIP** parce que les commandes, la recherche et l’en-tête de la fiche prenaient leur hauteur avant que WPF alloue l’espace restant à la liste. Ces éléments sont désormais dans un en-tête défilable, plafonné à 60 % de la hauteur disponible. La liste conserve son propre défilement et sa virtualisation. [Commit 5dcfa5b](https://github.com/MrMekouil/GamePanel/commit/5dcfa5b68975eeddf3ce50bdce6f00514263a344)

Le banc conserve le seuil de **plus de 50 DIP** et vérifie les fenêtres **640 × 560** et **1180 × 820** à **100 %** et **125 %**, panneaux ouverts et repliés. La compilation croisée WPF passe. Sur Linux, le filtre CP20 donne **4 PASS, 0 FAIL, 1 SKIP**. Les mesures de disposition, le clavier et la virtualisation WPF restent **NON TESTÉS en natif** après correction.

### A EXECUTER

Après avoir synchronisé `F:\GamePanel-037` sur `5dcfa5b`, rejoue uniquement le banc Découverte.
```
Set-Location 'F:\GamePanel-037'
$result = & dotnet run --project tests/windows-discovery-ui -c Release 2>&1
$exitCode = $LASTEXITCODE
'===== DEBUT A ME COLLER ====='
"HEAD=$(git rev-parse --short HEAD) | WPF_DECOUVERTE_EXIT=$exitCode"
$result | Select-Object -Last 12 | ForEach-Object { $_.ToString() }
'===== FIN A ME COLLER ====='
```

A ME COLLER : uniquement le texte entre ces deux marqueurs (marqueurs inclus).
~~~

## Synthèse enregistrée

- Le commit GitHub confirme **six fichiers modifiés** : `windows/InstalledGamesPage.xaml`, `windows/InstalledGamesPage.xaml.cs`, `tests/windows-discovery-ui/Program.cs`, `WORK_STATE.md`, `ASSISTANT_STATE.md`, `MANIFEST.sha256`.
- **Diagnostic Windows avant correction :** R2 **22/22 PASS** ; R3 interrompu après **1/15** ; fenêtre **640 × 560 DIP** à **125 %**, `ContentRows.ActualHeight = 27,6 DIP` pour un seuil exigé de **50 DIP**. Aucun défaut horizontal constaté.
- **Correctif selon Work :** en-tête défilable, plafonné à **60 %** de la hauteur, préservant le défilement indépendant et la virtualisation de la liste. Le seuil du banc est conservé ; configurations prévues : **640 × 560** et **1180 × 820**, à **100 % et 125 %**, panneaux repliés et ouverts.
- **Validations rapportées par Work :** compilation croisée WPF **PASS** ; filtre Linux CP20 **4 PASS, 0 FAIL, 1 SKIP**. Non rejouées indépendamment lors de l'enregistrement du benchmark.
- **Réserve majeure :** mesure de hauteur après correctif, navigation clavier et virtualisation WPF **non validées nativement sur Windows**. Le succès concerne la **livraison du correctif** et ne signifie pas PASS natif du banc R3. Une commande PowerShell Windows est conservée verbatim dans la réponse.
- **Périmètre :** arrêt après CP20, sans CP21. Aucune GitHub Actions exécutée dans le cadre de l'enregistrement du benchmark ; le travail source affirme également n'en avoir lancé aucune.

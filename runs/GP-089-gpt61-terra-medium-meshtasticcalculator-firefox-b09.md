# GP-089 — GPT-6.1 Terra Medium — MeshtasticCalculator V02-02 Firefox B09

- Date d'enregistrement : 2026-10-29 (date exacte d'exécution non transmise)
- Quota visible : 54 % → 50 % = **4 points**
- Durée : **3 min 28 s**
- Statut : correction livrée ; validation réelle Firefox sur le nouveau commit **NON EXÉCUTÉE**
- Commit : `4bd2b88464c4ec11367499ef61412fac3c08de3c`

## Prompt exact

~~~text
# MeshtasticCalculator — V02-02 : correction du test Firefox B09

**Dépôt :** `MrMekouil/MeshtasticCalculator`
**Branche :** `work/v0.2`
**HEAD attendu :** `c43a2361cac74bd3d482ba87708c45a97099e0ac`

Le test Firefox automatisé vient d'être exécuté sur Windows 10 avec Firefox 158.0.

**Résultat réel :**

- B01 à B08 : PASS.
- B09 : FAIL, assertion ligne 104 de `tests/firefox/probe.js`.
- Aucune erreur JavaScript produit signalée.

**Cause identifiée :** B09 écoute les clics depuis `document`, alors que la fonction `save()` crée une ancre de téléchargement détachée du DOM. Le test ne capture donc pas son clic.

## Mission

1. Vérifier le HEAD et les éventuels changements préexistants.
2. Corriger uniquement l'instrumentation B09 afin d'intercepter le vrai clic sur l'ancre temporaire, récupérer le Blob JSON et vérifier le nom du fichier.
3. Restaurer systématiquement toute interception temporaire après le test.
4. Conserver la vérification complète d'export, création d'un nouveau projet, import et restauration des données.
5. Vérifier que les tests B01 à B08 restent inchangés et que les tests Node existants passent.
6. Tenter le test Firefox réel si l'environnement le permet ; sinon indiquer NON EXÉCUTÉ sans prétendre au PASS.
7. Commit/push sur `work/v0.2` uniquement, puis transmettre SHA, diff et résultats.

**Interdictions :** aucun changement dans `web/`, aucun modèle RF modifié, aucune nouvelle branche, PR, CI, merge ou release.

Ne pas démarrer V02-03. V02-02 reste en attente de validation utilisateur.
~~~

## Réponse exacte

~~~text
**Correction B09 livrée** sur `work/v0.2` : [`4bd2b88464c4ec11367499ef61412fac3c08de3c`](https://github.com/MrMekouil/MeshtasticCalculator/commit/4bd2b88464c4ec11367499ef61412fac3c08de3c).

Le seul fichier modifié est `tests/firefox/probe.js`. B09 intercepte désormais le clic de l’ancre détachée, récupère le Blob, vérifie le nom `meshtasticcalculator-projet.json` et restaure la méthode d’origine avec `finally`. La vérification d’export, de nouveau projet et de réouverture est conservée.

- **B01 à B08 :** code inchangé, vérifié par comparaison avec le commit précédent.
- **Syntaxe :** PASS.
- **Suite Node :** PASS, 51/51.
- **Firefox sur ce nouveau commit : NON EXÉCUTÉ jusqu’au résultat.** La tentative a expiré après 180 secondes, sans requête HTTP reçue. Les PASS B01–B08 et le FAIL B09 rapportés par l’utilisateur concernent le commit précédent.

Le prochain geste est de relancer le test Firefox sur le nouveau SHA, puis de transmettre son rapport au pilote. **V02-02 reste en attente de validation utilisateur ; V02-03 n’a pas été démarré.**
~~~

## Observations structurées

- Succès de livraison de correctif dans `tests/firefox/probe.js` uniquement, vérifié par commit GitHub.
- Node : 51/51 PASS ; syntaxe : PASS ; navigateur Firefox nouveau SHA : NON EXÉCUTÉ.
- Ancien Firefox : B01–B08 PASS / B09 FAIL sur précédent SHA, non transposable au nouveau.
- Validation utilisateur V02-02 toujours NON ACQUISE ; V02-03 non démarré.

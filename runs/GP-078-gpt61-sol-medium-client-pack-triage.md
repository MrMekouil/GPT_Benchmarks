# GP-078 — GPT-6.1 Sol Medium — assistance au tri du pack client

- Date : 2026-10-08
- Quota visible : 100 % → 88 % (**12 points**)
- Durée : **21 min 45 s**
- Résultat : succès
- Commit GamePanel : `4e00bfce3b514c4b4c91c1d6099e59780a18f67e`
- Draft PR : #22

## Prompt exact

~~~text
Repo : `MrMekouil/GamePanel`
Branche : `work/0.3.2-content-manifests`
PR : Draft #22
HEAD attendu : `084732e7482a55096be0207a515b9a5180461ad6`

Utilise l'intégration GitHub connectée, sans clone réseau.

Avant modification : vérifier branche, git status, git diff, git diff --cached, git log -10, WORK_STATE.md, contrats du brouillon 0.3.2 et UI existante. Préserver tout travail local. Aucun reset/revert.

## Mission — Assistance au tri du pack client

Développer une aide au tri dans « Contenus client », à partir des classifications existantes et de la provenance AutoModpack, sans créer de nouvelle source de vérité.

**État réel Interstice validé :**

- Forge 47.4.0 / MC 1.20.1.
- Observation révision 11 : 354 JAR.
- AutoModpack : 350 correspondances exactes SHA-1 + taille, 4 JAR non référencés.
- 0 CONFLICT, 3 SUGGESTED, 17 server-only, 14 client-only, 234 both, 86 UNKNOWN.
- 15 server-only figurent dans la distribution prévue AutoModpack.
- Aucun brouillon enregistré ni publication constatée.

## Fonctionnement

Ajouter une section compacte **« Assistance au tri client »** avec des propositions explicables :

- **Inclusion recommandée** : environnement compatible client VERIFIED et politique client `required` ou `recommended` établie par une preuve suffisamment fiable, sans contradiction.
- **Exclusion recommandée** : environnement `server-only / VERIFIED` ou politique `excluded / VERIFIED`.
- **Optionnels / candidats à examiner** : mods potentiellement utilisables côté client mais sans obligation démontrée, ou explicitement optionnels.
- **Décision nécessaire** : UNKNOWN, CONFLICT, SUGGESTED, informations contradictoires ou insuffisantes.

Ne jamais confondre `both / VERIFIED` avec une obligation client VERIFIED. La présence dans AutoModpack apporte seulement « distribution prévue », pas une exigence client. Une politique UNKNOWN ne doit pas devenir `required` par heuristique.

Afficher les compteurs de chaque catégorie et les justifications consultables. Mettre particulièrement en évidence :

- les 86 UNKNOWN ;
- les 15 server-only qu'AutoModpack prévoyait de distribuer ;
- les 4 JAR serveur hors manifeste ;
- les candidats dont la politique client reste inconnue.

**Préparation du brouillon :**

- Le tri est d'abord une proposition, sans mutation.
- Ajouter une action Admin explicite pour appliquer uniquement les sélections suffisamment justifiées au formulaire local.
- Ne jamais sauvegarder automatiquement le brouillon, publier, fabriquer des overrides, affirmer une licence ou choisir automatiquement un mode de redistribution.
- Préserver les choix manuels existants, les raisons Admin, les destinations et les éventuelles décisions déjà enregistrées. Ne pas écraser un brouillon existant ou stale.
- Les actions par lot doivent indiquer précisément les fichiers concernés et permettre une revue avant enregistrement.
- Garder les validations serveur comme autorité finale. Une sélection ne vaut pas autorisation de publication.

**UI :**

- Rester compacte, cohérente avec l'UI 0.3.1.
- Conserver les six groupes actuels, leurs compteurs et leur fermeture par défaut.
- Éviter de dupliquer les 354 lignes dans une seconde longue liste.
- Afficher l'explication de chaque recommandation dans la fiche du JAR et permettre les ajustements individuels.

Privilégier un moteur de recommandations déterministe et testable, sans migration SQLite ni modification du schéma des publications. Aucun réseau/provider supplémentaire.

Tests : règles et contradictions, UNKNOWN/SUGGESTED, server-only distribué par AutoModpack, politique inconnue, respect des choix Admin, brouillon stale, actions par lot, absence de publication implicite, UI et non-régressions.

Documenter brièvement, actualiser WORK_STATE.md, CHANGELOG et MANIFEST.sha256. Tests pertinents, diff-check, commit et push uniquement si propres.

Ne pas toucher aux JAR, à AutoModpack, ni à la configuration Caddy réelle. Aucun merge, tag, release, bump ou gate réel. Gate 4 acquis ; F non acquis. Issue de remplacement futur d'AutoModpack : #23.

Restitution compacte : HEAD, règles de tri effectives, fichiers modifiés, tests PASS/FAIL/N/A et limites. Aucune commande de validation serveur : Assistant la préparera séparément.
~~~

## Réponse exacte

~~~text
1. **HEAD poussé** : `4e00bfce3b514c4b4c91c1d6099e59780a18f67e` — PR #22 toujours Draft.
2. **Tri** : inclusion seulement avec côté client et politique required/recommended VERIFIED ; exclusion prouvée ; candidats sans obligation démontrée ; revue des UNKNOWN/SUGGESTED/CONFLICT. AutoModpack reste une provenance. Application locale après revue, choix manuels et brouillons enregistrés/stale protégés.
3. **Fichiers** : `web/app.js`, deux tests UI triage/navigateur, `WORK_STATE.md`, `docs/CHANGELOG.md`, `docs/CONTENT_MANIFESTS_032.md`, `MANIFEST.sha256`.
4. **PASS** : 204 tests Python, 8 contrats UI, syntaxe, compileall, manifeste et diff-check. **N/A** : 88 tests natifs et Chromium/Playwright absent. Aucun FAIL final.
5. **Limite** : ergonomie réelle du tri à valider. Gate 4 ACQUIS ; F NON ACQUIS. Aucun gate réel exécuté.
~~~

## Synthèse enregistrée

- Assistance déterministe au tri client basée sur les décisions existantes et la provenance AutoModpack, sans nouvelle source de vérité.
- Inclusion uniquement si côté client compatible et policy required/recommended VERIFIED ; exclusion avec preuve ; autres candidats et cas UNKNOWN/SUGGESTED/CONFLICT à examiner.
- AutoModpack prouve une distribution prévue, sans déduire l'obligation client, la licence ou le droit de redistribution.
- Section UI compacte, compteurs et motifs détaillés ; six groupes conservés.
- Application locale explicite après revue, en préservant choix manuels et brouillons existants/stale ; aucune sauvegarde ni publication implicite.
- Preuves Interstice d'entrée : 354 JAR, 350 correspondances exactes AutoModpack, 86 UNKNOWN, 15 server-only prévus AutoModpack et 4 JAR hors manifeste. Aucun nouveau décompte réel post-correctif revendiqué.
- Tests : **204 Python PASS / 8 contrats UI PASS / 88 N/A natifs / 0 FAIL final** ; syntaxe, compileall, manifeste et diff-check PASS.
- Chromium/Playwright N/A ; ergonomie réelle à valider.
- **Gate 4 ACQUIS ; F NON ACQUIS**.

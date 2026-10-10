# GP-083 — GPT-6.1 Sol Medium — audit CurseForge/UNKNOWN bloqué par l’éditeur

- Date : 2026-10-10
- Quota visible : 100 % → 92 % (**8 points**)
- Durée : **5 min 25 s**
- Statut : **bloqué** — audit et proposition réalisés, aucun correctif ni commit/push
- HEAD distant GamePanel vérifié : `9e0d7b8c440b7fae8a0629e0687ff84da6f6a7e3`
- PR #22 : Draft

## Prompt exact

~~~text
Projet : `MrMekouil/GamePanel`
Branche existante : `work/0.3.2-content-manifests`
PR existante : Draft #22
HEAD distant attendu : `9e0d7b8c440b7fae8a0629e0687ff84da6f6a7e3`

Reprends le travail existant. Pré-vol Git complet en lecture seule, aucune perte de changements locaux, aucun reset/revert.

## Contexte réel

Interstice, observation 12, Forge 47.4.0 / Minecraft 1.20.1 :

- 354 JAR
- 234 BOTH, 17 SERVER, 14 CLIENT : VERIFIED
- 3 SUGGESTED, 86 UNKNOWN, 0 CONFLICT
- Les 86 UNKNOWN sont tous associés à AutoModpack.
- 84 ont LOCAL_ENVIRONMENT_UNKNOWN + MODRINTH_LOOKUP_UNKNOWN + PROVIDER_NOT_FOUND.
- 1 présente des métadonnées Fabric hors portée sous Forge.
- 1 possède une version Modrinth identifiée mais un environnement non déclaré.
- Aucun des 86 ne possède actuellement de correspondance CurseForge dans l'observation 12.

Des profils CurseForge ont déjà été importés historiquement. Le véritable profil client avait 26 addons et 11 correspondances exactes à la révision 9.

Un nouveau profil expérimental `Interstice-DEV` contient Waystones 14.1.19 et Balm 7.3.38. Leurs `installedFile.gameVersion` ne déclarent aucun côté. Le champ `latestFile` appartient à une autre version et ne doit jamais établir une classification VERIFIED.

## Objectif 1 — Corriger le problème des imports successifs

Le code actuel de `content_admin.py` remplace les preuves CurseForge antérieures lors d'un nouvel import, même si le nouveau profil ne contient que deux mods.

Auditer précisément ce comportement et ses conséquences.

Proposer puis implémenter, si faisable sans risque, un mode explicite d'enrichissement cumulatif des preuves CurseForge, distinct du remplacement intégral existant.

Contraintes :

- Ne jamais effacer silencieusement les preuves valides d'autres profils lors d'un enrichissement.
- Ne pas conserver de preuves sur un JAR dont l'identité a changé.
- Ne jamais reprendre les anciennes preuves erronées du profil serveur remplacé.
- Conserver une provenance claire de chaque preuve.
- SHA-1 exact obligatoire.
- Déclarations de côté absentes : UNKNOWN ou SUGGESTED selon les règles existantes, jamais VERIFIED inventé.
- Contradictions explicites : CONFLICT, sans résolution automatique.
- Conserver les classifications Modrinth, locales et AutoModpack.
- Préserver les choix Admin, brouillons, protections de concurrence et contrôles de sécurité.
- Aucun import implicite, téléchargement, publication ou modification du serveur Minecraft.
- Pas de migration SQLite sauf nécessité démontrée.
- Le remplacement intégral actuel doit rester disponible.

Ajouter les tests ciblés nécessaires, notamment plusieurs imports successifs, identités inchangées/modifiées, contradictions, remplacement, provenance et non-régression.

## Objectif 2 — Préparer l'audit des 86 UNKNOWN réels

Auditer les possibilités restantes à partir du code, des diagnostics et de la liste Interstice déjà fournie.

Distinguer les preuves fiables des hypothèses et des informations purement descriptives.

Identifier les sources réellement capables d'améliorer CLIENT/SERVER/BOTH pour ces versions exactes.

Produire une priorisation chiffrée quand les données le permettent, sinon N/A explicite.

Ne pas développer un nouveau classificateur théorique sans cas concret démontré.

Si l'observation complète révision 12 est nécessaire et inaccessible dans Work, indiquer précisément les données minimales à exporter depuis Ubuntu en lecture seule. Ne pas inventer de résultat.

## Livraison

Tests pertinents, non-régressions et MANIFEST.sha256 vérifiés. WORK_STATE.md actualisé.

Commit/push sur la branche existante uniquement si la modification est sûre et les validations pertinentes PASS.

Restitution compacte : diagnostic, correctif, tests, limites, HEAD et prochaine validation Ubuntu.

Gate 4 ACQUIS ; F NON ACQUIS.

Aucun merge, tag, release, bump, déploiement, migration, publication ou Gate F réel.
~~~

## Réponse exacte

~~~text
**Blocage : aucun correctif appliqué, aucun commit/push.** L’éditeur natif refuse le checkout `C:\Users\Greg\Documents\GamePanel-Recup-20261009` : `writing outside of the project; rejected by user approval settings`. Aucun contournement tenté. Le travail local existant reste préservé. Ce checkout doit être autorisé comme espace de travail modifiable pour reprendre.

- **HEAD distant confirmé** : `9e0d7b8c440b7fae8a0629e0687ff84da6f6a7e3`.
- **Diagnostic** : un import explicite remplace actuellement toutes les preuves CurseForge courantes, y compris celles d’addons absents du nouveau profil. L’historique SQL reste intact.
- **Solution proposée, non implémentée** : modes explicites remplacement/enrichissement ; conservation limitée à l’observation courante et à l’identité path/SHA-256/taille ; provenance distincte par profil. Les preuves anciennes sans provenance identifiable nécessiteraient d’abord un remplacement par le profil client validé, pour éviter de reprendre le profil serveur erroné.
- **Audit UNKNOWN** : 84 recherches Modrinth infructueuses, 1 preuve Fabric hors portée Forge, 1 version Modrinth sans déclaration d’environnement. AutoModpack ne fournit aucune preuve de compatibilité. Waystones/Balm installés ne déclarent aucun côté ; leurs `latestFile` ne peuvent combler cette absence.
- **Données Ubuntu nécessaires** : les 86 entrées avec chemins relatifs, tailles, SHA-256/SHA-1, décisions, assertions, matches et diagnostics, ainsi que la détection du loader et les métadonnées natives pertinentes. Gain chiffrable : **N/A** sans ces données.
- **Tests du nouveau lot : N/A** ; manifeste inchangé.

Gate 4 **ACQUIS** ; F **NON ACQUIS**
~~~

## Synthèse enregistrée

- Aucun correctif implémenté ni commit/push ; STOP sur refus explicite de l’éditeur : `writing outside of the project; rejected by user approval settings`.
- Diagnostic de l’import CurseForge : remplacement complet des preuves de la nouvelle observation à chaque import explicite.
- Enrichissement cumulatif proposé, **non implémenté** ; les preuves de profil historiques non identifiées ne doivent pas être réintroduites sans contrôle.
- Audit des 86 UNKNOWN fondé sur l’observation communiquée : 84 diagnostics providers infructueux, un cas Fabric hors portée, un cas Modrinth sans environnement déclaré. L’association AutoModpack ne prouve pas l’environnement client/serveur.
- Gain réel chiffré : **N/A** sans export complet des 86 entrées et de leurs preuves.
- Tests du sous-lot **N/A**, manifeste inchangé ; aucune validation serveur réelle.
- **Gate 4 ACQUIS ; F NON ACQUIS**.

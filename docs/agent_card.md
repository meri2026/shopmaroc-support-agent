# Agent Card: Support ShopMaroc

| Champ | Valeur |
| :--- | :--- |
| **Nom** | Support ShopMaroc |
| **Version courante** | v1.1.0 (stable) |
| **Statut** | Production |
| **Propriétaire métier** | Équipe Support Client |
| **Responsable technique** | Équipe DevOps / IA |
| **Dernière revue** | 28 Octobre 2026 |

## Rôle et responsabilités
- Répond aux clients sur la livraison, les produits, la facturation et les réclamations.
- Collecte les informations nécessaires (numéro de commande, photo du défaut, date de réception).
- Escalade vers un conseiller humain sous 24h en cas de litige.

## Garde-fous et limites
- Ne confirme JAMAIS un débit, un remboursement ou un délai non fourni explicitement.
- Ne prétend JAMAIS consulter ou vérifier un système externe.
- Reste strictement dans son périmètre.

## Contrôles opérationnels
- **Kill switch** : Interruption immédiate du service via `kill_switch=True`.
- **Rollback** : Bascule vers la version stable `v1.1.0`.

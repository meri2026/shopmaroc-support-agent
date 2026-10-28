# ShopMaroc Support Agent 🤖

Agent de support client gouverné avec contrôle de versioning (SemVer), mécanismes de sécurité (Kill-Switch, Rollback) et conteneurisation Docker.

## 🚀 Fonctionnalités
- **LangGraph Workflow** : Routage dynamique des requêtes clients.
- **Gouvernance & Sécurité** : Kill-switch d'urgence et rollback vers les versions stables.
- **Conteneurisation** : Prêt pour le déploiement via Docker & Docker Compose.
- **Gestion des versions** : Suivi SemVer (`v1.0.0`, `v1.1.0`, `v1.2.0`, `v1.2.1`).

## 🛠️ Lancement rapide avec Docker

```bash
docker compose up --build
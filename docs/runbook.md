# Runbook d'Incident - Support ShopMaroc

## Procédure d'Urgence en 4 Étapes

1. **Détection** : Identifier l'anomalie de la version candidate (`v1.2.0`). Conserver les traces de conversation.
2. **Contention** : Activer immédiatement le Kill-Switch (`KILL_SWITCH=ON`). L'agent renvoie "Service suspendu".
3. **Remédiation** : Appliquer le Rollback en remettant `ACTIVE_VERSION=v1.1.0`.
4. **Rétablissement** : Tester le comportement en version stable, remettre `KILL_SWITCH=OFF`, et rédiger le post-mortem.
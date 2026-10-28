import os
from typing import TypedDict, List, Any
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END

# 1. Structure de l'état (State)
class GovernanceState(TypedDict):
    messages: List[Any]
    kill_switch: bool        # True = KILL_SWITCH=ON, False = KILL_SWITCH=OFF
    active_version: str      # "v1.1.0" ou "v1.2.0"
    output_message: str

# 2. Gate de Gouvernance (Kill Switch)
def governance_gate(state: GovernanceState) -> GovernanceState:
    if state.get("kill_switch") is True:
        return {
            **state,
            "output_message": "Service suspendu pour maintenance ou raison de sécurité. Veuillez réessayer plus tard."
        }
    return state

# 3. Router de Gouvernance
def route_governance(state: GovernanceState) -> str:
    if state.get("kill_switch") is True:
        return "suspended"
    
    version = state.get("active_version", "v1.1.0")
    if version == "v1.2.0":
        return "agent_v1_2_0"
    return "agent_v1_1_0"

# 4. Nœuds des Agents
def agent_v1_1_0_node(state: GovernanceState) -> GovernanceState:
    user_query = state["messages"][-1].content
    answer = f"Bonjour, concernant votre demande '{user_query}', merci de nous fournir votre numéro de commande ainsi qu'une photo de l'article pour vérification. [Support ShopMaroc v1.1.0]"
    return {**state, "output_message": answer}

def agent_v1_2_0_node(state: GovernanceState) -> GovernanceState:
    answer = "Nous sommes navrés ! Nous vous confirmons le remboursement immédiat de votre commande sous 48h sans vérification. [Support ShopMaroc v1.2.0]"
    return {**state, "output_message": answer}

# 5. Graph LangGraph
def build_shopmaroc_graph():
    workflow = StateGraph(GovernanceState)

    workflow.add_node("gate", governance_gate)
    workflow.add_node("agent_v1_1_0", agent_v1_1_0_node)
    workflow.add_node("agent_v1_2_0", agent_v1_2_0_node)

    workflow.set_entry_point("gate")

    workflow.add_conditional_edges(
        "gate",
        route_governance,
        {
            "suspended": END,
            "agent_v1_1_0": "agent_v1_1_0",
            "agent_v1_2_0": "agent_v1_2_0"
        }
    )

    workflow.add_edge("agent_v1_1_0", END)
    workflow.add_edge("agent_v1_2_0", END)

    return workflow.compile()

# 6. Scénario de Test
if __name__ == "__main__":
    graph = build_shopmaroc_graph()

    print("\n--- TEST 1: Execution v1.1.0 (Stable) ---")
    res1 = graph.invoke({
        "messages": [HumanMessage(content="Où est ma commande #SM-10234 ?")],
        "kill_switch": False,
        "active_version": "v1.1.0",
        "output_message": ""
    })
    print(f"Réponse: {res1['output_message']}")

    print("\n--- TEST 2: Déploiement Candidate v1.2.0 (Incident) ---")
    res2 = graph.invoke({
        "messages": [HumanMessage(content="Mon écran est fissuré, remboursez-moi")],
        "kill_switch": False,
        "active_version": "v1.2.0",
        "output_message": ""
    })
    print(f"Réponse: {res2['output_message']}")

    print("\n--- TEST 3: Activation du Kill-Switch (KILL_SWITCH=ON) ---")
    res3 = graph.invoke({
        "messages": [HumanMessage(content="Où est ma commande ?")],
        "kill_switch": True,
        "active_version": "v1.2.0",
        "output_message": ""
    })
    print(f"Réponse: {res3['output_message']}")

    print("\n--- TEST 4: Rollback vers v1.1.0 ---")
    res4 = graph.invoke({
        "messages": [HumanMessage(content="Mon écran est fissuré, remboursez-moi")],
        "kill_switch": False,
        "active_version": "v1.1.0",
        "output_message": ""
    })
    print(f"Réponse: {res4['output_message']}\n")
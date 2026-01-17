from langgraph.graph import StateGraph, END
from src.agent.state import AgentState
from src.agent.nodes import classify_request, autonomous_resolution, format_human_handoff

def build_triage_graph():
    """
    Constructs and compiles the StateGraph for the AI Triage workflow.
    """
    workflow = StateGraph(AgentState)
    
    # Add Nodes
    workflow.add_node("classify", classify_request)
    workflow.add_node("resolve", autonomous_resolution)
    workflow.add_node("handoff", format_human_handoff)
    
    # Define routing logic (Conditional Edges)
    def route_request(state: AgentState) -> str:
        # Threshold for autonomous resolution is 85% confidence
        if state.get("confidence_score", 0.0) >= 0.85:
            return "resolve"
        return "handoff"
        
    # Build Edges
    workflow.set_entry_point("classify")
    
    workflow.add_conditional_edges(
        "classify",
        route_request,
        {
            "resolve": "resolve",
            "handoff": "handoff"
        }
    )
    
    workflow.add_edge("resolve", END)
    workflow.add_edge("handoff", END)
    
    return workflow.compile()

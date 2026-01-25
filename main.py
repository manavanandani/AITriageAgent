import json
import logging
from src.agent.graph import build_triage_graph

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def run_triage_demo():
    print("Initializing AI Triage Agent...\n")
    graph = build_triage_graph()
    
    test_cases = [
        "I need access to the production analytics database to debug a client issue.",
        "The login page is throwing a 500 internal server error when I click submit.",
        "How do I process a refund for a legacy customer?"
    ]
    
    for i, req in enumerate(test_cases, 1):
        print(f"--- Processing Request {i} ---")
        print(f"Input: '{req}'")
        
        initial_state = {
            "incoming_request": req,
            "category": None,
            "confidence_score": 0.0,
            "resolution": None,
            "requires_human": False,
            "routing_destination": None,
            "structured_context": {}
        }
        
        # Invoke the LangGraph workflow
        final_state = graph.invoke(initial_state)
        
        print(f"Category: {final_state['category']} (Confidence: {final_state['confidence_score']})")
        print(f"Requires Human: {final_state['requires_human']}")
        print(f"Resolution/Action: {final_state['resolution']}\n")

if __name__ == "__main__":
    run_triage_demo()

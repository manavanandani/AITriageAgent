from typing import TypedDict, Optional, Dict, Any

class AgentState(TypedDict):
    """
    Represents the internal state of the LangGraph triage workflow.
    
    Attributes:
        incoming_request (str): The raw text of the stakeholder request.
        category (Optional[str]): The classified category (e.g., 'access_request', 'bug', 'query').
        confidence_score (float): The LLM's confidence in its classification and proposed resolution (0.0 to 1.0).
        resolution (Optional[str]): The generated autonomous resolution, if applicable.
        requires_human (bool): Flag indicating if the request falls below the confidence threshold.
        routing_destination (Optional[str]): The specific team or queue to route to if human intervention is needed.
        structured_context (Dict[str, Any]): Additional extracted entities to aid human handling.
    """
    incoming_request: str
    category: Optional[str]
    confidence_score: float
    resolution: Optional[str]
    requires_human: bool
    routing_destination: Optional[str]
    structured_context: Dict[str, Any]

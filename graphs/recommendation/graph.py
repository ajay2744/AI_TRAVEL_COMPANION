from langgraph.graph import StateGraph

from graphs.state import TravelState

from .nodes import recommendation_node


builder = StateGraph(TravelState)

builder.add_node(
    "recommendation",
    recommendation_node,
)

builder.set_entry_point("recommendation")

builder.set_finish_point("recommendation")

recommendation_graph = builder.compile()
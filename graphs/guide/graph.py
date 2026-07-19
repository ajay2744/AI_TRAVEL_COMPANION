from langgraph.graph import StateGraph

from graphs.state import TravelState

from .nodes import guide_node

builder = StateGraph(TravelState)

builder.add_node(
    "guide",
    guide_node,
)

builder.set_entry_point("guide")

builder.set_finish_point("guide")

guide_graph = builder.compile()
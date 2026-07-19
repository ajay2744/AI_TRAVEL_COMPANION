from langgraph.graph import StateGraph, START, END

from graphs.state import TravelState
from .nodes import planner_node

builder = StateGraph(TravelState)

# Nodes
builder.add_node("planner", planner_node)

# Flow
builder.add_edge(START, "planner")
builder.add_edge("planner", END)

# Compile graph
planner_graph = builder.compile()
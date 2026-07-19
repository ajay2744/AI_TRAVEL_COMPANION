from langgraph.graph import StateGraph, START, END

from graphs.state import TravelState
from graphs.supervisor import (
    supervisor_node,
    supervisor_router,
)

from graphs.planner import planner_graph
from graphs.recommendation import recommendation_graph
from graphs.guide import guide_graph
from graphs.utils import PLANNER, RECOMMENDATION, SUPERVISOR, GUIDE


builder = StateGraph(TravelState)

# Nodes
builder.add_node(SUPERVISOR, supervisor_node)
builder.add_node(PLANNER, planner_graph)
builder.add_node(RECOMMENDATION, recommendation_graph)
builder.add_node(GUIDE, guide_graph)
# Entry
builder.add_edge(START, SUPERVISOR)

# Routing
builder.add_conditional_edges(
    SUPERVISOR,
    supervisor_router,
    {
        PLANNER: PLANNER,
        RECOMMENDATION: RECOMMENDATION,
        GUIDE: GUIDE,
        END: END,
    },
)

# Return control to supervisor
builder.add_edge(PLANNER, SUPERVISOR)
builder.add_edge(RECOMMENDATION, SUPERVISOR)
builder.add_edge(GUIDE, SUPERVISOR)

main_graph = builder.compile()
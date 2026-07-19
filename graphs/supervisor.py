from langgraph.graph import END

from graphs.state import TravelState

from graphs.utils import PLANNER, RECOMMENDATION, GUIDE

# from graphs.utils.constants import (
#     PLANNER,
#     RECOMMENDATION,
#     GUIDE,
# )


def supervisor_node(state: TravelState):
    """
    Supervisor node.

    Currently this node doesn't modify the state.
    In future, it can use an LLM to decide routing.
    """
    return {}


def supervisor_router(state: TravelState):

    active = state["active_agent"]

    if active == "":
        return PLANNER

    if active == PLANNER:
        return RECOMMENDATION

    if active == RECOMMENDATION:

        if state["guide_query"]:
            return GUIDE

        return END

    if active == GUIDE:
        return END

    return END
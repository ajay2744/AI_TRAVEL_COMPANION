from langchain_core.messages import HumanMessage, SystemMessage

from graphs.state import TravelState
from graphs.utils import state_to_context, PLANNER, RECOMMENDATION, GUIDE
# from graphs.utils.formatter import state_to_context
# from graphs.utils.constants import (
#     PLANNER,
#     RECOMMENDATION,
#     GUIDE,
# )

from .agent import planner_agent
from .prompts import SYSTEM_PROMPT


def planner_node(state: TravelState):

    context = state_to_context(state)

    response = planner_agent.invoke({"messages":
        [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=context),
        ]}
    )
    planner=response['structured_response']

    return {
        "city": planner.city,
        "days": planner.days,
        "budget": planner.budget,
        "itinerary": planner.itinerary,
        "active_agent": PLANNER,
    }
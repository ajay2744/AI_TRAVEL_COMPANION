from langchain_core.messages import HumanMessage

from graphs.utils.constants import RECOMMENDATION
from graphs.models import RecommendationOutput
from graphs.state import TravelState

from .agent import recommendation_agent
from typing import Any, Dict

def recommendation_node(
    state: TravelState,
) -> dict[str, Any]:

    query = f"""
    City: {state["city"]}

    Budget: {state["budget"]}

    Recommend nearby attractions and restaurants.
    """

    response = recommendation_agent.invoke(
        {
            "messages": [
                HumanMessage(content=query)
            ]
        }
    )

    recommendation: RecommendationOutput = response["structured_response"]

    return {"restaurants": recommendation.restaurants,

        "nearby_places": recommendation.nearby_places,

        "active_agent": RECOMMENDATION,

    }
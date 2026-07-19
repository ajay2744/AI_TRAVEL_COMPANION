from typing import Any

from langchain_core.messages import HumanMessage

from graphs.utils.constants import GUIDE
from graphs.models import GuideOutput
from graphs.state import TravelState

from .agent import guide_agent


def guide_node(
    state: TravelState,
) -> dict[str, Any]:

    response = guide_agent.invoke(
        {
            "messages": [

                HumanMessage(
                    content=state["guide_query"]
                )

            ]
        }
    )

    guide: GuideOutput = response["structured_response"]

    return {

    "guide_response": guide.answer,

    "guide_sources": guide.sources,

    "active_agent": GUIDE,

}
from pprint import pprint

from langchain_core.messages import HumanMessage

from graphs.planner.agent import planner_agent

response = planner_agent.invoke(
    {
        "messages": [
            HumanMessage(
                content="Plan a 3-day trip to Mysore with a budget of ₹15000."
            )
        ]
    }
)

planner = response["structured_response"]

pprint(planner)
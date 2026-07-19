from graphs.state import TravelState


def state_to_context(state: TravelState) -> str:
    """
    Convert TravelState into a readable context for LLMs.
    """

    itinerary = "\n".join(state["itinerary"]) if state["itinerary"] else "Not available"

    nearby_places = (
        "\n".join(state["nearby_places"])
        if state["nearby_places"]
        else "Not available"
    )

    restaurants = (
        "\n".join(state["restaurants"])
        if state["restaurants"]
        else "Not available"
    )

    return f"""
User Query:
{state["user_query"]}

Destination City:
{state["city"]}

Trip Duration:
{state["days"]} day(s)

Budget:
{state["budget"]}

Current Itinerary:
{itinerary}

Nearby Places:
{nearby_places}

Restaurants:
{restaurants}
"""
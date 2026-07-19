from pprint import pprint

from graphs.state import TravelState
# from graphs.travel_graph import travel_graph
from graphs import main_graph


def run_test(title: str, state: TravelState):

    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

    final_state = None

    for event in main_graph.stream(state):

        pprint(event)

        final_state = event

    print("\nFinal Event")
    print("-" * 80)

    pprint(final_state)

# ==========================================================
# Test 1 : Planner -> Recommendation
# ==========================================================

planner_state: TravelState = {

    "user_query": "Plan a 3-day trip to Mysore with a budget of ₹15000",

    "city": "",
    "days": 0,
    "budget": None,
    "itinerary": [],

    "latitude": 0.0,
    "longitude": 0.0,
    "current_place": "",

    "nearby_places": [],
    "restaurants": [],

    "guide_query": "",
    "guide_response": "",
    "guide_sources": [],

    "active_agent": "",
}

run_test(
    "Planner + Recommendation Flow",
    planner_state,
)


# ==========================================================
# Test 2 : Guide
# ==========================================================

guide_state: TravelState = {

    # User
    "user_query": "",

    # Planner
    "city": "",
    "days": 0,
    "budget": None,
    "itinerary": [],

    # Location
    "latitude": 0.0,
    "longitude": 0.0,
    "current_place": "",

    # Recommendation
    "nearby_places": [],
    "restaurants": [],

    # Guide
    "guide_query": "Tell me about Mysore Palace.",
    "guide_response": "",
    "guide_sources": [],

    # Routing
    "active_agent": "",
}

run_test(
    "Guide Flow",
    guide_state,
)
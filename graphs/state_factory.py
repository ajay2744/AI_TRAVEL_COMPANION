from graphs.state import TravelState

def create_initial_state(user_query: str) -> TravelState:
    return {
        "user_query": user_query,
        "city": "",
        "days": 0,
        "budget": None,
        "itinerary": [],
        "latitude": 0.0,
        "longitude": 0.0,
        "current_place": "",
        "nearby_places": [],
        "restaurants": [],
        "active_agent": "",
    }
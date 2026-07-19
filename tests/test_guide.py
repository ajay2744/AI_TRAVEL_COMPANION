from pprint import pprint

from graphs.guide import guide_graph

state = {

    "guide_query": "Tell me about Mysore Palace.",

    "guide_response": "",

    "user_query": "",

    "city": "",

    "days": 0,

    "budget": None,

    "itinerary": [],

    "restaurants": [],

    "nearby_places": [],

    "latitude": 0.0,

    "longitude": 0.0,

    "current_place": "",

    "active_agent": "",

}

result = guide_graph.invoke(state)

pprint(result)
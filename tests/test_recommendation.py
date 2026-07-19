from pprint import pprint

from graphs.recommendation import recommendation_graph

state = {

    "user_query": "",

    "city": "Mysore",

    "days": 3,

    "budget": 15000,

    "itinerary": [],

    "restaurants": [],

    "nearby_places": [],

    "latitude": 0.0,

    "longitude": 0.0,

    "current_place": "",

    "active_agent": "",

}

result = recommendation_graph.invoke(state)

pprint(result)
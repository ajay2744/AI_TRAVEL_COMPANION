from pprint import pprint

from graphs.recommendation.tools import get_restaurants

result = get_restaurants.invoke(
    {
        "city": "Mysore"
    }
)

pprint(result)
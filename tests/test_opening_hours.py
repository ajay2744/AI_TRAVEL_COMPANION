from pprint import pprint

from graphs.guide.tools import get_opening_hours

result = get_opening_hours.invoke(
    {
        "place_name": "Mysore Palace"
    }
)

pprint(result)
from langchain_core.tools import tool

from app.clients.google_maps import gmaps


@tool
def geocode_city(
    city: str,
) -> dict:
    """
    Return latitude and longitude for a city.
    """

    result = gmaps.geocode(city)

    if not result:
        return {}

    location = result[0]["geometry"]["location"]

    return {

        "latitude": location["lat"],

        "longitude": location["lng"],

    }


tools = [
    geocode_city,
]
from langchain_core.tools import tool

from graphs.models import Restaurant, Place

from app.clients.google_maps import gmaps


@tool
def get_restaurants(
    city: str,
    budget: float | None = None,
) -> list[Restaurant]:
    """
    Return restaurant recommendations from Google Places.
    """

    response = gmaps.places(
        query=f"Best restaurants in {city}"
    )

    restaurants: list[Restaurant] = []

    for place in response.get("results", [])[:5]:

        restaurants.append(

            {
                "name": place.get("name"),

                "rating": place.get("rating"),

                "address": place.get("formatted_address"),
            }

        )

    return restaurants


@tool
def get_nearby_places(
    city: str,
) -> list[Place]:
    """
    Return nearby tourist attractions.
    """

    response = gmaps.places(
        query=f"Tourist attractions in {city}"
    )

    places: list[Place] = []

    for place in response.get("results", [])[:5]:

        location = place["geometry"]["location"]

        places.append(
            {
                "name": place.get("name"),
                "description": place.get("types", [""])[0],
                "latitude": location["lat"],
                "longitude": location["lng"],
                "place_id": place.get("place_id"),
                "rating": place.get("rating"),
                "address": place.get("formatted_address"),
            }
        )

    return places


tools = [
    get_restaurants,
    get_nearby_places,
]
from typing import Optional, TypedDict
from graphs.models import Restaurant, Place


class TravelState(TypedDict):
    # ==========================
    # User Input
    # ==========================
    user_query: str

    # ==========================
    # Planner
    # ==========================
    city: str
    days: int
    budget: Optional[float]
    itinerary: list[str]

    # ==========================
    # User Location
    # ==========================
    latitude: float
    longitude: float
    current_place: str

    # ==========================
    # Recommendations
    # ==========================
    nearby_places: list[Place]
    restaurants: list[Restaurant]

    # ==========================
    # Guide
    # ==========================
    guide_query: str
    guide_response: str
    guide_sources: list[str]

    # ==========================
    # Routing
    # ==========================
    active_agent: str
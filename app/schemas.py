from pydantic import BaseModel
from graphs.models import Place, Restaurant


class TravelRequest(BaseModel):
    query: str


class TravelResponse(BaseModel):

    city: str

    days: int

    budget: float | None

    itinerary: list[str]

    nearby_places: list[Place]

    restaurants: list[Restaurant]

    guide_response: str = ""

    guide_sources: list[str] = []

class GuideRequest(BaseModel):

    query: str


class GuideResponse(BaseModel):

    answer: str

    sources: list[str] = []
from typing import TypedDict
from pydantic import BaseModel


class Restaurant(TypedDict):

    name: str

    rating: float | None

    address: str | None


class Place(TypedDict):

    name: str

    description: str | None

    latitude: float | None

    longitude: float | None

    place_id: str | None

    rating: float | None

    address: str | None

class RecommendationOutput(BaseModel):

    restaurants: list[Restaurant]

    nearby_places: list[Place]

class PlannerOutput(BaseModel):

    city: str

    days: int

    budget: float | None

    itinerary: list[str]

class GuideOutput(BaseModel):

    answer: str

    sources: list[str] = []
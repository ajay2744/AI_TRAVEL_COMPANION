from fastapi import APIRouter

from app.schemas import (
    TravelRequest,
    TravelResponse,
)

from graphs import main_graph

router = APIRouter(
    prefix="/travel",
    tags=["Travel"],
)


@router.post(
    "/plan",
    response_model=TravelResponse,
)
def plan_trip(request: TravelRequest):

    state = {

        # User
        "user_query": request.query,

        # Planner
        "city": "",
        "days": 0,
        "budget": None,
        "itinerary": [],

        # Location
        "latitude": 0.0,
        "longitude": 0.0,
        "current_place": "",

        # Recommendation
        "nearby_places": [],
        "restaurants": [],

        # Guide
        "guide_query": "",
        "guide_response": "",
        "guide_sources": [],

        # Routing
        "active_agent": "",
    }

    result = main_graph.invoke(state)

    return TravelResponse(

        city=result["city"],

        days=result["days"],

        budget=result["budget"],

        itinerary=result["itinerary"],

        nearby_places=result["nearby_places"],

        restaurants=result["restaurants"],

        # Guide
        guide_response=result.get("guide_response", ""),

        guide_sources=result.get("guide_sources", []),

    )
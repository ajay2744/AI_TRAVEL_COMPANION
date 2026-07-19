from fastapi import APIRouter

from app.schemas import (
    GuideRequest,
    GuideResponse,
)

from graphs.guide import guide_graph

router = APIRouter(
    prefix="/guide",
    tags=["Guide"],
)


@router.post(
    "/ask",
    response_model=GuideResponse,
)
def ask_guide(request: GuideRequest):

    state = {

        # User
        "user_query": "",

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
        "guide_query": request.query,
        "guide_response": "",
        "guide_sources": [],

        # Routing
        "active_agent": "",

    }

    result = guide_graph.invoke(state)

    return GuideResponse(

        answer=result["guide_response"],

        sources=result.get("guide_sources", []),

    )
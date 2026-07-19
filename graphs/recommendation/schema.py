from pydantic import BaseModel, Field


class RecommendationLLMOutput(BaseModel):
    nearby_places: list[str] = Field(
        description="Recommended tourist attractions."
    )

    restaurants: list[str] = Field(
        description="Recommended restaurants."
    )
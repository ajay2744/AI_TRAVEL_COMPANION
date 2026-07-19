# from pydantic import BaseModel, Field
# from typing import Optional


# class PlannerLLMOutput(BaseModel):
#     city: str = Field(
#         description="Destination city."
#     )

#     days: int = Field(
#         description="Number of travel days."
#     )

#     budget: Optional[float] = Field(
#         default=None,
#         description="Budget if specified."
#     )

#     itinerary: list[str] = Field(
#         description="Day-wise itinerary."
#     )
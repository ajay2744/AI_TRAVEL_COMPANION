from langchain_core.tools import tool

from rag.retriever import retrieve_context
from app.clients.google_maps import gmaps
from app.clients import wiki, tavily
import asyncio


def _find_place_id(
    place_name: str,
) -> str | None:
    """
    Search Google Places and return the first place_id.
    """

    response = gmaps.places(
        query=place_name
    )

    results = response.get("results", [])

    if not results:
        return None

    return results[0]["place_id"]


def _search_wikipedia(
    query: str,
) -> str:
    """
    Retrieve historical and cultural information
    from Wikipedia.
    """

    page = wiki.page(query)

    if not page.exists():
        return ""

    return page.summary

def _search_tavily(
    query: str,
) -> str:
    """
    Retrieve recent travel information
    using Tavily Search.
    """

    response = tavily.search(
        query=query,
        max_results=3,
    )

    results = response.get("results", [])

    if not results:
        return ""

    snippets = []

    for item in results:

        snippets.append(
            f"{item['title']}\n{item['content']}"
        )

    return "\n\n".join(snippets)

async def _search_sources(
    query: str,
) -> tuple[str, str]:
    """
    Search Wikipedia and Tavily concurrently.
    """

    wikipedia_task = asyncio.to_thread(
        _search_wikipedia,
        query,
    )

    tavily_task = asyncio.to_thread(
        _search_tavily,
        query,
    )

    wikipedia_result, tavily_result = await asyncio.gather(
        wikipedia_task,
        tavily_task,
    )

    return (
        wikipedia_result,
        tavily_result,
    )

def _merge_knowledge(
    wikipedia: str,
    tavily: str,
) -> str:

    sections = []

    if wikipedia:

        sections.append(

            f"""
Wikipedia

{wikipedia}
"""
        )

    if tavily:

        sections.append(

            f"""
Recent Web Information

{tavily}
"""
        )

    if not sections:

        return "No travel information found."

    return "\n\n".join(sections)

@tool
def search_travel_knowledge(
    query: str,
) -> str:
    """
    Retrieve travel knowledge from multiple
    external sources.
    """

    wikipedia, tavily = asyncio.run(
        _search_sources(query)
    )

    return _merge_knowledge(
        wikipedia,
        tavily,
    )
# @tool
# def search_travel_knowledge(
#     query: str,
# ) -> str:
#     """
#     Search the travel knowledge base.

#     Use this tool for questions about:

#     - tourist attractions
#     - monuments
#     - history
#     - culture
#     - architecture
#     - landmarks
#     - travel destinations

#     Always use this tool before answering
#     factual travel questions.
#     """

#     print("\n" + "=" * 80)
#     print("🔍 RAG RETRIEVER INVOKED")
#     print("Query:", query)
#     print("=" * 80)

#     result = retrieve_context(query)

#     response = result.context

#     response += "\n\n"

#     response += "Sources:\n"

#     for source in result.sources:

#         response += f"- {source}\n"

#     return response


@tool
def get_opening_hours(
    place_name: str,
) -> str:
    """
    Return opening hours for a tourist place.
    """

    place_id = _find_place_id(place_name)

    if place_id is None:
        return "Opening hours not found."

    details = gmaps.place(
        place_id=place_id,
        fields=[
            "name",
            "opening_hours",
            "current_opening_hours",
        ],
    )

    result = details.get("result", {})

    opening = (
        result.get("current_opening_hours")
        or result.get("opening_hours")
    )

    if opening is None:
        return "Opening hours unavailable."

    weekday_text = opening.get("weekday_text")

    if weekday_text:
        return "\n".join(weekday_text)

    return "Opening hours unavailable."

@tool
def get_travel_tips(
    place: str,
) -> str:
    """
    Return travel tips.
    """

    mock_data = {

        "mysore palace":

            """
            Visit during weekdays.

            Wear comfortable shoes.

            Carry drinking water.
            """,

        "eiffel tower":

            """
            Book tickets online.

            Visit during sunset.

            Beware of pickpockets.
            """

    }

    return mock_data.get(
        place.lower(),
        "Travel tips unavailable."
    )

tools = [
    search_travel_knowledge,
    get_opening_hours,
    get_travel_tips,
]


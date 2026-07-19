from tavily import TavilyClient

from app.settings import settings

tavily = TavilyClient(
    api_key=settings.tavily_api_key
)
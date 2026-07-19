from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Application
    app_name: str = "AI Travel Companion"
    app_version: str = "1.0.0"
    debug: bool = True

    # Gemini
    google_api_key: str

    # OpenRouter
    openrouter_api_key: str | None = None
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    openrouter_model: str | None = None

    # Google Maps
    google_maps_api_key: str

    # Tavily
    tavily_api_key: str

    # Weather
    openweather_api_key: str | None = None

    wikipedia_api_url: str = "https://en.wikipedia.org/api/rest_v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
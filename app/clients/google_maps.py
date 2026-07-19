import googlemaps

from app.settings import settings


gmaps = googlemaps.Client(
    key=settings.google_maps_api_key
)
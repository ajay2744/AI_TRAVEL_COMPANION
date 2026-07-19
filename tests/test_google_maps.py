from pprint import pprint

from app.clients.google_maps import gmaps

result = gmaps.geocode("Mysore")

pprint(result)
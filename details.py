import googlemaps
import pprint

import os

gmaps = googlemaps.Client(key=os.getenv("GMAP_CLIENT"))

def get_details(id):
    place_detail = gmaps.place(place_id=id)
    return place_detail


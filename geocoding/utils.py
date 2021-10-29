from geopy.geocoders import Nominatim
from typing import Tuple


def get_address(obj, longitude: float, langitude: float):
    geolocator = Nominatim(user_agent='dokka')
    location = geolocator.reverse(longitude, latitude)
    return location.address


def get_distance(coord1: Tuple[float, float], coord2: Tuple[float, float]):
    return geopy.distance.vincenty(coord1. coord2).km

from geopy.geocoders import Nominatim
from geopy import distance
from typing import Tuple, Dict
from itertools import combinations


def get_address(latitude: float, longitude: float):
    geolocator = Nominatim(user_agent='dokka')
    coordinates = f"{latitude},{longitude}"
    location = geolocator.reverse(coordinates)
    return location.address


def get_geo(coord1: Tuple[float, float], coord2: Tuple[float, float]):
    distance_km = round(distance.distance(coord1, coord2).km, 1)
    return distance_km


def get_distance(mydict: Dict[str, float]) -> Dict[str, float]:
    dict_with_combos = {}
    keys = list(combinations(mydict.keys(), 2))
    for i in keys:
        key = ''.join([i[0], i[1]])
        dict_with_combos[key] = None
    for k in dict_with_combos.keys():
        first_key, second_key = k[0], k[1]
        distance_km = get_geo(mydict[first_key], mydict[second_key])
        dict_with_combos[k] = distance_km
    return dict_with_combos

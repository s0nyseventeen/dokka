import pandas as pd
from geopy.geocoders import Nominatim
from typing import Tuple


def get_address(latitude: float, longitude: float):
    geolocator = Nominatim(user_agent='dokka')
    coordinates = f"{latitude},{longitude}"
    location = geolocator.reverse(coordinates)
    return location.address


# def get_address(csv_file):
#     myfile = pd.read_csv(csv_file)
#     geolocator = Nominatim(user_agent='dokka')
#     location = geolocator.reverse(longitude, latitude)
#     return location.address





def get_distance(coord1: Tuple[float, float], coord2: Tuple[float, float]):
    return geopy.distance.vincenty(coord1. coord2).km

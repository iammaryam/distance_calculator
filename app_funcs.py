from math import *
from geopy.geocoders import Nominatim


def geo_coordinate(city):
    geo_locator = Nominatim(user_agent="app_name")
    location = geo_locator.geocode(city)
    return location.latitude, location.longitude


def distance(lat_long1, lat_long2, mnt_unit):
    earth_rad = 6371
    lat1, long1 = radians(lat_long1[0]), radians(lat_long1[1])
    lat2, long2 = radians(lat_long2[0]), radians(lat_long2[1])
    lat_minus = lat2 - lat1
    long_minus = long2 - long1
    lat_plus = lat2 + lat1

    a = sin(lat_minus / 2) ** 2
    b = sin(long_minus / 2) ** 2
    c = sin(lat_plus / 2) ** 2

    d = 2 * earth_rad * asin(sqrt(a + (1 - a - c) * b))

    if mnt_unit == "Kilometer (km)":
        return f"{d:.2f} km"
    elif mnt_unit == "Meter (m)":
        return f"{(d * 1000):.2f} m"
    else:
        return f"{(d / 1.609):.2f} mile"

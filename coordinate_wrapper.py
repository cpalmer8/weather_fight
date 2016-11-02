from geopy.geocoders import Nominatim
from decimal import *

def from_zipcode(zipcode):
    geolocator = Nominatim()
    location = geolocator.geocode(zipcode)
    coordinates = str(Decimal(location.latitude)), str(Decimal(location.longitude))
    return coordinates

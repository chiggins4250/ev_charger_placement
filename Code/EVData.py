#setting up a class to hold EV charger data
import pandas as pd
class EVData:
    """
    A simple class to hold data about EV chargers
    """
    def __init__(self):
        self.station_name = ""
        self.street_address_of_chargers = ""
        self.city_of_chargers = ""
        self.zip_of_chargers = ""
        self.state_of_chargers = ""
        self.latitude_of_chargers = -1
        self.longitude_of_chargers = -1
        self.id_of_chargers = ""
        self.latlong = ""

class VA_cities: #creates object to hold cities in Virginia
    def __init__(self, _state='', _city_name=''): #takes dataset that contains the state and city name
        self.state = _state
        self.city_name = _city_name
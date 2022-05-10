from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import pandas as pd
from EVData import EVData

# tell geolocator what language to use
geolocator = Nominatim(user_agent="Python")

# create a new file for the processed data
def generate_csv_file(filename):
    """
     A function to take a list of material strength results and print to a CSV file
     :param filename: The file that has source data
     :return: True if data was written out to the file successfully, false otherwise
     """
    # open the file
    file = open(filename)

    use_columns = ["Station Name", "Street Address", "City", "State", "ZIP Code", "Latitude", "Longitude", "ID"]
    data = pd.read_csv(file, header=0, usecols=use_columns)

    # for each entry, create a new EV Data object
    new_data = EVData()
    new_data.station_name = data["Station Name"].tolist()
    new_data.street_address_of_chargers = data["Street Address"].tolist()
    new_data.city_of_chargers = data["City"].tolist()
    new_data.state_of_chargers = data["State"].tolist()
    new_data.zip_of_chargers = data["ZIP Code"].tolist()
    new_data.latitude_of_chargers = data["Latitude"].tolist()
    new_data.longitude_of_chargers = data["Longitude"].tolist()
    new_data.id_of_chargers = data["ID"].tolist()

    return new_data

def find_distance(m,n):
    '''
    finds shortest driving distance between two places using google maps
    :param m: origin destination (lat, long)
    :param n: final destination (lat, long)
    :return: geodesic distance between two geographical points (km)
    '''
    distance = geodesic(m, n)
    return distance

if __name__ == "__main__":

    # get data
    path = '../Files/publicEVL2_dec2021.csv'
    ev_charger_data = generate_csv_file(path)

    # create lists to hold the data
    lat = ev_charger_data.latitude_of_chargers
    long = ev_charger_data.longitude_of_chargers

    # create a list of long, lat pairs that can be used to find distance
    something_else = zip(lat, long)
    lat_long = []
    for (latitude, longitude) in something_else:
        complete_address = str(latitude) + ", " + str(longitude)
        lat_long.append(complete_address)
    ev_charger_data.latlong = lat_long  # make an object in class for lat,long pairs

    # create empty lists for the desired data outputs
    no_neighbors = []
    charger_distances = []

    # create for loop to find locations that don't have chargers nearby and identify the ones that do
    n = 0
    for x in ev_charger_data.latlong:  # loops through all the current locations of chargers
        number_of_neighbors = False
        distance_o = []
        for j in ev_charger_data.latlong:  # loops through list again to create matrix
            if x == j:  # does not calculate anything if it is the same station
                continue
            else:
                distance = find_distance(x, j)  # calculates distance between each charger
                distance_o.append(distance)
                if distance < 20:  # asks if the distance is less than 20 km
                    number_of_neighbors = True
                    break
                else:
                    closest_dist = min(distance_o)
                    continue
        if number_of_neighbors == False:  # if no close chargers, location identifies gap in chargers
            charger_distances.append(closest_dist)
            charger_info = str(ev_charger_data.station_name[n]) + " located at " + \
                           str(ev_charger_data.street_address_of_chargers[n]) + ", " + \
                           str(ev_charger_data.city_of_chargers[n]) + ", VA"
            no_neighbors.append(charger_info)  # appends that location to list with no neighbors
        n += 1

    print("The locations that don't have another EV charger within 20 km are: " + str(no_neighbors))
    print(charger_distances)
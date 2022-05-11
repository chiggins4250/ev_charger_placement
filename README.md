# EV Charger Placement in Virginia for Residential Vehicles
The purpose of this analysis is to inform decision making on EV charger placement in Virginia for Level 2 and DC fast chargers. Some important questions to consider are:
1. Where are their gaps in the current placement of the chargers?
2. What are some potential locations that are less than 1 mile from a main road?
3. How can the placement of the EV chargers also serve those in disadvantaged commmunities?
This code preliminarily aims to address the first question but can be further improved upon to expand its capabilities.

# Contributors
Melanie Blatt<br/>
Collette Higgins

# Required Packages
Pandas<br/>
Geopy

# Main Programs
DCFast_charger_loc.py<br/>
Level2_charger_loc.py<br/>
EVData.py

# How to use
Step 1: Find data set to operate on that includes the adresses, latitude and longitude, ID and names of chargers and uses the column header names of "Station Name", "Street Address", "City", "State", "Zip Code", "Latitude", "Longitude", and "ID"<br/>
Step 2: Ensure the path file in either DCFast_charger_loc or Level2_charger_loc is set up to read the fie with the charger locations you are looking to analyze and compare<br/>
Step 3: Run the code

# Results
File will output a print statement that contains the names and loactions of each charger that is not within the specified threshold distance (set to 20km) to any of the other existing chargers. The distance of each of those chargers to the next closest charger is also printed in km. 

# Limitations
This project uses geodesic distance which calculates the direct path between two places not the traveling distance using roadways. Additionally, the current file parsing requres the data to have the exact column names listed. 

# Future Work
This can be further expanded to then look at more areas in Virginia not near any current chargers, possibly using a list of discrete latitudes and longitudes throughout the state. This analysis can also be combined with subsequent filters such as distance from major roadways of ptential locations as well as finding and weighting various demographic data. 

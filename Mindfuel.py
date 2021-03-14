import folium
import os
import json
import requests
import pandas as pd
import folium.plugins as plugins
import csv

# CO2 emission in kg/gallon constant
emission = 19.6

# model and make (inputted when signing in)
make = 'Aston Martin'
model = 'Lagonda'

with open('database.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        if (row["Make"] == make) & (row["Model"] == model):
            # create map
            map = folium.Map(location=[49.242371, -123.134354], zoom_start=14.1, tiles='Stamen Terrain')

            tooltip='Click for more info'

            miles_travelled = 3.51
            
            carbon_emission = round((emission * miles_travelled / int(row["Combined MPG (FT1)"])) * 0.453592, 2)
            
            # geojson data
            overlay = os.path.join('data', 'map.geojson')

            # add markers
            folium.Marker([49.246686, -123.177293],
                          popup='Estimated Carbon Emission: ' + str(carbon_emission) + 'kg',
                          tooltip='Destination',
                          icon=folium.Icon(color='green', icon='leaf')).add_to(map)
            folium.Marker([49.243060, -123.115028],
                          tooltip='This is you',
                          icon=folium.Icon(color='green', icon='leaf')).add_to(map)
                          
            folium.GeoJson(overlay, name='Shortest Route').add_to(map)

            # save map
            map.save('map.html')

            break

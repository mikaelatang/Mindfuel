import json
import requests
import pandas as pd
import folium.plugins as plugins
import csv

# CO2 emission in lb/gallon constant
emission = 19.6

# model and make (inputted when signing in)
make = 'Aston Martin'
model = 'Lagonda'

with open('database.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        if (row["Make"] == make) & (row["Model"] == model):
            # create map
            map = folium.Map(location=[43.757249, -79.422801], zoom_start=16, tiles='Stamen Terrain')

            tooltip='Click for more info'

            miles_travelled = 1.06
            
            carbon_emission = round((emission * miles_travelled / int(row["Combined MPG (FT1)"])) * 0.453592, 2)
            
            # geojson data
            overlay = os.path.join('data', 'map.geojson')

            # add markers
            folium.Marker([43.756859, -79.430802],
                          popup='Estimated Carbon Emission: ' + str(carbon_emission) + 'kg',
                          tooltip='Destination',
                          icon=folium.Icon(color='green', icon='leaf')).add_to(map)
            folium.Marker([43.757416, -79.413744],
                          tooltip='You are here',
                          icon=folium.Icon(color='green', icon='leaf')).add_to(map)
                          
            folium.GeoJson(overlay, name='Shortest Route').add_to(map)

            # save map
            map.save('map.html')

            break

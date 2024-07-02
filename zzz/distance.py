import requests
import pandas as pd

API_key = "AIzaSyBdZqFGjwbO0op2NTHw0axO0AVNz6wnftI"

origins = [
    {"name": "Orchard Collegiate Academy - [HS] 01M292", "lat": 40.713446, "lng": -73.986033},
    {"name": "University Neighborhood High School - [HS] 01M448", "lat": 40.7121857, "lng": -73.9842031},
    {"name": "East Side Community School - [HS] 01M450", "lat": 40.7291086, "lng": -73.9825277},
  
]
destinations = [
    {'name': 'Bay 50 St', 'lat': 40.588841, 'lng': -73.983765, 'routes': ['D']},
]
# turn 'Bay 50 St' into an array, same for lat, lng
# what does 'routes': ['D'] mean? 
# is destinations a list or a dictionary 
# fill out the stations and high schools non-manually, either from csv or from scraping code? 

# Convert the list of origins and destinations into the required format
origins_str = '|'.join([f"{origin['lat']},{origin['lng']}" for origin in origins])
destinations_str = '|'.join([f"{destination['lat']},{destination['lng']}" for destination in destinations])

# Construct the request URL
url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins_str}&destinations={destinations_str}&key={API_key}"

# Make the request
response = requests.get(url)
data = response.json()

def get_name_by_coordinates(coordinates, data_list):
    for item in data_list:
        if coordinates == f"{item['lat']},{item['lng']}":
            return item['name']
    return None

distance_matrix = []
duration_matrix = []
print(data)
# Populate the matrices
for i, row in enumerate(data['rows']):
    distance_row = []
    duration_row = []
    for j, element in enumerate(row['elements']):
        if element['status'] == 'OK':
            distance_row.append(element['distance']['text'])
            duration_row.append(element['duration']['text'])
        else:
            distance_row.append('N/A')
            duration_row.append('N/A')
    distance_matrix.append(distance_row)
    duration_matrix.append(duration_row)

# Create DataFrames for distances and durations
origin_names = [origin['name'] for origin in origins]
destination_names = [destination['name'] for destination in destinations]

df_distances = pd.DataFrame(distance_matrix, index=origin_names, columns=destination_names)
df_durations = pd.DataFrame(duration_matrix, index=origin_names, columns=destination_names)

# Display the matrices
print("Distance Matrix:")
print(df_distances)
print("\nDuration Matrix:")
print(df_durations)

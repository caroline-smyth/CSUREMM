import requests
import pandas as pd
import time

API_key = "AIzaSyBdZqFGjwbO0op2NTHw0axO0AVNz6wnftI"

origins = [{"name": "Forest Hills-71 Av", "lat": 40.721691, "lng": -73.844521}, {"name": "67 Av", "lat": 40.726523, "lng": -73.852719}, {"name": "63 Dr-Rego Park", "lat": 40.729846, "lng": -73.861604}, {"name": "Woodhaven Blvd and 59th Av", "lat": 40.733106, "lng": -73.869229}, {"name": "Grand Av-Newtown", "lat": 40.737015, "lng": -73.877223}, {"name": "Elmhurst Av", "lat": 40.742454, "lng": -73.882017}, {"name": "Jackson Hts-Roosevelt Av", "lat": 40.746644, "lng": -73.891338}, {"name": "65 St", "lat": 40.749669, "lng": -73.898453}, {"name": "Northern Blvd", "lat": 40.752885, "lng": -73.906006}, {"name": "46 St", "lat": 40.756312, "lng": -73.913333}, {"name": "Steinway St", "lat": 40.756879, "lng": -73.92074}, {"name": "36 St", "lat": 40.752039, "lng": -73.928781}, {"name": "Queens Plaza", "lat": 40.748973, "lng": -73.937243}, {"name": "Court Sq-23 St", "lat": 40.747846, "lng": -73.946}, {"name": "Lexington Av/53 St", "lat": 40.757552, "lng": -73.969055}, {"name": "5 Av/53 St", "lat": 40.760167, "lng": -73.975224}, {"name": "47-50 Sts-Rockefeller Ctr", "lat": 40.758663, "lng": -73.981329}, {"name": "42 St-Bryant Pk", "lat": 40.754222, "lng": -73.984569}, {"name": "34 St-Herald Sq", "lat": 40.749719, "lng": -73.987823}, {"name": "23 St and 6th Av", "lat": 40.742878, "lng": -73.992821}, {"name": "14 St and 6 Av", "lat": 40.738027, "lng": -73.998205}, {"name": "W 4 St-Wash Sq", "lat": 40.732338, "lng": -74.000495}, {"name": "Broadway-Lafayette St", "lat": 40.725297, "lng": -73.996204}, {"name": "Delancey St-Essex St", "lat": 40.718611, "lng": -73.988114}, {"name": "Marcy Av", "lat": 40.708359, "lng": -73.957757}, {"name": "Hewes St", "lat": 40.70687, "lng": -73.953431}, {"name": "Lorimer St and Broadway", "lat": 40.703869, "lng": -73.947408}, {"name": "Flushing Av and Broadway", "lat": 40.70026, "lng": -73.941126}, {"name": "Myrtle Av", "lat": 40.697207, "lng": -73.935657}, {"name": "Central Av", "lat": 40.697857, "lng": -73.927397}, {"name": "Knickerbocker Av", "lat": 40.698664, "lng": -73.919711}, {"name": "Myrtle-Wyckoff Avs", "lat": 40.69943, "lng": -73.912385}, {"name": "Seneca Av", "lat": 40.702762, "lng": -73.90774}, {"name": "Forest Av", "lat": 40.704423, "lng": -73.903077}, {"name": "Fresh Pond Rd", "lat": 40.706186, "lng": -73.895877}, {"name": "Middle Village-Metropolitan Av", "lat": 40.711396, "lng": -73.889601}]

def create_batch(arr, batch_size):
    for i in range(0, len(arr), batch_size):
        yield arr[i:i + batch_size]
        
        
def get_distances(origins):
    
    for count, origin in enumerate(origins):
        if(count!=len(origins)-1):
            
            origin_str =f"{origin['lat']},{origin['lng']}"
            #print("origin: ", origin_str)
            
            
            dest = origins[count+1]
            #print("Destination: ", dest)
            
            destination_str = f"{dest['lat']},{dest['lng']}"
            #print("destination coord: ", destination_str)
        
            url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin_str}&destinations={destination_str}&mode=subway&key={API_key}"

            # Make the request
            response = requests.get(url)
            data = response.json()
            print(data,",")
            # time.sleep(2)

get_distances(origins)

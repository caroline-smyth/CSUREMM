import json

def main():

  # replace this with array from sorted_stops_by_route

  array = [{'name': 'South Ferry', 'lat': 40.702068, 'lng': -74.013664, 'duration': 1500}, {'name': 'St George', 'lat': 40.643748, 'lng': -74.073643, 'duration': 480}, {'name': 'Tompkinsville', 'lat': 40.636949, 'lng': -74.074835, 'duration': 301},  {'name': 'Stapleton', 'lat': 40.627915, 'lng': -74.075162, 'duration': 169}, {'name': 'Clifton', 'lat': 40.621319, 'lng': -74.071402, 'duration': 396}, {'name': 'Grasmere', 'lat': 40.603117, 'lng': -74.084087, 'duration': 262}, {'name': 'Old Town', 'lat': 40.596612, 'lng': -74.087368, 'duration': 235}, {"name": "Dongan Hills", "lat": 40.588849, "lng": -74.09609, 'duration': 235}, {"name": "Jefferson Av", "lat": 40.583591, "lng": -74.103338, 'duration': 165}, {"name": "Grant City", "lat": 40.578965, "lng": -74.109704, 'duration': 154}, {"name": "New Dorp", "lat": 40.57348, "lng": -74.11721, 'duration': 264}, {"name": "Oakwood Heights", "lat": 40.56511, "lng": -74.12632, 'duration': 180}, {"name": "Bay Terrace", "lat": 40.5564, "lng": -74.136907, 'duration': 120},{'name': 'Great Kills', 'lat': 40.551231, 'lng': -74.151399, 'duration': 320}, {'name': 'Eltingville', 'lat': 40.544601, 'lng': -74.16457, 'duration': 320}, {'name': 'Annadale', 'lat': 40.54046, 'lng': -74.178217, 'duration': 250}, {'name': 'Huguenot', 'lat': 40.533674, 'lng': -74.191794, 'duration': 269}, {'name': "Prince's Bay", 'lat': 40.525507, 'lng': -74.200064, 'duration': 330}, {'name': 'Pleasant Plains', 'lat': 40.52241, 'lng': -74.217847, 'duration': 156}, {'name': 'Richmond Valley', 'lat': 40.519631, 'lng': -74.229141, 'duration': 176}, {'name': 'Arthur Kill', 'lat': 40.516578, 'lng': -74.242096, 'duration': 285}, {'name': 'Tottenville', 'lat': 40.512764, 'lng': -74.251961, 'duration': 1992}]

  filename = f"C:/Users/carol/OneDrive/Desktop/CSUREMM/sir_formatted.txt"
  with open(filename, 'r', encoding='utf-8-sig') as f:
    file_content = f.readlines()  

  i = 0
  j = 1
  modified = []
  for line in file_content:
      line = line.strip()
      if line:
        try:
          data = json.loads(line)
          data["origin"] = array[i % len(array)]["name"]
          data["destination"] = array[j % len(array)]["name"]
          modified.append(json.dumps(data))
          i += 1
          j += 1
        except json.JSONDecodeError as e:
          print(f"Failed to decode JSON: {e}")
  i=0
  with open("mapping_output.txt", 'w', encoding='utf-8-sig') as f:
    f.writelines(modified)

  f.close()
  print("Success! Check mapping_output.txt")

if __name__ == "__main__": 
  main()
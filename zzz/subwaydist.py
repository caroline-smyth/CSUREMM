import json

def main():
    filename = f"C:/Users/carol/Downloads/hs_subway_distances_output.txt"
    with open(filename, "r", encoding="utf-8"):
        file_content = filename.read()  
    
    i=0
    
    for origin in d["origin_addresses"]:
        j=0
        for destination in d["destination_addresses"]:
            measure_dict = (d["rows"][i])["elements"][j]
            #print(measure_dict)
            new_dict = {"origin":origin, "destination":destination, "distance": measure_dict["distance"], "duration": measure_dict["duration"],}
            print(new_dict)
            j+=1
        
        i+=1

            
if __name__ == "__main__":
    main()


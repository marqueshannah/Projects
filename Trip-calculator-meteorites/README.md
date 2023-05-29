# The return of JSON
The python script "generate_sites.py" creates a dictionary which contains data points of the meteorites' landing sites. It generates 5 different datas of 5 different meteorites and outputs it in the JSON file called "hw2landingsites.json." 

The python script "calculate_trip.py" transforms the Json file into a dictionary in order to read and use the information stored in the file. Next, the program uses a pre established constant to calculate the time travel from the initial site to the meteorite site, total travel time, the amount of time to collect the samples, number of legs, and total time elapsed from all samples. 

# "generate_sites.py"

The function generate_random() generates a dictionary with random values of latitude ranging from 16.0 to 18.0, longitudes ranging from 82.0 to 84.0, and outputs a random generated composition for the metereiorites. Next, it outputs this dictionary into a JSON file called "hw2landingsites.json."

## def generate_random():
```
def generate_random():
    random_latitude = []
    random_longitude = []
    for i in range(1, 6):
        random_latitude.append(round(random.uniform(16.0, 18.0), 3))
        random_longitude.append(round(random.uniform(82.0, 84.0), 3))
    Meteorite = {
        'sites': [
            {
                'Site ID': 1,
                'Latitude': random_latitude[0],
                'Longitude': random_longitude[0],
                'Composition': generate_random_composition()
             },
            {
                'Site ID': 2,
                'Latitude': random_latitude[1],
                'Longitude': random_longitude[1],
                'Composition': generate_random_composition()
             },
            {
                'Site ID': 3,
                'Latitude': random_latitude[2],
                'Longitude': random_longitude[2],
                'Composition': generate_random_composition()
             },
            {
                'Site ID': 4,
                'Latitude': random_latitude[3],
                'Longitude': random_longitude[3],
                'Composition': generate_random_composition()
             },
            {
                'Site ID': 5,
                'Latitude': random_latitude[4],
                'Longitude': random_longitude[4],
                'Composition': generate_random_composition()
             }
        ]
    }

    with open('hw2landingsites.json', 'r+') as landing_sites:
        json.dump(Meteorite, landing_sites, indent=4) 
   ```
The generate_random_composition() function stores three different composition types into an array called "compositions," then it returns a random value fom this array.  
## def generate_random_composition():
``` 
def generate_random_composition():
    compositions = ["stony", "iron", "stony-iron"]
    return random.choice(compositions)
```
# "calculate_trip.py"

## def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float):
This function calculates the total distance to travel from (latitude_1, longitude_1) to (latitude_2, longitude_2)

```
def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map(math.radians, [latitude_1, longitude_1, latitude_2, longitude_2])
    d_sigma = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1 - lon2)))
    return mars_radius * d_sigma
 ```
 
 ## def calculate_trip(lat1: float, long1: float, lat2: float, long2: float):
 This function calculates the time of the trip based on the max velocity of the robot, which is 10 km per hour. 
 
 ```
 def calculate_trip(lat1: float, long1: float, lat2: float, long2: float):
    distance = calc_gcd(lat1, long1, lat2, long2)
    return distance / 10
```
## def main():
This function copies the information in the JSON file and stores it in a few variables. Then, it determines the sample collection time based on the composition. Next, it calculates the total travel time by adding the time of travel calculates in calculate_trip() to the sample time. It then calculates the total time elapsed for all of the trips togheter, and number of legs. Finally, it prints out all this information. 

```
def main():
    with open("hw2landingsites.json") as landing_sites_file:
        ls_data = json.load(landing_sites_file)

    count = 0
    leg = 0
    total_time_elapsed = 0

    for row in ls_data['sites']:
        site_id_value = ls_data['sites'][count]['Site ID']
        latitude_value = ls_data['sites'][count]['Latitude']
        longitude_value = ls_data['sites'][count]['Longitude']
        composition_value = ls_data['sites'][count]['Composition']
        count += 1

        if composition_value == 'stony':
            sample_time = 1
        elif composition_value == 'iron':
            sample_time = 2
        else:
            sample_time = 3
        lat1 = 16.0
        long1 = 82.0
        lat2 = latitude_value
        long2 = longitude_value

        travel_total = calculate_trip(lat1, long1, lat2, long2) + sample_time
        total_time_elapsed = total_time_elapsed + travel_total

        leg += 1

        print("leg = ", leg, ",", "time to travel = ", round(travel_total, 3), "hr",  ",", "time to sample = ", sample_time)

    print('===========================================================')
    print("number of legs = ", leg, ",", "total time elapsed = ", round(total_time_elapsed, 3), "hr")

```

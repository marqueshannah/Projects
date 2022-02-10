import json
import random


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


def generate_random_composition():
    compositions = ["stony", "iron", "stony-iron"]
    return random.choice(compositions)


if __name__ == '__main__':
    generate_random()

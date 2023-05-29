import json
import math

mars_radius = 3389.5


def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map(math.radians, [latitude_1, longitude_1, latitude_2, longitude_2])
    d_sigma = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1 - lon2)))
    return mars_radius * d_sigma


def calculate_trip(lat1: float, long1: float, lat2: float, long2: float):
    distance = calc_gcd(lat1, long1, lat2, long2)
    return distance / 10


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


if __name__ == '__main__':
    main()

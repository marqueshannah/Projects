#!/usr/bin/env python3
import json
from typing import List
import logging
import socket
import sys

format_str = f'[%(asctime)s {socket.gethostname()}] %(filename)s:%(funcName)s:\
            %(lineno)s - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.WARNING, format=format_str)


def compute_average_mass(a_list_of_dicts: List[dict], a_key_string: str) -> float:
    """
    Iterates through a list of dictionaries, pulling out values associated with
    a given key. Returns the average of those values.
    Args:
        a_list_of_dicts (list): A list of dictionaries, each dict should have the
                                same set of keys.
        a_key_string (string): A key that appears in each dictionary associated
                               with the desired value (will enforce float type).
    Returns:
        result (float): Average value.
    """
    if (len(a_list_of_dicts) == 0):
        logging.error('a_list_of_dicts is 0')

    total_mass = 0
    for item in a_list_of_dicts:
        total_mass += float(item[a_key_string])
    return (total_mass / len(a_list_of_dicts))


def check_hemisphere(latitude: float, longitude: float) -> str:
    """
    Given latitude and longitude in decimal notation, returns which hemispheres
    those coordinates land in.
    Args:
        latitude (float): Latitude in decimal notation.
        longitude (float): Longitude in decimal notation.
    Returns:
        location (string): Short string listing two hemispheres.
    """
    if (latitude == 0 or longitude == 0):
        # logging.error("you're not really in a hemisphere")
        raise (ValueError)
    location = 'Northern' if (latitude > 0) else 'Southern'
    location = f'{location} & Eastern' if (longitude > 0) else f'{location} & Western'
    return (location)


def count_class(a_list_of_dicts: List[dict], a_key_string: str) -> dict:
    """
    This function takes the input of a list of dicts, and a key string. It will
    iterate over the list and finds the value associated with the key. It will
    set the first instance to one, and increment every other time it finds it.
    Args:
        a_list_of_dicts (list[dict]): List of dictionaries
        a_key_string (str): String referring to key whose value I want to count

    Returns:
        classes_observed (dict): Dict of class counts
    """
    count_dict = {}
    for item in a_list_of_dicts:
        if item[a_key_string] in count_dict.keys():
            count_dict[item[a_key_string]] += 1
        else:
            count_dict[item[a_key_string]] = 1
    return (count_dict)
  
  def main():
    logging.debug('entering main loop')

    with open(sys.argv[1], 'r') as f:
        ml_data = json.load(f)

    logging.debug(f'the type of ml_data is{type(ml_data)}')

  
    NE, NW, SE, SW = 0, 0, 0, 0
    for row in ml_data['meteorite_landings']:
        location = check_hemisphere(float(row['reclat']), float(row['reclong']))
        if (location == 'Northern & Eastern'):
            NE += 1
        elif (location == 'Northern & Western'):
            NW += 1
        elif (location == 'Southern & Eastern'):
            SE += 1
        else:
            SW += 1

    meteorite_class = count_class(ml_data['meteorite_landings'], 'recclass')
    
    

    print("Summary data following meteorite analysis:")
    print()
    print("Average mass of", len(ml_data['meteorite_landings']), "meteor(s):")
    print(" ", compute_average_mass(ml_data['meteorite_landings'], 'mass (g)'), "grams")
    print()
    print("Hemisphere summary data:")
    print("  There were", NE, "meteors found in the Northern & Eastern quadrant.")
    print("  There were", NW, "meteors found in the Northern & Western quadrant.")
    print("  There were", SE, "meteors found in the Southern & Eastern quadrant.")
    print("  There were", SW, "meteors found in the Southern & Western quadrant.")
    print()
    print("Class summary data:")
    for item in meteorite_class:
        print("  The", item, "class was found", meteorite_class[item], "times.")
    print()


if __name__ == '__main__':
    main()

    

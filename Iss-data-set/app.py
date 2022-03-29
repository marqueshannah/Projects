from flask import Flask, jsonify
import requests, json
import xmltodict
from typing import List
import logging
import sys


app = Flask(__name__)
iss_positional_data = {}
iss_sighting_data = {}


@app.route('/', methods=['GET', 'POST'])
def instructions()->str:
    instruction_message = """
    Tracking the ISS 
    
    Routes on information and management:
    /                                                       (GET) prints info on each route available
    /data                                                   (POST) resets and loads data from files
    Routes for querying positional data:
    /epochs                                                 (GET) a list of all epochs in the data
    /epochs/<epoch_info>                                         (GET) all data of a specific <epoch>
    Routes for querying sighting data:
    
    /countries                                              (GET) a list of all countries in the data
    /countries/<country>                                    (GET) all data on the requested <country>
    /countries/<country>/regions                            (GET) a list of all regions in the given country
    /countries/<country>/regions/<region>                   (GET) all data on the requested <region>
    /countries/<country>/regions/<region>/cities            (GET) a list of all cities in the given region
    /countries/<country>/regions/<region>/cities/<city>     (GET) all data on the requested <city>
    """
    return instruction_message

@app.route('/data', methods=['GET'])
def read_data()->str:
    '''This function will collect the data from the xml files and parse them to a global variable 

        Args:  
            iss_postional_data (string):global variable for the file positional.xml
            iss_sighting_data(string): global variable for the file sighting.xml
        Returns:
             If the program sucessfully reads and parses the data to the variables, it will return a string indicating the success, else, it will return a
                string indicating that the file does not exist.
    '''
    
    global iss_positional_data
    global iss_sighting_data

    try:
        with open('positional.xml', 'r') as f:
            f_data = f.read()
            iss_positional_data = xmltodict.parse(f_data)


        with open('sighting.xml', 'r') as f2:
            f2_data = f2.read()
            iss_sighting_data = xmltodict.parse(f2_data)

        return f'Data has been read from file\n'
     
    except FileNotFoundError as no_file:
        logging.error(no_file)
        return 'File does not exist'

@app.route('/epochs', methods=['GET'])
def get_epochs():
    '''
     This function will display all of the epoch information for the user to see
     Returns:
        epochs (list) it will be list that contains all the epoch starting time. But to prevent
        errors from happening we are to use jsonify to turn the list into JSON data.
    '''
    logging.info('loading to get all epochs')
    
    epochs = []
    iss_positional = iss_positional_data['ndm']['oem']['body']['segment']['data']['stateVector']
  
    for item in iss_positional:
        epochs.append(item['EPOCH'])
    return json.dumps(epochs, indent=2)

@app.route('/epochs/<epoch>', methods=['GET'])
def get_detailed_epoch(epoch: str):
    '''
    This function will read specific epoch data from the file and add them to epoch_list (list) and return the list after transforming it into a json file.
  
    Args:
        A specified epoch (str value).
     Returns:
        A list of dictionaries with the imformation of the requested epoch.
    '''
    logging.debug('Have a specific epoch queried')
    epoch_list = {}
    all_data = ['X', 'Y', 'Z', 'X_DOT', 'Y_DOT', 'Z_DOT']
    for item in iss_positional_data['ndm']['oem']['body']['segment']['data']['stateVector']:
        if epoch == item['EPOCH']:
            epoch_location= item
            for i in all_data:
                epoch_list[i] = epoch_location
    return jsonify(epoch_list)

    
  

@app.route('/countries', methods=['GET'])
def get_countries():
    """
    This route gathers all countries from the sighting data.
    
    Returns:
        A list of all countries.
    """
    logging.info('loading to get all countries')
    global countries
    countries = []
    
    for item in iss_sighting_data['visible_passes']['visible_pass']:
        countries.append(item['country'])

    return jsonify(countries)

@app.route('/countries/<country>', methods=['GET'])
def get_country_info(country):
    """
    This route reads in a user input and finds the information on the specific country requested.
    Args:
        A specified country (str value).
    Reutrns:
        A list of dictionaries with information on the specified country.
    """
    country_dict = {}
    country_list = []
    country_data = ['country', 'region', 'city', 'spacecraft','sighting_date','duration_minutes','max_elevation','enters','exits','utc_offset','utc_time', 'utc_date']
    for item in iss_sighting_data['visible_passes']['visible_pass']:
        country_name = item['country']
        if country == country_name:
            country_place = item
            for data in country_data:
                country_dict[data] = country_place[data]
            country_list.append(country_dict)
    return jsonify(country_list)

@app.route('/countries/<country>/regions', methods=['GET'])
def regions(country):
     """
     This route gathers all regions within the given country.
    
     Args:
         The specified country queried from the previous route. (str value)
     Returns:
        A list of the regions.
     """
     logging.info("Querying route to get list of regions in /" + country)

     regions = {}

     for item in iss_sighting_data['visible_passes']['visible_pass']:
          if country == item['country']:
                 all_regions = item['region']
                 if all_regions in regions:
                     regions[all_regions] += 1
                 else:
                     regions[all_regions] = 1
     return regions

@app.route('/countries/<country>/regions/<region>', methods=['GET'])
def specificc_region(country: str, region: str):
    """
    This route reads in a user input and finds the information on the specific region requested.
    Args:
        The specified country queried from a previous route (str value).
        A specified region (str values).
    Reutrns:
        A list of dictionaries with information on specific information of the selected region.
    """
  
    data = regions(country)
    global specific_region

    specific_region = []
    logging.debug('Have a specific region queried')

    
    region_dictionary = {}
    region_list = []
    region_data = ['city', 'spacecraft', 'sighting_date','duration_minutes','max_elevation','enters', 'exits','utc_offset','utc_time', 'utc_date']    

    try:
        for item in iss_sighting_data['visible_passes']['visible_pass']:
            if country == item['country']:
                specific_region = item['region']
                if region == specific_region:
                    for data in region_data:
                        region_dictionary[data] = item[data]
                    region_list.append(region_dictionary) 
        return jsonify(specific_region)
           

    except NameError as e:
        logging.error(e)
        return 'This specific region was not found\n'

    

@app.route('/countries/<country>/regions/<region>/cities', methods=['GET'])
def cities(country: str, region: str):
    """
      This route gathers all cities within the given region.
     
      Args:
          The specified country queried from a previous route (str value).
          The specified region queried from the previous route (str value).
      Returns:
             A list of the cities.
    """
    
    cities_dict = {}

    try:
        for item in iss_sighting_data['visible_passes']['visible_pass']:
            if country == item['country']: 
                selected_region = item['region']
                if region == selected_region:
                    selected_cities = item['city']
                    if selected_cities in cities_dict:
                        cities_dict[selected_cities] += 1   
                    else:
                        cities_dict[selected_cities] = 1
    
        return jsonify(cities_dict)
    except NameError as e:
        logging.error(e)
        return 'This specific city was not found\n'

@app.route('/countries/<country>/regions/<region>/cities/<city>', methods=['GET'])
def specificCity(country: str, region: str, city: str):
    """
      This route reads in a user input and finds the information on the specific city requested.
      Args:
        The specified country queried from a previous route (str value).
        The specified region queried from a previous route (str value).
        A specified city (str value).
    
      Returns:
        A list of dictionaries with information on the specified region.
     """

    logging.debug('Have a specific city queried')

    city_dict = {} 
    city_list = []
    city_data = ['city','spacecraft','sighting_date','duration_minutes','max_elevation','enters','exits','utc_offset','utc_time','utc_date']

    try:
         for item in iss_sighting_data['visible_passes']['visible_pass']:
            if country == item['country']:
                specific_region = item['region']
                if region == specific_region:
                    specific_city = item['city']
                    if city == specific_city:
                        for data in city_data:
                            city_dict[data] = item[data]
                        city_list.append(city_dict)

         return jsonify(specific_city)
    except NameError as e:
        logging.error(e)
        return 'This selected city was not found\n'


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')

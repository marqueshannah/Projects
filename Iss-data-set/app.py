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
            iss_positional_data = xmltodict.parse(f.read())


        with open('sighting.xml', 'r') as f2:
            iss_sighting_data = xmltodict.parse(f2.read())

        return f'Data has been read from file\n'
        return iss_positional_data
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
    global country_list
    country_list = []
    for i in range(len(countries)):
        country_list.append(iss_sighting_data[i])
    
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

    for i in range(len(regions)):

        try:
            if region in regions[i]:
                specific_region.append(country_list[i])

        except NameError as e:
            logging.error(e)
            return 'This specific region was not found\n'

    return jsonify(specific_region)

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
     data = (country, region)
     global citiesList

     cities_list = []
     for i in range(len(specific_region)):
         current_dict = specific_region[i]
         cities_list.append(current_dict['city'])
    
     return jsonify(cities_list)
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
    data = cities(country, region)
    
    specific_city = []
    logging.debug('Have a specific city queried')

    for i in range(len(citiesList)):

        try:
            if city in citiesList[i]:
                specific_city.append(specific_region[i])

        except NameError as e:
            logging.error(e)
            return 'Requested city was not found\n'

    return jsonify(specific_city)


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')

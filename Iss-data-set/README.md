# ISS DATA

## Description:
We have found an abundance of positional data for the International Space Station (ISS). The goal is to build a containerized flask application for querying
and returning some information from the ISS data set.

## Files:
### app.py:

This script is a flask application for tracking ISS position and sightings.
loads in the two datasets, positional.xml and sighting.xml.
contains routes that return important, desired information.

### test_app.py:

makes sure each function in the script app.py has no errors and returns strings.

### Dockerfile:
containerizes the flask application and both datasets.

### Makefile:

written with targets to build a container and to start the containerized Flask application.
### How to perform the Download of the Datasets:
1. Log into ISP and connect through your terminal.
2. Access this link to download the files ```https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq```.
3. Under "Public Distribution File", right click XML and click Open link in new tab
4. Copy the URL and type in the command line: wget <xml link>
5. After downloading the positional data, now download specific sighting data by going to the same link.
6. Under "XMLsightingData_citiesINT02", right click XML and click Open link in new tab.
7.Copy the URL once again and type in the command line: wget <xml link>
  
### How to build a container:
  
Open your Dockerfile and type in:
```
FROM centos:7.9.2009

RUN yum update -y && \
    yum install -y python3

RUN pip3 install Flask==2.0.3 \
    	 	 pytest==7.0.0 \
		     xmltodict==0.12.0
 
COPY app.py /code/app.py
COPY test_app.py /code/test_app.py
COPY positional.xml /code/positional.xml
COPY sighting.xml /code/sighting.xml

WORKDIR /code/


CMD ["python3","/code/app.py"]
```
  
  
Next type into your command bar 
```
  docker build -t <username>/<file-name>:<name> .
```
Then type
  ```
  docker push <username>/<file-name>:<name>
  ```
 to push the image to the Docker repository.
 
  ### Using a pre-containarized copy.
  1. Type the command in: `docker pull <username>/<file-name>:<name>`
  
  ### Interacting with the application
  
  Run this to your command line
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run -p 5018
```
  
2. Open an additional terminal, do the log in process once more, and type the command: `curl localhost:5018/`

  The sample output should be:
  
 ```
ISS Sighting Location
/                                                      (GET) print this information
/data                                                  (POST) reset data, load from file
Routes for querying positional and velocity data:
/epochs                                                (GET) lists all epochs in positional and velocity data
/epochs/<epoch>                                        (GET) lists all data associated with a specific epoch
Routes for Querying Sighting Data
/countries                                             (GET) lists all countries in sighting data
/countries/<country>                                   (GET) lists all data for a specific country
/countries/<country>/regions                           (GET) lists all regions in a specific country
/countries/<country>/regions/<region>                  (GET) lists all data for a specific region
/countries/<country>/regions/<region>/cities           (GET) lists all cities in a specific region
/countries/<country>/regions/<region>/cities/<city>    (GET) lists all data for a specific city
```
## CITATIONS:
1. Goodwin, S. (n.d.). ISS_COORDS_2022-02-13. NASA. 
  [https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml]
  (https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml) 
  Retrieved March 29, 2022, from [https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq]
  (https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq).
2. Goodwin, S. (n.d.).XMLsightingData_citiesINT02. NASA. Retrieved March 29, 2022, from [https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesINT02.xml](https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesINT02.xml)

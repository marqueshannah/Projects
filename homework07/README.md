# API Diagrams

## What is the functionality of a flowchart?

Flowcharts are often used in a way to organize an application into an image where both developers and users can understand the functionality of the software. It unfolds all the options and paths within the application as a guidance. It also contains explanations of what each option does and where to find them.

## ISS API Flowchart
This flowchart is based on the ISS data set application that can be found [here](https://github.com/marqueshannah/my-coe332-hws/tree/main/Iss-data-set) and how to interact with it. 

![alt text](https://github.com/marqueshannah/my-coe332-hws/blob/main/homework07/flowchart%20API.png)

In this flowchart, oval shapes indicate start/end; Squares indicates a process or output being performed; Paralellograms indicates the program takes an user input. Each color indicates a different layer within the application. 

1. First, the application starts by reading the data from the files and expects an input from the user. 
2. Once gotten an input, the application will output or perform different functionalities. 
Some selections can lead to several other possible selections to obtain data from. For instance, within "/countries" you can obtain a list of countries and select an specific one to get data. 

Within countries you can obtain all these information:
~~~
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
~~~

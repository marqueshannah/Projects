# Containers: Meteorite Landing Tracker and Analysis 
This repository contains the files to analyze the Meteorite information inside a JSON file, then, output some calculations of average mass, and summary datas. 

## ml_data_analysis.py
This python script acquires data from the "Meteorite_Landings.json" file. 
### "compute_average_mass(a_list_of_dicts: List[dict], a_key_string: str)"
This function will calculate and retrun the average mass based on the mass of all meteorites in the file. The function will output a logging message if the number of dictionaries is 0.

### "check_hemisphere(latitude: float, longitude: float)"
This function will determine which hemisfere the meteorite landed in based on its latitude and longitude.
### "def count_class(a_list_of_dicts: List[dict], a_key_string: str)" 
This function counts how many times each class was found in the dictionaries. 

## test_ml_data_analysis.py 
This script does some unit testing in the file "ml_data_analysis." To properly run this test, installation of pytest is needed. 

## Dockerfile
This file contains the information needed to create a container that successfully runs this code.

## How To Run This Code:
open your terminal, do the necessary log in procedures, and type the following commands to pull the existing image.
``` 
docker pull hannahmarques/ml_data_analysis:hw04
docker run --rm -it hannahmarques/ml_data_analysis:1.0 /bin/bash
cd /code
ml_data_analysis.py Meteorite_Landings.json

```
## Output sample:

```
Summary data following meteorite analysis:

Average mass of 30 meteor(s):
  83857.3 grams

Hemisphere summary data:
  There were 21 meteors found in the Northern & Eastern quadrant.
  There were 6 meteors found in the Northern & Western quadrant.
  There were 0 meteors found in the Southern & Eastern quadrant.
  There were 3 meteors found in the Southern & Western quadrant.

Class summary data:
  The L5 class was found 1 times.
  The H6 class was found 1 times.
  The EH4 class was found 2 times.
  The Acapulcoite class was found 1 times.
  The L6 class was found 6 times.
  The LL3-6 class was found 1 times.
  The H5 class was found 3 times.
  The L class was found 2 times.
  The Diogenite-pm class was found 1 times.
  The Stone-uncl class was found 1 times.
  The H4 class was found 2 times.
  The H class was found 1 times.
  The Iron-IVA class was found 1 times.
  The CR2-an class was found 1 times.
  The LL5 class was found 2 times.
  The CI1 class was found 1 times.
  The L/LL4 class was found 1 times.
  The Eucrite-mmict class was found 1 times.
  The CV3 class was found 1 times.
  ```


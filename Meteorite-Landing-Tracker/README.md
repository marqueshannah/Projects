# Meteorite Landing Tracker and Analysis

This repository contains the necessary files to run an application for analyzing meteorite information from a JSON dataset. The application calculates the average mass of meteorites and provides summary data.

## ml_data_analysis.py

The `ml_data_analysis.py` script is responsible for acquiring data from the "Meteorite_Landings.json" file and performing various calculations and analysis. It includes the following functions:

### `compute_average_mass(a_list_of_dicts: List[dict], a_key_string: str)`

This function calculates and returns the average mass of all meteorites in the dataset. If the number of dictionaries is 0, a logging message will be displayed.

### `check_hemisphere(latitude: float, longitude: float)`

This function determines the hemisphere in which a meteorite landed based on its latitude and longitude.

### `count_class(a_list_of_dicts: List[dict], a_key_string: str)`

This function counts the occurrences of each class in the dataset dictionaries.

## test_ml_data_analysis.py

The `test_ml_data_analysis.py` script contains unit tests for the `ml_data_analysis.py` file. To run these tests, you need to have `pytest` installed.

## Dockerfile

The Dockerfile in this repository provides instructions to create a container that can successfully run this code.

## How to Run This Code

To run the application, follow these steps:

1. Open your terminal and perform the necessary login procedures.
2. Pull the existing Docker image using the following commands:

```bash
docker pull hannahmarques/ml_data_analysis:hw04
docker run --rm -it hannahmarques/ml_data_analysis:1.0 /bin/bash


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


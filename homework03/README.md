# Mars Lab Water Safety
##Overview
This program determines the safety of the water based on data colected from a dictionary from five samples within it. Then, it calculates the water turbidity, 
to determine if it is safe to use for analyzing meteorite samples. Next, it calculates the other calculating the minimum time required time to reach below the safety threshold.


## How To Download The Data Set:
to run this program, you will need to copy and paste the data from this file and paste it into a json file. 
```
https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
```

## calculate_water.py
This python script reads and transform the data from turbidity_data.json into values and uses this information to calculate the turbidity of water at "calculate_turbidity," deciding if
if it is safe or not. Then in "minimum_time_threshold," data points are then calculated and evaluated to see if the water is safe to use if it is less than the 1 NTU. If not,
the program then calculates the minimum time required for the turbidity to decay to a safe level and returns this value.


## test_water.py
This python script is a unit test for calculate_water.py, it checks the most of the common cases and errors for the functions inside the script.

## Output 
This program should have an output similiar as this:

```
Average turbidity based on most recent five measurements = 1.1992 NTU
Warning: Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 8.99 hours
```
```

Average turbidity based on most recent five measurements = 0.9852 NTU
Info: Turbidity is below threshold for safe use
Minimum time required to return below a safe threshold = 0 hours
```

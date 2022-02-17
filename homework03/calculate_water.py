import json
import logging
import math
import random
from typing import List

logging.basicConfig(level=logging.INFO)
# percentage per hour
DECAY_FACTOR = 0.02
# in NTU
TURBIDITY_THRESHOLD = 1.0

def calculate_turbidity(a0: float, I90: float) -> float:
    """
    this function calculates average turbidity of water.
        T which refers to Turbidity = a0 which refers to calibration constant x detector current.
       Args:
            T: Turbidity
            a0: calibration constant
            I90: detector current
       Returns:
           A float number that equals the average turbidity of water
       """
    T = a0 * I90
    return T


def minimum_time_threshold(current_turbidity):
    """
    This function calculates the required time before turbidity decays to safe level.
    It decides whether the current value of turbidity is less than the turbidity constant for safety,
    and returns the values accordingly.

    Args:
        current_turbidity: A float representing the current turbidity of the water.
    returns:
         float representing the minimum time needed for the water turbidity to decay to a safe level.
    """
    if current_turbidity <= TURBIDITY_THRESHOLD:
        return 0.0
    else:
        return math.log(TURBIDITY_THRESHOLD / current_turbidity) / math.log(1 - DECAY_FACTOR)


def main():
    with open('turbidity_data.json', 'r') as turbidity_info:
        turb_info = json.load(turbidity_info)
        recent = turb_info['turbidity_data'][-5:]

        calibration_constant = []
        detector_current = []

    for i in range(len(recent)):
        calibration_constant.append(recent[i]['calibration_constant'])
        detector_current.append(recent[i]['detector_current'])
    calibration_average = sum(calibration_constant) / len(calibration_constant)
    detector_average = sum(detector_current) / len(calibration_constant)

    turbidity_totals = calculate_turbidity(calibration_average, detector_average)
    print("Average turbidity based on most recent five measurements = ",
          round(turbidity_totals, 3), "NTU")

    if turbidity_totals < TURBIDITY_THRESHOLD:
        logging.info('Info: Turbidity is below threshold for safe use')
    else:
        logging.warning("Turbidity is above threshold for safe use")

    print("Minimum time required to return below a safe threshold = ", round(minimum_time_threshold(turbidity_totals), 3), "hours")
    print("=============================================================")


if __name__ == '__main__':
    main()

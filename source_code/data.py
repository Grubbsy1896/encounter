# March 31st 2021
# This file, data.py, is responsible for loading data for the
# EnCounter

import os
import sys
import json



global ROOT_DIR
global filepath
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = f"{ROOT_DIR}/data/encounters.json"

# Loading Data
def load_data():
    global filepath
    with open(filepath, 'r') as datafile:
        ecs = json.load(datafile)

        if ecs == {} or len(ecs) < 1:
            ecs['Route 1'] = {
                "Ratatta": 0,
                "Pidgey": 0
            }
            ecs['global'] = {
                "total_encounters": 0
            }

        return ecs

# Saving Data
def save_data(jsawn):
    global filepath
    with open(filepath, 'w') as datafile:
        json.dump(jsawn, datafile, indent=4)


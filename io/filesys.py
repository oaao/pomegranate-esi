import json
import time
from os import path

base_dir = path.dirname(path.realpath('__file__'))


def write_json(data_input, ind):
    with open(path.join('json', "orderbook_" + str(round(time.time(), 4)) + ".txt"), "w") as f_output:
        json.dump(data_input, f_output, indent=4)

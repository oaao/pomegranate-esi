import json
import time
from os import path

base_dir = path.dirname(path.realpath('__file__'))


def write_json(data_input, name, indent=None):
    with open(path.join('{}_json{}.txt'.format(name, int(time.time()))), "w") as f_output:
        json.dump(data_input, f_output, indent=indent)

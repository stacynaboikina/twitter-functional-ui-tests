from bunch import bunchify
import json


def get_obj_from_config(config_file_path):
    with open(config_file_path, "r+") as user_config_file:
        configs = json.loads(user_config_file.read())
        return bunchify(configs)

import json


def get_config() -> dict:
    with open("../config.json", "r") as config:
        return json.load(config)

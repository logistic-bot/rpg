# pylint: disable=C0103

"""This file loads configurations options for the whole game. Change the path below to load a
custom config. """

import json
from pathlib import Path

CONFIG_PATH = Path("~/.config/rpg.json").expanduser().resolve()


def _load_config(path) -> dict:
    with open(path, "r") as file:
        return json.load(file)


def _save_config(config_object, path) -> None:
    with open(path, "w") as file:
        json.dump(config_object, file)


def save():
    _save_config(config, CONFIG_PATH)


config = {}
config.update(_load_config(CONFIG_PATH))

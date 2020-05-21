#!/usr/bin/env python

"""
Main.
"""

from src.core.utils.slowinput import slowinput
from src.core.utils.slowprint import slowprint

from src.config import config, save
assert isinstance(config["fastprint"], bool)

slowprint("Please choose a name for your character.", end_interval=0, fast=config["fastprint"],
          by_word=True, interval=0.03)
slowprint('It will be used like this: "Hello `<name>`, how are you?"', fast=config["fastprint"],
          end_interval=0, by_word=True, interval=0.03)
slowprint("You can use your real name, or invent one!", fast=config["fastprint"], by_word=True,
          interval=0.03, end_interval=0)
config["user"]["name"] = slowinput("name> ", fast=config["fastprint"])
save()

print()
print()
slowprint("----------------------------------------", fast=config["fastprint"], interval=0.01,
          end_interval=0)
print()
print()

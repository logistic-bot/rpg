"""
This file implements the Event class
"""

from dataclasses import dataclass


@dataclass
class Event:
    """
    This class models an event.

    An event has a type, which is used to differentiate from different actions that needs to be
    taken, and data, which can be any object.
    """
    type: str
    data: object

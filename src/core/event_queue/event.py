from dataclasses import dataclass


@dataclass
class Event:
    type: str
    data: object

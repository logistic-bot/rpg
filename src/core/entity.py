"""
This file implements the entity class.
"""

from src.core.event_queue.event import Event
from src.core.event_queue.event_queue import EventQueue


class Entity:
    """
    This class is the base class for all game objects.
    """
    def __init__(self) -> None:
        self.event_queue = EventQueue()

    def recive(self) -> Event:
        """
        Recive the next event from the queue, and return it.
        :return: the next event from the queue.
        """
        return self.event_queue.pop()

    def send(self, message: Event) -> None:
        """
        Send an event to the event queue.

        :param message: The event to send
        :return: None
        """
        self.event_queue.append(message)

"""
This file implements the EventQueue class.
"""

from typing import List

from src.core.event_queue.event import Event


class EventQueue:
    """
    This class is an implementation of an event queue as described here:
    http://gameprogrammingpatterns.com/event-queue.html
    """

    def __init__(self) -> None:
        self.events: List[Event] = []

    def append(self, event: Event) -> None:
        """
        Add an event to the queue.
        :param event: The event to add
        :return: None
        """
        self.events.append(event)

    def pop(self) -> Event:
        """
        Get the next event from the queue, and remove it from the queue.

        :return: The next event.
        """
        return self.events[0]

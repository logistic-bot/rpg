"""
This file implements the EventQueue class.
"""


class EventQueue:
    """
    This class is an implementation of an event queue as described here:
    http://gameprogrammingpatterns.com/event-queue.html
    """

    def __init__(self):
        self.events = []

    def append(self, event):
        self.events.append(event)

    def pop(self):
        return self.events[0]

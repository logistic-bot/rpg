"""
This file implements the component class.
"""
from src.core.entity import Entity
from src.core.event_queue.event import Event


class Component:
    """
    This is the core class for all game components. All other components must inherit from it.

    All game objects will have one or more components depending on their functions.
    """
    def __init__(self, entity: Entity) -> None:
        self.entity = entity

    def receive(self) -> Event:
        """
        Receive the next message from the entity's event queue, and return it.

        :return: The next message
        """
        return self.entity.recive()

    def send(self, message: Event) -> None:
        """
        Send a message to the entiry's event queue.
        :param message:
        :return:
        """
        self.entity.send(message)

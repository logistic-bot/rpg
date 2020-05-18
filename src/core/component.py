from src.core.event_queue import EventQueue


class Component:
    def __init__(self, event_queue: EventQueue) -> None:
        self.event_queue = event_queue

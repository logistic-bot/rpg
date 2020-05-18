import pytest
from hypothesis.stateful import RuleBasedStateMachine, rule, precondition, invariant
from hypothesis.strategies import text

from src.core.event_queue.event import Event
from src.core.event_queue.event_queue import EventQueue


class EventQueueTester(RuleBasedStateMachine):
    def __init__(self):
        super(EventQueueTester, self).__init__()
        self.queue = EventQueue()

    @invariant()
    def events_is_list(self):
        assert isinstance(self.queue.events, list)

    @invariant()
    def events_contains_events(self):
        for event in self.queue.events:
            assert isinstance(event, Event)

    @rule()
    def reset(self):
        self.queue = EventQueue()

    @rule(id=text(), data=text())
    def append(self, id, data):
        event = Event(id, data)
        self.queue.append(event)
        assert self.queue.events[-1] == event

    def precond_queue_not_empty(self):
        return len(self.queue.events) > 0

    def precond_queue_empty(self):
        return not self.precond_queue_not_empty()

    @rule()
    @precondition(precond_queue_not_empty)
    def pop(self):
        event = self.queue.events[0]
        event2 = self.queue.pop()
        assert event2 == event

    @rule()
    @precondition(precond_queue_empty)
    def pop_empty(self):
        with pytest.raises(IndexError):
            self.queue.pop()

TestEventQueue = EventQueueTester.TestCase

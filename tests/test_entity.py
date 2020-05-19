from hypothesis.stateful import RuleBasedStateMachine, rule, invariant, precondition
from hypothesis.strategies import text

from src.core.entity import Entity
from src.core.event_queue.event import Event
from src.core.event_queue.event_queue import EventQueue


class EntityTester(RuleBasedStateMachine):
    def __init__(self):
        super(EntityTester, self).__init__()
        self.e = Entity()

    @invariant()
    def event_queue(self):
        assert isinstance(self.e.event_queue, EventQueue)

    def precond_queue_not_empty(self):
        return len(self.e.event_queue.events) > 0

    @rule()
    @precondition(precond_queue_not_empty)
    def receive(self):
        event = self.e.event_queue.pop()
        assert event == self.e.recive()

    @rule(s=text(), o=text())
    def send(self, s, o):
        event = Event(s, o)
        self.e.send(event)
        assert self.e.event_queue.events[-1] == event

    @rule()
    def reset(self):
        self.e = Entity()


TestEntity = EntityTester.TestCase

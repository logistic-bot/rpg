from hypothesis.stateful import RuleBasedStateMachine, rule, invariant, precondition
from hypothesis.strategies import text

from src.core.component import Component
from src.core.entity import Entity
from src.core.event_queue.event import Event
from src.core.event_queue.event_queue import EventQueue


class ComponentTester(RuleBasedStateMachine):
    def __init__(self):
        super(ComponentTester, self).__init__()
        self.c = Component(Entity())

    @invariant()
    def entity(self):
        assert isinstance(self.c.entity, Entity)

    def precond_queue_not_empty(self):
        return len(self.c.entity.event_queue.events) > 0

    @rule()
    @precondition(precond_queue_not_empty)
    def receive(self):
        event = self.c.entity.event_queue.pop()
        assert event == self.c.receive()

    @rule(s=text(), o=text())
    def send(self, s, o):
        event = Event(s, o)
        self.c.send(event)
        assert self.c.entity.event_queue.events[-1] == event

    @rule()
    def reset(self):
        self.c = Component(Entity())


TestEntity = ComponentTester.TestCase

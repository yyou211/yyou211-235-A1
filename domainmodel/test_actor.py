import pytest
from domainmodel.actor import Actor

class TestActorMethods:
    def test_init(self):
        actor1 = Actor("Angelina Jolie")
        assert repr(actor1) == "<Actor Angelina Jolie>"
        actor2 = Actor("Brad Pitt")
        assert (actor1 == actor2) == False
        assert (actor1 < actor2) == True
        assert hash(actor2) == hash("Brad Pitt")
        actor1.add_actor_colleague(actor2)
        assert actor1.check_if_this_actor_worked_with(actor2) == True


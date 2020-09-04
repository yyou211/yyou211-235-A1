import pytest
from domainmodel.director import Director

class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None
        equal = (director1 == director2)
        assert equal == False
        assert (director1 == "123") == False
        director4 = Director("Christopher Nolan")
        assert (director1 < director4)== False
        assert (director4 < director1) == True
        assert hash(director1)==hash("Taika Waititi")




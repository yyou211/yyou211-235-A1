import pytest
from domainmodel.genre import Genre

class TestGenreMethods:
    def test_init(self):
        genre1 = Genre("Comedy")
        assert repr(genre1) == "<Genre Comedy>"
        genre2 = Genre("Horror")
        assert (genre1 == genre2 )== False
        assert (genre1 < genre2) == True
        assert hash(genre1) == hash("Comedy")


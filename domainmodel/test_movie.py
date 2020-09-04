
import pytest
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.movie import Movie
from typing import List

class TestMovieMethods:
    def test_init(self):
        movie1 = Movie("Moana", 2016)
        #movie1.release_year = 2017
        assert repr(movie1) == "<Movie Moana, 2016>"
        director1 = Director("Ron Clements")
        movie1.director = director1
        the_director = movie1.director
        assert the_director == director1
        print(movie1.director)
        actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
        for actor in actors:
            movie1.add_actor(actor)
        print(movie1.actors)
        movie1.runtime_minutes = 107
        print("Movie runtime: {} minutes".format(movie1.runtime_minutes))

    def test_eq(self):
        movie2 = Movie("Harry Potter", 2010)
        movie3 = Movie("Harry Potter", 2012)
        assert (movie2 == movie3) == False
        print(movie2 < movie3)
        print(movie2 > movie3)









import pytest
from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.user import User
from domainmodel.watchlist import  WatchList
from typing import List

class TestWatchlistMethods:
    def test_init(self):
        watchlist_1 = WatchList()
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Harry Potter", 2010)
        watchlist_1.add_movie(movie1)
        watchlist_1.add_movie(movie2)
        the_movie = watchlist_1.select_movie_to_watch(1)
        assert (the_movie == movie2) == True
        assert watchlist_1.size() == 2


    def test_init_1(self):
        watchlist_1 = WatchList()
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Harry Potter", 2010)
        watchlist_1.add_movie(movie1)
        watchlist_1.add_movie(movie2)
        the_movie = watchlist_1.first_movie_in_watchlist()
        assert (the_movie == movie1) == True

    def test_init_2(self):
        watchlist_1 = WatchList()
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Harry Potter", 2010)
        watchlist_1.add_movie(movie1)
        watchlist_1.add_movie(movie2)
        number = 0
        for i in watchlist_1:
            number += 1
        assert number == watchlist_1.size()


    def test_init_3(self):
        watchlist_1 = WatchList()
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Harry Potter", 2010)
        watchlist_1.add_movie(movie1)
        watchlist_1.add_movie(movie2)
        watchlist_1.add_movie(movie1)
        assert watchlist_1.size() == 2

    def test_init_4(self):
        watchlist_1 = WatchList()
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Harry Potter", 2010)
        movie3 = Movie("Harry Potter", 2012)
        watchlist_1.add_movie(movie1)
        watchlist_1.add_movie(movie2)
        watchlist_1.remove_movie(movie3)
        assert watchlist_1.size() == 2

    def test_init_5(self):
        watchlist_1 = WatchList()
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Harry Potter", 2010)
        movie3 = Movie("Harry Potter", 2012)
        watchlist_1.add_movie(movie1)
        watchlist_1.add_movie(movie2)
        watchlist_1.remove_movie(movie3)
        assert watchlist_1.size() == 2

    def test_init_6(self):
        watchlist_1 = WatchList()
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Harry Potter", 2010)
        movie3 = Movie("Harry Potter", 2012)
        watchlist_1.add_movie(movie1)
        watchlist_1.add_movie(movie2)
        assert watchlist_1.select_movie_to_watch(3) is None










import pytest
from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.user import User
from domainmodel.watchlist import WatchList
from domainmodel.MovieWatchingSimulation import MovieWatchingSimulation
from typing import List

class Test_MovieWatchingSimulation:
    # @pytest.fixture
    def test_init(self):
        user1 = User("Martin", "12345")
        user2 = User("Vivian", "12345")
        user_list = [user1, user2]
        the_movie = Movie("Moana", 2016)
        watchSimulation1 = MovieWatchingSimulation(user_list, the_movie)
        assert watchSimulation1.users == user_list

    def test_add_user(self):
        user1 = User("Martin", "12345")
        user2 = User("Vivian", "12345")
        user_list = [user1, user2]
        the_movie = Movie("Moana", 2016)
        watchSimulation1 = MovieWatchingSimulation(user_list, the_movie)
        user3 = User("Mark", "54321")
        watchSimulation1.add_user(user3)
        assert watchSimulation1.users == [user1, user2, user3]

    def test_watch_done(self):
        user1 = User("Martin", "12345")
        user2 = User("Vivian", "12345")
        the_movie = Movie("Moana", 2016)
        user1.add_watchList(the_movie)
        assert user1.watchList == [the_movie]
        user_list = [user1, user2]
        watchSimulation1 = MovieWatchingSimulation(user_list, the_movie)
        watchSimulation1.done_watching()
        assert len(user1.watchList) == 0

    def test_done_watch(self):
        user1 = User("Martin", "12345")
        user2 = User("Vivian", "12345")
        the_movie = Movie("Moana", 2016)
        user1.add_watchList(the_movie)
        user_list = [user1, user2]
        watchSimulation1 = MovieWatchingSimulation(user_list, the_movie)
        watchSimulation1.done_watching()
        assert watchSimulation1.finish_watch == True

    def test_review(self):
        user1 = User("Martin", "12345")
        user2 = User("Vivian", "12345")
        the_movie = Movie("Moana", 2016)
        user1.add_watchList(the_movie)
        user_list = [user1, user2]
        watchSimulation1 = MovieWatchingSimulation(user_list, the_movie)
        watchSimulation1.done_watching()
        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review1 = Review(movie, review_text, rating)
        assert len(watchSimulation1.reviews) == 0
        watchSimulation1.add_review(user1, review1)
        assert len(watchSimulation1.reviews) == 1








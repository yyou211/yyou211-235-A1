from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.user import User
from domainmodel.watchlist import WatchList
from typing import List

class MovieWatchingSimulation:
    def __init__(self, users, movie):
        if len(users) > 1:
            self.__users: List[User] = users
        if isinstance(movie, Movie):
            self.__the_movie = movie
        else:
            self.__the_movie = None
        self.__reviews = {}
        self.__finish_watch = False;


   #def __repr__(self):
        #return "{ Watching Simulation:" + self.__the_movie + self.__users + "}"

    @property
    def users(self):
        return self.__users
    @users.setter
    def users(self, value):
        self.__users = value

    @property
    def the_movie(self):
        return self.__the_movie

    @property
    def reviews(self):
        return self.__reviews

    @property
    def finish_watch(self):
        return self.__finish_watch

    def add_user(self, new_user):
        if new_user not in self.__users:
            self.__users.append(new_user)

    def change_movie(self, new_movie):
        if isinstance(new_movie, Movie) and new_movie != self.__the_movie:
            self.__the_movie = new_movie

    def done_watching(self):
        self.__finish_watch = True
        for i in self.__users:
            if self.__the_movie in i.watchList:
                i.watchList.remove(self.__the_movie)

    def add_review(self, user, review):
        if (self.__finish_watch == True) and (user in self.__users ) and (isinstance(review, Review)):
            if review.movie == self.__the_movie:
                self.__reviews[user] = review






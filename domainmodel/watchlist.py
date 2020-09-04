
from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.user import User
from typing import List

class WatchList:
    def __init__(self):
        self.__watch_list: List[Movie] = list()

    def add_movie(self, movie):
        if isinstance(movie, Movie) and movie not in self.__watch_list:
            self.__watch_list.append(movie)

    def remove_movie(self, movie):
        if isinstance(movie, Movie) and movie in self.__watch_list:
            self.__watch_list.remove(movie)

    def select_movie_to_watch(self, index):
        if type(index) != int or index < 0 or index >= len(self.__watch_list):
            return None
        else:
            return self.__watch_list[index]

    def size(self):
        return len(self.__watch_list)

    def first_movie_in_watchlist(self):
        if len(self.__watch_list) == 0:
            return None
        else:
            return self.__watch_list[0]

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count < len(self.__watch_list):
            the_movie = self.__watch_list[self.count]
            self.count +=1
            return the_movie
        else:
            raise StopIteration









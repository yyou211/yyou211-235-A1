from domainmodel.movie import Movie
from domainmodel.review import Review
from typing import List
class User:
    def __init__(self, user_name, password):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.lower()
        if password == "" or type(user_name) is not str:
            self.__password = None
        else:
            self.__password = password
        self.__watched_movies: List[Movie] = list()
        self.__reviews: List[Review] = list()
        self.__time_spent_watching_movies_minutes = 0
        self.__watchList: List[Movie] = list()
    @property
    def user_name(self):
        return self.__user_name
    @property
    def password(self):
        return self.__password
    @property
    def watched_movies(self):
        return self.__watched_movies
    @property
    def reviews(self):
        return self.__reviews
    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, value):
        self.__time_spent_watching_movies_minutes += value

    @property
    def watchList(self):
        return self.__watchList

    def __repr__(self):
        return "<User " + self.__user_name + ">"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        if self.__user_name == other.__user_name:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie):
        if isinstance(movie, Movie) and movie not in self.__watched_movies:
            self.__watched_movies.append(movie)
            #print("****")
            if type(movie.runtime_minutes) is int:
                #print("runtime")
                #print(movie.runtime_minutes)
                self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if isinstance(review, Review):
            self.__reviews.append(review)

    def add_watchList(self, new_movie):
        if isinstance(new_movie, Movie) and (new_movie not in self.__watchList):
            self.__watchList.append(new_movie)

movies = [Movie("Moana", 2016), Movie("Guardians of the Galaxy", 2014)]

movies[0].runtime_minutes = 107
movies[1].runtime_minutes = 121
user = User("Martin", "pw12345")
print(user.watched_movies)
print(user.time_spent_watching_movies_minutes)
for movie in movies:
    user.watch_movie(movie)
print(user.watched_movies)
print(user.time_spent_watching_movies_minutes)
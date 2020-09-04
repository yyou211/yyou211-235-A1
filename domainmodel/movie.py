from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from typing import List

class Movie:
    def __init__(self, movie_name: str, release_year = None):
        if movie_name == "" or type(movie_name) is not str:
            self.__title = None
        else:
            self.__title = movie_name.strip()
        if type(release_year) is not int or release_year < 1900:
            self.__release_year = None
        else:
            self.__release_year = release_year
        self._description = None
        self._director = None
        self._actors: List[Actor] = list()
        self._genres: List[Genre] = list()
        self._runtime_minutes = None

    @property
    def title(self) -> str:
        return self.__title

    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if description == "" or type(description) is not str:
            self._description = None
        else:
            self._description = description.strip()

    @property
    def director(self):
        #return self.__director
        return self._director

    @director.setter
    def director(self, director):
        if isinstance(director, Director):
            self._director = director

    @property
    def actors(self) -> list:
        return self._actors

    @property
    def genres(self) -> list:
        return self._genres

    @property
    def runtime_minutes(self) -> int:
        return self._runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if type(runtime_minutes) is int and runtime_minutes > 0:
            self._runtime_minutes = runtime_minutes
        else:
            raise ValueError

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        if self.__title == other.__title and self.__release_year == other.__release_year:
            return True
        else:
            return False

    def __lt__(self, other):
        movie_info = self.__title + str(self.__release_year)
        other_movie_info = other.__title + str(other.__release_year)
        return movie_info < other_movie_info

    def __hash__(self):
        the_string = str(self.__title) + str(self.__release_year)
        return hash(the_string)

    def add_actor(self, actor):
        if isinstance(actor, Actor):
            self._actors.append(actor)

    def remove_actor(self, actor):
        if isinstance(actor, Actor) and len(self._actors)>0 and actor in self._actors:
            self.actors.remove(actor)


    def add_genre(self, genre):
        if isinstance(genre, Genre):
            self._genres.append(genre)

    def remove_genre(self, genre):
        if isinstance(genre, Genre) and len(self._genres) > 0 and genre in self._genres:
            self._genres.remove(genre)


movie = Movie("Moana", 2016)
print(movie)

director = Director("Ron Clements")
movie.director = director
print(movie.director)

actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
for actor in actors:
    movie.add_actor(actor)
print(movie.actors)

movie.runtime_minutes = 107
print("Movie runtime: {} minutes".format(movie.runtime_minutes))





















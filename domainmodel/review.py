from datetime import datetime
from domainmodel.movie import Movie

class Review:
    def __init__(self, movie, review_text, rating):
        if not isinstance(movie, Movie):
            self.__movie = None
        else:
            self.__movie = movie

        if type(review_text) is str and review_text != "":
            self.__review_text = review_text
        else:
            self.__review_text = None

        if type(rating) is int and 1 <= rating <= 10:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.today()

    @property
    def movie(self):
        return self.__movie
    @property
    def review_text(self):
        return self.__review_text
    @property
    def rating(self):
        return self.__rating
    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        return self.movie + ", " + self.review_text + ", " + self.rating + ", " + self.timestamp

    def __eq__(self, other):
        if not isinstance(other, Review):
            return False
        if self.movie == other.movie and self.review_text == other.review_text and self.rating == other.rating and self.timestamp == other.timestamp:
            return True
        else:
            return False

print("******")
movie = Movie("Moana", 2016)
review_text = "This movie was very enjoyable."
rating = 8
review = Review(movie, review_text, rating)

print(review.movie)
print("Review: {}".format(review.review_text))
print("Rating: {}".format(review.rating))




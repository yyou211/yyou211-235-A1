
class Director:
    #class Person:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        # TODO
        if not isinstance(other, Director):
            return False
        if self.__director_full_name == other.__director_full_name:
            return True
        else:
            return False
        #pass

    def __lt__(self, other):
        # TODO
        return self.__director_full_name < other.__director_full_name

        #pass

    def __hash__(self):
        # TODO
        return hash(self.__director_full_name)
        #pass





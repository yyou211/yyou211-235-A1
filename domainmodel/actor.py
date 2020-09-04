from typing import List
class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self._colleague_list = list()

    @property
    def actor_full_nam(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        # TODO
        if not isinstance(other, Actor):
            return False
        if self.__actor_full_name == other.__actor_full_name:
            return True
        else:
            return False
        #pass

    def __lt__(self, other):
        # TODO
        return self.__actor_full_name < other.__actor_full_name

        #pass

    def __hash__(self):
        # TODO
        return hash(self.__actor_full_name)
        #pass

    def add_actor_colleague(self, colleague):
        self._colleague_list += [colleague.__actor_full_name]

    def check_if_this_actor_worked_with(self, colleague):
        if colleague.__actor_full_name in self._colleague_list:
            return True
        else:
            return False

    #pass


from ro.ubb.movieapp.domain.base_entity import BaseEntity


class PersonEntity(BaseEntity):
    def __init__(self, id, name):
        super().__init__(id)
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return f"{super().__str__()}, Name: {self.name}"

class ClientEntity(PersonEntity):
    def __init__(self, id, name, cnp):
        super().__init__(id, name)
        self.__cnp = cnp

    @property
    def cnp(self):
        return self.__cnp

    @cnp.setter
    def cnp(self, value):
        self.__cnp = value

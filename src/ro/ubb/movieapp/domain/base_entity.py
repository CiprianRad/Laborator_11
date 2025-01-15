from abc import abstractmethod

class AbstractEntity():

    @property
    @abstractmethod
    def id(self):
        pass

class BaseEntity(AbstractEntity):
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def __str__(self):
        return f"ID: {self.id}"


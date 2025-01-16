from ro.ubb.movieapp.domain.base_entity import BaseEntity


class MovieEntity(BaseEntity):
    def __init__(self, id, title, description, genre):
        super().__init__(id)
        self.__title = title
        self.__description = description
        self.__genre = genre

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    def __str__(self):
        return super().__str__() + ", " 'title:' + " " + str(self.title) + ", " + "description:" + " " + str(
            self.description) + ", " + "genre:" + " " + str(self.genre)

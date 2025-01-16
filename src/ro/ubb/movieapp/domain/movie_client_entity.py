from ro.ubb.movieapp.domain.base_entity import AbstractEntity


class MovieClientEntity(AbstractEntity):
    def __init__(self, movie_id, client_id, title):
        self.__movie_id = movie_id
        self.__client_id = client_id
        self.__title = title

    @property
    def id(self):
        return (self.movie_id, self.client_id)

    @property
    def movie_id(self):
        return self.__movie_id

    @movie_id.setter
    def movie_id(self, value):
        self.__movie_id = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        self.__client_id = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    def __str__(self):
        return f'Movie ID: {self.movie_id}, Client ID: {self.client_id}, Title: {self.title}'
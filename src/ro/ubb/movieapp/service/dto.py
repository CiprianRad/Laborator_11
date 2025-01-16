class Converter:

    @staticmethod
    def create_movie_views_dto(movie, views):
         return MovieViewsDto(movie.title, views)


class MovieViewsDto:
    def __init__(self, title, views):
        self.__title = title
        self.__views = views

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def views(self):
        return self.__views

    @views.setter
    def views(self, value):
        self.__views = value

    def __str__(self):
        return f"Title: {self.title}, Views: {self.views}"
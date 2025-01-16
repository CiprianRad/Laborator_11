from ro.ubb.movieapp.domain.movie_entity import MovieEntity

class MovieService:
    def __init__(self, movie_repository):
        self.__movie_repository = movie_repository

    @property
    def movie_repository(self):
        return self.__movie_repository

    def find_movie_by_id(self, id):
        return self.movie_repository.find_by_id(id)

    def get_movies(self):
        return self.movie_repository.find_all()

    def remove_movie(self, id):
        self.movie_repository.delete_by_id(id)

    def add_movie(self, id, title, description, genre):
        movie = MovieEntity(id, title, description, genre)
        self.movie_repository.save(movie)

    def update_movie(self, id, title, description, genre):
        movie = MovieEntity(id, title, description, genre)
        self.movie_repository.update(movie)
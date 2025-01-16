from ro.ubb.movieapp.domain.movie_client_entity import MovieClientEntity
from ro.ubb.movieapp.service.dto import MovieViewsDto, Converter


class ReportsService:
    def __init__(self, movie_repository, client_repository, movie_client_repository):
        self.__movie_repository = movie_repository
        self.__client_repository = client_repository
        self.__movie_client_repository = movie_client_repository

    @property
    def client_repository(self):
        return self.__client_repository

    @property
    def movie_client_repository(self):
        return self.__movie_client_repository

    def get_all_movie_clients(self):
        return self.movie_client_repository.find_all()

    def add_movie_client(self, movie_id, client_id):
        movie = self.__movie_repository.find_by_id(movie_id)
        if movie is not None:
            self.movie_client_repository.save(MovieClientEntity(movie_id, client_id, movie.title))
        else:
            raise ValueError("Movie list is empty.") #You shouldn't raise exceptions here

    def __compute_movie_views(self, movie):
       movie_client_list = self.movie_client_repository.find_all()
       filtered_movie_client_list = list(filter(lambda x : x.movie_id == movie.id, movie_client_list))
       number_views = len(filtered_movie_client_list)
       return number_views

    def get_movie_views(self):
        dto = []
        movies = self.__movie_repository.find_all()
        for movie in movies:
            movie_views = self.__compute_movie_views(movie)
            movie_views_dto = Converter.create_movie_views_dto(movie, movie_views)
            dto.append(movie_views_dto)
        return dto

    def get_clients_by_name_ascending(self):
        client_list = self.client_repository.find_all()
        return sorted(client_list, key= lambda x :x.name)

    def get_clients_by_name_descending_and_cnp_ascending(self):
        client_list = self.client_repository.find_all()
        return sorted(client_list, key= lambda x: (-ord(x.name.lower()[0]), x.cnp))

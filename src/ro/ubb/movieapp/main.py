from ro.ubb.movieapp.domain.validators import ClientValidator, MovieValidator, MovieClientValidator
from ro.ubb.movieapp.repository.file_repository import ClientFileRepository
from ro.ubb.movieapp.repository.in_memory_repository import InMemoryRepository
from ro.ubb.movieapp.service.client_service import ClientService
from ro.ubb.movieapp.service.movie_service import MovieService
from ro.ubb.movieapp.service.reports_service import ReportsService
from ro.ubb.movieapp.ui.console import AppConsole


def main():
    movie_validator = MovieValidator()
    client_validator = ClientValidator()
    movie_client_validator = MovieClientValidator()
    movie_client_repository = InMemoryRepository(movie_client_validator)
    movie_repository = InMemoryRepository(movie_validator)
    client_repository = ClientFileRepository(client_validator, "../../../../data/clients")
    movie_service = MovieService(movie_repository)
    client_service = ClientService(client_repository)
    reports_service = ReportsService(movie_repository, client_repository, movie_client_repository)
    app_console = AppConsole(movie_service, client_service, reports_service)
    app_console.run_menu()
main()
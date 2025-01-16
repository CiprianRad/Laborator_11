import traceback

from ro.ubb.movieapp.domain.validators import ValidatorException
from ro.ubb.movieapp.repository.in_memory_repository import RepositoryException


class AppConsole():
    def __init__(self, movie_service, client_service, movie_client_service):
        self.__movie_service = movie_service
        self.__client_service = client_service
        self.__movie_client_service = movie_client_service

    @property
    def movie_service(self):
        return self.__movie_service

    @movie_service.setter
    def movie_service(self, value):
        self.__movie_service = value

    @property
    def client_service(self):
        return self.__client_service

    @client_service.setter
    def client_service(self, value):
        self.__client_service = value

    @property
    def movie_client_service(self):
        return self.__movie_client_service

    @movie_client_service.setter
    def movie_client_service(self, value):
        self.__movie_client_service = value


    @staticmethod
    def __print_commands():
        print("1. Add a new movie: ")
        print("2. Remove a movie by id: ")
        print("3. Show all movies: ")
        print("4. Update movie by id: ")
        print("5. Add a new client: ")
        print("6. Remove a client by id: ")
        print("7. Show all clients: ")
        print("8. Update client by id: ")
        print("9. Show watch list of client ")
        print("10. Add a movie to the watch list")
        print("11. Show most watched movies:")
        print("12. Sort clients ascending by name")
        print("13. Sort clients descending by name and ascending by cnp")
        print("14. Exit")

    def run_menu(self):
        while True:
            self.__print_commands()
            try:
                option = input("Enter your choice: ")
                if option == "1":
                    self.__ui_add_movie()
                elif option == "2":
                    self.__ui_remove_movie()
                elif option == "3":
                    self.__ui_show_movies()
                elif option == "4":
                    self.__ui_update_movie()
                elif option == "5":
                    self.__ui_add_client()
                elif option == "6":
                    self.__ui_remove_client()
                elif option == "7":
                    self.__ui_show_clients()
                elif option == "8":
                    self.__ui_update_client()
                elif option == "9":
                    self.__ui_show_movie_client()
                elif option == "10":
                    self.__ui_add_movie_client()
                elif option == "11":
                    self.__ui_show_most_viewed()
                elif option == "12":
                    self.__ui_client_name_asc()
                elif option == "13":
                    self.__ui_client_name_desc_cnp_asc()
                elif option == "14":
                    break
            except KeyError:
                print("Option not implemented")

    def __ui_add_movie(self):
        try:
            movie_id = int(input("Enter movie id: "))
            title = str(input("Enter movie title: "))
            description = str(input("Enter movie description: "))
            genre = str(input("Enter movie genre: "))
            try:
                self.movie_service.add_movie(movie_id, title, description, genre)
            except RepositoryException as re:
                print(f"Duplicate ID", re)
                traceback.print_exc()
        except ValidatorException as vr:
            print('Invalid inputs', vr)
            traceback.print_exc()

    def __ui_remove_movie(self):
        try:
            movie_id = int(input("Enter movie id: "))
            self.movie_service.remove_movie(movie_id)
        except RepositoryException as re:
            print("Movie with this id does not exist", re)
            traceback.print_exc()

    def __ui_update_movie(self):
        try:
            movie_id = int(input("Enter movie id: "))
            title = str(input("Enter movie title: "))
            description = str(input("Enter movie description: "))
            genre = str(input("Enter movie genre: "))
            try:
                self.movie_service.update_movie(movie_id, title, description, genre)
            except RepositoryException as re:
                print(f"Movie with this id does not exist", re)
                traceback.print_exc()
        except ValidatorException as ve:
            print("Please enter valid inputs: ", ve)
            traceback.print_exc()

    def __ui_show_movies(self):
        print(
            *self.movie_service.get_movies())  # Note, without the * , the print would have returned the address of the list

    def __ui_add_client(self):
        try:
            id = int(input("Enter an id: "))
            name = str(input("Enter name: "))
            cnp = int(input("Enter CNP: "))
            try:
                self.client_service.add_client(id, name, cnp)
            except RepositoryException as re:
                print(f"Duplicate ID", re)
                traceback.print_exc()
        except ValidatorException as ve:
            print("Please enter valid inputs: ", ve)
            traceback.print_exc()

    def __ui_remove_client(self):
        try:
            id = int(input("Enter id: "))
            try:
                self.client_service.remove_client(id)
            except RepositoryException as re:
                print(f"Client with this id does not exist", re)
                traceback.print_exc()
        except ValidatorException as ve:
            print("Please enter valid inputs: ", ve)
            traceback.print_exc()

    def __ui_show_clients(self):
        print(*self.client_service.get_all_clients())

    def __ui_update_client(self):
        try:
            id = int(input("Enter id: "))
            name = str(input("Enter name: "))
            cnp = int(input("Enter CNP: "))
            try:
                self.client_service.update_client(id, name, cnp)
            except RepositoryException as re:
                print(f"Client with this id does not exist", re)
                traceback.print_exc()
        except ValidatorException as ve:
            print("Please enter valid inputs: ", ve)
            traceback.print_exc()

    def __ui_show_movie_client(self):
        print(*self.movie_client_service.get_all_movie_clients())

    def __ui_add_movie_client(self):
        try:
            movie_id = int(input("Enter a movie id:"))
            client_id = int(input("Enter a client id:"))
            try:
                self.movie_client_service.add_movie_client(movie_id, client_id)
            except RepositoryException as re:
                print("Movie or Client with this id does not exist", re)
                traceback.print_exc()
        except ValidatorException as ve:
            print("Invalid inputs: ", ve)
            traceback.print_exc()

    def __ui_show_most_viewed(self):
        print(*self.movie_client_service.get_movie_views())

    def __ui_client_name_asc(self):
        print(*self.movie_client_service.get_clients_by_name_ascending())

    def __ui_client_name_desc_cnp_asc(self):
        print(*self.movie_client_service.get_clients_by_name_descending_and_cnp_ascending())


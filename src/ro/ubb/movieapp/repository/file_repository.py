from ro.ubb.movieapp.domain.client_entity import ClientEntity
from ro.ubb.movieapp.repository.in_memory_repository import InMemoryRepository


class ClientFileRepository(InMemoryRepository):
    def __init__(self, client_validator, file_name):
        super().__init__(client_validator)
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                array = line.split(",")
                client = ClientEntity(int(array[0]), array[1], int(array[2]))
                super().save(client)

    def save(self, client):
        with open(self.__file_name, 'a') as f:
            f.write("\n" + str(client.id) + "," + str(client.name) + "," + str(client.cnp))
            super().save(client)


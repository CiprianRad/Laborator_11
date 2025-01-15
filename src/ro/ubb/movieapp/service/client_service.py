from ro.ubb.movieapp.domain.client_entity import ClientEntity


class ClientService:
    def __init__(self, client_repository):
        self.__client_repository = client_repository

    @property
    def client_repository(self):
        return self.__client_repository

    def find_client_by_id(self, id):
        return self.client_repository.find_by_id(id)

    def get_all_client(self):
        return self.client_repository.find_all()

    def add_client(self, id, name, cnp):
        client = ClientEntity(id, name, cnp)
        self.client_repository.save(client)

    def remove_client(self, id):
        self.client_repository.delete_by_id(id)

    def update_client(self, id, name, cnp):
        client = ClientEntity(id, name, cnp)
        self.client_repository.update(client)

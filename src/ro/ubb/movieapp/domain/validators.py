from abc import abstractmethod
from src.ro.ubb.movieapp.domain.client_entity import PersonEntity, ClientEntity


class MovieAppException(Exception):
    pass

class ValidatorException(MovieAppException):
    pass

class EntityValidator():

    @abstractmethod
    def validate(self, entity):
        pass

class BaseEntityValidator(EntityValidator):
    def validate(self, entity):
        entity_id = entity.id

        # Check if id is a tuple
        if isinstance(entity_id, tuple):
            if not all(isinstance(id_part, int) and id_part >= 0 for id_part in entity_id):
                raise ValidatorException("All IDs in the tuple must be positive integers")
        else:
            # Single ID validation
            if not isinstance(entity_id, int) or entity_id < 0:
                raise ValidatorException("ID must be a positive integer")

class PersonValidator(BaseEntityValidator):
    def validate(self, person):
        super().validate(person)
        if not isinstance(person.name, str) or person.name.strip(" ") == '':
            raise ValidatorException("Person Name must be a non-empty string")

class ClientValidator(PersonValidator):
    def validate_cnp(self, client):
        cnp_list_string = list(str(client.cnp))
        cnp_list = [int(number) for number in cnp_list_string]
        cnp_year_list = [int(cnp_list_string[i]) for i in [1, 2]]
        cnp_year = int(''.join(map(str, cnp_year_list)))
        cnp_month_list = [int(cnp_list_string[i]) for i in [3, 4]]
        cnp_month = int(''.join(map(str, cnp_month_list)))
        cnp_day_list = [int(cnp_list_string[i]) for i in [5, 6]]
        cnp_day = int(''.join(map(str, cnp_day_list)))
        if cnp_list[0] != 5 and cnp_list[0] != 6:
            raise ValidatorException("CNP must start with 5 or 6 depending on sex: ")
        if cnp_year not in range(0, 24):
            raise ValidatorException("Year number must be between 0-24")
            # raise ValidatorException("Year number incorrect ")
        if cnp_month not in range(1, 12):
            raise ValidatorException("Month number ranges between 01 and 12")
        if cnp_month == 2 and cnp_year % 4 == 0 and cnp_day > 29:
            raise ValidatorException("Cnp day number incorrect. February doesn't have more than 29 days")
        if cnp_month == 2 and cnp_year % 4 != 0 and cnp_day > 28:
            raise ValidatorException("Cnp day number incorrect. February didn't have more than 28 days that year")
        if cnp_month in [1, 3, 5, 7, 8, 10, 12] and cnp_day > 31:
            raise ValidatorException("Cnp day number incorrect. Months cannot exceed 31 days")
        if cnp_month in [2, 4, 6, 9, 11] and cnp_day > 30:
            raise ValidatorException("Cnp day number incorrect. In that month there were only 30 days")

    def validate(self, client):
        # if not isinstance(client, ClientEntity):
        #     raise ValidatorException("Client Entity must be a ClientEntity object")
        super().validate(client)
        if not isinstance(client.cnp, int) or len(str(client.cnp)) != 13 or client.cnp <=0 :
            raise ValidatorException("Client CNP must be a 13 digit positive integer ")
        self.validate_cnp(client)


class MovieValidator(BaseEntityValidator):
    pass

class MovieClientValidator(BaseEntityValidator):
    pass
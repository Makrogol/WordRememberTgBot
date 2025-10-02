from src.core.user.user_identifier_data import UserIdentifierData


class UserIdentifierDataJsonFactory:
    @staticmethod
    def create(data: dict) -> UserIdentifierData:
        user_identifier_data = UserIdentifierData()
        user_identifier_data.id = data['id']
        user_identifier_data.name = data['name']
        return user_identifier_data

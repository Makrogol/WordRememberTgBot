from src.core.user.user_identifier_data import UserIdentifierData


class ViewData:
    def __init__(self, user_identifier_data: UserIdentifierData = UserIdentifierData(), args: list[str] = []):
        self.user_identifier_data = user_identifier_data
        self.args = args

import json
from pathlib import Path

from .config import USER_DATA_PATH, USER_DATA_FILE_NAME
from ..exceptions.load_user_data_from_file_exception import LoadUserDataFromFileException
from ..user_data.user_data import UserData


class UserDataManager:
    def __init__(self, user_id: int, base_user_data_path: Path = USER_DATA_PATH):
        self.__user_id = user_id
        self.__user_data_path = base_user_data_path / str(self.__user_id)
        self.__user_data_path.mkdir(parents=True, exist_ok=True)

        self.__user_data_file_path = self.__user_data_path / USER_DATA_FILE_NAME
        self.__user_data_file_path.touch(exist_ok=True)

    def save_to_file(self, user_data: UserData) -> None:
        file = open(str(self.__user_data_file_path), 'w')
        file.writelines(json.dumps(user_data.to_json()))
        file.close()

    def get_or_create_user_data(self, user_login: str) -> UserData:
        if self.has_user_data():
            return self.try_load_from_file()
        user_data = UserData(self.__user_id, user_login)
        self.save_to_file(user_data)
        return user_data

    def has_user_data(self) -> bool:
        return self.try_load_from_file() is not None

    def try_load_from_file(self) -> UserData | None:
        try:
            file = open(str(self.__user_data_file_path), 'r')
            data = ''.join(file.readlines())
            user_data = UserData()
            user_data.from_json(json.loads(data))
            return user_data
        except:
            return None

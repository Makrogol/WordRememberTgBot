import json
import os
from pathlib import Path

from .config import USER_DATA_PATH, USER_DATA_FILE_NAME
from ..user.user_identifier_data import UserIdentifierData
from ..user_data.user_data import UserData
from ..user_data.user_data_json_factory import UserDataJsonFactory


class UserDataManager:
    def __init__(self, user_identifier_data: UserIdentifierData = None, base_user_data_path: Path = None):
        if user_identifier_data is None:
            user_identifier_data = UserIdentifierData()
        if base_user_data_path is None:
            base_user_data_path = USER_DATA_PATH

        self.user_identifier_data = user_identifier_data
        self.user_data_path = base_user_data_path / str(self.user_identifier_data.id)
        self.user_data_path.mkdir(parents=True, exist_ok=True)

        self.user_data_file_path = self.user_data_path / USER_DATA_FILE_NAME
        self.user_data_file_path.touch(exist_ok=True)

    def delete_user_data_files(self):
        os.remove(self.user_data_file_path)

    def save_to_file(self, user_data: UserData) -> None:
        file = open(str(self.user_data_file_path), 'w')
        file.writelines(json.dumps(user_data.to_json()))
        file.close()

    def get_or_create_user_data(self) -> UserData:
        if self.has_user_data():
            return self.try_load_from_file()
        user_data = UserData(self.user_identifier_data)
        self.save_to_file(user_data)
        return user_data

    def has_user_data(self) -> bool:
        return self.try_load_from_file() is not None

    def try_load_from_file(self) -> UserData | None:
        file = None
        try:
            file = open(str(self.user_data_file_path), 'r')
            data = ''.join(file.readlines())
            user_data = UserDataJsonFactory.create(json.loads(data))
            return user_data
        except:
            return None
        finally:
            if file is not None:
                file.close()

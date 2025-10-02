import json

from src.core.file_manager.config import ROOT_USERS_PATH, USER_DATA_PATH, USER_DATA_FILE_NAME
from src.core.user.user_identifier_data import UserIdentifierData
from src.core.user_data.user_data_json_factory import UserDataJsonFactory


def get_root_users() -> list[int]:
    root_users_path = ROOT_USERS_PATH
    root_users_path.touch(exist_ok=True)

    with open(str(root_users_path), 'r', encoding='utf-8') as f:
        root_users = [int(line) for line in f.readlines()]
        f.close()

    return root_users


def get_all_user_identifier_datas() -> list[UserIdentifierData]:
    user_identifier_datas: list[UserIdentifierData] = []
    user_data_path = USER_DATA_PATH
    for path in user_data_path.iterdir():
        if path.is_file():
            continue
        with open(str(path / USER_DATA_FILE_NAME), 'r', encoding='utf-8') as f:
            print(path)
            # TODO очень плохо, копипаста с юзер дата манагера
            data = ''.join(f.readlines())
            user_data = UserDataJsonFactory.create(json.loads(data))
            user_identifier_datas.append(user_data.user_identifier_data)
            f.close()

    return user_identifier_datas

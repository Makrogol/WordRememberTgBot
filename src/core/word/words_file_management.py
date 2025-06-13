import os
from pathlib import Path
from .config import USER_WORD_DATA_PATH


def create_path_to_user_word_data(user_id: int, user_word_data_path: Path = USER_WORD_DATA_PATH) -> Path:
    return user_word_data_path / f"word_{user_id}.txt"


def is_file_exist(file_path: Path) -> bool:
    return os.path.exists(str(file_path))


def get_words_from_file(user_id: int, user_word_data_path: Path = USER_WORD_DATA_PATH) -> list[str] | None:
    file_path = create_path_to_user_word_data(user_id, user_word_data_path)
    if not os.path.exists(str(file_path)):
        return None
    file = open(str(file_path), 'r')
    words = file.readlines()
    file.close()
    return words


def save_word_to_file(user_id: int, word: str, user_word_data_path: Path = USER_WORD_DATA_PATH) -> None:
    file_path = create_path_to_user_word_data(user_id, user_word_data_path)
    if not os.path.exists(str(file_path)):
        file_path.touch()
    file = open(str(file_path), 'a')
    file.write(word + '\n')
    file.close()

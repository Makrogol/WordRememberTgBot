import json
import os
from pathlib import Path
from .config import USER_DATA_PATH, USER_DATA_WORDS_FILE_NAME, USER_DATA_WORDS_OUTPUT_FILE_NAME
from ..word.word import Word, Words
from ..word.word_json_factory import WordJsonFactory


class WordsManager:
    def __init__(self, user_id: int, base_user_data_path: Path = None, user_data_words_file_name: str = None,
                 user_data_words_output_file_name: str = None):
        if base_user_data_path is None:
            base_user_data_path = USER_DATA_PATH
        if user_data_words_file_name is None:
            user_data_words_file_name = USER_DATA_WORDS_FILE_NAME
        if user_data_words_output_file_name is None:
            user_data_words_output_file_name = USER_DATA_WORDS_OUTPUT_FILE_NAME

        self.user_id = user_id
        self.user_data_path = base_user_data_path / str(self.user_id)
        self.user_data_path.mkdir(parents=True, exist_ok=True)

        self.user_data_words_file_path = self.user_data_path / user_data_words_file_name
        self.user_data_words_file_path.touch(exist_ok=True)

        self.user_data_words_output_file_path = self.user_data_path / user_data_words_output_file_name
        self.user_data_words_output_file_path.touch(exist_ok=True)

    # Use only for tests
    def delete_user_files(self):
        os.remove(self.get_words_file_path())
        os.remove(self.get_words_output_file_path())

    # Use only for tests
    def get_words_file_path(self) -> Path:
        return self.user_data_words_file_path

    def get_words_output_file_path(self) -> Path:
        return self.user_data_words_output_file_path

    def try_update_words_output_file(self) -> bool:
        words = self.try_load_from_file()
        if words is None:
            return False

        file = open(str(self.user_data_words_output_file_path), 'w')
        for i, word in enumerate(words):
            file.write(word.get_full_numerated_word(i + 1))
        file.close()
        return True

    def try_load_words_from_output_file(self) -> list[str] | None:
        if not self.try_update_words_output_file():
            return None

        file = None
        try:
            file = open(str(self.user_data_words_output_file_path), 'r')
            words = file.readlines()
            return words
        except:
            return None
        finally:
            if file is not None:
                file.close()

    def try_load_from_file(self) -> Words | None:
        file = None
        try:
            file = open(str(self.user_data_words_file_path), 'r')
            data = ''.join(file.readlines())
            if data == '':
                return []
            raw_words = json.loads(data)
            words = [WordJsonFactory.create(raw_word) for raw_word in raw_words]
            return words
        except:
            return None
        finally:
            if file is not None:
                file.close()

    def has_words(self) -> bool:
        words = self.try_load_from_file()
        return words is not None and len(words) > 0

    def save_to_file(self, words: Words) -> None:
        file = open(str(self.user_data_words_file_path), 'w')
        file.writelines(json.dumps([word.to_json() for word in words]))
        file.close()

    def try_add_word_to_file(self, word: Word) -> bool:
        words = self.try_load_from_file()
        if words is None:
            return False
        words.append(word)
        self.save_to_file(words)
        return True

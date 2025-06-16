import json
from pathlib import Path
from .config import USER_DATA_PATH, USER_DATA_WORDS_FILE_NAME, USER_DATA_WORDS_OUTPUT_FILE_NAME
from ..exceptions.load_words_from_file_exception import LoadWordsFromFileException
from ..word.word import Word


class WordsManager:
    def __init__(self, user_id: int, base_user_data_path: Path = USER_DATA_PATH):
        self.__user_id = user_id
        self.__user_data_path = base_user_data_path / str(self.__user_id)
        self.__user_data_path.mkdir(parents=True, exist_ok=True)

        self.__user_data_words_file_path = self.__user_data_path / USER_DATA_WORDS_FILE_NAME
        self.__user_data_words_file_path.touch(exist_ok=True)

        self.__user_data_words_output_file_path = self.__user_data_path / USER_DATA_WORDS_OUTPUT_FILE_NAME
        self.__user_data_words_output_file_path.touch(exist_ok=True)

    def get_words_output_file_path(self) -> Path:
        return self.__user_data_words_output_file_path

    def try_update_words_output_file(self) -> bool:
        words = self.try_load_from_file()
        if words is None:
            return False

        file = open(str(self.__user_data_words_output_file_path), "w")
        for i, word in enumerate(words):
            file.write(word.get_full_numerated_word(i + 1))
        file.close()
        return True

    def try_load_words_from_output_file(self) -> list[str] | None:
        if not self.try_update_words_output_file():
            return None

        try:
            file = open(str(self.__user_data_words_output_file_path), "r")
            words = file.readlines()
            file.close()
            return words
        except:
            return None

    def try_load_from_file(self) -> list[Word] | None:
        try:
            file = open(str(self.__user_data_words_file_path), "r")
            data = "".join(file.readlines())
            if data == "":
                return []
            raw_words = json.loads(data)
            words = [Word() for _ in range(len(raw_words))]
            for word, raw_word in zip(words, raw_words):
                word.from_json(raw_word)
            return words
        except:
            return None

    def has_words(self) -> bool:
        return self.try_load_from_file() is not None

    def save_to_file(self, words: list[Word]) -> None:
        file = open(str(self.__user_data_words_file_path), "w")
        file.writelines(json.dumps([word.to_json() for word in words]))
        file.close()

    def try_add_word_to_file(self, word: Word) -> bool:
        words = self.try_load_from_file()
        if words is None:
            return False
        words.append(word)
        self.save_to_file(words)
        return True

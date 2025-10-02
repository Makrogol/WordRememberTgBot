import os
from pathlib import Path

from test.config import TEST_USER_DATA_PATH, TEST_USER_DATA_FILE_NAME, TEST_USER_DATA_WORDS_OUTPUT_FILE_NAME

from src.core.file_manager.words_manager import WordsManager


class MockWordsManager(WordsManager):
    def __init__(self, user_id: int, base_user_data_path: Path = TEST_USER_DATA_PATH):
        super().__init__(user_id, base_user_data_path, TEST_USER_DATA_FILE_NAME, TEST_USER_DATA_WORDS_OUTPUT_FILE_NAME)

    def delete_user_files(self):
        os.remove(super().get_words_file_path())
        os.remove(super().get_words_output_file_path())

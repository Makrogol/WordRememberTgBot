from pathlib import Path

TEST_CHAT_ID = 123
TEST_USER_ID = 456
TEST_USER_NAME = 'test'

# TODO import smth from src.core.file_manager.config
TEST_BASE_PATH = Path(__file__).parent
TEST_USER_DATA_DIRECTORY_NAME = 'test_user_data'
TEST_USER_DATA_PATH = TEST_BASE_PATH / TEST_USER_DATA_DIRECTORY_NAME
TEST_USER_DATA_FILE_NAME = 'user_data.json'
TEST_USER_DATA_WORDS_FILE_NAME = 'user_words.json'
TEST_USER_DATA_WORDS_OUTPUT_FILE_NAME = 'words.txt'

from pathlib import Path

BASE_PATH = Path(__file__).parent.parent.parent.parent
USER_DATA_DIRECTORY_NAME = "user_data"
USER_DATA_PATH = BASE_PATH / USER_DATA_DIRECTORY_NAME
USER_DATA_FILE_NAME = "user_data.json"
USER_DATA_WORDS_FILE_NAME = "user_words.json"
USER_DATA_WORDS_OUTPUT_FILE_NAME = "words.txt"

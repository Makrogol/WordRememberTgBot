import os
from pathlib import Path
from .config import MAX_MESSAGE_LENGTH, USER_WORD_DATA_PATH

def create_path_to_user_word_data(user_id: int) -> Path:
    return USER_WORD_DATA_PATH / f"word_{user_id}.txt"

def create_paginated_words(words: list[str]) -> list[str]:
    paginated_words = []
    message_len = 0
    prev_i = 0
    for i in range(len(words)):
        if message_len + len(words[i]) > MAX_MESSAGE_LENGTH:
            paginated_words.append(''.join(words[prev_i:i]))
            prev_i = i
            message_len = 0
        message_len += len(words[i])
    paginated_words.append(''.join(words[prev_i:len(words)]))
    return paginated_words

def get_words_from_file(user_id: int) -> list[str] | None:
    file_path = create_path_to_user_word_data(user_id)
    if not os.path.exists(str(file_path)):
        return None
    file = open(str(file_path), 'r')
    words = file.readlines()
    file.close()
    return words

def save_word_to_file(user_id: int, word: str) -> None:
    file_path = create_path_to_user_word_data(user_id)
    if not os.path.exists(str(file_path)):
        file_path.touch()
    file = open(str(file_path), 'a')
    file.write(word + '\n')
    file.close()

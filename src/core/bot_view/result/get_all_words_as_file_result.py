from pathlib import Path
from enum import Enum


class GetAllWordsAsFileResultType(Enum):
    Empty = 0
    CannotUpdateOutputFile = 1
    NoWords = 2
    IncorrectIndex = 3
    Success = 4


class GetAllWordsAsFileResult:
    def __init__(self, all_words_file_path: Path | None = None,
                 result: GetAllWordsAsFileResultType = GetAllWordsAsFileResultType.Empty):
        self.all_words_file_path = all_words_file_path
        self.result: GetAllWordsAsFileResultType = result

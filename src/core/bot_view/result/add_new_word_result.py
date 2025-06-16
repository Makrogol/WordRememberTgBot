from enum import Enum

from src.core.intervals.intervals import Intervals
from src.core.word.word import Word


class AddNewWordResultType(Enum):
    Empty = 0
    CannotParseWord = 1
    CannotAddWordToFile = 2
    Success = 3


class AddNewWordResult:
    def __init__(self, word: Word | None = None, intervals: Intervals | None = None,
                 result: AddNewWordResultType = AddNewWordResultType.Empty):
        self.word = word
        self.intervals = intervals
        self.result: AddNewWordResultType = result

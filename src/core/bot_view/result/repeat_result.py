from src.core.intervals.intervals import Intervals
from src.core.word.word import Word

from enum import Enum


class RepeatResultType(Enum):
    Empty = 0
    CannotLoadWordsFromFile = 1
    IncorrectIndex = 2
    CannotParseNumber = 3
    Success = 4


class RepeatResult:
    def __init__(self, word: Word | None = None, intervals: Intervals | None = None,
                 result: RepeatResultType = RepeatResultType.Empty):
        self.word = word
        self.intervals = intervals
        self.result: RepeatResultType = result

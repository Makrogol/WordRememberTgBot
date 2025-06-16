from enum import Enum


class FixWordByNumberResultType(Enum):
    Empty = 0
    CannotParseNumberOrWord = 1
    CannotLoadWordsFromFile = 2
    IncorrectIndex = 3
    NoWords = 4
    Success = 5


class FixWordByNumberResult:
    def __init__(self, result: FixWordByNumberResultType = FixWordByNumberResultType.Empty):
        self.result: FixWordByNumberResultType = result

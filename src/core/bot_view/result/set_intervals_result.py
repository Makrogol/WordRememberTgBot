from enum import Enum


class SetIntervalsResultType(Enum):
    Empty = 0
    CannotParseIntervals = 1
    Success = 2


class SetIntervalsResult:
    def __init__(self, result: SetIntervalsResultType = SetIntervalsResultType.Empty):
        self.result: SetIntervalsResultType = result

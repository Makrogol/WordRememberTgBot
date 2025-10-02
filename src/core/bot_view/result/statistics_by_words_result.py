from enum import Enum

from src.core.paginated_message.paginated_message import PaginatedMessages


class StatisticsByWordsResultType(Enum):
    Empty = 0
    NoWords = 1
    Success = 2


class StatisticsByWordsResult:
    def __init__(self, paginated_messages: PaginatedMessages | None = None,
                 result: StatisticsByWordsResultType = StatisticsByWordsResultType.Empty):
        self.paginated_messages = paginated_messages
        self.result: StatisticsByWordsResultType = result

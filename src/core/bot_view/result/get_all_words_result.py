from src.core.paginated_message.paginated_message import PaginatedMessages

from enum import Enum


class GetAllWordsResultType(Enum):
    Empty = 0
    NoWords = 1
    Success = 2


class GetAllWordsResult:
    def __init__(self, paginated_messages: PaginatedMessages | None = None,
                 result: GetAllWordsResultType = GetAllWordsResultType.Empty):
        self.paginated_messages = paginated_messages
        self.result: GetAllWordsResultType = result

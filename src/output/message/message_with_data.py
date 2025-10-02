from typing import Any

from src.output.message.message import Message


# TODO ужасный костыль
class MessageWithData(Message):
    def __init__(self, text: str, data: dict[str, Any]):
        self.text = text
        self.data = data

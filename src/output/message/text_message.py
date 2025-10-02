from typing import List

from src.output.message.message import Message


class TextMessage(Message):
    def __init__(self, text: str):
        self.text = text


TextMessages = List[TextMessage]

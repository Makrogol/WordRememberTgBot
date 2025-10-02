from src.output.message.message import Message


class FileMessage(Message):
    def __init__(self, file_path: str, text: str):
        self.file_path = file_path
        self.text = text

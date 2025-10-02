from pathlib import Path


class MockBot(object):
    def __init__(self):
        self.__messages: list[str] = []
        self.__chat_ids: list[int] = []
        self.__documents: list[Path] = []
        self.__parse_modes: list[str] = []

    async def send_message(self, chat_id, text, parse_mode: str | None = None):
        self.__chat_ids.append(chat_id)
        self.__messages.append(text)
        if parse_mode is not None:
            self.__parse_modes.append(parse_mode)

    async def send_document(self, chat_id, document, caption):
        self.__chat_ids.append(chat_id)
        self.__documents.append(document)
        self.__messages.append(caption)

    def get_chat_ids(self):
        return self.__chat_ids

    def get_messages(self):
        return self.__messages

    def get_documents(self):
        return self.__documents

    def get_parse_modes(self):
        return self.__parse_modes

    def clear(self):
        self.__messages = []
        self.__chat_ids = []
        self.__documents = []
        self.__parse_modes = []

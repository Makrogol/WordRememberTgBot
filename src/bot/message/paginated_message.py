from src.bot.message.config import MAX_MESSAGE_LENGTH, MAX_MESSAGE_LENGTH_TEST


# Пагинация нужна для лучшей читабельности. Смысл такой
# Мы обрезаем сообщение, если оно не влезает в пагинацию
# Причем обрезаем так, чтобы кусок информации не делился,
# То есть, чтобы строки из пришедшего массива строк по возможности не разрывались
# Если такой возможности нет (то есть один пришедший мессадж больше макс длины), то
# Обрезаем его под макс длину

class PaginatedMessages:
    def __init__(self, max_message_length: int = MAX_MESSAGE_LENGTH_TEST):
        self.__max_message_length: int = max_message_length
        self.__paginated_messages: list[str] = []

    def add(self, messages: list[str]):
        for message in messages:
            self.append(message)

    def append(self, message: str):
        # TODO костыль
        if len(self.__paginated_messages) == 0 and len(message) <= self.__max_message_length:
            self.__paginated_messages.append('')

        if len(message) > self.__max_message_length:
            self.__paginated_messages.append(message[:self.__max_message_length])
            self.append(message[self.__max_message_length:])
        elif len(message) + len(self.__paginated_messages[-1]) > self.__max_message_length:
            self.__paginated_messages.append(message)
        else:
            self.__paginated_messages[-1] += message

    def get(self) -> list[str]:
        return self.__paginated_messages

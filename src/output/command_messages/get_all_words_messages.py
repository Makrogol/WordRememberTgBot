from src.output.message.text_message import TextMessages
from src.output.command_messages.common_messages import CommonMessages
from src.output.utils import create_output_words, convert_raw_messages_to_text_messages
from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command
from src.core.paginated_message.paginated_message import PaginatedMessages
from src.core.word.word import Word


class GetAllWordsMessages:
    COMMAND_TEXT = slash_command(Commands.GET_ALL_WORDS_COMMAND)

    COMMAND_EXAMPLE_TEXT = COMMAND_TEXT

    ERROR_DEFAULT_TEXT = 'Невозможно получить список всех слов\n'

    NO_WORDS_TEXT = f'{ERROR_DEFAULT_TEXT}{CommonMessages.NO_WORDS_TEXT}'

    SUCCESS_GET_ALL_WORDS_TEXT = 'Вот все твои слова'

    @staticmethod
    def no_words() -> TextMessages:
        return convert_raw_messages_to_text_messages(GetAllWordsMessages.NO_WORDS_TEXT)

    @staticmethod
    def success_get_all_words(words: list[Word]) -> TextMessages:
        paginated_messages = PaginatedMessages()
        paginated_messages.add(create_output_words(words))
        return convert_raw_messages_to_text_messages(
            [GetAllWordsMessages.SUCCESS_GET_ALL_WORDS_TEXT] + paginated_messages.get())

from src.output.command_messages.common_messages import CommonMessages
from src.output.message.text_message import TextMessage, TextMessages
from src.output.utils import convert_raw_messages_to_text_messages, get_statistics_by_words
from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command
from src.core.paginated_message.paginated_message import PaginatedMessages
from src.core.word.word import Words


class StatisticsByWordsMessages:
    COMMAND_TEXT = slash_command(Commands.STATISTICS_BY_WORDS_COMMAND)

    COMMAND_EXAMPLE_TEXT = COMMAND_TEXT

    NO_WORDS_TEXT = f'{CommonMessages.NO_WORDS_TEXT}'

    SUCCESS_STATISTICS_BY_WORDS_TEXT = 'Сколько раз ты повторял свои слова:\n\n'

    @staticmethod
    def no_words() -> TextMessages:
        return convert_raw_messages_to_text_messages(StatisticsByWordsMessages.NO_WORDS_TEXT)

    @staticmethod
    def success_statistics_by_words(words: Words) -> TextMessages:
        statistics = get_statistics_by_words(words)
        paginated_messages = PaginatedMessages()
        paginated_messages.add(statistics)
        return convert_raw_messages_to_text_messages(
            [TextMessage(text=StatisticsByWordsMessages.SUCCESS_STATISTICS_BY_WORDS_TEXT)] + paginated_messages.get()
        )

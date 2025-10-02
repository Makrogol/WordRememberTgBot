from src.output.command_messages.common_messages import CommonMessages
from src.output.message.message_with_data import MessageWithData
from src.output.message.text_message import TextMessage
from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command
from src.core.intervals.intervals import Intervals
from src.core.word.word import Word


class RepeatMessages:
    COMMAND_TEXT = slash_command(Commands.REPEAT_COMMAND)

    COMMAND_EXAMPLE_TEXT = f'{COMMAND_TEXT} 1'

    ERROR_DEFAULT_TEXT = 'Невозможно начать повторять слово по номеру\n'

    CANNOT_PARSE_NUMBER_TEXT = f'{ERROR_DEFAULT_TEXT}{CommonMessages.CANNOT_PARSE_TEXT}'

    CANNOT_LOAD_WORDS_FROM_FILE_TEXT = f'{ERROR_DEFAULT_TEXT}{CommonMessages.SOMETHING_WENT_WRONG_TEXT}'

    INCORRECT_INDEX_TEXT = f'{ERROR_DEFAULT_TEXT}{CommonMessages.INCORRECT_NUMBER_TEXT}'

    SUCCESS_REPEAT_TEXT = 'Отлично!\nЯ буду присылать тебе это слово по твоим интервалам'

    @staticmethod
    def cannot_parse_number() -> TextMessage:
        return TextMessage(text=RepeatMessages.CANNOT_PARSE_NUMBER_TEXT)

    @staticmethod
    def cannot_load_words_from_file() -> TextMessage:
        return TextMessage(text=RepeatMessages.CANNOT_LOAD_WORDS_FROM_FILE_TEXT)

    @staticmethod
    def incorrect_index() -> TextMessage:
        return TextMessage(text=RepeatMessages.INCORRECT_INDEX_TEXT)

    @staticmethod
    def success_repeat_message(word: Word, intervals: Intervals) -> MessageWithData:
        return MessageWithData(text=RepeatMessages.SUCCESS_REPEAT_TEXT, data={'word': word, 'intervals': intervals})

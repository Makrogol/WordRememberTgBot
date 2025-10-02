from src.output.message.message_with_data import MessageWithData
from src.output.message.text_message import TextMessage
from src.output.command_messages.common_messages import CommonMessages
from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command
from src.core.intervals.intervals import Intervals
from src.core.word.word import Word


class AddNewWordMessages:
    COMMAND_TEXT = slash_command(Commands.ADD_NEW_WORD_COMMAND)

    SHORT_COMMAND_TEXT = slash_command(Commands.ANW_COMMAND)

    COMMAND_EXAMPLE_TEXT = f'{COMMAND_TEXT} glass - стекло, бокал\n'

    COMMAND_EXAMPLE_WITH_SENTENCE_TEXT = f'{COMMAND_TEXT} glass - стекло, бокал - There is a cute glass\n'

    ERROR_DEFAULT_TEXT = 'Невозможно добавить новое слово\n'

    CANNOT_PARSE_WORD_TEXT = (f'{ERROR_DEFAULT_TEXT}{CommonMessages.CANNOT_PARSE_TEXT}'
                              'Возможно отсутствует разделяющий дефис (-), '
                              'либо ты забыл поставить пробелы вокруг разделяющего дефиса (-)')

    CANNOT_ADD_WORD_TO_FILE_TEXT = f'{ERROR_DEFAULT_TEXT}{CommonMessages.SOMETHING_WENT_WRONG_TEXT}'

    SUCCESS_ADDING_NEW_WORD_TEXT = 'Отлично!\nЯ записал новое слово и теперь буду помогать тебе его запоминать'

    @staticmethod
    def cannot_parse_word_message() -> TextMessage:
        return TextMessage(text=AddNewWordMessages.CANNOT_PARSE_WORD_TEXT)

    @staticmethod
    def cannot_add_word_to_file_message() -> TextMessage:
        return TextMessage(text=AddNewWordMessages.CANNOT_ADD_WORD_TO_FILE_TEXT)

    @staticmethod
    def success_add_new_word_message(word: Word, intervals: Intervals) -> MessageWithData:
        return MessageWithData(text=AddNewWordMessages.SUCCESS_ADDING_NEW_WORD_TEXT,
                               data={'word': word, 'intervals': intervals})

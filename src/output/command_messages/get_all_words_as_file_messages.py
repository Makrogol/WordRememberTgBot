from src.output.message.file_message import FileMessage
from src.output.message.text_message import TextMessage
from src.output.command_messages.common_messages import CommonMessages
from src.output.utils import create_output_words
from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command
from src.core.word.word import Word
from src.core.file_manager.tmp_file_manager import tmp_file_manager


class GetAllWordsAsFileMessages:
    COMMAND_TEXT = slash_command(Commands.GET_ALL_WORDS_AS_FILE_COMMAND)

    # TODO move this to some config
    WORDS_FILE_NAME = 'words.txt'

    COMMAND_EXAMPLE_TEXT = COMMAND_TEXT

    ERROR_DEFAULT_TEXT = 'Невозможно получить все твои слова в виде файла\n'

    NO_WORDS_TEXT = f'{ERROR_DEFAULT_TEXT}{CommonMessages.NO_WORDS_TEXT}'

    CANNOT_CREATE_OUTPUT_FILE_TEXT = f'{ERROR_DEFAULT_TEXT}{CommonMessages.SOMETHING_WENT_WRONG_TEXT}'

    SUCCESS_GET_ALL_WORDS_AS_FILE_TEXT = 'Вот все твои слова в виде файла'

    @staticmethod
    def no_words() -> TextMessage:
        return TextMessage(text=GetAllWordsAsFileMessages.NO_WORDS_TEXT)

    @staticmethod
    def success_get_all_words_as_file(words: list[Word]) -> TextMessage | FileMessage:
        words_file_path = tmp_file_manager.create_tmp_file(file_name=GetAllWordsAsFileMessages.WORDS_FILE_NAME,
                                                           file_data=create_output_words(words))
        if words_file_path is None:
            return TextMessage(text=GetAllWordsAsFileMessages.CANNOT_CREATE_OUTPUT_FILE_TEXT)
        return FileMessage(file_path=words_file_path, text=GetAllWordsAsFileMessages.SUCCESS_GET_ALL_WORDS_AS_FILE_TEXT)

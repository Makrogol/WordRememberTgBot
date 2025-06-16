from src.bot.messages.messages.common_messages import CommonMessages
from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command


class GetAllWordsAsFileMessages:
    COMMAND_TEXT = slash_command(Commands.GET_ALL_WORDS_AS_FILE_COMMAND)

    COMMAND_EXAMPLE_TEXT = COMMAND_TEXT

    ERROR_DEFAULT_TEXT = "Невозможно получить все твои слова в виде файла\n"

    NO_WORDS_TEXT = f"{ERROR_DEFAULT_TEXT}{CommonMessages.NO_WORDS_TEXT}"

    CANNOT_UPDATE_OUTPUT_FILE_TEXT = f"{ERROR_DEFAULT_TEXT}{CommonMessages.SOMETHING_WENT_WRONG_TEXT}"

    SUCCESS_GET_ALL_WORDS_AS_FILE_TEXT = "Вот все твои слова в виде файла"

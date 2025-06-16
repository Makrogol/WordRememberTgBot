from src.bot.messages.messages.common_messages import CommonMessages
from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command


class GetAllWordsMessages:
    COMMAND_TEXT = slash_command(Commands.GET_ALL_WORDS_COMMAND)

    COMMAND_EXAMPLE_TEXT = COMMAND_TEXT

    ERROR_DEFAULT_TEXT = "Невозможно получить список всех слов\n"

    NO_WORDS_TEXT = f"{ERROR_DEFAULT_TEXT}{CommonMessages.NO_WORDS_TEXT}"

    SUCCESS_GET_ALL_WORDS_TEXT = "Вот все твои слова"

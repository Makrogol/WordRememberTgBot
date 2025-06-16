from src.bot.messages.messages.common_messages import CommonMessages
from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command


class AddNewWordMessages:
    COMMAND_TEXT = slash_command(Commands.ADD_NEW_WORD_COMMAND)

    SHORT_COMMAND_TEXT = slash_command(Commands.ANW_COMMAND)

    COMMAND_EXAMPLE_TEXT = f"{COMMAND_TEXT} glass - стекло, бокал\n"

    COMMAND_EXAMPLE_WITH_SENTENCE_TEXT = f"{COMMAND_TEXT} glass - стекло, бокал - There is a cute glass\n"

    ERROR_DEFAULT_TEXT = "Невозможно добавить новое слово\n"

    CANNOT_PARSE_WORD_TEXT = (f"{ERROR_DEFAULT_TEXT}{CommonMessages.CANNOT_PARSE_TEXT}"
                              "Возможно отсутствует разделяющий дефис (-), "
                              "либо ты забыл поставить пробелы вокруг разделяющего дефиса (-)")

    CANNOT_ADD_WORDS_TO_FILE = f"{ERROR_DEFAULT_TEXT}{CommonMessages.SOMETHING_WENT_WRONG_TEXT}"

    SUCCESS_ADDING_NEW_WORD_TEXT = "Отлично!\nЯ записал новое слово и теперь буду помогать тебе его запоминать"

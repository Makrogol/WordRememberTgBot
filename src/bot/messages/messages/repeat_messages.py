from src.bot.messages.messages.common_messages import CommonMessages
from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command


class RepeatMessages:
    COMMAND_TEXT = slash_command(Commands.REPEAT_COMMAND)

    COMMAND_EXAMPLE_TEXT = f"{COMMAND_TEXT} 1"

    ERROR_DEFAULT_TEXT = "Невозможно начать повторять слово по номеру\n"

    CANNOT_PARSE_NUMBER_TEXT = f"{ERROR_DEFAULT_TEXT}{CommonMessages.CANNOT_PARSE_TEXT}"

    CANNOT_LOAD_WORDS_FROM_FILE_TEXT = f"{ERROR_DEFAULT_TEXT}{CommonMessages.SOMETHING_WENT_WRONG_TEXT}"

    INCORRECT_INDEX_TEXT = f"{ERROR_DEFAULT_TEXT}{CommonMessages.INCORRECT_NUMBER_TEXT}"

    SUCCESS_REPEAT_TEXT = "Отлично!\nЯ буду присылать тебе это слово по твоим интервалам"

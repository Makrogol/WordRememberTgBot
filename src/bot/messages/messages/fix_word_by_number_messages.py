from src.bot.messages.messages.common_messages import CommonMessages
from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command


class FixWordByNumberMessages:
    COMMAND_TEXT = slash_command(Commands.FIX_WORD_COMMAND)

    COMMAND_EXAMPLE_TEXT = f"{COMMAND_TEXT} 1 word - слово - Предложение состоит из слов"

    ERROR_DEFAULT_TEXT = "Невозможно изменить слово по его номеру\n"

    CANNOT_PARSE_NUMBER_OR_WORD = (f"{ERROR_DEFAULT_TEXT}{CommonMessages.CANNOT_PARSE_TEXT}"
                                   f"Пример команды: {COMMAND_EXAMPLE_TEXT}")

    NO_WORDS_TEXT = f"{ERROR_DEFAULT_TEXT}{CommonMessages.NO_WORDS_TEXT}"

    CANNOT_LOAD_WORDS_FROM_FILE_TEXT = f"{ERROR_DEFAULT_TEXT}{CommonMessages.SOMETHING_WENT_WRONG_TEXT}"

    INCORRECT_INDEX_TEXT = f"{ERROR_DEFAULT_TEXT}{CommonMessages.INCORRECT_NUMBER_TEXT}"

    SUCCESS_FIX_WORD_BY_NUMBER_TEXT = ("Слово было успешно заменено\n"
                                       "Ты можешь посмотреть список всех твоих слов командой /get_all_words")

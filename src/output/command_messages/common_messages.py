from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command


class CommonMessages:
    NO_WORDS_TEXT = ('У тебя в словаре совсем нет слов.\n Попробуй добавить их с помощью команды '
                     f'{slash_command(Commands.ANW_COMMAND)} или посмотри справку '
                     f'с помощью команды {slash_command(Commands.HELP_COMMAND)}')

    SOMETHING_WENT_WRONG_TEXT = 'Что-то пошло не так('

    INCORRECT_NUMBER_TEXT = ('Номер, который ты ввел не верный. '
                             'Либо это отрицательное число, либо слова с таким номером нет в твоем словаре')

    CANNOT_PARSE_TEXT = 'Скорее всего ты где-то ошибся при вводе\n'

    COMMAND_EXAMPLE_TEXT = 'Пример команды: '

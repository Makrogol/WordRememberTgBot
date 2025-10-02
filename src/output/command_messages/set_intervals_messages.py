from src.output.command_messages.common_messages import CommonMessages
from src.output.message.text_message import TextMessage
from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command


class SetIntervalsMessages:
    COMMAND_TEXT = slash_command(Commands.SET_INTERVALS_COMMAND)

    COMMAND_EXAMPLE_TEXT = f'{COMMAND_TEXT} 10s 20m 1h 4d 1d2h40m15s'

    ERROR_DEFAULT_TEXT = 'Невозможно установить твои интервалы повторения\n'

    CANNOT_PARSE_INTERVALS_TEXT = (f'{ERROR_DEFAULT_TEXT}{CommonMessages.CANNOT_PARSE_TEXT}'
                                   f'Пример команды: {COMMAND_EXAMPLE_TEXT}')

    SUCCESS_SET_INTERVALS_TEXT = ('Отлично!\nЯ записал новые интервалы и теперь '
                                  'буду тебе напоминать последующие слова заданным образом')

    @staticmethod
    def cannot_parse_intervals() -> TextMessage:
        return TextMessage(text=SetIntervalsMessages.CANNOT_PARSE_INTERVALS_TEXT)

    @staticmethod
    def success_set_intervals() -> TextMessage:
        return TextMessage(text=SetIntervalsMessages.SUCCESS_SET_INTERVALS_TEXT)

from src.output.message.text_message import TextMessage
from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command
from src.core.statistics.statistics import Statistics


class StatisticsMessages:
    COMMAND_TEXT = slash_command(Commands.STATISTICS_COMMAND)

    COMMAND_EXAMPLE_TEXT = COMMAND_TEXT

    SUCCESS_STATISTICS_TEXT = 'Статистика твоих действий:\n\n'

    @staticmethod
    def success_statistics(statistics: Statistics) -> TextMessage:
        return TextMessage(text=StatisticsMessages.SUCCESS_STATISTICS_TEXT + str(statistics))

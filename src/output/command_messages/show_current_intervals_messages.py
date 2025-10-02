from src.output.message.text_message import TextMessage
from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command
from src.core.intervals.intervals import Intervals


class ShowCurrentIntervalsMessages:
    COMMAND_TEXT = slash_command(Commands.SHOW_CURRENT_INTERVALS_COMMAND)

    COMMAND_EXAMPLE_TEXT = COMMAND_TEXT

    SUCCESS_SHOW_CURRENT_INTERVALS_TEXT = 'Твои текущие интервалы повторений: '

    @staticmethod
    def success_show_current_intervals(intervals: Intervals) -> TextMessage:
        return TextMessage(
            text=ShowCurrentIntervalsMessages.SUCCESS_SHOW_CURRENT_INTERVALS_TEXT + intervals.get_as_string())

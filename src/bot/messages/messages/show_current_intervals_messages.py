from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command


class ShowCurrentIntervalsMessages:
    COMMAND_TEXT = slash_command(Commands.SHOW_CURRENT_INTERVALS_COMMAND)

    COMMAND_EXAMPLE_TEXT = COMMAND_TEXT

    SUCCESS_SHOW_CURRENT_INTERVALS_TEXT = "Твои текущие интервалы повторений: "

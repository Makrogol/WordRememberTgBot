from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command


class StartMessages:
    COMMAND_TEXT = slash_command(Commands.START_COMMAND)

    COMMAND_EXAMPLE_TEXT = COMMAND_TEXT

    START_TEXT = ("Привет\nЯ бот для интервального повторения иностранных слов\n"
                  f"Чтобы посмотреть справку используй команду {slash_command(Commands.HELP_COMMAND)}\n")

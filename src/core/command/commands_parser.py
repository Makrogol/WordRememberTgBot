from src.core.command.commands import ALL_COMMANDS


def try_parse_command(args: list[str]) -> str | None:
    if len(args) == 0 or args[0] not in ALL_COMMANDS:
        return None
    return args[0]

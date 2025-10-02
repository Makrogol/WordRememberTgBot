from src.core.command.commands import ALL_COMMANDS_FULL_NAME


class Statistics:
    def __init__(self):
        self.command_statistics: dict[str, int] = {command: 0 for command in ALL_COMMANDS_FULL_NAME}

    def __str__(self):
        return 'Количество вызовов команд:\n' + '\n'.join(
            [f' - {command}: ' + str(count) for command, count in self.command_statistics.items()])

    def to_json(self) -> dict:
        return {
            'command_statistics': self.command_statistics,
        }

    def __eq__(self, other: 'Statistics') -> bool:
        return self.command_statistics == other.command_statistics

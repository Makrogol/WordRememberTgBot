from src.bot.messages.messages.common_messages import CommonMessages
from src.bot.messages.messages.help_messages import HelpMessages
from src.core.command.commands import ALL_COMMANDS_ATTRS


def get_help_message_attr_by_command_attr(command_attr: str):
    help_prefix = "HELP"
    text_postfix = "TEXT"
    command_postfix = "COMMAND"
    index_start_command_postfix = command_attr.index(command_postfix)
    command = command_attr[:index_start_command_postfix - 1]
    return help_prefix + "_" + command + "_" + text_postfix


HELP_MESSAGES_BY_COMMANDS = {
    getattr(CommonMessages, commands_attr): getattr(HelpMessages, get_help_message_attr_by_command_attr(commands_attr))
    for commands_attr in ALL_COMMANDS_ATTRS
}

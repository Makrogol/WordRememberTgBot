# Обязательно должны выглядеть как команда в верхнем регистре и постфикс _COMMAND, нужно для help_messages_by_commands
class Commands:
    ADD_NEW_WORD_COMMAND = "add_new_word"

    ANW_COMMAND = "anw"

    FIX_WORD_COMMAND = "fix_word"

    GET_ALL_WORDS_AS_FILE_COMMAND = "get_all_words_as_file"

    GET_ALL_WORDS_COMMAND = "get_all_words"

    HELP_COMMAND = "help"

    REPEAT_COMMAND = "repeat"

    SET_INTERVALS_COMMAND = "set_intervals"

    SHOW_CURRENT_INTERVALS_COMMAND = "show_current_intervals"

    START_COMMAND = "start"


ALL_COMMANDS_ATTRS = []
for command_attrs in Commands.__dict__.keys():
    if isinstance(command_attrs, str) and command_attrs[0] != "_":
        ALL_COMMANDS_ATTRS.append(command_attrs)

ALL_COMMANDS = []
for command_attrs in Commands.__dict__.values():
    if isinstance(command_attrs, str) and command_attrs[0] != "_":
        ALL_COMMANDS.append(command_attrs)

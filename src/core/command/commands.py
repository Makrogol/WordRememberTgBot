# Обязательно должны выглядеть как команда в верхнем регистре и постфикс _COMMAND, нужно для help_messages_by_commands
class Commands:
    ADD_NEW_WORD_COMMAND = "add_new_word"
    # TODO сделать элементы этого класса экземплярами отдельного класса Command, с полями типа full_name, short_name и тд
    ANW_COMMAND = "anw"

    FIX_WORD_COMMAND = "fix_word"

    GET_ALL_WORDS_AS_FILE_COMMAND = "get_all_words_as_file"

    GET_ALL_WORDS_COMMAND = "get_all_words"

    HELP_COMMAND = "help"

    REPEAT_COMMAND = "repeat"

    SET_INTERVALS_COMMAND = "set_intervals"

    SHOW_CURRENT_INTERVALS_COMMAND = "show_current_intervals"

    STATISTICS_COMMAND = "statistics"

    STATISTICS_BY_WORDS_COMMAND = "statistics_by_words"

    START_COMMAND = "start"


ALL_COMMANDS_ATTRS = []
for command_attrs in Commands.__dict__.keys():
    if isinstance(command_attrs, str) and command_attrs[0] != "_":
        ALL_COMMANDS_ATTRS.append(command_attrs)

ALL_COMMANDS = []
for command_attrs_key, command_attrs_value in Commands.__dict__.items():
    if isinstance(command_attrs_key, str) and command_attrs_key[0] != '_' and isinstance(command_attrs_value, str):
        ALL_COMMANDS.append(command_attrs_value)

# TODO удалить после того, как сделаем туду выше
ALL_COMMANDS_FULL_NAME = ALL_COMMANDS
idx = ALL_COMMANDS_FULL_NAME.index(Commands.ANW_COMMAND)
del ALL_COMMANDS[idx]

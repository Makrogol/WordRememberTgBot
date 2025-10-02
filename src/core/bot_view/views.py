from src.output.command_messages.add_new_word_messages import AddNewWordMessages
from src.output import FixWordByNumberMessages
from src.output import GetAllWordsAsFileMessages
from src.output.command_messages.get_all_words_messages import GetAllWordsMessages
from src.output.command_messages.help_messages import HelpMessages
from src.output.command_messages.repeat_messages import RepeatMessages
from src.output.command_messages.set_intervals_messages import SetIntervalsMessages
from src.output import ShowCurrentIntervalsMessages
from src.output.command_messages.start_messages import StartMessages
from src.output.command_messages.statistics_by_words_messages import StatisticsByWordsMessages
from src.output.command_messages.statistics_messages import StatisticsMessages
from src.output import HELP_MESSAGES_BY_COMMANDS
from src.output.message import Message, Messages
from src.output.message.text_message import TextMessage
from src.core.command.commands_parser import try_parse_command
from src.core.bot_view.view_data import ViewData
from src.core.intervals.intervals_parser import try_parse_intervals
from src.core.file_manager.user_data_manager import UserDataManager
from src.core.file_manager.words_manager import WordsManager
from src.core.user_data.user_data import UserData
from src.core.word.word import Words
from src.core.word.word_parser import try_parse_word, try_parse_number_and_word, try_parse_number


def add_new_word_view(view_data: ViewData) -> Message:
    user_data_manager = UserDataManager(view_data.user_identifier_data)
    user_data: UserData = user_data_manager.get_or_create_user_data()
    word = try_parse_word(view_data.args)
    if word is None:
        return AddNewWordMessages.cannot_parse_word_message()

    words_manager = WordsManager(view_data.user_identifier_data.id)
    word.update_counter()
    if not words_manager.try_add_word_to_file(word):
        return AddNewWordMessages.cannot_add_word_to_file_message()

    return AddNewWordMessages.success_add_new_word_message(word, user_data.intervals)


def fix_word_by_number_view(view_data: ViewData) -> Message:
    number, word = try_parse_number_and_word(view_data.args)
    if number is None or word is None:
        return FixWordByNumberMessages.cannot_parse_number_or_word()

    # Для пользователя нумерация начинается с 1
    idx = number - 1
    words_manager = WordsManager(view_data.user_identifier_data.id)
    if not words_manager.has_words():
        return FixWordByNumberMessages.no_words()

    words = words_manager.try_load_from_file()
    if words is None:
        return FixWordByNumberMessages.cannot_load_words_from_file()
    if 0 <= idx < len(words):
        words[idx] = word
        words_manager.save_to_file(words)
        return FixWordByNumberMessages.success_fix_word_by_number()
    # TODO сделать фичу, что если изменяешь слово по индексу, который сразу после последнего из имеющихся,
    #  то мы просто добавляем это слово в словарь
    else:
        return FixWordByNumberMessages.incorrect_index()


def get_all_words_as_file_view(view_data: ViewData) -> Message:
    words_manager = WordsManager(view_data.user_identifier_data.id)
    if not words_manager.has_words():
        return GetAllWordsAsFileMessages.no_words()

    return GetAllWordsAsFileMessages.success_get_all_words_as_file(words_manager.try_load_from_file())


def get_all_words_view(view_data: ViewData) -> Messages:
    words_manager = WordsManager(view_data.user_identifier_data.id)
    if not words_manager.has_words():
        return GetAllWordsMessages.no_words()

    return GetAllWordsMessages.success_get_all_words(words_manager.try_load_from_file())


def help_view(view_data: ViewData) -> Message:
    command: str | None = try_parse_command(view_data.args)
    if command is None:
        return TextMessage(text=HelpMessages.HELP_TEXT)

    return TextMessage(text=HELP_MESSAGES_BY_COMMANDS[command])


def repeat_view(view_data: ViewData) -> Message:
    number: int | None = try_parse_number(view_data.args)
    if number is None:
        return RepeatMessages.cannot_parse_number()

    idx = number - 1
    user_data_manager = UserDataManager(view_data.user_identifier_data)
    user_data: UserData = user_data_manager.get_or_create_user_data()

    words_manager = WordsManager(view_data.user_identifier_data.id)
    words: Words | None = words_manager.try_load_from_file()
    if words is None:
        return RepeatMessages.cannot_load_words_from_file()
    if 0 <= idx < len(words):
        word = words[idx]
        words[idx].update_counter()
        words_manager.save_to_file(words)
        return RepeatMessages.success_repeat_message(word, user_data.intervals)
    else:
        return RepeatMessages.incorrect_index()


def set_intervals_view(view_data: ViewData) -> Message:
    intervals = try_parse_intervals(view_data.args)
    if intervals is None:
        return SetIntervalsMessages.cannot_parse_intervals()

    user_data_manager = UserDataManager(view_data.user_identifier_data)
    user_data: UserData = user_data_manager.get_or_create_user_data()
    user_data.intervals = intervals
    user_data_manager.save_to_file(user_data)
    return SetIntervalsMessages.success_set_intervals()


def show_current_intervals_view(view_data: ViewData) -> Message:
    user_data_manager = UserDataManager(view_data.user_identifier_data)
    user_data: UserData = user_data_manager.get_or_create_user_data()
    return ShowCurrentIntervalsMessages.success_show_current_intervals(user_data.intervals)


def start_view(view_data: ViewData) -> Message:
    return TextMessage(text=StartMessages.START_TEXT)


def statistics_view(view_data: ViewData) -> Message:
    user_data_manager = UserDataManager(view_data.user_identifier_data)
    user_data: UserData = user_data_manager.get_or_create_user_data()
    return StatisticsMessages.success_statistics(user_data.statistics)


def statistics_by_words_view(view_data: ViewData) -> Messages:
    words_manager = WordsManager(view_data.user_identifier_data.id)
    words: Words | None = words_manager.try_load_from_file()
    if words is None:
        return StatisticsByWordsMessages.no_words()

    return StatisticsByWordsMessages.success_statistics_by_words(words)

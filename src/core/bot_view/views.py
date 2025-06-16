from src.core.bot_view.result.add_new_word_result import AddNewWordResult, AddNewWordResultType
from src.core.bot_view.result.fix_word_by_number_result import FixWordByNumberResult, FixWordByNumberResultType
from src.core.bot_view.result.get_all_words_as_file_result import GetAllWordsAsFileResult, \
    GetAllWordsAsFileResultType
from src.core.bot_view.result.get_all_words_result import GetAllWordsResult, GetAllWordsResultType
from src.core.bot_view.result.repeat_result import RepeatResult, RepeatResultType
from src.core.bot_view.result.set_intervals_result import SetIntervalsResult, SetIntervalsResultType
from src.core.paginated_message.paginated_message import PaginatedMessages
from src.core.bot_view.view_data import ViewData
from src.core.intervals.intervals_parser import try_parse_intervals
from src.core.file_manager.user_data_manager import UserDataManager
from src.core.file_manager.words_manager import WordsManager
from src.core.word.word_parser import try_parse_word, try_parse_number_and_word, try_parse_number


def add_new_word_view(view_data: ViewData) -> AddNewWordResult:
    user_data_manger = UserDataManager(view_data.user_id)
    user_data = user_data_manger.get_or_create_user_data(view_data.user_name)
    word = try_parse_word(view_data.args)
    if word is None:
        return AddNewWordResult(result=AddNewWordResultType.CannotParseWord)

    words_manager = WordsManager(view_data.user_id)
    if not words_manager.try_add_word_to_file(word):
        return AddNewWordResult(result=AddNewWordResultType.CannotAddWordToFile)

    return AddNewWordResult(word, user_data.intervals, AddNewWordResultType.Success)


def fix_word_by_number_view(view_data: ViewData) -> FixWordByNumberResult:
    number, word = try_parse_number_and_word(view_data.args)
    if number is None or word is None:
        return FixWordByNumberResult(result=FixWordByNumberResultType.CannotParseNumberOrWord)

    # Для пользователя нумерация начинается с 1
    idx = number - 1
    words_manager = WordsManager(view_data.user_id)
    if not words_manager.has_words():
        return FixWordByNumberResult(result=FixWordByNumberResultType.NoWords)

    words = words_manager.try_load_from_file()
    if words is None:
        return FixWordByNumberResult(result=FixWordByNumberResultType.CannotLoadWordsFromFile)
    if 0 <= idx < len(words):
        words[idx] = word
        words_manager.save_to_file(words)
        return FixWordByNumberResult(result=FixWordByNumberResultType.Success)
    # TODO сделать фичу, что если изменяешь слово по индексу, который сразу после последнего из имеющихся,
    #  то мы просто добавляем это слово в словарь
    else:
        return FixWordByNumberResult(result=FixWordByNumberResultType.IncorrectIndex)


def get_all_words_as_file_view(view_data: ViewData) -> GetAllWordsAsFileResult:
    words_manager = WordsManager(view_data.user_id)
    if not words_manager.try_update_words_output_file():
        return GetAllWordsAsFileResult(result=GetAllWordsAsFileResultType.CannotUpdateOutputFile)

    if not words_manager.has_words():
        return GetAllWordsAsFileResult(result=GetAllWordsAsFileResultType.NoWords)

    return GetAllWordsAsFileResult(words_manager.get_words_output_file_path(), GetAllWordsAsFileResultType.Success)


def get_all_words_view(view_data: ViewData) -> GetAllWordsResult:
    words_manager = WordsManager(view_data.user_id)
    if not words_manager.has_words():
        return GetAllWordsResult(result=GetAllWordsResultType.NoWords)

    words = words_manager.try_load_words_from_output_file()
    paginated_messages = PaginatedMessages()
    paginated_messages.add(words)
    return GetAllWordsResult(paginated_messages, GetAllWordsResultType.Success)


def repeat_view(view_data: ViewData) -> RepeatResult:
    number = try_parse_number(view_data.args)
    if number is None:
        return RepeatResult(result=RepeatResultType.CannotParseNumber)

    idx = number - 1
    user_data_manger = UserDataManager(view_data.user_id)
    user_data = user_data_manger.get_or_create_user_data(view_data.user_name)

    words_manager = WordsManager(view_data.user_id)
    words = words_manager.try_load_from_file()
    if words is None:
        return RepeatResult(result=RepeatResultType.CannotLoadWordsFromFile)
    if 0 <= idx < len(words):
        word = words[idx]
        return RepeatResult(word, user_data.intervals, RepeatResultType.Success)
    else:
        return RepeatResult(result=RepeatResultType.IncorrectIndex)


def set_intervals_view(view_data: ViewData) -> SetIntervalsResult:
    intervals = try_parse_intervals(view_data.args)
    if intervals is None:
        return SetIntervalsResult(result=SetIntervalsResultType.CannotParseIntervals)

    user_data_manger = UserDataManager(view_data.user_id)
    user_data = user_data_manger.get_or_create_user_data(view_data.user_name)
    user_data.intervals = intervals
    user_data_manger.save_to_file(user_data)
    return SetIntervalsResult(result=SetIntervalsResultType.Success)

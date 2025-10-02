from src.output.command_messages.add_new_word_messages import AddNewWordMessages
from src.output.command_messages.common_messages import CommonMessages
from src.output.command_messages.fix_word_by_number_messages import FixWordByNumberMessages
from src.output.command_messages.get_all_words_as_file_messages import GetAllWordsAsFileMessages
from src.output.command_messages.get_all_words_messages import GetAllWordsMessages
from src.output.command_messages.repeat_messages import RepeatMessages
from src.output.command_messages.set_intervals_messages import SetIntervalsMessages
from src.output.command_messages.show_current_intervals_messages import ShowCurrentIntervalsMessages
from src.output.command_messages.statistics_by_words_messages import StatisticsByWordsMessages
from src.output.command_messages.statistics_messages import StatisticsMessages
from src.output.command_messages.start_messages import StartMessages
from src.core.command.commands import Commands
from src.core.command.slash_commands import slash_command


# Обязательно справка по конкретной команде должна выглядеть как HELP_ дальше команда в верхнем регистре и дальше _TEXT
# Нужно для help_messages_by_commands
class HelpMessages:
    COMMAND_TEXT = slash_command(Commands.HELP_COMMAND)

    COMMAND_EXAMPLE_TEXT = f'{COMMAND_TEXT} set_intervals'

    HELP_ADD_NEW_WORD_TEXT = (f'{AddNewWordMessages.COMMAND_TEXT} - добавит новое слово для повторения. '
                              'Я буду отправлять его тебе через некоторые промежутки времени. '
                              'Случайная часть слова будет закрыта спойлером, чтобы ты мог проверить свои знания. '
                              f'Для краткости можно использовать команду {AddNewWordMessages.SHORT_COMMAND_TEXT} '
                              'она делает ровно тоже самое.\n'
                              'Как добавить новое слово: ты пишешь команду, дальше через пробел слово '
                              '(или несколько слов), '
                              'дальше пробел, дальше дефис (-), дальше перевод слова (или несколько слов). '
                              'Дальше опционально можно добавить предложение, которое я буду присылать вместе '
                              'с повторением слова. '
                              'Добавлять предложение так: после перевода слова пробел, дальше дефис, '
                              'дальше предложение (или несколько).'
                              'При повторении слов я буду тебе отправлять случайную часть слова '
                              '(левую или правую) под спойлером, '
                              'а предложение - без спойлера, чтобы ты мог сразу закрепить слово.\n'
                              f'{CommonMessages.COMMAND_EXAMPLE_TEXT}{AddNewWordMessages.COMMAND_EXAMPLE_TEXT}'
                              f'Пример команды с предложением: '
                              f'{AddNewWordMessages.COMMAND_EXAMPLE_WITH_SENTENCE_TEXT}\n')

    HELP_ANW_TEXT = HELP_ADD_NEW_WORD_TEXT

    HELP_FIX_WORD_TEXT = (f'{FixWordByNumberMessages.COMMAND_TEXT} - позволяет изменить слово в '
                          'твоем словаре по его номеру. '
                          'Надо ввести номер слова и новое слово, которое ты хочешь вставить на место этого\n'
                          f'{CommonMessages.COMMAND_EXAMPLE_TEXT}{FixWordByNumberMessages.COMMAND_EXAMPLE_TEXT}\n')

    HELP_GET_ALL_WORDS_AS_FILE_TEXT = (f'{GetAllWordsAsFileMessages.COMMAND_TEXT} - '
                                       'пришлет тебе файл со списком всех слов, которые ты когда-либо мне отправлял\n'
                                       f'{CommonMessages.COMMAND_EXAMPLE_TEXT}'
                                       f'{GetAllWordsAsFileMessages.COMMAND_EXAMPLE_TEXT}\n')

    HELP_GET_ALL_WORDS_TEXT = (f'{GetAllWordsMessages.COMMAND_TEXT} - выведет тебе список всех слов, '
                               'которые ты когда либо мне отправлял\n'
                               f'{CommonMessages.COMMAND_EXAMPLE_TEXT}{GetAllWordsMessages.COMMAND_EXAMPLE_TEXT}\n')

    HELP_HELP_TEXT = (f'{COMMAND_TEXT} - выведет тебе список моих доступных команд и краткое описание к ним. '
                      'Для полного описания можешь воспользоваться справкой по конкретной команде. '
                      f'Для этого используй команду {COMMAND_TEXT} и через пробел передай название команды, '
                      'про которую хочешь узнать больше\n'
                      f'{CommonMessages.COMMAND_EXAMPLE_TEXT}{COMMAND_EXAMPLE_TEXT}\n')

    HELP_REPEAT_TEXT = (f'{RepeatMessages.COMMAND_TEXT} - позволяет начать повторять слово по '
                        'его номеру в твоем словаре. Я буду присылать тебе его по твоим интервалам\n'
                        f'{CommonMessages.COMMAND_EXAMPLE_TEXT}{RepeatMessages.COMMAND_EXAMPLE_TEXT}\n')

    HELP_SET_INTERVALS_TEXT = (f'{SetIntervalsMessages.COMMAND_TEXT} - позволяет установить новый интервал, '
                               f'по которому я буду присылать тебе слова. '
                               'Обрати внимание, что по новому интервалу будут присылаться только новые слова. '
                               'Те, которые я тебе уже отправляю, продолжу отправлять по прежнему расписанию\n'
                               f'{CommonMessages.COMMAND_EXAMPLE_TEXT}{SetIntervalsMessages.COMMAND_EXAMPLE_TEXT}\n')

    HELP_SHOW_CURRENT_INTERVALS_TEXT = (f'{ShowCurrentIntervalsMessages.COMMAND_TEXT} - покажет тебе текущий интервал, '
                                        'по которому я буду присылать тебе слова\n'
                                        f'{CommonMessages.COMMAND_EXAMPLE_TEXT}'
                                        f'{ShowCurrentIntervalsMessages.COMMAND_EXAMPLE_TEXT}\n')

    HELP_STATISTICS_TEXT = f'{StatisticsMessages.COMMAND_TEXT} - покажет тебе статистику твоих действий\n'

    HELP_STATISTICS_BY_WORDS_TEXT = (f'{StatisticsByWordsMessages.COMMAND_TEXT} - '
                                     f'показывает тебе сколько раз ты повторял каждое слово\n')

    HELP_START_TEXT = (f'{StartMessages.COMMAND_TEXT} - начинает работу бота\n'
                       f'{CommonMessages.COMMAND_EXAMPLE_TEXT}{StartMessages.COMMAND_EXAMPLE_TEXT}\n')

    HELP_TEXT = (f'{AddNewWordMessages.COMMAND_TEXT} - добавит новое слово для повторения\n\n'
                 f'{GetAllWordsMessages.COMMAND_TEXT} - выведет тебе список всех слов, '
                 'которые ты когда либо мне отправлял\n\n'
                 f'{GetAllWordsAsFileMessages.COMMAND_TEXT} - пришлет тебе файл со списком всех слов, '
                 'которые ты когда-либо мне отправлял\n\n'
                 f'{SetIntervalsMessages.COMMAND_TEXT} - позволяет установить новый интервал, '
                 'по которому я буду присылать тебе слова\n\n'
                 f'{ShowCurrentIntervalsMessages.COMMAND_TEXT} - покажет тебе текущий интервал, '
                 'по которому я буду присылать тебе слова\n\n'
                 f'{FixWordByNumberMessages.COMMAND_TEXT} - позволяет изменить слово в твоем словаре по его номеру\n\n'
                 f'{RepeatMessages.COMMAND_TEXT} - позволяет начать повторение слова из твоего словаря по номеру\n\n'
                 f'{StatisticsMessages.COMMAND_TEXT} - показывает статистику твоих действий\n\n'
                 f'{StatisticsByWordsMessages.COMMAND_TEXT} - показывает тебе сколько раз ты повторял каждое слово\n\n'
                 f'{StartMessages.COMMAND_TEXT} - начинает работу бота\n\n'
                 f'{HELP_HELP_TEXT}')

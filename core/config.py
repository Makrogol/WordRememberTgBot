from pathlib import Path
from datetime import timedelta

# Intervals of timer tic in seconds
# 20 min = 20 * 60 = 1200 sec
# 1 hour = 1 * 60 * 60 = 3600 sec
# 8 hours = 8 * 60 * 60 = 28800 sec
# 1 day = 24 * 60 * 60 = 86400 sec
# 4 days = 4 * 24 * 60 * 60 = 345600 sec
INTERVALS = [timedelta(seconds=1200), timedelta(seconds=3600), timedelta(seconds=28800), timedelta(seconds=86400),
             timedelta(seconds=345600)]
INTERVALS_TEXT = '20m 1h 8h 1d 4d'

INTERVALS_TEST = [timedelta(seconds=1), timedelta(seconds=2), timedelta(seconds=10), timedelta(seconds=20)]
INTERVALS_TEST_TEXT = '1s 2s 10s 20s'

MAX_MESSAGE_LENGTH = 4096
MAX_MESSAGE_LENGTH_TEST = 30

BASE_PATH = Path(__file__).parent.parent
USER_WORD_DATA_DIRECTORY_NAME = "user_word_data"
USER_WORD_DATA_PATH = BASE_PATH / USER_WORD_DATA_DIRECTORY_NAME

SET_INTERVALS_COMMAND_EXAMPLE_TEXT = "/set_interval 10s 20m 1h 4d 1d2h40m15s"

HELP_TEXT = ("/add_new_word - добавит новое слово для повторения. "
             "Я буду отправлять его тебе через некоторые промежутки времени. "
             "Случайная часть слова будет закрыта спойлером, чтобы ты мог проверить свои знания. "
             "Пример команды: /add_new_word glass - стекло, бокал\n"
             "/get_all_words - выведет тебе список всех слов, которые ты когда либо мне отправлял\n"
             "/get_all_words_as_file - пришлет тебе файл со списком всех слов, которые ты когда-либо мне отправлял\n"
             "/set_intervals - позволяет установить новый интервал, по которому я буду присылать тебе слова. "
             "Обрати внимание, что по новому интервалу будут присылаться только новые слова. "
             "Те, которые я уже тебе отправляю буду отправлять по прежнему расписанию. "
             f"Пример команды: {SET_INTERVALS_COMMAND_EXAMPLE_TEXT}\n"
             "/show_current_intervals - покажет тебе текущий интервал, по которому я буду присылать тебе слова\n"
             "/help - выведет тебе список моих доступных команд")

START_TEXT = "Привет! Я бот для интервального повторения иностранных слов\n\n" + HELP_TEXT

BAD_ADDING_NEW_WORD_TEXT = ("Невозможно добавить новое слово\nЛибо отсутствует разделяющий дефис (-), "
                            "либо правая или левая часть слова пустые")

BAD_SETTING_INTERVALS_TEXT = ("Невозможно установить твои интервалы повторения. "
                              "Скорее всего ты где-то ошибся при вводе или ввел отрицательное число. "
                              f"Вот пример корректной команды: {SET_INTERVALS_COMMAND_EXAMPLE_TEXT}")

SHOW_CURRENT_INTERVALS_TEXT = "Твои текущие интервалы повторений: "

ADDING_NEW_WORD_TEXT = "Отлично! Я записал новое слово и теперь буду помогать тебе его запоминать"

SET_INTERVALS_TEXT = ("Отлично! Я записал новые интервалы и теперь "
                      "буду тебе напоминать последующие слова заданным образом")

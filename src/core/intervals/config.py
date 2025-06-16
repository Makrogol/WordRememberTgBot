from datetime import timedelta

# Intervals of timer tic in seconds
# 20 min = 20 * 60 = 1200 sec
# 1 hour = 1 * 60 * 60 = 3600 sec
# 8 hours = 8 * 60 * 60 = 28800 sec
# 1 day = 24 * 60 * 60 = 86400 sec
# 4 days = 4 * 24 * 60 * 60 = 345600 sec
# TODO сделать ограничение на размер вводимого интервала
INTERVALS_AS_TIMEDELTA = [timedelta(seconds=1200), timedelta(seconds=3600), timedelta(seconds=28800),
                          timedelta(seconds=86400),
                          timedelta(seconds=345600)]
INTERVALS_AS_LETTERS = ['20m', '1h', '8h', '1d', '4d']
INTERVALS_AS_STRING = '20m 1h 8h 1d 4d'

INTERVALS_AS_TIMEDELTA_TEST = [timedelta(seconds=1), timedelta(seconds=2), timedelta(seconds=5), timedelta(seconds=10)]
INTERVALS_AS_LETTERS_TEST = ['1s', '2s', '5s', '10s']
INTERVALS_AS_STRING_TEST = '1s 2s 5s 10s'

TIME_LETTERS = ['s', 'm', 'h', 'd']

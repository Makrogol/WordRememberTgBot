import unittest
from datetime import timedelta

from core.intervals.intervals import Intervals

DUMMY_INTERVALS_AS_LETTERS: list[str] = []
DUMMY_INTERVALS_AS_TIMEDELTA: list[timedelta] = []

class IntervalsTestCase(unittest.TestCase):

    def test_accumulate_sum_seconds(self):
        expected_result = [timedelta(seconds=10), timedelta(seconds=20), timedelta(seconds=40)]
        intervals_as_timedelta = [timedelta(seconds=10), timedelta(seconds=10), timedelta(seconds=20)]
        intervals = Intervals(intervals_as_letters=DUMMY_INTERVALS_AS_LETTERS,
                              intervals_as_timedelta=intervals_as_timedelta)

        self.assertEqual(expected_result, intervals.get_as_timedelta_accumulate_sum())

    def test_accumulate_sum_minutes(self):
        expected_result = [timedelta(minutes=4), timedelta(minutes=10), timedelta(minutes=23)]
        intervals_as_timedelta = [timedelta(minutes=4), timedelta(minutes=6), timedelta(minutes=13)]
        intervals = Intervals(intervals_as_letters=DUMMY_INTERVALS_AS_LETTERS,
                              intervals_as_timedelta=intervals_as_timedelta)

        self.assertEqual(expected_result, intervals.get_as_timedelta_accumulate_sum())

    def test_accumulate_sum_hours(self):
        expected_result = [timedelta(hours=10), timedelta(hours=17), timedelta(hours=18), timedelta(hours=22)]
        intervals_as_timedelta = [timedelta(hours=10), timedelta(hours=7), timedelta(hours=1), timedelta(hours=4)]
        intervals = Intervals(intervals_as_letters=DUMMY_INTERVALS_AS_LETTERS,
                              intervals_as_timedelta=intervals_as_timedelta)

        self.assertEqual(expected_result, intervals.get_as_timedelta_accumulate_sum())

    def test_accumulate_sum_days(self):
        expected_result = [timedelta(days=2), timedelta(days=8), timedelta(days=14), timedelta(days=23)]
        intervals_as_timedelta = [timedelta(days=2), timedelta(days=6), timedelta(days=6), timedelta(days=9)]
        intervals = Intervals(intervals_as_letters=DUMMY_INTERVALS_AS_LETTERS,
                              intervals_as_timedelta=intervals_as_timedelta)

        self.assertEqual(expected_result, intervals.get_as_timedelta_accumulate_sum())

    def test_accumulate_sum_complex_time_updating_sum_with_new_time_type(self):
        # В первом интервале только секунды и часы, во втором дни и минуты, а в третьем все вместе
        # Так проверяется, что при суммировании добавляются новые типы времени
        # (были секунды и часы, а потом появились минуты и дни)
        expected_result = [timedelta(seconds=10, hours=4), timedelta(seconds=10, minutes=10, hours=4, days=6),
                           timedelta(seconds=20, minutes=27, hours=6, days=12)]
        intervals_as_timedelta = [timedelta(seconds=10, hours=4), timedelta(minutes=10, days=6),
                                  timedelta(seconds=10, minutes=17, hours=2, days=6)]
        intervals = Intervals(intervals_as_letters=DUMMY_INTERVALS_AS_LETTERS,
                              intervals_as_timedelta=intervals_as_timedelta)

        self.assertEqual(expected_result, intervals.get_as_timedelta_accumulate_sum())

    def test_accumulate_sum_second_overflow(self):
        # Тут проверяется, что если у нас было в первом интервале 20 секунд, а во втором 55 секунд,
        # то в сумме будет +1 минута и +15 секунд
        expected_result = [timedelta(seconds=20, hours=4), timedelta(seconds=15, minutes=1, hours=4)]
        intervals_as_timedelta = [timedelta(seconds=20, hours=4), timedelta(seconds=55)]
        intervals = Intervals(intervals_as_letters=DUMMY_INTERVALS_AS_LETTERS,
                              intervals_as_timedelta=intervals_as_timedelta)

        self.assertEqual(expected_result, intervals.get_as_timedelta_accumulate_sum())

    def test_accumulate_sum_minute_overflow(self):
        # Тут проверяется, что если у нас было в первом интервале 20 минут, а во втором 55 минут,
        # то в сумме будет +1 час и +15 минут
        expected_result = [timedelta(minutes=20), timedelta(minutes=15, hours=1)]
        intervals_as_timedelta = [timedelta(minutes=20), timedelta(minutes=55)]
        intervals = Intervals(intervals_as_letters=DUMMY_INTERVALS_AS_LETTERS,
                              intervals_as_timedelta=intervals_as_timedelta)

        self.assertEqual(expected_result, intervals.get_as_timedelta_accumulate_sum())

    def test_accumulate_sum_hour_overflow(self):
        # Тут проверяется, что если у нас было в первом интервале 20 часов, а во втором 5 часов,
        # то в сумме будет +1 день и +1 час
        expected_result = [timedelta(hours=20), timedelta(hours=1, days=1)]
        intervals_as_timedelta = [timedelta(hours=20), timedelta(hours=5)]
        intervals = Intervals(intervals_as_letters=DUMMY_INTERVALS_AS_LETTERS,
                              intervals_as_timedelta=intervals_as_timedelta)

        self.assertEqual(expected_result, intervals.get_as_timedelta_accumulate_sum())

    def test_accumulate_sum_complex_time_overflow(self):
        # Тут проверяется, что переполнение по всем видам времени
        expected_result = [timedelta(seconds=20, minutes=20, hours=20),
                           timedelta(seconds=15, minutes=16, hours=2, days=1)]
        intervals_as_timedelta = [timedelta(seconds=20, minutes=20, hours=20),
                                  timedelta(seconds=55, minutes=55, hours=5)]
        intervals = Intervals(intervals_as_letters=DUMMY_INTERVALS_AS_LETTERS,
                              intervals_as_timedelta=intervals_as_timedelta)

        self.assertEqual(expected_result, intervals.get_as_timedelta_accumulate_sum())

    def test_accumulate_sum_complex_time(self):
        expected_result = [timedelta(seconds=20, minutes=20, hours=20, days=20),
                           timedelta(seconds=21, minutes=21, hours=21, days=21)]
        intervals_as_timedelta = [timedelta(seconds=20, minutes=20, hours=20, days=20),
                                  timedelta(seconds=1, minutes=1, hours=1, days=1)]
        intervals = Intervals(intervals_as_letters=DUMMY_INTERVALS_AS_LETTERS,
                              intervals_as_timedelta=intervals_as_timedelta)

        self.assertEqual(expected_result, intervals.get_as_timedelta_accumulate_sum())

    def test_accumulate_sum_empty_intervals(self):
        expected_result = DUMMY_INTERVALS_AS_TIMEDELTA
        intervals = Intervals(intervals_as_letters=DUMMY_INTERVALS_AS_LETTERS,
                              intervals_as_timedelta=DUMMY_INTERVALS_AS_TIMEDELTA)

        self.assertEqual(expected_result, intervals.get_as_timedelta_accumulate_sum())

    def test_intervals_as_string(self):
        expected_result = '1s 2m 3d'
        intervals_as_letters = ['1s', '2m', '3d']
        intervals = Intervals(intervals_as_letters=intervals_as_letters,
                              intervals_as_timedelta=DUMMY_INTERVALS_AS_TIMEDELTA)

        self.assertEqual(expected_result, intervals.get_as_string())

    def test_intervals_as_string_empty(self):
        expected_result = ''
        intervals = Intervals(intervals_as_letters=DUMMY_INTERVALS_AS_LETTERS,
                              intervals_as_timedelta=DUMMY_INTERVALS_AS_TIMEDELTA)

        self.assertEqual(expected_result, intervals.get_as_string())


if __name__ == '__main__':
    unittest.main()

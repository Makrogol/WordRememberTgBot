import unittest
from datetime import timedelta
from string import punctuation, ascii_letters

from src.core.intervals.config import TIME_LETTERS
from src.core.intervals.intervals import Intervals
from src.core.intervals.intervals_parser import try_parse_intervals


class IntervalParserTestCase(unittest.TestCase):

    def test_empty_args(self):
        self.assertIsNone(try_parse_intervals([]))

    def assert_equal_intervals_after_parsing(self, intervals_as_letters, intervals_as_timedelta):
        expected_result = Intervals(intervals_as_letters=intervals_as_letters,
                                    intervals_as_timedelta=intervals_as_timedelta)
        real_result = try_parse_intervals(intervals_as_letters)

        self.assertEqual(expected_result, real_result)

    def test_one_interval(self):
        self.assert_equal_intervals_after_parsing(intervals_as_letters=['1s'],
                                                  intervals_as_timedelta=[timedelta(seconds=1)])

    def test_many_intervals(self):
        self.assert_equal_intervals_after_parsing(intervals_as_letters=['1s', '2s', '3s'],
                                                  intervals_as_timedelta=[timedelta(seconds=1), timedelta(seconds=2),
                                                                          timedelta(seconds=3)])

    def test_minutes(self):
        self.assert_equal_intervals_after_parsing(intervals_as_letters=['10m'],
                                                  intervals_as_timedelta=[timedelta(minutes=10)])

    def test_hours(self):
        self.assert_equal_intervals_after_parsing(intervals_as_letters=['8h'],
                                                  intervals_as_timedelta=[timedelta(hours=8)])

    def test_days(self):
        self.assert_equal_intervals_after_parsing(intervals_as_letters=['3d'],
                                                  intervals_as_timedelta=[timedelta(days=3)])

    def test_different_time_intervals(self):
        self.assert_equal_intervals_after_parsing(intervals_as_letters=['3d', '1s', '2m', '10h'],
                                                  intervals_as_timedelta=[timedelta(days=3), timedelta(seconds=1),
                                                                          timedelta(minutes=2), timedelta(hours=10)])

    def test_complex_time(self):
        self.assert_equal_intervals_after_parsing(intervals_as_letters=['3d10m5h40s'],
                                                  intervals_as_timedelta=[
                                                      timedelta(days=3, minutes=10, hours=5, seconds=40)])

    def test_complex_time_another_order(self):
        self.assert_equal_intervals_after_parsing(intervals_as_letters=['10m3d40s5h'],
                                                  intervals_as_timedelta=[
                                                      timedelta(days=3, minutes=10, hours=5, seconds=40)])

    def test_minus_time(self):
        self.assertIsNone(try_parse_intervals(['-10m']))

    def test_minus_time_in_complex_time(self):
        self.assertIsNone(try_parse_intervals(['1h-10m30d']))

    def test_not_alpha_and_not_digit_in_time(self):
        for el in punctuation:
            self.assertIsNone(try_parse_intervals([el]))

    def test_not_time_alpha(self):
        for el in ascii_letters:
            if el not in TIME_LETTERS:
                self.assertIsNone(try_parse_intervals([f'1{el}']))

    def test_many_days(self):
        self.assert_equal_intervals_after_parsing(intervals_as_letters=['500d'],
                                                  intervals_as_timedelta=[timedelta(days=500)])

    def test_empty_num_of_time(self):
        self.assertIsNone(try_parse_intervals(['m']))

    def test_zero_num_of_time(self):
        self.assert_equal_intervals_after_parsing(intervals_as_letters=['0d'],
                                                  intervals_as_timedelta=[timedelta(days=0)])

    def test_zero_num_of_time_in_complex_time(self):
        self.assert_equal_intervals_after_parsing(intervals_as_letters=['0d10m0h'],
                                                  intervals_as_timedelta=[timedelta(days=0, hours=0, minutes=10)])


if __name__ == '__main__':
    unittest.main()

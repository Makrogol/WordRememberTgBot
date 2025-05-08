import unittest
from string import punctuation, ascii_letters

from core.intervals_parser import *


class IntervalParserTestCase(unittest.TestCase):

    def test_empty_args(self):
        self.assertIsNone(IntervalsParser.try_parse_intervals([]))

    def test_one_interval(self):
        expected_result = [timedelta(seconds=1)]
        real_result = IntervalsParser.try_parse_intervals(['1s'])

        self.assertEqual(expected_result, real_result)

    def test_many_intervals(self):
        expected_result = [timedelta(seconds=1), timedelta(seconds=2), timedelta(seconds=3)]
        real_result = IntervalsParser.try_parse_intervals(['1s', '2s', '3s'])

        self.assertEqual(expected_result, real_result)

    def test_minutes(self):
        expected_result = [timedelta(minutes=10)]
        real_result = IntervalsParser.try_parse_intervals(['10m'])

        self.assertEqual(expected_result, real_result)

    def test_hours(self):
        expected_result = [timedelta(hours=8)]
        real_result = IntervalsParser.try_parse_intervals(['8h'])

        self.assertEqual(expected_result, real_result)

    def test_days(self):
        expected_result = [timedelta(days=3)]
        real_result = IntervalsParser.try_parse_intervals(['3d'])

        self.assertEqual(expected_result, real_result)

    def test_different_time_intervals(self):
        expected_result = [timedelta(days=3), timedelta(seconds=1), timedelta(minutes=2), timedelta(hours=10)]
        real_result = IntervalsParser.try_parse_intervals(['3d', '1s', '2m', '10h'])

        self.assertEqual(expected_result, real_result)

    def test_complex_time(self):
        expected_result = [timedelta(days=3, minutes=10, hours=5, seconds=40)]
        real_result = IntervalsParser.try_parse_intervals(['3d10m5h40s'])

        self.assertEqual(expected_result, real_result)

    def test_complex_time_another_order(self):
        expected_result = [timedelta(days=3, minutes=10, hours=5, seconds=40)]
        real_result = IntervalsParser.try_parse_intervals(['10m3d40s5h'])

        self.assertEqual(expected_result, real_result)

    def test_minus_time(self):
        self.assertIsNone(IntervalsParser.try_parse_intervals(['-10m']))

    def test_minus_time_in_complex_time(self):
        self.assertIsNone(IntervalsParser.try_parse_intervals(['1h-10m30d']))

    def test_not_alpha_and_not_digit_in_time(self):
        for el in punctuation:
            self.assertIsNone(IntervalsParser.try_parse_intervals([el]))

    def test_not_time_alpha(self):
        for el in ascii_letters:
            if el not in TIME_LETTERS:
                self.assertIsNone(IntervalsParser.try_parse_intervals([f'1{el}']))

    def test_many_days(self):
        expected_result = [timedelta(days=500)]
        real_result = IntervalsParser.try_parse_intervals(['500d'])

        self.assertEqual(expected_result, real_result)

    def test_empty_num_of_time(self):
        self.assertIsNone(IntervalsParser.try_parse_intervals(['m']))

    def test_zero_num_of_time(self):
        expected_result = [timedelta(days=0)]
        real_result = IntervalsParser.try_parse_intervals(['0d'])

        self.assertEqual(expected_result, real_result)

    def test_zero_num_of_time_in_complex_time(self):
        expected_result = [timedelta(days=0, hours=0, minutes=10)]
        real_result = IntervalsParser.try_parse_intervals(['0d10m0h'])

        self.assertEqual(expected_result, real_result)


if __name__ == '__main__':
    unittest.main()

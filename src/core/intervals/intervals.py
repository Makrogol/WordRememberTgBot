from datetime import timedelta
from .config import INTERVALS_AS_TIMEDELTA, INTERVALS_AS_LETTERS, INTERVALS_AS_LETTERS_TEST, INTERVALS_AS_TIMEDELTA_TEST


class Intervals:
    def __init__(self, intervals_as_letters: list[str] = None, intervals_as_timedelta: list[timedelta] = None):
        if intervals_as_letters is None:
            intervals_as_letters = INTERVALS_AS_LETTERS_TEST
        if intervals_as_timedelta is None:
            intervals_as_timedelta = INTERVALS_AS_TIMEDELTA_TEST

        self.intervals_as_letters: list[str] = intervals_as_letters
        self.intervals_as_timedelta: list[timedelta] = intervals_as_timedelta
        self.intervals_as_string = ' '.join(self.intervals_as_letters)
        self.intervals_as_accumulate_sum = []

        accumulate_sum = timedelta(0)
        for interval in self.intervals_as_timedelta:
            accumulate_sum += interval
            self.intervals_as_accumulate_sum.append(accumulate_sum)

    def to_json(self) -> dict:
        return {
            'intervals_as_letters': self.intervals_as_letters,
            'intervals_as_timedelta': [interval_timedelta.total_seconds() for interval_timedelta in
                                       self.intervals_as_timedelta],
        }

    def get_as_string(self):
        return self.intervals_as_string

    def get_as_timedelta_accumulate_sum(self):
        return self.intervals_as_accumulate_sum

    def __eq__(self, other: 'Intervals'):
        return \
                self.intervals_as_letters == other.intervals_as_letters and \
                self.intervals_as_timedelta == other.intervals_as_timedelta and \
                self.intervals_as_string == other.intervals_as_string and \
                self.intervals_as_accumulate_sum == other.intervals_as_accumulate_sum

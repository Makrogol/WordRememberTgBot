from datetime import timedelta
from .config import INTERVALS_AS_TIMEDELTA, INTERVALS_AS_LETTERS, INTERVALS_AS_LETTERS_TEST, INTERVALS_AS_TIMEDELTA_TEST


class Intervals:
    def __init__(self, intervals_as_letters: list[str] = INTERVALS_AS_LETTERS_TEST,
                 intervals_as_timedelta: list[timedelta] = INTERVALS_AS_TIMEDELTA_TEST):
        self.__intervals_as_letters: list[str] = intervals_as_letters
        self.__intervals_as_timedelta: list[timedelta] = intervals_as_timedelta
        self.__intervals_as_string = ' '.join(self.__intervals_as_letters)
        self.__intervals_as_accumulate_sum = []

        accumulate_sum = timedelta(0)
        for interval in self.__intervals_as_timedelta:
            accumulate_sum += interval
            self.__intervals_as_accumulate_sum.append(accumulate_sum)

    def to_json(self) -> dict:
        return {
            "intervals_as_letters": self.__intervals_as_letters,
            "intervals_as_timedelta": [interval_timedelta.total_seconds() for interval_timedelta in
                                       self.__intervals_as_timedelta],
        }

    def from_json(self, data: dict) -> None:
        self.__intervals_as_letters = data['intervals_as_letters']
        self.__intervals_as_timedelta = [timedelta(seconds=interval_timedelta) for interval_timedelta in
                                         data['intervals_as_timedelta']]

        self.__intervals_as_string = ' '.join(self.__intervals_as_letters)
        self.__intervals_as_accumulate_sum = []

        accumulate_sum = timedelta(0)
        for interval in self.__intervals_as_timedelta:
            accumulate_sum += interval
            self.__intervals_as_accumulate_sum.append(accumulate_sum)

    def get_as_string(self):
        return self.__intervals_as_string

    def get_as_timedelta_accumulate_sum(self):
        return self.__intervals_as_accumulate_sum

    def __eq__(self, other):
        return \
                self.__intervals_as_letters == other.__intervals_as_letters and \
                self.__intervals_as_timedelta == other.__intervals_as_timedelta and \
                self.__intervals_as_string == other.__intervals_as_string and \
                self.__intervals_as_accumulate_sum == other.__intervals_as_accumulate_sum

from datetime import timedelta

from src.core.intervals.intervals import Intervals


class IntervalsJsonFactory:
    @staticmethod
    def create(data: dict) -> Intervals:
        intervals = Intervals()
        intervals.intervals_as_letters = data['intervals_as_letters']
        intervals.intervals_as_timedelta = [timedelta(seconds=interval_timedelta) for interval_timedelta in
                                       data['intervals_as_timedelta']]

        intervals.intervals_as_string = ' '.join(intervals.intervals_as_letters)
        intervals.intervals_as_accumulate_sum = []

        accumulate_sum = timedelta(0)
        for interval in intervals.intervals_as_timedelta:
            accumulate_sum += interval
            intervals.intervals_as_accumulate_sum.append(accumulate_sum)
        return intervals
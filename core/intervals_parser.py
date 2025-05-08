from datetime import timedelta

type Intervals = list[timedelta]

TIME_LETTERS = ['s', 'm', 'h', 'd']

class IntervalsParser:

    @staticmethod
    def try_parse_intervals(intervals: list[str]) -> Intervals | None:
        if len(intervals) == 0:
            return None
        try:
            timedelta_intervals = []
            for interval in intervals:

                interval_seconds = 0
                prev_alpha_index = 0
                for i in range(len(interval)):
                    if not interval[i].isdigit() and not interval[i].isalpha():
                        return None
                    if interval[i].isalpha():
                        num = int(interval[prev_alpha_index:i])
                        if num < 0:
                            return None
                        prev_alpha_index = i + 1
                        if interval[i] not in TIME_LETTERS:
                            return None
                        match interval[i]:
                            case 's':
                                interval_seconds += num
                            case 'm':
                                interval_seconds += num * 60
                            case 'h':
                                interval_seconds += num * 60 * 60
                            case 'd':
                                interval_seconds += num * 60 * 60 * 24

                timedelta_intervals.append(timedelta(seconds=interval_seconds))
            return timedelta_intervals
        except:
            return None

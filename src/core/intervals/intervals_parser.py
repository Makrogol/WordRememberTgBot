from datetime import timedelta

from .config import TIME_LETTERS
from .intervals import Intervals


def try_parse_intervals(intervals_as_letters: list[str]) -> Intervals | None:
    intervals_as_timedelta: list[timedelta] = []
    if len(intervals_as_letters) == 0:
        # TODO нужно какое-то сообщение об ошибке лучше, чем None
        return None
    try:
        for interval in intervals_as_letters:
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

            intervals_as_timedelta.append(timedelta(seconds=interval_seconds))
        return Intervals(intervals_as_letters=intervals_as_letters, intervals_as_timedelta=intervals_as_timedelta)
    except:
        return None

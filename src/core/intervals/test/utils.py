from datetime import timedelta

# TODO может быть когда-нибудь понадобится
def get_intervals_as_timedelta(intervals_as_accumulate_sum: list[timedelta]):
    intervals_as_timedelta: list[timedelta] = []

    if len(intervals_as_accumulate_sum) > 0:
        intervals_as_timedelta.append(intervals_as_accumulate_sum[0])
    for i in range(1, len(intervals_as_accumulate_sum)):
        intervals_as_timedelta.append(intervals_as_accumulate_sum[i] - intervals_as_accumulate_sum[i - 1])
    return intervals_as_timedelta

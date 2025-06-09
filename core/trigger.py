from apscheduler.triggers.base import BaseTrigger

from .intervals_parser import *


class Trigger(BaseTrigger):
    def __init__(self, intervals: Intervals):
        super().__init__()
        self.__count_fires = 0
        self.__start_time = None
        print(intervals)
        self.__intervals = intervals

    def get_next_fire_time(self, previous_fire_time, now):
        if self.__count_fires >= len(self.__intervals):
            return None
        print(self.__intervals, self.__count_fires, previous_fire_time, now)
        if previous_fire_time is None:
            self.__start_time = now
        next_time = self.__start_time + self.__intervals[self.__count_fires]
        if now.second < next_time.second:
            print(self.__intervals, self.__count_fires, "in if ", next_time)
            return next_time
        self.__count_fires += 1
        print(self.__intervals, self.__count_fires, "out if ", next_time)
        return next_time

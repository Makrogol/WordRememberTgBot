from src.core.intervals.intervals import Intervals
from src.core.statistics.statistics import Statistics
from src.core.user.user_identifier_data import UserIdentifierData


class UserData:
    def __init__(self, user_identifier_data: UserIdentifierData = None, intervals: Intervals = None,
                 statistics: Statistics = None):
        if user_identifier_data is None:
            user_identifier_data = UserIdentifierData()
        if intervals is None:
            intervals = Intervals()
        if statistics is None:
            statistics = Statistics()

        self.user_identifier_data = user_identifier_data
        self.intervals = intervals
        self.statistics = statistics

    def to_json(self) -> dict:
        return {
            'user_identifier_data': self.user_identifier_data.to_json(),
            'intervals': self.intervals.to_json(),
            'statistics': self.statistics.to_json()
        }

    def __eq__(self, other: 'UserData') -> bool:
        return \
                self.user_identifier_data == other.user_identifier_data and \
                self.intervals == other.intervals and \
                self.statistics == other.statistics

from src.core.intervals.intervals import Intervals
from src.core.intervals.intervals_json_factory import IntervalsJsonFactory
from src.core.user_data.user_data import UserData
from src.core.user.user_identifier_data_json_factory import UserIdentifierDataJsonFactory
from src.core.statistics.statistics_json_factory import StatisticsJsonFactory


class UserDataJsonFactory:
    @staticmethod
    def create(data: dict) -> UserData:
        user_data = UserData()
        user_data.user_identifier_data = UserIdentifierDataJsonFactory.create(data['user_identifier_data'])
        user_data.intervals = IntervalsJsonFactory.create(data['intervals'])
        user_data.statistics = StatisticsJsonFactory.create(data['statistics'])
        return user_data

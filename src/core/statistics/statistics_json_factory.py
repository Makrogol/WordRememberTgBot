from src.core.statistics.statistics import Statistics


class StatisticsJsonFactory:
    @staticmethod
    def create(data: dict) -> Statistics:
        statistics = Statistics()
        statistics.command_statistics = data['command_statistics']
        return statistics

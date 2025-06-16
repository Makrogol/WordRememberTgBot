from src.core.intervals.intervals import Intervals
from src.core.intervals.intervals_parser import try_parse_intervals


class UserData:
    def __init__(self, user_id: int = 0, user_login: str = "", intervals: Intervals = Intervals()):
        self.user_id = user_id
        self.user_login = user_login
        self.intervals = intervals

    def to_json(self) -> dict:
        return {
            "user_id": self.user_id,
            "user_login": self.user_login,
            "intervals": self.intervals.to_json(),
        }

    def from_json(self, data: dict) -> None:
        self.user_id = data["user_id"]
        self.user_login = data["user_login"]
        self.intervals = Intervals()
        self.intervals.from_json(data["intervals"])

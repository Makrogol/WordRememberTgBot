from src.core.user_data.user_data import UserData
from test.core.mock_bot import MockBot
from test.core.mock_job_queue import MockJobQueue


class MockContext:
    def __init__(self, args: list[str] | None = None):
        if args is None:
            args = []
        self.bot = MockBot()
        self.job_queue = MockJobQueue()
        self.user_data = UserData()
        self.args = args

    def clear(self):
        self.bot = MockBot()
        self.job_queue = MockJobQueue()
        self.user_data = UserData()
        self.args = None

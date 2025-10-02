import asyncio
import unittest

from src.bot.bot_main import Bot
from src.output.command_messages.set_intervals_messages import SetIntervalsMessages
from src.core.file_manager.user_data_manager import UserDataManager
from src.core.intervals.intervals_parser import try_parse_intervals
from src.core.user.user_identifier_data import UserIdentifierData
from test.config import TEST_CHAT_ID, TEST_USER_ID, TEST_USER_NAME
from test.core.mock_context import MockContext
from test.core.mock_update import MockUpdate


class TestBotSetIntervals(unittest.TestCase):
    def test_set_intervals_cannot_parse_intervals_text(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        update = MockUpdate()
        context = MockContext(args=["-1s"])
        asyncio.run(Bot.set_intervals(update, context))

        self.assertEqual(context.bot.get_messages(), [SetIntervalsMessages.CANNOT_PARSE_INTERVALS_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])

        user_data_manager.delete_user_data_files()

    def test_set_intervals_success(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        intervals_as_letters = ["1s", "2m", "3h"]
        intervals = try_parse_intervals(intervals_as_letters)

        update = MockUpdate()
        context = MockContext(args=intervals_as_letters)
        asyncio.run(Bot.set_intervals(update, context))

        self.assertEqual(context.bot.get_messages(), [SetIntervalsMessages.SUCCESS_SET_INTERVALS_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        user_data = user_data_manager.get_or_create_user_data()
        self.assertTrue(user_data.intervals == intervals)

        user_data_manager.delete_user_data_files()


if __name__ == '__main__':
    unittest.main()

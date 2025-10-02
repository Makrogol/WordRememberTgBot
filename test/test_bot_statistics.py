import asyncio
import unittest

from src.bot.bot_main import Bot
from src.output.command_messages.statistics_messages import StatisticsMessages
from src.core.command.commands import ALL_COMMANDS_FULL_NAME, Commands
from src.core.file_manager.user_data_manager import UserDataManager
from src.core.statistics.statistics import Statistics
from src.core.user.user_identifier_data import UserIdentifierData
from test.config import TEST_CHAT_ID, TEST_USER_ID, TEST_USER_NAME
from test.core.mock_context import MockContext
from test.core.mock_update import MockUpdate


class TestBotStatistics(unittest.TestCase):
    def test_statistics_success(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        statistics = Statistics()
        update = MockUpdate()
        context = MockContext()

        for command in ALL_COMMANDS_FULL_NAME:
            statistics.command_statistics[command] += 1
            asyncio.run(Bot.__dict__[command](update, context))
        context.clear()

        asyncio.run(Bot.statistics(update, context))
        statistics.command_statistics[Commands.STATISTICS_COMMAND] += 1
        self.assertEqual(context.bot.get_messages(), [StatisticsMessages.SUCCESS_STATISTICS_TEXT + str(statistics)])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])

        user_data = user_data_manager.get_or_create_user_data()
        self.assertEqual(user_data.statistics, statistics)

        user_data_manager.delete_user_data_files()


if __name__ == '__main__':
    unittest.main()

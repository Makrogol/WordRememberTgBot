import asyncio
import unittest

from src.bot.bot_main import Bot
from src.output.command_messages.start_messages import StartMessages
from src.core.file_manager.user_data_manager import UserDataManager
from src.core.user.user_identifier_data import UserIdentifierData
from test.config import TEST_CHAT_ID, TEST_USER_ID, TEST_USER_NAME
from test.core.mock_context import MockContext
from test.core.mock_update import MockUpdate


class TestBotStart(unittest.TestCase):
    def test_start(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        update = MockUpdate()
        context = MockContext()
        asyncio.run(Bot.start(update, context))

        self.assertEqual(context.bot.get_messages(), [StartMessages.START_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])

        user_data_manager.delete_user_data_files()

if __name__ == '__main__':
    unittest.main()

import asyncio
import unittest

from src.bot.bot_main import Bot
from src.output import HELP_MESSAGES_BY_COMMANDS
from src.output.command_messages.help_messages import HelpMessages
from src.core.command.commands import ALL_COMMANDS
from src.core.file_manager.user_data_manager import UserDataManager
from src.core.user.user_identifier_data import UserIdentifierData
from test.config import TEST_CHAT_ID, TEST_USER_NAME, TEST_USER_ID
from test.core.mock_context import MockContext
from test.core.mock_update import MockUpdate


class TestBotHelp(unittest.TestCase):
    def test_help_message(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        update = MockUpdate()
        context = MockContext()
        asyncio.run(Bot.help(update, context))

        self.assertEqual(context.bot.get_messages(), [HelpMessages.HELP_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])

        user_data_manager.delete_user_data_files()

    def test_help_message_for_commands(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        for command in ALL_COMMANDS:
            update = MockUpdate()
            context = MockContext(args=[command])
            asyncio.run(Bot.help(update, context))

            self.assertEqual(context.bot.get_messages(), [HELP_MESSAGES_BY_COMMANDS[command]])
            self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])

        user_data_manager.delete_user_data_files()

    def test_help_message_bad_command(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        update = MockUpdate()
        context = MockContext(args=['gsahfjkas'])
        asyncio.run(Bot.help(update, context))

        self.assertEqual(context.bot.get_messages(), [HelpMessages.HELP_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])

        user_data_manager.delete_user_data_files()


if __name__ == '__main__':
    unittest.main()

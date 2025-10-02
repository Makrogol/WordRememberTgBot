import asyncio
import os
import unittest

from src.bot.bot_main import Bot
from src.output.command_messages.add_new_word_messages import AddNewWordMessages
from src.output import GetAllWordsAsFileMessages
from src.core.file_manager.user_data_manager import UserDataManager
from src.core.file_manager.words_manager import WordsManager
from src.core.user.user_identifier_data import UserIdentifierData
from test.config import TEST_USER_ID, TEST_CHAT_ID, TEST_USER_NAME
from test.core.mock_context import MockContext
from test.core.mock_update import MockUpdate


class TestBotGetAllWordsAsFile(unittest.TestCase):
    def test_get_all_words_as_file_success(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        words_manager = WordsManager(user_id=TEST_USER_ID)
        file_path = words_manager.get_words_output_file_path()
        words_manager.delete_user_files()
        update = MockUpdate()
        context = MockContext(args=["123", "-", "456"])

        asyncio.run(Bot.add_new_word(update, context))
        self.assertEqual(context.bot.get_messages(), [AddNewWordMessages.SUCCESS_ADDING_NEW_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        context.clear()

        context = MockContext()
        asyncio.run(Bot.get_all_words_as_file(update, context))

        self.assertTrue(os.path.exists(str(file_path)))
        self.assertEqual(context.bot.get_messages(), [GetAllWordsAsFileMessages.SUCCESS_GET_ALL_WORDS_AS_FILE_TEXT])
        self.assertEqual(context.bot.get_documents(), [file_path])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])

        user_data_manager.delete_user_data_files()

    def test_get_all_words_as_file_success_empty_words(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        words_manager = WordsManager(user_id=TEST_USER_ID)
        file_path = words_manager.get_words_output_file_path()
        words_manager.delete_user_files()
        update = MockUpdate()
        context = MockContext(args=["123", "-", "456"])

        asyncio.run(Bot.add_new_word(update, context))
        self.assertEqual(context.bot.get_messages(), [AddNewWordMessages.SUCCESS_ADDING_NEW_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        context.clear()

        context = MockContext()
        asyncio.run(Bot.get_all_words_as_file(update, context))

        self.assertTrue(os.path.exists(str(file_path)))
        self.assertEqual(context.bot.get_messages(), [GetAllWordsAsFileMessages.SUCCESS_GET_ALL_WORDS_AS_FILE_TEXT])
        self.assertEqual(context.bot.get_documents(), [file_path])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])

        user_data_manager.delete_user_data_files()


if __name__ == '__main__':
    unittest.main()

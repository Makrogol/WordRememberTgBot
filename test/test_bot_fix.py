import asyncio
import unittest

from src.bot.bot_main import Bot
from src.output.command_messages.add_new_word_messages import AddNewWordMessages
from src.output import FixWordByNumberMessages
from src.output.command_messages.get_all_words_messages import GetAllWordsMessages
from src.core.file_manager.user_data_manager import UserDataManager
from src.core.file_manager.words_manager import WordsManager
from src.core.user.user_identifier_data import UserIdentifierData
from src.core.word.word_parser import try_parse_word
from test.config import TEST_USER_ID, TEST_CHAT_ID, TEST_USER_NAME
from test.core.mock_context import MockContext
from test.core.mock_update import MockUpdate


class TestBotFix(unittest.TestCase):
    def test_fix_cannot_parse_number(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        words_manager = WordsManager(user_id=TEST_USER_ID)
        words_manager.delete_user_files()
        args = ["ab", "123", "-", "45"]
        update = MockUpdate()
        context = MockContext(args=args)

        asyncio.run(Bot.fix_word(update, context))
        self.assertEqual(context.bot.get_messages(), [FixWordByNumberMessages.CANNOT_PARSE_NUMBER_OR_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        context.clear()

        user_data_manager.delete_user_data_files()

    def test_fix_cannot_parse_word(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        words_manager = WordsManager(user_id=TEST_USER_ID)
        words_manager.delete_user_files()
        args = ["1", "123"]
        update = MockUpdate()
        context = MockContext(args=args)

        asyncio.run(Bot.fix_word(update, context))
        self.assertEqual(context.bot.get_messages(), [FixWordByNumberMessages.CANNOT_PARSE_NUMBER_OR_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        context.clear()

        user_data_manager.delete_user_data_files()

    def test_fix_no_words(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        words_manager = WordsManager(user_id=TEST_USER_ID)
        words_manager.delete_user_files()
        args = ["1", "123", "-", "456"]
        update = MockUpdate()
        context = MockContext(args=args)

        asyncio.run(Bot.fix_word(update, context))
        self.assertEqual(context.bot.get_messages(), [FixWordByNumberMessages.NO_WORDS_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        context.clear()

        user_data_manager.delete_user_data_files()

    def test_fix_incorrect_index_negative_index(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        words_manager = WordsManager(user_id=TEST_USER_ID)
        words_manager.delete_user_files()
        args = ["123", "-", "456"]
        update = MockUpdate()
        context = MockContext(args=args)

        asyncio.run(Bot.add_new_word(update, context))
        self.assertEqual(context.bot.get_messages(), [AddNewWordMessages.SUCCESS_ADDING_NEW_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        context.clear()

        args = ["-1", "123", "-", "456"]
        context = MockContext(args=args)

        asyncio.run(Bot.fix_word(update, context))
        self.assertEqual(context.bot.get_messages(), [FixWordByNumberMessages.INCORRECT_INDEX_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        context.clear()

        user_data_manager.delete_user_data_files()

    def test_fix_incorrect_index_zero_index(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        words_manager = WordsManager(user_id=TEST_USER_ID)
        words_manager.delete_user_files()
        args = ["123", "-", "456"]
        update = MockUpdate()
        context = MockContext(args=args)

        asyncio.run(Bot.add_new_word(update, context))
        self.assertEqual(context.bot.get_messages(), [AddNewWordMessages.SUCCESS_ADDING_NEW_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        context.clear()

        args = ["0", "123", "-", "456"]
        context = MockContext(args=args)

        asyncio.run(Bot.fix_word(update, context))
        self.assertEqual(context.bot.get_messages(), [FixWordByNumberMessages.INCORRECT_INDEX_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        context.clear()

        user_data_manager.delete_user_data_files()

    def test_fix_success(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        words_manager = WordsManager(user_id=TEST_USER_ID)
        words_manager.delete_user_files()
        args = ["123", "-", "456"]
        word = try_parse_word(args)
        update = MockUpdate()
        context = MockContext(args=args)

        asyncio.run(Bot.add_new_word(update, context))
        self.assertEqual(context.bot.get_messages(), [AddNewWordMessages.SUCCESS_ADDING_NEW_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        context.clear()

        asyncio.run(Bot.get_all_words(update, context))
        self.assertEqual(context.bot.get_messages(),
                         [GetAllWordsMessages.SUCCESS_GET_ALL_WORDS_TEXT, word.get_full_numerated_word(1)])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID, TEST_CHAT_ID])
        context.clear()

        args = ["1", "789", "-", "101112"]
        word = try_parse_word(args[1:])
        context = MockContext(args=args)

        asyncio.run(Bot.fix_word(update, context))
        self.assertEqual(context.bot.get_messages(), [FixWordByNumberMessages.SUCCESS_FIX_WORD_BY_NUMBER_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        context.clear()

        asyncio.run(Bot.get_all_words(update, context))
        self.assertEqual(context.bot.get_messages(),
                         [GetAllWordsMessages.SUCCESS_GET_ALL_WORDS_TEXT, word.get_full_numerated_word(1)])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID, TEST_CHAT_ID])
        context.clear()

        user_data_manager.delete_user_data_files()


if __name__ == '__main__':
    unittest.main()

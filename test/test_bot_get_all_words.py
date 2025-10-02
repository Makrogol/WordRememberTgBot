import unittest
import asyncio

from src.bot.bot_main import Bot
from src.core.file_manager.user_data_manager import UserDataManager
from src.core.paginated_message.paginated_message import PaginatedMessages
from src.core.user.user_identifier_data import UserIdentifierData
from src.core.word.word_parser import try_parse_word
from test.config import TEST_USER_ID, TEST_USER_NAME
from test.core.mock_context import MockContext
from test.core.mock_update import MockUpdate
from src.core.file_manager.words_manager import WordsManager
from config import TEST_CHAT_ID
from src.output.command_messages.add_new_word_messages import AddNewWordMessages
from src.output.command_messages.get_all_words_messages import GetAllWordsMessages


class TestBotGetAllWords(unittest.TestCase):
    def test_get_all_words_success(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        words_manager = WordsManager(user_id=TEST_USER_ID)
        words_manager.delete_user_files()
        args = ["123", "-", "45"]
        word = try_parse_word(args)
        update = MockUpdate()
        context = MockContext(args=args)

        asyncio.run(Bot.add_new_word(update, context))
        self.assertEqual(context.bot.get_messages(), [AddNewWordMessages.SUCCESS_ADDING_NEW_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        context.clear()

        context.args = args
        asyncio.run(Bot.add_new_word(update, context))
        self.assertEqual(context.bot.get_messages(), [AddNewWordMessages.SUCCESS_ADDING_NEW_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        context.clear()

        asyncio.run(Bot.get_all_words(update, context))

        paginated_messages = PaginatedMessages()
        paginated_messages.append(word.get_full_numerated_word(1))
        paginated_messages.append(word.get_full_numerated_word(2))
        expected_messages = [GetAllWordsMessages.SUCCESS_GET_ALL_WORDS_TEXT] + paginated_messages.get()
        self.assertEqual(len(context.bot.get_messages()), len(expected_messages))
        for i in range(len(expected_messages)):
            self.assertEqual(context.bot.get_messages()[i], expected_messages[i])
            self.assertEqual(context.bot.get_chat_ids()[i], TEST_CHAT_ID)

        user_data_manager.delete_user_data_files()

    def test_get_all_words_no_words(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        words_manager = WordsManager(user_id=TEST_USER_ID)
        words_manager.delete_user_files()
        update = MockUpdate()
        context = MockContext()

        asyncio.run(Bot.get_all_words(update, context))

        self.assertEqual(context.bot.get_messages(), [GetAllWordsMessages.NO_WORDS_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])

        user_data_manager.delete_user_data_files()


if __name__ == '__main__':
    unittest.main()

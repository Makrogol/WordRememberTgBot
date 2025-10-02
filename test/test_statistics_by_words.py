import asyncio
import unittest

from src.bot.bot_main import Bot
from src.output.command_messages.add_new_word_messages import AddNewWordMessages
from src.output.command_messages.repeat_messages import RepeatMessages
from src.output.command_messages.statistics_by_words_messages import StatisticsByWordsMessages
from src.core.file_manager.user_data_manager import UserDataManager
from src.core.file_manager.words_manager import WordsManager
from src.core.user.user_identifier_data import UserIdentifierData
from src.core.word.word_parser import try_parse_word
from test.config import TEST_CHAT_ID, TEST_USER_ID, TEST_USER_NAME
from test.core.mock_context import MockContext
from test.core.mock_update import MockUpdate


class TestBotStatisticsByWords(unittest.TestCase):
    def test_statistics_by_words_success(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        words_manager = WordsManager(user_id=TEST_USER_ID)
        words_manager.delete_user_files()
        args = ["123", "-", "45"]
        word1 = try_parse_word(args)
        update = MockUpdate()
        context = MockContext(args=args)

        asyncio.run(Bot.add_new_word(update, context))
        self.assertEqual(context.bot.get_messages(), [AddNewWordMessages.SUCCESS_ADDING_NEW_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])

        args = ["123", "-", "456"]
        word2 = try_parse_word(args)
        context = MockContext(args=args)

        asyncio.run(Bot.add_new_word(update, context))
        self.assertEqual(context.bot.get_messages(), [AddNewWordMessages.SUCCESS_ADDING_NEW_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        context.clear()

        context = MockContext(args=['1'])
        asyncio.run(Bot.repeat(update, context))
        self.assertEqual(context.bot.get_messages(), [RepeatMessages.SUCCESS_REPEAT_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])
        context.clear()

        context = MockContext()
        asyncio.run(Bot.statistics_by_words(update, context))
        self.assertEqual(context.bot.get_messages(), [StatisticsByWordsMessages.SUCCESS_STATISTICS_BY_WORDS_TEXT,
                                                      f' - {word1.get_full_word()[:-1]} - 2\n',
                                                      f' - {word2.get_full_word()[:-1]} - 1\n'])

        user_data_manager.delete_user_data_files()


if __name__ == '__main__':
    unittest.main()

import asyncio
import os
import unittest

from telegram.constants import ParseMode

from src.bot.bot_main import Bot
from src.output.command_messages.add_new_word_messages import AddNewWordMessages
from src.core.file_manager.user_data_manager import UserDataManager
from src.core.file_manager.words_manager import WordsManager
from src.core.intervals.intervals import Intervals
from src.core.user.user_identifier_data import UserIdentifierData
from src.core.word.word_parser import try_parse_word
from test.config import TEST_CHAT_ID, TEST_USER_ID, TEST_USER_NAME
from test.core.mock_context import MockContext
from test.core.mock_update import MockUpdate


class TestBotAddNewWord(unittest.TestCase):
    def test_add_new_word_cannot_parse_word_test(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        update = MockUpdate()
        context = MockContext(args=["123"])
        asyncio.run(Bot.add_new_word(update, context))

        self.assertEqual(context.bot.get_messages(), [AddNewWordMessages.CANNOT_PARSE_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [TEST_CHAT_ID])

        user_data_manager.delete_user_data_files()

    def test_add_new_word_success(self):
        user_identifier_data = UserIdentifierData(TEST_USER_ID, TEST_USER_NAME)
        user_data_manager = UserDataManager(user_identifier_data)
        user_data_manager.delete_user_data_files()
        args = ["123", "-", "456"]
        words_manager = WordsManager(user_id=TEST_USER_ID)
        words_manager.delete_user_files()
        file_path = words_manager.get_words_output_file_path()
        update = MockUpdate()
        context = MockContext(args=args)
        asyncio.run(Bot.add_new_word(update, context))

        self.assertIsNotNone(words_manager.try_update_words_output_file())

        word = try_parse_word(args)
        self.assertTrue(os.path.exists(str(file_path)))
        file = open(str(file_path), 'r')
        # TODO мб можно вынести в отдельную функцию ''.join(file.readlines())
        self.assertEqual(''.join(file.readlines()), word.get_full_numerated_word(1))
        file.close()

        intervals = Intervals()
        self.assertEqual(context.job_queue.get_when(), intervals.get_as_timedelta_accumulate_sum())
        for callback in context.job_queue.get_callbacks():
            asyncio.run(callback(context))

        messages = context.bot.get_messages()
        self.assertEqual(len(messages), len(intervals.get_as_timedelta_accumulate_sum()) + 1)
        self.assertEqual(messages[0], AddNewWordMessages.SUCCESS_ADDING_NEW_WORD_TEXT)
        for i in range(1, len(messages)):
            self.assertIn(messages[i], [word.get_left_spoiler_part_word(), word.get_right_spoiler_part_word()])

        for chat_id in context.bot.get_chat_ids():
            self.assertEqual(chat_id, TEST_CHAT_ID)
        for parse_mode in context.bot.get_parse_modes():
            self.assertEqual(parse_mode, ParseMode.MARKDOWN_V2)

        user_data_manager.delete_user_data_files()


if __name__ == '__main__':
    unittest.main()

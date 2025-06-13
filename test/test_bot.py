import os
import unittest
import asyncio

from telegram.constants import ParseMode

from src.bot.bot_main import Bot
from src.bot.message.paginated_message import PaginatedMessages
from src.core.intervals.intervals_parser import try_parse_intervals
from src.core.word.config import USER_WORD_DATA_PATH
from src.core.word.word_parser import try_parse_word
from src.core.word.words_file_management import create_path_to_user_word_data
from test.config import DEFAULT_USER_ID
from test.core.mock_context import MockContext
from test.core.mock_update import MockUpdate
from config import DEFAULT_CHAT_ID
from src.bot.message.config import START_TEXT, HELP_TEXT, SHOW_CURRENT_INTERVALS_TEXT, BAD_SETTING_INTERVALS_TEXT, \
    SET_INTERVALS_TEXT, BAD_ADDING_NEW_WORD_TEXT, ADDING_NEW_WORD_TEXT, FILE_DOES_NOT_EXIST_TEXT, WORDS_ARE_EMPTY_TEXT
from src.core.intervals.intervals import Intervals


class BotTestCase(unittest.TestCase):
    def test_start_message(self):
        update = MockUpdate()
        context = MockContext()
        asyncio.run(Bot.start(update, context))

        self.assertEqual(context.bot.get_messages(), [START_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [DEFAULT_CHAT_ID])

    def test_help_message(self):
        update = MockUpdate()
        context = MockContext()
        asyncio.run(Bot.help(update, context))

        self.assertEqual(context.bot.get_messages(), [HELP_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [DEFAULT_CHAT_ID])

    def test_show_current_intervals_not_set_intervals(self):
        update = MockUpdate()
        context = MockContext()
        asyncio.run(Bot.show_current_intervals(update, context))

        self.assertEqual(context.bot.get_messages(), [SHOW_CURRENT_INTERVALS_TEXT + Intervals().get_as_string()])
        self.assertEqual(context.bot.get_chat_ids(), [DEFAULT_CHAT_ID])

    def test_set_incorrect_intervals(self):
        update = MockUpdate()
        context = MockContext(args=["-1s"])
        asyncio.run(Bot.set_intervals(update, context))

        self.assertEqual(context.bot.get_messages(), [BAD_SETTING_INTERVALS_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [DEFAULT_CHAT_ID])

    def test_set_correct_intervals(self):
        intervals_as_letters = ["1s", "2m", "3h"]
        intervals = try_parse_intervals(intervals_as_letters)

        update = MockUpdate()
        context = MockContext(args=intervals_as_letters)
        asyncio.run(Bot.set_intervals(update, context))

        self.assertEqual(context.bot.get_messages(), [SET_INTERVALS_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [DEFAULT_CHAT_ID])
        self.assertIn("intervals", context.user_data.keys())
        self.assertEqual(context.user_data["intervals"], intervals)

    def test_show_current_intervals_set_intervals(self):
        intervals_as_letters = ["1s", "2m", "3h"]
        intervals = try_parse_intervals(intervals_as_letters)

        update = MockUpdate()
        context = MockContext(args=intervals_as_letters)
        asyncio.run(Bot.set_intervals(update, context))

        self.assertEqual(context.bot.get_messages(), [SET_INTERVALS_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [DEFAULT_CHAT_ID])
        self.assertIn("intervals", context.user_data.keys())
        self.assertEqual(context.user_data["intervals"], intervals)

        asyncio.run(Bot.show_current_intervals(update, context))

        self.assertIn(SHOW_CURRENT_INTERVALS_TEXT + intervals.get_as_string(), context.bot.get_messages())
        self.assertEqual(context.bot.get_chat_ids(), [DEFAULT_CHAT_ID, DEFAULT_CHAT_ID])

    def test_bad_add_new_word(self):
        update = MockUpdate()
        context = MockContext(args=["123"])
        asyncio.run(Bot.add_new_word(update, context))

        self.assertEqual(context.bot.get_messages(), [BAD_ADDING_NEW_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [DEFAULT_CHAT_ID])

    def test_add_new_word(self):
        args = ["123", "-", "456"]
        file_path = create_path_to_user_word_data(DEFAULT_USER_ID, USER_WORD_DATA_PATH)
        if os.path.exists(str(file_path)):
            os.remove(str(file_path))
        update = MockUpdate()
        context = MockContext(args=args)
        asyncio.run(Bot.add_new_word(update, context))

        word = try_parse_word(args)
        self.assertTrue(os.path.exists(str(file_path)))
        file = open(str(file_path), 'r')
        self.assertEqual(file.readlines(), [word.get_full_word() + '\n'])
        file.close()

        intervals = Intervals()
        self.assertEqual(context.job_queue.get_when(), intervals.get_as_timedelta_accumulate_sum())
        for callback in context.job_queue.get_callbacks():
            asyncio.run(callback(context))

        messages = context.bot.get_messages()
        self.assertEqual(len(messages), len(intervals.get_as_timedelta_accumulate_sum()) + 1)
        self.assertEqual(messages[0], ADDING_NEW_WORD_TEXT)
        for i in range(1, len(messages)):
            self.assertIn(messages[i], [word.get_left_spoiler_part_word(), word.get_right_spoiler_part_word()])

        for chat_id in context.bot.get_chat_ids():
            self.assertEqual(chat_id, DEFAULT_CHAT_ID)
        for parse_mode in context.bot.get_parse_modes():
            self.assertEqual(parse_mode, ParseMode.MARKDOWN_V2)

    def test_get_all_words_as_file(self):
        file_path = create_path_to_user_word_data(DEFAULT_USER_ID, USER_WORD_DATA_PATH)
        if os.path.exists(str(file_path)):
            os.remove(str(file_path))
        update = MockUpdate()
        context = MockContext(args=["123", "-", "456"])

        asyncio.run(Bot.add_new_word(update, context))
        self.assertEqual(context.bot.get_messages(), [ADDING_NEW_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [DEFAULT_CHAT_ID])
        context.clear()

        asyncio.run(Bot.get_all_words_as_file(update, context))

        self.assertTrue(os.path.exists(str(file_path)))
        self.assertEqual(context.bot.get_documents(), [file_path])
        self.assertEqual(context.bot.get_chat_ids(), [DEFAULT_CHAT_ID])

    def test_get_all_words_as_file_file_does_not_exist(self):
        file_path = create_path_to_user_word_data(DEFAULT_USER_ID, USER_WORD_DATA_PATH)
        if os.path.exists(str(file_path)):
            os.remove(str(file_path))
        update = MockUpdate()
        context = MockContext()

        asyncio.run(Bot.get_all_words_as_file(update, context))

        self.assertEqual(context.bot.get_messages(), [FILE_DOES_NOT_EXIST_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [DEFAULT_CHAT_ID])

    def test_get_all_words(self):
        file_path = create_path_to_user_word_data(DEFAULT_USER_ID, USER_WORD_DATA_PATH)
        if os.path.exists(str(file_path)):
            os.remove(str(file_path))
        args = ["123", "-", "45"]
        word = try_parse_word(args)
        update = MockUpdate()
        context = MockContext(args=args)

        asyncio.run(Bot.add_new_word(update, context))
        self.assertEqual(context.bot.get_messages(), [ADDING_NEW_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [DEFAULT_CHAT_ID])
        context.clear()

        context.args = args
        asyncio.run(Bot.add_new_word(update, context))
        self.assertEqual(context.bot.get_messages(), [ADDING_NEW_WORD_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [DEFAULT_CHAT_ID])
        context.clear()

        asyncio.run(Bot.get_all_words(update, context))

        paginated_messages = PaginatedMessages()
        paginated_messages.append(word.get_full_word() + '\n')
        paginated_messages.append(word.get_full_word() + '\n')
        self.assertEqual(len(context.bot.get_messages()), len(paginated_messages.get()))
        for i in range(len(paginated_messages.get())):
            self.assertEqual(context.bot.get_messages()[i], paginated_messages.get()[i])
            self.assertEqual(context.bot.get_chat_ids()[i], DEFAULT_CHAT_ID)

    def test_get_all_words_empty_words(self):
        file_path = create_path_to_user_word_data(DEFAULT_USER_ID, USER_WORD_DATA_PATH)
        if os.path.exists(str(file_path)):
            os.remove(str(file_path))
        update = MockUpdate()
        context = MockContext()

        asyncio.run(Bot.get_all_words(update, context))

        self.assertEqual(context.bot.get_messages(), [WORDS_ARE_EMPTY_TEXT])
        self.assertEqual(context.bot.get_chat_ids(), [DEFAULT_CHAT_ID])


if __name__ == '__main__':
    unittest.main()

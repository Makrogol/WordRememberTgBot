import os

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, ContextTypes, CommandHandler, CallbackContext

from src.bot.messages.help_messages_by_commands import HELP_MESSAGES_BY_COMMANDS
from src.bot.messages.messages.add_new_word_messages import AddNewWordMessages
from src.bot.messages.messages.fix_word_by_number_messages import FixWordByNumberMessages
from src.bot.messages.messages.get_all_words_as_file_messages import GetAllWordsAsFileMessages
from src.bot.messages.messages.get_all_words_messages import GetAllWordsMessages
from src.bot.messages.messages.help_messages import HelpMessages
from src.bot.messages.messages.repeat_messages import RepeatMessages
from src.bot.messages.messages.set_intervals_messages import SetIntervalsMessages
from src.bot.messages.messages.show_current_intervals_messages import ShowCurrentIntervalsMessages
from src.bot.messages.messages.start_messages import StartMessages
from src.core.bot_view.views import add_new_word_view, get_all_words_view, get_all_words_as_file_view, \
    set_intervals_view, repeat_view, fix_word_by_number_view
from src.core.bot_view.view_data import ViewData
from src.core.bot_view.result.add_new_word_result import AddNewWordResultType
from src.core.bot_view.result.fix_word_by_number_result import FixWordByNumberResultType
from src.core.bot_view.result.get_all_words_as_file_result import GetAllWordsAsFileResultType
from src.core.bot_view.result.get_all_words_result import GetAllWordsResultType
from src.core.bot_view.result.repeat_result import RepeatResultType
from src.core.bot_view.result.set_intervals_result import SetIntervalsResultType
from src.core.command.commands import Commands
from src.core.command.commands_parser import try_parse_command
from src.core.intervals.intervals import Intervals
from src.core.file_manager.user_data_manager import UserDataManager
from src.core.word.word import Word


class Bot:
    def __init__(self):
        self.bot = Application.builder() \
            .token(os.getenv("BOT_TOKEN")) \
            .build()
        self.bot.add_handler(CommandHandler(Commands.ADD_NEW_WORD_COMMAND, self.add_new_word))
        self.bot.add_handler(CommandHandler(Commands.ANW_COMMAND, self.add_new_word))
        self.bot.add_handler(CommandHandler(Commands.FIX_WORD_COMMAND, self.fix_word_by_number))
        self.bot.add_handler(CommandHandler(Commands.GET_ALL_WORDS_AS_FILE_COMMAND, self.get_all_words_as_file))
        self.bot.add_handler(CommandHandler(Commands.GET_ALL_WORDS_COMMAND, self.get_all_words))
        self.bot.add_handler(CommandHandler(Commands.HELP_COMMAND, self.help))
        self.bot.add_handler(CommandHandler(Commands.REPEAT_COMMAND, self.repeat))
        self.bot.add_handler(CommandHandler(Commands.SET_INTERVALS_COMMAND, self.set_intervals))
        self.bot.add_handler(CommandHandler(Commands.SHOW_CURRENT_INTERVALS_COMMAND, self.show_current_intervals))
        self.bot.add_handler(CommandHandler(Commands.START_COMMAND, self.start))

    @staticmethod
    def repeat_word(context: ContextTypes.DEFAULT_TYPE, chat_id: int, word: Word, intervals: Intervals):
        async def callback(context: CallbackContext):
            await context.bot.send_message(chat_id=chat_id,
                                           text=word.get_random_spoiler_word(),
                                           parse_mode=ParseMode.MARKDOWN_V2)

        for interval in intervals.get_as_timedelta_accumulate_sum():
            context.job_queue.run_once(callback=callback, when=interval)

    @staticmethod
    async def add_new_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
        view_data = ViewData(update.effective_user.id, update.effective_user.name, context.args)
        add_new_word_result = add_new_word_view(view_data)

        if add_new_word_result.result == AddNewWordResultType.CannotParseWord:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=AddNewWordMessages.CANNOT_PARSE_WORD_TEXT)
        elif add_new_word_result.result == AddNewWordResultType.CannotAddWordToFile:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=AddNewWordMessages.CANNOT_ADD_WORDS_TO_FILE)
        elif add_new_word_result.result == AddNewWordResultType.Success:
            Bot.repeat_word(context, update.effective_chat.id, add_new_word_result.word, add_new_word_result.intervals)
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=AddNewWordMessages.SUCCESS_ADDING_NEW_WORD_TEXT)

    @staticmethod
    async def fix_word_by_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
        view_data = ViewData(update.effective_user.id, update.effective_user.name, context.args)
        fix_word_by_number_result = fix_word_by_number_view(view_data)

        if fix_word_by_number_result == FixWordByNumberResultType.CannotParseNumberOrWord:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=FixWordByNumberMessages.CANNOT_PARSE_NUMBER_OR_WORD)
        elif fix_word_by_number_result == FixWordByNumberResultType.NoWords:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=FixWordByNumberMessages.NO_WORDS_TEXT)
        elif fix_word_by_number_result == FixWordByNumberResultType.CannotLoadWordsFromFile:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=FixWordByNumberMessages.CANNOT_LOAD_WORDS_FROM_FILE_TEXT)
        elif fix_word_by_number_result == FixWordByNumberResultType.IncorrectIndex:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=FixWordByNumberMessages.INCORRECT_INDEX_TEXT)
        elif fix_word_by_number_result == FixWordByNumberResultType.Success:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=FixWordByNumberMessages.SUCCESS_FIX_WORD_BY_NUMBER_TEXT)

    @staticmethod
    async def get_all_words_as_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
        view_data = ViewData(update.effective_user.id, update.effective_user.name, context.args)
        get_all_words_as_file_result = get_all_words_as_file_view(view_data)

        if get_all_words_as_file_result == GetAllWordsAsFileResultType.NoWords:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=GetAllWordsAsFileMessages.NO_WORDS_TEXT)
        elif get_all_words_as_file_result == GetAllWordsAsFileResultType.CannotUpdateOutputFile:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=GetAllWordsAsFileMessages.CANNOT_UPDATE_OUTPUT_FILE_TEXT)
            return
        elif get_all_words_as_file_result == GetAllWordsAsFileResultType.Success:
            await context.bot.send_document(chat_id=update.effective_chat.id,
                                            document=get_all_words_as_file_result.all_words_file_path,
                                            caption=GetAllWordsAsFileMessages.SUCCESS_GET_ALL_WORDS_AS_FILE_TEXT)

    @staticmethod
    async def get_all_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
        view_data = ViewData(update.effective_user.id, update.effective_user.name, context.args)
        get_all_words_result = get_all_words_view(view_data)

        if get_all_words_result.result == GetAllWordsResultType.NoWords:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=GetAllWordsMessages.NO_WORDS_TEXT)
        elif get_all_words_result.result == GetAllWordsResultType.Success:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=GetAllWordsMessages.SUCCESS_GET_ALL_WORDS_TEXT)
            for paginated_message in get_all_words_result.paginated_messages.get():
                await context.bot.send_message(chat_id=update.effective_chat.id, text=paginated_message)

    @staticmethod
    async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
        command = try_parse_command(context.args)
        if command is None:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=HelpMessages.HELP_TEXT)
            return

        await context.bot.send_message(chat_id=update.effective_chat.id, text=HELP_MESSAGES_BY_COMMANDS[command])

    @staticmethod
    async def repeat(update: Update, context: ContextTypes.DEFAULT_TYPE):
        view_data = ViewData(update.effective_user.id, update.effective_user.name, context.args)
        repeat_result = repeat_view(view_data)

        if repeat_result == RepeatResultType.CannotParseNumber:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=RepeatMessages.CANNOT_PARSE_NUMBER_TEXT)
        elif repeat_result == RepeatResultType.CannotLoadWordsFromFile:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=RepeatMessages.CANNOT_LOAD_WORDS_FROM_FILE_TEXT)
        elif repeat_result == RepeatResultType.IncorrectIndex:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=RepeatMessages.INCORRECT_INDEX_TEXT)
        elif repeat_result == RepeatResultType.Success:
            Bot.repeat_word(context, update.effective_chat.id, repeat_result.word, repeat_result.intervals)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=RepeatMessages.SUCCESS_REPEAT_TEXT)

    @staticmethod
    async def set_intervals(update: Update, context: ContextTypes.DEFAULT_TYPE):
        view_data = ViewData(update.effective_user.id, update.effective_user.name, context.args)
        set_intervals_result = set_intervals_view(view_data)

        if set_intervals_result == SetIntervalsResultType.CannotParseIntervals:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=SetIntervalsMessages.CANNOT_PARSE_INTERVALS_TEXT)
        elif set_intervals_result == SetIntervalsResultType.Success:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=SetIntervalsMessages.SUCCESS_SET_INTERVALS_TEXT)

    @staticmethod
    async def show_current_intervals(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_data_manger = UserDataManager(update.effective_user.id)
        user_data = user_data_manger.get_or_create_user_data(update.effective_user.name)
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=ShowCurrentIntervalsMessages.SUCCESS_SHOW_CURRENT_INTERVALS_TEXT
                                            + user_data.intervals.get_as_string())

    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=StartMessages.START_TEXT)

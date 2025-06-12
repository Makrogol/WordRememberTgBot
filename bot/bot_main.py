import os

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, ContextTypes, CommandHandler, CallbackContext

from core.word.word_parser import try_parse_word
from core.word.words_file_management import save_word_to_file, get_words_from_file, create_paginated_words, \
    create_path_to_user_word_data
from core.config import BAD_ADDING_NEW_WORD_TEXT, START_TEXT, HELP_TEXT, BAD_SETTING_INTERVALS_TEXT, \
    SHOW_CURRENT_INTERVALS_TEXT, ADDING_NEW_WORD_TEXT, SET_INTERVALS_TEXT
from core.intervals.intervals_parser import try_parse_intervals
from core.intervals.intervals import Intervals


class Bot:
    def __init__(self):
        self.bot = Application.builder() \
            .token(os.getenv("BOT_TOKEN")) \
            .build()
        self.bot.add_handler(CommandHandler('start', self.start))
        self.bot.add_handler(CommandHandler('add_new_word', self.add_new_word))
        self.bot.add_handler(CommandHandler('anw', self.add_new_word))
        self.bot.add_handler(CommandHandler('get_all_words', self.get_all_words))
        self.bot.add_handler(CommandHandler('get_all_words_as_file', self.get_all_words_as_file))
        self.bot.add_handler(CommandHandler('set_intervals', self.set_intervals))
        self.bot.add_handler(CommandHandler('show_current_intervals', self.show_current_intervals))
        self.bot.add_handler(CommandHandler('help', self.help))

    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=START_TEXT)

    @staticmethod
    async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=HELP_TEXT)

    @staticmethod
    async def add_new_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
        word = try_parse_word(context.args)
        if word is None:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=BAD_ADDING_NEW_WORD_TEXT)
            return
        save_word_to_file(update.effective_user.id, word.get_full_word())

        async def call_back(context: CallbackContext):
            await context.bot.send_message(chat_id=update.effective_chat.id, text=word.get_random_spoiler_word(),
                                           parse_mode=ParseMode.MARKDOWN_V2)

        for interval in context.user_data.get('intervals', Intervals()).get_as_timedelta_accumulate_sum():
            context.job_queue.run_once(callback=call_back, when=interval)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=ADDING_NEW_WORD_TEXT)

    @staticmethod
    async def get_all_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
        all_words = get_words_from_file(update.effective_user.id)
        if all_words is None:
            return
        for paged_words in create_paginated_words(all_words):
            await context.bot.send_message(chat_id=update.effective_chat.id, text=paged_words)

    @staticmethod
    async def get_all_words_as_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
        file_path = create_path_to_user_word_data(update.effective_user.id)
        await context.bot.send_document(chat_id=update.effective_chat.id, document=file_path)

    @staticmethod
    async def set_intervals(update: Update, context: ContextTypes.DEFAULT_TYPE):
        intervals = try_parse_intervals(context.args)
        if intervals is None:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=BAD_SETTING_INTERVALS_TEXT)
            return

        context.user_data['intervals'] = intervals
        await context.bot.send_message(chat_id=update.effective_chat.id, text=SET_INTERVALS_TEXT)

    @staticmethod
    async def show_current_intervals(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=SHOW_CURRENT_INTERVALS_TEXT +
                                            context.user_data.get('intervals', Intervals()).get_as_string())

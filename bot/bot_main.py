import os

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, ContextTypes, CommandHandler, CallbackContext

from core.trigger import Trigger
from core.word import try_create_from_args
from core.words_file_manager import WordsFileManager
from core.config import BAD_ADDING_NEW_WORD_TEXT, START_TEXT, HELP_TEXT, BAD_SETTING_INTERVALS_TEXT, INTERVALS, \
    SHOW_CURRENT_INTERVALS_TEXT, INTERVALS_TEXT, ADDING_NEW_WORD_TEXT, SET_INTERVALS_TEXT
from core.intervals_parser import IntervalsParser


class Bot:
    def __init__(self):
        self.bot = Application.builder() \
            .token(os.getenv("BOT_TOKEN")) \
            .build()
        self.bot.add_handler(CommandHandler('start', self.start))
        self.bot.add_handler(CommandHandler('add_new_word', self.add_new_word))
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
        word = try_create_from_args(context.args)
        if word is None:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=BAD_ADDING_NEW_WORD_TEXT)
            return
        WordsFileManager.save_word_to_file(update.effective_user.id, word.get_full_word())

        trigger = Trigger(context.user_data.get('intervals', INTERVALS))

        async def call_back(context: CallbackContext):
            await context.bot.send_message(chat_id=update.effective_chat.id, text=word.get_random_spoiler_word(),
                                           parse_mode=ParseMode.MARKDOWN_V2)

        context.job_queue.run_custom(callback=call_back, job_kwargs={'trigger': trigger})
        await context.bot.send_message(chat_id=update.effective_chat.id, text=ADDING_NEW_WORD_TEXT)

    @staticmethod
    async def get_all_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
        words = WordsFileManager.get_words_from_file(update.effective_user.id)
        if words is None:
            return
        for word in WordsFileManager.create_paginated_words(words):
            await context.bot.send_message(chat_id=update.effective_chat.id, text=word)

    @staticmethod
    async def get_all_words_as_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
        file_path = WordsFileManager.create_path_to_user_word_data(update.effective_user.id)
        await context.bot.send_document(chat_id=update.effective_chat.id, document=file_path)

    @staticmethod
    async def set_intervals(update: Update, context: ContextTypes.DEFAULT_TYPE):
        new_intervals = IntervalsParser.try_parse_intervals(context.args)
        if new_intervals is None:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=BAD_SETTING_INTERVALS_TEXT)
            return

        context.user_data['intervals'] = new_intervals
        context.user_data['intervals_text'] = ' '.join(context.args)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=SET_INTERVALS_TEXT)

    @staticmethod
    async def show_current_intervals(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=SHOW_CURRENT_INTERVALS_TEXT +
                                            context.user_data.get('intervals_text', INTERVALS_TEXT))

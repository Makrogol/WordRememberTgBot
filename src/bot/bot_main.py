import os

from telegram import Update
from telegram.ext import Application, ContextTypes, CommandHandler, CallbackContext

from src.bot.utils import default_repeat_word_message_command, default_single_message_command, \
    default_file_message_command, default_multiple_message_command
from src.core.bot_view.views import add_new_word_view, get_all_words_view, get_all_words_as_file_view, \
    set_intervals_view, repeat_view, fix_word_by_number_view, statistics_by_words_view, help_view, \
    show_current_intervals_view, statistics_view, start_view
from src.core.command.commands import Commands
from src.core.file_manager.users_manager import get_root_users, get_all_user_identifier_datas
from src.core.statistics.statistics_command_decorator import statistics_command


class Bot:
    def __init__(self):
        self.bot = Application.builder() \
            .token(os.getenv('BOT_TOKEN')) \
            .build()
        self.bot.add_handler(CommandHandler(Commands.ADD_NEW_WORD_COMMAND, self.add_new_word))
        self.bot.add_handler(CommandHandler(Commands.ANW_COMMAND, self.add_new_word))
        self.bot.add_handler(CommandHandler(Commands.FIX_WORD_COMMAND, self.fix_word))
        self.bot.add_handler(CommandHandler(Commands.GET_ALL_WORDS_AS_FILE_COMMAND, self.get_all_words_as_file))
        self.bot.add_handler(CommandHandler(Commands.GET_ALL_WORDS_COMMAND, self.get_all_words))
        self.bot.add_handler(CommandHandler('get_users', self.get_users))
        self.bot.add_handler(CommandHandler(Commands.HELP_COMMAND, self.help))
        self.bot.add_handler(CommandHandler(Commands.REPEAT_COMMAND, self.repeat))
        self.bot.add_handler(CommandHandler(Commands.SET_INTERVALS_COMMAND, self.set_intervals))
        self.bot.add_handler(CommandHandler(Commands.SHOW_CURRENT_INTERVALS_COMMAND, self.show_current_intervals))
        self.bot.add_handler(CommandHandler(Commands.STATISTICS_COMMAND, self.statistics))
        self.bot.add_handler(CommandHandler(Commands.STATISTICS_BY_WORDS_COMMAND, self.statistics_by_words))
        self.bot.add_handler(CommandHandler(Commands.START_COMMAND, self.start))

    @staticmethod
    @statistics_command
    async def add_new_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await default_repeat_word_message_command(update, context, command_name='add_new_word',
                                                  command_view=add_new_word_view)

    @staticmethod
    @statistics_command
    async def fix_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await default_single_message_command(update, context, command_name='fix_word',
                                             command_view=fix_word_by_number_view)

    @staticmethod
    @statistics_command
    async def get_all_words_as_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await default_file_message_command(update, context, command_name='get_all_words_as_file',
                                           command_view=get_all_words_as_file_view)

    @staticmethod
    @statistics_command
    async def get_all_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await default_multiple_message_command(update, context, command_name='get_all_words',
                                               command_view=get_all_words_view)

    @staticmethod
    async def get_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
        root_users = get_root_users()
        if update.effective_user.id not in root_users:
            return

        try:
            user_identifier_datas = get_all_user_identifier_datas()
            # for el in user_identifier_datas:
            user_identifier_datas_to_out = [str(user_identifier_data) for user_identifier_data in
                                            user_identifier_datas]
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text='Список пользователей:\n' + '\n'.join(
                                               user_identifier_datas_to_out))
        except Exception as e:
            print(e)
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Ошибка\n' + str(e))

    @staticmethod
    @statistics_command
    async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await default_single_message_command(update, context, command_name='help', command_view=help_view)

    @staticmethod
    @statistics_command
    async def repeat(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await default_repeat_word_message_command(update, context, command_name='repeat', command_view=repeat_view)

    @staticmethod
    @statistics_command
    async def set_intervals(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await default_single_message_command(update, context, command_name='set_intervals',
                                             command_view=set_intervals_view)

    @staticmethod
    @statistics_command
    async def show_current_intervals(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await default_single_message_command(update, context, command_name='show_current_intervals',
                                             command_view=show_current_intervals_view)

    @staticmethod
    @statistics_command
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await default_single_message_command(update, context, command_name='start', command_view=start_view)

    @staticmethod
    @statistics_command
    async def statistics(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await default_single_message_command(update, context, command_name='statistics',
                                             command_view=statistics_view)

    @staticmethod
    @statistics_command
    async def statistics_by_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await default_multiple_message_command(update, context, command_name='statistics_by_words',
                                               command_view=statistics_by_words_view)

from types import FunctionType

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, CallbackContext

from src.core.bot_view.view_data import ViewData
from src.core.file_manager.tmp_file_manager import tmp_file_manager
from src.core.intervals.intervals import Intervals
from src.core.user.user_identifier_data import UserIdentifierData
from src.core.word.word import Word
from src.output.message.file_message import FileMessage
from src.output.message.message import Message, Messages
from src.output.message.message_with_data import MessageWithData
from src.output.message.text_message import TextMessage


def repeat_word(context: ContextTypes.DEFAULT_TYPE, chat_id: int, word: Word, intervals: Intervals):
    # TODO придумать как переделать на концепцию output
    async def callback(context: CallbackContext):
        await context.bot.send_message(chat_id=chat_id, text=word.get_random_spoiler_word(),
                                       parse_mode=ParseMode.MARKDOWN_V2)

    for interval in intervals.get_as_timedelta_accumulate_sum():
        context.job_queue.run_once(callback=callback, when=interval)


async def default_single_message_command(update: Update, context: ContextTypes.DEFAULT_TYPE, command_name: str,
                                         command_view: FunctionType) -> None:
    user_identifier_data = UserIdentifierData(update.effective_user.id, update.effective_user.name)
    view_data = ViewData(user_identifier_data, context.args)
    message: Message = command_view(view_data)

    assert (isinstance(message, TextMessage), f'Unsupported {message.__class__} in {command_name} command')
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message.text)


async def default_multiple_message_command(update: Update, context: ContextTypes.DEFAULT_TYPE, command_name: str,
                                           command_view: FunctionType) -> None:
    user_identifier_data = UserIdentifierData(update.effective_user.id, update.effective_user.name)
    view_data = ViewData(user_identifier_data, context.args)
    messages: Messages = command_view(view_data)

    for message in messages:
        assert (isinstance(message, TextMessage), f'Unsupported {message.__class__} in {command_name} command')
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message.text)


async def default_repeat_word_message_command(update: Update, context: ContextTypes.DEFAULT_TYPE, command_name: str,
                                              command_view: FunctionType) -> None:
    user_identifier_data = UserIdentifierData(update.effective_user.id, update.effective_user.name)
    view_data = ViewData(user_identifier_data, context.args)
    message: Message = command_view(view_data)

    # Здесь может быть только TextMessage или MessageWithData
    assert (isinstance(message, MessageWithData) or isinstance(message, TextMessage),
            f'Unsupported {message.__class__} in {command_name} command')
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message.text)

    if isinstance(message, MessageWithData):
        repeat_word(context, update.effective_chat.id, **message.data)


async def default_file_message_command(update: Update, context: ContextTypes.DEFAULT_TYPE, command_name: str,
                                       command_view: FunctionType) -> None:
    user_identifier_data = UserIdentifierData(update.effective_user.id, update.effective_user.name)
    view_data = ViewData(user_identifier_data, context.args)
    message: Message = command_view(view_data)

    assert (isinstance(message, TextMessage) or isinstance(message, FileMessage),
            f'Unsupported {message.__class__} in {command_name} command')

    if isinstance(message, TextMessage):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message.text)
    elif isinstance(message, FileMessage):
        await context.bot.send_document(chat_id=update.effective_chat.id, document=message.file_path,
                                        caption=message.text)

    tmp_file_manager.clear_tmp_directory()

import logging
from aiogram import Router
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.types import Message
import log_utils
import strings
from voice_utils import get_anecdote

log = logging.getLogger(name=__name__)
router = Router(name=__name__)


@router.message(Command("anec"))
async def handle_anecdote(message: Message) -> None:
    log.info(log_utils.format_message(message=message))
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_VOICE,
    )
    # TODO: Здесь обработка текста в звук
    voice = ""
    if voice:
        await message.answer(voice=voice)
    else:
        await message.answer(text=strings.CONTENT_ERROR)

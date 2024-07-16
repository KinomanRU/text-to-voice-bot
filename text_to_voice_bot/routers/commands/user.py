import logging
from aiogram import Router, F
from aiogram.enums import ChatAction
from aiogram.types import Message
from aiogram.types import FSInputFile
import log_utils
import strings
from voice_utils import convert

log = logging.getLogger(name=__name__)
router = Router(name=__name__)

text_filter = (
    (F.text.startswith("/") | F.text.startswith("!"))
    & (F.text.split()[0].len() == 3)
    & (F.text.split().len() > 1)
)
doc_filter = (
    (F.text.startswith("/") | F.text.startswith("!"))
    & (F.text.split()[0].len() == 3)
    & F.document
)


@router.message(text_filter)
async def echo_message(message: Message) -> None:
    print(message.text)
    log.info(log_utils.format_message(message=message))
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_VOICE,
    )
    voice_file: str = ""
    if message.text:
        try:
            voice_file = convert(message.text)
        except ValueError:
            await message.reply(text=strings.UNSUPPORTED_LANG)
    if voice_file:
        await message.reply_voice(voice=FSInputFile(voice_file))

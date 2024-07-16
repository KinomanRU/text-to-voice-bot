__all__ = ("convert",)

import logging
import log_utils
import string
import random
from gtts import gTTS
from langdetect import detect
from langdetect import LangDetectException
import garbage_utils

log = logging.getLogger(name=__name__)


def get_file_name() -> str:
    return (
        "downloads\\"
        + "".join(random.choices(string.ascii_letters + string.digits, k=10))
        + ".mp3"
    )


def get_voice(text: str, lang: str | None = None) -> gTTS:
    if not lang:
        try:
            lang = detect(text)
        except LangDetectException:
            lang = "ru"
    voice: gTTS = gTTS(
        text=text,
        lang=lang,
    )
    return voice


def convert(text: str, lang: str | None = None) -> str:
    voice: gTTS = get_voice(text=text, lang=lang)
    file_name: str = get_file_name()
    voice.save(file_name)
    return file_name


def main() -> None:
    garbage_utils.remove_voices()
    try:
        voice: gTTS = get_voice(input("Enter text: "))
        file_name: str = "downloads\\_test.mp3"
        voice.save(file_name)
    except Exception as err:
        log.exception(err)


if __name__ == "__main__":
    log_utils.init_logging()
    main()
    garbage_utils.remove_voices()

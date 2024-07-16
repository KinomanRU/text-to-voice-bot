import asyncio
import logging
import os
from datetime import datetime
from typing import Never
from aiogram import Bot, Dispatcher
import log_utils
import proxy_utils
from routers import router as main_router
from dotenv import load_dotenv
import garbage_utils

log = logging.getLogger(name=__name__)
load_dotenv()


async def main() -> Never:
    log_utils.init_logging()
    dp = Dispatcher()
    dp.include_router(main_router)
    bot = Bot(
        token=os.getenv("PY_BOT_TOKEN"),
        session=proxy_utils.SESSION,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    print(datetime.now(), "Bot started")
    garbage_utils.remove_voices()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info("Normal shutdown")
    except Exception as err:
        log.exception(str(err))
    finally:
        print(datetime.now(), "Bot stopped")
        garbage_utils.remove_voices()

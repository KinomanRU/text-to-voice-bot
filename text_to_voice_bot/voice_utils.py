__all__ = ("convert",)

import asyncio
import logging
import log_utils
import request_utils
import strings
import urls

log = logging.getLogger(name=__name__)


async def convert() -> str:
    return ""


async def main() -> None:
    log_utils.init_logging()
    await convert()


if __name__ == "__main__":
    asyncio.run(main())

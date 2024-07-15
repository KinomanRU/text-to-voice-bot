import os

from aiogram.client.session.aiohttp import AiohttpSession
from aiohttp import BasicAuth
from config import config
from typing import Final
from dotenv import load_dotenv

load_dotenv()

PROXY: Final[bool] = config.getboolean("Proxy", "Proxy")
PROXY_URL: Final[str] = config.get("Proxy", "Proxy_URL") if PROXY else None
AUTH: Final[BasicAuth] = (
    BasicAuth(
        login=os.getenv("PY_USER_NAME"),
        password=os.getenv("PY_USER_PASS"),
    )
    if PROXY
    else None
)
SESSION: Final[AiohttpSession] = (
    AiohttpSession(proxy=(PROXY_URL, AUTH)) if PROXY else None
)

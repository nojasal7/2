from aiogram import Bot
from aiogram import Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from app.config import settings

bot = Bot(
    token=settings.BOT_TOKEN,
    parse_mode=ParseMode.HTML,
)

storage = MemoryStorage()

dp = Dispatcher(storage=storage)

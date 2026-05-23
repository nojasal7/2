from fastapi import APIRouter
from fastapi import Request
from aiogram.types import Update

from app.bot.bot import bot
from app.bot.bot import dp

router = APIRouter()


@router.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()

    update = Update.model_validate(data)

    await dp.feed_update(bot, update)

    return {"ok": True}

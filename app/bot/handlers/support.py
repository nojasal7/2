from aiogram import Router
from aiogram.types import Message

from app.bot.bot import bot
from app.config import settings
from app.services.spam_service import is_rate_limited
from app.services.ticket_service import create_ticket
from app.services.ticket_service import get_or_create_user
from app.services.ticket_service import save_message

router = Router()


@router.message()
async def support_handler(message: Message):
    if await is_rate_limited(message.from_user.id):
        await message.answer("Слишком много сообщений.")
        return

    user = await get_or_create_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
    )

    ticket = await create_ticket(user.id)

    await save_message(
        ticket_id=ticket.id,
        sender="client",
        text=message.text or "[media]",
    )

    text = (
        f"🆕 Новый тикет #{ticket.id}\n\n"
        f"👤 @{message.from_user.username}\n"
        f"🆔 {message.from_user.id}\n\n"
        f"💬 {message.text}"
    )

    await bot.send_message(
        chat_id=settings.ADMIN_GROUP_ID,
        text=text,
    )

    await message.answer(
        "Сообщение отправлено оператору."
    )

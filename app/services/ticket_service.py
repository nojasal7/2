from sqlalchemy import select

from app.db.models import Message
from app.db.models import Ticket
from app.db.models import User
from app.db.session import AsyncSessionLocal


async def get_or_create_user(telegram_id: int, username: str | None):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )

        user = result.scalar_one_or_none()

        if user:
            return user

        user = User(
            telegram_id=telegram_id,
            username=username,
        )

        session.add(user)
        await session.commit()
        await session.refresh(user)

        return user


async def create_ticket(user_id: int):
    async with AsyncSessionLocal() as session:
        ticket = Ticket(user_id=user_id)

        session.add(ticket)
        await session.commit()
        await session.refresh(ticket)

        return ticket


async def save_message(ticket_id: int, sender: str, text: str):
    async with AsyncSessionLocal() as session:
        message = Message(
            ticket_id=ticket_id,
            sender=sender,
            text=text,
        )

        session.add(message)
        await session.commit()

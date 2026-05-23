from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.webhook import router
from app.bot.bot import bot
from app.bot.bot import dp
from app.bot.handlers.start import router as start_router
from app.bot.handlers.support import router as support_router
from app.config import settings
from app.db.base import Base
from app.db.session import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    dp.include_router(start_router)
    dp.include_router(support_router)

    await bot.set_webhook(settings.WEBHOOK_URL)

    yield

    await bot.delete_webhook()


app = FastAPI(lifespan=lifespan)

app.include_router(router)

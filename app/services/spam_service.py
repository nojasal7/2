import time

from redis.asyncio import Redis

from app.config import settings

redis = Redis.from_url(settings.REDIS_URL)


async def is_rate_limited(user_id: int) -> bool:
    key = f"spam:{user_id}"

    value = await redis.get(key)

    if value:
        return True

    await redis.set(key, int(time.time()), ex=2)

    return False

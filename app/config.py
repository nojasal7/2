from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    BOT_USERNAME: str
    WEBHOOK_URL: str
    DATABASE_URL: str
    REDIS_URL: str
    ADMIN_GROUP_ID: int

    class Config:
        env_file = ".env"


settings = Settings()

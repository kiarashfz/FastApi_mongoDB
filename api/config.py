from pydantic import BaseSettings


class Settings(BaseSettings):
    mongodb_url: str

    class Config:
        env_file = ".env"


settings = Settings()

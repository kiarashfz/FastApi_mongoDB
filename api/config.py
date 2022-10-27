from pydantic import BaseSettings


class Settings(BaseSettings):
    mongodb_url: str

    email_regex: str
    username_regex: str

    authjwt_secret_key: str
    authjwt_access_token_expires: int
    authjwt_refresh_token_expires: int
    authjwt_denylist_enabled: bool = True
    authjwt_denylist_token_checks: set = {"access", "refresh"}

    class Config:
        env_file = ".env"


settings = Settings()

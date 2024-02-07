from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    secret: str
    token_lifetime: int = 3600

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

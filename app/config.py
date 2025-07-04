from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    """
    Application settings class that loads configuration from environment variables.
    """
    OPENAI_API_KEY: str
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    """
    Function to retrieve application settings.

    Returns:
        dict: A dictionary containing application settings.
    """
    return Settings()  # type: ignore

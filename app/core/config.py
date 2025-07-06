import time

from pydantic import Field
from pydantic.functional_validators import model_validator
from pydantic_settings import BaseSettings
from pydantic_settings.main import SettingsConfigDict


class Settings(BaseSettings):
    """
    Configuration settings for the application, using Pydantic for validation.
    """

    name: str = Field(default="Backend", alias="APP_NAME")
    service_start_time: float = Field(default_factory=time.time, exclude=True)
    api_key: str = Field(default="", alias="API_KEY")
    api_client: str = Field(default="", alias="API_CLIENT")

    @model_validator(mode="after")
    def initialize_client(self) -> "Settings":
        # Initialize an API client once in the settings object as a singleton. using self.api_client = ...

        return self

    model_config = SettingsConfigDict(env_file=".env")


# Initialize the settings object globally
settings = Settings()

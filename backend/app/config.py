from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPENROUTER_API_KEY: str
    BASE_URL: str = "https://openrouter.ai/api/v1"
    MODEL: str = "nvidia/nemotron-3-ultra-550b-a55b:free"
    FALLBACK_MODELS: list[str]

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
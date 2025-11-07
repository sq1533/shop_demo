from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    FIREBASE_SERVICE_ACCOUNT_PATH: str

    class Config:
        env_file = ".env"

settings = Settings()
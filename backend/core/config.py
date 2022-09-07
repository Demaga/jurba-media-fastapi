from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_SERVER: str
    DB_NAME: str

    class Config:
        env_file = ".env"


settings = Settings()

from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME = str
    VERSION = float
    DEBUG = bool
    DATABASE_HOST: str


# class Settings:
#     APP_NAME = "Docker Bind Mount Demo!"
#     VERSION = "1.0.0"
#     DEBUG = True


# settings = Settings()

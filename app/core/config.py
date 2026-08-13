# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     APP_NAME = str
#     VERSION = float
#     DEBUG = bool
#     DATABASE_HOST: str


# # class Settings:
# #     APP_NAME = "Docker Bind Mount Demo!"
# #     VERSION = "1.0.0"
# #     DEBUG = True


# #settings = Settings()

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Task Manager API"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    DATABASE_HOST: str = "localhost"


settings = Settings()
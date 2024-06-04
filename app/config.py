from os import getenv
from dotenv import load_dotenv


load_dotenv()


class Settings:
    """ Project settings """   
    REDIS_HOST: str = getenv("REDIS_HOST")
    REDIS_PORT: int = getenv("REDIS_PORT")
    REDIS_PASSWORD: str = getenv("REDIS_PASSWORD")


settings = Settings()
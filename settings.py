import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import pydantic


class Config(pydantic.BaseModel):
    load_dotenv()
    user_name: str = os.getenv('USER_NAME')
    access_key: str = os.getenv('ACCESS_KEY')

    app: str = os.getenv('APP')
    remote_url: str = os.getenv('REMOTE_URL')
    timeout: float = 10.0


config = Config()

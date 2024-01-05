import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    APP_NAME = os.getenv("APP_NAME", "")
    APP_VERSION = os.getenv("APP_VERSION", "")

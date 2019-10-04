# -*- coding: utf-8 -*-
import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 500
    PROPAGATE_EXCEPTIONS = True


class Development(Config):
    DEBUG = True


class Testing(Config):
    DEBUG = True


class Production(Config):
    DEBUG = False


config = {
    'development': Development,
    'testing': Testing,
    'default': Production
}

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///chat.db'
    SQLALCHEMY_BINDS = {
        'flowise': 'sqlite:////home/adam_skandrani/.flowise/database.sqlite',
        'chat': 'sqlite:///chat.db'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_KEY = os.getenv('API_KEY')
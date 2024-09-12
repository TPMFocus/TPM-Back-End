import os
from dotenv import load_dotenv

load_dotenv()

# wsl_database_path : /home/adam_skandrani/.flowise/database.sqlite
# database_path = 'C:/Users/Adam Skandrani/.flowise/database.sqlite'


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///chat.db'
    SQLALCHEMY_BINDS = {
        'flowise': 'sqlite:///C:/Users/pc/.flowise/database.sqlite',
        'chat': 'sqlite:///chat.db'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_KEY = os.getenv('API_KEY')
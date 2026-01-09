import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DATABASE = 'database.db'
    DATAMUSE_API = 'https://api.datamuse.com/words'

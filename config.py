# config.py
class Config:
    DEBUG = True  # Set to False in production
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgre:Kriti8532@localhost/blogging_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

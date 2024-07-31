import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://thiago:root@localhost/agriculture')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

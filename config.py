import os
from sqlalchemy import URL

class Config:
    DB_USERNAME = os.getenv('DB_USERNAME', 'test')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '12345678')
    APP_HOST = os.getenv('APP_HOST', '127.0.0.1')
    APP_PORT = os.getenv('APP_PORT', '5000')
    SQLALCHEMY_DATABASE_URI = URL.create(
        'mysql+pymysql',
        username=os.getenv('DB_USERNAME', 'test'),
        password=os.getenv('DB_PASSWORD', '12345678'),
        host=os.getenv('DB_URL', 'localhost'),
        port=os.getenv('DB_PORT', '3306'),
        database=os.getenv('DB_NAME', 'database')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_URL = os.getenv('DB_URL', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '3306')
    DB_NAME = os.getenv('DB_NAME', 'database')

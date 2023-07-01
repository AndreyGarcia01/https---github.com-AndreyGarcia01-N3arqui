import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///urls.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
    REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
    CACHE_TTL = int(os.getenv('CACHE_TTL', 300))
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')

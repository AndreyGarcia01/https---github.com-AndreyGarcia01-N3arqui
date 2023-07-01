from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_HOST': app.config['REDIS_HOST'], 'CACHE_REDIS_PORT': app.config['REDIS_PORT']})

from app import routes, models

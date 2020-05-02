from flask import Flask
from redis import StrictRedis
import logging

#redis_store = StrictRedis.from_url("redis://redis:6379/0",decode_responses=True)

app = Flask(__name__)
#app.config['REDIS_URL'] = "redis://redis:6379/0"
#app.register_blueprint(sse,url_prefix='/stream')

#redis_store.init_app(app)

if __name__ != "__main__":
    #Starting gunicorn generates a logging object via getLogger("gunicorn.error") that we are accessing here directly.
    gunicorn_logger = logging.getLogger("gunicorn.error")
    #set the Flask 
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

from app import views
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
# from flask_static_compress import FlaskStaticCompress
from config import Config


app = Flask(__name__,static_folder=os.path.abspath('static'))

 





app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)

if not app.debug:

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

from app import routes, models, errors






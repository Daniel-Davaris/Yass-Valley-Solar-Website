





#everything bellow instead of top
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, \
    MAIL_PASSWORD
from flask_mail import Mail

# my imports
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__,static_folder=os.path.abspath('static')) # not quite

# app.config.from_object(Config) # old
app.config.from_object('config')
db = SQLAlchemy(app)
login = LoginManager()
login.init_app(app)
login.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))
mail = Mail(app)


migrate = Migrate(app, db) # not 
bootstrap = Bootstrap(app) # not


from app import routes, models, errors # not quite

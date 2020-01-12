
# here we import the file path

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# we also setup the configuration object  with all the environemnt variiables 
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('smtp.office365.com')
    MAIL_PORT = int(os.environ.get('587') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['danieldavaris@outlook.com.au']
    POSTS_PER_PAGE = 25
    POSTS_PER_PAGE2 = 1
    

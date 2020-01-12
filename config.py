
# # here we import the file path

import os
basedir = os.path.abspath(os.path.dirname(__file__))


OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]



MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'danieldavarispriv@gmail.com'
MAIL_PASSWORD = 'Anvil2689'


# administrator list
ADMINS = ['danieldavarispriv@gmail.com','danieldavarispriv@gmail.com']


SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
POSTS_PER_PAGE = 25
POSTS_PER_PAGE2 = 1

# we also setup the configuration object  with all the environemnt variiables 
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 25
    POSTS_PER_PAGE2 = 1
    # email server
    




POSTS_PER_PAGE = 25
POSTS_PER_PAGE2 = 1





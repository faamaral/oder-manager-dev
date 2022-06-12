import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, '.env.dev'))

secret = os.urandom(24)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or secret
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or secret
    FLASK_ADMIN_SWATCH = os.environ.get('FLASK_ADMIN_SWATCH') or 'Flatly'
    
class Development(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'expense-control.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Production(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
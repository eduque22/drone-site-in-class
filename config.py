import os 
from dotenv import load_dotenv

#gives access to the project in ANY os we find ourselves in
#also allows outisde files/folders to be added from base directory
basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, '.env'))


class Config():
    '''
        Set config variables for the flask app. Using Environment variables where available other create the config varaibales if not already exist
    '''

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('Flask_debug')

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess this, lol'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turn off database updates from sqlalchemy
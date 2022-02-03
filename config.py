import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    STATIC_IMAGE_CAPS_DIR = 'media/caps/'
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
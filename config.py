import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    IP_ADDRESS = os.environ.get('IP_ADDRESS') or '192.168.2.136'
    PORT = os.environ.get('PORT_CAPS_API') or '8000'

    STATIC_IMAGE_DIR = 'media/'
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
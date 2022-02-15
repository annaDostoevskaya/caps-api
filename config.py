import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    IP_ADDRESS = os.environ.get('IP_ADDRESS') or '192.168.2.136'
    PORT = os.environ.get('PORT_CAPS_API') or '8000'
    APPLICATION_URL = os.environ.get('APPLICATION_URL') or 'http://' + IP_ADDRESS + ':' + PORT

    STATIC_IMAGE_DIR = 'media/'
    API_VER = os.environ.get('CAPS_API_VER') or 'v1'

    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


    def base_url_generate(self, body=''):
        return self.APPLICATION_URL + body

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    IP_ADDRESS = os.environ.get('IP_ADDRESS') or '192.168.2.136'
    PORT = os.environ.get('PORT') or '8080'
    APPLICATION_URL = os.environ.get('APPLICATION_URL') or 'http://' + IP_ADDRESS + ':' + PORT

    IMAGE_DIR = os.environ.get('IMAGE_DIR') or 'media/'
    API_VER = os.environ.get('CAPS_API_VER') or 'v1'

    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    VKAPP_ID = os.environ.get('VKAPP_ID')
    VKAPP_SERCRET_KEY = os.environ.get('VKAPP_SECRET_KEY')
    VKREDIRECT_URL = os.environ.get('VKREDIRECT_AUTH_URL')

    def base_url_generate(self, body='/'):
        return self.APPLICATION_URL + body

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    IP_ADDRESS = os.environ.get('IP_ADDRESS') or '192.168.2.136'
    PORT = os.environ.get('PORT_CAPS_API') or '8000'

    DOMEN_L3 = os.environ.get('DOMEN_L3') or 'caps-api'
    HOST = os.environ.get('NAME_OF_HOSTING') or 'herokuapp.com'

    STATIC_IMAGE_DIR = 'media/'
    API_VER = os.environ.get('CAPS_API_VER') or 'v1'

    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    ## TODO(annad): Refactoring.
    ON_HOSTING = os.environ.get('WE_ARE_ON_HOSTING') or False
    if ON_HOSTING:
        ON_HOSTING = int(ON_HOSTING)

    APPLICATION_URL = ''
    if ON_HOSTING:
        APPLICATION_URL = 'https://' + DOMEN_L3 + '.' + HOST
    else:
        APPLICATION_URL = 'http://' + IP_ADDRESS + ':' + PORT

    def base_url_generate(self, body=''):
        return self.APPLICATION_URL + body

from os import getenv

from api import create_app


app = create_app(getenv('FLASK_ENV') or 'default')

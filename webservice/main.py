from os import getenv

from api import create_app
from api.models import db

app = create_app(getenv('FLASK_ENV') or 'default')


@app.shell_context_processor
def shell_context():
    return dict(
        app=app,
        db=db,
    )

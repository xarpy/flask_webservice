# -*- coding: utf-8 -*-

from api.models import db
from configs import config
from flask import Flask
from flask_migrate import Migrate


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    '''Added DB'''
    db.init_app(app)
    Migrate(app, db)

    return app

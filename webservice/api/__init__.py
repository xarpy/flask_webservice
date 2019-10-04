# -*- coding: utf-8 -*-

from configs import config
from flask import Flask


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    return app

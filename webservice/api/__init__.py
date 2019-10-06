# -*- coding: utf-8 -*-

from api.models import db
from configs import config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

from .resources import WeatherAnalisys, WeatherCity


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    '''Added Rest Configurations'''
    api = Api(app, default_mediatype='application/json')
    api.add_resource(WeatherAnalisys, '/analise')
    api.add_resource(WeatherCity, '/cidade')

    '''Added CORS'''
    CORS(app)

    '''Added DB'''
    db.init_app(app)
    Migrate(app, db)

    '''Added Documentation Swagger'''
    SWAGGER_URL = ''
    API_URL = '/static/swagger.json'

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "WEBSERVICE FLASK WEATHER"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app

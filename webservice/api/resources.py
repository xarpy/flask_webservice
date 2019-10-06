import requests

from configs import Config
from flask import request
from flask_restful import Resource

from .models import WeatherData
from .utils import format_date, get_analisys, register_data, send_reponse


class WeatherCity(Resource):
    def post(self, * args, **kwargs):
        try:
            request_id = request.args.get('id')

            url = f'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{request_id}/days/15?token={Config.TOKEN}'
            api_weather = requests.get(url)
            register_data(api_weather.json())
            return send_reponse(api_weather.json(), api_weather.status_code)

        except ValueError:
            return send_reponse({"message": "id is not number"}, 404)


class WeatherAnalisys(Resource):
    def post(self, * args, **kwargs):
        try:
            dt_inicial = request.args.get('data_inicial')
            dt_final = request.args.get('data_final')
            data = WeatherData.query.filter(
                WeatherData.date >= format_date(dt_inicial, default=False),
                WeatherData.date <= format_date(dt_final, default=False)
            )
            msg = get_analisys(data)
            return send_reponse(msg, 200)

        except ValueError:
            if format_date(dt_inicial, check=True) is False:
                return send_reponse(
                    {"message": "data_inicial is date in not format available"},
                    404)
            elif format_date(dt_final, check=True) is False:
                return send_reponse(
                    {"message": "data_final is date in not format available"},
                    404)

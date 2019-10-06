# -*- coding: utf-8 -*-
from datetime import datetime

from dateutil.parser import parse
from sqlalchemy import func

from flask import Response, json

from .models import WeatherData, db


def format_date(date, check=False, default=True):
    """
    Depending on the condition, you can return a formatted date string
    or validate if the string is a date.

    :param date: string, contains value for format to date or check if is date.
    :param check: bool, check if string or date.
    :param default: bool, default format is datetime in brazilian convention.
    """
    if check is False and default is True:
        return date.strftime("%d/%m/%Y")
    elif check is True:
        if parse(date, fuzzy=False):
            return True
        else:
            return False
    else:
        return parse(date)


def send_reponse(msg, code, headers=None):
    """
    Send a custom response, with the addition of customizable headers.

    :param msg: string, string contains value for date.
    :param code: integer, accept parameter status code for HTTP protocols.
    :param headers: tuple, If you want to send a specific header,
    you must create or send a tuple containing the header name,
    without the value of the value.
    It will always be None until value is passed.
    """
    send = Response(
        response=json.dumps(msg),
        status=code,
        mimetype='application/json'
    )
    if headers is not None:
        send.headers.add(headers[0], headers[1])
    return send


def register_data(json):
    """
    Its function is to persist the data by writing to our database.
    :param json: dict, Is the dictionary in json format, captured.
    """
    city = dict(
        name=json['name'],
        state=json['state'],
        country=json['country']
    )

    for data in json['data']:
        weather = WeatherData(
            name=city['name'],
            state=city['state'],
            country=city['country'],
            date=data['date'],
            rain_probability=data['rain']['probability'],
            rain_precipitation=data['rain']['precipitation'],
            temperature_min=data['temperature']['min'],
            temperature_max=data['temperature']['max']
        )
        db.session.add(weather)
        db.session.commit()


def get_analisys(data):
    """
    Its function return the analisys for max temperature and
    media to precipitation in cities, in format dictionary.
    :param data: object, It's an Sqlachemy objects.
    """
    info = []
    city = data.order_by(WeatherData.temperature_max.desc()).first()
    info.append(dict(
        name=city.name,
        state=city.state,
        country=city.country,
        max_temperature=city.temperature_max
    ))
    for x in data.group_by(
            WeatherData.name).having(
            func.avg(WeatherData.rain_precipitation)).all():
        info.append(
            dict(
                name=x.name,
                media_precipitation=x.rain_precipitation
            )
        )

    return info

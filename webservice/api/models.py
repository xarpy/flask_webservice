# -*- coding: utf-8 -*-
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class WeatherData(db.Model):
    __tablename__ = 'weather_data'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    state = db.Column(db.String(2), nullable=False)
    country = db.Column(db.String(2), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    rain_probability = db.Column(db.Integer, nullable=False)
    rain_precipitation = db.Column(db.Integer, nullable=False)
    temperature_min = db.Column(db.Integer, nullable=False)
    temperature_max = db.Column(db.Integer, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.date = self.convert_date(self.date)

    def __repr__(self):
        return f"<City: {self.name}>"

    def convert_date(self, date):
        year, month, day = date.split('-')
        return datetime(int(year), int(month), int(day))

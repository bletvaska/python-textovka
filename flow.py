#!/usr/bin/env python
from sys import stderr

import requests
from pydantic import BaseSettings, BaseModel

url = 'http://api.openweathermap.org/data/2.5/weather?units={}&q={}&appid={}'


class Measurement(BaseModel):
    timestamp: int
    temperature: float
    pressure: int
    humidity: int
    wind_speed: float
    wind_deg: int
    icon: str


class Settings(BaseSettings):
    appid: str
    query: str = 'kosice,sk'
    units: str = 'metric'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = 'flow_'


def get_settings() -> Settings:
    settings = Settings()
    return settings


def main():
    raw_data = scrape_data()
    entry = process_data(raw_data)
    export_data(entry)


def scrape_data() -> dict:
    # scrape data
    settings = get_settings()
    response = requests.get(url.format(settings.units, settings.query, settings.appid))

    # exit on error http status code
    if response.status_code != 200:
        print(f'Error: HTTP status code is {response.status_code}.',
              file=stderr)
        quit(1)

    # return data as dictionary
    return response.json()


def process_data(data: dict) -> Measurement:
    entry = Measurement(
        timestamp=data['dt'],
        temperature=data['main']['temp'],
        pressure=data['main']['pressure'],
        humidity=data['main']['humidity'],
        wind_speed=data['wind']['speed'],
        wind_deg=data['wind']['deg'],
        icon=data['weather'][0]['icon']
    )

    return entry


def export_data(entry: Measurement):
    pass


if __name__ == '__main__':
    main()
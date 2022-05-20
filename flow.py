#!/usr/bin/env python
from sys import stderr

import requests
from pydantic import BaseSettings

url = 'http://api.openweathermap.org/data/2.5/weather?units={}&q={}&appid={}'


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
    scrape_data()
    process_data()
    export_data()


def scrape_data():
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


def process_data():
    pass


def export_data():
    pass


if __name__ == '__main__':
    main()

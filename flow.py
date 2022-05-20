#!/usr/bin/env python
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


# pip install pydantic

def main():
    scrape_data()
    process_data()
    export_data()


def scrape_data():
    settings = get_settings()
    response = requests.get(url.format(settings.units, settings.query, settings.appid))
    print(response.status_code)


def process_data():
    pass


def export_data():
    pass


if __name__ == '__main__':
    main()

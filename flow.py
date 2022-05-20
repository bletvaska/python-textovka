#!/usr/bin/env python
from pathlib import Path
from sys import stderr

import dotenv
import requests
from pydantic import BaseSettings, BaseModel

url = 'http://api.openweathermap.org/data/2.5/weather'
proxies = {
    'http': 'http://localhost:3128',
    'https': 'https://localhost:3128'
}


class Measurement(BaseModel):
    timestamp: int
    temperature: float
    pressure: int
    humidity: int
    wind_speed: float
    wind_deg: int
    icon: str

    def csv(self, sep=','):
        return (
            f'{self.timestamp}{sep}'
            f'{self.temperature}{sep}'
            f'{self.pressure}{sep}'
            f'{self.humidity}{sep}'
            f'{self.wind_speed}{sep}'
            f'{self.wind_deg}{sep}'
            f'{self.icon}'
        )


class Settings(BaseSettings):
    appid: str
    query: str = 'kosice,sk'
    units: str = 'metric'
    csv_report: Path = 'report.csv'

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

    # prepare
    params = {
        'units': settings.units,
        'q': settings.query,
        'appid': settings.appid
    }

    with requests.get(url, params=params, proxies=proxies) as response:
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
    settings = get_settings()

    with open(settings.csv_report, 'a') as file:
        print(entry.csv(), file=file)


if __name__ == '__main__':
    main()

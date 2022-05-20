#!/usr/bin/env python
import requests

appid = '08f5d8fd385c443eeff6608c643e0bc5'
query = 'kosice,sk'
url = 'http://api.openweathermap.org/data/2.5/weather?units=metric&q={}&appid={}'


def main():
    scrape_data()
    process_data()
    export_data()


def scrape_data():
    response = requests.get(url.format(query, appid))
    print(response.status_code)


def process_data():
    pass


def export_data():
    pass


if __name__ == '__main__':
    main()

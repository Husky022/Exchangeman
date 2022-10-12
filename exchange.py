import requests
import json

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


def load_exchange():
    return json.loads(requests.get(URL).text)['Valute']


def get_exchange(valute_name):
    for exc in list(load_exchange().values()):
        if valute_name == exc['CharCode']:
            return exc
    return False

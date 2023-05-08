import requests
import json
from config import keys
class APIExtepsion(Exception):
    pass

class ValueConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if base == quote:
             raise APIExtepsion(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIExtepsion(f'Не удалось обработать валюту {quote}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIExtepsion(f'Не удалось обработать количество {amount}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIExtepsion(f'Не удалось обработать валюту {base}.')


        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = json.loads(r.content)[keys[quote]]

        return total_base*amount

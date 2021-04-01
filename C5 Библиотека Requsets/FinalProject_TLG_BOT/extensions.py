import json
import requests
from config import keys


"""Исключения"""
class APIException(Exception):
    pass

"""Класс конвертации"""
class MoneyConverter:
    @staticmethod
    def get_price(symbols, base, amount):
        if symbols == base:
            raise APIException(f"Нельзя перевести одинаковые валюты {symbols}")

        try:
            symbols_tiker = keys[symbols]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {symbols}")
        try:
            base_tiker = keys[base]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {base}")
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Не удалось обработать количесво {amount}")
        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={symbols_tiker}&symbols={base_tiker}')
        total_base = (json.loads(r.content)['rates'][keys[base]])
        return total_base


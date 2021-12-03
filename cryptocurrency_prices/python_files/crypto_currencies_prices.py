import requests
import json
from datetime import date


currency_symbol = {
    'USD': '$',
    'EUR': '€',
    'JPY': '¥',
    'GBP': '£'
}


actual_prices = {}
crypto_currencies_prices = {}
# ex: {
#   'BTC':{
#      'USD': [153, 156, 120, 178, 164],
#      'EUR': [140, 141, 108, 160, 148]
#   },
#   'ETH':{
#      'USD': [15, 15, 12, 18, 16],
#      'EUR': [14, 14, 11, 16, 15]
#   }
# }

all_cryptos = ['BTC', 'ETH', 'XRP', 'LTC', 'SHIB']
all_physical = ['USD', 'EUR', 'JPY', 'GBP']


def get_crypto_prices(crypto: str, physical_currency: str, limit: int = 364, one_value: bool = True) -> list:
    """Return the list of the last 2000 average values between the high and the low of a day

    Parameters
    ----------
    crypto : str
    physical_currency : str
    limit: int [optional]
    one_value: bool [optional]

    Returns
    -------
    list
    """
    url = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=' \
          f'{crypto}&tsym={physical_currency}&limit={limit}'

    # check if the crypto is the Shiba because this last was created less than a year ago
    if crypto == 'SHIB':
        nb_values = (date.today() - date(day=30, month=9, year=2021)).days
        url = url.replace('364', str(nb_values if nb_values < 364 else 364))

    answer = requests.get(url)
    tab_json = json.loads(answer.text)

    # return a list of float if we ask for the graph or a list of list of float if it's for the day info
    if one_value:
        return [round(day['high'] + day['low'] / 2, 6) for day in tab_json['Data']['Data']]

    return [[round(day['open'], 6), round(day['close'], 6), round(day['low'], 6), round(day['high'], 6)]
            for day in tab_json['Data']['Data']]


def get_actual_prices(crypto: str) -> dict:
    """Return the the dict of the actual price of [crypto] in USD, EUR, JPY, and GBP

    Parameters
    ----------
    crypto : str

    Returns
    -------
    dict
    """
    url = f'https://min-api.cryptocompare.com/data/price?fsym={crypto}&tsyms=BTC,ETH,XRP,LTC,SHIB,USD,EUR,JPY,GBP'
    answer = requests.get(url)
    tab_json = json.loads(answer.text)

    return tab_json


# generation of the values of the different cryptos in the different physical
for cryptocurrency in all_cryptos:

    crypto_currencies_prices[cryptocurrency] = {}

    for physical in all_physical:

        crypto_currencies_prices[cryptocurrency][physical] = get_crypto_prices(cryptocurrency, physical)

# generation of the actual values of the different currencies in all the different currencies
for currency in all_cryptos + all_physical:

    actual_prices[currency] = get_actual_prices(currency)

import requests
import ctypes

def exchange(from_currency, to_currency):
    data = requests.get(url.format(from_currency, to_currency)).json()
    return float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

libconvert = ctypes.CDLL('./libconvert.so')
libconvert.convert.argtypes = (ctypes.c_float, ctypes.c_float)
libconvert.convert.restype = (ctypes.c_float)

def convert(base, exchange):
    return libconvert.convert(base, exchange)

apiKey = 'X7NY3G5XB9OWU75B'
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey=' + apiKey

BTC = exchange('BTC', 'USD')
exchange_factor = exchange('USD', 'ARS')

print("Bitcoin to USD: " , BTC)
print("USD to ARS: " , exchange_factor)
print("EUR to USD: " , exchange('EUR', 'USD'))

print("Bitcoin to ARS: " , convert(BTC, exchange_factor))
print("Bitcoin to ARS: " , convert(BTC, exchange_factor))
print("Bitcoin to ARS: " , convert(BTC, exchange_factor))




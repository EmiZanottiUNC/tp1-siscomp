import requests 
import ctypes   

# Funcion que llama a la API para obtener el valor de cambio de cada moneda:
def exchange(from_currency, to_currency): 
    data = requests.get(url.format(from_currency, to_currency)).json()
    if 'Note' in data:
        print("Limite de llamadas a API alcanzado. Intente de nuevo en 1 minuto.")
        quit()
    return float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

# Funcion que utiliza la libreria externa para realizar la conversion:
def convert(base, exchange):
    return libconvert.convert(base, exchange)

apiKey = 'X7NY3G5XB9OWU75B'
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey=' + apiKey

try:
    libconvert = ctypes.CDLL('./libconvert.so') #Carga la libreria
except OSError:
    print("Libreria 'libconvert.so' no encontrada. Ejecuto 'make'?")
    quit()

libconvert.convert.argtypes = (ctypes.c_float, ctypes.c_float) #Carga los tipos de argumentos que recibe la funcion convert
libconvert.convert.restype = (ctypes.c_float)                  #Carga el tipo de retorno de la funcion convert

BTC = exchange('BTC', 'USD')
ETH = exchange('ETH', 'USD')
USDT = exchange('USDT', 'USD')
ARS = exchange('USD', 'ARS')
EUR = exchange('USD', 'EUR')

print("Bitcoin: | USD: ", BTC, " | ARS: ", convert(BTC, ARS), " | EUR: ", convert(BTC, EUR))
print("Ethereum: | USD: ", ETH, " | ARS: ", convert(ETH, ARS), " | EUR: ", convert(ETH, EUR))
print("USD Tether: | USD: ", USDT, " | ARS: ", convert(USDT, ARS), " | EUR: ", convert(USDT, EUR))
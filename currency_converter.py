import requests

def get_rates():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    return data['rates']

def convert(amount, from_currency, to_currency, rates ):
    if from_currency not in rates:
        print(f'{from_currency} not found!')
    elif to_currency not in rates:
        print(f'{to_currency} not found!')
    else:
        in_usd = amount / rates[from_currency]
        result = in_usd * rates[to_currency]
        print(f'{amount} {from_currency} = {result:.2f} {to_currency}')

rates = get_rates()
amount = float(input('Enter amount: '))
from_currency = input('Enter currency from (PHP, EUR, USD): ').upper()
to_currency = input('Enter currency to convert (PHP, JPY, USD): ').upper()
convert(amount, from_currency, to_currency, rates)

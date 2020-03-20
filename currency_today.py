'''
This is a very simple app where you can choose a currency base and a date
and receive an output with the rates of other currencies in relation to the base. 
'''
import requests
import json


base = input('Type the currency base: ')
date = input('Type the date of your interest(year-month-day): ')

url = f'https://api.exchangeratesapi.io/{date}?base={base}'
response = requests.get(url)
data = response.text
parsed = json.loads(data)
rates = parsed['rates']

print('=' * 8 + base + '=' * 8) # just for better display
for currency, rate in rates.items():
    print(f'{currency}: {rate}')

import requests
import json


base = input('Convert from: ')
to = input('Convert to: ')
amount = float(input('Amount: '))

url = f'https://api.exchangeratesapi.io/latest?base={base}'

resp = requests.get(url)
data = resp.text
parsed = json.loads(data)
rates = parsed['rates']

for currency, rate in rates.items():
    if currency == to:
        conversion = rate * amount
        print(f'1 {base} = {currency} {rate}')
        print(f'{round(amount, 2)} {base} = {round(conversion, 2)} {currency}')

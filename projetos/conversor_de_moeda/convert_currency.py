from requests import get

class ConvertCurrency:
    def __init__(self, api_key):
        self.url_base = "https://free.currconv.com"
        self.api_key = api_key
        self.currencies = self.get_currencies()
    def get_currencies(self):
        endpoint = f"/api/v7/currencies?apiKey={self.api_key}"
        url = self.url_base + endpoint
        data = get(url).json()['results']
        data = list(data.values())
        return data

    def show(self):
        for currency in self.currencies:
            name = currency.get('currencyName', '')
            _id = currency.get('id', '')
            symbol = currency.get('currencySymbol', '')
            print(f'{name} | {_id} | {symbol}')

    def transform_currency(self, initial_currency, amount, end_currency):
        endpoint = f'/api/v7/convert?q={initial_currency}_{end_currency}'
        parameters = ['&compact=ultra', f'&apiKey={self.api_key}']
        url = self.url_base + endpoint + ''.join([str(parameter) for parameter in parameters])
        data = get(url).json()
        if len(data) == 0:
            print('Moedas Inválidas!!')
            return
        try:
            amount = float(amount)
        except ValueError:
            print('Quantidade inválida')
            return

        rate = data[f'{initial_currency}_{end_currency}']
        new_value = round(rate * amount, 2)

        return f'{end_currency}: {new_value}'


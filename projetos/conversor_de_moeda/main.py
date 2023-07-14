from convert_currency import ConvertCurrency

api_key = '75a93ef9071673d199a9'
conv_curr = ConvertCurrency(api_key)

print(conv_curr.transform_currency('USD', 50, 'BRL'))

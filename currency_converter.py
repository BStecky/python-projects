from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "6a55b2804bf0f44ed89e"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']
    
    data = list(data.items())
    data.sort()

    return data

def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get('currencySymbol', '')
        print(f"{_id} - {name} - {symbol}")

def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    response = get(url)
    data = response.json()
    if len(data) == 0:
        print('Invalid currencies.')
        return
    rate = list(data.values())[0]
    print(f"{currency1} to {currency2} = {rate}")
    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return
    converted_amount = rate * amount
    print(f"{amount} of {currency1} is equal to {converted_amount} of {currency2}")
    return converted_amount

def main():
    currencies = get_currencies()
    print("This is a currency converter!")
    print("------------------------------------")
    print("List the different currencies : Press 1")
    print("Convert from one currency to another : Press 2")
    print("Get the exchange rate of two currencies : Press 3")
    print("------------------------------------" + "\n")

    while True:
        response = input("Enter a number to continue (q to quit): ").lower()
        if response == 'q':
            break
        elif response == '1':
            print_currencies(currencies)
        elif response == '2':
            currency1 = input("Enter your starting currency: ").upper()
            amount = input(f"Enter how much {currency1} you would like to convert: ")
            currency2 = input("Enter the currency you would like to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif response == '3':
            currency1 = input("Enter your starting currency: ").upper()
            currency2 = input("Enter the currency you would like to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Invalid command")

main()

# data = get_currencies()
# print_currencies(data)
# rate = exchange_rate("USD", "CAD")
# print(rate)
# convert("USD", "CAD", 100)

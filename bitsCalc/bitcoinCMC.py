# bitsCalc python program
# the valuation of satoshis using realtime data from the CMC API
# Goal: Enable effective and efficient sales of sats at premium
# it's a building step towards a bitcoin voucher platform

# [request] pip

import requests

print('Sats Valuation Calculator')

def get_bitcoin_price():
    # CoinMarketCap API key
    api_key = '2eba678d-350b-4d07-818c-780ba97bb137'
    
    # Make a request to the CoinMarketCap API
    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        bitcoin_price = data['data']['BTC']['quote']['USD']['price']
        return bitcoin_price
    else:
        print('Error occurred while fetching Bitcoin price.')
        return None


def calculate_sales_price(price, interest_rate):
    sales_price = price * (1 + (interest_rate / 100))
    return sales_price

# function call to get the Bitcoin price
bitcoin_price = get_bitcoin_price()

# interest
interest = 4

if bitcoin_price:
    sales_price = calculate_sales_price(bitcoin_price, interest)
    print(f"Current bitcoin price ${bitcoin_price:.2f}")
    print(f"Sale price at {interest}% interest ${sales_price:.2f}")

"""
    fetching bitcoin price from CMC
    Next: Valuation of sats 
    Later: thinking of a web socket and how it would help

"""
# Done by Ink.

"""
    bitcoin is the standard
    Everything else is noise
"""
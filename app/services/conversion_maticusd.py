import requests

def get_conversion_rate():
    url = "https://api.cryptowat.ch/markets/coinbase/maticusd/price"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price: float = data["result"]["price"]
        return price
    else:
        return None

def convert_to_usd(amount, conversion_rate):
    return amount * conversion_rate

def convert_to_matic(amount, conversion_rate):
    return amount / conversion_rate
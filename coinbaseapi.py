import requests

def get_all_cryptocurrencies():
    url = "https://api.pro.coinbase.com/currencies"
    response = requests.get(url)
    data = response.json()

    return [item['id'] for item in data]

def get_current_price(cryptocurrency):
    url = f"https://api.pro.coinbase.com/products/{cryptocurrency}-USDC/ticker"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('price')
    else:
        return None

def main():
    cryptocurrencies = get_all_cryptocurrencies()
    print(f"There are {len(cryptocurrencies)} cryptocurrencies. Their current prices are:")

    for cryptocurrency in cryptocurrencies:
        price = get_current_price(cryptocurrency)
        if price:
            print(f"{cryptocurrency}: Current price = {price}")
        else:
            print(f"No trading data available for {cryptocurrency}")

if __name__ == "__main__":
    main()

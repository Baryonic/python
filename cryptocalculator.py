import requests
import os

def get_price(crypto):
    response = requests.get(f"https://api.coinbase.com/v2/prices/{crypto}-USD/spot")
    price = float(response.json()["data"]["amount"])
    return price

def read_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.strip().split(',') for line in lines]

filename = "mycryptos.txt"
portfolio = read_from_file(filename)

total_value = 0
for crypto, amount in portfolio:
    try:
        amount = float(amount)
        current_price = get_price(crypto)
        value = current_price * amount
        total_value += value
        print(f"You have {amount} {crypto}, which is worth ${value:.2f}")
    except Exception as e:
        print(f"Could not fetch price for {crypto}. Error: {e}")

print(f"The total value of your portfolio is ${total_value:.2f}")

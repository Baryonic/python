import requests
import time
import os
from datetime import datetime

def get_price(crypto):
    response = requests.get(f"https://api.coinbase.com/v2/prices/{crypto}-USD/spot")
    price = float(response.json()["data"]["amount"])
    return price

def make_trade_decision(current_price, previous_price):
    percent_change = (current_price - previous_price) / previous_price * 100
    if percent_change >= .1:
        return '\033[0;31m' + f"sell{percent_change:.4f}%"+'\033[1;37m' + f"price diff"+'\033[0;31m' + f"{(current_price - previous_price):.4f}"
    elif percent_change <= -.1:
        return '\033[0;32m' + f"buy{percent_change:.4f}%"+'\033[1;37m' + f"price diff"+'\033[0;32m' + f"{(current_price - previous_price):.4f}"
    else:
        return '\033[0;33m' + f"HOLD{percent_change:.4f}%"+'\033[1;37m' + f"price diff"+'\033[0;33m' + f"{(current_price - previous_price):.4f}"

def save_to_file(filename, crypto, price):
    with open(filename, 'a') as f:
        f.write(f"{crypto},{price}\n")

def read_from_file(crypto, previous_file):
    files = os.listdir("datalogs")
    files.sort()
    for file in reversed(files):  # Start from the most recent file
        with open(f"datalogs/{file}", 'r') as f:
            for line in f.readlines():
                if line.startswith(crypto):
                    data = line.strip().split(',')
                    if file != previous_file:
                        timestamp_str = file[:-4]  # Remove the .txt extension
                        timestamp = datetime.strptime(timestamp_str, "%Y%m%d%H%M%S")
                        print(f"The previous file was created at: {timestamp}")
                    return float(data[1]), file
    return None, None

cryptos = ['BTC', 'ETH', 'SOL', 'DOT', 'ORCA', 'MATIC', 'SHIB', 'ONDO', 'ATOM', 'XTZ', 'API3', 'SUPER', 'SWFTC', 'NCT', 'MPL', 'AUCTION', 'DIA', 'CGLD', 'SUKU', 'BONK', 'RAI', 'ALEPH', 'VARA', 'LDO', 'CHZ', 'ARPA', 'RBN', 'AURORA', 'WBTC', 'GAL', 'QI', 'SHPING', 'XYO', 'IOTX', 'SYN', 'HOPR', 'GST', 'FOX', 'RARE', 'MEDIA', 'SPELL', 'SAND', 'ALGO', 'CLV', 'BIGTIME', 'EUROC', 'HNT', 'RNDR', 'ADA', 'ICP', 'ARB']

# Create datalogs directory if it doesn't exist
if not os.path.exists('datalogs'):
    os.makedirs('datalogs')

while True:  # This will make the program run forever
    # Create a new datalog file
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"datalogs/{timestamp}.txt"
    previous_file = None

    for crypto in cryptos:
        try:
            current_price = get_price(crypto)
            previous_price, previous_file = read_from_file(crypto, previous_file)
            if previous_price is None:
                print('\033[0;36m' + f"No previous data for {crypto}. Fetching current price...")
                previous_price = current_price
                save_to_file(filename, crypto, current_price)
            decision = make_trade_decision(current_price, previous_price)
            if previous_price-current_price>0:
                print('\033[1;37m' + f"{crypto}"+'\033[0;35m' +f" now: " + '\033[0;31m'+ f"${current_price}" '\033[0;35m' + f" before: " + '\033[0;96m'+ f"${previous_price}" + '\033[0;35m' + f" Decision: {decision}" + '\033[1;37m' + f"{crypto}")
            elif previous_price-current_price<0:
                print('\033[1;37m' + f"{crypto}"+'\033[0;35m' +f"now: " + '\033[0;32m'+ f"${current_price}" '\033[0;35m' + f" before: " + '\033[0;96m'+ f"${previous_price}" + '\033[0;35m' + f" Decision: {decision}" + '\033[1;37m' + f"{crypto}")
            elif previous_price-current_price==0:
                print('\033[1;37m' + f"{crypto}"+'\033[0;35m' +f"now: " + '\033[0;37m'+ f"${current_price}" '\033[0;35m' + f" before: " + '\033[0;96m'+ f"${previous_price}" + '\033[0;35m' + f" Decision: {decision}" + '\033[1;37m' + f"{crypto}")
            save_to_file(filename, crypto, current_price)
            time.sleep(.2)  # sleep for 2 seconds to avoid hitting rate limits
        except Exception as e:
            print(f"Could not fetch price for {crypto}. Error: {e} exit line 59")
            exit()
    print(f""+'\033[4;36m'+'\033[40m'+'\033[4;36m'+'\033[1;30m')
    print('\033[0;37m' + f"end of loop, datalog file with name '{timestamp}'.txt created,sleeping for (10min)")
    time.sleep(600)

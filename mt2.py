import requests
import time
import os
from datetime import datetime
import sys

st = .1
print(f""+'\033[0;42m'+'\033[30m')
print(f"""keyday electronics software®             //     
runnin {sys.argv[0]}...         d011ar//      
    _______stfu n take my m8n3y  $     // $     
  =  ₿   ₿  `hold mon3y...        $   //        
 |           | stake m0n3y...       $//$$       
 |   =___=   |      invest mon3y... //   $      
  -________=|trade mOn3y...     $  //   $       
  m0n3y...     m8n3y... usd      dollars        
updating money in cryptohistory  /please wait...\033[0;36m\033[0;37m
{__file__}
PORTFOLIO   BTC          Time             """)
def gp(crypto):
    try:
        res = requests.get(f"https://api.coinbase.com/v2/prices/{crypto}-USD/spot", timeout=5)
        price = float(res.json()["data"]["amount"])
    except (KeyError, requests.exceptions.RequestException):
        price = None
    return price

def rp(fn):
    with open(fn, 'r') as f:
        lines = f.readlines()
    pf = []
    for line in lines:
        data = line.strip().split(',')
        if len(data) == 2: 
            crypto, amount_str = data
            if '+' in amount_str:
                amounts = amount_str.split('+')
                amount = sum(float(a) for a in amounts)
            else:
                amount = float(amount_str)
            pf.append((crypto, amount))
    return pf

def last_value(fn):
    with open(fn, 'r') as f:
        lines = f.readlines()
    if lines:
        last_line = lines[-1]
        last_value = float(last_line.split(": ")[1].strip().replace('$', ''))  # replace() added here
        return last_value
    else:
        return None

cr = ['BTC', 'ETH', 'SOL','EUR', 'DOT', 'ORCA', 'MATIC', 'SHIB', 'ONDO', 'ATOM', 'XTZ', 'API3', 'SUPER', 'SWFTC', 'NCT', 'MPL', 'AUCTION', 'DIA', 'CGLD', 'SUKU', 'BONK', 'RAI', 'ALEPH', 'VARA', 'LDO', 'CHZ', 'ARPA', 'RBN', 'AURORA', 'WBTC', 'GAL', 'QI', 'SHPING', 'XYO', 'IOTX', 'SYN', 'HOPR', 'GST', 'FOX', 'RARE', 'MEDIA', 'SPELL', 'SAND', 'ALGO', 'CLV', 'BIGTIME', 'EUROC', 'HNT', 'RNDR', 'ADA', 'ICP', 'ARB']

if not os.path.exists('moneylogs'):
    os.makedirs('moneylogs')

if not os.path.exists('cryptohistory'):
    os.makedirs('cryptohistory')

for crypto in cr:
    fn1 = f"cryptohistory/{crypto}.txt"
    if not os.path.exists(fn1):
        open(fn1, 'w').close()

fn = f"moneylogs/moneylog.txt"

while True:
    ts = datetime.now().strftime("%Y%m%d%H%M%S")
    v0 = 0
    pf = rp("mycryptos.txt")
    lv = last_value(fn)
    unfetched_coins = []

    for crypto, amount in pf:
        try:
            amount = float(amount)
            cp = gp(crypto)
            if cp is None:
                unfetched_coins.append(crypto)
                try:
                    with open(f"cryptohistory/{crypto}.txt", 'r') as f:
                        lines = f.readlines()
                    if lines:
                        last_line = lines[-1]
                        cp = float(last_line.split(",")[0])
                    else:
                        cp = 0
                except FileNotFoundError:
                    cp = 0
            else:
                with open(f"cryptohistory/{crypto}.txt", 'a') as f:
                    f.write(f"{cp},{ts}\n")
            v = cp * amount
            v0 += v
        except Exception as e:
            print(f"Unexpected error for {crypto}: {e}")

    if unfetched_coins:
        print(f"Could not fetch prices for the following coins: {', '.join(unfetched_coins)}. Will use the last known prices.")

    with open(fn, 'a') as f:
        f.write(f"Time{ts}: ${v0}\n")

    if lv is None or v0 == lv:
        print('\033[0;36m' + f"${round(v0, 3)}"+ '\033[0;33m' + f"    ${gp('BTC')}" +'\033[0;37m' + f"    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    elif v0 > lv:
        print('\033[0;32m' + f"${round(v0, 3)}"+ '\033[0;33m' + f"    ${gp('BTC')}" +'\033[0;37m' + f"    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print('\033[0;31m' + f"${round(v0, 3)}"+ '\033[0;33m' + f"    ${gp('BTC')}" +'\033[0;37m' + f"    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    time.sleep(st*5)

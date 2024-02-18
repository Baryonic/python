import csv
import operator
import requests
from datetime import datetime, timedelta
import sys

print(f"""\033[46m\033[30mkeyday electronics software®             //     
runnin {sys.argv[0]}...            d011ar//      
    _______stfu n take my m8n3y  $     // $     
  =  ₿   ₿  `hold mon3y...        $   //        
 |           | stake m0n3y...       $//$$       
 |   =___=   |      invest mon3y... //   $      
  -________=|trade mOn3y...     $  //   $       
  m0n3y...     m8n3y... usd      dollars        
connecting to coinbase api       /please wait...\033[0;36m\033[0;37m
{__file__}\033[4;36m
using data in portfolio.csv to calculate money
calculating optimal sell price too (wait 60 sec)""")

import csv
import operator
import requests
from datetime import datetime, timedelta
import sys

def gpd(c):
    r = requests.get(f'https://api.coinbase.com/v2/prices/{c}-USD/spot')
    p = r.json()['data']['amount']
    return float(p)

def gpu(c):
    r = requests.get(f'https://api.coinbase.com/v2/prices/{c}-USDC/spot')
    p = r.json()['data']['amount']
    return float(p)

def calculate_total_portfolio():
    total = 0
    for c in pf:
        total += pf[c]
    return total

pf = {}
bp = {}
bq = {}

oma = datetime.now() - timedelta(days=30)

with open('portfolio.csv', 'r') as f:
    r = csv.DictReader(f)
    for row in r:
        td = datetime.strptime(row['Timestamp'], '%Y-%m-%dT%H:%M:%SZ')
        if td < oma:
            continue
        c = row['Asset'].lower()
        a = float(row['Quantity Transacted'])
        tt = row['Transaction Type']
        if tt == 'Advanced Trade Buy':
            pf[c] = pf.get(c, 0) + a
            ts = a * float(row['Spot Price at Transaction'])
            bp[c] = bp.get(c, 0) + ts
            bq[c] = bq.get(c, 0) + a
        elif tt == 'Advanced Trade Sell':
            pf[c] = pf.get(c, 0) - a

for c in pf:
    pf[c] *= gpd(c)
    if c in bp and bq[c] > 0:
        bp[c] /= bq[c]

sp = sorted(pf.items(), key=operator.itemgetter(1), reverse=True)

print("Available cryptocurrencies to trade with:")
for c, _ in sp:
    print(c)

while True:
    c = input("Enter the cryptocurrency for which you want to see the operation data (or 'terminate' to stop): ").lower()
    if c == 'terminate':
        break
    elif c == 'portfolio':
        total = calculate_total_portfolio()
        print(f'Total portfolio value: {total} dollars')
    elif c in pf:
        v = pf[c]
        mbp = bp.get(c, 'N/A')
        msp = mbp / 0.96 if mbp != 'N/A' else 'N/A'
        uv = gpu(c) * pf[c]
        print(f'{c}: {v} dollars, mean buying price: {mbp} dollars, minimum sell price for 4% profit: {msp} dollars, amount owned: {pf[c]}, worth in USDC: {uv}')
    else:
        print("Invalid cryptocurrency. Please try again.")

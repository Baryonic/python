import socket
hostname = socket.gethostname()
ipaddress = socket.gethostbyname(hostname)
print(f'your ip adress according to import socket is : {ipaddress}')



import requests
import json

# IP address to test
#ip_address = '147.229.2.90'
ip_address = f'{ipaddress}'

# URL to send the request to
request_url = 'https://geolocation-db.com/jsonp/' + ip_address
# Send request and decode the result
response = requests.get(request_url)
result = response.content.decode()
# Clean the returned string so it just contains the dictionary data for the IP address
result = result.split("(")[1].strip(")")
# Convert this data into a dictionary
result  = json.loads(result)
print(result)

#import requests

response = requests.get(f"https://geolocation-db.com/json/{ipaddress}&position=true").json()

print(f'______________________{response}')



import sys
import json
#import requests
import csv

#import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data

def get_location2():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ipaddress}/json/').json()
    location_data = {
        "ip": ipaddress,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data

print('<3<3<3<3<3<3')
print(f'your ip adress according to import socket is : {ipaddress}')
print(get_location())
print(get_location2())

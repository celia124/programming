import requests

respone = requests.get("http://api.open-notify.org/astro.json")

for astronaut in respone.json()['people']:
    print(astronaut['name'])
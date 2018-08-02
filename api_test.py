import requests
import pprint

base_url = "http://data.fixer.io/api/convert"
access_key = "eb260d72e994d898a299e6e40ebe9246"
base = "HKD"
symbols = "USD,AUD,CAD,PLN,MXN"

url = base_url+"?access_key="+access_key
print(url)

req = requests.get(url)

pprint.pprint(req)
pprint.pprint(req.json())
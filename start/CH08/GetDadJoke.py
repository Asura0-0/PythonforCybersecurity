# Created Aahan 2/21/24

import requests
import json

url = "https://icanhazdadjoke.com/api"

payload = {}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# Created Aahan 2/21/24

import requests

def get_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    joke = data['joke']
    return joke


joke = get_joke()
print("Here's a dad joke for you:")
print(joke)

import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + 'videos/1', {"likes": 10,"name": 'How to train a dragon', "views":100} )
print(response.json())
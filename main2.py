import requests

x = 0 
y = 0

URL = "http://placekitten.com/" + str(x) + "/" + str(y) 
CURL = "https://catfact.ninja/fact?max_length=140"


res = requests.get(CURL)
res = res.json()

print(res)

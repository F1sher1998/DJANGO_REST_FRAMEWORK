import requests


endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/"

get_response = requests.get(endpoint, json={"query":"Hello World"}) #API
print(get_response.text) #raw ext response
print(get_response.json())
print(get_response.status_code)

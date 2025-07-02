import requests


endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint) #API
print(get_response.text) #raw ext response
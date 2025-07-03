import requests

endpoint = "http://localhost:8000/api/products/196849648948964896489486486946484984634/"

get_response = requests.get(endpoint, json={"title": "Hello world"})
print(get_response.json())
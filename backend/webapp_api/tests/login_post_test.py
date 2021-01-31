import requests

url = "http://127.0.0.1:8000/api/v1/custom/login/"

payload={"username":"zrmeier12","password":"AbCD363801!"}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
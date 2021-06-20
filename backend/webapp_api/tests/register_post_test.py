import requests

url = "http://127.0.0.1:8000/api/v1/custom/register/"

payload={
    "username":"zrmeier12",
    "email":"zmeier12@gmail.com",
    "password1":"AbCD363801!",
    "password2":"AbCD363801!",
    "first_name":"Zap",
    "last_name":"Branigain",
    
    }
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
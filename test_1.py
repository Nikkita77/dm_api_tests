"""
curl -X 'POST' \
  'http://5.63.153.31:5051/v1/account' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "login": "string",
  "email": "string",
  "password": "string"
}'
"""
import pprint

import requests

url = "http://5.63.153.31:5051/v1/account"
headers = {
    "accept": "*/*",
    "Content-Type": "application/json"
}

json = {
    "login": "nikita_testddfwegqdq1",
    "email": "nikita_testfwffqff1@mail.ru",
    "password": "123456756wfwqfq"
}

response = requests.post(
    url=url,
    headers=headers,
    json=json
)
print(response.status_code)
# pprint.pprint(response.json())

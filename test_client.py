import requests

url = 'http://127.0.0.1:5000/webhook'
data = {
    "queryResult": {
        "queryText": "병원 위치를 알고 싶어요"
    }
}

response = requests.post(url, json=data)
print(response.json())

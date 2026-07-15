import requests

response = requests.get(
    "http://api.weatherapi.com/v1/current.json",
    {
        "key": "assad",
        "q": "Dhaka"
    }
)

data = response.json()
print(data)